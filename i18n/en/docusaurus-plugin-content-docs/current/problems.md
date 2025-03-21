---
sidebar_position: 7
---

# Issues {#issues}

If you encounter any issues or have suggestions while using the software, please visit the [GitHub repository](https://github.com/gitbobobo/StreamMusic):

1. Go to the **Issues** tab and search for existing reports.
2. If no similar issue exists, create a new one and **provide detailed information**, such as OS version, server version, Stream Music version, logs, screenshots, etc. **The more details you provide, the easier it is to reproduce and resolve the issue.**

:::note Viewing Logs

On the About page, tap the version number repeatedly to enable Developer Mode.

:::

## Music Services {#services}

### Unable to Log In {#login}

Possible causes:

- Incorrect username/password.
- Invalid server address (must include protocol, IP, and port).
- Self-signed or incomplete SSL certificate chain.
- Proxy software intercepting `127.0.0.1`.

### Navidrome Fails to Scan Beyond 50,000 Songs {#navidrome-scan}

In Navidrome versions ≤0.52, there’s a known bug in the song query logic. Upgrade to the latest version.  
If upgrading is not possible, set the Docker environment variable `ND_DEVOFFSETOPTIMIZE` to a value greater than your total song count.

:::info

Related issue: [The retrieval of data fails when sorting by createAt after the number of songs exceeds 50,000.](https://github.com/navidrome/navidrome/issues/3006)

:::

### Fuzzy Search Not Working {#search}

- **Direct Connection Mode**: Fuzzy search depends on server support. For Navidrome, enable the `SearchFullString` environment variable.  
- **Library Mode**: Fuzzy search is client-side. Report any failures promptly.

## Playback {#playback}

### Android Background Playback Pauses (No Sound) {#background}

1. **Stream Music** → **Help** → Disable battery optimization.  
2. **System Settings** → **Stream Music** → Network & Data → Allow background data usage.  
   *Steps may vary by device. For Huawei: Battery → More Settings → Keep Network Connected During Sleep.*

### Playback Duration Keeps Updating {#transcoding}

This occurs when the server is transcoding the track. The displayed duration reflects the buffered content. Wait for transcoding to complete.

### Mobile Data Playback Fails {#ffmpeg}

- Ensure your server is publicly accessible.  
- If transcoding fails (common on mobile data), check if `ffmpeg` is properly configured on the server.  

:::info

Recommendation: Use Docker for server deployment to avoid configuration issues.

:::

## Platform-Specific {#platform}

### Android Notification Controls Fail {#notification}

This is likely an OS bug. Disable battery optimization for Stream Music in system settings.  

:::info

Related issue: [Android notification controls stop working](https://github.com/gitbobobo/StreamMusic/issues/145).  
Post v1.2.8, the Help page detects battery optimization status and redirects to settings.

:::

### Android Car Bluetooth Metadata Not Updating {#bluetooth}

Occurs after screen lock. Track progress: [Android MediaItem not updating via Bluetooth](https://github.com/ryanheise/audio_service/issues/908).

### Bitwarden Clicks Blocked by Floating Lyrics (Android) {#overlay}

Locked lyrics overlay may interfere. Unlock/disable lyrics temporarily via the notification panel.

### High CPU Usage/Overheating {#cpu}

Caused by Flutter animations. Enable **Power Saving Mode** in theme settings (default: ON).  

:::info

Related issue: [High CPU usage and overheating](https://github.com/gitbobobo/StreamMusic/issues/60).

:::

### CarPlay/Notification Controls Fail to Skip Tracks {#carplay-notification}

Disable **"Allow Concurrent Playback"** in settings. This is an iOS limitation.

## Membership {#vip}

### Invalid Signature When Restoring Purchase {#signature}

Likely caused by incorrect device time. Sync your device clock.

### Invalid Email Format {#email}

Type the email manually. Avoid pasting extra spaces or line breaks.

### Device Limit {#device-limit}

Exceeding 7 devices automatically logs out the oldest one. No manual management needed.

## other {#other}

### Security Concerns {#security}

Some users worry about credential leaks. Clarifications:  

- NAS music is niche; data volume is too small for commercial exploitation.  
- Tech-savvy NAS users would detect malicious code, risking developer reputation.  

Still concerned? Use a dedicated music-only account. If server IP exposure worries you, choose trusted software instead.