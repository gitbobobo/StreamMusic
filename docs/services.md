---
sidebar_position: 2
---

# 音乐服务

就我个人使用体验来讲，目前并不存在完美的音乐服务，它们各有优缺点，需要根据自己的需求酌情选择。

## 支持版本

- Navidrome 0.49.3 及以上
- Plex 1.29.2 及以上，支持 OTP 验证码登录
- AudioStation DSM 6 及以上，支持 OTP 验证码登录
- Emby  4.7.14.0 及以上
- Jellyfin 10.8.10 及以上
- Subsonic 1.15.0 及以上

## 功能比较

`-` 未知

|  | Subsonic | Navidrome | Audio Station | Emby | Jellyfin | Plex |
| ------- | ------- | ------- | --- | --- | --- | --- |
| 内嵌歌词<sup>1</sup> | - | ✅ |  | ✅ |  | |
| 外置歌词 | - |  | ✅ | ✅ | ✅ | ✅ |
| 在线歌词 | - |  | ✅ | ✅ | ✅ | ✅ |
| 歌手简介 | - | ✅ | | ✅ | ✅ | ✅ |
| 歌手头像 | - | *<sup>2</sup> | *<sup>3</sup> | ✅ | ✅ | ✅ |
| 多艺术家 | - |  | - | ✅ | ✅ | |
| 回放增益 | - | ✅  | ✅ | | | ✅ |
| 评分功能<sup>4</sup> | ✅ | ✅  | ✅ |  |  | ✅ |
| 收藏功能<sup>5</sup> | ✅ | ✅  | | ✅ | ✅ | |
| 文件夹 | - | | ✅ | ✅ | | ✅ |
| 删除接口 | - | | | ✅ | ✅ | ✅ |


1. 自 1.2.8 起，音流可读取音乐文件内嵌歌词，详细支持情况[点此查看](/docs/notes/plugins#audio_metadata_reader)。
2. Navidrome 若要显示歌手头像，需要配置 Spotify API（国内环境即使配置了也很难有作用），或在歌手文件夹下放一张名为 `artist.*` 的图片。[Artwork location resolution](https://www.navidrome.org/docs/usage/artwork/#artists)
3. Audio Station 的歌手头像用的是音乐库中的专辑图片。
4. Audio Station 只能对歌曲评分。
5. Audio Station 和 Plex 没有收藏功能，音流会将评级为 🌟🌟🌟🌟🌟 的歌曲视为收藏的歌曲。
