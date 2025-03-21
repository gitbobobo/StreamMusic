---
sidebar_position: 6
---

# Plex 接口文档

:::note 参考文档：

- [Plex API（非官方）](https://plexapi.dev/)
- [python-plexapi](https://github.com/pkkid/python-plexapi)
- [Plex Audio Transcoder File Extension](https://www.reddit.com/r/PleX/comments/189gtej/plex_audio_transcoder_file_extension/)

:::

## 认证

若无特殊说明，下文所有请求均需携带以下请求头。

| 参数名 | 备注 |
| --- | --- |
| X-Plex-Client-Identifier | 设备 ID |
| X-Plex-Platform | 操作系统，可选值：`Web`, `Android`, `iOS`, `MacOSX`, `Windows`, `Linux` |
| X-Plex-Provides | 应用类型，可选值：`player` |
| X-Plex-Product | 应用名称 |
| X-Plex-Version | 应用版本号 |
| X-Plex-Device | 设备型号 |
| X-Plex-Device-Name | 设备名 |
| X-Plex-Token | 访问令牌，登录成功后必填 |


### signin 登录

POST: `https://plex.tv/api/v2/users/signin`

body(`application/json`):

| 参数名 | 备注 |
| --- | --- |
| login | 用户名 |
| password | 密码 |
| verificationCode | OTP 验证码，可选 |
| rememberMe | 记住登录状态，可选值：`true`, `false` |

401 response:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<errors>
	<error code="1029" message="Please enter the verification code" status="401"/>
</errors>
```

response:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<user id="xxx" uuid="xxx" username="xxx" title="xxx" email="xxx@xxx.com" friendlyName="" locale="" confirmed="1" joinedAt="1701051277" emailOnlyAuth="0" hasPassword="1" protected="0" thumb="https://plex.tv/users/xxx/avatar?c=xxx" authToken="xxx" mailingListStatus="active" mailingListActive="1" scrobbleTypes="" country="CN" subscriptionDescription="Lifetime Plex Pass" restricted="0" anonymous="0" home="0" guest="0" homeSize="1" homeAdmin="0" maxHomeSize="15" rememberExpiresAt="1714812929" adsConsent="" adsConsentSetAt="" adsConsentReminderAt="" experimentalFeatures="1" twoFactorEnabled="1" backupCodesCreated="1">
	<subscription active="1" subscribedAt="2024-03-24 05:13:37 UTC" status="Active" paymentService="braintree" plan="lifetime">
		<features>
			<feature id="guided-upgrade"/>
			<feature id="increase-password-complexity"/>
			<feature id="upgrade-3ds2"/>
			<feature id="ad-countdown-timer"/>
			<feature id="adaptive_bitrate"/>
			<feature id="amazon-loop-debug"/>
			<feature id="Android - Dolby Vision"/>
			<feature id="Android - PiP"/>
			<feature id="avod-ad-analysis"/>
			<feature id="avod-new-media"/>
			<feature id="blacklist_get_signin"/>
			<feature id="camera_upload"/>
			<feature id="CU Sunset"/>
			<feature id="client-radio-stations"/>
			<feature id="cloudsync"/>
			<feature id="comments_and_replies_push_notifications"/>
			<feature id="friend_request_push_notifications"/>
			<feature id="community_access_plex_tv"/>
			<feature id="companions_sonos"/>
			<feature id="content_filter"/>
			<feature id="custom-home-removal"/>
			<feature id="grandfather-sync"/>
			<feature id="disable_home_user_friendships"/>
			<feature id="disable_sharing_friendships"/>
			<feature id="downloads-gating"/>
			<feature id="drm_support"/>
			<feature id="dvr"/>
			<feature id="dvr-block-unsupported-countries"/>
			<feature id="epg-recent-channels"/>
			<feature id="federated-auth"/>
			<feature id="global-continue-watching"/>
			<feature id="hwtranscode"/>
			<feature id="hardware_transcoding"/>
			<feature id="home"/>
			<feature id="HRK_enable_EUR"/>
			<feature id="imagga-v2"/>
			<feature id="ios14-privacy-banner"/>
			<feature id="item_clusters"/>
			<feature id="iterable-notification-tokens"/>
			<feature id="keep-payment-method"/>
			<feature id="kevin-bacon"/>
			<feature id="korea-consent"/>
			<feature id="lets_encrypt"/>
			<feature id="lightning-dvr-pivot"/>
			<feature id="livetv"/>
			<feature id="allow_dvr"/>
			<feature id="live-tv-support-incomplete-segments"/>
			<feature id="tuner-sharing"/>
			<feature id="lyrics"/>
			<feature id="metadata_search"/>
			<feature id="vod_cloudflare"/>
			<feature id="music_videos"/>
			<feature id="new_plex_pass_prices"/>
			<feature id="news-provider-sunset-modal"/>
			<feature id="nominatim"/>
			<feature id="pass"/>
			<feature id="photos-favorites"/>
			<feature id="photos-metadata-edition"/>
			<feature id="photosV6-edit"/>
			<feature id="photosV6-tv-albums"/>
			<feature id="pms_health"/>
			<feature id="premium-dashboard"/>
			<feature id="premium_music_metadata"/>
			<feature id="shared_server_notification"/>
			<feature id="shared_source_notification"/>
			<feature id="require-plex-nonce"/>
			<feature id="scrobbling-service-plex-tv"/>
			<feature id="album-types"/>
			<feature id="collections"/>
			<feature id="music-analysis"/>
			<feature id="radio"/>
			<feature id="session_bandwidth_restrictions"/>
			<feature id="session_kick"/>
			<feature id="exclude restrictions"/>
			<feature id="signin_notification"/>
			<feature id="signin_with_apple"/>
			<feature id="sleep-timer"/>
			<feature id="spring_serve_ad_provider"/>
			<feature id="sync"/>
			<feature id="trailers"/>
			<feature id="transcoder_cache"/>
			<feature id="boost-voices"/>
			<feature id="TREBLE-show-features"/>
			<feature id="silence-removal"/>
			<feature id="sweet-fades"/>
			<feature id="visualizers"/>
			<feature id="volume-leveling"/>
			<feature id="two-factor-authentication"/>
			<feature id="unsupportedtuners"/>
			<feature id="vod-schema"/>
			<feature id="watch-together-invite"/>
			<feature id="watchlist-rss"/>
			<feature id="web_server_dashboard"/>
			<feature id="webhooks"/>
		</features>
	</subscription>
	<profile autoSelectAudio="0" defaultAudioLanguage="zh" defaultSubtitleLanguage="zh" autoSelectSubtitle="0" defaultSubtitleAccessibility="0" defaultSubtitleForced="0" watchedIndicator="1"/>
	<entitlements>
		<entitlement id="all"/>
		<entitlement id="roku"/>
		<entitlement id="android"/>
		<entitlement id="xbox_one"/>
		<entitlement id="xbox_360"/>
		<entitlement id="windows"/>
		<entitlement id="windows_phone"/>
		<entitlement id="ios"/>
	</entitlements>
	<roles>
		<role id="plexpass"/>
	</roles>
	<subscriptions>
		<subscription id="" mode="lifetime" renewsAt="" endsAt="" canceled="0" gracePeriod="0" onHold="0" canReactivate="0" canUpgrade="0" canDowngrade="0" canConvert="0" type="plexpass" transfer="0" state="active">
			<billing paymentMethodId="">
				<internalPaymentMethod/>
			</billing>
		</subscription>
	</subscriptions>
	<pastSubscriptions></pastSubscriptions>
	<trials></trials>
	<services>
		<service identifier="epg" endpoint="https://epg.provider.plex.tv" token="xxx=" secret="" status="online"/>
		<service identifier="epg-staging" endpoint="https://epg-staging.provider.plex.tv" token="xxx=" secret="" status="online"/>
		<service identifier="epg-dev" endpoint="https://epg-dev.provider.plex.tv" token="xxx=" secret="" status="online"/>
		<service identifier="eyeq" endpoint="https://c4412416.ipg.web.cddbp.net/webapi/xml/1.0/" token="6iUU7xxxVrBzA/xxx+xxx" secret="" status="online"/>
		<service identifier="eyeq-channel-icons" endpoint="http://akamai-b.cdn.cddbp.net/cds/2.0/image" token="" secret="" status="online"/>
		<service identifier="graph-dev" endpoint="https://community-dev.plex.tv" token="" secret="" status="online"/>
		<service identifier="graph-staging" endpoint="https://community-staging.plex.tv" token="" secret="" status="online"/>
		<service identifier="community-dev" endpoint="https://community-dev.plex.tv" token="" secret="" status="online"/>
		<service identifier="community-staging" endpoint="https://community-staging.plex.tv" token="" secret="" status="online"/>
		<service identifier="community" endpoint="https://community.plex.tv" token="" secret="" status="online"/>
		<service identifier="metadata" endpoint="https://metadata.provider.plex.tv" token="xxx=" secret="" status="online"/>
		<service identifier="scrobbling" endpoint="https://scrobbles.plex.tv" token="xxx.xxx.ukvm_-xxx-xxx-xxx-3Vamxi7eNG-xxx-xxx-d7z-xxx" secret="" status="online"/>
		<service identifier="metadata-dev" endpoint="https://metadata-dev.provider.plex.tv" token="xxx=" secret="" status="online"/>
		<service identifier="metadata-provider" endpoint="https://mpm.plex.tv/" token="" secret="" status="online"/>
		<service identifier="tmsapi" endpoint="https://tmsapi.plex.tv/v1.1/" token="xxx+OQ=" secret="" status="online"/>
		<service identifier="subtitles-search" endpoint="https://metadata.provider.plex.tv/library/streams/matches" token="xxx=" secret="" status="online"/>
		<service identifier="acoustid" endpoint="https://acoustid.plex.tv/" token="xxx==" secret="" status="online"/>
		<service identifier="lyricfind" endpoint="https://lyricfind.plex.tv/" token="xxx+/xxx/zqV1" secret="H8q1AfgeOcf8+xxx+teyIOw" status="online"/>
		<service identifier="lyricfind-search" endpoint="https://lyricfind.plex.tv/" token="4HRR+YgScsy+xxx+xxx" secret="" status="online"/>
		<service identifier="tvdb" endpoint="https://api4.thetvdb.com/" token="xxx+9EAH+xxx/xxx" secret="" status="online"/>
	</services>
</user>
```

### resources 获取资源列表

GET: `https://plex.tv/api/v2/resources?includeHttps=1&includeRelay=1`

response:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<resources>
<resource name="xxx" product="Plex Media Server" productVersion="1.29.2" platform="Linux" platformVersion="DSM" device="DS+" clientIdentifier="xxx" createdAt="2024-03-17T11:34:53Z" lastSeenAt="2024-04-19T19:09:52Z" provides="server" ownerId="" sourceTitle="" publicAddress="22.22.22.22" accessToken="xxx" owned="1" home="0" synced="0" relay="1" presence="1" httpsRequired="0" publicAddressMatches="1" dnsRebindingProtection="0" natLoopbackSupported="0">
  <connections>
    <connection protocol="https" address="192.168.22.22" port="32400" uri="https://192-168-22-22.xxx.plex.direct:32400" local="1" relay="0" IPv6="0"/>
    <connection protocol="https" address="139.162.22.22" port="8443" uri="https://139-162-22-22.xxx.plex.direct:8443" local="0" relay="1" IPv6="0"/>
  </connections>
</resource>
</resources>
```

### 测试服务器连通性

GET: `[host]`

response:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<MediaContainer size="25" allowCameraUpload="1" allowChannelAccess="1" allowMediaDeletion="1" allowSharing="1" allowSync="1" allowTuners="1" backgroundProcessing="1" certificate="1" companionProxy="1" countryCode="chn" diagnostics="logs,databases,streaminglogs" eventStream="1" friendlyName="xxx" hubSearch="1" itemClusters="1" livetv="7" machineIdentifier="xxx" mediaProviders="1" multiuser="1" musicAnalysis="2" myPlex="1" myPlexMappingState="mapped" myPlexSigninState="ok" myPlexSubscription="1" myPlexUsername="xxx" offlineTranscode="1" ownerFeatures="fec722a0-a6d4-4fbd-96dc-4ffb02b072c5,federated-auth,hardware_transcoding,home,hwtranscode,item_clusters,kevin-bacon,livetv,loudness,lyrics,music-analysis,music_videos,pass,photosV6-edit,photosV6-tv-albums,premium_music_metadata,radio,server-manager,session_bandwidth_restrictions,session_kick,shared-radio,sync,trailers,tuner-sharing,type-first,unsupportedtuners,webhooks" photoAutoTag="1" platform="Linux" platformVersion="DSM" pluginHost="1" pushNotifications="0" readOnlyLibraries="0" streamingBrainABRVersion="3" streamingBrainVersion="2" sync="1" transcoderActiveVideoSessions="0" transcoderAudio="1" transcoderLyrics="1" transcoderPhoto="1" transcoderSubtitles="1" transcoderVideo="1" transcoderVideoBitrates="64,96,208,320,720,1500,2000,3000,4000,8000,10000,12000,20000" transcoderVideoQualities="0,1,2,3,4,5,6,7,8,9,10,11,12" transcoderVideoRemuxOnly="1" transcoderVideoResolutions="128,128,160,240,320,480,768,720,720,1080,1080,1080,1080" updatedAt="1712973038" updater="1" version="1.29.2" voiceSearch="1">
<Directory count="1" key="actions" title="actions" />
<Directory count="1" key="activities" title="activities" />
<Directory count="1" key="butler" title="butler" />
<Directory count="1" key="channels" title="channels" />
<Directory count="1" key="clients" title="clients" />
<Directory count="1" key="devices" title="devices" />
<Directory count="1" key="diagnostics" title="diagnostics" />
<Directory count="1" key="hubs" title="hubs" />
<Directory count="3" key="library" title="library" />
<Directory count="3" key="livetv" title="livetv" />
<Directory count="3" key="media" title="media" />
<Directory count="3" key="metadata" title="metadata" />
<Directory count="1" key="neighborhood" title="neighborhood" />
<Directory count="1" key="playQueues" title="playQueues" />
<Directory count="1" key="player" title="player" />
<Directory count="1" key="playlists" title="playlists" />
<Directory count="1" key="resources" title="resources" />
<Directory count="1" key="search" title="search" />
<Directory count="1" key="server" title="server" />
<Directory count="1" key="servers" title="servers" />
<Directory count="1" key="statistics" title="statistics" />
<Directory count="1" key="system" title="system" />
<Directory count="1" key="transcode" title="transcode" />
<Directory count="1" key="updater" title="updater" />
<Directory count="1" key="user" title="user" />
</MediaContainer>
```

## 请求节点

### agents 获取代理（插件）列表

GET: `[host]/system/agents/com.plexapp.agents.none/config/8?X-Plex-Token=[token]`

结尾的 `8` 表示查询艺术家相关的代理。

response:

```xml
<?xml version="1.0" encoding="utf-8"?>
<MediaContainer noHistory="0" replaceParent="0" size="9" identifier="com.plexapp.system">
  <Agent name="Personal Media Artists" enabled="1" hasPrefs="0" identifier="com.plexapp.agents.none"/>
  <Agent name="Local Media Assets (Artists)" enabled="1" hasPrefs="0" identifier="com.plexapp.agents.localmedia"/>
  <Agent name="Fanart.tv" hasPrefs="1" identifier="com.plexapp.agents.fanarttv"/>
  <Agent name="Home Theater Backdrops" hasPrefs="0" identifier="com.plexapp.agents.htbackdrops"/>
  <Agent name="Last.fm" hasPrefs="1" identifier="com.plexapp.agents.lastfm"/>
  <Agent name="Musicbrainz" hasPrefs="1" identifier="org.musicbrainz.agents.music"/>
  <Agent name="Plex Music" hasPrefs="1" identifier="tv.plex.agents.music"/>
</MediaContainer>
```

### sections 获取资料库列表

GET: `[host]/library/sections`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<MediaContainer size="1" allowSync="0" title1="Plex Library">
<Directory allowSync="1" art="/:/resources/artist-fanart.jpg" composite="/library/sections/1/composite/xxx" filters="1" refreshing="0" thumb="/:/resources/artist.png" key="1" type="artist" title="&#38899;&#20048;" agent="com.plexapp.agents.xxx" scanner="Plex Music Scanner" language="zh" uuid="0d645d8b-xxxx-44f5-xxxx-7b90f6be6d67" updatedAt="1711858705" createdAt="1710675339" scannedAt="1713579735" content="1" directory="1" contentChangedAt="198267" hidden="0">
<Location id="1" path="/volume1/music" />
</Directory>
</MediaContainer>
```

在返回的列表中筛选 `type="artist"`的资料库，记录一下 `key` 值。

### sections 获取专辑列表

GET: `[host]/library/sections/[sectionKey]/all`

query:

| 参数名 | 备注 |
| --- | --- |
| type | 类型，固定为 `9` |
| sort | 排序方式，默认按专辑艺术家排序，可选值 `addedAt:desc` |
| title | 标题，可选 |
| includeAdvanced | `1` |
| includeCollections | `1` |
| includeExternalMedia | `1` |
| X-Plex-Container-Start | 起始行数 |
| X-Plex-Container-Size | 结果数量 |

response:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<MediaContainer size="1" totalSize="3636" offset="100" allowSync="1" art="/:/resources/artist-fanart.jpg" identifier="com.plexapp.plugins.library" librarySectionID="1" librarySectionTitle="&#38899;&#20048;" librarySectionUUID="0d645d8b-6bca-44f5-8105-7b90f6be6d67" mediaTagPrefix="/system/bundle/media/flags/" mediaTagVersion="1667296136" nocache="1" thumb="/:/resources/artist.png" title1="&#38899;&#20048;" title2="All Artists" viewGroup="artist" viewMode="65592">
<Directory ratingKey="8014" key="/library/metadata/8014/children" parentRatingKey="8013" guid="local://8014" parentGuid="plex://artist/5d07bc05403c6402904ac4d2" type="album" title="Sing Me to Sleep" parentKey="/library/metadata/8013" parentTitle="Ben Folds" summary="" index="1" year="2015" thumb="/library/metadata/8014/thumb/1710932639" art="/library/metadata/8013/art/1711359519" parentThumb="/library/metadata/8013/thumb/1711359519" originallyAvailableAt="2015-01-01" addedAt="1710931892" updatedAt="1710932639" loudnessAnalysisVersion="2">
</Directory>
</MediaContainer>
```
### metadata 获取专辑信息

GET: `[host]/library/metadata/[id]`

query:

| 参数名 | 备注 |
| --- | --- |
| includeConcerts | `1` |
| includeExtras | `1` |
| includeOnDeck | `1` |
| includePopularLeaves | `1` |
| includePreferences | `1` |
| includeChapters | `1` |
| includeStations | `1` |
| includeMarkers | `1` |
| includeExternalMedia | `1` |
| asyncAugmentMetadata | `1` |
| includeRelated | `1` |
| checkFiles | `1` |
| asyncRefreshAnalysis | `1` |
| asyncRefreshLocalMediaAgent | `1` |

response:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<MediaContainer size="1" allowSync="1" identifier="com.plexapp.plugins.library" librarySectionID="1" librarySectionTitle="&#38899;&#20048;" librarySectionUUID="0d645d8b-6bca-44f5-8105-7b90f6be6d67" mediaTagPrefix="/system/bundle/media/flags/" mediaTagVersion="1667296136">
<Directory ratingKey="8014" key="/library/metadata/8014/children" parentRatingKey="8013" guid="local://8014" parentGuid="plex://artist/5d07bc05403c6402904ac4d2" type="album" title="Sing Me to Sleep" parentKey="/library/metadata/8013" librarySectionTitle="&#38899;&#20048;" librarySectionID="1" librarySectionKey="/library/sections/1" parentTitle="Ben Folds" summary="" index="1" year="2015" thumb="/library/metadata/8014/thumb/1710932639" art="/library/metadata/8013/art/1711359519" parentThumb="/library/metadata/8013/thumb/1711359519" originallyAvailableAt="2015-01-01" leafCount="1" viewedLeafCount="0" addedAt="1710931892" updatedAt="1710932639" loudnessAnalysisVersion="2">
<Extras size="0">
</Extras>
<Related>
</Related>
</Directory>
</MediaContainer>
```

### children 获取歌手名下的专辑

GET: `[host]/library/metadata/[id]/children`

query:

| 参数名 | 备注 |
| --- | --- |
| excludeAllLeaves | `1` |

### sections 获取歌手列表

GET: `[host]/library/sections/[sectionKey]/all`

query:

| 参数名 | 备注 |
| --- | --- |
| type | 类型，固定为 `8` |
| includeAdvanced | `1` |
| includeCollections | `1` |
| includeExternalMedia | `1` |
| X-Plex-Container-Start | 起始行数 |
| X-Plex-Container-Size | 结果数量 |

response:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<MediaContainer size="2" totalSize="858" offset="0" allowSync="1" art="/:/resources/artist-fanart.jpg" identifier="com.plexapp.plugins.library" librarySectionID="1" librarySectionTitle="音乐" librarySectionUUID="0d645d8b-6bca-44f5-8105-7b90f6be6d67" mediaTagPrefix="/system/bundle/media/flags/" mediaTagVersion="1667296136" nocache="1" thumb="/:/resources/artist.png" title1="音乐" title2="All Artists" viewGroup="artist" viewMode="65592">
	<Directory ratingKey="21227" key="/library/metadata/21227/children" guid="com.plexapp.agents.xxx://85323?lang=zh" type="artist" title="2 Unlimited" titleSort="2 UNLIMITED" summary="来自荷兰的二人跳舞组合“双人无极”（2 Unlimited）是由主音歌手anita Doth和说唱手ray Slijngaard所组成，配合两位长期合作的作曲人jean-paul De Coster和作词人phil Wilde。首张单曲《get Ready For This》一推出，立即红遍全球，而且四年后再一次打上美国billboard四十位之内；该乐队先后推出三张销量惊人的专辑，分别是：get Ready,no Limit和real Thing；碟内每张单曲均成绩骄人：《no Limit》是35个国家排行榜的冠军单曲，总销量超越250万张；随后的《tribal Dance》、《maximum Drive》、《no One》等都是排行榜冠军歌曲。本专辑收录他们所有精彩流行作品，更收录三首全新歌曲，另外不特别加送精选串烧歌。Techno跳舞音乐的兴起和流行，“双人无极”组合可说是功不可没，他们亦代表了 Techno Dance文化。" index="1" thumb="/library/metadata/21227/thumb/1711359363" art="/library/metadata/21227/art/1711359363" addedAt="1710940905" updatedAt="1711359363"></Directory>
	<Directory ratingKey="17139" key="/library/metadata/17139/children" guid="com.plexapp.agents.xxx://31081554?lang=zh" type="artist" title="24kGoldn" titleSort="24KGOLDN" summary="24KGOLDN是一名说唱歌手、歌手、编剧和来自加利福尼亚旧金山的前USC学生，吹嘘诸如“Valentino”和“City of Angels”。他的首张EP《Dropped Outta College》现在在唱片公司/哥伦比亚唱片公司上映。" index="1" thumb="/library/metadata/17139/thumb/1711359367" addedAt="1710937685" updatedAt="1711359367"></Directory>
</MediaContainer>
```

### metadata 获取歌手信息

GET: `[host]/library/metadata/[id]`

query:

| 参数名 | 备注 |
| --- | --- |
| includeConcerts | `1` |
| includeExtras | `1` |
| includeOnDeck | `1` |
| includePopularLeaves | `1` |
| includePreferences | `1` |
| includeChapters | `1` |
| includeStations | `1` |
| includeMarkers | `1` |
| includeExternalMedia | `1` |
| asyncAugmentMetadata | `1` |
| includeRelated | `1` |
| checkFiles | `1` |
| asyncRefreshAnalysis | `1` |
| asyncRefreshLocalMediaAgent | `1` |

response:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<MediaContainer size="1" allowSync="1" identifier="com.plexapp.plugins.library" librarySectionID="1" librarySectionTitle="音乐" librarySectionUUID="0d645d8b-6bca-44f5-8105-7b90f6be6d67" mediaTagPrefix="/system/bundle/media/flags/" mediaTagVersion="1667296136">
	<Directory ratingKey="17139" key="/library/metadata/17139/children" guid="com.plexapp.agents.xxx://31081554?lang=zh" type="artist" title="24kGoldn" titleSort="24KGOLDN" librarySectionTitle="音乐" librarySectionID="1" librarySectionKey="/library/sections/1" summary="24KGOLDN是一名说唱歌手、歌手、编剧和来自加利福尼亚旧金山的前USC学生，吹嘘诸如“Valentino”和“City of Angels”。他的首张EP《Dropped Outta College》现在在唱片公司/哥伦比亚唱片公司上映。" index="1" thumb="/library/metadata/17139/thumb/1711359367" addedAt="1710937685" updatedAt="1711359367">
		<Guid id="mbid://0fe5df51-ba65-4784-ba85-7d024a107a8a" />
		<Location path="/volume1/music/24kGoldn" />
		<Preferences>
			<Setting id="albumSort" label="Album sorting" summary="How to sort the albums for an artist." type="text" default="-1" value="-1" hidden="0" advanced="0" group="" enumValues="-1:Library default|0:Newest first|1:Oldest first|2:By name" />
		</Preferences>
		<Extras size="0"></Extras>
		<Related>
			<Hub key="/library/sections/1/all?artist.id=17139&type=9&format=EP,Single&resolveTags=1&sort=year:desc,originallyAvailableAt:desc,artist.titleSort:desc,album.titleSort,album.index,album.id,album.originallyAvailableAt" title="Singles & EPs" type="album" hubIdentifier="artist.albums.singles" context="hub.artist.albums.singles" size="0" more="0" style="shelf"></Hub>
			<Hub key="/library/sections/1/all?artist.id=17139&type=9&format!=EP,Single&subformat=Live&resolveTags=1&sort=year:desc,originallyAvailableAt:desc,artist.titleSort:desc,album.titleSort,album.index,album.id,album.originallyAvailableAt" title="Live Albums" type="album" hubIdentifier="artist.albums.live" context="hub.artist.albums.live" size="0" more="0" style="shelf"></Hub>
			<Hub key="/library/sections/1/all?artist.id=17139&type=9&format!=EP,Single&subformat=Soundtrack&subformat!=Live&resolveTags=1&sort=year:desc,originallyAvailableAt:desc,artist.titleSort:desc,album.titleSort,album.index,album.id,album.originallyAvailableAt" title="Soundtracks" type="album" hubIdentifier="artist.albums.soundtrack" context="hub.artist.albums.soundtrack" size="0" more="0" style="shelf"></Hub>
			<Hub key="/library/sections/1/all?artist.id=17139&type=9&format!=EP,Single&subformat=Compilation&subformat!=Live,Soundtrack&resolveTags=1&sort=year:desc,originallyAvailableAt:desc,artist.titleSort:desc,album.titleSort,album.index,album.id,album.originallyAvailableAt" title="Compilations" type="album" hubIdentifier="artist.albums.compilation" context="hub.artist.albums.compilation" size="0" more="0" style="shelf"></Hub>
			<Hub key="/library/sections/1/all?artist.id=17139&type=9&format!=EP,Single&subformat=Demo&subformat!=Live,Soundtrack,Compilation&resolveTags=1&sort=year:desc,originallyAvailableAt:desc,artist.titleSort:desc,album.titleSort,album.index,album.id,album.originallyAvailableAt" title="Demos" type="album" hubIdentifier="artist.albums.demo" context="hub.artist.albums.demo" size="0" more="0" style="shelf"></Hub>
			<Hub key="/library/sections/1/all?artist.id=17139&type=9&format!=EP,Single&subformat=Remix&subformat!=Live,Soundtrack,Compilation,Demo&resolveTags=1&sort=year:desc,originallyAvailableAt:desc,artist.titleSort:desc,album.titleSort,album.index,album.id,album.originallyAvailableAt" title="Remixes" type="album" hubIdentifier="artist.albums.remix" context="hub.artist.albums.remix" size="0" more="0" style="shelf"></Hub>
		</Related>
		<Stations size="1">
			<Playlist key="/library/metadata/17139/station/fb23b278-81c4-410a-a187-ae92906c6973?type=10" guid="" type="playlist" title="24kGoldn Radio" librarySectionTitle="音乐" librarySectionID="1" librarySectionKey="/library/sections/1" summary="" smart="1" playlistType="audio" leafCount="0" icon="playlist://image.radio" radio="1"></Playlist>
		</Stations>
		<PopularLeaves size="0" key="/library/sections/1/all?album.subformat!=Compilation,Live&artist.id=17139&group=title&limit=100&ratingCount>=1&resolveTags=1&sort=ratingCount:desc&type=10"></PopularLeaves>
	</Directory>
</MediaContainer>
```

### photo 图片链接

GET: `[host]/photo/:/transcode`

query:

| 参数名 | 备注 |
| --- | --- |
| width | 宽度 |
| height | 高度 |
| minSize | `1` |
| upscale | `1` |
| url | `[thumb]?X-Plex-Token=[token]` |
| X-Plex-Token | 访问令牌 |

### playlists 创建歌单

GET: `[host]/playlists`

首先需要通过 [测试服务器连通性](#测试服务器连通性) 的响应拿到 `machineIdentifier`

query:

| 参数名 | 备注 |
| --- | --- |
| type | 类型，固定为 `audio` |
| title | 歌单名 |
| smart | 是否智能歌单，可选值：`1`, `0` |
| uri | `server://[machineIdentifier]/com.plexapp.plugins.library/library/metadata/[歌曲ID列表]` |

response:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<MediaContainer size="1">
	<Playlist ratingKey="24055" key="/playlists/24055/items" guid="com.plexapp.agents.none://3a0bd837-d83a-4d59-bdca-4d6e747fab35" type="playlist" title="6655" summary="" smart="0" playlistType="audio" leafCount="0" addedAt="1713620514" updatedAt="1713620514"></Playlist>
</MediaContainer>
```

### playlists 删除歌单

DELETE: `[host]/playlists/[id]`

### metadata 删除歌曲

DELETE: `[host]/library/metadata/[id]`

### folder 获取目录列表

GET: `/library/sections/[sectionId]/folder`

query:

| 参数名 | 备注 |
| --- | --- |
| X-Plex-Container-Start | 行数偏移 |
| X-Plex-Container-Size | 结果数量 |
| includeCollections | `1` |
| includeExternalMedia | `1` |
| includeAdvanced | `1` |
| includeMeta | `1` |
| parent | 目录ID，不传时查询根目录 |

### genre 获取类型列表

GET: `[host]/library/sections/[sectionId]/genre`

query:

| 参数名 | 备注 |
| --- | --- |
| type | `9` |

response:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<MediaContainer size="32" allowSync="0" art="/:/resources/artist-fanart.jpg" content="secondary" identifier="com.plexapp.plugins.library" mediaTagPrefix="/system/bundle/media/flags/" mediaTagVersion="1667296136" nocache="1" thumb="/:/resources/artist.png" title1="音乐" title2="By Genre" viewGroup="secondary" viewMode="65592">
	<Directory fastKey="/library/sections/1/all?genre=231" key="231" title="Abstract" type="genre" />
	<Directory fastKey="/library/sections/1/all?genre=19984" key="19984" title="Alternative 另类" type="genre" />
	<Directory fastKey="/library/sections/1/all?genre=3941" key="3941" title="国际流行" type="genre" />
	<Directory fastKey="/library/sections/1/all?genre=19688" key="19688" title="流行" type="genre" />
	<Directory fastKey="/library/sections/1/all?genre=1625" key="1625" title="粤语流行" type="genre" />
</MediaContainer>
```

### streams 获取歌词

GET: `[host]/library/streams/[id]`

query:

| 参数名 | 备注 |
| --- | --- |
| format | 格式，可选值：`xml` |

response:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<MediaContainer size="1">
	<Lyrics provider="com.plexapp.agents.localmedia" minLines="0" timed="1" author="" by="">
		<Line startOffset="0" endOffset="1000">
			<Span text="作词 : xxx" startOffset="1000" endOffset="2000" />
		</Line>
	</Lyrics>
</MediaContainer>
```

### matches 获取歌手匹配结果

GET: `[host]/library/metadata/[id]/matches`

query:

| 参数名 | 备注 |
| --- | --- |
| manual | 是否手动，固定为 `0` |
| agent | 代理ID |

response:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<MediaContainer size="4" identifier="com.plexapp.plugins.library" mediaTagPrefix="/system/bundle/media/flags/" mediaTagVersion="1667296136">
	<SearchResult guid="com.plexapp.agents.xxx://791534?lang=zh" name="戴荃" score="106" lifespanEnded="0"></SearchResult>
	<SearchResult guid="com.plexapp.agents.xxx://791534?lang=zh" name="戴荃" score="106" lifespanEnded="0"></SearchResult>
	<SearchResult guid="com.plexapp.agents.xxx://11975111?lang=zh" name="ilem" score="86" lifespanEnded="0"></SearchResult>
	<SearchResult guid="com.plexapp.agents.xxx://11975111?lang=zh" name="ilem" score="77" lifespanEnded="0"></SearchResult>
</MediaContainer>
```

### match 确认歌手匹配结果

PUT: `[host]/library/metadata/[id]/match`

query:

| 参数名 | 备注 |
| --- | --- |
| name | 歌手名 |
| agent |  |

### playlists 获取歌单列表

GET: `[host]/playlists`

query:

| 参数名 | 备注 |
| --- | --- |
| playlistType | `audio` |

response:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<MediaContainer size="3">
	<Playlist ratingKey="24053" key="/playlists/24053/items" guid="com.plexapp.agents.none://de11d190-442c-4c2e-853f-6c8e4c078e27" type="playlist" title="1999年老歌by慕星人" summary="" smart="0" playlistType="audio" composite="/playlists/24053/composite/1713319718" viewCount="1" lastViewedAt="1713319717" duration="7984000" leafCount="30" addedAt="1713319717" updatedAt="1713319718"></Playlist>
</MediaContainer>
```

### rate 评分歌曲/专辑/歌手

PUT: `[host]/:/rate`

query:

| 参数名 | 备注 |
| --- | --- |
| key | 歌曲/专辑/歌手ID |
| identifier | `com.plexapp.plugins.library` |
| rating | 评分，0-10之间 |

### scrobble 滚动播放记录

**更新播放进度**

GET: `[host]/:/timeline`

query:

| 参数名 | 备注 |
| --- | --- |
| ratingKey | 歌曲ID |
| time | 播放进度，单位：ms |
| state | 播放状态，可选值：`playing`, `paused` |

> 此接口不会将歌曲播放次数+1，需要手动调用下面的接口。

**将歌曲标记为已播放**

GET: `[host]/:/scrobble`

query:

| 参数名 | 备注 |
| --- | --- |
| key | 歌曲ID |
| identifier | `com.plexapp.plugins.library` |

### sections 获取歌曲列表

GET: `[host]/library/sections/[sectionKey]/all`

query:

| 参数名 | 备注 |
| --- | --- |
| type | 类型，固定为 `10` |
| sort | 排序方式，可选值：`random`, `addedAt`, `year`, `lastViewedAt`, `titleSort`, `album.titleSort`, `ratingCount`，若要倒序，则使用 `addedAt:desc` 这种格式。 |
| includeCollections | `1` |
| includeExternalMedia | `1` |
| artist.id | 歌手ID，可选 |
| userRating | 评分，可选 |
| title | 标题，可选 |
| X-Plex-Container-Start | 起始行数 |
| X-Plex-Container-Size | 结果数量 |

response:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<MediaContainer size="1" totalSize="19403" offset="0" allowSync="1" art="/:/resources/artist-fanart.jpg" identifier="com.plexapp.plugins.library" librarySectionID="1" librarySectionTitle="音乐" librarySectionUUID="0d645d8b-6bca-44f5-8105-7b90f6be6d67" mediaTagPrefix="/system/bundle/media/flags/" mediaTagVersion="1667296136" nocache="1" thumb="/:/resources/artist.png" title1="音乐" title2="All Artists" viewGroup="artist" viewMode="65592">
	<Track ratingKey="3609" key="/library/metadata/3609" parentRatingKey="3608" grandparentRatingKey="3605" guid="plex://track/6344359ca5c478aa2b7a54b8" parentGuid="plex://album/633ae09ba5c478aa2b6619d2" grandparentGuid="plex://artist/633ae07aa5c478aa2b62fd54" type="track" title="可能否" grandparentKey="/library/metadata/3605" parentKey="/library/metadata/3608" grandparentTitle="木小雅" parentTitle="可能否" summary="" index="1" parentIndex="1" ratingCount="673" userRating="10.0" lastRatedAt="1713319768" parentYear="2018" thumb="/library/metadata/3608/thumb/1710954289" parentThumb="/library/metadata/3608/thumb/1710954289" duration="227944" addedAt="1638002162" updatedAt="1711289822">
		<Media id="2800" duration="227944" bitrate="128" audioChannels="2" audioCodec="mp3" container="mp3">
			<Part id="2800" key="/library/parts/2800/1711051647/file.mp3" duration="227944" file="/volume1/music/木小雅/可能否/可能否.mp3" size="3727358" container="mp3" hasThumbnail="1" />
		</Media>
	</Track>
</MediaContainer>
```

### metadata 获取歌曲信息

GET: `[host]/library/metadata/[id]`

query:

| 参数名 | 备注 |
| --- | --- |
| includeConcerts | `1` |
| includeExtras | `1` |
| includeOnDeck | `1` |
| includePopularLeaves | `1` |
| includePreferences | `1` |
| includeChapters | `1` |
| includeStations | `1` |
| includeMarkers | `1` |
| includeExternalMedia | `1` |
| asyncAugmentMetadata | `1` |
| includeRelated | `1` |
| checkFiles | `1` |

response:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<MediaContainer size="1" allowSync="1" augmentationKey="/library/metadata/augmentations/88" identifier="com.plexapp.plugins.library" librarySectionID="1" librarySectionTitle="音乐" librarySectionUUID="0d645d8b-6bca-44f5-8105-7b90f6be6d67" mediaTagPrefix="/system/bundle/media/flags/" mediaTagVersion="1667296136">
	<Track ratingKey="3609" key="/library/metadata/3609" parentRatingKey="3608" grandparentRatingKey="3605" guid="plex://track/6344359ca5c478aa2b7a54b8" parentGuid="plex://album/633ae09ba5c478aa2b6619d2" grandparentGuid="plex://artist/633ae07aa5c478aa2b62fd54" type="track" title="可能否" grandparentKey="/library/metadata/3605" parentKey="/library/metadata/3608" librarySectionTitle="音乐" librarySectionID="1" librarySectionKey="/library/sections/1" grandparentTitle="木小雅" parentTitle="可能否" summary="" index="1" parentIndex="1" ratingCount="673" userRating="10.0" lastRatedAt="1713319768" parentYear="2018" thumb="/library/metadata/3608/thumb/1710954289" parentThumb="/library/metadata/3608/thumb/1710954289" duration="227944" addedAt="1638002162" updatedAt="1711289822">
		<Media id="2800" duration="227944" bitrate="128" audioChannels="2" audioCodec="mp3" container="mp3">
			<Part accessible="1" exists="1" id="2800" key="/library/parts/2800/1711051647/file.mp3" duration="227944" file="/volume1/music/木小雅/可能否/可能否.mp3" size="3727358" container="mp3" hasThumbnail="1">
				<Stream id="2800" streamType="2" selected="1" codec="mp3" index="0" channels="2" bitrate="128" albumGain="-3.84" albumPeak="1.000000" albumRange="12.185394" audioChannelLayout="stereo" gain="-3.84" loudness="-14.16" lra="12.19" peak="1.000000" samplingRate="44100" displayTitle="MP3 (Stereo)" extendedDisplayTitle="MP3 (Stereo)"></Stream>
			</Part>
		</Media>
		<Guid id="mbid://ea6cdd7e-d9fc-419c-b994-01c1c1f79b5c" />
		<Extras size="0"></Extras>
		<Related></Related>
	</Track>
</MediaContainer>
```

### children 获取专辑中的歌曲

GET: `[host]/library/metadata/[id]/children`

query:

| 参数名 | 备注 |
| --- | --- |
| excludeAllLeaves | `1` |

### items 获取歌单中的歌曲

GET: `[host]/playlists/[id]/items`

query:

| 参数名 | 备注 |
| --- | --- |
| type | `track` |

response:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<MediaContainer size="2" composite="/playlists/23237/composite/1712824484" duration="490" leafCount="2" playlistType="audio" ratingKey="23237" smart="0" title="古风">
	<Track ratingKey="20887" key="/library/metadata/20887" parentRatingKey="20886" grandparentRatingKey="20808" guid="local://20887" parentGuid="local://20886" grandparentGuid="plex://artist/5d07bc92403c64029052193c" type="track" title="是你" grandparentKey="/library/metadata/20808" parentKey="/library/metadata/20886" librarySectionTitle="音乐" librarySectionID="1" librarySectionKey="/library/sections/1" grandparentTitle="弦子" parentTitle="长风渡 影视原声带" originalTitle="弦子/李茂" summary="" index="3" parentIndex="1" userRating="10.0" viewCount="10" lastViewedAt="1713282859" lastRatedAt="1711882837" parentYear="2023" thumb="/library/metadata/20886/thumb/1710944657" parentThumb="/library/metadata/20886/thumb/1710944657" playlistItemID="46" duration="253397" addedAt="1710940658" updatedAt="1711291448">
		<Media id="16815" duration="253397" bitrate="1701" audioChannels="2" audioCodec="flac" container="flac">
			<Part id="16815" key="/library/parts/16815/1711029835/file.flac" duration="253397" file="/volume1/music/弦子/李茂/长风渡 影视原声带/弦子 _ 李茂 - 是你.flac" size="53958405" container="flac" hasThumbnail="1" />
		</Media>
	</Track>
	<Track ratingKey="23890" key="/library/metadata/23890" parentRatingKey="23888" grandparentRatingKey="6277" guid="com.plexapp.agents.qqmusic://0011CYh41MbdFm/001YwctD3AleZ4/-1/10?lang=zh" parentGuid="com.plexapp.agents.qqmusic://0011CYh41MbdFm/001YwctD3AleZ4?lang=zh" grandparentGuid="com.plexapp.agents.qqmusic://0011CYh41MbdFm?lang=zh" parentStudio="寰亚音乐" type="track" title="Anita" grandparentKey="/library/metadata/6277" parentKey="/library/metadata/23888" librarySectionTitle="音乐" librarySectionID="1" librarySectionKey="/library/sections/1" grandparentTitle="梅艳芳" parentTitle="封面女郎" originalTitle="梅艳芳" summary="" index="10" viewCount="1" lastViewedAt="1712824795" parentYear="1990" thumb="/library/metadata/23888/thumb/1712719241" parentThumb="/library/metadata/23888/thumb/1712719241" grandparentThumb="/library/metadata/6277/thumb/1711889072" playlistItemID="48" duration="237373" addedAt="1712719232" updatedAt="1712719399">
		<Media id="19277" duration="237373" bitrate="842" audioChannels="2" audioCodec="flac" container="flac">
			<Part id="19277" key="/library/parts/19277/1712645733/file.flac" duration="237373" file="/volume1/music/梅艳芳/封面女郎/梅艳芳-Anita.flac" size="25106519" container="flac" hasThumbnail="1" />
		</Media>
	</Track>
</MediaContainer>
```

### 收藏歌曲/专辑/歌手

Plex 没有收藏功能，建议筛选评分为 10 的作为收藏项目。

### transcode 歌曲播放链接

**不转码**

首先需要获取歌曲信息中的 `Track.Media.Part.key`

GET: `[host]/[partKey]`

query:

| 参数名 | 备注 |
| --- | --- |
| X-Plex-Token | 访问令牌 |
| X-Plex-Platform | 操作系统，可选值：`Web`, `Android`, `iOS`, `MacOSX`, `Windows`, `Linux` |

**转码**

GET: `[host]/music/:/transcode/universal/start`

query:

| 参数名 | 备注 |
| --- | --- |
| path | `/library/metadata/[id]` |
| directPlay | `0` |
| musicBitrate | 比特率 |
| session | 会话ID，客户端随机生成 |
| X-Plex-Token | 访问令牌 |
| X-Plex-Platform | 操作系统，可选值：`Web`, `iOS` |

:::note

转码还有更详细的配置，这里记录是直接返回转码后的文件的链接，若需 hls 等其他协议，请参考顶部列出的参考文档。

:::

### items 添加歌曲到歌单

PUT: `[host]/playlists/[id]/items`

query:

| 参数名 | 备注 |
| --- | --- |
| uri | `server://[machineIdentifier]/com.plexapp.plugins.library/library/metadata/[歌曲ID列表]` |

### items 从歌单中移除歌曲

DELETE: `[host]/playlists/[id]/items/[songId]`

:::note

此接口只能单个移除。

:::

### playlists 更新歌单信息

PUT: `[host]/playlists/[id]`

query:

| 参数名 | 备注 |
| --- | --- |
| title | 歌单名 |
| summary | 评论，可选 |