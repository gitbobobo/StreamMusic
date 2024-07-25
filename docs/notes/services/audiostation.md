---
sidebar_position: 5
---

# AudioStation 接口文档

:::note 参考文档：

- [DSM 登录 Web API 指南](https://global.synologydownload.com/download/Document/Software/DeveloperGuide/Os/DSM/All/enu/DSM_Login_Web_API_Guide_enu.pdf)

AudioStation 没有官方的接口文档，以下均为抓包所得。

:::

## 认证

:::tip

AudioStation 部分节点返回的是正常的 json 格式，部分节点返回的是转为字符串的 json 格式，需要手动判断并处理一下。

:::

### Serv.php 获取访问地址（可选）

POST: `https://global.quickconnect.cn/Serv.php`

body(`application/json`):

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `1` |
| id | 固定填 `dsm` |
| serverID | quickconnect ID |
| get_ca_fingerprints | 固定填 `true` |
| command | 固定填 `get_server_info` |

response:

```json
{
    "command": "get_server_info",
    "env": {
        "control_host": "cnc.quickconnect.cn",
        "relay_region": "cn"
    },
    "errno": 0,
    "server": {
        "ca_fingerprints": [
            "xxx",
            "xxxx",
            "xxxxx"
        ],
        "ddns": "NULL",
        "ds_state": "CONNECTED",
        "external": {
            "ip": "00.00.00.000",
            "ipv6": "::"
        },
        "fqdn": "NULL",
        "gateway": "192.168.00.1",
        "interface": [
            {
                "ip": "192.168.00.5",
                "ipv6": [
                    {
                        "addr_type": 0,
                        "address": "xxxx:15b0:xxxx:4246:xxxx:d0ff:xxxx:db15",
                        "prefix_length": 64,
                        "scope": "global"
                    },
                    {
                        "addr_type": 32,
                        "address": "fe80::xxxx:d0ff:xxxx:db15",
                        "prefix_length": 64,
                        "scope": "link"
                    }
                ],
                "mask": "255.255.255.0",
                "name": "eth0"
            }
        ],
        "ipv6_tunnel": [],
        "is_bsm": false,
        "pingpong_path": "",
        "redirect_prefix": "",
        "serverID": "0000000",
        "tcp_punch_port": 0,
        "udp_punch_port": 45785
    },
    "service": {
        "port": 5000,
        "ext_port": 0,
        "pingpong": "UNKNOWN",
        "pingpong_desc": []
    },
    "smartdns": {
        "host": "xxxx.direct.quickconnect.cn",
        "lan": [
            "192-168-00-5.xxxx.direct.quickconnect.cn"
        ],
        "lanv6": [
            "syn6-xxxx.xxxx.direct.quickconnect.cn",
            "syn6-xxxxxx.xxxx.direct.quickconnect.cn"
        ],
        "hole_punch": "127-0-0-1.xxxx.direct.quickconnect.cn"
    },
    "version": 1
}
```

:::note

server, service, env 字段可能不存在，不存在时表示此节点未保存当前 quickconnect ID 的信息，需要通过 `sites` 字段保存的其他节点列表重新调用此接口查询。

:::

### Serv.php 开启代理（可选）

controlHost 从上一步的 `env.control_host` 获取，上一步若未获取到 `service.relay_ip`，则表示此时未开启代理，可通过此接口开启代理。

POST: `https://[controlHost]/Serv.php`

body(`application/json`):

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `1` |
| id | 固定填 `dsm` |
| serverID | quickconnect ID |
| platform | 平台，可选值：`Web`, `Android`, `iOS`, `MacOSX`, `Windows`, `Linux` |
| command | 固定填 `request_tunnel` |

response:

```json
{
    "command": "request_tunnel",
    "env": {
        "control_host": "cnc.quickconnect.cn",
        "relay_region": "xxx"
    },
    "errno": 0,
    "server": {
        "ddns": "NULL",
        "ds_state": "CONNECTED",
        "external": {
            "ip": "00.00.00.000",
            "ipv6": "::"
        },
        "fqdn": "NULL",
        "gateway": "192.168.00.5",
        "interface": [
            {
                "ip": "192.168.00.00",
                "ipv6": [
                    {
                        "addr_type": 0,
                        "address": "xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:db15",
                        "prefix_length": 64,
                        "scope": "global"
                    },
                    {
                        "addr_type": 32,
                        "address": "fe80::xxxx:xxxx:xxxx:db15",
                        "prefix_length": 64,
                        "scope": "link"
                    }
                ],
                "mask": "255.255.255.0",
                "name": "eth0"
            }
        ],
        "ipv6_tunnel": [],
        "is_bsm": false,
        "pingpong_path": "",
        "redirect_prefix": "",
        "serverID": "0000",
        "tcp_punch_port": 0,
        "udp_punch_port": 45785
    },
    "service": {
        "port": 5000,
        "ext_port": 0,
        "pingpong": "UNKNOWN",
        "pingpong_desc": [],
        "relay_ip": "xx.xx.xxx.xx",
        "relay_dn": "synr-xxx.xxxx.direct.quickconnect.cn",
        "relay_port": 39833,
        "vpn_ip": "xxx.xxx.xxx.xxx",
        "https_ip": "xxx.xxx.xxx.xxx",
        "https_port": 443
    },
    "smartdns": {
        "host": "xxxx.direct.quickconnect.cn",
        "lan": [
            "192-168-00-00.xxxx.direct.quickconnect.cn"
        ],
        "lanv6": [
            "syn6-xxxx.xx.direct.quickconnect.cn",
            "syn6-xxxx.xx.direct.quickconnect.cn"
        ],
        "hole_punch": "127-0-0-1.xxxx.direct.quickconnect.cn"
    },
    "version": 1
}
```

### pingpong.cgi 测试服务器连通性

通过以上两步可以获取到包括内网地址，外网地址以及代理地址，通过此接口是否超时判断地址是否可用，程序中按自定义的优先级使用即可。

GET: `[host]/webman/pingpong.cgi?quickconnect=true`

### query.cgi 获取可用端点

GET: `[host]/webapi/query.cgi`

query:

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `1` |
| api | 固定填 `SYNO.API.Info` |
| method | 固定填 `query` |
| query | 查询范围，可选值：`all` |

```json
{
    "data": {
        "SYNO.API.Auth": {
            "maxVersion": 7,
            "minVersion": 1,
            "path": "entry.cgi"
        },
        "SYNO.API.Auth.Key": {
            "maxVersion": 7,
            "minVersion": 7,
            "path": "entry.cgi",
            "requestFormat": "JSON"
        },
        "SYNO.API.Auth.Key.Code": {
            "maxVersion": 7,
            "minVersion": 7,
            "path": "entry.cgi",
            "requestFormat": "JSON"
        },
        "SYNO.API.Auth.RedirectURI": {
            "maxVersion": 1,
            "minVersion": 1,
            "path": "entry.cgi",
            "requestFormat": "JSON"
        },
        "SYNO.API.Auth.Type": {
            "maxVersion": 1,
            "minVersion": 1,
            "path": "entry.cgi",
            "requestFormat": "JSON"
        },
        "SYNO.API.Auth.UIConfig": {
            "maxVersion": 1,
            "minVersion": 1,
            "path": "entry.cgi",
            "requestFormat": "JSON"
        },
        "SYNO.API.Encryption": {
            "maxVersion": 1,
            "minVersion": 1,
            "path": "entry.cgi",
            "requestFormat": "JSON"
        },
        "SYNO.API.Info": {
            "maxVersion": 1,
            "minVersion": 1,
            "path": "entry.cgi",
            "requestFormat": "JSON"
        },
        "SYNO.API.OTP": {
            "maxVersion": 1,
            "minVersion": 1,
            "path": "otp.cgi"
        },
        "SYNO.AudioPlayer": {
            "maxVersion": 2,
            "minVersion": 2,
            "path": "entry.cgi",
            "requestFormat": "JSON"
        },
        "SYNO.AudioPlayer.Stream": {
            "maxVersion": 2,
            "minVersion": 2,
            "path": "entry.cgi",
            "requestFormat": "JSON"
        },
        "SYNO.AudioStation.Album": {
            "maxVersion": 3,
            "minVersion": 1,
            "path": "AudioStation/album.cgi"
        },
        "SYNO.AudioStation.Artist": {
            "maxVersion": 4,
            "minVersion": 1,
            "path": "AudioStation/artist.cgi"
        },
        "SYNO.AudioStation.Browse.Playlist": {
            "maxVersion": 1,
            "minVersion": 1,
            "path": "entry.cgi",
            "requestFormat": "JSON"
        },
        "SYNO.AudioStation.Composer": {
            "maxVersion": 2,
            "minVersion": 1,
            "path": "AudioStation/composer.cgi"
        },
        "SYNO.AudioStation.Cover": {
            "maxVersion": 3,
            "minVersion": 1,
            "path": "AudioStation/cover.cgi"
        },
        "SYNO.AudioStation.Download": {
            "maxVersion": 1,
            "minVersion": 1,
            "path": "AudioStation/download.cgi"
        },
        "SYNO.AudioStation.Folder": {
            "maxVersion": 3,
            "minVersion": 1,
            "path": "AudioStation/folder.cgi"
        },
        "SYNO.AudioStation.Genre": {
            "maxVersion": 3,
            "minVersion": 1,
            "path": "AudioStation/genre.cgi"
        },
        "SYNO.AudioStation.Info": {
            "maxVersion": 6,
            "minVersion": 1,
            "path": "AudioStation/info.cgi"
        },
        "SYNO.AudioStation.Lyrics": {
            "maxVersion": 2,
            "minVersion": 1,
            "path": "AudioStation/lyrics.cgi"
        },
        "SYNO.AudioStation.LyricsSearch": {
            "maxVersion": 2,
            "minVersion": 1,
            "path": "AudioStation/lyrics_search.cgi"
        },
        "SYNO.AudioStation.MediaServer": {
            "maxVersion": 1,
            "minVersion": 1,
            "path": "AudioStation/media_server.cgi"
        },
        "SYNO.AudioStation.Pin": {
            "maxVersion": 1,
            "minVersion": 1,
            "path": "entry.cgi",
            "requestFormat": "JSON"
        },
        "SYNO.AudioStation.Playlist": {
            "maxVersion": 3,
            "minVersion": 1,
            "path": "AudioStation/playlist.cgi"
        },
        "SYNO.AudioStation.Proxy": {
            "maxVersion": 2,
            "minVersion": 1,
            "path": "AudioStation/proxy.cgi"
        },
        "SYNO.AudioStation.Radio": {
            "maxVersion": 2,
            "minVersion": 1,
            "path": "AudioStation/radio.cgi"
        },
        "SYNO.AudioStation.RemotePlayer": {
            "maxVersion": 3,
            "minVersion": 1,
            "path": "AudioStation/remote_player.cgi"
        },
        "SYNO.AudioStation.RemotePlayerStatus": {
            "maxVersion": 2,
            "minVersion": 1,
            "path": "AudioStation/remote_player_status.cgi"
        },
        "SYNO.AudioStation.Search": {
            "maxVersion": 1,
            "minVersion": 1,
            "path": "AudioStation/search.cgi"
        },
        "SYNO.AudioStation.Song": {
            "maxVersion": 3,
            "minVersion": 1,
            "path": "AudioStation/song.cgi"
        },
        "SYNO.AudioStation.Stream": {
            "maxVersion": 2,
            "minVersion": 1,
            "path": "AudioStation/stream.cgi"
        },
        "SYNO.AudioStation.Tag": {
            "maxVersion": 1,
            "minVersion": 1,
            "path": "entry.cgi",
            "requestFormat": "JSON"
        },
        "SYNO.AudioStation.VoiceAssistant.Browse": {
            "maxVersion": 1,
            "minVersion": 1,
            "path": "entry.cgi",
            "requestFormat": "JSON"
        },
        "SYNO.AudioStation.VoiceAssistant.Challenge": {
            "maxVersion": 1,
            "minVersion": 1,
            "path": "entry.cgi",
            "requestFormat": "JSON"
        },
        "SYNO.AudioStation.VoiceAssistant.Info": {
            "maxVersion": 1,
            "minVersion": 1,
            "path": "entry.cgi",
            "requestFormat": "JSON"
        },
        "SYNO.AudioStation.VoiceAssistant.Stream": {
            "maxVersion": 1,
            "minVersion": 1,
            "path": "entry.cgi",
            "requestFormat": "JSON"
        },
        "SYNO.AudioStation.WebPlayer": {
            "maxVersion": 1,
            "minVersion": 1,
            "path": "AudioStation/web_player.cgi"
        },
        "SYNO.Auth.ForgotPwd": {
            "maxVersion": 1,
            "minVersion": 1,
            "path": "entry.cgi",
            "requestFormat": "JSON"
        },
        "SYNO.Auth.RescueEmail": {
            "maxVersion": 1,
            "minVersion": 1,
            "path": "entry.cgi",
            "requestFormat": "JSON"
        },
    },
    "success": true
}
```

通过此端点返回的端点列表，可获取到对应端点的请求路径，在后续请求中均会先通过固定的`端点 key` 来获取请求路径，建议第一次获取之后在程序中保存一下方便后续使用。

### Auth 登录

key：`SYNO.API.Auth`

POST: `[host]/webapi/[path]`

body(`application/json`):

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `6` |
| api | 固定填 `SYNO.API.Auth` |
| method | 固定填 `login` |
| session | 固定填 `audiostation` |
| device_name | 设备名 |
| account | 用户名 |
| passwd | 密码，若用户配置了二次验证，在登录重试时应填上次登录返回的 token |
| enable_device_token | 固定填 `yes` 以保证下次自动登录时无需再让用户输入验证码 |
| otp_code | OTP 验证码，可选 |
| device_id | 设备 ID，登录成功后 `did` 字段的值 |

403 response（需要传 OTP 验证码）:

```json
{
    "error": {
        "code": 403,
        "errors": {
            "token": "eyJ0eXAiOiJKV1Qxxx",
            "types": [
                {
                    "type": "otp"
                }
            ]
        }
    },
    "success": false
}
```

response:

```json
{
    "data": {
        "did": "Bonqh4M59r3vxxx",
        "is_portal_port": false,
        "sid": "EGVGrBZsJ7fKJ1GpYhplKJewLxxx"
    },
    "success": true
}
```

header:

```json
{
    "set-cookie": [
        "id=xxxx;expires=Sat, 27-Apr-2024 03:09:10 GMT;max-age=604800;path=/;HttpOnly",
        "did=xxxx;expires=Sun, 20-Apr-2025 03:09:10 GMT;max-age=31536000;path=/;HttpOnly"
    ]
}
```

程序在登录成功后，应保存 `did`, `sid`, `id` 字段的值，在 DSM 6 中，仅首次登录后会返回 did。

## 请求节点

以下请求均需从上面的 [获取可用端点](#querycgi-获取可用端点) 取得对应的访问路径，最终组装的路径如：`[host]/webapi/[path]`，下文不再赘述，仅写出端点对应的 key，若请求中需要填写参数，则为参数名 `api` 的值。

### Album 获取专辑列表

GET query:

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `3` |
| api | `SYNO.AudioStation.Album` |
| method | `list` |
| library | 查询范围，可选值： `all`, `personal` |
| additional | `avg_rating` |
| offset | 行数偏移 |
| limit | 结果数量，可选 |
| sort_by | 排序方式，可选值：`time`, `random`, `year`, `name`, `display_artist`, `avg_rating` |
| sort_direction | 排序，可选值：`ASC`, `DESC` |
| filter | 专辑名，可选 |
| artist | 歌手名，可选 |
| genre | 类型名，可选 |

response:

```json
{
    "data": {
        "albums": [
            {
                "additional": {
                    "avg_rating": {
                        "rating": 5
                    }
                },
                "album_artist": "麦小兜",
                "artist": "",
                "display_artist": "麦小兜",
                "name": "9420",
                "year": 2017
            }
        ],
        "offset": 0,
        "total": 3528
    },
    "success": true
}
```

### Artist 获取歌手列表

GET query:

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `3` |
| api | `SYNO.AudioStation.Artist` |
| method | `list` |
| library | 查询范围，可选值： `all`, `personal` |
| additional | `avg_rating` |
| genre | 类型名，可选 |
| offset | 行数偏移 |
| limit | 结果数量，可选 |
| sort_by | 排序方式，可选值：`name` |
| sort_direction | 排序，可选值：`ASC`, `DESC` |

response:

```json
{
    "data": {
        "artists": [
            {
                "additional": {
                    "avg_rating": {
                        "rating": 0
                    }
                },
                "name": "多田葵 (ただ あおい)"
            }
        ],
        "offset": 100,
        "total": 939
    },
    "success": true
}
```

:::caution

此接口返回的歌手列表大概率是专辑艺术家列表而非艺术家列表，这会导致部分歌手无法从此接口获取。

:::

### Cover 图片链接

GET query:

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `1` |
| api | `SYNO.AudioStation.Cover` |
| method | 可选值：`getsongcover`, `getcover` |
| library | 查询范围，可选值： `all`, `personal` |
| id | 歌曲ID，`method=getsongcover`时填写 |
| artist_name | 歌手名，`method=getcover` 且要获取歌手图片时填写 |
| album_name | 专辑名，`method=getcover` 且要获取专辑封面时填写 |
| album_artist_name | 专辑艺术家名，`method=getcover` 且要获取专辑封面时填写 |
| _sid | Session ID，登录后的 `sid` 字段 |

### Playlist 创建歌单

POST query:

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `2` |
| api | `SYNO.AudioStation.Playlist` |
| method | `create` |
| library | 查询范围，可选值： `all`, `personal` |
| name | 歌单名 |

response:

```json
{
    "data": {
        "id": "playlist_personal_normal/19"
    },
    "success": true
}
```

### Playlist 删除歌单

POST query:

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `2` |
| api | `SYNO.AudioStation.Playlist` |
| method | `delete` |
| id | 歌单ID |

### Folder 获取目录列表

POST data:

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `2` |
| api | `SYNO.AudioStation.Folder` |
| method | `list` |
| library | `all` |
| additional | 附加信息，可选值：`song_tag`, `song_audio`, `song_rating` |
| sort_by | `song_rating` |
| sort_direction | `ASC` |
| id | 目录ID，不传则查询根目录，示例：`dir_1609` |
| offset | 行数偏移 |
| limit | 结果数量 |

response:

```json
{
    "data": {
        "folder_total": 14,
        "id": "dir_1413",
        "items": [
            {
                "id": "dir_4380",
                "is_personal": false,
                "path": "/music/阿悄/阿悄单曲集",
                "title": "阿悄单曲集",
                "type": "folder"
            },
            {
                "id": "dir_6213",
                "is_personal": false,
                "path": "/music/阿悄/最坚强的...阿悄勇敢作品集",
                "title": "最坚强的...阿悄勇敢作品集",
                "type": "folder"
            },
            {
                "additional": {
                    "song_audio": {
                        "bitrate": 320000,
                        "channel": 2,
                        "codec": "mp3",
                        "container": "mp3",
                        "duration": 213,
                        "filesize": 8633172,
                        "frequency": 44100
                    },
                    "song_rating": {
                        "rating": 0
                    },
                    "song_tag": {
                        "album": "流行网络歌",
                        "album_artist": "",
                        "artist": "徐良/阿悄",
                        "comment": "",
                        "composer": "",
                        "disc": 0,
                        "genre": "Blues",
                        "track": 47,
                        "year": 2008
                    }
                },
                "id": "music_4607",
                "path": "/music/阿悄/徐良 _ 阿悄 - 犯贱.mp3",
                "title": "犯贱",
                "type": "file"
            }
        ],
        "offset": 0,
        "total": 15
    },
    "success": true
}
```

### Genre 获取类型列表

POST data:

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `3` |
| api | `SYNO.AudioStation.Genre` |
| method | `list` |
| library | 查询范围，可选值： `all`, `personal` |
| offset | 行数偏移 |
| limit | 结果数量，可选 |
| sort_by | 排序方式，`name` |
| sort_direction | 排序方向，`ASC`, `DESC` |

response:

```json
{
    "data": {
        "genres": [
            {
                "additional": {
                    "avg_rating": {
                        "rating": 0
                    }
                },
                "name": ""
            },
            {
                "additional": {
                    "avg_rating": {
                        "rating": 5
                    }
                },
                "name": "国际流行"
            },
            {
                "additional": {
                    "avg_rating": {
                        "rating": 5
                    }
                },
                "name": "国语流行"
            },
            {
                "additional": {
                    "avg_rating": {
                        "rating": 0
                    }
                },
                "name": ""
            }
        ],
        "offset": 0,
        "total": 44
    },
    "success": true
}
```

:::note
AudioStation 的空字符串显示为`未知的歌曲类型`.
:::

### Lyrics 获取歌词

GET query:

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `2` |
| api | `SYNO.AudioStation.Lyrics` |
| method | `getlyrics` |
| id | 歌曲ID |

response:

```json
{
    "data": {
        "lyrics": ""
    },
    "success": true
}
```

### LyricsSearch 搜索歌词

此接口依赖 AudioStation 安装的歌词插件。

GET query:

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `2` |
| api | `SYNO.AudioStation.LyricsSearch` |
| method | `searchlyrics` |
| title | 标题 |
| artist | 歌手 |
| limit | 结果数量 |
| additional | `full_lyrics` |

response:

```json
{
    "data": {
        "lyrics": [
            {
                "additional": {
                    "full_lyrics": "[ti:原来你也在这里 (《她从海上来》电视剧主题曲)]\n[ar:刘若英]\n[al:我的失败与伟大 2nd Version]\n[by:]\n[offset:0]\n[00:00.00]原来你也在这里 - 刘若英 (Rene Liu)\n[00:03.45]词：姚谦\n[00:06.90]曲：中岛美雪\n[00:10.35]编曲：屠颖\n[00:13.81]请允许我尘埃落定\n[00:16.93]用沉默埋葬了过去\n[00:20.29]满身风雨我从海上来\n[00:23.42]才隐居在这沙漠里\n[00:26.37]\n[00:27.04]该隐瞒的事总清晰\n[00:30.25]千言万语只能无语\n[00:33.61]爱是天时地利的迷信\n[00:36.69]喔 原来你也在这里\n[00:40.30]啊 那一个人\n[00:42.88]是不是只存在梦境里\n[00:46.24]\n[00:47.09]为什么我用尽全身力气\n[00:50.27]却换来半生回忆\n[00:52.57]\n[00:53.80]若不是你渴望眼睛\n[00:56.98]若不是我救赎心情\n[00:59.81]\n[01:00.33]在千山万水人海相遇\n[01:03.42]喔 原来你也在这里\n[01:06.43]\n[01:37.15]请允许我尘埃落定\n[01:40.34]用沉默埋葬了过去\n[01:43.60]满身风雨我从海上来\n[01:46.78]才隐居在这沙漠里\n[01:49.42]\n[01:50.27]该隐瞒的事总清晰\n[01:53.59]千言万语只能无语\n[01:56.98]爱是天时地利的迷信\n[02:00.14]喔 原来你也在这里\n[02:03.59]啊 那一个人\n[02:06.18]是不是只存在梦境里\n[02:09.46]\n[02:10.17]为什么我用尽全身力气\n[02:13.56]却换来半生回忆\n[02:16.28]\n[02:17.05]若不是你渴望眼睛\n[02:20.36]若不是我救赎心情\n[02:23.63]在千山万水人海相遇\n[02:26.82]喔 原来你也在这里\n[02:30.44]啊 那一个人\n[02:32.86]是不是只存在梦境里\n[02:36.26]\n[02:37.01]为什么我用尽全身力气\n[02:40.30]却换来半生回忆\n[02:42.96]\n[02:43.70]若不是你渴望眼睛\n[02:47.00]若不是我救赎心情\n[02:50.24]在千山万水人海相遇\n[02:53.47]喔 原来你也在这里\n[02:56.44]\n[02:56.96]该隐瞒的事总清晰\n[03:00.33]千言万语只能无语\n[03:03.72]爱是天时地利的迷信\n[03:07.01]喔 原来你也在这里"
                },
                "artist": "刘若英",
                "id": "Lrc@136473",
                "partial_lyrics": "136473; Album: 我的失败与伟大",
                "plugin": "pluginName",
                "title": "原来你也在这里"
            }
        ]
    },
    "success": true
}
```

### Playlist 获取歌单列表

GET query:

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `2` |
| api | `SYNO.AudioStation.Playlist` |
| method | `list` |
| library | 查询范围，可选值： `all`, `personal` |
| offset | 行数偏移 |
| limit | 结果数量，可选 |

response:

```json
{
    "data": {
        "offset": 0,
        "playlists": [
            {
                "id": "playlist_personal_normal/__SYNO_AUDIO_SHARED_SONGS__",
                "library": "personal",
                "name": "__SYNO_AUDIO_SHARED_SONGS__",
                "sharing_status": "none",
                "type": "normal"
            },
            {
                "id": "playlist_personal_normal/19",
                "library": "personal",
                "name": "6655",
                "path": "/homes/xxx/music/playlists",
                "sharing_status": "none",
                "type": "normal"
            },
            {
                "id": "playlist_personal_smart/ぐされ",
                "library": "personal",
                "name": "ぐされ",
                "sharing_status": "valid",
                "type": "smart"
            }
        ],
        "total": 6
    },
    "success": true
}
```

### Song 歌曲评分

POST query:

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `3` |
| api | `SYNO.AudioStation.Song` |
| method | `setrating` |
| id | 歌曲ID |
| rating | 分数，0-5之间 |

### Info 获取服务器信息

GET query:

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `1` |
| api | `SYNO.AudioStation.Info` |
| method | `getinfo` |

response:

```json
{
    "data": {
        "path": "/webman/3rdparty/AudioStation",
        "version": {
            "build": "5508",
            "major": "7",
            "minor": "1"
        }
    },
    "success": true
}
```

### Search 搜索歌曲/专辑/歌手

GET query:

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `1` |
| api |`SYNO.AudioStation.Search` |
| method | `list` |
| library | 查询范围，可选值： `all`, `personal` |
| offset | 行数偏移 |
| limit | 结果数量，可选 |
| keyword | 关键词 |
| sort_by | 排序方式，可选值：`title` |
| sort_direction | 排序，可选值：`ASC`, `DESC` |
| additional | 附加信息，可选值：`song_tag`, `song_audio`, `song_rating` |

response:

```json
{
    "data": {
        "albumTotal": 3,
        "albums": [
            {
                "album_artist": "王菲",
                "artist": "",
                "display_artist": "王菲",
                "name": "王菲",
                "year": 0
            },
            {
                "album_artist": "王菲",
                "artist": "",
                "display_artist": "王菲",
                "name": "王菲 2001同名专辑",
                "year": 0
            },
            {
                "album_artist": "王菲",
                "artist": "",
                "display_artist": "王菲",
                "name": "王菲珍藏集",
                "year": 2004
            }
        ],
        "artistTotal": 2,
        "artists": [
            {
                "name": "王菲"
            },
            {
                "name": "王菲/邓丽君"
            },
        ],
        "songTotal": 0,
        "songs": []
    },
    "success": true
}
```

### Song 获取歌曲列表

POST data:

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `3` |
| api |`SYNO.AudioStation.Song` |
| method | `list` |
| library | 查询范围，可选值： `all`, `personal` |
| offset | 行数偏移 |
| limit | 结果数量，可选 |
| rating_filter | 评分，可选 |
| album_artist | 专辑艺术家，可选 |
| album | 专辑名，可选 |
| artist | 歌手名，可选 |
| genre | 类型名，可选 |
| sort_by | 排序方式，可选值：`title`, `name`, `artist`, `random` |
| sort_direction | 排序，可选值：`ASC`, `DESC` |
| additional | 附加信息列表，可选值：`song_tag`, `song_audio`, `song_rating` |

:::note

目前没有找到如何按添加时间排序的方式，似乎只能按专辑的添加时间排序后，一个个从专辑中获取？

:::

response:

```json
{
    "data": {
        "offset": 0,
        "songs": [
            {
                "additional": {
                    "song_audio": {
                        "bitrate": 982000,
                        "channel": 2,
                        "codec": "flac",
                        "container": "flac",
                        "duration": 238,
                        "filesize": 29618503,
                        "frequency": 44100
                    },
                    "song_rating": {
                        "rating": 0
                    },
                    "song_tag": {
                        "album": "如果没有你",
                        "album_artist": "莫文蔚",
                        "artist": "莫文蔚",
                        "comment": "",
                        "composer": "",
                        "disc": 0,
                        "genre": "",
                        "rg_album_gain": "-8.19",
                        "rg_album_peak": "1",
                        "rg_track_gain": "-8.92",
                        "rg_track_peak": "1",
                        "track": 4,
                        "year": 2006
                    }
                },
                "id": "music_36034",
                "path": "/music/莫文蔚/如果没有你/莫文蔚-24Hrs.flac",
                "title": "24Hrs",
                "type": "file"
            },
        ],
        "total": 59
    },
    "success": true
}
```

### Playlist 获取歌单中的歌曲

GET query:

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `2` |
| api |`SYNO.AudioStation.Playlist` |
| method | `getinfo` |
| library | 查询范围，可选值： `all`, `personal` |
| offset | 行数偏移 |
| limit | 结果数量，可选 |
| id | 歌单ID |
| sort_direction | 排序，可选值：`ASC` |
| additional | 附加信息列表，可选值：`songs_song_tag`, `songs_song_audio`, `songs_song_rating` |

:::note

从歌单中移除歌曲时，传入的 ID 列表是此接口返回的歌曲顺序索引，从 0 开始。

:::

### 收藏歌曲

AudioStation 没有此接口，建议使用评分为 5 星的歌曲来替代，通过 `rating_filter` 可以较为方便地获取到歌曲列表。

### Stream 歌曲播放链接

GET query:

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `2` |
| api | `SYNO.AudioStation.Stream` |
| method | 可选值：`stream`, `transcode` |
| id | 歌曲ID |
| format | 歌曲格式，`method=transcode` 时填写，可选值：`mp3` |
| _sid | Session ID，登录后的 `sid` 字段 |

当 `method=transcode` 时，请求路径后需添加 `0.mp3`，即 `[host]/webapi/[path]/0.mp3?xxx=xx`。

:::note

若歌曲是整轨文件的某个音轨，歌曲 ID 的格式为 `music_v_1111`。对于这种文件我自己尝试是无法播放的，建议识别到歌曲 ID 包含 `_v_` 的歌曲时，强制使用转码的播放链接。

:::

### Playlist 从歌单中移除歌曲

POST query:

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `2` |
| api |`SYNO.AudioStation.Playlist` |
| method | `updatesongs` |
| offset | 待移除的歌曲的起始行数 |
| limit | 需要移除的歌曲数量，注：从起始行数开始的所有歌曲都会被移除 |
| songs | 待添加的歌曲 ID 列表，用于回溯上面两个参数中间误删的歌曲 |
| id | 歌单ID |

:::caution

这个接口的删除逻辑较难理解，建议自己在网页端抓包尝试一下。

:::

### Playlist 添加歌曲到歌单

POST query:

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `2` |
| api |`SYNO.AudioStation.Playlist` |
| method | `updatesongs` |
| offset | `-1` |
| limit | `0` |
| songs | 待添加的歌曲 ID 列表 |
| id | 歌单ID |

### Playlist 重命名歌单

POST query:

| 参数名 | 备注 |
| --- | --- |
| version | 版本，固定填 `2` |
| api |`SYNO.AudioStation.Playlist` |
| method | `rename` |
| new_name | 歌单名 |
| id | 歌单ID |