---
sidebar_position: 2
---

# Navidrome 接口文档

:::note

Navidrome 目前还没有官方的接口文档，以下均为抓包所得。

0.55.0 版本对原生接口进行了重大重构，以下内容部分已经过时。

:::

## 认证

### login 登录

POST：`[host]/auth/login`

body(`application/json`)：

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| username | Y | | 用户名 |
| password | Y | | 密码 |

响应内容：

```json
{
    "id": "34c4xxxx-xxxx-xxxx-xxxx-6442b9a3xxxx",
    "isAdmin": true,
    "lastFMApiKey": "xxx",
    "name": "username",
    "subsonicSalt": "xxx",
    "subsonicToken": "xxxxx",
    "token": "xxxx",
    "username": "username"
}
```

在之后的请求中，需要在请求头中携带以下信息：

- `x-nd-authorization`: 'Bearer `token`'
- `x-nd-client-unique-id`: `id`

### keepalive 登录状态保活

GET: `[host]/api/keepalive/keepalive`

## 请求节点

### album 获取专辑列表

GET: `[host]/api/album`

query:

| 参数名 | 备注 |
| --- | --- |
| _start | 起始行数，0开始 |
| _end | 结束行数 |
| _order | 排序，可选值 `ASC`, `DESC` |
| _sort | 排序方式，可选值 `random`, `createdAt`, `min_year`, `play_count`, `play_date`, `name`, `albumArtist`, `rating`, 可用`,`分割多个排序方式，如 `min_year asc,date asc` |
| artist_id | 歌手id，可选 |
| rating | 评分，可选 |
| starred | 收藏状态(`true/false`)，可选 |
| name | 专辑名(like 查询)，可选 |

:::note 待补充：

1. 如何查询在某个区间的年代，自测 `min_year` 和 `max_year` 只有相等的判断，同时传也不会判断区间。
2. 如何查询歌曲数量大于某个值的专辑
3. 专辑名的筛选是否可以添加多个关键词筛选

:::

响应内容：

```json
[
    {
        "playCount": 14,
        "playDate": "2024-04-18T07:37:46.658+08:00",
        "rating": 0,
        "starred": false,
        "starredAt": null,
        "id": "2e7e41725443fa5e8a637a4668e63e98",
        "name": "放下",
        "embedArtPath": "/volume1/music/胡夏/放下/胡夏-放下.flac",
        "artistId": "6d095fad618e04185bd66998450041da",
        "artist": "胡夏",
        "albumArtistId": "6d095fad618e04185bd66998450041da",
        "albumArtist": "胡夏",
        "allArtistIds": "6d095fad618e04185bd66998450041da",
        "maxYear": 2013,
        "minYear": 2013,
        "date": "2013",
        "maxOriginalYear": 0,
        "minOriginalYear": 0,
        "releases": 1,
        "compilation": false,
        "songCount": 1,
        "duration": 337.08,
        "size": 35163552,
        "genre": "",
        "genres": null,
        "fullText": " 放下 胡夏",
        "orderAlbumName": "放下",
        "orderAlbumArtistName": "胡夏",
        "paths": "/volume1/music/胡夏/放下",
        "externalInfoUpdatedAt": null,
        "createdAt": "2024-03-02T01:04:46.424670828+08:00",
        "updatedAt": "2024-03-21T20:41:28.340360006+08:00"
    }
]
```

响应头：

- `x-total-count`: 总行数

### album/[id] 获取专辑信息

GET: `[host]/api/album/[id]`

响应内容：

