---
sidebar_position: 3
---

# Jellyfin 接口文档

:::note 参考文档：

- [Jellyfin API](https://api.jellyfin.org/)

:::

## 认证

### AuthenticateByName 登录

POST: `[host]/Users/AuthenticateByName`

body(`application/json`):

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| Username | Y | | 用户名 |
| Pw | Y | | 密码 |

response:

```json
{
    "User": {
        "Name": "username",
        "ServerId": "68ca97fexxxf41a08axxxf3d057a5f75",
        "Id": "cb70exxx1bxxx96ab14xxx6151ba2250",
        "HasPassword": true,
        "HasConfiguredPassword": true,
        "HasConfiguredEasyPassword": false,
        "EnableAutoLogin": false,
        "LastLoginDate": "2024-04-19T02:51:02.6245939Z",
        "LastActivityDate": "2024-04-19T02:51:02.6245939Z",
        "Configuration": {
            "PlayDefaultAudioTrack": true,
            "SubtitleLanguagePreference": "",
            "DisplayMissingEpisodes": false,
            "GroupedFolders": [],
            "SubtitleMode": "Default",
            "DisplayCollectionsView": false,
            "EnableLocalPassword": false,
            "OrderedViews": [],
            "LatestItemsExcludes": [],
            "MyMediaExcludes": [],
            "HidePlayedInLatest": true,
            "RememberAudioSelections": true,
            "RememberSubtitleSelections": true,
            "EnableNextEpisodeAutoPlay": true
        },
        "Policy": {
            "IsAdministrator": true,
            "IsHidden": true,
            "IsDisabled": false,
            "BlockedTags": [],
            "EnableUserPreferenceAccess": true,
            "AccessSchedules": [],
            "BlockUnratedItems": [],
            "EnableRemoteControlOfOtherUsers": true,
            "EnableSharedDeviceControl": true,
            "EnableRemoteAccess": true,
            "EnableLiveTvManagement": true,
            "EnableLiveTvAccess": true,
            "EnableMediaPlayback": true,
            "EnableAudioPlaybackTranscoding": true,
            "EnableVideoPlaybackTranscoding": true,
            "EnablePlaybackRemuxing": true,
            "ForceRemoteSourceTranscoding": false,
            "EnableContentDeletion": true,
            "EnableContentDeletionFromFolders": [],
            "EnableContentDownloading": true,
            "EnableSyncTranscoding": true,
            "EnableMediaConversion": true,
            "EnabledDevices": [],
            "EnableAllDevices": true,
            "EnabledChannels": [],
            "EnableAllChannels": true,
            "EnabledFolders": [],
            "EnableAllFolders": true,
            "InvalidLoginAttemptCount": 0,
            "LoginAttemptsBeforeLockout": -1,
            "MaxActiveSessions": 0,
            "EnablePublicSharing": true,
            "BlockedMediaFolders": [],
            "BlockedChannels": [],
            "RemoteClientBitrateLimit": 0,
            "AuthenticationProviderId": "Jellyfin.Server.Implementations.Users.DefaultAuthenticationProvider",
            "PasswordResetProviderId": "Jellyfin.Server.Implementations.Users.DefaultPasswordResetProvider",
            "SyncPlayAccess": "CreateAndJoinGroups"
        }
    },
    "SessionInfo": {
        "PlayState": {
            "CanSeek": false,
            "IsPaused": false,
            "IsMuted": false,
            "RepeatMode": "RepeatNone"
        },
        "AdditionalUsers": [],
        "Capabilities": {
            "PlayableMediaTypes": [],
            "SupportedCommands": [],
            "SupportsMediaControl": false,
            "SupportsContentUploading": false,
            "SupportsPersistentIdentifier": true,
            "SupportsSync": false
        },
        "RemoteEndPoint": "172.27.0.1",
        "PlayableMediaTypes": [],
        "Id": "15fffxxxd3fxxx30cca43f59fbe23e5b",
        "UserId": "cb70eae21b42496ab14xxx6151xxx250",
        "UserName": "username",
        "Client": "StreamMusicTest",
        "LastActivityDate": "2024-04-19T02:51:02.8736846Z",
        "LastPlaybackCheckIn": "0001-01-01T00:00:00.0000000Z",
        "DeviceName": "MBP",
        "DeviceId": "6tgrf7a0qwcfrxxx3bxka0vb",
        "ApplicationVersion": "1.2.6",
        "IsActive": true,
        "SupportsMediaControl": false,
        "SupportsRemoteControl": false,
        "NowPlayingQueue": [],
        "NowPlayingQueueFullItems": [],
        "HasCustomDeviceName": false,
        "ServerId": "68ca97fe91ff41xxxaa2xxxd057a5f75",
        "SupportedCommands": []
    },
    "AccessToken": "602f3582cxxx4d2xxx83d920ad606e22",
    "ServerId": "68ca97fe91fxxxx08aaxxx3d057a5f75"
}
```

在后续的请求中，需要携带以下参数：

| 参数名 | 备注 |
| --- | --- |
| MediaBrowser Client | 客户端名称 |
| Device | 设备名 |
| DeviceId | 设备Id |
| Version | 客户端版本号 |
| Token | 访问令牌，登录后从响应中的 `AccessToken` 字段获取 |

最后，将以上参数组装起来放在请求头中：

`Authorization: MediaBrowser Client="$clientName", Device="$deviceName", DeviceId="$deviceId", Version="$clientVersion"`

:::tip

响应中的 `User.Id` 在后续很多请求中都有用到，建议登录后保存一下。

:::

### Ping 测试服务器连通性

GET: `[host]/System/Ping`

## 请求节点

### Items 获取专辑列表

GET: `[host]/Users/[UserId]/Items`

query:

| 参数名 | 备注 |
| --- | --- |
| GenreIds | 类型ID，可选 |
| SortBy | 排序方式列表，可选值: `Random`, `DateCreated`, `PremiereDate`, `PlayCount`, `DatePlayed`, `SortName`, `CommunityRating` |
| SortOrder | 排序，可选值: `Ascending`, `Descending` |
| IncludeItemTypes | 包含的项目类型，可选值：`MusicAlbum` |
| Recursive | 是否递归查询 |
| Fields | 包含的字段列表，可选值：`SortName`, `BasicSyncInfo`, `ChildCount`, `DateCreated` |
| ImageTypeLimit | 返回的每个图片类型图片数量 |
| EnableImageTypes | 图片类型列表，可选值：`Primary`, `Backdrop`, `Banner`, `Thumb` |
| StartIndex | 起始行数 |
| Limit | 最大数量，可选 |
| artistIds | 歌手 id 列表，可选 |
| SearchTerm | 搜索词，可选 |

response:

```json
{
    "Items": [
        {
            "Name": "飞驰于你",
            "ServerId": "68ca97fe91ff41a08aa2ff3d057a5f75",
            "Id": "bb725906dce0e1d5dcbb5e2aab50f590",
            "DateCreated": "2024-03-25T09:34:11.7249608Z",
            "SortName": "飞驰于你",
            "PremiereDate": "2018-01-01T00:00:00.0000000Z",
            "ChannelId": null,
            "RunTimeTicks": 2441376768,
            "ProductionYear": 2018,
            "IsFolder": true,
            "Type": "MusicAlbum",
            "ParentBackdropItemId": "9cb24036603a4bbdaf15891d3f8215b0",
            "ParentBackdropImageTags": [
                "17c8f1f8c484ca3f6f9dee5102176e1e"
            ],
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false,
                "Key": "bb725906-dce0-e1d5-dcbb-5e2aab50f590"
            },
            "ChildCount": 1,
            "Artists": [
                "许嵩"
            ],
            "ArtistItems": [
                {
                    "Name": "许嵩",
                    "Id": "9cb24036603a4bbdaf15891d3f8215b0"
                }
            ],
            "AlbumArtist": "许嵩",
            "AlbumArtists": [
                {
                    "Name": "许嵩",
                    "Id": "9cb24036603a4bbdaf15891d3f8215b0"
                }
            ],
            "ImageTags": {
                "Primary": "b9a921b8a933b371c1075b3c9d046352"
            },
            "BackdropImageTags": [],
            "ImageBlurHashes": {
                "Primary": {
                    "b9a921b8a933b371c1075b3c9d046352": "eH9QXCRj0K%M?HD%oe-;RkIUE2of$*NFNHt7ayR*ofs.%2ayIoofxa"
                },
                "Backdrop": {
                    "17c8f1f8c484ca3f6f9dee5102176e1e": "WTHetT_3.9?bjFt8%hRPofWBRit70L9FMwRjozM{-;IUjZayWXt7"
                }
            },
            "LocationType": "FileSystem"
        }
    ],
    "TotalRecordCount": 42,
    "StartIndex": 0
}
```

### Items/[id] 获取专辑信息

GET: `[host]/Users/[UserId]/Items/[id]`

response:

```json
{
    "Name": "飞驰于你",
    "ServerId": "68ca97fe91ff41a08aa2ff3d057a5f75",
    "Id": "bb725906dce0e1d5dcbb5e2aab50f590",
    "Etag": "2d38f05eeaa5ac3b0afb97617bc7f30d",
    "DateCreated": "2024-03-25T09:34:11.7249608Z",
    "CanDelete": true,
    "CanDownload": false,
    "SortName": "飞驰于你",
    "PremiereDate": "2018-01-01T00:00:00.0000000Z",
    "ExternalUrls": [],
    "Path": "/media/许嵩/飞驰于你",
    "EnableMediaSourceDisplay": true,
    "ChannelId": null,
    "Taglines": [],
    "Genres": [],
    "CumulativeRunTimeTicks": 2441376768,
    "RunTimeTicks": 2441376768,
    "PlayAccess": "Full",
    "ProductionYear": 2018,
    "RemoteTrailers": [],
    "ProviderIds": {},
    "IsFolder": true,
    "ParentId": "e630c2b62934f5dbab323976e997f90c",
    "Type": "MusicAlbum",
    "People": [],
    "Studios": [],
    "GenreItems": [],
    "ParentBackdropItemId": "9cb24036603a4bbdaf15891d3f8215b0",
    "ParentBackdropImageTags": [
        "17c8f1f8c484ca3f6f9dee5102176e1e"
    ],
    "LocalTrailerCount": 0,
    "UserData": {
        "PlaybackPositionTicks": 0,
        "PlayCount": 0,
        "IsFavorite": false,
        "Played": false,
        "Key": "bb725906-dce0-e1d5-dcbb-5e2aab50f590"
    },
    "RecursiveItemCount": 1,
    "ChildCount": 1,
    "SpecialFeatureCount": 0,
    "DisplayPreferencesId": "f13d7f51d4f1f8b6fcd620855eb88c1e",
    "Tags": [],
    "PrimaryImageAspectRatio": 1,
    "Artists": [
        "许嵩"
    ],
    "ArtistItems": [
        {
            "Name": "许嵩",
            "Id": "9cb24036603a4bbdaf15891d3f8215b0"
        }
    ],
    "AlbumArtist": "许嵩",
    "AlbumArtists": [
        {
            "Name": "许嵩",
            "Id": "9cb24036603a4bbdaf15891d3f8215b0"
        }
    ],
    "ImageTags": {
        "Primary": "b9a921b8a933b371c1075b3c9d046352"
    },
    "BackdropImageTags": [],
    "ImageBlurHashes": {
        "Primary": {
            "b9a921b8a933b371c1075b3c9d046352": "eH9QXCRj0K%M?HD%oe-;RkIUE2of$*NFNHt7ayR*ofs.%2ayIoofxa"
        },
        "Backdrop": {
            "17c8f1f8c484ca3f6f9dee5102176e1e": "WTHetT_3.9?bjFt8%hRPofWBRit70L9FMwRjozM{-;IUjZayWXt7"
        }
    },
    "LocationType": "FileSystem",
    "LockedFields": [],
    "LockData": false
}
```

### Artists 获取歌手列表

GET: `[host]/Artists`

query:

| 参数名 | 备注 |
| --- | --- |
| SortBy | 排序方式列表，可选值: `Random`, `DateCreated`, `PremiereDate`, `PlayCount`, `DatePlayed`, `SortName`, `CommunityRating` |
| SortOrder | 排序，可选值: `Ascending`, `Descending` |
| Recursive | 是否递归查询 |
| Fields | 包含的字段列表，可选值：`SortName`, `BasicSyncInfo`, `PrimaryImageAspectRatio` |
| ImageTypeLimit | 返回的每个图片类型图片数量 |
| EnableImageTypes | 图片类型列表，可选值：`Primary`, `Backdrop`, `Banner`, `Thumb` |
| StartIndex | 起始行数 |
| Limit | 最大数量，可选 |
| userId | 用户ID |
| SearchTerm | 搜索词，可选 |

response:

```json
{
    "Items": [
        {
            "Name": "许嵩",
            "ServerId": "68ca97fe91ff41a08aa2ff3d057a5f75",
            "Id": "9cb24036603a4bbdaf15891d3f8215b0",
            "SortName": "许嵩",
            "ChannelId": null,
            "RunTimeTicks": 47480836096,
            "Type": "MusicArtist",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": true,
                "Played": false,
                "Key": "Artist-Musicbrainz-ca084e75-0f3e-4c05-9f4d-b2714a8c8bb5"
            },
            "PrimaryImageAspectRatio": 1,
            "ImageTags": {
                "Primary": "cd6cc0deefafccfc624ae98786cbcf89"
            },
            "BackdropImageTags": [
                "17c8f1f8c484ca3f6f9dee5102176e1e"
            ],
            "ImageBlurHashes": {
                "Backdrop": {
                    "17c8f1f8c484ca3f6f9dee5102176e1e": "WTHetT_3.9?bjFt8%hRPofWBRit70L9FMwRjozM{-;IUjZayWXt7"
                },
                "Primary": {
                    "cd6cc0deefafccfc624ae98786cbcf89": "eIFE.a-:^6IAxZ56E1.7-;t7snV@RkbHX8~CtRV[RPE1NGaekCxtt7"
                }
            },
            "LocationType": "FileSystem"
        }
    ],
    "TotalRecordCount": 1,
    "StartIndex": 0
}
```

### Items/[id] 获取歌手信息

GET: `[host]/Users/[UserId]/Items/[id]`

response:

```json
{
    "Name": "许嵩",
    "ServerId": "68ca97fe91ff41a08aa2ff3d057a5f75",
    "Id": "9cb24036603a4bbdaf15891d3f8215b0",
    "Etag": "5c8277637eb996c93c816e3b637b92f2",
    "DateCreated": "2024-03-31T00:53:11.0325164Z",
    "CanDelete": false,
    "CanDownload": false,
    "SortName": "许嵩",
    "ExternalUrls": [
        {
            "Name": "MusicBrainz",
            "Url": "https://musicbrainz.org/artist/ca084e75-0f3e-4c05-9f4d-b2714a8c8bb5"
        }
    ],
    "Path": "/config/metadata/artists/许嵩",
    "EnableMediaSourceDisplay": true,
    "ChannelId": null,
    "Taglines": [],
    "Genres": [],
    "RunTimeTicks": 47480834304,
    "PlayAccess": "Full",
    "RemoteTrailers": [],
    "ProviderIds": {
        "MusicBrainzArtist": "ca084e75-0f3e-4c05-9f4d-b2714a8c8bb5"
    },
    "ParentId": null,
    "Type": "MusicArtist",
    "People": [],
    "Studios": [],
    "GenreItems": [],
    "LocalTrailerCount": 0,
    "UserData": {
        "PlaybackPositionTicks": 0,
        "PlayCount": 0,
        "IsFavorite": true,
        "Played": false,
        "Key": "Artist-Musicbrainz-ca084e75-0f3e-4c05-9f4d-b2714a8c8bb5"
    },
    "ChildCount": 174,
    "SpecialFeatureCount": 0,
    "DisplayPreferencesId": "184fdd0115d1192d2c763ca9df5e4ccc",
    "Tags": [],
    "PrimaryImageAspectRatio": 1,
    "ImageTags": {
        "Primary": "cd6cc0deefafccfc624ae98786cbcf89"
    },
    "BackdropImageTags": [
        "17c8f1f8c484ca3f6f9dee5102176e1e"
    ],
    "ImageBlurHashes": {
        "Backdrop": {
            "17c8f1f8c484ca3f6f9dee5102176e1e": "WTHetT_3.9?bjFt8%hRPofWBRit70L9FMwRjozM{-;IUjZayWXt7"
        },
        "Primary": {
            "cd6cc0deefafccfc624ae98786cbcf89": "eIFE.a-:^6IAxZ56E1.7-;t7snV@RkbHX8~CtRV[RPE1NGaekCxtt7"
        }
    },
    "LocationType": "FileSystem",
    "LockedFields": [],
    "SongCount": 132,
    "AlbumCount": 42,
    "MusicVideoCount": 0,
    "LockData": false
}
```

### Similar 获取相似歌手

GET: `[host]/Artists/[id]/Similar`

query:

| 参数名 | 备注 |
| --- | --- |
| limit | 结果数量 |
| Fields | 包含的字段列表，可选值：`SortName`, `BasicSyncInfo`, `PrimaryImageAspectRatio`, `Overview` |

response:

```json
{
    "Items": [],
    "TotalRecordCount": 0,
    "StartIndex": 0
}
```

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
| Ids | 包含的歌曲ID列表 |
| UserId | 用户名 |
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

### Genres 获取全部类型

GET: `[host]/Genres`

query:

| 参数名 | 备注 |
| --- | --- |
| ParentId | 28e9960207c978c0d9aaefc8ae2d3a79 |
| Recursive | 是否递归查询 |
| userId | 用户ID |
| StartIndex | 起始行数 |
| SortBy | 固定值，`SortName` |
| SortOrder | 固定值，`Ascending` |
| Fields | 结果内容，`PrimaryImageAspectRatio,ItemCounts` |

response:

```json
{
    "Items": [
        {
            "Name": "Blues",
            "ServerId": "9c37aa3250ca4fdcaefd7c5d527c4dc9",
            "Id": "df8727bc10d9300f2539c1ade11bca86",
            "ChannelId": null,
            "Type": "MusicGenre",
            "PrimaryImageAspectRatio": 1,
            "ImageTags": {
                "Primary": "a9cce81ed92265900007e40efc6f103f"
            },
            "BackdropImageTags": [],
            "ImageBlurHashes": {
                "Primary": {
                    "a9cce81ed92265900007e40efc6f103f": "eDB|4@_2%MWs0L?G?axut8-;s;ogfQRjRP4oNGWBax%M9aWBj[xu-o"
                }
            },
            "LocationType": "FileSystem",
            "MediaType": "Unknown"
        },
        {
            "Name": "General Chinese Pop",
            "ServerId": "9c37aa3250ca4fdcaefd7c5d527c4dc9",
            "Id": "db26524cecf61e7877ca36a7ce56e977",
            "ChannelId": null,
            "Type": "MusicGenre",
            "PrimaryImageAspectRatio": 1,
            "ImageTags": {
                "Primary": "76ead409c6e0e1a6b4aca1b68c3a9f97"
            },
            "BackdropImageTags": [],
            "ImageBlurHashes": {
                "Primary": {
                    "76ead409c6e0e1a6b4aca1b68c3a9f97": "euH_f9RjfQM{of?HayfQWBoffQfQfQfQfQ~WWBfQRkt7%MoffQt7j["
                }
            },
            "LocationType": "FileSystem",
            "MediaType": "Unknown"
        },
        {
            "Name": "国语流行",
            "ServerId": "9c37aa3250ca4fdcaefd7c5d527c4dc9",
            "Id": "eb1c5035435d9cdae1b1e707b5b10d3e",
            "ChannelId": null,
            "Type": "MusicGenre",
            "PrimaryImageAspectRatio": 1,
            "ImageTags": {
                "Primary": "b7f4de3edc193f2ed8828cb8723207ae"
            },
            "BackdropImageTags": [],
            "ImageBlurHashes": {
                "Primary": {
                    "b7f4de3edc193f2ed8828cb8723207ae": "eMP72#D*fQ01~pj[azfQj[RjfQfQfQfQfQWBfQfQofM{odt7fQxuoy"
                }
            },
            "LocationType": "FileSystem",
            "MediaType": "Unknown"
        },
        {
            "Name": "Pop",
            "ServerId": "9c37aa3250ca4fdcaefd7c5d527c4dc9",
            "Id": "f1f202f389018ad2c0766af4b0fcb155",
            "ChannelId": null,
            "Type": "MusicGenre",
            "PrimaryImageAspectRatio": 1,
            "ImageTags": {
                "Primary": "b1b7f3253c1eb7961d690e50119fffe2"
            },
            "BackdropImageTags": [],
            "ImageBlurHashes": {
                "Primary": {
                    "b1b7f3253c1eb7961d690e50119fffe2": "ecJi^ENHfQEM0g=|oefQt6EL9bt6fQ\u001a|k7azfQafn+WCayfQafxa"
                }
            },
            "LocationType": "FileSystem",
            "MediaType": "Unknown"
        },
        {
            "Name": "R&B",
            "ServerId": "9c37aa3250ca4fdcaefd7c5d527c4dc9",
            "Id": "d2b41a81a1122b14418c423b2f3616e9",
            "ChannelId": null,
            "Type": "MusicGenre",
            "PrimaryImageAspectRatio": 1,
            "ImageTags": {
                "Primary": "8b1af59966f74172e8c53872d75450f2"
            },
            "BackdropImageTags": [],
            "ImageBlurHashes": {
                "Primary": {
                    "8b1af59966f74172e8c53872d75450f2": "eCDc8ZI[%2x]0fxCxWE1R*IotRx]-;-:xuD*s:IU-oof%gt8t7%gxD"
                }
            },
            "LocationType": "FileSystem",
            "MediaType": "Unknown"
        }
    ],
    "TotalRecordCount": 5,
    "StartIndex": 0
}
```

### Lyrics 获取歌词

GET: `[host]/Audio/[id]/Lyrics`

response:

```json
{
    "Metadata": {},
    "Lyrics": [
        {
            "Text": "作词 : G.E.M.邓紫棋",
            "Start": 0
        },
        {
            "Text": "作曲 : DEE.P/JOHNSON REBECCA ROSE/TE DI/SOL",
            "Start": 10000000
        },
        {
            "Text": "编曲：Lupo Groinig",
            "Start": 43100000
        },
        {
            "Text": "监制：Lupo Groinig",
            "Start": 53100000
        },
        {
            "Text": "说不出说不出一句话",
            "Start": 137300000
        },
        {
            "Text": "连我自己都很惊讶",
            "Start": 163500000
        },
        {
            "Text": "这死去的爱",
            "Start": 2629600000
        }
    ]
}
```

### Items 获取歌单列表

GET: `[host]/Users/[UserId]/Items`

query:

| 参数名 | 备注 |
| --- | --- |
| SortBy | 排序方式列表，可选值: `DateCreated`, `SortName`|
| SortOrder | 排序，可选值: `Ascending`, `Descending` |
| Recursive | 是否递归查询 |
| includeItemTypes | 项目类型，可选值：`Playlist` |
| Fields | 包含的字段列表，可选值：`SortName`, `CanDelete`, `PrimaryImageAspectRatio` |
| mediaTypes | 媒体类型，可选值：`Audio` |
| StartIndex | 起始行数 |
| Limit | 最大数量，可选 |

response:

```json
{
    "Items": [
        {
            "Name": "test",
            "ServerId": "68ca97fe91ff41a08aa2ff3d057a5f75",
            "Id": "8fda11ea1088480124aef0e80277054e",
            "CanDelete": true,
            "SortName": "test",
            "ChannelId": null,
            "RunTimeTicks": 326515949568,
            "IsFolder": true,
            "Type": "Playlist",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false,
                "Key": "8fda11ea-1088-4801-24ae-f0e80277054e"
            },
            "ChildCount": 132,
            "PrimaryImageAspectRatio": 1,
            "ImageTags": {
                "Primary": "f775f0319d617c09251a65e80da362ef"
            },
            "BackdropImageTags": [],
            "ImageBlurHashes": {
                "Primary": {
                    "f775f0319d617c09251a65e80da362ef": "eI9jfgWBfQNG0KM{j[fQj[xufQfQfQfQfQE0j[fQof%MELoLfQs:xZ"
                }
            },
            "LocationType": "FileSystem",
            "MediaType": "Audio"
        },
        {
            "Name": "信息学3",
            "ServerId": "68ca97fe91ff41a08aa2ff3d057a5f75",
            "Id": "bea612652ad4b3578c76fa87a13e7fa7",
            "CanDelete": true,
            "SortName": "信息学0000000003",
            "ChannelId": null,
            "RunTimeTicks": 0,
            "IsFolder": true,
            "Type": "Playlist",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false,
                "Key": "bea61265-2ad4-b357-8c76-fa87a13e7fa7"
            },
            "ImageTags": {},
            "BackdropImageTags": [],
            "ImageBlurHashes": {},
            "LocationType": "FileSystem",
            "MediaType": "Audio"
        }
    ],
    "TotalRecordCount": 2,
    "StartIndex": 0
}
```

### Info 获取服务器信息

GET: `[host]/System/Info`

response:

```json
{
    "OperatingSystemDisplayName": "Linux",
    "HasPendingRestart": false,
    "IsShuttingDown": false,
    "SupportsLibraryMonitor": true,
    "WebSocketPortNumber": 8096,
    "CompletedInstallations": [],
    "CanSelfRestart": false,
    "CanLaunchWebBrowser": false,
    "ProgramDataPath": "/config",
    "WebPath": "/jellyfin/jellyfin-web",
    "ItemsByNamePath": "/config/metadata",
    "CachePath": "/cache",
    "LogPath": "/config/log",
    "InternalMetadataPath": "/config/metadata",
    "TranscodingTempPath": "/config/transcodes",
    "HasUpdateAvailable": false,
    "EncoderLocation": "NotFound",
    "SystemArchitecture": "X64",
    "LocalAddress": "http://172.27.0.2:8096",
    "ServerName": "e4941b681250",
    "Version": "10.8.13",
    "OperatingSystem": "Linux",
    "Id": "68ca97fe91ff41a08aa2ff3d057a5f75"
}
```

### ScheduledTasks 获取扫描状态

GET: `[host]/ScheduledTasks`

response:

```json
[
    {
        "Name": "Refresh Guide",
        "State": "Idle",
        "Id": "3339d81856535fbbee58d6d99ec83461",
        "LastExecutionResult": {
            "StartTimeUtc": "2024-04-18T16:00:54.8238573Z",
            "EndTimeUtc": "2024-04-18T16:00:57.8271289Z",
            "Status": "Completed",
            "Name": "Refresh Guide",
            "Key": "RefreshGuide",
            "Id": "3339d81856535fbbee58d6d99ec83461"
        },
        "Triggers": [
            {
                "Type": "IntervalTrigger",
                "IntervalTicks": 864000000000
            }
        ],
        "Description": "Downloads channel information from live tv services.",
        "Category": "Live TV",
        "IsHidden": true,
        "Key": "RefreshGuide"
    },
    {
        "Name": "TasksRefreshChannels",
        "State": "Idle",
        "Id": "a27c54259520b2e5c509def68c8f4c45",
        "LastExecutionResult": {
            "StartTimeUtc": "2024-04-18T16:00:54.7149059Z",
            "EndTimeUtc": "2024-04-18T16:00:54.7455027Z",
            "Status": "Completed",
            "Name": "TasksRefreshChannels",
            "Key": "RefreshInternetChannels",
            "Id": "a27c54259520b2e5c509def68c8f4c45"
        },
        "Triggers": [
            {
                "Type": "IntervalTrigger",
                "IntervalTicks": 864000000000
            }
        ],
        "Description": "TasksRefreshChannelsDescription",
        "Category": "互联网频道",
        "IsHidden": true,
        "Key": "RefreshInternetChannels"
    },
    {
        "Name": "下载缺少的字幕",
        "State": "Idle",
        "Id": "2c66a88bca43e565d7f8099f825478f1",
        "LastExecutionResult": {
            "StartTimeUtc": "2024-04-18T15:00:56.4262005Z",
            "EndTimeUtc": "2024-04-18T15:00:56.4262914Z",
            "Status": "Completed",
            "Name": "下载缺少的字幕",
            "Key": "DownloadSubtitles",
            "Id": "2c66a88bca43e565d7f8099f825478f1"
        },
        "Triggers": [
            {
                "Type": "IntervalTrigger",
                "IntervalTicks": 864000000000
            }
        ],
        "Description": "根据元数据设置在互联网上搜索缺少的字幕。",
        "Category": "媒体库",
        "IsHidden": false,
        "Key": "DownloadSubtitles"
    },
    {
        "Name": "优化数据库",
        "State": "Idle",
        "Id": "31de9ce83b9223d338c77b1a635e144b",
        "LastExecutionResult": {
            "StartTimeUtc": "2024-04-18T16:01:01.5741968Z",
            "EndTimeUtc": "2024-04-18T16:01:01.9621083Z",
            "Status": "Completed",
            "Name": "优化数据库",
            "Key": "OptimizeDatabaseTask",
            "Id": "31de9ce83b9223d338c77b1a635e144b"
        },
        "Triggers": [
            {
                "Type": "IntervalTrigger",
                "IntervalTicks": 864000000000
            }
        ],
        "Description": "压缩数据库并优化可用空间，在扫描库或执行其他数据库修改后运行此任务可能会提高性能。",
        "Category": "维护",
        "IsHidden": false,
        "Key": "OptimizeDatabaseTask"
    },
    {
        "Name": "关键帧提取器",
        "State": "Idle",
        "Id": "f302d80f31bcacf76f979d277d448581",
        "Triggers": [],
        "Description": "从视频文件中提取关键帧以创建更准确的HLS播放列表。这项任务可能需要很长时间。",
        "Category": "媒体库",
        "IsHidden": false,
        "Key": "KeyframeExtraction"
    },
    {
        "Name": "刷新人员",
        "State": "Idle",
        "Id": "866456ed0d44e15468124ce33d85961e",
        "LastExecutionResult": {
            "StartTimeUtc": "2024-04-12T16:00:55.7846583Z",
            "EndTimeUtc": "2024-04-12T16:00:55.7856805Z",
            "Status": "Completed",
            "Name": "刷新人员",
            "Key": "RefreshPeople",
            "Id": "866456ed0d44e15468124ce33d85961e"
        },
        "Triggers": [
            {
                "Type": "IntervalTrigger",
                "IntervalTicks": 6048000000000
            }
        ],
        "Description": "更新媒体库中演员和导演的元数据。",
        "Category": "媒体库",
        "IsHidden": false,
        "Key": "RefreshPeople"
    },
    {
        "Name": "扫描媒体库",
        "State": "Idle",
        "Id": "7738148ffcd07979c7ceb148e06b3aed",
        "LastExecutionResult": {
            "StartTimeUtc": "2024-04-18T21:01:51.1025101Z",
            "EndTimeUtc": "2024-04-18T21:01:52.1775033Z",
            "Status": "Completed",
            "Name": "扫描媒体库",
            "Key": "RefreshLibrary",
            "Id": "7738148ffcd07979c7ceb148e06b3aed"
        },
        "Triggers": [
            {
                "Type": "IntervalTrigger",
                "IntervalTicks": 432000000000
            }
        ],
        "Description": "扫描你的媒体库以获取新文件并刷新元数据。",
        "Category": "媒体库",
        "IsHidden": false,
        "Key": "RefreshLibrary"
    },
    {
        "Name": "提取章节图片",
        "State": "Idle",
        "Id": "4e6637c832ed644d1af3370a2506e80a",
        "LastExecutionResult": {
            "StartTimeUtc": "2024-04-19T02:00:00.0269008Z",
            "EndTimeUtc": "2024-04-19T02:00:00.1078383Z",
            "Status": "Completed",
            "Name": "提取章节图片",
            "Key": "RefreshChapterImages",
            "Id": "4e6637c832ed644d1af3370a2506e80a"
        },
        "Triggers": [
            {
                "Type": "DailyTrigger",
                "TimeOfDayTicks": 72000000000,
                "MaxRuntimeTicks": 144000000000
            }
        ],
        "Description": "为包含章节的视频提取缩略图。",
        "Category": "媒体库",
        "IsHidden": false,
        "Key": "RefreshChapterImages"
    },
    {
        "Name": "更新插件",
        "State": "Idle",
        "Id": "f9b057c054e9e6daee4a88ffd146a403",
        "LastExecutionResult": {
            "StartTimeUtc": "2024-04-18T15:00:53.891681Z",
            "EndTimeUtc": "2024-04-18T15:00:57.2248519Z",
            "Status": "Completed",
            "Name": "更新插件",
            "Key": "PluginUpdates",
            "Id": "f9b057c054e9e6daee4a88ffd146a403"
        },
        "Triggers": [
            {
                "Type": "StartupTrigger"
            },
            {
                "Type": "IntervalTrigger",
                "IntervalTicks": 864000000000
            }
        ],
        "Description": "为已设置为自动更新的插件下载和安装更新。",
        "Category": "应用程序",
        "IsHidden": false,
        "Key": "PluginUpdates"
    },
    {
        "Name": "清理日志目录",
        "State": "Idle",
        "Id": "1c8ede62c521bea0bf851344f5b8ca40",
        "LastExecutionResult": {
            "StartTimeUtc": "2024-04-18T15:00:55.6453189Z",
            "EndTimeUtc": "2024-04-18T15:00:55.6581013Z",
            "Status": "Completed",
            "Name": "清理日志目录",
            "Key": "CleanLogFiles",
            "Id": "1c8ede62c521bea0bf851344f5b8ca40"
        },
        "Triggers": [
            {
                "Type": "IntervalTrigger",
                "IntervalTicks": 864000000000
            }
        ],
        "Description": "删除存在超过 3 天的的日志文件。",
        "Category": "维护",
        "IsHidden": false,
        "Key": "CleanLogFiles"
    },
    {
        "Name": "清理程序日志",
        "State": "Idle",
        "Id": "b461ef918ab28520928183e794350e3c",
        "Triggers": [],
        "Description": "删除早于设置时间的活动日志条目。",
        "Category": "维护",
        "IsHidden": false,
        "Key": "CleanActivityLog"
    },
    {
        "Name": "清理缓存目录",
        "State": "Idle",
        "Id": "241d4fcb19a1d557ee62428e411da609",
        "LastExecutionResult": {
            "StartTimeUtc": "2024-04-18T15:00:59.0776557Z",
            "EndTimeUtc": "2024-04-18T15:00:59.2224953Z",
            "Status": "Completed",
            "Name": "清理缓存目录",
            "Key": "DeleteCacheFiles",
            "Id": "241d4fcb19a1d557ee62428e411da609"
        },
        "Triggers": [
            {
                "Type": "IntervalTrigger",
                "IntervalTicks": 864000000000
            }
        ],
        "Description": "删除系统不再需要的缓存文件。",
        "Category": "维护",
        "IsHidden": false,
        "Key": "DeleteCacheFiles"
    },
    {
        "Name": "清理转码目录",
        "State": "Idle",
        "Id": "7d8088c10902f1bf4072ded42437bcfb",
        "LastExecutionResult": {
            "StartTimeUtc": "2024-04-18T15:00:55.9292122Z",
            "EndTimeUtc": "2024-04-18T15:00:55.9294865Z",
            "Status": "Completed",
            "Name": "清理转码目录",
            "Key": "DeleteTranscodeFiles",
            "Id": "7d8088c10902f1bf4072ded42437bcfb"
        },
        "Triggers": [
            {
                "Type": "IntervalTrigger",
                "IntervalTicks": 864000000000
            }
        ],
        "Description": "删除存在超过 1 天的转码文件。",
        "Category": "维护",
        "IsHidden": false,
        "Key": "DeleteTranscodeFiles"
    }
]
```

:::caution

此接口需要管理员权限才能访问！

:::

### PlayedItems/[id] 滚动播放记录

POST: `[host]/Users/[UserId]/PlayedItems/[id]`

query:

| 参数名 | 备注 |
| --- | --- |
| datePlayed | 播放时间，ISO8601 |

### Similar 获取相似歌曲

GET: `[host]/Items/[id]/Similar`

query:

| 参数名 | 备注 |
| --- | --- |
| Limit | 结果数量 |
| Fields | 包含的字段列表，可选值：`AudioInfo`, `SortName`, `MediaSources`, `DateCreated` |
| userId | 用户ID |

response:

```json
{
    "Items": [
        {
            "Name": "半城烟沙",
            "ServerId": "68ca97fe91ff41a08aa2ff3d057a5f75",
            "Id": "a46bd635fb5f64d007180788b0e36cd6",
            "DateCreated": "2024-03-21T10:52:08.2380753Z",
            "SortName": "0001 - 半城烟沙",
            "PremiereDate": "2010-01-01T00:00:00.0000000Z",
            "MediaSources": [
                {
                    "Protocol": "File",
                    "Id": "a46bd635fb5f64d007180788b0e36cd6",
                    "Path": "/media/许嵩/半城烟沙/半城烟沙 - 许嵩.mp3",
                    "Type": "Default",
                    "Container": "mp3",
                    "Size": 11818653,
                    "Name": "半城烟沙 - 许嵩",
                    "IsRemote": false,
                    "ETag": "a112f50492ca04c9115eceb9ae498883",
                    "RunTimeTicks": 2946351104,
                    "ReadAtNativeFramerate": false,
                    "IgnoreDts": false,
                    "IgnoreIndex": false,
                    "GenPtsInput": false,
                    "SupportsTranscoding": true,
                    "SupportsDirectStream": true,
                    "SupportsDirectPlay": true,
                    "IsInfiniteStream": false,
                    "RequiresOpening": false,
                    "RequiresClosing": false,
                    "RequiresLooping": false,
                    "SupportsProbing": true,
                    "MediaStreams": [
                        {
                            "Codec": "mp3",
                            "TimeBase": "1/14112000",
                            "DisplayTitle": "MP3 - Stereo",
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
                            "Level": 0
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
                            "PixelFormat": "yuvj420p",
                            "Level": -99
                        }
                    ],
                    "MediaAttachments": [],
                    "Formats": [],
                    "Bitrate": 320902,
                    "RequiredHttpHeaders": {},
                    "DefaultAudioStreamIndex": 0
                }
            ],
            "ChannelId": null,
            "RunTimeTicks": 2946351104,
            "ProductionYear": 2010,
            "IndexNumber": 1,
            "IsFolder": false,
            "Type": "Audio",
            "ParentBackdropItemId": "9cb24036603a4bbdaf15891d3f8215b0",
            "ParentBackdropImageTags": [
                "17c8f1f8c484ca3f6f9dee5102176e1e"
            ],
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false,
                "Key": "半城烟沙 - 许嵩"
            },
            "Artists": [
                "许嵩"
            ],
            "ArtistItems": [
                {
                    "Name": "许嵩",
                    "Id": "9cb24036603a4bbdaf15891d3f8215b0"
                }
            ],
            "Album": "半城烟沙",
            "AlbumId": "2d5cef1257c1614eeeef82c35debb3af",
            "AlbumPrimaryImageTag": "bb5b481820e918f1bbaa89f963028b3d",
            "AlbumArtist": "许嵩",
            "AlbumArtists": [
                {
                    "Name": "许嵩",
                    "Id": "9cb24036603a4bbdaf15891d3f8215b0"
                }
            ],
            "ImageTags": {
                "Primary": "f4a103853e2272c22c8bdea78b154f25"
            },
            "BackdropImageTags": [],
            "ImageBlurHashes": {
                "Primary": {
                    "f4a103853e2272c22c8bdea78b154f25": "eH9QXCRj0K%M?HD%oe-;RkIUE2of$*NFNHt7ayR*ofs.%2ayIoofxa",
                    "bb5b481820e918f1bbaa89f963028b3d": "eH9QXCRj0K%M?HD%oe-;RkIUE2of$*NFNHt7ayR*ofs.%2ayIoofxa"
                },
                "Backdrop": {
                    "17c8f1f8c484ca3f6f9dee5102176e1e": "WTHetT_3.9?bjFt8%hRPofWBRit70L9FMwRjozM{-;IUjZayWXt7"
                }
            },
            "LocationType": "FileSystem",
            "MediaType": "Audio"
        }
    ],
    "TotalRecordCount": 1,
    "StartIndex": 0
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
| Fields | 包含的字段列表，可选值：`SortName`, `MediaSources`, `AudioInfo`, `DateCreated` |
| ImageTypeLimit | 返回的每个图片类型图片数量 |
| EnableImageTypes | 图片类型列表，可选值：`Primary` |
| StartIndex | 起始行数 |
| Limit | 最大数量，可选 |
| isFavorite | 收藏状态，可选 |
| SearchTerm | 搜索词，可选 |
| Years | 发行年份列表，可选 |

response:

```json
{
    "Items": [
        {
            "Name": "Play With Style",
            "ServerId": "68ca97fe91ff41a08aa2ff3d057a5f75",
            "Id": "39de54ec99682f60e77133bd51759673",
            "DateCreated": "2024-03-21T10:50:57.4570251Z",
            "SortName": "0001 - 0007 - Play With Style",
            "PremiereDate": "2012-01-01T00:00:00.0000000Z",
            "MediaSources": [
                {
                    "Protocol": "File",
                    "Id": "39de54ec99682f60e77133bd51759673",
                    "Path": "/media/许嵩/梦游计/Play With Style - 许嵩.flac",
                    "Type": "Default",
                    "Container": "flac",
                    "Size": 19795534,
                    "Name": "Play With Style - 许嵩",
                    "IsRemote": false,
                    "ETag": "6054c45b3db258b551c8bc6f300bc5ba",
                    "RunTimeTicks": 1750671232,
                    "ReadAtNativeFramerate": false,
                    "IgnoreDts": false,
                    "IgnoreIndex": false,
                    "GenPtsInput": false,
                    "SupportsTranscoding": true,
                    "SupportsDirectStream": true,
                    "SupportsDirectPlay": true,
                    "IsInfiniteStream": false,
                    "RequiresOpening": false,
                    "RequiresClosing": false,
                    "RequiresLooping": false,
                    "SupportsProbing": true,
                    "MediaStreams": [
                        {
                            "Codec": "flac",
                            "TimeBase": "1/44100",
                            "DisplayTitle": "FLAC - Stereo",
                            "IsInterlaced": false,
                            "ChannelLayout": "stereo",
                            "BitRate": 904591,
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
                            "Level": 0
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
                            "PixelFormat": "yuvj420p",
                            "Level": -99
                        }
                    ],
                    "MediaAttachments": [],
                    "Formats": [],
                    "Bitrate": 904591,
                    "RequiredHttpHeaders": {},
                    "DefaultAudioStreamIndex": 0
                }
            ],
            "ChannelId": null,
            "RunTimeTicks": 1750671232,
            "ProductionYear": 2012,
            "IndexNumber": 7,
            "ParentIndexNumber": 1,
            "IsFolder": false,
            "Type": "Audio",
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false,
                "Key": "许嵩-梦游计-0001-0007Play With Style"
            },
            "Artists": [
                "许嵩"
            ],
            "ArtistItems": [
                {
                    "Name": "许嵩",
                    "Id": "9cb24036603a4bbdaf15891d3f8215b0"
                }
            ],
            "Album": "梦游计",
            "AlbumId": "c1037c12ede81c855bbf38a4846248f9",
            "AlbumPrimaryImageTag": "ac75515d40f6197331cc7a62f990c255",
            "AlbumArtist": "许嵩",
            "AlbumArtists": [
                {
                    "Name": "许嵩",
                    "Id": "9cb24036603a4bbdaf15891d3f8215b0"
                }
            ],
            "ImageTags": {
                "Primary": "3efca2f6e537a66851e786453858e744"
            },
            "ImageBlurHashes": {
                "Primary": {
                    "3efca2f6e537a66851e786453858e744": "eH9QXCRj0K%M?HD%oe-;RkIUE2of$*NFNHt7ayR*ofs.%2ayIoofxa",
                    "ac75515d40f6197331cc7a62f990c255": "eH9QXCRj0K%M?HD%oe-;RkIUE2of$*NFNHt7ayR*ofs.%2ayIoofxa"
                }
            },
            "LocationType": "FileSystem",
            "MediaType": "Audio"
        }
    ],
    "TotalRecordCount": 132,
    "StartIndex": 0
}
```

### Items/[id] 获取歌曲信息

GET: `[host]/Users/[UserId]/Items/[id]`

response:

```json
{
    "Name": "Play With Style",
    "ServerId": "68ca97fe91ff41a08aa2ff3d057a5f75",
    "Id": "39de54ec99682f60e77133bd51759673",
    "Etag": "87d4beea009b1b89fed5089433b47e5c",
    "DateCreated": "2024-03-21T10:50:57.4570251Z",
    "CanDelete": true,
    "CanDownload": true,
    "SortName": "0001 - 0007 - Play With Style",
    "PremiereDate": "2012-01-01T00:00:00.0000000Z",
    "ExternalUrls": [],
    "MediaSources": [
        {
            "Protocol": "File",
            "Id": "39de54ec99682f60e77133bd51759673",
            "Path": "/media/许嵩/梦游计/Play With Style - 许嵩.flac",
            "Type": "Default",
            "Container": "flac",
            "Size": 19795534,
            "Name": "Play With Style - 许嵩",
            "IsRemote": false,
            "ETag": "6054c45b3db258b551c8bc6f300bc5ba",
            "RunTimeTicks": 1750671232,
            "ReadAtNativeFramerate": false,
            "IgnoreDts": false,
            "IgnoreIndex": false,
            "GenPtsInput": false,
            "SupportsTranscoding": true,
            "SupportsDirectStream": true,
            "SupportsDirectPlay": true,
            "IsInfiniteStream": false,
            "RequiresOpening": false,
            "RequiresClosing": false,
            "RequiresLooping": false,
            "SupportsProbing": true,
            "MediaStreams": [
                {
                    "Codec": "flac",
                    "TimeBase": "1/44100",
                    "DisplayTitle": "FLAC - Stereo",
                    "IsInterlaced": false,
                    "ChannelLayout": "stereo",
                    "BitRate": 904591,
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
                    "Level": 0
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
                    "PixelFormat": "yuvj420p",
                    "Level": -99
                }
            ],
            "MediaAttachments": [],
            "Formats": [],
            "Bitrate": 904591,
            "RequiredHttpHeaders": {},
            "DefaultAudioStreamIndex": 0
        }
    ],
    "Path": "/media/许嵩/梦游计/Play With Style - 许嵩.flac",
    "EnableMediaSourceDisplay": true,
    "ChannelId": null,
    "Taglines": [],
    "Genres": [],
    "RunTimeTicks": 1750671232,
    "PlayAccess": "Full",
    "ProductionYear": 2012,
    "IndexNumber": 7,
    "ParentIndexNumber": 1,
    "RemoteTrailers": [],
    "ProviderIds": {},
    "IsFolder": false,
    "ParentId": "c1037c12ede81c855bbf38a4846248f9",
    "Type": "Audio",
    "People": [],
    "Studios": [],
    "GenreItems": [],
    "ParentBackdropItemId": "9cb24036603a4bbdaf15891d3f8215b0",
    "ParentBackdropImageTags": [
        "17c8f1f8c484ca3f6f9dee5102176e1e"
    ],
    "LocalTrailerCount": 0,
    "UserData": {
        "PlaybackPositionTicks": 0,
        "PlayCount": 0,
        "IsFavorite": false,
        "Played": false,
        "Key": "许嵩-梦游计-0001-0007Play With Style"
    },
    "SpecialFeatureCount": 0,
    "DisplayPreferencesId": "61bba315f137702baa296a1c417faada",
    "Tags": [],
    "PrimaryImageAspectRatio": 1,
    "Artists": [
        "许嵩"
    ],
    "ArtistItems": [
        {
            "Name": "许嵩",
            "Id": "9cb24036603a4bbdaf15891d3f8215b0"
        }
    ],
    "Album": "梦游计",
    "AlbumId": "c1037c12ede81c855bbf38a4846248f9",
    "AlbumPrimaryImageTag": "ac75515d40f6197331cc7a62f990c255",
    "AlbumArtist": "许嵩",
    "AlbumArtists": [
        {
            "Name": "许嵩",
            "Id": "9cb24036603a4bbdaf15891d3f8215b0"
        }
    ],
    "MediaStreams": [
        {
            "Codec": "flac",
            "TimeBase": "1/44100",
            "DisplayTitle": "FLAC - Stereo",
            "IsInterlaced": false,
            "ChannelLayout": "stereo",
            "BitRate": 904591,
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
            "Level": 0
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
            "PixelFormat": "yuvj420p",
            "Level": -99
        }
    ],
    "ImageTags": {
        "Primary": "3efca2f6e537a66851e786453858e744"
    },
    "BackdropImageTags": [],
    "ImageBlurHashes": {
        "Primary": {
            "3efca2f6e537a66851e786453858e744": "eH9QXCRj0K%M?HD%oe-;RkIUE2of$*NFNHt7ayR*ofs.%2ayIoofxa",
            "ac75515d40f6197331cc7a62f990c255": "eH9QXCRj0K%M?HD%oe-;RkIUE2of$*NFNHt7ayR*ofs.%2ayIoofxa"
        },
        "Backdrop": {
            "17c8f1f8c484ca3f6f9dee5102176e1e": "WTHetT_3.9?bjFt8%hRPofWBRit70L9FMwRjozM{-;IUjZayWXt7"
        }
    },
    "LocationType": "FileSystem",
    "MediaType": "Audio",
    "LockedFields": [],
    "LockData": false
}
```

### Items 获取专辑中的歌曲

GET: `[host]/Users/[UserId]/Items`

query:

| 参数名 | 备注 |
| --- | --- |
| SortBy | 排序方式列表，可选值: `ParentIndexNumber`, `IndexNumber`, `SortName` |
| Fields | 包含的字段列表，可选值：`ItemCounts`, `PrimaryImageAspectRatio`, `BasicSyncInfo`, `CanDelete`, `MediaSourceCount`, `MediaSources`, `ProductionYear` |
| ParentId | 专辑ID |

response:

```json
{
    "Items": [
        {
            "Name": "飞驰于你",
            "ServerId": "68ca97fe91ff41a08aa2ff3d057a5f75",
            "Id": "487267c2b069ccb9b5a345d93bb82fe3",
            "CanDelete": true,
            "PremiereDate": "2018-01-01T00:00:00.0000000Z",
            "MediaSources": [
                {
                    "Protocol": "File",
                    "Id": "487267c2b069ccb9b5a345d93bb82fe3",
                    "Path": "/media/许嵩/飞驰于你/飞驰于你 - 许嵩.flac",
                    "Type": "Default",
                    "Container": "flac",
                    "Size": 31228248,
                    "Name": "飞驰于你 - 许嵩",
                    "IsRemote": false,
                    "ETag": "5c149de4705594742c9784ae3aa52785",
                    "RunTimeTicks": 2441376768,
                    "ReadAtNativeFramerate": false,
                    "IgnoreDts": false,
                    "IgnoreIndex": false,
                    "GenPtsInput": false,
                    "SupportsTranscoding": true,
                    "SupportsDirectStream": true,
                    "SupportsDirectPlay": true,
                    "IsInfiniteStream": false,
                    "RequiresOpening": false,
                    "RequiresClosing": false,
                    "RequiresLooping": false,
                    "SupportsProbing": true,
                    "MediaStreams": [
                        {
                            "Codec": "flac",
                            "TimeBase": "1/44100",
                            "DisplayTitle": "FLAC - Stereo",
                            "IsInterlaced": false,
                            "ChannelLayout": "stereo",
                            "BitRate": 1023299,
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
                            "Level": 0
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
                            "PixelFormat": "yuvj420p",
                            "Level": -99
                        }
                    ],
                    "MediaAttachments": [],
                    "Formats": [],
                    "Bitrate": 1023299,
                    "RequiredHttpHeaders": {},
                    "DefaultAudioStreamIndex": 0
                }
            ],
            "ChannelId": null,
            "RunTimeTicks": 2441376768,
            "ProductionYear": 2018,
            "IndexNumber": 1,
            "ParentIndexNumber": 1,
            "IsFolder": false,
            "Type": "Audio",
            "ParentBackdropItemId": "9cb24036603a4bbdaf15891d3f8215b0",
            "ParentBackdropImageTags": [
                "17c8f1f8c484ca3f6f9dee5102176e1e"
            ],
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false,
                "Key": "许嵩-飞驰于你-0001-0001飞驰于你"
            },
            "PrimaryImageAspectRatio": 1,
            "Artists": [
                "许嵩"
            ],
            "ArtistItems": [
                {
                    "Name": "许嵩",
                    "Id": "9cb24036603a4bbdaf15891d3f8215b0"
                }
            ],
            "Album": "飞驰于你",
            "AlbumId": "bb725906dce0e1d5dcbb5e2aab50f590",
            "AlbumPrimaryImageTag": "b9a921b8a933b371c1075b3c9d046352",
            "AlbumArtist": "许嵩",
            "AlbumArtists": [
                {
                    "Name": "许嵩",
                    "Id": "9cb24036603a4bbdaf15891d3f8215b0"
                }
            ],
            "ImageTags": {
                "Primary": "c1a904073873e3cdc4e8c0fcfc91a933"
            },
            "BackdropImageTags": [],
            "ImageBlurHashes": {
                "Primary": {
                    "c1a904073873e3cdc4e8c0fcfc91a933": "eH9QXCRj0K%M?HD%oe-;RkIUE2of$*NFNHt7ayR*ofs.%2ayIoofxa",
                    "b9a921b8a933b371c1075b3c9d046352": "eH9QXCRj0K%M?HD%oe-;RkIUE2of$*NFNHt7ayR*ofs.%2ayIoofxa"
                },
                "Backdrop": {
                    "17c8f1f8c484ca3f6f9dee5102176e1e": "WTHetT_3.9?bjFt8%hRPofWBRit70L9FMwRjozM{-;IUjZayWXt7"
                }
            },
            "LocationType": "FileSystem",
            "MediaType": "Audio"
        }
    ],
    "TotalRecordCount": 1,
    "StartIndex": 0
}
```

### Items 获取歌手名下歌曲

GET: `[host]/Users/[UserId]/Items`

| 参数名 | 备注 |
| --- | --- |
| SortBy | 排序方式列表，可选值: `CommunityRating`, `SortName` |
| SortOrder | 排序，可选值: `Ascending`, `Descending` |
| IncludeItemTypes | 包含的项目类型，可选值：`Audio` |
| Recursive | 是否递归查询 |
| Fields | 包含的字段列表，可选值：`SortName`, `MediaSources`, `PrimaryImageAspectRatio`, `BasicSyncInfo`, `ProductionYear` |
| ImageTypeLimit | 返回的每个图片类型图片数量 |
| EnableImageTypes | 图片类型列表，可选值：`Primary` |
| StartIndex | 起始行数 |
| Limit | 最大数量，可选 |
| artists | 歌手名列表 |

### Items 获取歌单中的歌曲

GET: `[host]/Playlists/[id]/Items`

query:

| 参数名 | 备注 |
| --- | --- |
| fields | 包含的属性列表，可选值: `SortName`, `CanDelete`, `MediaSources`, `DateCreated`, `ProductionYear` |
| userId | 用户ID |

response:

```json
{
    "Items": [
        {
            "Name": "飞驰于你",
            "ServerId": "68ca97fe91ff41a08aa2ff3d057a5f75",
            "Id": "487267c2b069ccb9b5a345d93bb82fe3",
            "PlaylistItemId": "857c1587c25342499d4723c72ca2b759",
            "DateCreated": "2024-03-21T10:54:53.3621923Z",
            "CanDelete": true,
            "SortName": "0001 - 0001 - 飞驰于你",
            "PremiereDate": "2018-01-01T00:00:00.0000000Z",
            "MediaSources": [
                {
                    "Protocol": "File",
                    "Id": "487267c2b069ccb9b5a345d93bb82fe3",
                    "Path": "/media/许嵩/飞驰于你/飞驰于你 - 许嵩.flac",
                    "Type": "Default",
                    "Container": "flac",
                    "Size": 31228248,
                    "Name": "飞驰于你 - 许嵩",
                    "IsRemote": false,
                    "ETag": "5c149de4705594742c9784ae3aa52785",
                    "RunTimeTicks": 2441376768,
                    "ReadAtNativeFramerate": false,
                    "IgnoreDts": false,
                    "IgnoreIndex": false,
                    "GenPtsInput": false,
                    "SupportsTranscoding": true,
                    "SupportsDirectStream": true,
                    "SupportsDirectPlay": true,
                    "IsInfiniteStream": false,
                    "RequiresOpening": false,
                    "RequiresClosing": false,
                    "RequiresLooping": false,
                    "SupportsProbing": true,
                    "MediaStreams": [
                        {
                            "Codec": "flac",
                            "TimeBase": "1/44100",
                            "DisplayTitle": "FLAC - Stereo",
                            "IsInterlaced": false,
                            "ChannelLayout": "stereo",
                            "BitRate": 1023299,
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
                            "Level": 0
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
                            "PixelFormat": "yuvj420p",
                            "Level": -99
                        }
                    ],
                    "MediaAttachments": [],
                    "Formats": [],
                    "Bitrate": 1023299,
                    "RequiredHttpHeaders": {},
                    "DefaultAudioStreamIndex": 0
                }
            ],
            "ChannelId": null,
            "RunTimeTicks": 2441376768,
            "ProductionYear": 2018,
            "IndexNumber": 1,
            "ParentIndexNumber": 1,
            "IsFolder": false,
            "Type": "Audio",
            "ParentBackdropItemId": "9cb24036603a4bbdaf15891d3f8215b0",
            "ParentBackdropImageTags": [
                "17c8f1f8c484ca3f6f9dee5102176e1e"
            ],
            "UserData": {
                "PlaybackPositionTicks": 0,
                "PlayCount": 0,
                "IsFavorite": false,
                "Played": false,
                "Key": "许嵩-飞驰于你-0001-0001飞驰于你"
            },
            "Artists": [
                "许嵩"
            ],
            "ArtistItems": [
                {
                    "Name": "许嵩",
                    "Id": "9cb24036603a4bbdaf15891d3f8215b0"
                }
            ],
            "Album": "飞驰于你",
            "AlbumId": "bb725906dce0e1d5dcbb5e2aab50f590",
            "AlbumPrimaryImageTag": "b9a921b8a933b371c1075b3c9d046352",
            "AlbumArtist": "许嵩",
            "AlbumArtists": [
                {
                    "Name": "许嵩",
                    "Id": "9cb24036603a4bbdaf15891d3f8215b0"
                }
            ],
            "ImageTags": {
                "Primary": "c1a904073873e3cdc4e8c0fcfc91a933"
            },
            "BackdropImageTags": [],
            "ImageBlurHashes": {
                "Primary": {
                    "c1a904073873e3cdc4e8c0fcfc91a933": "eH9QXCRj0K%M?HD%oe-;RkIUE2of$*NFNHt7ayR*ofs.%2ayIoofxa",
                    "b9a921b8a933b371c1075b3c9d046352": "eH9QXCRj0K%M?HD%oe-;RkIUE2of$*NFNHt7ayR*ofs.%2ayIoofxa"
                },
                "Backdrop": {
                    "17c8f1f8c484ca3f6f9dee5102176e1e": "WTHetT_3.9?bjFt8%hRPofWBRit70L9FMwRjozM{-;IUjZayWXt7"
                }
            },
            "LocationType": "FileSystem",
            "MediaType": "Audio"
        }
    ],
    "TotalRecordCount": 1,
    "StartIndex": 0
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