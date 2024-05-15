---
sidebar_position: 6
---

# 常见问题

如果软件使用过程中遇到问题或有任何建议，请在 Github 上找到 [此仓库](https://github.com/gitbobobo/StreamMusic)：

1. 进入 issues 标签页，使用搜索功能查找有无相同问题。
2. 若没有找到，请新建问题，并**提供尽可能详尽的信息**，如系统版本，服务端版本，音流版本，日志，截图等信息，**提供的信息越全面，越有可能帮助我复现问题，以便更快找到原因并解决**。

:::note 日志查看方式

反馈建议页面，不要选择类型，连续点击通过邮件发送 3 次，点击右上角图标即可查看最新日志。

关于页面，连续点击版本号可进入开发者模式，目前开发者模式下可调整日志等级。

:::

## 音乐服务

### 无法登录

可能原因：

- 账号密码输错
- 主机地址输错（需包含协议、地址和端口号）
- 使用了自签名的证书（暂时不打算支持）
- 使用了代理软件，代理软件把 127.0.0.1 拦截了

### Navidrome 扫描到 50000 首歌曲后失败

在 Navidrome 0.52 及之前版本，按添加时间查询歌曲的逻辑有些问题，请升级到最新版本以解决此问题。

若您的 Navidrome 无法升级，可尝试将 Docker 的环境变量 `ND_DEVOFFSETOPTIMIZE` 设置为大于您曲库数量的数字。

:::info 

关联问题：[The retrieval of data fails when sorting by createAt after the number of songs exceeds 50,000.](https://github.com/navidrome/navidrome/issues/3006)

:::

## 播放

### 安卓后台播放自动暂停（没有声音）

请在后台管理中允许音流后台运行，然后重新启动音流。

若依旧有此问题，请检查手机设置中是否有类似「允许后台流量」的选项。

### 播放时总时长一直在更新

这表示当前歌曲正在服务端转码，播放器无法得知歌曲真实的总时长，因此会显示当前已获取的音频内容的总时长。

等待歌曲转码完成即可，这是正常现象。

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

### CarPlay 或通知中心无法控制上一曲下一曲

请在设置中关闭 `与其他应用同时播放` 的选项。

这是 iOS 的系统特性，非软件 bug。

### App 未打开时无法使用 CarPlay

在 App 未打开时，flutter 引擎尚未初始化，此时无法接收到 CarPlay 已连接的消息，也就无法处理 CarPlay 有关的逻辑了。

:::info

相关问题：[CarPlay app required Flutter App open first?](https://github.com/oguzhnatly/flutter_carplay/issues/12)

尝试了这个帖子中的做法，可以实现不打开 app 显示 CarPlay 界面，但无法播放音乐，手动进入应用后界面会卡住不动。

等之后再研究研究。

:::

## 会员

### 恢复购买时提示签名信息错误

大概率是你的设备时间和正常时间相差太大导致的。

### 设备数量

目前新设备上线会自动将超出设备数量的旧设备踢下线，因此无需手动管理上线的设备。

## 其他问题

### 安全问题

部分用户可能担心软件会私自传输他们的服务器账号密码，我觉得这种担心是没有必要的。原因如下：

- 音流不是公司开发的，拿到这些数据对我个人来讲毫无意义。NAS 音乐是个小众需求，用户量大不起来，数据过少就没有商业价值。
- 玩 NAS 的或多或少都懂点技术，若我插入恶意代码，被发现的概率很大，我为什么放着持续的收益不要，冒着丢掉自己名声的风险去拿这些数据呢？

看了这些若你还是不放心，可以专门建一个只能访问音乐服务的账号使用。

若你觉得地址暴露了也有危险，那就没办法了，请选择你信任的软件使用吧。
