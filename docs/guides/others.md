---
sidebar_position: 5
---

# 其他

## 分区

部分用户不止用音流聆听音乐，还会用音流收听有声书，而媒体库的分区功能可以很好的区分不同类型的音频，避免干扰到我们想要聆听的内容。

目前仅 Emby、Jellyfin 和 Plex 支持添加多个媒体库（分区）。

您在添加有声书类型的媒体库时：

- 对于 Emby ，可以将媒体库类型设置为有声读物或音乐。
- 对于 Jellyfin 和 Plex，只能将媒体库类型设置为音乐，因为 Jellyfin 的书籍类型包含对文本类型书籍的支持，数据的展示方式和音乐是截然不同的。

## 列表元素

绿色序号表示您从未听过这首歌，这在听有声书时会比较有用。

![](https://oss.aqzscn.cn/resource/blog/img/2024/90011-293fd6ac80a1ce9bc85adf176c807e19.png)

在某个专辑的歌曲列表中，序号指的是音轨号，而右上角的数字表示碟号。

![](https://oss.aqzscn.cn/resource/blog/img/2024/90642-5882f5ffcf3b92988a49aaa5dac913c3.png)

歌手列表右侧的扳手图标表示此歌手名下存在重复文件。

![](https://oss.aqzscn.cn/resource/blog/img/2024/7ec2a-423ad72f94ace289a7d801936d02e3f6.png)

## 设备间同步配置信息

您可能会在多个设备安装音流，每次安装后都要输入一遍甚至更多遍服务器信息，想必是非常痛苦的。

因此音流提供了扫码同步配置信息的功能，显示二维码的设备会开启一个 HTTP 服务，您可以使用局域网中安装了音流的设备扫码同步数据，若设备是桌面设备，亦可在侧边栏搜索框中输入二维码底部的网址以同步数据。

二维码页面的入口位于「添加资料库」和「帮助 - 数据同步」中。

:::caution

1. 扫码同步功能涉及到的数据仅会在局域网中传输，音流仅对数据做了最基础的加密，因此请尽量在安全的局域网环境中使用，避免泄露您的账号信息。
2. 扫码识别二维码使用了 [mobile_scanner](https://github.com/juliansteenbakker/mobile_scanner) 插件，可能有部分识别不到的情况，可尝试返回重进更换一个新的二维码。

:::

## 歌词

目前只支持 LRC 格式的歌词，详细可参考 [维基百科](https://zh.wikipedia.org/wiki/LRC%E6%A0%BC%E5%BC%8F)。

对于双语歌词，目前支持以下两种格式：

**相同时间轴**

```
[00:01.123] 歌词
[00:01.123] 翻译
```

**以【】包裹**

```
[00:01.123] 歌词【翻译】
```