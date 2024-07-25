---
sidebar_position: 5
---

# CarPlay

## 歌词显示

苹果出于安全考量，是不允许在 CarPlay 中显示歌词的。

因此音流能做的就是只显示单行歌词，此功能需要开启「歌词 - 歌词通知」开关。

## 使用限制

在当前版本，必须在手机上打开音流才能使用 CarPlay。

在 App 未打开时，flutter 引擎尚未初始化，此时无法接收到 CarPlay 已连接的消息，也就无法处理 CarPlay 有关的逻辑了。

:::info

相关问题：[CarPlay app required Flutter App open first?](https://github.com/oguzhnatly/flutter_carplay/issues/12)

尝试了这个帖子中的做法，可以实现不打开 app 显示 CarPlay 界面，但无法播放音乐，手动进入应用后界面会卡住不动。

等之后再研究研究。

:::