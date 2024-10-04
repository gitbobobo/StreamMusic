# SMTC 适配

做音乐播放器，绕不开的就是要把当前播放的媒体告知操作系统。在 Android、iOS 及 macOS 平台，[audio_service](https://github.com/ryanheise/audio_service) 插件都能很好的完成任务。

在 Windows 系统上，SMTC(SystemMediaTransportControls, 系统媒体传输控件) 负责显示媒体内容并提供控制按钮。

此前音流一直使用 [smtc_windows](https://pub.dev/packages/smtc_windows) 这个插件来完成这个任务，但使用这个插件对我来说有两个痛点：

- 无法使用本地图片（插件作者是 spotube 的作者，软件中大部分资源都是在线获取的，所以可能未来也不会加入此功能）
- 构建产物在 x86 的机器上运行就会报错（导致我只能在 arm 架构的 Windows 系统打包）。

所以一直以来就想通过 [flutter_rust_bridge](https://cjycode.com/flutter_rust_bridge/quickstart) 这个插件自己实现一下，奈何自己不懂 Rust，实在不知道该怎么从一个空白文件开始写起。

还好最近在掘金上看到一个大佬写的文章：[Flutter 应用如何支持 SMTC](https://juejin.cn/post/7363556508603432972)，遂下定决心改造当前项目。

## 启用 Melos

[Melos](https://invertase.docs.page/melos) 用于管理多个包在一个存储库的协同工作，对我来说，以下两个特点是吸引我使用它的原因：

- Executing simultaneous commands across packages.（跨包执行同时命令。）
- Listing of local packages & their dependencies.（本地包及其依赖项的列表。）

:::tip

启用 Melos 这个步骤对于 **SMTC 适配**来说并非必须的，只是我个人的选择。

如果只想了解如何适配 SMTC，直接阅读原文章 [Flutter 应用如何支持 SMTC](https://juejin.cn/post/7363556508603432972) 是更好的选择。

:::

在命令行使用 `dart pub global activate melos` 命令全局激活一下，按照[官方文档指引](https://invertase.docs.page/melos/getting-started)创建对应的文件与文件夹结构。

```
my_project
├── apps
│   ├── apps_1
│   └── apps_2
├── packages
│   ├── package_1
│   └── package_2
├── melos.yaml
├── pubspec.yaml
└── README.md
```

对于 `melos.yaml`，我提供一个目前我所使用的示例文件，仅供参考：

```yaml title="melos.yaml"
name: stream_music

packages:
  - apps/**/
  - packages/**/

ignore:
  - '**/.dart_tool/**'
  - '**/.idea/**'
  - '**/.vscode/**'
  - '**/build/**'
  - '**/example'

scripts:
  gen:frb:
    run: |
      melos exec -c 6 --fail-fast -- \
        "flutter_rust_bridge_codegen generate"
    description: |
      Generate dart files for FlutterRustBridge.
    packageFilters:
      scope: 'stream_music'

  build:windows:
    run: |
      melos exec -c 6 --fail-fast -- \
        "flutter build windows"
    description: |
      Build app for Windows.
    packageFilters:
      dirExists:
        - windows
      scope: 'stream_music'

  build:msix:
    run: |
      melos exec -c 6 --fail-fast -- \
        "dart run msix:publish"
    description: |
      Build app for Windows msix.
    packageFilters:
      dirExists:
        - windows
      scope: 'stream_music'

  build:ios:
    run: |
      melos exec -c 6 --fail-fast -- \
        "flutter build ios --config-only"
    description: |
      更新 iOS 应用配置.
    packageFilters:
      dirExists:
        - ios
      scope: 'stream_music'

  clean:
    run: |
      melos exec -c 6 --fail-fast -- \
        "flutter clean"
    description: |
      Clean all packages.
    packageFilters:
      scope: 'stream_music'
```

## 迁移项目

在 Rust 安装完成后，执行命令 `cargo install flutter_rust_bridge_codegen` 以安装 flutter_rust_bridge 的脚手架工具。

尽管 flutter_rust_bridge 提供了迁移已有项目的命令：`flutter_rust_bridge_codegen integrate`，但似乎在我的项目中并不好用。

因此我直接使用 `flutter_rust_bridge_codegen create my_app` 命令创建一个新的项目，然后一点点比较新旧项目的不同，最后也算是完成了迁移。

迁移完成后，使用 `melos bs` 命令引导一下项目，这个命令会安装所有包依赖项，并将所有本地包链接在一起，而且在 `melos.yaml` 中定义的脚本命令也会直接出现在 Android Studio 的运行配置中。

![](https://oss.aqzscn.cn/resource/blog/img/2024/2877c-551314d6ad5cb4871c61dd880b232e37.png)

## 适配 SMTC

这个步骤大部分参考大佬的 [Flutter 应用如何支持 SMTC](https://juejin.cn/post/7363556508603432972)，再次表示感谢～

添加 Rust 依赖：

```toml title="rust/Cargo.toml"
[dependencies]
flutter_rust_bridge = "=2.3.0"
windows = { version = "0.58.0", features = [
    "Media_Playback",
    "Storage",
    "Storage_Streams",
    "Storage_FileProperties"
]}
```

添加 `smtc` 模块

```rust title="rust/src/api/mod.rs"
pub mod smtc;

```

补充 `smtc` 逻辑，这里的代码与原文的有些许不同，主要目的是为了能在不同平台编译通过，且尽量不修改 dart 的调用代码。

```rust title="rust/src/api/smtc.rs"
use flutter_rust_bridge::frb;
#[cfg(target_os = "windows")]
use windows::{
    core::HSTRING,
    Foundation::TypedEventHandler,
    Media::{
        MediaPlaybackStatus, MediaPlaybackType, Playback::MediaPlayer,
        SystemMediaTransportControls, SystemMediaTransportControlsButton,
        SystemMediaTransportControlsButtonPressedEventArgs,
    },
    Storage::{FileProperties::ThumbnailMode, StorageFile, Streams::RandomAccessStreamReference},
};

use crate::frb_generated::StreamSink;

pub struct SmtcFlutter {
    #[cfg(target_os = "windows")]
    _smtc: SystemMediaTransportControls,
    #[cfg(target_os = "windows")]
    _player: MediaPlayer,
}

pub enum SMTCControlEvent {
    Play,
    Pause,
    Previous,
    Next,
    Unknown,
}

pub enum SMTCState {
    Paused,
    Playing,
}

/// Apis for Flutter
impl SmtcFlutter {
    #[frb(sync)]
    pub fn new() -> Self {
        #[cfg(target_os = "windows")]
        return Self::_new().unwrap();
        #[cfg(not(target_os = "windows"))]
        return SmtcFlutter {};
    }

    pub fn subscribe_to_control_events(&self, sink: StreamSink<SMTCControlEvent>) {
        #[cfg(target_os = "windows")]
        self._smtc
            .ButtonPressed(&TypedEventHandler::<
                SystemMediaTransportControls,
                SystemMediaTransportControlsButtonPressedEventArgs,
            >::new(move |_, event| {
                let event = event.as_ref().unwrap().Button().unwrap();
                let event = match event {
                    SystemMediaTransportControlsButton::Play => SMTCControlEvent::Play,
                    SystemMediaTransportControlsButton::Pause => SMTCControlEvent::Pause,
                    SystemMediaTransportControlsButton::Next => SMTCControlEvent::Next,
                    SystemMediaTransportControlsButton::Previous => SMTCControlEvent::Previous,
                    _ => SMTCControlEvent::Unknown,
                };
                sink.add(event).unwrap();

                Ok(())
            }))
            .unwrap();
    }

    pub fn update_state(&self, state: SMTCState) {
        #[cfg(target_os = "windows")]
        self._update_state(state).unwrap();
    }

    pub fn update_display(&self, title: String, artist: String, album: String, path: Option<String>) {
        #[cfg(target_os = "windows")]
        self._update_display(
            HSTRING::from(title),
            HSTRING::from(artist),
            HSTRING::from(album),
            path.map(HSTRING::from),
        )
        .unwrap();
    }

    pub fn close(self) {
        #[cfg(target_os = "windows")]
        self._player.Close().unwrap();
    }
}

#[cfg(target_os = "windows")]
impl SmtcFlutter {
    fn _init_controls(smtc: &SystemMediaTransportControls) -> Result<(), windows::core::Error> {
        // 下一首
        smtc.SetIsNextEnabled(true)?;
        // 暂停
        smtc.SetIsPauseEnabled(true)?;
        // 播放（恢复）
        smtc.SetIsPlayEnabled(true)?;
        // 上一首
        smtc.SetIsPreviousEnabled(true)?;

        Ok(())
    }

    fn _new() -> Result<Self, windows::core::Error> {
        let _player = MediaPlayer::new()?;
        _player.CommandManager()?.SetIsEnabled(false)?;

        let _smtc = _player.SystemMediaTransportControls()?;
        Self::_init_controls(&_smtc)?;

        Ok(Self { _smtc, _player })
    }

    fn _update_state(&self, state: SMTCState) -> Result<(), windows::core::Error> {
        let state = match state {
            SMTCState::Playing => MediaPlaybackStatus::Playing,
            SMTCState::Paused => MediaPlaybackStatus::Paused,
        };
        self._smtc.SetPlaybackStatus(state)?;

        Ok(())
    }

    fn _update_display(
        &self,
        title: HSTRING,
        artist: HSTRING,
        album: HSTRING,
        path: Option<HSTRING>,
    ) -> Result<(), windows::core::Error> {
        let updater = self._smtc.DisplayUpdater()?;
        updater.SetType(MediaPlaybackType::Music)?;

        let music_properties = updater.MusicProperties()?;
        music_properties.SetTitle(&title)?;
        music_properties.SetArtist(&artist)?;
        music_properties.SetAlbumTitle(&album)?;

        if let Some(path) = path {
            let file = StorageFile::GetFileFromPathAsync(&path)?.get()?;
            let thumbnail = file
                .GetThumbnailAsyncOverloadDefaultSizeDefaultOptions(ThumbnailMode::MusicView)?
                .get()?;
            updater.SetThumbnail(&RandomAccessStreamReference::CreateFromStream(&thumbnail)?)?;
        }

        updater.Update()?;

        if !(self._smtc.IsEnabled()?) {
            self._smtc.SetIsEnabled(true)?;
        }

        Ok(())
    }
}
```

执行命令 `flutter_rust_bridge_codegen generate` 生成 dart 端代码，根据自己的业务逻辑进行调用即可。

```dart title="audio_handler.dart"
SmtcFlutter? _smtc;

if (Platform.isWindows) {
    _smtc = SmtcFlutter();
    // 监听点击事件
    _smtc?.subscribeToControlEvents().listen((event) {
        switch (event) {
            case SMTCControlEvent.play:
                play();
                break;
            case SMTCControlEvent.pause:
                pause();
                break;
            case SMTCControlEvent.previous:
                skipToPrevious();
                break;
            case SMTCControlEvent.next:
                skipToNext();
                break;
            case SMTCControlEvent.unknown:
                break;
        }
    });
}

// 更新媒体信息
_smtc?.updateDisplay(
    title: event?.title ?? '',
    artist: event?.artist ?? '',
    album: event?.album ?? '',
    path: event?.artUri?.toString(),
);

// 更新播放状态
_smtc?.updateState(state: event ? SMTCState.playing : SMTCState.paused);
```
