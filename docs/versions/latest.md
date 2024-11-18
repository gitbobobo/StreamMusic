---
sidebar_position: 99
---

# 最新版本

更新于：2024-11-17

:::tip 护甲+1

import DayCounter from '@site/src/components/DayCounter';

音流发布至今已有 <DayCounter dateStr="2023-06-06"/> 天了，共更新了 33 个版本，还是个很年轻的播放器呢～

因个人开发经验与精力所限，且要兼顾多个平台与音乐服务，更新速度与 bug 解决速度难免要慢一些，望诸君见谅。

但我始终相信：下个版本会更好！

:::

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import Button from '@mui/material/Button';
import WindowIcon from '@mui/icons-material/Window';
import AppleIcon from '@mui/icons-material/Apple';
import AndroidIcon from '@mui/icons-material/Android';

## V1.3.3（2024-11-17）

<Tabs groupId="operating-systems">
<TabItem value="android" label="Android">
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.3/app-arm64-v8a-release.apk">ARM64 版本</Button>
    <span class="ml-md gray">MD5: 010b0ccd625d3f7c872dab9da7502df6</span>
</div>
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.3/app-armeabi-v7a-release.apk">ARMV7 版本</Button>
    <span class="ml-md gray">MD5: ae92e104f118c6b6f0a4256003cd8952</span>
</div>
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.3/app-x86_64-release.apk">x86 版本</Button>
    <span class="ml-md gray">MD5: 0b44f215d577ecedef30b2e0f715a815</span>
</div>
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.3/app-release.apk">通用版本（体积较大）</Button>
    <span class="ml-md gray">MD5: f6ff5c17704238315dfa5d82a26f126d</span>
</div>
</TabItem>

