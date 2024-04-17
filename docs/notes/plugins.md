---
sidebar_position: 1
---

# 插件分享

如果没有开源项目的支持，就不会有现在的音流～

如果您觉得音流的某个功能帮到了您，可以考虑为这些项目点亮 🌟 或提供支持。

## 界面

### macos_ui

[macos_ui](https://github.com/macosui/macos_ui) 与 Flutter 自带的 Material Widgets 和 Cupertino Widgets 一样，都是为了实现在对应平台设计语言的组件库。

[点此查看](https://macosui.github.io/macos_ui/#/)在线演示。

![](https://oss.aqzscn.cn/resource/blog/img/2024/84187-8f40569512f26dedc256e709c73a4de9.png)

### fluent_ui

[fluent_ui](https://github.com/bdlukaa/fluent_ui) 是用于实现 Windows 平台 fluent 设计语言的组件库，这里面的组件相较于 `macos_ui` 里的组件功能更加完善。

[点此查看](https://bdlukaa.github.io/fluent_ui/)在线演示。

![](https://oss.aqzscn.cn/resource/blog/img/2024/65e8d-fc810c37b1bd57ddc5161705e21c8343.png)

### pulldown_button

[pulldown_button](https://github.com/notDmDrl/pull_down_button) 实现了类似 iOS 下拉菜单的效果，动画效果十分丝滑，如果能支持二级菜单就更完美了。

![](https://oss.aqzscn.cn/resource/blog/img/2024/faae1-9ad0cf3582cd7ff590b3e02645f19bc7.png)

## 平台相关

### macos_window_utils

[macos_window_utils](https://github.com/macosui/macos_window_utils.dart) 是 `macos_ui` 作者的另一作品，主要功能是控制窗口的各种属性，如是否模糊、是否隐藏标题栏等，配合 macos_ui 食用更佳。

### flutter_acrylic

[flutter_acrylic](https://github.com/alexmercerind/flutter_acrylic) 可以在 macOS、Windows、Linux 平台实现窗口模糊/透明效果，其中 macOS 依赖了 `macos_window_utils` 插件，因此如果使用此插件就无需再引入 `macos_window_utils` 了。

## 音频

### media_kit

[media_kit](https://github.com/media-kit/media-kit) 是一个播放插件，可以用来播放视频或音频。与 flutter 平台其他播放插件不同的是，它的底层使用的是鼎鼎有名的 MPV，因此对[媒体格式](https://github.com/media-kit/media-kit?tab=readme-ov-file#supported-formats)的兼容性达到了十分恐怖的地步。

<details>
  <summary>点击查看支持格式</summary>

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

我很难抑制我对它的喜爱之情，因为之前一直在苦苦寻找一款能代替 `just_audio` 的播放插件而不得。而现在在 media_kit 的帮助下，以前遇到的很多播放问题都已迎刃而解。

所以大家，都看到这里了，快去给 [media_kit](https://github.com/media-kit/media-kit) 点亮 🌟 吧～

### audio_service

[audio_service](https://github.com/ryanheise/audio_service) 用于通知系统当前正在播放的音乐并与系统控件交互，还可以用来保持音乐后台播放。

目前支持 Android、iOS、macOS，对 Windows 的支持可以参见我的[魔改版本](https://github.com/gitbobobo/audio_service)，一是加入了安卓状态栏歌词的支持，二是通过 [smtc_windows](https://github.com/KRTirtho/smtc_windows) 插件实现了对 Windows 的媒体通知的支持。

### audio_metadata_reader

[audio_metadata_reader](https://github.com/ClementBeal/audio_metadata_reader) 是一款用于读取音乐文件标签信息的插件，目前支持以下格式：

| File Format | Metadata Format(s)      | Read |
| ----------- | ----------------------- | ---- |
| MP3         | `ID3v2` `ID3v3` `ID3v4` | ✅   |
| MP4         | `iTunes-style ilst`     | ✅   |
| FLAC        | `Vorbis Comments`       | ✅   |
| OGG         | `Vorbis Comments`       | ✅   |
| Opus        | `Vorbis Comments`       | ✅   |

### taggy

[taggy](https://github.com/DMouayad/taggy) 同样也是一款读取/写入音乐文件标签信息的插件，但底层连接的是 [lofty](https://github.com/Serial-ATA/lofty-rs/)，拥有更为广泛的格式支持：

| File Format | Metadata Format(s)           |
|-------------|------------------------------|
| AAC (ADTS)  | `ID3v2`, `ID3v1`             |
| Ape         | `APE`, `ID3v2`\*, `ID3v1`    |
| AIFF        | `ID3v2`, `Text Chunks`       |
| FLAC        | `Vorbis Comments`, `ID3v2`\* |
| MP3         | `ID3v2`, `ID3v1`, `APE`      |
| MP4         | `iTunes-style ilst`          |
| MPC         | `APE`, `ID3v2`\*, `ID3v1`\*  |                        
| Opus        | `Vorbis Comments`            |
| Ogg Vorbis  | `Vorbis Comments`            |
| Speex       | `Vorbis Comments`            |
| WAV         | `ID3v2`, `RIFF INFO`         |
| WavPack     | `APE`, `ID3v1`               |

\* The tag will be **read only**, due to lack of official support

:::info

既然 taggy 这么强大，我为什么还要先介绍 audio_metadata_reader 呢？

因为我只能在安卓平台成功运行起 taggy😭，其他平台不知是我使用方法问题还是作者并未测试，我这里是无法运行的。

因此目前音流会在安卓平台使用 taggy 解析音乐标签，而在其他平台使用 audio_metadata_reader 解析音乐标签。

:::