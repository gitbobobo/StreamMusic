---
sidebar_position: 3
---

# Playback Logic {#playback}

Stream Music's playback logic differs slightly from common music apps, incorporating unique design philosophies.  
**New users are strongly encouraged to read this section for optimal usage.**

## Playback Modes {#mode}

By default, Stream Music uses **Queue Playback**. Enable the loop switch to apply looping to both queue and shuffle modes.

![](https://oss.aqzscn.cn//resource/blog/img/2023/860419a28223c06c03964ff34a5a8668.png)

When selecting songs from a list, queue playback is the default behavior.

![](https://oss.aqzscn.cn//resource/blog/img/2023/e3f0f7469a58b3955598f8965eeef658.png)

If the list header includes the following buttons:  
- Click the **circle icon** to jump to the current track.  
- Click the **double-arrow icon** to switch the list's playback mode.

:::tip Track Navigation Upgrade (v1.3.0):

1. If the playback queue matches the current list, navigation jumps to the current track.  
2. If the queues differ, navigation jumps to the first unplayed track in the list.  

For paginated lists: If no matching track exists on the current page, scrolling to the bottom triggers loading the next page.  
:::

**Playback mode changes from song lists are saved per list type.**  
Changes from the playback queue or player page are temporary and session-only.

## Playback Controls {#control}

![](https://oss.aqzscn.cn//resource/blog/img/2023/15d11e29bb8e27f58378743eb86f6fd0.png)

Control bar features:  
- Tap the cover to play/pause.  
- Tap the lyrics area to enter full-screen playback.  
- Tap the right-side button to open the current queue.  

**Swipe gestures on lyrics area**:  
- Swipe right ➔ Previous track.  
- Swipe left ➔ Next track.

## DLNA {#dlna}

- DLNA streams the server's playback URL to devices. Ensure DLNA devices can access your server.  
- For compatibility, playback status updates use **polling**, causing ~2-second delays for some operations.  