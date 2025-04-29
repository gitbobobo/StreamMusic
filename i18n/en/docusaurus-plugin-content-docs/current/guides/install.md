---
sidebar_position: 1
---

# Installation {#installation}

Installation guides for Android and Windows. Latest installers can be found [here](../versions/latest).

## Android {#android}

Four APK variants are provided for different chip architectures:

- For modern smartphones (released in recent years), choose `app-arm64-v8a-release.apk`.
- If unsure about your device's architecture, download `app-release.apk`.

:::caution

APKs for different architectures **cannot** be installed over each other. Uninstall existing versions before switching architectures.

:::

## Windows {#windows}

Windows version currently provides only **x64 MSIX** installer (Microsoft Store format). To install outside the Store, you must first install the developer certificate.

import Button from '@mui/material/Button';
import DownloadIcon from '@mui/icons-material/Download';

<Button variant="contained" startIcon={<DownloadIcon />} href="https://oss2.aqzscn.cn/stream-music/stream_music_win.crt">Stream Music Certificate</Button>

### Standard Installation {#standard}

1. Double-click the certificate file. Select **Local Computer** during installation.
   
   ![Snipaste_2023-12-29_20-37-44](https://oss2.aqzscn.cn/halo/2023/Snipaste_2023-12-29_20-37-44.png)

2. Store the certificate in **Trusted Root Certification Authorities**.
   
   :::info

   User feedback: Adding to "Trusted People" also works.

   :::

   ![Snipaste_2023-12-29_20-39-16](https://oss2.aqzscn.cn/halo/2023/Snipaste_2023-12-29_20-39-16.png)

3. After certificate installation, double-click the MSIX file to install Stream Music.

### Alternative Installation (Legacy Windows) {#legacy}

MSIX requires Windows 10 or later. For Windows 7/8 users:

:::warning

**Not recommended for Windows 7** due to missing dependencies and lack of Flutter support.

:::

1. Download the MSIX file and open it with any archive tool (e.g., 7-Zip):

   ![Snipaste_2023-12-29_20-46-42](https://oss2.aqzscn.cn/halo/2023/Snipaste_2023-12-29_20-46-42.png)

2. Extract all files to your desired installation directory.

3. Launch via `stream_music.exe`:

   ![Snipaste_2023-12-29_20-49-22](https://oss2.aqzscn.cn/halo/2023/Snipaste_2023-12-29_20-49-22.png)