```json
{
    "playCount": 14,
    "playDate": "2024-04-18T07:37:46.658+08:00",
    "rating": 0,
    "starred": false,
    "starredAt": null,
    "id": "2e7e41725443fa5e8a637a4668e63e98",
    "name": "放下",
    "embedArtPath": "/volume1/music/胡夏/放下/胡夏-放下.flac",
    "artistId": "6d095fad618e04185bd66998450041da",
    "artist": "胡夏",
    "albumArtistId": "6d095fad618e04185bd66998450041da",
    "albumArtist": "胡夏",
    "allArtistIds": "6d095fad618e04185bd66998450041da",
    "maxYear": 2013,
    "minYear": 2013,
    "date": "2013",
    "maxOriginalYear": 0,
    "minOriginalYear": 0,
    "releases": 1,
    "compilation": false,
    "songCount": 1,
    "duration": 337.08,
    "size": 35163552,
    "genre": "",
    "genres": null,
    "fullText": " 放下 胡夏",
    "orderAlbumName": "放下",
    "orderAlbumArtistName": "胡夏",
    "paths": "/volume1/music/胡夏/放下",
    "externalInfoUpdatedAt": null,
    "createdAt": "2024-03-02T01:04:46.424670828+08:00",
    "updatedAt": "2024-03-21T20:41:28.340360006+08:00"
}
```

### artist/[id] 获取歌手信息

GET: `[host]/api/artist/[id]`

响应内容：

```json
{
    "playCount": 42,
    "playDate": "2024-04-18T08:27:04.036+08:00",
    "rating": 0,
    "starred": false,
    "starredAt": null,
    "id": "6d095fad618e04185bd66998450041da",
    "name": "胡夏",
    "albumCount": 19,
    "songCount": 60,
    "genres": null,
    "fullText": " 胡夏",
    "orderArtistName": "胡夏",
    "size": 1714942860,
    "externalUrl": "https://www.last.fm/music/%E8%83%A1%E5%A4%8F",
    "externalInfoUpdatedAt": "0001-01-01T00:00:00Z"
}
```

### getArtistInfo 获取歌手简介及相似歌手

