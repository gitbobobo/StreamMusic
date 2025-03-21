---
sidebar_position: 5
---

# CarPlay {#carplay}

## Lyrics Display {#lyrics}

Due to Apple's safety restrictions, **full lyrics display is prohibited in CarPlay**.  
Stream Music provides a **single-line lyric preview** by enabling the **"Lyrics - Lyric Notifications"** switch.

## Limitations {#limitation}

**The app must be open on your phone** for CarPlay functionality.  

When the app is closed, the Flutter engine remains uninitialized, preventing CarPlay connection detection and playback control.

:::info

Related issue: [CarPlay app requires Flutter App open first?](https://github.com/oguzhnatly/flutter_carplay/issues/12)  

Current workarounds allow CarPlay interface display without opening the app, but **music playback fails**, and the UI may freeze after manually launching the app. Further investigation is ongoing.

:::