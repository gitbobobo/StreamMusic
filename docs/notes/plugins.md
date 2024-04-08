---
sidebar_position: 1
---

# 插件分享

如果没有开源项目的支持，就不会有现在的音流～

## 界面

### macos_ui

macos_ui 与 Flutter 自带的 Material Widgets 和 Cupertino Widgets 一样，都是为了实现在对应平台设计语言的组件库。

[点此查看](https://macosui.github.io/macos_ui/#/)在线演示。

![](https://oss.aqzscn.cn/resource/blog/img/2024/84187-8f40569512f26dedc256e709c73a4de9.png)

### fluent_ui

fluent_ui 是用于实现 Windows 平台 fluent 设计语言的组件库，这里面的组件相较于 `macos_ui` 里的组件功能更加完善。

[点此查看](https://bdlukaa.github.io/fluent_ui/)在线演示。

![](https://oss.aqzscn.cn/resource/blog/img/2024/65e8d-fc810c37b1bd57ddc5161705e21c8343.png)

### pulldown_button

[pulldown_button](https://github.com/notDmDrl/pull_down_button) 实现了类似 iOS 下拉菜单的效果，动画效果十分丝滑，如果能支持二级菜单就更完美了。

![](https://oss.aqzscn.cn/resource/blog/img/2024/faae1-9ad0cf3582cd7ff590b3e02645f19bc7.png)

## 平台相关

### macos_window_utils

macos_window_utils 是 `macos_ui` 作者的另一作品，主要功能是控制窗口的各种属性，如是否模糊、是否隐藏标题栏等，配合 macos_ui 食用更佳。

### flutter_acrylic

flutter_acrylic 可以在 macOS、Windows、Linux 平台实现窗口模糊/透明效果，其中 macOS 依赖了 `macos_window_utils` 插件，因此如果使用此插件就无需再引入 `macos_window_utils` 了。