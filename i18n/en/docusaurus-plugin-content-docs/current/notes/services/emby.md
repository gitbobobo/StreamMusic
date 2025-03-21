---
sidebar_position: 4
---

# Emby 接口文档

:::note 参考文档：

- [Emby API](https://github.com/MediaBrowser/Emby/wiki)

:::

## 认证

### AuthenticateByName 登录

参见 Jellyfin 的 [AuthenticateByName](./jellyfin#authenticatebyname-登录) 接口。

### Ping 测试服务器连通性

GET: `[host]/System/Ping`

## 请求节点

### Items 获取专辑列表

GET: `[host]/Users/[UserId]/Items`

query:

| 参数名 | 备注 |
| --- | --- |
| SortBy | 排序方式列表，可选值: `Random`, `DateCreated`, `PremiereDate`, `PlayCount`, `DatePlayed`, `SortName`, `CommunityRating` |
| SortOrder | 排序，可选值: `Ascending`, `Descending` |
| IncludeItemTypes | 包含的项目类型，可选值：`MusicAlbum` |
| Recursive | 是否递归查询 |
| Fields | 包含的字段列表，可选值：`SortName`, `BasicSyncInfo`, `ChildCount`, `DateCreated`, `ProductionYear` |
| ImageTypeLimit | 返回的每个图片类型图片数量 |
| EnableImageTypes | 图片类型列表，可选值：`Primary`, `Backdrop`, `Thumb` |
| StartIndex | 起始行数 |
| Limit | 最大数量，可选 |
| ParentId | 父视图ID，可选 |
| artistIds | 歌手 id 列表，可选 |
| GenreIds | 类型ID列表，可选 |
| SearchTerm | 搜索词，可选 |

response:

```json
{
    "Items": [
        {
            "Name": "爆笑三国演义",
            "ServerId": "54068b26c84949dc809677381d1267a9",
            "Id": "79106",
            "DateCreated": "2024-04-12T01:50:05.0000000Z",
            "SupportsSync": true,
            "SortName": "爆笑三国演义",
            "RunTimeTicks": 3305120000,
            "ProductionYear": 2023,
            "IsFolder": true,
            "Type": "MusicAlbum",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false
            },
            "Artists": [
                "佳音少儿、 金德哥哥"
            ],
            "ArtistItems": [
                {
                    "Name": "佳音少儿、 金德哥哥",
                    "Id": "79105"
                }
            ],
            "Composers": [],
            "AlbumArtist": "佳音少儿、 金德哥哥",
            "AlbumArtists": [
                {
                    "Name": "佳音少儿、 金德哥哥",
                    "Id": "79105"
                }
            ],
            "ImageTags": {},
            "BackdropImageTags": []
        },
        {
            "Name": "森之恋歌",
            "ServerId": "54068b26c84949dc809677381d1267a9",
            "Id": "79103",
            "DateCreated": "2024-04-10T04:24:53.0000000Z",
            "SupportsSync": true,
            "SortName": "森之恋歌",
            "RunTimeTicks": 2332317080,
            "ProductionYear": 2022,
            "IsFolder": true,
            "Type": "MusicAlbum",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false
            },
            "Artists": [
                "单依纯"
            ],
            "ArtistItems": [
                {
                    "Name": "单依纯",
                    "Id": "7113"
                }
            ],
            "Composers": [],
            "AlbumArtist": "单依纯",
            "AlbumArtists": [
                {
                    "Name": "单依纯",
                    "Id": "7113"
                }
            ],
            "ImageTags": {
                "Primary": "08f7baa96fe117a2d22ced7f34f292f1"
            },
            "BackdropImageTags": []
        }
    ],
    "TotalRecordCount": 3654
}
```

### Items/[id] 获取专辑信息

GET: `[host]/Users/[UserId]/Items/[id]`

response:

```json
{
    "Name": "森之恋歌",
    "ServerId": "54068b26c84949dc809677381d1267a9",
    "Id": "79103",
    "Etag": "3fe9c1df1c602725cefae4ab30e445b6",
    "DateCreated": "2024-04-10T04:24:53.0000000Z",
    "CanDelete": true,
    "CanDownload": false,
    "PresentationUniqueKey": "b1e9c0c3922344d4b852b46bd0130b23",
    "SupportsSync": true,
    "SortName": "森之恋歌",
    "ForcedSortName": "森之恋歌",
    "ExternalUrls": [],
    "Taglines": [],
    "Genres": [],
    "RunTimeTicks": 2332317080,
    "PlayAccess": "Full",
    "ProductionYear": 2022,
    "RemoteTrailers": [],
    "ProviderIds": {},
    "IsFolder": true,
    "Type": "MusicAlbum",
    "Studios": [],
    "GenreItems": [],
    "TagItems": [],
    "UserData": {
        "PlaybackPositionTicks": 0,
        "PlayCount": 0,
        "IsFavorite": false,
        "Played": false
    },
    "DisplayPreferencesId": "f13d7f51d4f1f8b6fcd620855eb88c1e",
    "PrimaryImageAspectRatio": 1,
    "Artists": [
        "单依纯"
    ],
    "ArtistItems": [
        {
            "Name": "单依纯",
            "Id": "7113"
        }
    ],
    "Composers": [],
    "AlbumArtist": "单依纯",
    "AlbumArtists": [
        {
            "Name": "单依纯",
            "Id": "7113"
        }
    ],
    "ImageTags": {
        "Primary": "08f7baa96fe117a2d22ced7f34f292f1"
    },
    "BackdropImageTags": [],
    "LockedFields": [],
    "LockData": false
}
```

### AlbumArtists 获取专辑艺术家列表

GET: `[host]/Artists/AlbumArtists`

其他格式与歌手列表一致。

### Artists 获取歌手列表

参见 Jellyfin 的 [Artists](./jellyfin#artists-获取歌手列表) 接口。

补充 query：

| 参数名 | 备注 |
| --- | --- |
| ParentId | 父视图ID，可选 |
| GenreIds | 类型ID列表，可选 |

### Items/[id] 获取歌手信息

参见 Jellyfin 的 [Items/id](./jellyfin#itemsid-获取歌手信息) 接口。

### Similar 获取相似歌手

参见 Jellyfin 的 [Similar](./jellyfin#similar-获取相似歌手) 接口。

### Images 图片链接

GET: `[host]/Items/[id]/Primary?fillHeight=600&fillWidth=600`

:::note

请求头需要添加授权信息。

:::

### Playlists 创建歌单

POST: `[host]/Playlists`

body(`application/json`):

| 参数名 | 备注 |
| --- | --- |
| Name | 歌单名 |
| Ids | 包含的歌曲ID列表，不建议传空列表，因为 Emby 的电影和音乐可以混在一个歌单里，初始化时有音乐方便后续只查询包含音乐的歌单。 |
| MediaType | 媒体类型，可选值：`Audio` |

response:

```json
{
    "Id": "bea612652ad4b3578c76fa87a13e7fa7"
}
```

### Items/[id] 删除歌单

DELETE: `[host]/Items/[id]`

response code: 204

### Items 从服务器删除歌曲

DELETE: `[host]/Items`

query:

| 参数名 | 备注 |
| --- | --- |
| Ids | 包含的歌曲ID列表 |

:::caution

危险操作，此接口需要管理员权限。

:::

### Items 获取目录列表

GET: `[host]/Users/[UserId]/Items`

query:

| 参数名 | 备注 |
| --- | --- |
| ParentId | 目录ID，传音乐库ID时查询根目录 |
| EnableImageTypes | `Primary,Backdrop,Thumb` |
| ImageTypeLimit | `1` |
| SortBy | 排序方式，可选值：`IsFolder`, `Filename` |
| StartIndex | 行数偏移 |
| Limit | 结果数量 |
| Fields | 返回的列，可选值：`BasicSyncInfo,CanDelete,PrimaryImageAspectRatio,ProductionYear,Status,EndDate` |

response:

```json
{
    "Items": [
        {
            "Name": "阿悄单曲集",
            "ServerId": "5472030a784c45f4a90845bd9886bc98",
            "Id": "27163",
            "CanDelete": true,
            "SupportsSync": true,
            "IsFolder": true,
            "Type": "Folder",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false
            },
            "ImageTags": {},
            "BackdropImageTags": [],
            "PrimaryImageItemId": "27182",
            "PrimaryImageTag": "1b50e7c8bca70c47ddb8ba969c9d34ad"
        },
        {
            "Name": "最坚强的...阿悄勇敢作品集",
            "ServerId": "5472030a784c45f4a90845bd9886bc98",
            "Id": "27173",
            "CanDelete": true,
            "SupportsSync": true,
            "IsFolder": true,
            "Type": "Folder",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false
            },
            "ImageTags": {},
            "BackdropImageTags": [],
            "PrimaryImageItemId": "27193",
            "PrimaryImageTag": "60c07108c93ed897bd7b5ad4624e1090"
        },
        {
            "Name": "犯贱",
            "ServerId": "5472030a784c45f4a90845bd9886bc98",
            "Id": "27159",
            "CanDelete": true,
            "SupportsSync": true,
            "RunTimeTicks": 2138906120,
            "ProductionYear": 2008,
            "IndexNumber": 47,
            "IsFolder": false,
            "Type": "Audio",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false
            },
            "PrimaryImageAspectRatio": 1,
            "Artists": [
                "徐良",
                "阿悄"
            ],
            "ArtistItems": [
                {
                    "Name": "徐良",
                    "Id": "54622"
                },
                {
                    "Name": "阿悄",
                    "Id": "55566"
                }
            ],
            "Composers": [],
            "Album": "流行网络歌",
            "AlbumArtists": [],
            "ImageTags": {
                "Primary": "f50019d3a0df167ac2cd3797aa3fe0b9"
            },
            "BackdropImageTags": [],
            "MediaType": "Audio"
        }
    ],
    "TotalRecordCount": 15
}
```

### Genres 获取全部类型

GET: `[host]/Genres`

query:

| 参数名 | 备注 |
| --- | --- |
| ParentId | 20111 |
| Recursive | 是否递归查询 |
| IncludeItemTypes | 固定值，`MusicAlbum` |
| userId | 用户ID |
| StartIndex | 起始行数 |
| Limit | 最大行数 |
| SortBy | 固定值，`SortName` |
| SortOrder | 固定值，`Ascending` |

response:

```json
{
    "Items": [
        {
            "Name": "播客",
            "ServerId": "5472030a784c45f4a90845bd9886bc98",
            "Id": "59145",
            "CanDelete": false,
            "SupportsSync": true,
            "Type": "MusicGenre",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false
            },
            "PrimaryImageAspectRatio": 1,
            "ImageTags": {
                "Primary": "c7a60444a93cb13209189ed883f8a638"
            },
            "BackdropImageTags": []
        },
        {
            "Name": "古风",
            "ServerId": "5472030a784c45f4a90845bd9886bc98",
            "Id": "61242",
            "CanDelete": false,
            "SupportsSync": true,
            "Type": "MusicGenre",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false
            },
            "PrimaryImageAspectRatio": 1,
            "ImageTags": {
                "Primary": "fb59591640202c85ef243b7e1df8789d"
            },
            "BackdropImageTags": []
        },
    ],
    "TotalRecordCount": 38
}
```

### Stream.js 获取歌词

GET: `[host]/Items/[id]/[MediaSourceId]/Subtitles/[SubtitleIndex]/Stream.js`

> SubtitleIndex 从歌曲信息中获取，取 `MediaStreams[Type=Subtitle&Codec=lrc].Index` 的值

query:

| 参数名 | 备注 |
| --- | --- |
| MediaBrowser Client | 客户端名称 |
| Device | 设备名 |
| DeviceId | 设备Id |
| Version | 客户端版本号 |
| Token | 访问令牌，登录后从响应中的 `AccessToken` 字段获取 |

response:

```json
{
    "TrackEvents": [
        {
            "Text": "艾里甫与赛乃姆 - 刀郎",
            "StartPositionTicks": 0,
            "EndPositionTicks": 90000000
        },
        {
            "Text": "词：刀郎",
            "StartPositionTicks": 90000000,
            "EndPositionTicks": 180000000
        },
        {
            "Text": "曲：刀郎",
            "StartPositionTicks": 180000000,
            "EndPositionTicks": 270100000
        },
        {
            "Text": "从小和你青梅竹马相约在天山下",
            "StartPositionTicks": 270100000,
            "EndPositionTicks": 339300000
        },
        {
            "Text": "",
            "StartPositionTicks": 339300000,
            "EndPositionTicks": 371200000
        },
        {
            "Text": "我们本来是天底下最幸福的人啊",
            "StartPositionTicks": 371200000,
            "EndPositionTicks": 457400000
        },
        {
            "Text": "",
            "StartPositionTicks": 457400000,
            "EndPositionTicks": 470100000
        },
        {
            "Text": "赛乃姆你是花丛中最美的石榴花",
            "StartPositionTicks": 470100000,
            "EndPositionTicks": 551700000
        },
        {
            "Text": "",
            "StartPositionTicks": 551700000,
            "EndPositionTicks": 570800000
        },
        {
            "Text": "艾里甫我却是巴格达上孤独的阿卡",
            "StartPositionTicks": 570800000,
            "EndPositionTicks": 643300000
        },
        {
            "Text": "",
            "StartPositionTicks": 643300000,
            "EndPositionTicks": 696000000
        },
        {
            "Text": "夜莺歌声在每个夜晚都会陪伴她",
            "StartPositionTicks": 696000000,
            "EndPositionTicks": 765400000
        },
        {
            "Text": "",
            "StartPositionTicks": 765400000,
            "EndPositionTicks": 795500000
        },
        {
            "Text": "我的琴声却飘荡在遥远的巴格达",
            "StartPositionTicks": 795500000,
            "EndPositionTicks": 877900000
        },
        {
            "Text": "",
            "StartPositionTicks": 877900000,
            "EndPositionTicks": 896800000
        },
        {
            "Text": "为了爱情我被放逐在天涯",
            "StartPositionTicks": 896800000,
            "EndPositionTicks": 976600000
        },
        {
            "Text": "",
            "StartPositionTicks": 976600000,
            "EndPositionTicks": 996000000
        },
        {
            "Text": "莫非今生和你厮守变成了神话",
            "StartPositionTicks": 996000000,
            "EndPositionTicks": 1067300000
        },
        {
            "Text": "",
            "StartPositionTicks": 1067300000,
            "EndPositionTicks": 1095900000
        },
        {
            "Text": "我寻遍天山南北我要找到你赛乃姆",
            "StartPositionTicks": 1095900000,
            "EndPositionTicks": 1181700000
        },
        {
            "Text": "",
            "StartPositionTicks": 1181700000,
            "EndPositionTicks": 1195800000
        },
        {
            "Text": "不管是跋山涉水历尽千辛万苦",
            "StartPositionTicks": 1195800000,
            "EndPositionTicks": 1281000000
        },
        {
            "Text": "",
            "StartPositionTicks": 1281000000,
            "EndPositionTicks": 1295300000
        },
        {
            "Text": "花园里种不出天山上的雪莲花",
            "StartPositionTicks": 1295300000,
            "EndPositionTicks": 1376800000
        },
        {
            "Text": "",
            "StartPositionTicks": 1376800000,
            "EndPositionTicks": 1395600000
        },
        {
            "Text": "不历经磨难我找不到今生的幸福",
            "StartPositionTicks": 1395600000,
            "EndPositionTicks": 1481900000
        },
        {
            "Text": "",
            "StartPositionTicks": 1481900000,
            "EndPositionTicks": 1758000000
        },
        {
            "Text": "夜莺歌声在每个夜晚都会陪伴她",
            "StartPositionTicks": 1758000000,
            "EndPositionTicks": 1826600000
        },
        {
            "Text": "",
            "StartPositionTicks": 1826600000,
            "EndPositionTicks": 1857600000
        },
        {
            "Text": "我的琴声却飘荡在遥远的巴格达",
            "StartPositionTicks": 1857600000,
            "EndPositionTicks": 1939100000
        },
        {
            "Text": "",
            "StartPositionTicks": 1939100000,
            "EndPositionTicks": 1958600000
        },
        {
            "Text": "为了爱情我被放逐在天涯",
            "StartPositionTicks": 1958600000,
            "EndPositionTicks": 2039600000
        },
        {
            "Text": "",
            "StartPositionTicks": 2039600000,
            "EndPositionTicks": 2059000000
        },
        {
            "Text": "莫非今生和你厮守变成了神话",
            "StartPositionTicks": 2059000000,
            "EndPositionTicks": 2131000000
        },
        {
            "Text": "",
            "StartPositionTicks": 2131000000,
            "EndPositionTicks": 2158800000
        },
        {
            "Text": "我寻遍天山南北我要找到你赛乃姆",
            "StartPositionTicks": 2158800000,
            "EndPositionTicks": 2242800000
        },
        {
            "Text": "",
            "StartPositionTicks": 2242800000,
            "EndPositionTicks": 2258300000
        },
        {
            "Text": "不管是跋山涉水历尽千辛万苦",
            "StartPositionTicks": 2258300000,
            "EndPositionTicks": 2343300000
        },
        {
            "Text": "",
            "StartPositionTicks": 2343300000,
            "EndPositionTicks": 2358900000
        },
        {
            "Text": "花园里种不出天山上的雪莲花",
            "StartPositionTicks": 2358900000,
            "EndPositionTicks": 2439100000
        },
        {
            "Text": "",
            "StartPositionTicks": 2439100000,
            "EndPositionTicks": 2458700000
        },
        {
            "Text": "不历经磨难我找不到今生的幸福",
            "StartPositionTicks": 2458700000,
            "EndPositionTicks": 2543500000
        },
        {
            "Text": "",
            "StartPositionTicks": 2543500000,
            "EndPositionTicks": 2572400000
        },
        {
            "Text": "我寻遍天山南北我要找到你赛乃姆",
            "StartPositionTicks": 2572400000,
            "EndPositionTicks": 2655000000
        },
        {
            "Text": "",
            "StartPositionTicks": 2655000000,
            "EndPositionTicks": 2669100000
        },
        {
            "Text": "不管是跋山涉水历尽千辛万苦",
            "StartPositionTicks": 2669100000,
            "EndPositionTicks": 2756300000
        },
        {
            "Text": "",
            "StartPositionTicks": 2756300000,
            "EndPositionTicks": 2771600000
        },
        {
            "Text": "花园里种不出天山上的雪莲花",
            "StartPositionTicks": 2771600000,
            "EndPositionTicks": 2851700000
        },
        {
            "Text": "",
            "StartPositionTicks": 2851700000,
            "EndPositionTicks": 2869600000
        },
        {
            "Text": "不历经磨难我找不到今生的幸福",
            "StartPositionTicks": 2869600000
        }
    ]
}
```

### Views 获取视图列表

GET: `[host]/Users/[UserId]/Views`

response:

```json
{
    "Items": [
        {
            "Name": "电影",
            "ServerId": "54068b26c84949dc809677381d1267a9",
            "Id": "11013",
            "Guid": "3227ce1e069754c594af25ea66d69fc7",
            "Etag": "f0a63776848cf0513618763c2e49df1e",
            "DateCreated": "2023-12-07T05:32:20.0000000Z",
            "CanDelete": false,
            "CanDownload": false,
            "PresentationUniqueKey": "3227ce1e069754c594af25ea66d69fc7",
            "SortName": "电影",
            "ForcedSortName": "电影",
            "ExternalUrls": [],
            "Path": "/var/packages/EmbyServer/var/root/default/电影",
            "Taglines": [],
            "FileName": "电影",
            "PlayAccess": "Full",
            "RemoteTrailers": [],
            "ProviderIds": {},
            "IsFolder": true,
            "ParentId": "1",
            "Type": "CollectionFolder",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false
            },
            "ChildCount": 3,
            "DisplayPreferencesId": "3227ce1e069754c594af25ea66d69fc7",
            "PrimaryImageAspectRatio": 1.7777777777777777,
            "CollectionType": "movies",
            "ImageTags": {
                "Primary": "405c8c5a67bf8e5ded4bd593b5af9926"
            },
            "BackdropImageTags": [],
            "LockedFields": [],
            "LockData": false
        },
        {
            "Name": "电视剧",
            "ServerId": "54068b26c84949dc809677381d1267a9",
            "Id": "12075",
            "Guid": "fc8fa12ee6bc083abb484b1b0bbc420f",
            "Etag": "57b2fc16eb7cf0f78b1bf89743af526c",
            "DateCreated": "2023-12-07T05:35:46.0000000Z",
            "CanDelete": false,
            "CanDownload": false,
            "PresentationUniqueKey": "fc8fa12ee6bc083abb484b1b0bbc420f",
            "SortName": "电视剧",
            "ForcedSortName": "电视剧",
            "ExternalUrls": [],
            "Path": "/var/packages/EmbyServer/var/root/default/电视剧",
            "Taglines": [],
            "FileName": "电视剧",
            "PlayAccess": "Full",
            "RemoteTrailers": [],
            "ProviderIds": {},
            "IsFolder": true,
            "ParentId": "1",
            "Type": "CollectionFolder",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false
            },
            "ChildCount": 4,
            "DisplayPreferencesId": "fc8fa12ee6bc083abb484b1b0bbc420f",
            "PrimaryImageAspectRatio": 0.6666666666666666,
            "CollectionType": "tvshows",
            "ImageTags": {
                "Primary": "71dd3f151805e02efca3fa7331ea0ffc"
            },
            "BackdropImageTags": [
                "b5b4ab3a04d43f9dad650208c956ee56"
            ],
            "LockedFields": [],
            "LockData": false
        },
        {
            "Name": "综艺",
            "ServerId": "54068b26c84949dc809677381d1267a9",
            "Id": "14508",
            "Guid": "22376d03fca73f102a0de4d40ed3cd41",
            "Etag": "f0a63776848cf0513618763c2e49df1e",
            "DateCreated": "2023-12-07T05:38:21.0000000Z",
            "CanDelete": false,
            "CanDownload": false,
            "PresentationUniqueKey": "22376d03fca73f102a0de4d40ed3cd41",
            "SortName": "综艺",
            "ForcedSortName": "综艺",
            "ExternalUrls": [],
            "Path": "/var/packages/EmbyServer/var/root/default/综艺",
            "Taglines": [],
            "FileName": "综艺",
            "PlayAccess": "Full",
            "RemoteTrailers": [],
            "ProviderIds": {},
            "IsFolder": true,
            "ParentId": "1",
            "Type": "CollectionFolder",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false
            },
            "ChildCount": 4,
            "DisplayPreferencesId": "22376d03fca73f102a0de4d40ed3cd41",
            "PrimaryImageAspectRatio": 1.7777777777777777,
            "CollectionType": "tvshows",
            "ImageTags": {
                "Primary": "faf947548d07f9e99462e33fbf38a593"
            },
            "BackdropImageTags": [],
            "LockedFields": [],
            "LockData": false
        },
        {
            "Name": "音乐",
            "ServerId": "54068b26c84949dc809677381d1267a9",
            "Id": "4",
            "Guid": "28e9960207c978c0d9aaefc8ae2d3a79",
            "Etag": "1805ebfb97d3af5c940a5d654007f81e",
            "DateCreated": "2023-11-26T06:22:14.0000000Z",
            "CanDelete": false,
            "CanDownload": false,
            "PresentationUniqueKey": "28e9960207c978c0d9aaefc8ae2d3a79",
            "SortName": "音乐",
            "ForcedSortName": "音乐",
            "ExternalUrls": [],
            "Path": "/var/packages/EmbyServer/var/root/default/音乐",
            "Taglines": [],
            "FileName": "音乐",
            "PlayAccess": "Full",
            "RemoteTrailers": [],
            "ProviderIds": {},
            "IsFolder": true,
            "ParentId": "1",
            "Type": "CollectionFolder",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false
            },
            "ChildCount": 6,
            "DisplayPreferencesId": "28e9960207c978c0d9aaefc8ae2d3a79",
            "PrimaryImageAspectRatio": 1.7777777777777777,
            "CollectionType": "music",
            "ImageTags": {
                "Primary": "f7c61a28148d5a2fad6ca0bda48ebf49"
            },
            "BackdropImageTags": [],
            "LockedFields": [],
            "LockData": false
        },
        {
            "Name": "合集",
            "ServerId": "54068b26c84949dc809677381d1267a9",
            "Id": "30885",
            "Guid": "e7bfe656953e3fad0bdf034be7969a97",
            "Etag": "4cc2e1798871df8cf8649fb49a223731",
            "DateCreated": "2023-12-07T20:39:49.0000000Z",
            "CanDelete": false,
            "CanDownload": false,
            "PresentationUniqueKey": "e7bfe656953e3fad0bdf034be7969a97",
            "SortName": "合集",
            "ForcedSortName": "合集",
            "ExternalUrls": [],
            "Path": "/var/packages/EmbyServer/var/root/default/合集",
            "Taglines": [],
            "FileName": "合集",
            "PlayAccess": "Full",
            "RemoteTrailers": [],
            "ProviderIds": {},
            "IsFolder": true,
            "ParentId": "1",
            "Type": "CollectionFolder",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false
            },
            "ChildCount": 3,
            "DisplayPreferencesId": "e7bfe656953e3fad0bdf034be7969a97",
            "PrimaryImageAspectRatio": 1.7777777777777777,
            "CollectionType": "boxsets",
            "ImageTags": {
                "Primary": "30a549922a74abc9f506e7b363ccfc65"
            },
            "BackdropImageTags": [],
            "LockedFields": [],
            "LockData": false
        },
        {
            "Name": "短视频",
            "ServerId": "54068b26c84949dc809677381d1267a9",
            "Id": "31373",
            "Guid": "9548a2410227b737d377fefbd086a046",
            "Etag": "b262db8903af6dc3c585931b679cf387",
            "DateCreated": "2023-12-14T03:01:56.0000000Z",
            "CanDelete": false,
            "CanDownload": false,
            "PresentationUniqueKey": "9548a2410227b737d377fefbd086a046",
            "SortName": "短视频",
            "ForcedSortName": "短视频",
            "ExternalUrls": [],
            "Path": "/var/packages/EmbyServer/var/root/default/混合内容",
            "Taglines": [],
            "FileName": "混合内容",
            "PlayAccess": "Full",
            "RemoteTrailers": [],
            "ProviderIds": {},
            "IsFolder": true,
            "ParentId": "1",
            "Type": "CollectionFolder",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false
            },
            "ChildCount": 9,
            "DisplayPreferencesId": "9548a2410227b737d377fefbd086a046",
            "PrimaryImageAspectRatio": 1.7777777777777777,
            "ImageTags": {
                "Primary": "604035e56178ae7a63e5039e405b7c69"
            },
            "BackdropImageTags": [],
            "LockedFields": [],
            "LockData": false
        },
        {
            "Name": "纪录片",
            "ServerId": "54068b26c84949dc809677381d1267a9",
            "Id": "64855",
            "Guid": "1c474c9c4d728d1a2f621adad0f221ae",
            "Etag": "57b2fc16eb7cf0f78b1bf89743af526c",
            "DateCreated": "2024-02-28T13:12:33.0000000Z",
            "CanDelete": false,
            "CanDownload": false,
            "PresentationUniqueKey": "1c474c9c4d728d1a2f621adad0f221ae",
            "SortName": "纪录片",
            "ForcedSortName": "纪录片",
            "ExternalUrls": [],
            "Path": "/var/packages/EmbyServer/var/root/default/纪录片",
            "Taglines": [],
            "FileName": "纪录片",
            "PlayAccess": "Full",
            "RemoteTrailers": [],
            "ProviderIds": {},
            "IsFolder": true,
            "ParentId": "1",
            "Type": "CollectionFolder",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false
            },
            "ChildCount": 6,
            "DisplayPreferencesId": "1c474c9c4d728d1a2f621adad0f221ae",
            "PrimaryImageAspectRatio": 0.6688963210702341,
            "CollectionType": "tvshows",
            "ImageTags": {
                "Primary": "a3a250e5e6f81e1c058d335d63b31786"
            },
            "BackdropImageTags": [
                "4876668c3b323fa676ca5ff5b5a2fd3f"
            ],
            "LockedFields": [],
            "LockData": false
        }
    ],
    "TotalRecordCount": 7
}
```

### Items 获取歌单列表

GET: `[host]/Users/[UserId]/Items`

query:

| 参数名 | 备注 |
| --- | --- |
| SortBy | 排序方式列表，可选值: `SortName`|
| SortOrder | 排序，可选值: `Ascending`, `Descending` |
| ParentId | 视图ID，由上一步获取，筛选 `CollectionType = music` 的视图 |
| GenreIds | 类型ID列表，可选 |
| Recursive | 是否递归查询 |
| includeItemTypes | 项目类型，可选值：`Playlist` |
| Fields | 包含的字段列表，可选值：`SortName`, `CanDelete`, `PrimaryImageAspectRatio`, `BasicSyncInfo`, `Container`, `ProductionYear`, `Status`, `EndDate`, `Prefix` |
| EnableImageTypes | 图像类型列表，可选值：`Primary`, `Backdrop`, `Thumb` |
| StartIndex | 起始行数 |
| Limit | 最大数量，可选 |

response:

```json
{
    "Items": [
        {
            "Name": "电影列表",
            "ServerId": "54068b26c84949dc809677381d1267a9",
            "Id": "66945",
            "Prefix": "电",
            "CanDelete": true,
            "SupportsSync": true,
            "RunTimeTicks": 87574387960,
            "IsFolder": true,
            "Type": "Playlist",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false
            },
            "PrimaryImageAspectRatio": 1,
            "ImageTags": {
                "Primary": "7a76da4af13b608e8498635c878e5752"
            },
            "BackdropImageTags": []
        },
        {
            "Name": "纯歌曲",
            "ServerId": "54068b26c84949dc809677381d1267a9",
            "Id": "66946",
            "Prefix": "纯",
            "CanDelete": true,
            "SupportsSync": true,
            "RunTimeTicks": 4177020410,
            "IsFolder": true,
            "Type": "Playlist",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false
            },
            "PrimaryImageAspectRatio": 1,
            "ImageTags": {
                "Primary": "ea67ae6c9fb3232d03d03d18e4ec2ef0"
            },
            "BackdropImageTags": []
        }
    ],
    "TotalRecordCount": 2
}
```

### Info 获取服务器信息

参见 Jellyfin 的 [Info](./jellyfin#info-获取服务器信息) 接口。

### ScheduledTasks 获取扫描状态

参见 Jellyfin 的 [ScheduledTasks](jellyfin#scheduledtasks-获取扫描状态) 接口。

### PlayedItems/[id] 滚动播放记录

**播放开始**

POST：`[host]/Sessions/Playing`

body:

| 参数名 | 备注 |
| --- | --- |
| ItemId | 歌曲ID |
| PlaySessionId | 会话ID |
| PositionTicks | 播放进度 |
| IsPaused | 是否暂停 |
| PlaybackRate | 播放速度 |
| PlayMethod | 播放方式，可选值：`Transcode`, `DirectPlay`, `DirectStream` |

**播放进度**

POST：`[host]/Sessions/Playing/Progress`

body:

| 参数名 | 备注 |
| --- | --- |
| ItemId | 歌曲ID |
| PlaySessionId | 会话ID |
| PositionTicks | 播放进度 |
| IsPaused | 是否暂停 |
| PlaybackRate | 播放速度 |
| PlayMethod | 播放方式，可选值：`Transcode`, `DirectPlay`, `DirectStream` |

Emby 文档中对播放进度的报告时机说明如下：

- 每 10 秒自动报告一次（用于校准服务器上的自动进度增量）
- 在用户于播放器进行任何交互后立即进行

报告进度的原因如下，音流仅会对勾选的事件报告进度：

- [x] TimeUpdate 时间更新
- [x] Pause 暂停
- [x] Unpause 取消暂停
- [ ] VolumeChange 音量变化
- [ ] RepeatModeChange 重复模式更改
- [ ] AudioTrackChange 音轨更改
- [ ] SubtitleTrackChange 字幕更改
- [ ] PlaylistItemMove 播放列表项移动
- [ ] PlaylistItemRemove 播放列表项删除
- [ ] PlaylistItemAdd 播放列表项添加
- [ ] QualityChange 质量变革
- [ ] SubtitleOffsetChange 字幕偏移
- [x] PlaybackRateChange 播放速度改变

**标记为已播放**

> 向 Emby 上报**播放开始**状态时，播放次数已经自动+1，因此无需使用此接口。

POST: `[host]/Users/[UserId]/PlayedItems/[id]`

query:

| 参数名 | 备注 |
| --- | --- |
| datePlayed | 播放时间，yyyyMMddHHmmss |

Last.fm 开发者文档中对 scrobble 的条件有以下要求：

- 曲目时长必须超过 30 秒
- 曲目已经播放了 4 分钟或总时长的一半（以较早发生者为准）

满足这些条件后，随时可以发送 scrobble 请求，通常最方便的做法是在曲目播放完毕后发送。

:::info

在 1.3.0 及之前版本，音流会在歌曲播放到 1/4 时上报播放记录。

在 1.3.1 及之后版本，音流将遵循上述文档中建议的做法来上报播放记录。

:::

### Similar 获取相似歌曲

GET: `[host]/Items/[id]/Similar`

query:

| 参数名 | 备注 |
| --- | --- |
| Limit | 结果数量 |
| Fields | 包含的字段列表，可选值：`AudioInfo`, `SortName`, `MediaSources`, `DateCreated`, `ProductionYear` |
| userId | 用户ID |

response:

```json
{
    "Items": [
        {
            "Name": "狼爱上羊",
            "ServerId": "54068b26c84949dc809677381d1267a9",
            "Id": "45898",
            "DateCreated": "2023-07-28T11:12:03.0000000Z",
            "Container": "ogg",
            "SortName": "狼爱上羊",
            "MediaSources": [
                {
                    "Protocol": "File",
                    "Id": "32fa0822ae32197cce9c1861acced72e",
                    "Path": "/volume1/music/刀郎/歌曲合辑/刀郎 - 狼爱上羊.ogg",
                    "Type": "Default",
                    "Container": "ogg",
                    "Size": 5938532,
                    "Name": "刀郎 - 狼爱上羊",
                    "IsRemote": false,
                    "RunTimeTicks": 4400587760,
                    "SupportsTranscoding": true,
                    "SupportsDirectStream": true,
                    "SupportsDirectPlay": true,
                    "IsInfiniteStream": false,
                    "RequiresOpening": false,
                    "RequiresClosing": false,
                    "RequiresLooping": false,
                    "SupportsProbing": false,
                    "MediaStreams": [
                        {
                            "Codec": "vorbis",
                            "TimeBase": "1/44100",
                            "Title": "狼爱上羊",
                            "DisplayTitle": "Und VORBIS stereo",
                            "IsInterlaced": false,
                            "ChannelLayout": "stereo",
                            "BitRate": 96000,
                            "Channels": 2,
                            "SampleRate": 44100,
                            "IsDefault": false,
                            "IsForced": false,
                            "Type": "Audio",
                            "Index": 0,
                            "IsExternal": false,
                            "IsTextSubtitleStream": false,
                            "SupportsExternalStream": false,
                            "Protocol": "File",
                            "AttachmentSize": 0
                        },
                        {
                            "Codec": "mjpeg",
                            "ColorSpace": "bt470bg",
                            "Comment": "Cover (front)",
                            "TimeBase": "1/90000",
                            "IsInterlaced": false,
                            "BitDepth": 8,
                            "RefFrames": 1,
                            "IsDefault": false,
                            "IsForced": false,
                            "Height": 750,
                            "Width": 750,
                            "RealFrameRate": 90000,
                            "Profile": "Baseline",
                            "Type": "EmbeddedImage",
                            "AspectRatio": "1:1",
                            "Index": 1,
                            "IsExternal": false,
                            "IsTextSubtitleStream": false,
                            "SupportsExternalStream": false,
                            "Protocol": "File",
                            "PixelFormat": "yuvj420p",
                            "Level": -99,
                            "IsAnamorphic": false,
                            "AttachmentSize": 0
                        },
                        {
                            "Codec": "text",
                            "Title": "Lyrics",
                            "Extradata": "[00:00.00]作词 : 汤潮 演唱:汤潮\n[00:28.62]北风呼呼的刮\n[00:33.35]雪花飘飘洒洒\n[00:38.70]突然传来了一声枪响\n[00:42.64]这匹狼他受了重伤\n[00:47.30]但他侥幸逃脱了\n[00:51.84]救它的是一只羊\n[00:55.89]从此它们约定三生\n[01:00.51]苦诉着衷肠\n[01:04.41]\n[01:05.26]狼说亲爱的\n[01:10.17]谢谢你为我疗伤\n[01:14.93]不管未来有多少的风雨\n[01:19.48]我都为你去抗\n[01:24.15]羊说不要客气\n[01:28.65]谁让我爱上了你\n[01:33.38]在你身边有多么的危险\n[01:37.97]我都会陪伴你\n[01:42.16]就这样 他们快乐的流浪\n[01:49.39]就这样 他们为爱歌唱\n[01:55.50]\n[01:56.45]狼爱上羊啊爱的疯狂\n[02:01.60]谁让他们真爱了一场\n[02:05.60]狼爱上羊啊并不荒唐\n[02:10.30]他们说有爱就有方向\n[02:14.85]狼爱上羊啊爱的风光\n[02:19.51]他们穿破世俗的城墙\n[02:24.30]狼爱上羊啊爱的疯狂\n[02:28.67]他们相互搀扶去远方\n[02:32.63]\n[02:45.63]\n[02:58.82]狼说亲爱的\n[03:03.28]谢谢你为我疗伤\n[03:07.72]不管未来有多少的风雨\n[03:12.58]我都为你去抗\n[03:17.16]羊说不要客气\n[03:21.61]谁让我爱上了你\n[03:26.32]在你身边有多么的危险\n[03:31.10]我都会陪伴你\n[03:35.17]就这样 他们快乐的流浪\n[03:42.50]就这样 他们为爱歌唱\n[03:48.59]\n[03:49.63]狼爱上羊啊爱的疯狂\n[03:54.70]谁让他们真爱了一场\n[03:58.78]狼爱上羊啊并不荒唐\n[04:03.40]他们说有爱就有方向\n[04:07.81]狼爱上羊啊爱的风光\n[04:12.54]他们穿破世俗的城墙\n[04:17.10]狼爱上羊啊爱的疯狂\n[04:21.82]他们相互搀扶去远方\n[04:27.42]",
                            "DisplayTitle": "Und (TEXT)",
                            "IsInterlaced": false,
                            "IsDefault": false,
                            "IsForced": false,
                            "Type": "Subtitle",
                            "Index": 2,
                            "IsExternal": false,
                            "IsTextSubtitleStream": true,
                            "SupportsExternalStream": true,
                            "Protocol": "File",
                            "AttachmentSize": 0,
                            "SubtitleLocationType": "InternalStream"
                        }
                    ],
                    "Formats": [],
                    "Bitrate": 107958,
                    "RequiredHttpHeaders": {},
                    "ReadAtNativeFramerate": false,
                    "DefaultAudioStreamIndex": 0,
                    "DefaultSubtitleStreamIndex": 2
                }
            ],
            "RunTimeTicks": 4400587760,
            "Size": 5938532,
            "Bitrate": 107958,
            "ProductionYear": 2005,
            "IndexNumber": 2,
            "IsFolder": false,
            "Type": "Audio",
            "ParentBackdropItemId": "10126",
            "ParentBackdropImageTags": [
                "401cc5f81954801ecbcc6235ac18705b"
            ],
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false
            },
            "Artists": [
                "刀郎"
            ],
            "ArtistItems": [
                {
                    "Name": "刀郎",
                    "Id": "10126"
                }
            ],
            "Composers": [],
            "Album": "歌曲合辑",
            "AlbumId": "10130",
            "AlbumPrimaryImageTag": "b2b7edb1ed1d0fee7ede1a1b6ed6c341",
            "AlbumArtist": "刀郎",
            "AlbumArtists": [
                {
                    "Name": "刀郎",
                    "Id": "10126"
                }
            ],
            "ImageTags": {
                "Primary": "96bc3d572a66e162f9b1a8304edb4364"
            },
            "BackdropImageTags": [],
            "MediaType": "Audio"
        }
    ],
    "TotalRecordCount": 1
}
```

### Items 获取歌曲列表

GET: `[host]/Users/[UserId]/Items`

query:

| 参数名 | 备注 |
| --- | --- |
| SortBy | 排序方式列表，可选值: `Random`, `DateCreated`, `PremiereDate`, `PlayCount`, `DatePlayed`, `SortName`, `CommunityRating` |
| SortOrder | 排序，可选值: `Ascending`, `Descending` |
| IncludeItemTypes | 包含的项目类型，可选值：`Audio` |
| Recursive | 是否递归查询 |
| Fields | 包含的字段列表，可选值：`SortName`, `MediaSources`, `AudioInfo`, `DateCreated`, `ProductionYear` |
| ImageTypeLimit | 返回的每个图片类型图片数量 |
| EnableImageTypes | 图片类型列表，可选值：`Primary` |
| StartIndex | 起始行数 |
| Limit | 最大数量，可选 |
| ParentId | 父视图ID，可选 |
| GenreIds | 类型ID列表，可选 |
| isFavorite | 收藏状态，可选 |
| SearchTerm | 搜索词，可选 |

response:

```json
{
    "Items": [
        {
            "Name": "9420",
            "ServerId": "54068b26c84949dc809677381d1267a9",
            "Id": "50985",
            "DateCreated": "2021-11-27T08:31:24.0000000Z",
            "Container": "mp3",
            "SortName": "9420",
            "MediaSources": [
                {
                    "Protocol": "File",
                    "Id": "74ec19f32687018d22e64b9a41eb6336",
                    "Path": "/volume1/music/麦小兜/9420/9420.mp3",
                    "Type": "Default",
                    "Container": "mp3",
                    "Size": 9225558,
                    "Name": "9420",
                    "IsRemote": false,
                    "RunTimeTicks": 2291983670,
                    "SupportsTranscoding": true,
                    "SupportsDirectStream": true,
                    "SupportsDirectPlay": true,
                    "IsInfiniteStream": false,
                    "RequiresOpening": false,
                    "RequiresClosing": false,
                    "RequiresLooping": false,
                    "SupportsProbing": false,
                    "MediaStreams": [
                        {
                            "Codec": "mp3",
                            "TimeBase": "1/14112000",
                            "DisplayTitle": "Und MP3 stereo",
                            "IsInterlaced": false,
                            "ChannelLayout": "stereo",
                            "BitRate": 320000,
                            "Channels": 2,
                            "SampleRate": 44100,
                            "IsDefault": false,
                            "IsForced": false,
                            "Type": "Audio",
                            "Index": 0,
                            "IsExternal": false,
                            "IsTextSubtitleStream": false,
                            "SupportsExternalStream": false,
                            "Protocol": "File",
                            "AttachmentSize": 0
                        },
                        {
                            "Codec": "mjpeg",
                            "ColorSpace": "bt470bg",
                            "Comment": "Cover (front)",
                            "TimeBase": "1/90000",
                            "IsInterlaced": false,
                            "BitDepth": 8,
                            "RefFrames": 1,
                            "IsDefault": false,
                            "IsForced": false,
                            "Height": 600,
                            "Width": 600,
                            "RealFrameRate": 90000,
                            "Profile": "Baseline",
                            "Type": "EmbeddedImage",
                            "AspectRatio": "1:1",
                            "Index": 1,
                            "IsExternal": false,
                            "IsTextSubtitleStream": false,
                            "SupportsExternalStream": false,
                            "Protocol": "File",
                            "PixelFormat": "yuvj420p",
                            "Level": -99,
                            "IsAnamorphic": false,
                            "AttachmentSize": 0
                        },
                        {
                            "Codec": "text",
                            "Title": "Lyrics",
                            "Extradata": "[ti:9420]\n[ar:麦小兜]\n[al:9420]\n[00:00.00]9420 - 麦小兜\n[00:05.05]词：可泽\n[00:10.10]曲：可泽\n[00:15.15]编曲：杨栋梁\n[00:20.21]制作公司：Hikoon Music\n[00:25.26]手牵手一起走在幸福的大街\n[00:28.21]微风缓缓的吹来你我相依偎\n[00:31.15]爱的目光如此的热烈\n[00:34.97]\n[00:36.94]这份爱就像是在燃烧的火堆\n[00:39.95]炽热的火焰如同盛开的玫瑰\n[00:42.85]不管白天黑夜继续的沉醉\n[00:46.30]\n[00:47.59]整个世界弥漫\n[00:48.97]\n[00:49.47]薄荷般的气味\n[00:51.45]耳边\n[00:52.34]你的呢喃不停吹\n[00:54.20]所有\n[00:55.14]孤单寂寞 都被悄悄震碎\n[00:59.39]你的眼神就像\n[01:00.49]\n[01:01.08]流淌着的河水\n[01:02.94]流进\n[01:03.42]\n[01:04.01]我的身体润心扉\n[01:05.98]洗涤\n[01:06.95]所有悲伤烦恼带来安慰\n[01:11.08]关于我们\n[01:13.84]我只想说\n[01:16.68]简单一句\n[01:19.53]就是爱你\n[01:22.52]比翼双飞\n[01:25.41]金蝉做媒\n[01:28.26]天造地设的一对\n[01:33.61]\n[01:58.93]手牵手一起走在幸福的大街\n[02:01.91]微风缓缓的吹来你我相依偎\n[02:04.79]爱的目光如此的热烈\n[02:08.76]\n[02:10.76]这份爱就像是在燃烧的火堆\n[02:13.50]炽热的火焰如同盛开的玫瑰\n[02:16.51]不管白天黑夜继续的沉醉\n[02:20.08]\n[02:21.22]整个世界弥漫\n[02:23.12]薄荷般的气味\n[02:25.04]耳边\n[02:25.98]你的呢喃不停吹\n[02:27.90]所有\n[02:28.82]孤单寂寞都被悄悄震碎\n[02:32.96]你的眼神就像\n[02:34.71]流淌着的河水\n[02:36.69]流进\n[02:37.66]我的身体润心扉\n[02:39.57]洗涤\n[02:40.52]所有悲伤烦恼带来安慰\n[02:44.81]关于我们\n[02:47.45]我只想说\n[02:50.28]简单一句\n[02:53.16]就是爱你\n[02:56.07]比翼双飞\n[02:59.08]金蝉做媒\n[03:01.95]天造地设的一对\n[03:07.33]\n[03:08.08]关于我们\n[03:10.90]我只想说\n[03:13.80]简单一句\n[03:16.61]就是爱你\n[03:19.58]比翼双飞\n[03:22.56]金蝉做媒\n[03:25.48]天造地设的一对",
                            "DisplayTitle": "Und (TEXT)",
                            "IsInterlaced": false,
                            "IsDefault": false,
                            "IsForced": false,
                            "Type": "Subtitle",
                            "Index": 2,
                            "IsExternal": false,
                            "IsTextSubtitleStream": true,
                            "SupportsExternalStream": true,
                            "Protocol": "File",
                            "AttachmentSize": 0,
                            "SubtitleLocationType": "InternalStream"
                        }
                    ],
                    "Formats": [],
                    "Bitrate": 322011,
                    "RequiredHttpHeaders": {},
                    "ReadAtNativeFramerate": false,
                    "DefaultAudioStreamIndex": 0,
                    "DefaultSubtitleStreamIndex": 2
                }
            ],
            "RunTimeTicks": 2291983670,
            "Size": 9225558,
            "Bitrate": 322011,
            "ProductionYear": 2017,
            "IndexNumber": 1,
            "IsFolder": false,
            "Type": "Audio",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false
            },
            "Artists": [
                "麦小兜"
            ],
            "ArtistItems": [
                {
                    "Name": "麦小兜",
                    "Id": "7855"
                }
            ],
            "Composers": [],
            "Album": "9420",
            "AlbumId": "7856",
            "AlbumPrimaryImageTag": "605950b8b45c1dffe57a5c3d3870916a",
            "AlbumArtist": "麦小兜",
            "AlbumArtists": [
                {
                    "Name": "麦小兜",
                    "Id": "7855"
                }
            ],
            "ImageTags": {
                "Primary": "c36a54ac99a7ef10be9fc0626a1d502b"
            },
            "MediaType": "Audio"
        }
    ],
    "TotalRecordCount": 19408
}
```

### Items/[id] 获取歌曲信息

GET: `[host]/Users/[UserId]/Items/[id]`

response:

```json
{
    "Name": "艾里甫与赛乃姆",
    "ServerId": "54068b26c84949dc809677381d1267a9",
    "Id": "45902",
    "Etag": "06ffa98cf3145f04578fddcff6ee66f8",
    "DateCreated": "2023-07-28T11:12:06.0000000Z",
    "CanDelete": true,
    "CanDownload": true,
    "PresentationUniqueKey": "2578eaf86b158fd6b3a97034431faf41",
    "SupportsSync": true,
    "Container": "flac",
    "SortName": "艾里甫与赛乃姆",
    "ForcedSortName": "艾里甫与赛乃姆",
    "ExternalUrls": [],
    "MediaSources": [
        {
            "Protocol": "File",
            "Id": "2578eaf86b158fd6b3a97034431faf41",
            "Path": "/volume1/music/刀郎/2002年的第一场雪/刀郎 - 艾里甫与赛乃姆.flac",
            "Type": "Default",
            "Container": "flac",
            "Size": 43685853,
            "Name": "刀郎 - 艾里甫与赛乃姆",
            "IsRemote": false,
            "RunTimeTicks": 3525466670,
            "SupportsTranscoding": true,
            "SupportsDirectStream": true,
            "SupportsDirectPlay": true,
            "IsInfiniteStream": false,
            "RequiresOpening": false,
            "RequiresClosing": false,
            "RequiresLooping": false,
            "SupportsProbing": false,
            "MediaStreams": [
                {
                    "Codec": "flac",
                    "TimeBase": "1/44100",
                    "DisplayTitle": "Und FLAC stereo",
                    "IsInterlaced": false,
                    "ChannelLayout": "stereo",
                    "BitRate": 991320,
                    "BitDepth": 16,
                    "Channels": 2,
                    "SampleRate": 44100,
                    "IsDefault": false,
                    "IsForced": false,
                    "Type": "Audio",
                    "Index": 0,
                    "IsExternal": false,
                    "IsTextSubtitleStream": false,
                    "SupportsExternalStream": false,
                    "Protocol": "File",
                    "AttachmentSize": 0
                },
                {
                    "Codec": "mjpeg",
                    "ColorSpace": "bt470bg",
                    "Comment": "Other",
                    "TimeBase": "1/90000",
                    "IsInterlaced": false,
                    "BitDepth": 8,
                    "RefFrames": 1,
                    "IsDefault": false,
                    "IsForced": false,
                    "Height": 500,
                    "Width": 500,
                    "RealFrameRate": 90000,
                    "Profile": "Baseline",
                    "Type": "EmbeddedImage",
                    "AspectRatio": "1:1",
                    "Index": 1,
                    "IsExternal": false,
                    "IsTextSubtitleStream": false,
                    "SupportsExternalStream": false,
                    "Protocol": "File",
                    "PixelFormat": "yuvj444p",
                    "Level": -99,
                    "IsAnamorphic": false,
                    "AttachmentSize": 0
                },
                {
                    "Codec": "text",
                    "Title": "Lyrics",
                    "Extradata": "[ti:艾里甫与赛乃姆]\n[ar:刀郎]\n[al:2002年的第一场雪]\n[00:00.00]艾里甫与赛乃姆 - 刀郎\n[00:09.00]词：刀郎\n[00:18.00]曲：刀郎\n[00:27.01]从小和你青梅竹马相约在天山下\n[00:33.93]\n[00:37.12]我们本来是天底下最幸福的人啊\n[00:45.74]\n[00:47.01]赛乃姆你是花丛中最美的石榴花\n[00:55.17]\n[00:57.08]艾里甫我却是巴格达上孤独的阿卡\n[01:04.33]\n[01:09.60]夜莺歌声在每个夜晚都会陪伴她\n[01:16.54]\n[01:19.55]我的琴声却飘荡在遥远的巴格达\n[01:27.79]\n[01:29.68]为了爱情我被放逐在天涯\n[01:37.66]\n[01:39.60]莫非今生和你厮守变成了神话\n[01:46.73]\n[01:49.59]我寻遍天山南北我要找到你赛乃姆\n[01:58.17]\n[01:59.58]不管是跋山涉水历尽千辛万苦\n[02:08.10]\n[02:09.53]花园里种不出天山上的雪莲花\n[02:17.68]\n[02:19.56]不历经磨难我找不到今生的幸福\n[02:28.19]\n[02:55.80]夜莺歌声在每个夜晚都会陪伴她\n[03:02.66]\n[03:05.76]我的琴声却飘荡在遥远的巴格达\n[03:13.91]\n[03:15.86]为了爱情我被放逐在天涯\n[03:23.96]\n[03:25.90]莫非今生和你厮守变成了神话\n[03:33.10]\n[03:35.88]我寻遍天山南北我要找到你赛乃姆\n[03:44.28]\n[03:45.83]不管是跋山涉水历尽千辛万苦\n[03:54.33]\n[03:55.89]花园里种不出天山上的雪莲花\n[04:03.91]\n[04:05.87]不历经磨难我找不到今生的幸福\n[04:14.35]\n[04:17.24]我寻遍天山南北我要找到你赛乃姆\n[04:25.50]\n[04:26.91]不管是跋山涉水历尽千辛万苦\n[04:35.63]\n[04:37.16]花园里种不出天山上的雪莲花\n[04:45.17]\n[04:46.96]不历经磨难我找不到今生的幸福",
                    "DisplayTitle": "Und (TEXT)",
                    "IsInterlaced": false,
                    "IsDefault": false,
                    "IsForced": false,
                    "Type": "Subtitle",
                    "Index": 2,
                    "IsExternal": false,
                    "IsTextSubtitleStream": true,
                    "SupportsExternalStream": true,
                    "Protocol": "File",
                    "AttachmentSize": 0,
                    "SubtitleLocationType": "InternalStream"
                }
            ],
            "Formats": [],
            "Bitrate": 991320,
            "RequiredHttpHeaders": {},
            "ReadAtNativeFramerate": false,
            "DefaultAudioStreamIndex": 0,
            "DefaultSubtitleStreamIndex": 2
        }
    ],
    "Path": "/volume1/music/刀郎/2002年的第一场雪/刀郎 - 艾里甫与赛乃姆.flac",
    "Taglines": [],
    "Genres": [],
    "RunTimeTicks": 3525466670,
    "Size": 43685853,
    "FileName": "刀郎 - 艾里甫与赛乃姆.flac",
    "Bitrate": 991320,
    "PlayAccess": "Full",
    "ProductionYear": 2004,
    "IndexNumber": 5,
    "ParentIndexNumber": 1,
    "RemoteTrailers": [],
    "ProviderIds": {},
    "IsFolder": false,
    "ParentId": "45874",
    "Type": "Audio",
    "Studios": [],
    "GenreItems": [],
    "TagItems": [],
    "ParentBackdropItemId": "10126",
    "ParentBackdropImageTags": [
        "401cc5f81954801ecbcc6235ac18705b"
    ],
    "UserData": {
        "PlaybackPositionTicks": 0,
        "PlayCount": 1,
        "IsFavorite": false,
        "LastPlayedDate": "2024-04-19T14:29:46.0000000Z",
        "Played": true
    },
    "DisplayPreferencesId": "61bba315f137702baa296a1c417faada",
    "PrimaryImageAspectRatio": 1,
    "Artists": [
        "刀郎"
    ],
    "ArtistItems": [
        {
            "Name": "刀郎",
            "Id": "10126"
        }
    ],
    "Composers": [],
    "Album": "2002年的第一场雪",
    "AlbumId": "10139",
    "AlbumPrimaryImageTag": "0775ee34b85f766a6fc47fdf647b4bc4",
    "AlbumArtist": "刀郎",
    "AlbumArtists": [
        {
            "Name": "刀郎",
            "Id": "10126"
        }
    ],
    "MediaStreams": [
        {
            "Codec": "flac",
            "TimeBase": "1/44100",
            "DisplayTitle": "Und FLAC stereo",
            "IsInterlaced": false,
            "ChannelLayout": "stereo",
            "BitRate": 991320,
            "BitDepth": 16,
            "Channels": 2,
            "SampleRate": 44100,
            "IsDefault": false,
            "IsForced": false,
            "Type": "Audio",
            "Index": 0,
            "IsExternal": false,
            "IsTextSubtitleStream": false,
            "SupportsExternalStream": false,
            "Protocol": "File",
            "AttachmentSize": 0
        },
        {
            "Codec": "mjpeg",
            "ColorSpace": "bt470bg",
            "Comment": "Other",
            "TimeBase": "1/90000",
            "IsInterlaced": false,
            "BitDepth": 8,
            "RefFrames": 1,
            "IsDefault": false,
            "IsForced": false,
            "Height": 500,
            "Width": 500,
            "RealFrameRate": 90000,
            "Profile": "Baseline",
            "Type": "EmbeddedImage",
            "AspectRatio": "1:1",
            "Index": 1,
            "IsExternal": false,
            "IsTextSubtitleStream": false,
            "SupportsExternalStream": false,
            "Protocol": "File",
            "PixelFormat": "yuvj444p",
            "Level": -99,
            "IsAnamorphic": false,
            "AttachmentSize": 0
        },
        {
            "Codec": "text",
            "Title": "Lyrics",
            "Extradata": "[ti:艾里甫与赛乃姆]\n[ar:刀郎]\n[al:2002年的第一场雪]\n[00:00.00]艾里甫与赛乃姆 - 刀郎\n[00:09.00]词：刀郎\n[00:18.00]曲：刀郎\n[00:27.01]从小和你青梅竹马相约在天山下\n[00:33.93]\n[00:37.12]我们本来是天底下最幸福的人啊\n[00:45.74]\n[00:47.01]赛乃姆你是花丛中最美的石榴花\n[00:55.17]\n[00:57.08]艾里甫我却是巴格达上孤独的阿卡\n[01:04.33]\n[01:09.60]夜莺歌声在每个夜晚都会陪伴她\n[01:16.54]\n[01:19.55]我的琴声却飘荡在遥远的巴格达\n[01:27.79]\n[01:29.68]为了爱情我被放逐在天涯\n[01:37.66]\n[01:39.60]莫非今生和你厮守变成了神话\n[01:46.73]\n[01:49.59]我寻遍天山南北我要找到你赛乃姆\n[01:58.17]\n[01:59.58]不管是跋山涉水历尽千辛万苦\n[02:08.10]\n[02:09.53]花园里种不出天山上的雪莲花\n[02:17.68]\n[02:19.56]不历经磨难我找不到今生的幸福\n[02:28.19]\n[02:55.80]夜莺歌声在每个夜晚都会陪伴她\n[03:02.66]\n[03:05.76]我的琴声却飘荡在遥远的巴格达\n[03:13.91]\n[03:15.86]为了爱情我被放逐在天涯\n[03:23.96]\n[03:25.90]莫非今生和你厮守变成了神话\n[03:33.10]\n[03:35.88]我寻遍天山南北我要找到你赛乃姆\n[03:44.28]\n[03:45.83]不管是跋山涉水历尽千辛万苦\n[03:54.33]\n[03:55.89]花园里种不出天山上的雪莲花\n[04:03.91]\n[04:05.87]不历经磨难我找不到今生的幸福\n[04:14.35]\n[04:17.24]我寻遍天山南北我要找到你赛乃姆\n[04:25.50]\n[04:26.91]不管是跋山涉水历尽千辛万苦\n[04:35.63]\n[04:37.16]花园里种不出天山上的雪莲花\n[04:45.17]\n[04:46.96]不历经磨难我找不到今生的幸福",
            "DisplayTitle": "Und (TEXT)",
            "IsInterlaced": false,
            "IsDefault": false,
            "IsForced": false,
            "Type": "Subtitle",
            "Index": 2,
            "IsExternal": false,
            "IsTextSubtitleStream": true,
            "SupportsExternalStream": true,
            "Protocol": "File",
            "AttachmentSize": 0,
            "SubtitleLocationType": "InternalStream"
        }
    ],
    "ImageTags": {
        "Primary": "d236a8e730c9c4b54e2a9c4a4c7be5df"
    },
    "BackdropImageTags": [],
    "MediaType": "Audio",
    "LockedFields": [],
    "LockData": false
}
```

### Items 获取专辑中的歌曲

参见 Jellyfin 的 [Items](jellyfin#items-获取专辑中的歌曲) 接口。

### Items 获取歌手名下歌曲

参见 Jellyfin 的 [Items](jellyfin#items-获取歌手名下歌曲) 接口。

### Items 获取歌单中的歌曲

GET: `[host]/Users/[UserId]/Items`

query:

| 参数名 | 备注 |
| --- | --- |
| SortBy | 排序方式列表，可选值: `ListItemOrder`, `SortName`, `Album,ParentIndexNumber,IndexNumber`, `Artist,Album,ParentIndexNumber,IndexNumber,SortName` |
| SortOrder | 排序，可选值: `Ascending`, `Descending` |
| Fields | 包含的字段列表，可选值：`PrimaryImageAspectRatio`, `MediaSources`, `AudioInfo`, `DateCreated`, `ProductionYear` |
| ImageTypeLimit | 返回的每个图片类型图片数量 |
| StartIndex | 起始行数 |
| Limit | 最大数量，可选 |
| ParentId | 歌单ID |

response:

```json
{
    "Items": [
        {
            "Name": "9420",
            "ServerId": "54068b26c84949dc809677381d1267a9",
            "Id": "50985",
            "DateCreated": "2021-11-27T08:31:24.0000000Z",
            "Container": "mp3",
            "SortName": "9420",
            "MediaSources": [
                {
                    "Protocol": "File",
                    "Id": "74ec19f32687018d22e64b9a41eb6336",
                    "Path": "/volume1/music/麦小兜/9420/9420.mp3",
                    "Type": "Default",
                    "Container": "mp3",
                    "Size": 9225558,
                    "Name": "9420",
                    "IsRemote": false,
                    "RunTimeTicks": 2291983670,
                    "SupportsTranscoding": true,
                    "SupportsDirectStream": true,
                    "SupportsDirectPlay": true,
                    "IsInfiniteStream": false,
                    "RequiresOpening": false,
                    "RequiresClosing": false,
                    "RequiresLooping": false,
                    "SupportsProbing": false,
                    "MediaStreams": [
                        {
                            "Codec": "mp3",
                            "TimeBase": "1/14112000",
                            "DisplayTitle": "Und MP3 stereo",
                            "IsInterlaced": false,
                            "ChannelLayout": "stereo",
                            "BitRate": 320000,
                            "Channels": 2,
                            "SampleRate": 44100,
                            "IsDefault": false,
                            "IsForced": false,
                            "Type": "Audio",
                            "Index": 0,
                            "IsExternal": false,
                            "IsTextSubtitleStream": false,
                            "SupportsExternalStream": false,
                            "Protocol": "File",
                            "AttachmentSize": 0
                        },
                        {
                            "Codec": "mjpeg",
                            "ColorSpace": "bt470bg",
                            "Comment": "Cover (front)",
                            "TimeBase": "1/90000",
                            "IsInterlaced": false,
                            "BitDepth": 8,
                            "RefFrames": 1,
                            "IsDefault": false,
                            "IsForced": false,
                            "Height": 600,
                            "Width": 600,
                            "RealFrameRate": 90000,
                            "Profile": "Baseline",
                            "Type": "EmbeddedImage",
                            "AspectRatio": "1:1",
                            "Index": 1,
                            "IsExternal": false,
                            "IsTextSubtitleStream": false,
                            "SupportsExternalStream": false,
                            "Protocol": "File",
                            "PixelFormat": "yuvj420p",
                            "Level": -99,
                            "IsAnamorphic": false,
                            "AttachmentSize": 0
                        },
                        {
                            "Codec": "text",
                            "Title": "Lyrics",
                            "Extradata": "[ti:9420]\n[ar:麦小兜]\n[al:9420]\n[00:00.00]9420 - 麦小兜\n[00:05.05]词：可泽\n[00:10.10]曲：可泽\n[00:15.15]编曲：杨栋梁\n[00:20.21]制作公司：Hikoon Music\n[00:25.26]手牵手一起走在幸福的大街\n[00:28.21]微风缓缓的吹来你我相依偎\n[00:31.15]爱的目光如此的热烈\n[00:34.97]\n[00:36.94]这份爱就像是在燃烧的火堆\n[00:39.95]炽热的火焰如同盛开的玫瑰\n[00:42.85]不管白天黑夜继续的沉醉\n[00:46.30]\n[00:47.59]整个世界弥漫\n[00:48.97]\n[00:49.47]薄荷般的气味\n[00:51.45]耳边\n[00:52.34]你的呢喃不停吹\n[00:54.20]所有\n[00:55.14]孤单寂寞 都被悄悄震碎\n[00:59.39]你的眼神就像\n[01:00.49]\n[01:01.08]流淌着的河水\n[01:02.94]流进\n[01:03.42]\n[01:04.01]我的身体润心扉\n[01:05.98]洗涤\n[01:06.95]所有悲伤烦恼带来安慰\n[01:11.08]关于我们\n[01:13.84]我只想说\n[01:16.68]简单一句\n[01:19.53]就是爱你\n[01:22.52]比翼双飞\n[01:25.41]金蝉做媒\n[01:28.26]天造地设的一对\n[01:33.61]\n[01:58.93]手牵手一起走在幸福的大街\n[02:01.91]微风缓缓的吹来你我相依偎\n[02:04.79]爱的目光如此的热烈\n[02:08.76]\n[02:10.76]这份爱就像是在燃烧的火堆\n[02:13.50]炽热的火焰如同盛开的玫瑰\n[02:16.51]不管白天黑夜继续的沉醉\n[02:20.08]\n[02:21.22]整个世界弥漫\n[02:23.12]薄荷般的气味\n[02:25.04]耳边\n[02:25.98]你的呢喃不停吹\n[02:27.90]所有\n[02:28.82]孤单寂寞都被悄悄震碎\n[02:32.96]你的眼神就像\n[02:34.71]流淌着的河水\n[02:36.69]流进\n[02:37.66]我的身体润心扉\n[02:39.57]洗涤\n[02:40.52]所有悲伤烦恼带来安慰\n[02:44.81]关于我们\n[02:47.45]我只想说\n[02:50.28]简单一句\n[02:53.16]就是爱你\n[02:56.07]比翼双飞\n[02:59.08]金蝉做媒\n[03:01.95]天造地设的一对\n[03:07.33]\n[03:08.08]关于我们\n[03:10.90]我只想说\n[03:13.80]简单一句\n[03:16.61]就是爱你\n[03:19.58]比翼双飞\n[03:22.56]金蝉做媒\n[03:25.48]天造地设的一对",
                            "DisplayTitle": "Und (TEXT)",
                            "IsInterlaced": false,
                            "IsDefault": false,
                            "IsForced": false,
                            "Type": "Subtitle",
                            "Index": 2,
                            "IsExternal": false,
                            "IsTextSubtitleStream": true,
                            "SupportsExternalStream": true,
                            "Protocol": "File",
                            "AttachmentSize": 0,
                            "SubtitleLocationType": "InternalStream"
                        }
                    ],
                    "Formats": [],
                    "Bitrate": 322011,
                    "RequiredHttpHeaders": {},
                    "ReadAtNativeFramerate": false,
                    "DefaultAudioStreamIndex": 0,
                    "DefaultSubtitleStreamIndex": 2
                }
            ],
            "RunTimeTicks": 2291983670,
            "Size": 9225558,
            "Bitrate": 322011,
            "ProductionYear": 2017,
            "IndexNumber": 1,
            "IsFolder": false,
            "Type": "Audio",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false
            },
            "Artists": [
                "麦小兜"
            ],
            "ArtistItems": [
                {
                    "Name": "麦小兜",
                    "Id": "7855"
                }
            ],
            "Composers": [],
            "Album": "9420",
            "AlbumId": "7856",
            "AlbumPrimaryImageTag": "605950b8b45c1dffe57a5c3d3870916a",
            "AlbumArtist": "麦小兜",
            "AlbumArtists": [
                {
                    "Name": "麦小兜",
                    "Id": "7855"
                }
            ],
            "ImageTags": {
                "Primary": "c36a54ac99a7ef10be9fc0626a1d502b"
            },
            "MediaType": "Audio"
        }
    ],
    "TotalRecordCount": 19408
}
```

### FavoriteItems/[id] 收藏歌曲/专辑/歌手

POST: `[host]/Users/[UserId]/FavoriteItems/[id]`

### stream 歌曲播放链接

GET: `[host]/Audio/[id]/stream`

query:

| 参数名 | 备注 |
| --- | --- |
| static | 是否转码，不转码时填写 |
| audioCodec | 格式，可选值：`mp3`, `aac` |
| audioBitRate | 比特率，转码时填写 |

:::note

请求头需要携带授权信息。

:::

### FavoriteItems[id] 取消收藏

DELETE: `[host]/Users/[UserId]/FavoriteItems/[id]`

### Items 添加歌曲到歌单

POST: `[host]/Playlists/[id]/Items`

query:

| 参数名 | 备注 |
| --- | --- |
| Ids | 歌曲ID列表 |
| UserId | 用户ID |

response code: 204

### Items 从歌单中移除歌曲

DELETE: `[host]/Playlists/[id]/Items`

query:

| 参数名 | 备注 |
| --- | --- |
| entryIds | 歌曲ID列表 |

response code: 204

### Items/[id] 修改歌单信息

POST: `[host]/Items/[id]`

body(`application/json`):

| 参数名 | 备注 |
| --- | --- |
| Name | 歌单名 |
| Id | 歌单ID |

response code: 204