<TabItem value="win" label="Windows">
<div class="mv-sm">
    <Button variant="contained" startIcon={<WindowIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.3/stream_music_1.3.3.6.msix">立即下载</Button>
    <span class="ml-md gray">MD5: 2d474371df21c7d8cd1cd75e98f46363</span>
</div>

:::caution

若安装失败请查看[安装教程](../guides/install)

:::
</TabItem>

<TabItem value="mac" label="macOS">
<div class="mv-sm">
    <Button variant="contained" startIcon={<AppleIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.3/StreamMusic_1.3.3.dmg">立即下载</Button>
    <span class="ml-md gray">MD5: d2e1ca2f3b7ac1c2229499ef744565fb</span>
</div>
</TabItem>
</Tabs>

更新内容:

- 👑 桌面端支持迷你窗口
- 👑 iOS 14.2 及以上版本支持画中画歌词
- iOS 通知中心组件支持显示收藏按钮
- 桌面端新增[关闭窗口快捷键](https://github.com/gitbobobo/StreamMusic/issues/627)
- [桌面端支持全局热键](https://github.com/gitbobobo/StreamMusic/issues/363)，开关位于**帮助 - 快捷键**
- 多语言支持繁体中文
- 谷歌翻译接口可配置基础地址
- [自定义封面接口请求歌曲封面时会附加歌曲路径信息](https://github.com/gitbobobo/StreamMusic/issues/650)
- 调整安卓设置界面字体大小
- 媒体库模式在同步数据时可选择手动取消
- 支持[批量删除重复歌曲](https://github.com/gitbobobo/StreamMusic/issues/680)
- 优化[虚拟键盘自动隐藏逻辑](https://github.com/gitbobobo/StreamMusic/issues/639)
- 在不支持的服务端中隐藏文件夹和专辑艺术家的入口
- 安卓桌面歌词支持宽度调节
- 修复[安卓桌面歌词无法显示的问题](https://github.com/gitbobobo/StreamMusic/issues/615)
- 修复[逐字歌词解析问题](https://github.com/gitbobobo/StreamMusic/issues/605)
- 修复登录页面无法切换 TV 模式的问题
- 修复 Windows 端歌手详情页文字重叠的问题
- 修复[定时停止功能中，勾选播完当前歌曲后停止导致功能失效的问题](https://github.com/gitbobobo/StreamMusic/issues/618)
- 修复安卓耳机线控失效的问题
- 修复 DLNA 连接小爱音箱时无法更新播放状态的问题
- 修复切换资料库时首页部分数据未更新的问题

## V1.3.2（2024-10-04）

<Tabs groupId="operating-systems">
<TabItem value="android" label="Android">
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.2/app-arm64-v8a-release.apk">ARM64 版本</Button>
    <span class="ml-md gray">MD5: 39d89dca63685ef98c440ca5efd2abeb</span>
</div>
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.2/app-armeabi-v7a-release.apk">ARMV7 版本</Button>
    <span class="ml-md gray">MD5: 4fe07080fbe91f4f8b699a3da79c8aa4</span>
</div>
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.2/app-x86_64-release.apk">x86 版本</Button>
    <span class="ml-md gray">MD5: 0fff06886b64b713337682793426639a</span>
</div>
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.2/app-release.apk">通用版本（体积较大）</Button>
    <span class="ml-md gray">MD5: 99a4b99ed10d2d11e70318d925e30905</span>
</div>
</TabItem>

<TabItem value="win" label="Windows">
<div class="mv-sm">
    <Button variant="contained" startIcon={<WindowIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.2/stream_music_1.3.2.6.msix">立即下载</Button>
    <span class="ml-md gray">MD5: 81cf96d4ee3c6b122eab1456e6a673e3</span>
</div>

:::caution

若安装失败请查看[安装教程](../guides/install)

:::
</TabItem>

<TabItem value="mac" label="macOS">
<div class="mv-sm">
    <Button variant="contained" startIcon={<AppleIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.2/StreamMusic_1.3.2.dmg">立即下载</Button>
    <span class="ml-md gray">MD5: bbad7b8ad5030553dae4357b59a9bab0</span>
</div>
</TabItem>
</Tabs>

更新内容：

- 移动端添加桌面小组件（播放控制与实时歌词）
- 为设置界面项目添加图标(主题中开启)，并适应各平台风格
- 播放界面适应亮色风格
- 支持在应用内切换语言
- 优化歌手详情页在移动端横屏状态的表现
- [单曲循环时允许按下一曲切歌](https://github.com/gitbobobo/StreamMusic/issues/487)
- [AudioStation 支持按音轨号排序](https://github.com/gitbobobo/StreamMusic/issues/525)，新增按音轨号排序方式
- [稍微增加横屏状态下播放页封面的尺寸](https://github.com/gitbobobo/StreamMusic/issues/448)
- [重复歌曲数量大于 9 时显示为 9+](https://github.com/gitbobobo/StreamMusic/issues/589)
- 播放页的歌词选项添加「生成翻译」功能
- [优化屏幕常亮触发逻辑](https://github.com/gitbobobo/StreamMusic/issues/600)
- 媒体库模式下，[同年发行的专辑按照专辑名排序](https://github.com/gitbobobo/StreamMusic/issues/476)
- [媒体库模式使用实时搜索](https://github.com/gitbobobo/StreamMusic/issues/599)
- 修复 [Windows 端无法搜索到 DLNA 设备的问题](https://github.com/gitbobobo/StreamMusic/issues/578)
- 修复无法播放DSF格式的问题 #388 #548
- 优化歌曲缓存逻辑，现已重新支持不转码播放 ogg 格式
- 修复 [VIVO 系手机不显示通知组件的问题](https://github.com/gitbobobo/StreamMusic/issues/394)
- 修复安卓通知栏播放按钮无法点击的问题
- 修复 [Jellyfin 封面不显示](https://github.com/gitbobobo/StreamMusic/issues/535)的问题
- 修复[切换播放模式后界面未更新](https://github.com/gitbobobo/StreamMusic/issues/537)的问题
- 修复 Subsonic 直连模式获取不到歌手的歌曲列表的问题
- 修复 [AudioStation 全部播放随机范围过小](https://github.com/gitbobobo/StreamMusic/issues/526)的问题
- 修复[播放已下载歌曲无法自动切歌的问题](https://github.com/gitbobobo/StreamMusic/issues/557)
- 修复[歌单内包含重复歌曲导致无法在启动时恢复播放列表的问题](https://github.com/gitbobobo/StreamMusic/issues/538)
- 修复 [windows 端无法切换歌单的问题](https://github.com/gitbobobo/StreamMusic/issues/576)

## V1.3.1（2024-09-02）

<Tabs groupId="operating-systems">
<TabItem value="android" label="Android">
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.1/app-arm64-v8a-release.apk">ARM64 版本</Button>
    <span class="ml-md gray">MD5: dd95dadfc5e0da5390a56a4c2333b529</span>
</div>
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.1/app-armeabi-v7a-release.apk">ARMV7 版本</Button>
    <span class="ml-md gray">MD5: c6cc33ba5efa185d3daea8f62bdf399a</span>
</div>
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.1/app-x86_64-release.apk">x86 版本</Button>
    <span class="ml-md gray">MD5: be12b8d86a1d9867c6b2b6cfbddcee47</span>
</div>
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.1/app-release.apk">通用版本（体积较大）</Button>
    <span class="ml-md gray">MD5: 4e8d8000211401a7f1aa5f36a63ef0c7</span>
</div>
</TabItem>

<TabItem value="win" label="Windows">
<div class="mv-sm">
    <Button variant="contained" startIcon={<WindowIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.1/stream_music_1.3.1.5.msix">立即下载</Button>
    <span class="ml-md gray">MD5: 9eb42a5d0d3730034ec76030dee86bb9</span>
</div>

:::caution

若安装失败请查看[安装教程](../guides/install)

:::
</TabItem>

<TabItem value="mac" label="macOS">
<div class="mv-sm">
    <Button variant="contained" startIcon={<AppleIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.1/StreamMusic_1.3.1.dmg">立即下载</Button>
    <span class="ml-md gray">MD5: 156a5e98e00c9e0287f36169be4cbf38</span>
</div>

:::caution

当前版本修复了与最新版 Mac 系统的兼容问题，安装前需要先在访达 - 应用程序按 `Command + Delete` 删除之前安装的版本，否则会同时存在两个音流。

:::
</TabItem>
</Tabs>

更新内容：

- [DLNA 功能修复](https://github.com/gitbobobo/StreamMusic/issues/254)
- [Windows 新增任务栏快捷操作与播放进度显示](https://github.com/gitbobobo/StreamMusic/issues/220)
- 新增专辑艺术家列表（仅Emby和Jellyfin有效，其他服务端等同于歌手列表）
- 支持多艺术家跳转(此前默认跳转第一个)
- 支持[配置代理地址](https://github.com/gitbobobo/StreamMusic/issues/447)
- 去掉实时搜索逻辑（可能导致搜索时间过长），需按回车键触发搜索
- 手机端的首页显示资料库别名
- 调整纯色主题配色
- 对话框样式改为各个平台的原生样式，后续将逐步替换其他组件
- 支持[上报播放中的状态](https://github.com/gitbobobo/StreamMusic/issues/437)
- [歌曲详情显示缓存位置](https://github.com/gitbobobo/StreamMusic/issues/151)
- Emby/Jellyfin 增加全部分区的选项
- 封面显示逻辑调整回原来的（歌曲展示歌曲封面，专辑展示专辑封面）
- [修改歌曲列表默认封面](https://github.com/gitbobobo/StreamMusic/issues/468)
- 优化重定向歌曲资源的处理逻辑
- 调整歌词偏移后，按对勾会调用歌词确认接口
- [调整歌词与翻译的间距](https://github.com/gitbobobo/StreamMusic/issues/474)
- 同步数据的IP地址现可识别多网卡的IP地址
- [恢复自定义API保存按钮](https://github.com/gitbobobo/StreamMusic/issues/458)
- [媒体库模式文件夹模糊搜索](https://github.com/gitbobobo/StreamMusic/issues/481)不再对大小写敏感
- [提升歌手详情页按钮可见性](https://github.com/gitbobobo/StreamMusic/issues/477)
- 兼容 [macOS Beta 3](https://github.com/gitbobobo/StreamMusic/issues/414)
- 修复无法导入歌单的问题
- 修复自定义歌单顺序无法保存的问题
- 修复首页批量歌单歌曲时只能下载第一首的问题
- 兼容 [Jellyfin 10.8](https://github.com/gitbobobo/StreamMusic/issues/429)
- 修复 Plex 在 CarPlay 中点击歌曲列表后闪退的问题
- 修复 [Jellyfin 不显示封面的问题](https://github.com/gitbobobo/StreamMusic/issues/435)
- 修复无法删除已下载的歌曲的问题
- 修复媒体库模式下最近与最常播放不显示的问题
- 修复[直连模式下群晖无法按歌手筛选专辑和歌曲的问题](https://github.com/gitbobobo/StreamMusic/issues/433)
- 修复添加 BaseUrl 后无法播放的问题 [#438](https://github.com/gitbobobo/StreamMusic/issues/438) [#396](https://github.com/gitbobobo/StreamMusic/issues/396)
- 修复[无法播放文件夹下歌曲的问题](https://github.com/gitbobobo/StreamMusic/issues/473)
- 修复[媒体库模式下群晖无法按添加时间倒序](https://github.com/gitbobobo/StreamMusic/issues/459)的问题
- 修复[支付宝订单号恢复页面按钮不可用的问题](https://github.com/gitbobobo/StreamMusic/issues/453)
- 修复[低版本安卓无法恢复购买的问题](https://github.com/gitbobobo/StreamMusic/issues/469)
- 修复 [TV 版第二次打开时可能卡在启动页](https://github.com/gitbobobo/StreamMusic/issues/446)的问题
- 修复桌面端搜索到多个歌词时无法滚动选择的问题（添加底部指示器）
- 修复[随机播放歌单内歌曲时随机范围过小](https://github.com/gitbobobo/StreamMusic/issues/530)的问题
- 修复修改系统时区后歌词不会自动滚动的问题
- 修复[播放高码率文件可能出现电流声](https://github.com/gitbobobo/StreamMusic/issues/518)的问题


## V1.3.0（2024-07-25）

:::success 早鸟优惠<sup>2</sup>

为庆祝音流达成适配安卓 TV 的里程碑，特开启第二波早鸟优惠，活动时间为 2024-07-26 至 2024-08-08。

在此期间音流会员价格将降低 10 元，您可以 38 元的特惠价购入音流终身会员。

活动结束后，音流终身会员价格将调整至 58 元。

:::

<Tabs groupId="operating-systems">
<TabItem value="android" label="Android">
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.0/app-arm64-v8a-release.apk">ARM64 版本</Button>
    <span class="ml-md gray">MD5: 1cddbc720c19dde02d9d50d9a2106c35</span>
</div>
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.0/app-armeabi-v7a-release.apk">ARMV7 版本</Button>
    <span class="ml-md gray">MD5: 445eaba3783884ddb4207e99947ebd52</span>
</div>
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.0/app-x86_64-release.apk">x86 版本</Button>
    <span class="ml-md gray">MD5: b9bb45b1be24ca2efb9a1fcbcdc8b668</span>
</div>
<div class="mv-sm">
    <Button variant="contained" startIcon={<AndroidIcon />} href="https://oss.aqzscn.cn/stream-music/versions/1.3.0/app-release.apk">通用版本（体积较大）</Button>
    <span class="ml-md gray">MD5: 6ecf08468ec68879f50d78dc14dfd628</span>
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
