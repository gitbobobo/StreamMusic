---
sidebar_position: 4
---

# Track Playback History via Last.FM {#lastfm}

Seeing others share ​**annual music reports** at year-end while you have none? Don't worry! You can record your listening history through Last.FM and happily share your stats with friends later～

![](https://oss.aqzscn.cn/resource/blog/img/2024/8e26c-0835da59547fd34cc652db034d977f09.png)

Since StreamMusic isn't open-source, direct Last.FM integration might pose copyright risks. This guide demonstrates server-side configuration instead.

:::info
I've emailed Last.FM for API access but received no response.
:::

## Create Last.FM Account {#account}

Register at https://www.last.fm/. ​**QQ email addresses may fail registration**.

## Report Plays via Navidrome {#navidrome}

Enable Last.FM scrobbling in Navidrome's web interface:

![](https://oss.aqzscn.cn/resource/blog/img/2024/b269c-862548c7f7e351f285de76a02c0b8389.png)

## Report Plays via Emby {#emby}

1. Install the Last.fm metadata plugin under "Metadata" in Emby's admin panel.
2. Restart server.
3. Configure via sidebar settings:

![](https://oss.aqzscn.cn/resource/blog/img/2024/58760-e43cba8065b629dfcf3285068d40d7eb.png)