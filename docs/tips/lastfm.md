---
sidebar_position: 4
---

# 通过 Last.FM 记录播放记录 {#lastfm}

年末的时候看到别人在发**听歌年度报告**而自己却没有？不用担心，你可以通过 Last.FM 记录你的播放记录，然后就可以在年末的时候愉快地向朋友分享了～

![](https://oss2.aqzscn.cn/resource/blog/img/2024/8e26c-0835da59547fd34cc652db034d977f09.png)

由于音流非开源软件，如果直接接入 Last.FM 可能会有侵权风险，所以下面的教程将以服务端配置为例。

:::info

我已经向 Last.FM 发送邮件请求接入，但很遗憾并未得到回复。

:::

## 注册 Last.FM 账号 {#account}

前往 https://www.last.fm/ 注册即可，**使用 QQ 邮箱可能会导致无法注册**。

## 通过 Navidrome 上报播放记录 {#navidrome}

在 Navidrome 的网页端启用 Last.FM 的喜好记录即可。

![](https://oss2.aqzscn.cn/resource/blog/img/2024/b269c-862548c7f7e351f285de76a02c0b8389.png)

## 通过 Emby 上报播放记录 {#emby}

在 Emby 的管理页面中，安装元数据分类的 Last.fm 插件后重启服务器，即可在侧边栏进行配置。

![](https://oss2.aqzscn.cn/resource/blog/img/2024/58760-e43cba8065b629dfcf3285068d40d7eb.png)

## 通过 Plex 上报播放记录 {#plex}

在 Plex 中配置 Last.fm 授权之后即可上报播放记录，可通过此链接抵达：https://plex.tv/users/other-services