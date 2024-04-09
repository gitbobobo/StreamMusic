---
sidebar_position: 99
---

# 最新版本

更新于：2024-04-09

:::tip 护甲+1

import DayCounter from '@site/src/components/DayCounter';

音流发布至今已有 <DayCounter dateStr="2023-06-06"/> 天了，共更新了 27 个版本，还是个很年轻的播放器呢～

因个人开发经验与精力所限，且要兼顾多个平台与音乐服务，更新速度与 bug 解决速度难免要慢一些，望诸君见谅。

但我始终相信：下个版本会更好！

:::

## V1.2.7（2024-04-08）

更新内容：

- 支持[专辑/歌手收藏功能](https://github.com/gitbobobo/StreamMusic/issues/155)，增加对应的筛选功能
- 删除自动切换离线模式的逻辑
- 调整部分界面的弹出菜单样式
- 降低联网验证会员身份的概率
- 支持多艺术家【[#116](https://github.com/gitbobobo/StreamMusic/issues/116), [#96](https://github.com/gitbobobo/StreamMusic/issues/96)】
- 自定义 API 封面接口支持单独配置获取专辑还是歌手（取消请求歌曲封面，[统一改为获取专辑封面](https://github.com/gitbobobo/StreamMusic/issues/209)）
- [提升歌词解析的兼容性](https://github.com/gitbobobo/StreamMusic/issues/190)
- 支持[连接至 Plex](https://github.com/gitbobobo/StreamMusic/issues/43)，暂未适配转码播放，请注意流量消耗（下个版本适配）
- Audio Station 喜欢功能调整为获取五星评分的歌曲
- Emby 禁止直接创建歌单，可选中歌曲后在添加到歌单的弹框中创建新歌单
- 修复[Subsonic 封面图片混乱的问题](https://github.com/gitbobobo/StreamMusic/issues/189)
- [桌面端点击控制栏可显示播放控制按钮](https://github.com/gitbobobo/StreamMusic/issues/182)，用于适配触屏操作
- Windows 改为单进程应用

安卓版下载地址：

- [app-arm64-v8a-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.7/app-arm64-v8a-release.apk)
- [app-armeabi-v7a-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.7/app-armeabi-v7a-release.apk)
- [app-x86_64-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.7/app-x86_64-release.apk)
- [app-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.7/app-release.apk)

Mac 下载地址：[音流v1.2.7.dmg](https://oss.aqzscn.cn/stream-music/versions/1.2.7/音流v1.2.7.dmg)

Windows 版下载地址：[stream_music_1.2.7.1.msix](https://oss.aqzscn.cn/stream-music/versions/1.2.7/stream_music_1.2.7.1.msix)

## V1.2.6（2024-03-15）

更新内容：

- AudioStation/Navidrome/Subsonic 新增歌曲评分功能
- Emby 现在只会显示存在音频的播放列表（此外，无需开启在主页显示播放列表视图也能获取播放列表了）
- 优化检查更新逻辑
- 优化[登录时自动补充端口号的逻辑](https://github.com/gitbobobo/StreamMusic/issues/172)
- 允许[应用系统字体缩放（仅缩小）](https://github.com/gitbobobo/StreamMusic/issues/169)
- 修复[在输入框中按空格键触发快捷键响应的问题](https://github.com/gitbobobo/StreamMusic/issues/175)
- 修复[播放队列最后一首歌重放的问题](https://github.com/gitbobobo/StreamMusic/issues/157)
- 【安卓】桌面歌词增加[双行显示的选项](https://github.com/gitbobobo/StreamMusic/issues/61)
- 【Mac/Windows】适配桌面端窗口外观

安卓版下载地址：

- [app-arm64-v8a-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.6/app-arm64-v8a-release.apk)
- [app-armeabi-v7a-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.6/app-armeabi-v7a-release.apk)
- [app-x86_64-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.6/app-x86_64-release.apk)
- [app-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.6/app-release.apk)

Mac 下载地址：[音流v1.2.6.dmg](https://oss.aqzscn.cn/stream-music/versions/1.2.6/音流v1.2.6.dmg)

Windows 版下载地址：[stream_music_1.2.6.1.msix](https://oss.aqzscn.cn/stream-music/versions/1.2.6/stream_music_1.2.6.1.msix)

## V1.2.5（2024-03-03）

更新内容：

- 默认主题支持自定义背景
- 登录时若未填写端口号则自动补充默认 HTTP 端口号
- 修复[音乐自动回到开头的问题](https://github.com/gitbobobo/StreamMusic/issues/157)
- 暂时禁用系统字体缩放功能
- 【iOS】初步[支持 CarPlay](https://github.com/gitbobobo/StreamMusic/issues/68)
- 【Mac/Windows】更换为沉浸式窗口标题栏
- 【Mac/Windows】支持最小化到托盘/ Dock 栏
- 【Windows】[修复音乐缓存不生效的问题](https://github.com/gitbobobo/StreamMusic/issues/161)

安卓版下载地址：

- [app-arm64-v8a-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.5/app-arm64-v8a-release.apk)
- [app-armeabi-v7a-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.5/app-armeabi-v7a-release.apk)
- [app-x86_64-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.5/app-x86_64-release.apk)
- [app-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.5/app-release.apk)

Mac 下载地址：[音流v1.2.5.dmg](https://oss.aqzscn.cn/stream-music/versions/1.2.5/音流v1.2.5.dmg)

Windows 版下载地址：[stream_music_1.2.5.0.msix](https://oss.aqzscn.cn/stream-music/versions/1.2.5/stream_music_1.2.5.0.msix)

> Windows 更新此版本可能导致窗口全屏点不到关闭按钮，若遇到此问题，请删除`用户目录/AppData/Roaming/cn.aqzscn`目录（应用数据所在目录）后重新打开。

## V1.2.4（2024-02-13）

更新内容：

- 新增重复歌曲检测功能（歌手详情页面）
- 歌曲转码时可以切换应用或锁屏了
- 自定义 API 新增歌曲详情接口
- 现可通过翻译接口翻译歌词（需手动操作）
- 现可识别同一行的中英文歌词并分离（需手动操作）
- 【iOS】修复更新应用导致已下载音乐丢失的问题

安卓版下载地址：

- [app-arm64-v8a-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.4/app-arm64-v8a-release.apk)
- [app-armeabi-v7a-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.4/app-armeabi-v7a-release.apk)
- [app-x86_64-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.4/app-x86_64-release.apk)
- [app-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.4/app-release.apk)

Mac 下载地址：[音流v1.2.4.dmg](https://oss.aqzscn.cn/stream-music/versions/1.2.4/音流v1.2.4.dmg)

Windows 版下载地址：[stream_music_1.2.4.0.msix](https://oss.aqzscn.cn/stream-music/versions/1.2.4/stream_music_1.2.4.0.msix)

## V1.2.3（2024-01-30）

更新内容：

- 修复歌曲切换后信息未更新的问题
- 【安卓】写入文件前先询问存储权限

安卓版下载地址：

- [app-arm64-v8a-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.3/app-arm64-v8a-release.apk)
- [app-armeabi-v7a-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.3/app-armeabi-v7a-release.apk)
- [app-x86_64-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.3/app-x86_64-release.apk)
- [app-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.3/app-release.apk)

Mac 下载地址：[音流v1.2.3.dmg](https://oss.aqzscn.cn/stream-music/versions/1.2.3/音流v1.2.3.dmg)

Windows 版下载地址：[stream_music_1.2.3.1.msix](https://oss.aqzscn.cn/stream-music/versions/1.2.3/stream_music_1.2.3.1.msix)

## V1.2.2（2024-01-27）

更新内容：

- 支持调节应用内音量
- 歌单导入导出功能（m3u 格式，iOS 暂不支持）
- 支持 Emby 歌词接口
- 适配 Navidrome 0.51（需重新同步数据）
- 【Windows】支持媒体通知
- 全平台支持蓝牙歌词（原锁屏歌词）
- 修复了一些问题

> 感觉叫蓝牙歌词也不太合适，不知道你有没有更简单明了的叫法。

安卓版下载地址：

- [app-arm64-v8a-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.2/app-arm64-v8a-release.apk)
- [app-armeabi-v7a-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.2/app-armeabi-v7a-release.apk)
- [app-x86_64-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.2/app-x86_64-release.apk)
- [app-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.2/app-release.apk)

Mac 下载地址：[音流v1.2.2.dmg](https://oss.aqzscn.cn/stream-music/versions/1.2.2/音流v1.2.2.dmg)

Windows 版下载地址：[stream_music_1.2.2.2.msix](https://oss.aqzscn.cn/stream-music/versions/1.2.2/stream_music_1.2.2.2.msix)

## V1.2.1（2024-01-14）

更新内容：

- [支持专辑艺术家标签](https://github.com/gitbobobo/StreamMusic/issues/114)
- [自动同步方式改为增量同步](https://github.com/gitbobobo/StreamMusic/issues/100)
- [歌曲预缓存功能](https://github.com/gitbobobo/StreamMusic/issues/58)
- 调整移动网络下内网地址可达性的判断逻辑
- 从未播放过的歌曲前面的**序号**将以绿色表示
- [提升曲库中包含长音频（有声书）文件的使用体验](https://github.com/gitbobobo/StreamMusic/issues/21)
- 歌词字体增加**极大**的选项
- 【安卓】[修复返回键逻辑异常的问题](https://github.com/gitbobobo/StreamMusic/issues/112)
- 【桌面端】可恢复上次打开时的窗口大小

安卓版下载地址：

- [app-arm64-v8a-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.1/app-arm64-v8a-release.apk)
- [app-armeabi-v7a-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.1/app-armeabi-v7a-release.apk)
- [app-x86_64-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.1/app-x86_64-release.apk)
- [app-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.1/app-release.apk)

Mac 下载地址：[音流v1.2.1.dmg](https://oss.aqzscn.cn/stream-music/versions/1.2.1/音流v1.2.1.dmg)

Windows 版下载地址：[stream_music_1.2.1.2.msix](https://oss.aqzscn.cn/stream-music/versions/1.2.1/stream_music_1.2.1.2.msix)

## V1.2.0（2023-12-29）

更新内容：

- 【Android、MacOS、Windows】可选择文件下载位置
- 【Android】支持支付宝支付
- 首页最近播放和最常播放可选择显示专辑或歌曲（主题-主页）
- 首屏可选择推荐页或首页（主题-主页）
- 支持[歌词确认接口](https://aqzscn.cn/archives/stream-music-custom-api#%E7%A1%AE%E8%AE%A4%E6%AD%8C%E8%AF%8D)
- 歌词中的空行可选择是否显示（主题-歌词）
- 支持单独刷新歌单列表
- 歌曲列表支持本地搜索

安卓版下载地址：

- [app-arm64-v8a-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.0/app-arm64-v8a-release.apk)
- [app-armeabi-v7a-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.0/app-armeabi-v7a-release.apk)
- [app-x86_64-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.0/app-x86_64-release.apk)
- [app-release.apk](https://oss.aqzscn.cn/stream-music/versions/1.2.0/app-release.apk)

Mac 下载地址：[音流v1.2.0.dmg](https://oss.aqzscn.cn/stream-music/versions/1.2.0/音流v1.2.0.dmg)

Windows 版下载地址：[stream_music_1.2.0.0.msix](https://oss.aqzscn.cn/stream-music/versions/1.2.0/stream_music_1.2.0.0.msix)

windows 版安装方法详见 [Windows 版音流安装教程](https://aqzscn.cn/archives/stream-music-win)

