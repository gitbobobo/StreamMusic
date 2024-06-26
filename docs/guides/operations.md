---
sidebar_position: 2
---

# 操作指引

音流的某些操作逻辑和主流的音乐 APP 有所不同，或较难发现，特在此说明。

## 播放模式

音流默认是队列播放，如需循环播放，可打开此开关，对队列播放和随机播放都会生效。

![](https://oss.aqzscn.cn//resource/blog/img/2023/860419a28223c06c03964ff34a5a8668.png)

从歌曲列表中选择歌曲播放，默认是队列播放。

![](https://oss.aqzscn.cn//resource/blog/img/2023/e3f0f7469a58b3955598f8965eeef658.png)

若列表头部有上面的按钮，则可点击有圆圈的按钮定位到当前歌曲，点击两个箭头的按钮切换列表的播放模式。

**从歌曲列表切换播放模式会保存到配置中，不同的歌曲列表类型会分别存储用户偏好的播放模式。**

反之，从播放列表或播放页面切换播放模式则是临时操作，仅当次生效。

## 播放控制

![](https://oss.aqzscn.cn//resource/blog/img/2023/15d11e29bb8e27f58378743eb86f6fd0.png)

音流的控制栏如上图所示，可通过点击封面播放/暂停，点击歌词区域进入播放页，点击右侧按钮弹出正在播放列表。

从歌词区域向右滑动切换上一曲，向左滑动切换下一曲。

## 列表元素

绿色序号表示您从未听过这首歌，这在听有声书时会比较有用。

![](https://oss.aqzscn.cn/resource/blog/img/2024/90011-293fd6ac80a1ce9bc85adf176c807e19.png)

:::tip

歌曲在播放到 1/4 位置时会向服务器发送滚动播放记录的请求（AudioStation 不支持此接口）。

:::

在某个专辑的歌曲列表中，序号指的是音轨号，而右上角的数字表示碟号。

![](https://oss.aqzscn.cn/resource/blog/img/2024/90642-5882f5ffcf3b92988a49aaa5dac913c3.png)

歌手列表右侧的扳手图标表示此歌手名下存在重复文件。

![](https://oss.aqzscn.cn/resource/blog/img/2024/7ec2a-423ad72f94ace289a7d801936d02e3f6.png)

## 资料库同步

### 自动同步

应用启动时会检测服务端歌曲数量，如果大于本地副本歌曲数量，则增量同步缺失的数据。

:::warning

增量更新的原理是按歌曲添加时间倒序查询，因此若您在服务端删除或修改过歌曲，则需要手动点击同步按钮从头同步。

:::

应用启动时需要恢复上次播放列表，某些音乐服务的歌曲资源或图片资源需要登录后才能获取，因此将播放器的初始化放在了登录操作之后，若您在播放歌曲时遇到了**播放器正在初始化**的提示，请耐心等待片刻。

### 手动同步

若自动同步无法满足您的需求，请点击音乐资料库的「立即同步」按钮手动更新本地副本。

:::info

手动同步是全量更新，若同步过程中中断，下次启动后会自动进行增量更新。

:::

### 直连模式

在直连模式下，应用不会一次性将服务端的数据缓存下来（即上述两种同步方式均不会启用），您的每次操作都会从服务器获取数据。若您的曲库较大，可以尝试开启此选项，以提升首次进入应用时的体验。

但请注意，由于直连模式完全依赖服务端接口的返回结果，现有功能可能会失去部分特性：

- 每日推荐无法筛选歌曲时长，即可能有部分长音频进入每日推荐。
- 无法检测重复歌曲。
- 在没有文件夹接口的服务端（Subsonic/Navidrome/Jellyfin）中，文件夹功能仅显示本地副本中的数据（即手动查询过的数据）。
- 部分排序和过滤功能不可用。