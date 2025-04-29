---
sidebar_position: 5
---

# Miscellaneous {#other}

## Partitions {#partition}

Some users utilize Stream Music not only for music but also for audiobooks. The partition feature helps separate different audio types to avoid interference.

Currently, **Emby, Jellyfin, and Plex** support multiple media libraries (partitions):

- **Emby**: Set media library type to "Audiobooks" or "Music".
- **Jellyfin/Plex**: Must use "Music" type, as their "Books" category is designed for text-based content with incompatible layouts.

## List Elements {#list}

- **Green index numbers** indicate unplayed tracks (useful for audiobook progress tracking).  
  ![](https://oss2.aqzscn.cn/resource/blog/img/2024/90011-293fd6ac80a1ce9bc85adf176c807e19.png)

- **Track numbers** in album lists show disc number (top-right) and track order (index).  
  ![](https://oss2.aqzscn.cn/resource/blog/img/2024/90642-5882f5ffcf3b92988a49aaa5dac913c3.png)

- **Wrench icon** in artist lists indicates duplicate files.  
  ![](https://oss2.aqzscn.cn/resource/blog/img/2024/7ec2a-423ad72f94ace289a7d801936d02e3f6.png)

## Cross-Device Configuration Sync {#qr}

Sync server settings across devices via QR code or LAN URL to avoid repetitive setup:

- Access via **"Add Library"** or **Help → Data Sync**.
- Desktop users can manually enter the URL shown below the QR code.

:::caution

1. Data is transmitted over LAN with basic encryption. Use only in trusted networks.
2. QR scanning uses [mobile_scanner](https://github.com/juliansteenbakker/mobile_scanner). Retry if recognition fails.

:::

## Lyrics {#lyrics}

Supports **LRC format** ([Wikipedia](https://en.wikipedia.org/wiki/LRC_(file_format))). Bilingual lyrics formats:

**Same timestamp**  

```
[00:01.123] Lyrics
[00:01.123] Translation
```

**Bracketed format**  

```
[00:01.123] Lyrics【Translation】
```