参见 Subsonic 的 [getArtistInfo](subsonic#getartistinfo2-获取歌手简介和相似歌手列表) 接口。

### artist 获取歌手列表

GET: `[host]/api/artist`

query:

| 参数名 | 备注 |
| --- | --- |
| _start | 起始行数，0开始 |
| _end | 结束行数，_end 和 _start 都等于 0 时可以查询全部 |
| _order | 排序，可选值 `ASC`, `DESC` |
| _sort | 排序方式，可选值 `random`, `play_count`, `play_date`, `name`, `rating`, 可用`,`分割多个排序方式，如 `min_year asc,date asc` |
| rating | 评分，可选 |
| starred | 收藏状态(`true/false`)，可选 |
| name | 歌手名(like 查询)，可选 |
| role | 角色，可选，0.55.0 及以上版本可用，以下版本添加此参数会出错 |

响应内容：

```json
[
    {
        "playCount": 42,
        "playDate": "2024-04-18T08:27:04.036+08:00",
        "rating": 0,
        "starred": false,
        "starredAt": null,
        "id": "6d095fad618e04185bd66998450041da",
        "name": "胡夏",
        "albumCount": 19,
        "songCount": 60,
        "genres": null,
        "fullText": " 胡夏",
        "orderArtistName": "胡夏",
        "size": 1714942860,
        "mbzArtistId": "2ccbc670-5fe9-450a-a4ab-4d87131214b3",
        "smallImageUrl": "https://i.scdn.co/image/ab67616d0000485129c9ac0b10fb4f016de87b11",
        "mediumImageUrl": "https://i.scdn.co/image/ab67616d00001e0229c9ac0b10fb4f016de87b11",
        "largeImageUrl": "https://i.scdn.co/image/ab67616d0000b27329c9ac0b10fb4f016de87b11",
        "externalUrl": "https://www.last.fm/music/%E8%83%A1%E5%A4%8F",
        "externalInfoUpdatedAt": "2024-04-18T16:10:03.997920721+08:00"
    }
]
```

响应头：

- `x-total-count`: 总行数

### getCoverArt 封面图片

参见 Subsonic 的 [getCoverArt](./subsonic#getcoverart-封面图片)

### playlist 创建歌单

POST: `[host]/api/playlist`

body(`application/json`):

| 参数名 | 备注 |
| --- | --- |
| name | 歌单名 |
| comment | 评论 |
| public | 其他人是否可见 |

响应内容：

```json
{
    "id": "775cca70-cd09-4029-9858-583098bef519"
}
```

### playlist/[id] 删除歌单

DELETE: `[host]/api/playlist/[id]`

响应内容：

```json
{}
```

### song/[id] 获取歌曲信息

GET: `[host]/api/song/[id]`

### playlist 获取歌单列表

GET: `[host]/api/playlist`

query:

| 参数名 | 备注 |
| --- | --- |
| _start | 起始行数，0开始 |
| _end | 结束行数，_end 和 _start 都等于 0 时可以查询全部 |
| _order | 排序，可选值 `ASC`, `DESC` |
| _sort | 排序方式，可选值 `random`, `name`, 可用`,`分割多个排序方式，如 `max_year asc,date asc` |

响应内容：

```json
[
    {
        "id": "355c94bd-4bef-485a-8945-d6d9d02191cd",
        "name": "1999年老歌by慕星人",
        "comment": "",
        "duration": 8280.36,
        "size": 951975104,
        "songCount": 31,
        "ownerName": "userA",
        "ownerId": "34c42e25-70f8-42d3-83ff-6442b9a341a4",
        "public": false,
        "path": "",
        "sync": false,
        "createdAt": "2024-04-09T15:28:28.917434949+08:00",
        "updatedAt": "2024-04-17T22:32:12.507824702+08:00",
        "rules": null,
        "evaluatedAt": null
    },
    {
        "id": "bd200cad-839e-4818-85af-7e438fb6aef0",
        "name": "15515",
        "comment": "",
        "duration": 170.67,
        "size": 19324940,
        "songCount": 1,
        "ownerName": "userB",
        "ownerId": "631ec3f3-0d00-4648-b404-ce4e95c305f2",
        "public": false,
        "path": "",
        "sync": false,
        "createdAt": "2024-03-17T18:55:34.432021369+08:00",
        "updatedAt": "2024-03-17T18:55:47.208985366+08:00",
        "rules": null,
        "evaluatedAt": null
    },
]
```

响应头：

- `x-total-count`: 总行数

### setRating 评分

参见 Subsonic 的 [setRating](./subsonic#setrating-评分) 接口。

### getScanStatus 获取扫描状态

参见 Subsonic 的 [getScanStatus](./subsonic#getscanstatus-获取扫描状态) 接口。

:::tip

这个接口获取到的歌曲数量可能与实际不符，建议从歌曲列表接口的响应头中获取歌曲总数。

:::

### scrobble 滚动播放记录

参见 Subsonic 的 [scrobble](./subsonic#scrobble-滚动播放记录) 接口。

### search2 搜索歌曲/专辑/歌手

参见 Subsonic 的 [search2](./subsonic#search2-搜索歌曲专辑歌手) 接口。

### getSimilarSongs 获取相似歌曲

参见 Subsonic 的 [getSimilarSongs](./subsonic#getsimilarsongs-获取相似歌曲) 接口。

### song 获取歌曲列表

GET: `[host]/api/song`

query:

| 参数名 | 备注 |
| --- | --- |
| _start | 起始行数，0开始 |
| _end | 结束行数，_end 和 _start 都等于 0 时可以查询全部歌手 |
| _order | 排序，可选值 `ASC`, `DESC` |
| _sort | 排序方式，可选值 `random`, `createdAt`, `max_year`, `play_count`, `play_date`, `title`, `album`, `rating`, 可用`,`分割多个排序方式，如 `max_year asc,date asc` |
| album_id | 专辑id |
| starred | 收藏状态 |
| title | 标题 |

响应内容：

```json
[
    {
        "playCount": 14,
        "playDate": "2024-04-18T07:37:46.658+08:00",
        "rating": 4,
        "starred": true,
        "starredAt": "2024-03-02T01:06:30.37479538+08:00",
        "bookmarkPosition": 0,
        "id": "be7daa6fc04bbbed2e0aaf15fc0b48df",
        "path": "/volume1/music/胡夏/放下/胡夏-放下.flac",
        "title": "放下",
        "album": "放下",
        "artistId": "6d095fad618e04185bd66998450041da",
        "artist": "胡夏",
        "albumArtistId": "6d095fad618e04185bd66998450041da",
        "albumArtist": "胡夏",
        "albumId": "2e7e41725443fa5e8a637a4668e63e98",
        "hasCoverArt": true,
        "trackNumber": 1,
        "discNumber": 0,
        "year": 2013,
        "date": "2013",
        "originalYear": 0,
        "releaseYear": 0,
        "size": 35163552,
        "suffix": "flac",
        "duration": 337.08,
        "bitRate": 822,
        "channels": 2,
        "genre": "",
        "genres": null,
        "fullText": " 放下 胡夏",
        "orderTitle": "放下",
        "orderAlbumName": "放下",
        "orderArtistName": "胡夏",
        "orderAlbumArtistName": "胡夏",
        "compilation": false,
        "lyrics": "[{\"lang\":\"xxx\",\"line\":[{\"start\":0,\"value\":\"作词 : 丁丁张\"},{\"start\":370,\"value\":\"作曲 : 陈嵩\"},{\"start\":750,\"value\":\"风吹凉一杯茶\"},{\"start\":5800,\"value\":\"夕阳跑赢了老马\"},{\"start\":10400,\"value\":\"回头看雪染白长头发\"},{\"start\":19450,\"value\":\"少年被风催大\"},{\"start\":24350,\"value\":\"容颜未改心有疤\"},{\"start\":28500,\"value\":\"我爱你爱让我放下\"},{\"start\":38370,\"value\":\"放下\"},{\"start\":42920,\"value\":\"一只手握不住流沙\"},{\"start\":49220,\"value\":\"两双眼留不住落花\"},{\"start\":55480,\"value\":\"风吹草云落下你心如野马\"},{\"start\":62280,\"value\":\"等下时光请等一下\"},{\"start\":68440,\"value\":\"千只雀追不上流霞\"},{\"start\":74440,\"value\":\"万只蝶抵不过霜打\"},{\"start\":81540,\"value\":\"水滴石风在刮我声音沙哑\"},{\"start\":87500,\"value\":\"放下容我将你放下\"},{\"start\":94100,\"value\":\"天地江湖日月\"},{\"start\":95550,\"value\":\"不留不念不说话\"},{\"start\":100450,\"value\":\"繁华世界弱水\"},{\"start\":101850,\"value\":\"三千一瓢怎盛下\"},{\"start\":106100,\"value\":\"风吹凉一杯茶\"},{\"start\":109250,\"value\":\"夕阳跑赢了老马\"},{\"start\":112350,\"value\":\"回头看雪染白长头发\"},{\"start\":118600,\"value\":\"少年被风催大\"},{\"start\":121850,\"value\":\"容颜未改心有疤\"},{\"start\":125060,\"value\":\"我爱你爱让我放下\"},{\"start\":147120,\"value\":\"一个人走不到天涯\"},{\"start\":153420,\"value\":\"两场雪封不住嫩芽\"},{\"start\":159720,\"value\":\"月升起云落下你笑颜如花\"},{\"start\":166370,\"value\":\"等下时光请等一下\"},{\"start\":172370,\"value\":\"千个字说不出情话\"},{\"start\":178670,\"value\":\"万封信写不完牵挂\"},{\"start\":185310,\"value\":\"山走远风在刮我心乱如麻\"},{\"start\":191710,\"value\":\"放下容我将你放下\"},{\"start\":198460,\"value\":\"天地江湖日月\"},{\"start\":199860,\"value\":\"不留不念不说话\"},{\"start\":204710,\"value\":\"繁华世界弱水\"},{\"start\":206110,\"value\":\"三千一瓢怎盛下\"},{\"start\":210260,\"value\":\"风吹凉一杯茶\"},{\"start\":213410,\"value\":\"夕阳跑赢了老马\"},{\"start\":216560,\"value\":\"回头看雪染白长头发\"},{\"start\":222910,\"value\":\"少年被风催大\"},{\"start\":226670,\"value\":\"容颜未改心有疤\"},{\"start\":229210,\"value\":\"我爱你爱让我放下\"},{\"start\":235510,\"value\":\"风吹凉一杯茶\"},{\"start\":238660,\"value\":\"夕阳跑赢了老马\"},{\"start\":241810,\"value\":\"回头看雪染白长头发\"},{\"start\":248690,\"value\":\"少年被风催大\"},{\"start\":251210,\"value\":\"容颜未改心有疤\"},{\"start\":258830,\"value\":\"我爱你爱让我放下\"},{\"start\":267250,\"value\":\"忘了你爱让我放下\"}],\"synced\":true}]",
        "rgAlbumGain": -6.4,
        "rgAlbumPeak": 0.810242,
        "rgTrackGain": -6.4,
        "rgTrackPeak": 0.810242,
        "createdAt": "2024-03-02T01:04:46.424670828+08:00",
        "updatedAt": "2024-03-21T20:41:28.340360006+08:00"
    }
]
```

响应头：

- `x-total-count`: 总行数

:::caution

当 `_sort` = `createdAt` 时，最多可以获取到 5w 条记录，再往后服务端会报错。

:::

### getTopSongs 获取歌手的热门歌曲

参见 Subsonic 的 [getTopSongs](./subsonic#gettopsongs-获取歌手的热门歌曲) 接口。

### playlist/tracks 获取歌单中的歌曲列表

GET: `[host]/api/playlist/[id]/tracks`

query:

| 参数名 | 备注 |
| --- | --- |
| _start | 起始行数，0开始 |
| _end | 结束行数，_end 和 _start 都等于 0 时可以查询全部 |
| _order | 排序，可选值 `ASC`, `DESC` |
| _sort | 排序方式，可选值 `id`, `createdAt`, 可用`,`分割多个排序方式，如 `max_year asc,date asc` |
| playlist_id | 歌单id |

响应内容：

```json
[
    {
        "id": "1",
        "mediaFileId": "45bbcdc311aeb7c4cfd4ab5fb8db3b68",
        "playlistId": "355c94bd-4bef-485a-8945-d6d9d02191cd",
        "playCount": 5,
        "playDate": "2024-03-23T15:52:34.334+08:00",
        "rating": 0,
        "starred": true,
        "starredAt": "2024-02-05T14:07:28.428223292+08:00",
        "bookmarkPosition": 0,
        "path": "/volume1/music/张宇/雨一直下/张宇-雨一直下.flac",
        "title": "雨一直下",
        "album": "雨一直下",
        "artistId": "1fed6de3753b8cf668a4eb4c485a70cb",
        "artist": "张宇",
        "albumArtistId": "1fed6de3753b8cf668a4eb4c485a70cb",
        "albumArtist": "张宇",
        "albumId": "986a826c9d21925f2be641d370d81e32",
        "hasCoverArt": true,
        "trackNumber": 1,
        "discNumber": 0,
        "year": 1999,
        "date": "1999",
        "originalYear": 0,
        "releaseYear": 0,
        "size": 37831941,
        "suffix": "flac",
        "duration": 290.31,
        "bitRate": 1035,
        "channels": 2,
        "genre": "",
        "genres": null,
        "fullText": " 张宇 雨一直下",
        "orderTitle": "雨一直下",
        "orderAlbumName": "雨一直下",
        "orderArtistName": "张宇",
        "orderAlbumArtistName": "张宇",
        "compilation": false,
        "lyrics": "[{\"lang\":\"xxx\",\"line\":[{\"start\":0,\"value\":\"作词 : 十一郎\"},{\"start\":810,\"value\":\"作曲 : 张宇\"},{\"start\":1630,\"value\":\"编曲 : Michael Thompson\"},{\"start\":2450,\"value\":\"\"},{\"start\":40130,\"value\":\"雨一直下\"},{\"start\":43500,\"value\":\"气氛不算融洽\"},{\"start\":48150,\"value\":\"在同个屋檐下\"},{\"start\":49790,\"value\":\"你渐渐感到心在变化\"},{\"start\":53760,\"value\":\"你爱着他\"},{\"start\":57010,\"value\":\"也许也带着恨吧\"},{\"start\":61540,\"value\":\"青春耗了一大半\"},{\"start\":63380,\"value\":\"原来只是陪他玩耍\"},{\"start\":67330,\"value\":\"正想离开他\"},{\"start\":70830,\"value\":\"他却拿着鲜花\"},{\"start\":75390,\"value\":\"说不着边的话\"},{\"start\":77090,\"value\":\"让整个场面更加尴尬\"},{\"start\":80980,\"value\":\"不可思议吧\"},{\"start\":84580,\"value\":\"梦在瞬间崩塌\"},{\"start\":88920,\"value\":\"为何当初那么傻\"},{\"start\":90770,\"value\":\"还一心想要嫁给他\"},{\"start\":95340,\"value\":\"就是爱到深处 才怨他\"},{\"start\":99620,\"value\":\"舍不舍得 都断了吧\"},{\"start\":102560,\"value\":\"那是从来\"},{\"start\":103670,\"value\":\"都没有后路的悬崖\"},{\"start\":109030,\"value\":\"就是爱到深处 才由他\"},{\"start\":113200,\"value\":\"碎了心 也要放得下\"},{\"start\":116300,\"value\":\"难道忘了那爱他的伤\"},{\"start\":119070,\"value\":\"已密密麻麻\"},{\"start\":122380,\"value\":\"雨一直下\"},{\"start\":125740,\"value\":\"气氛不算融洽\"},{\"start\":130210,\"value\":\"在同个屋檐下\"},{\"start\":131950,\"value\":\"你渐渐感到心在变化\"},{\"start\":135890,\"value\":\"不可思议吧\"},{\"start\":139390,\"value\":\"梦在瞬间崩塌\"},{\"start\":143700,\"value\":\"为何当初那么傻\"},{\"start\":145580,\"value\":\"还一心想要嫁给他\"},{\"start\":150120,\"value\":\"就是爱到深处 才怨他\"},{\"start\":154360,\"value\":\"舍不舍得 都断了吧\"},{\"start\":157440,\"value\":\"那是从来\"},{\"start\":158480,\"value\":\"都没有后路的悬崖\"},{\"start\":163810,\"value\":\"就是爱到深处 才由他\"},{\"start\":168080,\"value\":\"碎了心 也要放得下\"},{\"start\":171150,\"value\":\"难道忘了那爱他的伤\"},{\"start\":173920,\"value\":\"已密密麻麻\"},{\"start\":177090,\"value\":\"不要再为了他挣扎\"},{\"start\":180270,\"value\":\"不要再为他左牵右挂\"},{\"start\":183760,\"value\":\"今后不管他爱不爱谁\"},{\"start\":186910,\"value\":\"快乐吗 都随他\"},{\"start\":204950,\"value\":\"就是爱到深处 才由他\"},{\"start\":209130,\"value\":\"碎了心 也要放得下\"},{\"start\":212180,\"value\":\"难道忘了那爱他的伤\"},{\"start\":215010,\"value\":\"已密密麻麻\"},{\"start\":218590,\"value\":\"就是爱到深处 才怨他\"},{\"start\":222760,\"value\":\"舍不舍得都断了吧\"},{\"start\":225920,\"value\":\"那是从来\"},{\"start\":227000,\"value\":\"都没有后路的悬崖\"},{\"start\":232340,\"value\":\"就是爱到深处 才由他\"},{\"start\":236570,\"value\":\"碎了心 也要放得下\"},{\"start\":239640,\"value\":\"难道忘了那爱他的伤\"},{\"start\":242430,\"value\":\"已密密麻麻\"},{\"start\":246940,\"value\":\"\"},{\"start\":247360,\"value\":\"Arranged By – Michael Thompson\"},{\"start\":247590,\"value\":\"Acoustic Guitar – Michael Thompson\"},{\"start\":247760,\"value\":\"Electric Guitar – Michael Thompson\"},{\"start\":247940,\"value\":\"Guitar [Wah Wah] – Michael Thompson\"},{\"start\":248130,\"value\":\"Soloist – Michael Thompson\"},{\"start\":248330,\"value\":\"Bass – Randy Jackson\"},{\"start\":248510,\"value\":\"Drums – Vinnie Colaiuta\"},{\"start\":248690,\"value\":\"Engineer – Bill Drescher\"},{\"start\":248880,\"value\":\"Engineer – David N. Cole\"},{\"start\":249050,\"value\":\"Keyboards – Jeffrey \\\"CJ\\\" Vanston\"},{\"start\":249230,\"value\":\"Programmed By – Jeffrey \\\"CJ\\\" Vanston\"},{\"start\":249400,\"value\":\"Synth – Jeffrey \\\"CJ\\\" Vanston\"},{\"start\":249590,\"value\":\"Lyrics By – 萧慧文\"},{\"start\":249780,\"value\":\"Music By – 张宇\"},{\"start\":249970,\"value\":\"Producer – David N. Cole, Phil Chang\"},{\"start\":250140,\"value\":\"Mixed By – David N. Cole\"},{\"start\":250500,\"value\":\"Recorded By – Bill Schnee, Greg Droman, Richard Flack\"}],\"synced\":true}]",
        "rgAlbumGain": -8.76,
        "rgAlbumPeak": 0.998901,
        "rgTrackGain": -9.65,
        "rgTrackPeak": 0.988953,
        "createdAt": "2024-02-04T00:11:12.548089502+08:00",
        "updatedAt": "2024-03-21T21:42:11.165237602+08:00"
    }
]
```

响应头：

- `x-total-count`: 总行数

:::tip

`id` 用于从歌单中删除歌曲，从 1 开始计数。

:::

### star 收藏歌曲/专辑/歌手

参见 Subsonic 的 [star](./subsonic#star-收藏歌曲专辑歌手) 接口。

### stream 歌曲播放链接

参见 Subsonic 的 [stream](./subsonic#stream-歌曲播放链接) 接口。

### unstar 取消收藏

参见 Subsonic 的 [unstar](./subsonic#unstar-取消收藏) 接口。

### playlist/[id] 更新歌单

PUT: `[host]/api/playlist/[id]`

body(`application/json`)

| 参数名 | 备注 |
| --- | --- |
| name | 歌单名 |
| comment | 评论 |
| public | 其他人是否可见 |

### playlist/tracks 添加歌曲到歌单

POST: `[host]/api/playlist/[id]/tracks`

body(`application/json`):

| 参数名 | 备注 |
| --- | --- |
| ids | 待添加的歌曲id列表, `,`分割 |

### playlist/tracks 从歌单中移除歌曲

DELETE: `[host]/api/playlist/[id]/tracks`

query:

| 参数名 | 备注 |
| --- | --- |
| id | 待移除的歌曲id，多个id则以 `id=2&id=3` 的形式发起请求 |