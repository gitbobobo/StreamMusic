---
sidebar_position: 1
---

# Subsonic 接口文档

:::note 参考文档：

- [Subsonic](https://www.subsonic.org/pages/api.jsp)
- ~~[OpenSubsonic](https://opensubsonic.netlify.app/docs/)~~

:::

## 认证

所有请求均需携带以下参数：

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| u | Y | | 用户名 |
| t | Y | | 以md5(密码+盐)计算出的身份验证令牌 |
| s | Y | | 盐（随机生成，至少6位） |
| v | Y | | 客户端实现的协议版本 |
| c | Y | | 客户端名称 |
| f | N | xml | 返回格式，可选值: `xml`, `json`, `jsonp`。 |

示例：
```js
password = 'sesame'
salt = 'c19b2d'
token = md5('sesamec19b2d') = '26719a1196d2a940705a59634eb18eab'
url = 'http://your-server/rest/ping.view?u=joe&t=26719a1196d2a940705a59634eb18eab&s=c19b2d&v=1.12.0&c=myapp'
```

## 错误代码

| 代码 | 备注 |
| --- | --- |
| 0 | 一般性错误 |
| 10 | 缺少参数 |
| 20 | 客户端版本过低 |
| 30 | 服务端版本过低 |
| 40 | 用户名或密码错误 |
| 50 | 无权限 |
| 60 | Subsonic 试用期已结束 |
| 70 | 未找到请求的数据 |

示例：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<subsonic-response xmlns="http://subsonic.org/restapi" status="failed" version="1.1.0">
   <error code="40" message="Wrong username or password"/>
</subsonic-response>
```

## 请求节点

以下节点中，凡是允许填写多个值的，均为以`,`分割的。

:::tip

因 URL 长度限制，批量处理时最好分批请求。

:::

### getAlbumList2 获取专辑列表

请求地址：`http://your-server/rest/getAlbumList2`

最低版本：1.8.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| type | Y |  | 排序方式，可选值: `random`, `newest`, `frequent`, `recent`, `starred`, `alphabeticalByName`, `alphabeticalByArtist`. 特殊值: `byYear`, `byGenre` |
| size | N | 10 | 返回结果数量，最大值 500 |
| offset | N | 0 | 偏移数量，用于分页获取数据 |
| fromYear | Y(type = byYear) |  | 年代最小值，若 最小值大于最大值，将倒序返回结果 |
| toYear | Y(type = byYear) |  | 年代最大值 |
| genre | Y(type = byGenre) |  | 流派 |
| musicFolderId | N |  | |

示例：

```xml
<subsonic-response
	xmlns="http://subsonic.org/restapi" status="ok" version="1.8.0">
	<albumList2>
		<album id="1768" name="Duets" coverArt="al-1768" songCount="2" created="2002-11-09T15:44:40" duration="514" artist="Nik Kershaw" artistId="829"/>
		<album id="2277" name="Hot" coverArt="al-2277" songCount="4" created="2004-11-28T00:06:52" duration="1110" artist="Melanie B" artistId="1242"/>
		<album id="4201" name="Bande A Part" coverArt="al-4201" songCount="14" created="2007-10-29T19:25:05" duration="3061" artist="Nouvelle Vague" artistId="2060"/>
		<album id="2910" name="Soundtrack From Twin Peaks" coverArt="al-2910" songCount="6" created="2002-11-17T09:58:42" duration="1802" artist="Angelo Badalamenti" artistId="1515"/>
		<album id="3109" name="Wild One" coverArt="al-3109" songCount="38" created="2001-04-17T00:20:08" duration="9282" artist="Thin Lizzy" artistId="661"/>
		<album id="1151" name="Perleporten" coverArt="al-1151" songCount="2" created="2002-11-16T22:24:22" duration="494" artist="Magnus Grønneberg" artistId="747"/>
		<album id="2204" name="Wholesale Meats And Fish" coverArt="al-2204" songCount="24" created="2004-11-27T23:44:31" duration="5362" artist="Letters To Cleo" artistId="1216"/>
		<album id="114" name="Sounds of the Seventies: AM Nuggets" coverArt="al-114" songCount="2" created="2004-03-09T07:32:46" duration="420" artist="Rubettes" artistId="97"/>
		<album id="279" name="Waiting for the Day" coverArt="al-279" songCount="2" created="2004-11-27T17:49:19" duration="448" artist="Bachelor Girl" artistId="231"/>
		<album id="4414" name="For Sale" songCount="14" created="2007-10-30T00:11:58" duration="2046" artist="The Beatles" artistId="509"/>
	</albumList2>
</subsonic-response>
```

### getAlbum 获取专辑信息及音轨列表

请求地址：`http://your-server/rest/getAlbum`

最低版本：1.8.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| id | Y |  | 专辑id |

示例：

```xml
<subsonic-response
	xmlns="http://subsonic.org/restapi" status="ok" version="1.8.0">
	<album id="11053" name="High Voltage" coverArt="al-11053" songCount="8" created="2004-11-27T20:23:32" duration="2414" artist="AC/DC" artistId="5432">
		<song id="71463" parent="71381" title="The Jack" album="High Voltage" artist="AC/DC" isDir="false" coverArt="71381" created="2004-11-08T23:36:11" duration="352" bitRate="128" size="5624132" suffix="mp3" contentType="audio/mpeg" isVideo="false" path="ACDC/High voltage/ACDC - The Jack.mp3" albumId="11053" artistId="5432" type="music"/>
		<song id="71464" parent="71381" title="Tnt" album="High Voltage" artist="AC/DC" isDir="false" coverArt="71381" created="2004-11-08T23:36:11" duration="215" bitRate="128" size="3433798" suffix="mp3" contentType="audio/mpeg" isVideo="false" path="ACDC/High voltage/ACDC - TNT.mp3" albumId="11053" artistId="5432" type="music"/>
		<song id="71458" parent="71381" title="It's A Long Way To The Top" album="High Voltage" artist="AC/DC" isDir="false" coverArt="71381" created="2004-11-27T20:23:32" duration="315" bitRate="128" year="1976" genre="Rock" size="5037357" suffix="mp3" contentType="audio/mpeg" isVideo="false" path="ACDC/High voltage/ACDC - It's a long way to the top if you wanna rock 'n 'roll.mp3" albumId="11053" artistId="5432" type="music"/>
		<song id="71461" parent="71381" title="Rock 'n' Roll Singer." album="High Voltage" artist="AC/DC" isDir="false" coverArt="71381" created="2004-11-27T20:23:33" duration="303" bitRate="128" track="2" year="1976" genre="Rock" size="4861680" suffix="mp3" contentType="audio/mpeg" isVideo="false" path="ACDC/High voltage/ACDC - Rock N Roll Singer.mp3" albumId="11053" artistId="5432" type="music"/>
		<song id="71460" parent="71381" title="Live Wire" album="High Voltage" artist="AC/DC" isDir="false" coverArt="71381" created="2004-11-27T20:23:33" duration="349" bitRate="128" track="4" year="1976" genre="Rock" size="5600206" suffix="mp3" contentType="audio/mpeg" isVideo="false" path="ACDC/High voltage/ACDC - Live Wire.mp3" albumId="11053" artistId="5432" type="music"/>
		<song id="71456" parent="71381" title="Can I sit next to you girl" album="High Voltage" artist="AC/DC" isDir="false" coverArt="71381" created="2004-11-27T20:23:32" duration="251" bitRate="128" track="6" year="1976" genre="Rock" size="4028276" suffix="mp3" contentType="audio/mpeg" isVideo="false" path="ACDC/High voltage/ACDC - Can I Sit Next To You Girl.mp3" albumId="11053" artistId="5432" type="music"/>
		<song id="71459" parent="71381" title="Little Lover" album="High Voltage" artist="AC/DC" isDir="false" coverArt="71381" created="2004-11-27T20:23:33" duration="339" bitRate="128" track="7" year="1976" genre="Rock" size="5435119" suffix="mp3" contentType="audio/mpeg" isVideo="false" path="ACDC/High voltage/ACDC - Little Lover.mp3" albumId="11053" artistId="5432" type="music"/>
		<song id="71462" parent="71381" title="She's Got Balls" album="High Voltage" artist="AC/DC" isDir="false" coverArt="71381" created="2004-11-27T20:23:34" duration="290" bitRate="128" track="8" year="1976" genre="Rock" size="4651866" suffix="mp3" contentType="audio/mpeg" isVideo="false" path="ACDC/High voltage/ACDC - Shes Got Balls.mp3" albumId="11053" artistId="5432" type="music"/>
	</album>
</subsonic-response>
```

### getArtist 获取歌手信息及专辑列表

请求地址：`http://your-server/rest/getArtist`

最低版本：1.8.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| id | Y |  | 歌手id |

示例：

```xml
<subsonic-response
	xmlns="http://subsonic.org/restapi" status="ok" version="1.8.0">
	<artist id="5432" name="AC/DC" coverArt="ar-5432" albumCount="15">
		<album id="11047" name="Back In Black" coverArt="al-11047" songCount="10" created="2004-11-08T23:33:11" duration="2534" artist="AC/DC" artistId="5432"/>
		<album id="11048" name="Black Ice" coverArt="al-11048" songCount="15" created="2008-10-30T09:20:52" duration="3332" artist="AC/DC" artistId="5432"/>
		<album id="11049" name="Blow up your Video" coverArt="al-11049" songCount="10" created="2004-11-27T19:22:45" duration="2578" artist="AC/DC" artistId="5432"/>
		<album id="11050" name="Flick Of The Switch" coverArt="al-11050" songCount="10" created="2004-11-27T19:22:51" duration="2222" artist="AC/DC" artistId="5432"/>
		<album id="11051" name="Fly On The Wall" coverArt="al-11051" songCount="10" created="2004-11-27T19:22:57" duration="2405" artist="AC/DC" artistId="5432"/>
		<album id="11052" name="For Those About To Rock" coverArt="al-11052" songCount="10" created="2004-11-08T23:35:02" duration="2403" artist="AC/DC" artistId="5432"/>
		<album id="11053" name="High Voltage" coverArt="al-11053" songCount="8" created="2004-11-27T20:23:32" duration="2414" artist="AC/DC" artistId="5432"/>
		<album id="10489" name="Highway To Hell" coverArt="al-10489" songCount="12" created="2009-06-15T09:41:54" duration="2745" artist="AC/DC" artistId="5432"/>
		<album id="11054" name="If You Want Blood..." coverArt="al-11054" songCount="1" created="2004-11-27T20:23:32" duration="304" artist="AC/DC" artistId="5432"/>
		<album id="11056" name="Let There Be Rock" coverArt="al-11056" songCount="8" created="2004-11-27T20:33:40" duration="2449" artist="AC/DC" artistId="5432"/>
		<album id="11057" name="Live - Special Collector's Edition" coverArt="al-11057" songCount="22" created="2004-11-08T23:37:09" duration="6999" artist="AC/DC" artistId="5432"/>
		<album id="11058" name="Powerage" coverArt="al-11058" songCount="9" created="2004-11-27T20:33:41" duration="2380" artist="AC/DC" artistId="5432"/>
		<album id="11059" name="Stiff Upper Lip" coverArt="al-11059" songCount="11" created="2004-11-08T23:41:13" duration="2595" artist="AC/DC" artistId="5432"/>
		<album id="11060" name="The Razors Edge" coverArt="al-11060" songCount="12" created="2004-11-27T20:33:42" duration="2787" artist="AC/DC" artistId="5432"/>
		<album id="11061" name="Who Made Who" coverArt="al-11061" songCount="9" created="2004-11-08T23:43:18" duration="2291" artist="AC/DC" artistId="5432"/>
	</artist>
</subsonic-response>
```

### getArtistInfo2 获取歌手简介和相似歌手列表

请求地址：`http://your-server/rest/getArtistInfo2`

最低版本：1.11.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| id | Y |  | 歌手id |
| count | N |  | 相似歌手数量 |
| includeNotPresent | N |  | 是否返回媒体库不存在的歌手 |

示例：

```xml
<subsonic-response
	xmlns="http://subsonic.org/restapi" status="ok" version="1.11.0">
	<artistInfo2>
		<biography>Black Sabbath is an English 
			<a target='_blank' href="http://www.last.fm/tag/heavy metal" class="bbcode_tag" rel="tag">heavy metal</a> band that formed in 1968 in Birmingham, West Midlands, England, United Kingdom, originally comprising 
			<a target='_blank' href="http://www.last.fm/music/Ozzy+Osbourne" class="bbcode_artist">Ozzy Osbourne</a> (vocals), 
			<a target='_blank' href="http://www.last.fm/music/Tony+Iommi" class="bbcode_artist">Tony Iommi</a> (guitar), 
			<a target='_blank' href="http://www.last.fm/music/Geezer+Butler" class="bbcode_artist">Geezer Butler</a> (bass), and 
			<a target='_blank' href="http://www.last.fm/music/Bill+Ward" class="bbcode_artist">Bill Ward</a> (drums). In the early 
			<a target='_blank' href="http://www.last.fm/tag/70s" class="bbcode_tag" rel="tag">70s</a>, they were the first to pair heavily distorted, sonically dissonant 
			<a target='_blank' href="http://www.last.fm/tag/blues rock" class="bbcode_tag" rel="tag">blues rock</a> at slow speeds with lyrics about drugs, mental pain and abominations of war, thus giving birth to generations of metal bands that followed in their wake. 
			<a target='_blank' href="http://www.last.fm/music/Black+Sabbath">Read more about Black Sabbath on Last.fm</a>.
		</biography>
		<musicBrainzId>5182c1d9-c7d2-4dad-afa0-ccfeada921a8</musicBrainzId>
		<lastFmUrl>http://www.last.fm/music/Black+Sabbath</lastFmUrl>
		<smallImageUrl>http://userserve-ak.last.fm/serve/64/27904353.jpg</smallImageUrl>
		<mediumImageUrl>http://userserve-ak.last.fm/serve/126/27904353.jpg</mediumImageUrl>
		<largeImageUrl>http://userserve-ak.last.fm/serve/_/27904353/Black+Sabbath+sabbath+1970.jpg</largeImageUrl>
		<similarArtist id="279" name="AC/DC" coverArt="ar-279" albumCount="15"/>
		<similarArtist id="278" name="Accept" coverArt="ar-278" albumCount="1"/>
		<similarArtist id="433" name="Kiss" coverArt="ar-433" albumCount="1"/>
		<similarArtist id="372" name="Bruce Dickinson" coverArt="ar-372" albumCount="2"/>
		<similarArtist id="290" name="Alice in Chains" coverArt="ar-290" albumCount="3"/>
		<similarArtist id="285" name="Aerosmith" coverArt="ar-285" albumCount="2"/>
		<similarArtist id="396" name="The Doors" albumCount="1"/>
		<similarArtist id="397" name="Guns N' Roses" albumCount="1"/>
	</artistInfo2>
</subsonic-response>
```

### getIndexes 获取歌手列表

请求地址：`http://your-server/rest/getIndexes`

最低版本：1.0.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| musicFolderId | N |  |  |
| ifModifiedSince | N |  | 返回给定时间之后发生修改的歌手列表，单位：毫秒，自1970.1.1之后的差值 |

示例：

```xml
<subsonic-response
	xmlns="http://subsonic.org/restapi" status="ok" version="1.10.1">
	<indexes lastModified="237462836472342" ignoredArticles="The El La Los Las Le Les">
		<shortcut id="11" name="Audio books"/>
		<shortcut id="10" name="Podcasts"/>
		<index name="A">
			<artist id="1" name="ABBA"/>
			<artist id="2" name="Alanis Morisette"/>
			<artist id="3" name="Alphaville" starred="2013-11-02T12:30:00"/>
		</index>
		<index name="B">
			<artist name="Bob Dylan" id="4"/>
		</index>
		<child id="111" parent="11" title="Dancing Queen" isDir="false" album="Arrival" artist="ABBA" track="7" year="1978" genre="Pop" coverArt="24" size="8421341" contentType="audio/mpeg" suffix="mp3" duration="146" bitRate="128" path="ABBA/Arrival/Dancing Queen.mp3"/>
		<child id="112" parent="11" title="Money, Money, Money" isDir="false" album="Arrival" artist="ABBA" track="7" year="1978" genre="Pop" coverArt="25" size="4910028" contentType="audio/flac" suffix="flac" transcodedContentType="audio/mpeg" transcodedSuffix="mp3" duration="208" bitRate="128" path="ABBA/Arrival/Money, Money, Money.mp3"/>
	</indexes>
</subsonic-response>
```

### getCoverArt 封面图片

请求地址：`http://your-server/rest/getCoverArt`

最低版本：1.0.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| id | Y |  | 歌曲/专辑/歌手id，其中专辑id应添加前缀 `al-`，歌手id应添加前缀 `ar-` |
| size | N |  | 图片大小，示例：`600` |

### createPlaylist 创建或更新歌单名

请求地址：`http://your-server/rest/createPlaylist`

最低版本：1.2.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| playlistId | Y（更新时填写） |  | 歌单id |
| name | Y（创建时填写） |  | 歌单名 |

早期版本返回空的 `<subsonic-response> `, 自 1.14.0 之后会返回创建/更新后的歌单。

### deletePlaylist 删除歌单

请求地址：`http://your-server/rest/createPlaylist`

最低版本：1.2.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| id | Y |  | 歌单id |

### ping 测试服务连通性或登录

请求地址：`http://your-server/rest/ping`

最低版本：1.0.0

### getGenres 获取全部类型

请求地址：`http://your-server/rest/getGenres`

最低版本：1.9.0

示例：

```xml
<subsonic-response
	xmlns="http://subsonic.org/restapi" status="ok" version="1.10.2">
	<genres>
		<genre songCount="28" albumCount="6">Electronic</genre>
		<genre songCount="6" albumCount="2">Hard Rock</genre>
		<genre songCount="8" albumCount="2">R&B</genre>
		<genre songCount="22" albumCount="2">Blues</genre>
		<genre songCount="2" albumCount="2">Podcast</genre>
		<genre songCount="11" albumCount="1">Brit Pop</genre>
		<genre songCount="14" albumCount="1">Live</genre>
	</genres>
</subsonic-response>
```

### getLyrics 获取歌词

请求地址：`http://your-server/rest/getLyrics`

最低版本：1.2.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| artist | N |  | 歌手名 |
| title | N |  | 歌曲名 |

示例：

```xml
<subsonic-response
	xmlns="http://subsonic.org/restapi" status="ok" version="1.2.0">
	<lyrics artist="Muse" title="Hysteria"> It's bugging me Grating me And twisting me around Yeah I'm endlessly Caving in And turning inside out Cause I want it now I want it now Give me your heart and your soul And I'm breaking out I'm breaking out That's when she'll lose control It's holding me Morphing me And forcing me to strive To be endlessly Cold within And dreaming I'm alive Cause I want it now I want it now Give me your heart and your soul I'm not breaking down I'm breaking out That's when she'll lose control And I want you now I want you now I'll feel my heart implode And I'm breaking out Escaping now Feeling my faith erode </lyrics>
</subsonic-response>
```

### getPlaylists 获取歌单列表

请求地址：`http://your-server/rest/getPlaylists`

最低版本：1.0.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| username | N |  | 获取某个用户名下的歌单列表，使用此参数的用户必须有管理员权限 |

示例：

```xml
<subsonic-response
	xmlns="http://subsonic.org/restapi" status="ok" version="1.11.0">
	<playlists>
		<playlist id="15" name="Some random songs" comment="Just something I tossed together" owner="admin" public="false" songCount="6" duration="1391" created="2012-04-17T19:53:44" coverArt="pl-15">
			<allowedUser>sindre</allowedUser>
			<allowedUser>john</allowedUser>
		</playlist>
		<playlist id="16" name="More random songs" comment="No comment" owner="admin" public="true" songCount="5" duration="1018" created="2012-04-17T19:55:49" coverArt="pl-16"/>
	</playlists>
</subsonic-response>
```

### setRating 评分

请求地址：`http://your-server/rest/setRating`

最低版本：1.6.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| id | Y |  | 歌曲/专辑/歌手id |
| rating | Y |  | 分数，范围：0-5 |

### getScanStatus 获取扫描状态

请求地址：`http://your-server/rest/getScanStatus`

最低版本：1.15.0

示例：

```xml
<subsonic-response
	xmlns="http://subsonic.org/restapi" status="ok" version="1.15.0">
	<scanStatus scanning="true" count="5422"/>
</subsonic-response>
```

### scrobble 滚动播放记录

请求地址：`http://your-server/rest/scrobble`

最低版本：1.5.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| id | Y |  | 歌曲id |
| time | N |  | 播放时间，自1970以来的毫秒数 |
| submission | N | True | 是否提交，不提交则表示正在播放 |

### search2 搜索歌曲/专辑/歌手

请求地址：`http://your-server/rest/search2`

最低版本：1.4.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| query | Y |  | 关键词，传 `""` 时可用于获取全部数据 |
| artistCount | N | 20 | 返回的最大歌手数量 |
| artistOffset | N | 0 | 歌手列表偏移量 |
| albumCount | N | 20 | 返回的最大专辑数量 |
| albumOffset | N | 0 | 专辑列表偏移量 |
| songCount | N | 20 | 返回的最大歌曲数量 |
| songOffset | N | 0 | 歌曲列表偏移量 |
| musicFolderId | N |  |  |

示例：

```xml
<subsonic-response
	xmlns="http://subsonic.org/restapi" status="ok" version="1.10.1">
	<searchResult2>
		<artist id="1" name="ABBA" starred="2012-04-05T18:40:08"/>
		<album id="11" parent="1" title="Arrival" artist="ABBA" isDir="true" coverArt="22"/>
		<album id="12" parent="1" title="Super Trouper" artist="ABBA" isDir="true" coverArt="23"/>
		<song id="112" parent="11" title="Money, Money, Money" isDir="false" album="Arrival" artist="ABBA" track="7" year="1978" genre="Pop" coverArt="25" size="4910028" contentType="audio/flac" suffix="flac" transcodedContentType="audio/mpeg" transcodedSuffix="mp3" path="ABBA/Arrival/Money, Money, Money.mp3"/>
	</searchResult2>
</subsonic-response>
```

### getSongsByGenre 获取某个类型的歌曲列表

请求地址：`http://your-server/rest/getSongsByGenre`

最低版本：1.9.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| genre | Y |  | 类型名 |
| count | N | 10 | 返回的歌曲数量，最大 500 |
| offset | N | 0 | 起始行数，用于分页 |

示例：

```xml
<subsonic-response
	xmlns="http://subsonic.org/restapi" status="ok" version="1.9.0">
	<songsByGenre>
		<song id="16" parent="15" title="Atrapado" album="Antígona" artist="Antígona" isDir="false" coverArt="15" created="2012-12-26T17:05:54" duration="261" bitRate="128" track="1" year="2008" genre="Metal" size="4188288" suffix="mp3" contentType="audio/mpeg" isVideo="false" path="Antigona/Antigona/01 - Atrapado.mp3" albumId="2" artistId="2" type="music"/>
		<song id="17" parent="15" title="Gritar al cielo" album="Antígona" artist="Antígona" isDir="false" coverArt="15" created="2012-12-26T17:05:44" duration="233" bitRate="128" track="2" year="2008" genre="Metal" size="3737728" suffix="mp3" contentType="audio/mpeg" isVideo="false" path="Antigona/Antigona/02 - Gritar al cielo.mp3" albumId="2" artistId="2" type="music"/>
		<song id="18" parent="15" title="En sus garras" album="Antígona" artist="Antígona" isDir="false" coverArt="15" created="2012-12-26T17:05:22" duration="239" bitRate="128" track="3" year="2008" genre="Metal" size="3846272" suffix="mp3" contentType="audio/mpeg" isVideo="false" path="Antigona/Antigona/03 - En sus garras.mp3" albumId="2" artistId="2" type="music"/>
		<song id="19" parent="15" title="Nuevos Horizontes" album="Antígona" artist="Antígona" isDir="false" coverArt="15" created="2012-12-26T17:05:35" duration="310" bitRate="128" track="4" year="2008" genre="Metal" size="4980864" suffix="mp3" contentType="audio/mpeg" isVideo="false" path="Antigona/Antigona/04 - Nuevos Horizontes.mp3" albumId="2" artistId="2" type="music"/>
	</songsByGenre>
</subsonic-response>
```

### getSimilarSongs 获取相似歌曲

请求地址：`http://your-server/rest/getSimilarSongs`

最低版本：1.11.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| id | Y |  | 歌手/专辑/歌曲id |
| count | N | 50 | 返回的歌曲数量 |

示例：

```xml
<subsonic-response
	xmlns="http://subsonic.org/restapi" status="ok" version="1.11.0">
	<similarSongs>
		<song id="1631" parent="1628" isDir="false" title="A Whiter Shade Of Pale" album="Medusa" artist="Annie Lennox" track="3" coverArt="1628" size="5068173" contentType="audio/mpeg" suffix="mp3" duration="316" bitRate="128" path="Annie Lennox/Medusa/03 - A Whiter Shade Of Pale.MP3" isVideo="false" created="2004-11-08T22:21:17.000Z" albumId="471" artistId="305" type="music"/>
		<song id="4654" parent="4643" isDir="false" title="somebodys somebody" album="christina aguilera" artist="christina aguilera" track="8" year="1999" genre="Pop" coverArt="4643" size="6039760" contentType="audio/mpeg" suffix="mp3" duration="302" bitRate="160" path="Christina Aguilera/Album/08-cps-christina_aguilera--somebodys_somebody.mp3" isVideo="false" created="2004-11-25T22:18:53.000Z" albumId="698" type="music"/>
		<song id="2592" parent="2590" isDir="false" title="Higher Ground" album="Higher Ground" artist="Barbra Streisand" track="2" genre="Pop Vocals" coverArt="2590" size="5271680" contentType="audio/mpeg" suffix="mp3" duration="263" bitRate="160" path="Barbra Streisand/Higher Ground/02 - Higher Ground.mp3" isVideo="false" created="2002-11-09T14:36:28.000Z" albumId="524" artistId="328" type="music"/>
		<song id="1435" parent="1412" isDir="false" title="I dreamed you" album="Freak Of Nature" artist="Anastacia" track="11" year="2001" genre="Pop" coverArt="1412" size="4879261" contentType="audio/mpeg" suffix="mp3" duration="305" bitRate="128" path="Anastacia/Freak Of Nature/Anastacia - Freak Of Nature - 11 - I dreamed you .mp3" isVideo="false" created="2004-11-27T19:43:58.000Z" albumId="453" artistId="152" type="music"/>
		<song id="4664" parent="4644" isDir="false" title="The Christmas Song" album="My Kind Of Christmas" artist="Christina Aguilera" track="9" genre="Pop" coverArt="4644" size="4239446" contentType="audio/mpeg" suffix="mp3" duration="265" bitRate="128" path="Christina Aguilera/My Kind Of Christmas/09 - The Christmas Song.mp3" isVideo="false" created="2003-07-20T13:00:48.000Z" albumId="700" artistId="102" type="music"/>
		<song id="4118" parent="4111" isDir="false" title="The Hook Up" album="In The Zone" artist="Britney Spears" track="9" year="2003" genre="Pop" coverArt="4111" size="5623047" contentType="audio/mpeg" suffix="mp3" duration="234" bitRate="192" path="Britney Spears/In the Zone/09 - The Hook Up.mp3" isVideo="false" created="2004-11-27T20:27:16.000Z" albumId="653" artistId="79" type="music"/>
		<song id="1637" parent="1628" isDir="false" title="Waiting In Vain" album="Medusa" artist="Annie Lennox" track="9" coverArt="1628" size="5453102" contentType="audio/mpeg" suffix="mp3" duration="340" bitRate="128" path="Annie Lennox/Medusa/09 - Waiting In Vain.MP3" isVideo="false" created="2004-11-08T22:21:32.000Z" albumId="471" artistId="305" type="music"/>
		<song id="4520" parent="4519" isDir="false" title="Save Up All Your Tears" album="Love Hurts" artist="Cher" track="1" year="1991" genre="Pop" coverArt="4519" size="3831936" contentType="audio/mpeg" suffix="mp3" duration="239" bitRate="128" path="Cher/Love Hurts/01-Save Up All Your Tears.mp3" isVideo="false" created="2004-11-14T12:35:07.000Z" albumId="689" artistId="67" type="music"/>
		<song id="4684" parent="4646" isDir="false" title="Make Over" album="Stripped" artist="Christina Aguilera" track="12" year="2002" genre="Rock" coverArt="4646" size="6065009" contentType="audio/mpeg" suffix="mp3" duration="253" bitRate="192" path="Christina Aguilera/Stripped/(12) Christina Aguilera - Make Over.mp3" isVideo="false" created="2004-11-25T22:18:56.000Z" albumId="277" artistId="102" type="music"/>
		<song id="1629" parent="1628" isDir="false" title="No More I Love You's" album="Medusa" artist="Annie Lennox" track="1" coverArt="1628" size="4686874" contentType="audio/mpeg" suffix="mp3" duration="292" bitRate="128" path="Annie Lennox/Medusa/01 - No More I Love You's.MP3" isVideo="false" created="2004-11-08T22:21:29.000Z" albumId="471" artistId="305" type="music"/>
	</similarSongs>
</subsonic-response>
```

### getRandomSongs 随机获取歌曲

请求地址：`http://your-server/rest/getRandomSongs`

最低版本：1.2.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| size | N | 10 | 结果数量，最大500条 |

示例：

```xml
<subsonic-response
	xmlns="http://subsonic.org/restapi" status="ok" version="1.16.1" type="navidrome" serverVersion="0.52.0 (92a98cd5)" openSubsonic="true">
	<randomSongs>
		<song id="072f97e35d3c7a361daec0264d8941b3" parent="cf859b29e87f5e9e25ef0cf78ca22b84" isDir="false" title="独上西楼" album="邓丽君 Vol.2" artist="邓丽君" track="3" year="2007" coverArt="mf-072f97e35d3c7a361daec0264d8941b3_65fc18d7" size="16584611" contentType="audio/flac" suffix="flac" duration="163" bitRate="809" path="邓丽君/邓丽君 Vol.2/03 - 独上西楼.flac" created="2024-04-30T10:25:33.16687882Z" albumId="cf859b29e87f5e9e25ef0cf78ca22b84" artistId="8fccbf2dbaf0d3b8a486f385cce4f803" type="music" isVideo="false" bpm="0" comment="" sortName="" mediaType="song" musicBrainzId="" channelCount="2">
			<replayGain trackPeak="1" albumPeak="1"></replayGain>
		</song>
		<song id="de28115e41db88f25e3d02e6e5021d45" parent="661b3dda98a12c146da788d3bd204c8f" isDir="false" title="Dancing in the Rain" album="我们在中场相遇" artist="莫文蔚" track="7" year="2018" coverArt="mf-de28115e41db88f25e3d02e6e5021d45_65fc36a5" size="59678579" contentType="audio/flac" suffix="flac" duration="260" bitRate="1818" path="莫文蔚/我们在中场相遇/07 - Dancing in the Rain.flac" created="2024-04-30T10:17:01.624046459Z" albumId="661b3dda98a12c146da788d3bd204c8f" artistId="47418e7b558c66b3114fb8c9571cff24" type="music" isVideo="false" bpm="0" comment="" sortName="" mediaType="song" musicBrainzId="" channelCount="2">
			<replayGain trackGain="-9.18" albumGain="-8.72" trackPeak="0.964932" albumPeak="0.999969"></replayGain>
		</song>
	</randomSongs>
</subsonic-response>
```

### getStarred 获取收藏歌曲/专辑/歌手

请求地址：`http://your-server/rest/getStarred`

最低版本：1.8.0

### getSong 获取歌曲信息

请求地址：`http://your-server/rest/getSong`

最低版本：1.8.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| id | Y |  | 歌曲id |

示例：

```xml
<subsonic-response
	xmlns="http://subsonic.org/restapi" status="ok" version="1.8.0">
	<song id="48228" parent="48203" title="You Shook Me All Night Long" album="Back In Black" artist="AC/DC" isDir="false" coverArt="48203" created="2004-11-08T23:33:11" duration="210" bitRate="112" size="2945619" suffix="mp3" contentType="audio/mpeg" isVideo="false" path="ACDC/Back in black/ACDC - You Shook Me All Night Long.mp3"/>
</subsonic-response>
```

### getTopSongs 获取歌手的热门歌曲

请求地址：`http://your-server/rest/getTopSongs`

最低版本：1.13.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| artist | Y |  | 歌手名 |
| count | N | 50 | 返回的歌曲数量 |

示例：

```xml
<subsonic-response
	xmlns="http://subsonic.org/restapi" status="ok" version="1.13.0">
	<topSongs>
		<song id="1013" parent="1008" isDir="false" title="London Leatherboys" album="Balls To The Wall" artist="Accept" track="2" year="1984" genre="Metal" coverArt="1008" size="5706432" contentType="audio/mpeg" suffix="mp3" duration="237" bitRate="192" path="Accept/Balls To The Wall/Accept - London Leatherboys - 02.mp3" isVideo="false" created="2004-11-27T17:22:37.000Z" albumId="411" artistId="278" type="music"/>
		<song id="1012" parent="1008" isDir="false" title="Head Over Heels" album="Balls To The Wall" artist="Accept" track="4" year="1984" genre="Metal" coverArt="1008" size="6219527" contentType="audio/mpeg" suffix="mp3" duration="259" bitRate="192" path="Accept/Balls To The Wall/Accept - Head Over Heels - 04.mp3" isVideo="false" created="2004-11-27T17:22:35.000Z" starred="2015-01-03T21:12:10.070Z" albumId="411" artistId="278" type="music"/>
		<song id="1016" parent="1008" isDir="false" title="Love Child" album="Balls To The Wall" artist="Accept" track="6" year="1984" genre="Metal" coverArt="1008" size="5156143" contentType="audio/mpeg" suffix="mp3" duration="214" bitRate="192" path="Accept/Balls To The Wall/Accept - Love Child - 06.mp3" isVideo="false" created="2004-11-27T17:22:42.000Z" starred="2014-12-30T15:05:03.815Z" albumId="411" artistId="278" type="music"/>
	</topSongs>
</subsonic-response>
```

### getPlaylist 获取歌单中的歌曲

请求地址：`http://your-server/rest/getPlaylist`

最低版本：1.0.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| id | Y |  | 歌单id |

示例：

```xml
<subsonic-response
	xmlns="http://subsonic.org/restapi" status="ok" version="1.11.0">
	<script/>
	<playlist id="15" name="kokos" comment="fan" owner="admin" public="true" songCount="6" duration="1391" created="2012-04-17T19:53:44" coverArt="pl-15">
		<allowedUser>sindre</allowedUser>
		<allowedUser>john</allowedUser>
		<entry id="657" parent="655" title="Making Me Nervous" album="I Don't Know What I'm Doing" artist="Brad Sucks" isDir="false" coverArt="655" created="2008-04-10T07:10:32" duration="159" bitRate="202" track="1" year="2003" size="4060113" suffix="mp3" contentType="audio/mpeg" isVideo="false" path="Brad Sucks/I Don't Know What I'm Doing/01 - Making Me Nervous.mp3" albumId="58" artistId="45" type="music"/>
		<entry id="823" parent="784" title="Piano escena" album="BSO Sebastian" artist="PeerGynt Lobogris" isDir="false" coverArt="784" created="2009-01-14T22:26:29" duration="129" bitRate="170" track="8" year="2008" genre="Blues" size="2799954" suffix="mp3" contentType="audio/mpeg" isVideo="false" path="PeerGynt Lobogris/BSO Sebastian/08 - Piano escena.mp3" albumId="75" artistId="54" type="music"/>
		<entry id="748" parent="746" title="Stories from Emona II" album="Between two worlds" artist="Maya Filipič" isDir="false" coverArt="746" created="2008-07-30T22:05:40" duration="335" bitRate="176" track="2" year="2008" genre="Classical" size="7458214" suffix="mp3" contentType="audio/mpeg" isVideo="false" path="Maya Filipic/Between two worlds/02 - Stories from Emona II.mp3" albumId="68" artistId="51" type="music"/>
		<entry id="848" parent="827" title="Run enemy" album="Eve" artist="Shearer" isDir="false" coverArt="827" created="2009-01-15T22:54:38" duration="331" bitRate="195" track="14" year="2008" genre="Rock" size="8160185" suffix="mp3" contentType="audio/mpeg" isVideo="false" path="Shearer/Eve/14 - Run enemy.mp3" albumId="77" artistId="55" type="music"/>
		<entry id="884" parent="874" title="Isolation" album="Kosmonaut" artist="Ugress" isDir="false" coverArt="874" created="2009-01-14T21:34:49" duration="320" bitRate="160" track="4" year="2006" genre="Electronic" size="6412176" suffix="mp3" contentType="audio/mpeg" isVideo="false" path="Ugress/Kosmonaut/Ugress-KosmonautEP-04-Isolation.mp3" albumId="81" artistId="57" type="music"/>
		<entry id="805" parent="783" title="Bajo siete lunas (intro)" album="Broken Dreams" artist="PeerGynt Lobogris" isDir="false" coverArt="783" created="2008-12-19T14:13:58" duration="117" bitRate="225" track="1" year="2008" genre="Blues" size="3363271" suffix="mp3" contentType="audio/mpeg" isVideo="false" path="PeerGynt Lobogris/Broken Dreams/01 - Bajo siete lunas (intro).mp3" albumId="74" artistId="54" type="music"/>
	</playlist>
</subsonic-response>
```

### star 收藏歌曲/专辑/歌手

请求地址：`http://your-server/rest/star`

最低版本：1.8.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| id | N |  | 歌曲/专辑/歌手id，允许填写多个值 |
| albumId | N |  | 专辑id，允许填写多个值 |
| artistId | N |  | 歌手id，允许填写多个值 |

### stream 歌曲播放链接

请求地址：`http://your-server/rest/stream`

最低版本：1.0.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| id | Y |  | 歌曲id |
| maxBitRate | N |  | 比特率，设为0则不转码 |
| format | N |  | 文件格式，特殊值 `raw` 以禁用转码 |
| estimateContentLength | N | false | 将 content-length 设为转码后的估计值 |

### unstar 取消收藏

请求地址：`http://your-server/rest/unstar`

最低版本：1.8.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| id | N |  | 歌曲/专辑/歌手id，允许填写多个值 |
| albumId | N |  | 专辑id，允许填写多个值 |
| artistId | N |  | 歌手id，允许填写多个值 |

### updatePlaylist 更新歌单

请求地址：`http://your-server/rest/updatePlaylist`

最低版本：1.8.0

| 参数名 | 是否必填 | 默认值 | 备注 |
| --- | --- | --- | --- |
| playlistId | Y |  | 歌单id |
| name | N |  | 歌单名 |
| comment | N |  | 评论 |
| public | N |  | 是否对所有用户可见 |
| songIdToAdd | N |  | 待添加的歌曲id，允许填写多个值 |
| songIndexToRemove | N |  | 待删除的歌曲id，允许填写多个值 |