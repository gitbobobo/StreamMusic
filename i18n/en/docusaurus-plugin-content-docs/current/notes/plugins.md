---
sidebar_position: 1
---

# Used Plugins

Without the support of open-source projects, StreamMusic wouldn't exist as it does today～

If any feature of StreamMusic has helped you, consider giving these projects a 🌟 or supporting them.

## UI {#ui}

### macos_ui

[macos_ui](https://github.com/macosui/macos_ui), like Flutter's built-in Material Widgets and Cupertino Widgets, implements component libraries following macOS design guidelines.

[Click here to view](https://macosui.github.io/macos_ui/#/) the live demo.

![](https://oss2.aqzscn.cn/resource/blog/img/2024/84187-8f40569512f26dedc256e709c73a4de9.png)

### fluent_ui

[fluent_ui](https://github.com/bdlukaa/fluent_ui) implements Windows Fluent Design components. Compared to `macos_ui`, its components are more feature-complete.

[Click here to view](https://bdlukaa.github.io/fluent_ui/) the live demo.

![](https://oss2.aqzscn.cn/resource/blog/img/2024/65e8d-fc810c37b1bd57ddc5161705e21c8343.png)

### pulldown_button

[pulldown_button](https://github.com/notDmDrl/pull_down_button) implements iOS-style pull-down menus with smooth animations. It would be perfect if it supported nested menus.

![](https://oss2.aqzscn.cn/resource/blog/img/2024/faae1-9ad0cf3582cd7ff590b3e02645f19bc7.png)

## Platform Features {#platform}

### macos_window_utils

[macos_window_utils](https://github.com/macosui/macos_window_utils.dart), another creation by the `macos_ui` author, controls window properties like blur effect and title bar visibility. Best used with macos_ui.

### flutter_acrylic

[flutter_acrylic](https://github.com/alexmercerind/flutter_acrylic) enables window blur/transparency effects on macOS/Windows/Linux. On macOS, it depends on `macos_window_utils`, so no need to include both.

### window_manager

[window_manager](https://pub.dev/packages/window_manager) controls window properties on desktop platforms.

### tray_manager

[tray_manager](https://pub.dev/packages/tray_manager) customizes system tray behaviors.

### windows_taskbar

[windows_taskbar](https://pub.dev/packages/windows_taskbar) adds preview buttons and progress bars to Windows taskbar icons - particularly useful for music players.

### flutter_carplay

[flutter_carplay](https://pub.dev/packages/flutter_carplay) enables CarPlay support for iOS (minimum iOS 14).  

The original author hasn't updated it recently - consider using community forks.  
A current challenge is launching the Flutter engine when CarPlay connects while ensuring smooth app switching between CarPlay and phone.

### flutter_rust_bridge

As the name suggests, [flutter_rust_bridge](https://cjycode.com/flutter_rust_bridge/quickstart) bridges Flutter and Rust by generating glue code. Flutter apps gain access to Rust's rich ecosystem, while Rust apps leverage Flutter's cross-platform UI.

I've followed this project for years but hesitated to adopt it due to my Rust inexperience. After optimizing Windows SMTC features using [this guide](https://juejin.cn/post/7363556508603432972), I've gained [some insights](./adaptive/smtc) and feel ready to migrate.

The core workflow when using Rust plugins involves two steps:

```rust title="image.rs"
// Define struct
pub struct RsImage {}
// Implement methods
impl RsImage {
  pub fn blur(img_path: String) -> Result<Vec<u8>, String> {
    // Use Rust crates to implement features...
  }
}
```
For a Rust Newbie, Understanding ownership concepts is essential. Lifetime issues might arise, but my current principle is to resolve compiler errors without explicit lifetime annotations whenever possible. As a simple API caller, I haven't encountered situations requiring manual lifetime tagging yet.

Compared to other languages, Rust does feel awkward initially - error handling patterns, optional unwrapping, ownership borrowing etc. But most issues can be solved with GPT's help. The benefits of accessing Rust's cross-platform ecosystem make these growing pains worthwhile 😄

## Networking {#network}

### dio

[dio](https://pub.dev/packages/dio) is a powerful HTTP client featuring interceptors, request cancellation, and custom adapters. Community plugins further simplify networking tasks.

Dart's native HTTP client only handles standard requests properly. Non-standard implementations can fail, making it inferior to platform-native networking.

While dio offers [native_dio_adapter](https://github.com/cfug/dio/tree/main/plugins/native_dio_adapter) for native platform requests, it only works on Android/iOS - insufficient for StreamMusic's multi-platform needs.

### rhttp(rust)

[rhttp](https://github.com/Tienisto/rhttp) leverages Rust's renowned `reqwest` for requests, offering better compatibility than Dart's HTTP stack.

StreamMusic v1.3.2 uses rhttp for image fetching and song caching with improved compatibility and system proxy support. Future plans include migrating all networking to rhttp if stability holds.

### rupnp(rust)

[rupnp](https://github.com/jakobhellermann/rupnp) (Rust UPnP) replaced Dart's [upnp2](https://github.com/daniel-naegele/upnp.dart) due to mysterious Windows DLNA device discovery failures with the Dart version.

### shelf

[shelf](https://pub.dev/packages/shelf) creates local HTTP servers, with [shelf_proxy](https://pub.dev/packages/shelf_proxy) simplifying proxy setups. Note: iOS suspends local servers when app enters background - implement detection and restart mechanisms.

### connectivity_plus

[connectivity_plus](https://pub.dev/packages/connectivity_plus) monitors network status changes.

### network_info_plus

[network_info_plus](https://pub.dev/packages/network_info_plus) retrieves Wi-Fi details like IP addresses.

### url_launcher

[url_launcher](https://pub.dev/packages/url_launcher) opens URLs in default browsers.

## Audio {#audio}

### media_kit

[media_kit](https://github.com/media-kit/media-kit) uses MPV under the hood, achieving unparalleled [format compatibility](https://github.com/media-kit/media-kit?tab=readme-ov-file#supported-formats) for audio/video playback - a key differentiator from other Flutter players.

<details>
  <summary>Supported Formats (Click to Expand)</summary>

- 3dostr          3DO STR
- 4xm             4X Technologies
- aa              Audible AA format files
- aac             raw ADTS AAC (Advanced Audio Coding)
- aax             CRI AAX
- ac3             raw AC-3
- ace             tri-Ace Audio Container
- acm             Interplay ACM
- act             ACT Voice file format
- adf             Artworx Data Format
- adp             ADP
- ads             Sony PS2 ADS
- adx             CRI ADX
- aea             MD STUDIO audio
- afc             AFC
- aiff            Audio IFF
- aix             CRI AIX
- alaw            PCM A-law
- alias_pix       Alias/Wavefront PIX image
- alp             LEGO Racers ALP
- amr             3GPP AMR
- amrnb           raw AMR-NB
- amrwb           raw AMR-WB
- anm             Deluxe Paint Animation
- apac            raw APAC
- apc             CRYO APC
- ape             Monkey's Audio
- apm             Ubisoft Rayman 2 APM
- apng            Animated Portable Network Graphics
- aptx            raw aptX
- aptx_hd         raw aptX HD
- aqtitle         AQTitle subtitles
- argo_asf        Argonaut Games ASF
- argo_brp        Argonaut Games BRP
- argo_cvg        Argonaut Games CVG
- asf             ASF (Advanced / Active Streaming Format)
- asf_o           ASF (Advanced / Active Streaming Format)
- ass             SSA (SubStation Alpha) subtitle
- ast             AST (Audio Stream)
- au              Sun AU
- av1             AV1 Annex B
- avi             AVI (Audio Video Interleaved)
- avr             AVR (Audio Visual Research)
- avs             Argonaut Games Creature Shock
- avs2            raw AVS2-P2/IEEE1857.4
- avs3            raw AVS3-P2/IEEE1857.10
- bethsoftvid     Bethesda Softworks VID
- bfi             Brute Force & Ignorance
- bfstm           BFSTM (Binary Cafe Stream)
- bin             Binary text
- bink            Bink
- binka           Bink Audio
- bit             G.729 BIT file format
- bitpacked       Bitpacked
- bmp_pipe        piped bmp sequence
- bmv             Discworld II BMV
- boa             Black Ops Audio
- bonk            raw Bonk
- brender_pix     BRender PIX image
- brstm           BRSTM (Binary Revolution Stream)
- c93             Interplay C93
- caf             Apple CAF (Core Audio Format)
- cavsvideo       raw Chinese AVS (Audio Video Standard)
- cdg             CD Graphics
- cdxl            Commodore CDXL video
- cine            Phantom Cine
- codec2          codec2 .c2 demuxer
- codec2raw       raw codec2 demuxer
- concat          Virtual concatenation script
- cri_pipe        piped cri sequence
- dash            Dynamic Adaptive Streaming over HTTP
- data            raw data
- daud            D-Cinema audio
- dcstr           Sega DC STR
- dds_pipe        piped dds sequence
- derf            Xilam DERF
- dfa             Chronomaster DFA
- dfpwm           raw DFPWM1a
- dhav            Video DAV
- dirac           raw Dirac
- dnxhd           raw DNxHD (SMPTE VC-3)
- dpx_pipe        piped dpx sequence
- dsf             DSD Stream File (DSF)
- dshow           DirectShow capture
- dsicin          Delphine Software International CIN
- dss             Digital Speech Standard (DSS)
- dts             raw DTS
- dtshd           raw DTS-HD
- dv              DV (Digital Video)
- dvbsub          raw dvbsub
- dvbtxt          dvbtxt
- dxa             DXA
- ea              Electronic Arts Multimedia
- ea_cdata        Electronic Arts cdata
- eac3            raw E-AC-3
- epaf            Ensoniq Paris Audio File
- exr_pipe        piped exr sequence
- f32be           PCM 32-bit floating-point big-endian
- f32le           PCM 32-bit floating-point little-endian
- f64be           PCM 64-bit floating-point big-endian
- f64le           PCM 64-bit floating-point little-endian
- ffmetadata      FFmpeg metadata in text
- film_cpk        Sega FILM / CPK
- filmstrip       Adobe Filmstrip
- fits            Flexible Image Transport System
- flac            raw FLAC
- flic            FLI/FLC/FLX animation
- flv             FLV (Flash Video)
- frm             Megalux Frame
- fsb             FMOD Sample Bank
- fwse            Capcom's MT Framework sound
- g722            raw G.722
- g723_1          G.723.1
- g726            raw big-endian G.726 ("left aligned")
- g726le          raw little-endian G.726 ("right aligned")
- g729            G.729 raw format demuxer
- gdigrab         GDI API Windows frame grabber
- gdv             Gremlin Digital Video
- gem_pipe        piped gem sequence
- genh            GENeric Header
- gif             CompuServe Graphics Interchange Format (GIF)
- gif_pipe        piped gif sequence
- gsm             raw GSM
- gxf             GXF (General eXchange Format)
- h261            raw H.261
- h263            raw H.263
- h264            raw H.264 video
- hca             CRI HCA
- hcom            Macintosh HCOM
- hdr_pipe        piped hdr sequence
- hevc            raw HEVC video
- hls             Apple HTTP Live Streaming
- hnm             Cryo HNM v4
- ico             Microsoft Windows ICO
- idcin           id Cinematic
- idf             iCE Draw File
- iff             IFF (Interchange File Format)
- ifv             IFV CCTV DVR
- ilbc            iLBC storage
- image2          image2 sequence
- image2pipe      piped image2 sequence
- imf             IMF (Interoperable Master Format)
- ingenient       raw Ingenient MJPEG
- ipmovie         Interplay MVE
- ipu             raw IPU Video
- ircam           Berkeley/IRCAM/CARL Sound Format
- iss             Funcom ISS
- iv8             IndigoVision 8000 video
- ivf             On2 IVF
- ivr             IVR (Internet Video Recording)
- j2k_pipe        piped j2k sequence
- jacosub         JACOsub subtitle format
- jpeg_pipe       piped jpeg sequence
- jpegls_pipe     piped jpegls sequence
- jpegxl_pipe     piped jpegxl sequence
- jv              Bitmap Brothers JV
- kux             KUX (YouKu)
- kvag            Simon & Schuster Interactive VAG
- laf             LAF (Limitless Audio Format)
- lavfi           Libavfilter virtual input device
- live_flv        live RTMP FLV (Flash Video)
- lmlm4           raw lmlm4
- loas            LOAS AudioSyncStream
- lrc             LRC lyrics
- luodat          Video CCTV DAT
- lvf             LVF
- lxf             VR native stream (LXF)
- m4v             raw MPEG-4 video
- matroska,webm   Matroska / WebM
- mca             MCA Audio Format
- mcc             MacCaption
- mgsts           Metal Gear Solid: The Twin Snakes
- microdvd        MicroDVD subtitle format
- mjpeg           raw MJPEG video
- mjpeg_2000      raw MJPEG 2000 video
- mlp             raw MLP
- mlv             Magic Lantern Video (MLV)
- mm              American Laser Games MM
- mmf             Yamaha SMAF
- mods            MobiClip MODS
- moflex          MobiClip MOFLEX
- mov,mp4,m4a,3gp,3g2,mj2 QuickTime / MOV
- mp3             MP2/3 (MPEG audio layer 2/3)
- mpc             Musepack
- mpc8            Musepack SV8
- mpeg            MPEG-PS (MPEG-2 Program Stream)
- mpegts          MPEG-TS (MPEG-2 Transport Stream)
- mpegtsraw       raw MPEG-TS (MPEG-2 Transport Stream)
- mpegvideo       raw MPEG video
- mpjpeg          MIME multipart JPEG
- mpl2            MPL2 subtitles
- mpsub           MPlayer subtitles
- msf             Sony PS3 MSF
- msnwctcp        MSN TCP Webcam stream
- msp             Microsoft Paint (MSP))
- mtaf            Konami PS2 MTAF
- mtv             MTV
- mulaw           PCM mu-law
- musx            Eurocom MUSX
- mv              Silicon Graphics Movie
- mvi             Motion Pixels MVI
- mxf             MXF (Material eXchange Format)
- mxg             MxPEG clip
- nc              NC camera feed
- nistsphere      NIST SPeech HEader REsources
- nsp             Computerized Speech Lab NSP
- nsv             Nullsoft Streaming Video
- nut             NUT
- nuv             NuppelVideo
- obu             AV1 low overhead OBU
- ogg             Ogg
- oma             Sony OpenMG audio
- paf             Amazing Studio Packed Animation File
- pam_pipe        piped pam sequence
- pbm_pipe        piped pbm sequence
- pcx_pipe        piped pcx sequence
- pfm_pipe        piped pfm sequence
- pgm_pipe        piped pgm sequence
- pgmyuv_pipe     piped pgmyuv sequence
- pgx_pipe        piped pgx sequence
- phm_pipe        piped phm sequence
- photocd_pipe    piped photocd sequence
- pictor_pipe     piped pictor sequence
- pjs             PJS (Phoenix Japanimation Society) subtitles
- pmp             Playstation Portable PMP
- png_pipe        piped png sequence
- pp_bnk          Pro Pinball Series Soundbank
- ppm_pipe        piped ppm sequence
- psd_pipe        piped psd sequence
- psxstr          Sony Playstation STR
- pva             TechnoTrend PVA
- pvf             PVF (Portable Voice Format)
- qcp             QCP
- qdraw_pipe      piped qdraw sequence
- qoi_pipe        piped qoi sequence
- r3d             REDCODE R3D
- rawvideo        raw video
- realtext        RealText subtitle format
- redspark        RedSpark
- rka             RKA (RK Audio)
- rl2             RL2
- rm              RealMedia
- roq             id RoQ
- rpl             RPL / ARMovie
- rsd             GameCube RSD
- rso             Lego Mindstorms RSO
- rtp             RTP input
- rtsp            RTSP input
- s16be           PCM signed 16-bit big-endian
- s16le           PCM signed 16-bit little-endian
- s24be           PCM signed 24-bit big-endian
- s24le           PCM signed 24-bit little-endian
- s32be           PCM signed 32-bit big-endian
- s32le           PCM signed 32-bit little-endian
- s337m           SMPTE 337M
- s8              PCM signed 8-bit
- sami            SAMI subtitle format
- sap             SAP input
- sbc             raw SBC (low-complexity subband codec)
- sbg             SBaGen binaural beats script
- scc             Scenarist Closed Captions
- scd             Square Enix SCD
- sdns            Xbox SDNS
- sdp             SDP
- sdr2            SDR2
- sds             MIDI Sample Dump Standard
- sdx             Sample Dump eXchange
- ser             SER (Simple uncompressed video format for astronomical capturing)
- sga             Digital Pictures SGA
- sgi_pipe        piped sgi sequence
- shn             raw Shorten
- siff            Beam Software SIFF
- simbiosis_imx   Simbiosis Interactive IMX
- sln             Asterisk raw pcm
- smjpeg          Loki SDL MJPEG
- smk             Smacker
- smush           LucasArts Smush
- sol             Sierra SOL
- sox             SoX native
- spdif           IEC 61937 (compressed data in S/PDIF)
- srt             SubRip subtitle
- stl             Spruce subtitle format
- subviewer       SubViewer subtitle format
- subviewer1      SubViewer v1 subtitle format
- sunrast_pipe    piped sunrast sequence
- sup             raw HDMV Presentation Graphic Stream subtitles
- svag            Konami PS2 SVAG
- svg_pipe        piped svg sequence
- svs             Square SVS
- swf             SWF (ShockWave Flash)
- tak             raw TAK
- tedcaptions     TED Talks captions
- thp             THP
- tiertexseq      Tiertex Limited SEQ
- tiff_pipe       piped tiff sequence
- tmv             8088flex TMV
- truehd          raw TrueHD
- tta             TTA (True Audio)
- tty             Tele-typewriter
- txd             Renderware TeXture Dictionary
- ty              TiVo TY Stream
- u16be           PCM unsigned 16-bit big-endian
- u16le           PCM unsigned 16-bit little-endian
- u24be           PCM unsigned 24-bit big-endian
- u24le           PCM unsigned 24-bit little-endian
- u32be           PCM unsigned 32-bit big-endian
- u32le           PCM unsigned 32-bit little-endian
- u8              PCM unsigned 8-bit
- v210            Uncompressed 4:2:2 10-bit
- v210x           Uncompressed 4:2:2 10-bit
- vag             Sony PS2 VAG
- vbn_pipe        piped vbn sequence
- vc1             raw VC-1
- vc1test         VC-1 test bitstream
- vfwcap          VfW video capture
- vidc            PCM Archimedes VIDC
- vividas         Vividas VIV
- vivo            Vivo
- vmd             Sierra VMD
- vobsub          VobSub subtitle format
- voc             Creative Voice
- vpk             Sony PS2 VPK
- vplayer         VPlayer subtitles
- vqf             Nippon Telegraph and Telephone Corporation (NTT) TwinVQ
- w64             Sony Wave64
- wady            Marble WADY
- wav             WAV / WAVE (Waveform Audio)
- wavarc          Waveform Archiver
- wc3movie        Wing Commander III movie
- webm_dash_manifest WebM DASH Manifest
- webp_pipe       piped webp sequence
- webvtt          WebVTT subtitle
- wsaud           Westwood Studios audio
- wsd             Wideband Single-bit Data (WSD)
- wsvqa           Westwood Studios VQA
- wtv             Windows Television (WTV)
- wv              WavPack
- wve             Psion 3 audio
- xa              Maxis XA
- xbin            eXtended BINary text (XBIN)
- xbm_pipe        piped xbm sequence
- xmd             Konami XMD
- xmv             Microsoft XMV
- xpm_pipe        piped xpm sequence
- xvag            Sony PS3 XVAG
- xwd_pipe        piped xwd sequence
- xwma            Microsoft xWMA
- yop             Psygnosis YOP
- yuv4mpegpipe    YUV4MPEG pipe

</details>

I can't contain my enthusiasm for this plugin. After struggling to find a worthy replacement for `just_audio`, media_kit has effortlessly resolved numerous playback issues I previously encountered.

So folks, now that you've read this, go show some love and [give media_kit a 🌟](https://github.com/media-kit/media-kit)!

:::note Dev Tip

Using default configurations may cause crashes when playing high-bitrate files on HarmonyOS. Apply this workaround:

```dart
NativePlayer get nativePlayer => player.platform as NativePlayer;

if (Platform.isAndroid) {
  // Fix crash on HarmonyOS when playing high-bitrate files
  await nativePlayer.setProperty("ao", "audiotrack,opensles,");
}
```

此处代码参考了 [spotube](https://github.com/KRTirtho/spotube) 项目的 [custom_player.dart](https://github.com/KRTirtho/spotube/blob/cb95663412fcc9a829c5657e0160132f13fb0649/lib/services/audio_player/custom_player.dart#L68)。

:::

### audio_service

[audio_service](https://github.com/ryanheise/audio_service) handles system music notifications, media controls interaction, and background playback persistence.

Currently supports Android, iOS, macOS. For Windows support, see my [modified version](https://github.com/gitbobobo/audio_service) which:
1. Adds Android status bar lyrics support
2. Implements Windows media notifications via [smtc_windows](https://github.com/KRTirtho/smtc_windows)

### lofty(rust)

[lofty](https://github.com/Serial-ATA/lofty-rs) - Rust library for reading audio file metadata tags. Supported formats:

| File Format    | Metadata Format(s)                 |
|----------------|------------------------------------|
| AAC (ADTS)     | `ID3v2`, `ID3v1`                  |
| Ape            | `APE`, `ID3v2`\*, `ID3v1`         |
| AIFF           | `ID3v2`, `Text Chunks`            |
| FLAC           | `Vorbis Comments`, `ID3v2`\*       |
| MP3            | `ID3v2`, `ID3v1`, `APE`           |
| MP4            | `iTunes-style ilst`               |
| MPC            | `APE`, `ID3v2`\*, `ID3v1`\*       |                        
| Opus           | `Vorbis Comments`                  |
| Ogg Vorbis     | `Vorbis Comments`                  |
| Speex          | `Vorbis Comments`                  |
| WAV            | `ID3v2`, `RIFF INFO`               |
| WavPack        | `APE`, `ID3v1`                    |

\* Read-only due to lack of official spec support

## Flutter Community {#community}

### Flutter Candies

[Flutter Candies](https://github.com/fluttercandies) - A thriving plugin ecosystem that fills gaps in official components' functionality. The maintainer actively shares insights on [Juejin](https://juejin.cn/user/254742428916408/posts) (I'm a silent follower 😉).

StreamMusic uses these Flutter Candies plugins:

- [extended_nested_scroll_view](https://github.com/fluttercandies/extended_nested_scroll_view)  
  Solves transparent header scrolling issues and syncs list scrolling in song list/artist detail pages.

- [loading_more_list](https://github.com/fluttercandies/loading_more_list)  
  Implements "load more" functionality without ScrollController.

- [scrollview_observer](https://github.com/fluttercandies/flutter_scrollview_observer)  
  Powers dynamic grid/list view switching with AZ jumping.

- [flutter_smart_dialog](https://github.com/fluttercandies/flutter_smart_dialog)  
  Context-free global dialogs/toasts.