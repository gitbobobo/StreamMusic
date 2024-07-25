---
sidebar_position: 99
---

# 最新版本

更新于：2024-07-25

:::tip 护甲+1

import DayCounter from '@site/src/components/DayCounter';

音流发布至今已有 <DayCounter dateStr="2023-06-06"/> 天了，共更新了 30 个版本，还是个很年轻的播放器呢～

因个人开发经验与精力所限，且要兼顾多个平台与音乐服务，更新速度与 bug 解决速度难免要慢一些，望诸君见谅。

但我始终相信：下个版本会更好！

:::

## V1.3.0（2024-07-25）

:::success 早鸟优惠<sup>2</sup>

为庆祝音流达成适配安卓 TV 的里程碑，特开启第二波早鸟优惠，活动时间为 2024-07-26 至 2024-08-08。

在此期间音流会员价格将降低 10 元，您可以 38 元的特惠价购入音流终身会员。

活动结束后，音流终身会员价格将调整至 58 元。

:::

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import Button from '@mui/material/Button';
import WindowIcon from '@mui/icons-material/Window';
import AppleIcon from '@mui/icons-material/Apple';
import AndroidIcon from '@mui/icons-material/Android';

<Tabs groupId="operating-systems">
<TabItem value="android" label="Android">
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.0/app-arm64-v8a-release.apk">ARM64 版本</Button>
    <span class="ml-md gray">MD5: afe89bf8a90d99b9bff59b564269cae1</span>
</div>
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.0/app-armeabi-v7a-release.apk">ARMV7 版本</Button>
    <span class="ml-md gray">MD5: f86ee784113971179266b401f78fda09</span>
</div>
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.0/app-x86_64-release.apk">x86 版本</Button>
    <span class="ml-md gray">MD5: f13062c48f656e8b8d438edc5c0f0a4c</span>
</div>
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.0/app-release.apk">通用版本（体积较大）</Button>
    <span class="ml-md gray">MD5: ebe45f09ef85adec90dfc6bbcabda1b2</span>
</div>
</TabItem>

<TabItem value="win" label="Windows">
<div class="mv-sm">
    <Button variant="contained" startIcon={<WindowIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.0/stream_music_1.3.0.5.msix">立即下载</Button>
    <span class="ml-md gray">MD5: 94a7f1c000e033c59fbed040590bb94c</span>
</div>
</TabItem>

<TabItem value="mac" label="macOS">

:::caution

Mac OS 请暂时不要升级至 Beta 3 版本，会导致音流无法使用。

:::

<div class="mv-sm">
    <Button variant="contained" startIcon={<AppleIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.0/音流v1.3.0.dmg">立即下载</Button>
    <span class="ml-md gray">MD5: c622937c89b16df5eb510b129e1dd3c8</span>
</div>
</TabItem>
</Tabs>

更新内容：

- [适配安卓TV](https://github.com/gitbobobo/StreamMusic/issues/23)，建议手机上下载安装包后，通过 [localsend](https://github.com/localsend/localsend) 发送给TV端，以便后续更新。
- 新增扫码同步数据的功能（若无法识别请返回重进换一个二维码）
- 支持[多服务器切换](https://github.com/gitbobobo/StreamMusic/issues/35)，支持分区选择
- 支持按流派筛选歌曲/专辑/歌手
- 支持自定义歌单排序
- 提升线路切换速度（主线路连接失败后，优先使用最先连接成功的线路）
- 增加标记歌曲为已播放的功能
- 升级歌曲定位功能
- [按评分筛选增加没有评分的选项](https://github.com/gitbobobo/StreamMusic/issues/362)
- 支持[主线路编辑](https://github.com/gitbobobo/StreamMusic/issues/327)
- 依次同步歌曲、专辑和歌手数据以解决[服务器并发请求过多无法正常获取响应](https://github.com/gitbobobo/StreamMusic/issues/365)的问题
- 长音频播放页的上一曲下一曲按钮改为快进快退
- [播放时忽略未完整缓存的歌曲](https://github.com/gitbobobo/StreamMusic/issues/316)
- [切歌之后如果没有图片，显示默认 Logo](https://github.com/gitbobobo/StreamMusic/issues/305)
- 调整Windows返回按钮位置
- [Audio Station 支持选择转码比特率](https://github.com/gitbobobo/StreamMusic/issues/286)
- 支持 [Jellyfin 的歌词接口](https://github.com/gitbobobo/StreamMusic/issues/289)
- [Emby/Jellyfin 不校验密码是否填写](https://github.com/gitbobobo/StreamMusic/issues/377)
- [Navidrome 占位图片视为无图片](https://github.com/gitbobobo/StreamMusic/issues/355)
- 修复媒体库模式下歌手页面无法搜索歌手的问题
- 修复[媒体库模式评分和收藏操作界面不更新](https://github.com/gitbobobo/StreamMusic/issues/348)的问题
- 修复自动下载会重复下载歌曲的问题
- 修复[自定义歌词接口切换歌词失效](https://github.com/gitbobobo/StreamMusic/issues/392)
- 修复[重新打开app后无法记忆上次播放位置的问题](https://github.com/gitbobobo/StreamMusic/issues/236)
- 修复一些卡在加载中提示的情况
- 修复单曲循环只上报了一次播放记录的问题
- 修复专辑页面和歌单页面的排序问题，[#301](https://github.com/gitbobobo/StreamMusic/issues/301), [#303](https://github.com/gitbobobo/StreamMusic/issues/303)
- 修复ogg格式只有第一次能播放的问题（缓存的ogg格式数据有问题，临时处理方式：对所有ogg格式转码后播放）
- 修复[搜索结果页歌曲无法播放的问题](https://github.com/gitbobobo/StreamMusic/issues/297)
- 修复[流派详情页未筛选数据的问题](https://github.com/gitbobobo/StreamMusic/issues/422)
- 修复 Emby 可能不显示歌词的问题
- 修复 [Emby 最近播放和最常播放顺序颠倒](https://github.com/gitbobobo/StreamMusic/issues/376) 的问题
- 修复 [Audio Station 登录过期后不显示图片，无法播放的问题](https://github.com/gitbobobo/StreamMusic/issues/321)
- 修复[媒体库模式无法识别MTW的歌手简介的问题](https://github.com/gitbobobo/StreamMusic/issues/311)
- 修复群晖或 Plex 自动获取的 IP 会重复添加的问题
- [Android] 修复[关闭系统省电模式后，从任务管理器杀死应用，音乐仍在播放的问题](https://github.com/gitbobobo/StreamMusic/issues/239)

文档更新：

使用说明部分有较多更新，建议完整阅读。
