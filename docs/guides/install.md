---
sidebar_position: 1
---

# 安装

Android 和 Windows 安装教程，最新安装包可在[这里](../versions/latest)找到。

## Android

Android 一共提供四个安装包，分别对应不同的芯片架构。

一般最近几年的手机选择 `app-arm64-v8a-release.apk` 即可，若不确定自己手机的芯片架构，请选择 `app-release.apk` 下载安装。

:::caution

不同架构的安装包不能覆盖安装，只能选择卸载重装。

:::

## Windows

Windows 版音流目前只提供 x64 架构的 msix 格式安装包，这是微软应用商店的安装格式，因此在商店外安装，需要先在电脑上安装开发者对应的证书。

import Button from '@mui/material/Button';
import DownloadIcon from '@mui/icons-material/Download';

<Button variant="contained" startIcon={<DownloadIcon />} href="https://oss.aqzscn.cn/stream-music/stream_music_win.crt">音流证书</Button>

### 一、标准安装方式

双击证书文件开始安装，安装位置选择`本地计算机`。

![Snipaste_2023-12-29_20-37-44](https://oss.aqzscn.cn/halo/2023/Snipaste_2023-12-29_20-37-44.png)

下一步，将证书存储到`受信任的根证书颁发机构中`。

:::info

收到用户反馈：添加到 `受信任人` 后即可安装。

:::

![Snipaste_2023-12-29_20-39-16](https://oss.aqzscn.cn/halo/2023/Snipaste_2023-12-29_20-39-16.png)

安装完成后，以后就可以直接双击 `msix` 格式的安装包进行安装了。

### 二、非标准安装方式

msix 格式对系统的要求较高，需要 win10 以上才可使用，对于还停留在 win7 或 win8 的用户，可通过此种方式安装。

:::warning

win7 由于缺少较多依赖，且 Flutter 官方已不再支持，不建议尝试安装。

:::

首先下载音流 msix 格式的安装包，使用任意压缩软件打开：

![Snipaste_2023-12-29_20-46-42](https://oss.aqzscn.cn/halo/2023/Snipaste_2023-12-29_20-46-42.png)

把压缩包内的文件全部解压到你想要安装的位置，然后通过 `stream_music.exe` 打开软件即可。

![Snipaste_2023-12-29_20-49-22](https://oss.aqzscn.cn/halo/2023/Snipaste_2023-12-29_20-49-22.png)