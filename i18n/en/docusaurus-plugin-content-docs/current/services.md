---
sidebar_position: 2
---

# Services {#services}

From my personal experience, there is currently no perfect music service - each has its own pros and cons. You should choose based on your specific needs.

## Supported Versions {#versions}

- Navidrome 0.49.3 and above
- Plex 1.29.2 and above (supports OTP verification code login, shared music libraries not currently supported)
- AudioStation DSM 6 and above (supports OTP verification code login)
- Emby 4.7.14.0 and above
- Jellyfin 10.8.10 and above
- Subsonic 1.15.0 and above

## Feature Comparison {#comparison}

`-` Unknown

| Feature | Subsonic | Navidrome | Audio Station | Emby | Jellyfin | Plex |
| ------- | ------- | ------- | --- | --- | --- | --- |
| Embedded Lyrics<sup>1</sup> | - | ✅ |  | ✅ | ✅ | |
| External Lyrics | - |  | ✅ | ✅ | ✅ | ✅ |
| Online Lyrics | - |  | ✅ | ✅ | ✅ | ✅ |
| Artist Bio | - | ✅ | | ✅ | ✅ | ✅ |
| Artist Image | - | *<sup>2</sup> | *<sup>3</sup> | ✅ | ✅ | ✅ |
| Multiple Artists | - |  | - | ✅ | ✅ | |
| Replay Gain | - | ✅  | ✅ | | | ✅ |
| Rating<sup>4</sup> | ✅ | ✅  | ✅ |  |  | ✅ |
| Favorites<sup>5</sup> | ✅ | ✅  | | ✅ | ✅ | |
| Folder View | - | | ✅ | ✅ | | ✅ |
| Delete API | - | | | ✅ | ✅ | ✅ |


1. Since v1.2.8, Stream Music can read embedded lyrics when "Cache While Playing" is enabled.
2. For Navidrome artist images: Requires Spotify API configuration (may not work effectively in Chinese environments) or placing an image named `artist.*` in the artist folder. [Artwork location resolution](https://www.navidrome.org/docs/usage/artwork/#artists)
3. Audio Station uses album artwork from music library for artist images.
4. Audio Station only supports song ratings.
5. Audio Station and Plex lack favorites feature. Stream Music treats songs rated 🌟🌟🌟🌟🌟 as favorites.