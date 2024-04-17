---
sidebar_position: 6
---

# 常见问题

如果软件使用过程中遇到问题或有任何建议，请在 [github](https://github.com/gitbobobo/StreamMusic) 上创建 issue。

## 音乐服务

### 无法登录

可能原因：

- 账号密码输错
- 主机地址输错（需包含协议、地址和端口号）
- 使用了自签名的证书（暂时不打算支持）

### Navidrome 只能获取 50500 首歌曲

Navidrome 按添加时间倒序查询歌曲的接口有问题，在查询数量在 50000 首附近时会报错。若您的曲库数量较大，请关闭设置中的 **增量更新** 来同步全部歌曲。

## 平台相关

### 安卓通知栏播放控制失效

这似乎是安卓系统的 bug，目前的解决方案是：在系统设置中关闭音流的电池优化。

:::info

关联问题：[安卓手机通知栏控制失效](https://github.com/gitbobobo/StreamMusic/issues/145)

1.2.8 之后会在帮助页面检测电池优化是否已经关闭，点击可跳转到对应的系统设置。

:::

### 安卓车载蓝牙歌曲信息不更新或更新有延迟

这似乎发生在安卓手机锁屏之后，目前暂未发现解决办法，具体处理进度参见问题 [Android MediaItem is not updating on car display through bluetooth](https://github.com/ryanheise/audio_service/issues/908)。

### 安卓开启桌面歌词后 Bitwarden 应用内无响应

这应该是 Bitwarden 的安全机制导致的，因为识别到了悬浮窗。

:::info

相关问题：[Android Bitwarden App - controls not working](https://www.reddit.com/r/Bitwarden/comments/x0jmbr/android_bitwarden_app_controls_not_working/)

:::

### 应用发烫或CPU占用过高

这个属于 Flutter 的优化问题，在界面中存在循环动画时，CPU 占用就会异常的高。

在主题设置中有个省电模式的开关，默认是开启的，一般不要关闭，不过也可尝试一下自己的手机是否能 Hold 住哈哈。

:::info

相关问题：[CPU占用有点高，手机发烫](https://github.com/gitbobobo/StreamMusic/issues/60)

:::

### App 未打开时无法使用 CarPlay

在 App 未打开时，flutter 引擎尚未初始化，此时无法接收到 CarPlay 已连接的消息，也就无法处理 CarPlay 有关的逻辑了。

:::info

相关问题：[CarPlay app required Flutter App open first?](https://github.com/oguzhnatly/flutter_carplay/issues/12)

尝试了这个帖子中的做法，可以实现不打开 app 显示 CarPlay 界面，但无法播放音乐，手动进入应用后界面会卡住不动。

等之后再研究研究。

:::

## 其他问题

### 安全问题

部分用户可能担心软件会私自传输他们的服务器账号密码，我觉得这种担心是没有必要的。原因如下：

- 音流不是公司开发的，拿到这些数据对我个人来讲毫无意义。NAS 音乐是个小众需求，用户量大不起来，数据过少就没有商业价值。
- 玩 NAS 的或多或少都懂点技术，若我插入恶意代码，被发现的概率很大，我为什么放着持续的收益不要，冒着丢掉自己名声的风险去拿这些数据呢？

看了这些若你还是不放心，可以专门建一个只能访问音乐服务的账号使用。

若你觉得地址暴露了也有危险，那就没办法了，请选择你信任的软件使用吧。
