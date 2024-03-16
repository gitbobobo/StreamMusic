---
sidebar_position: 3
---

# 自定义 API 文档

某些情况下，音乐服务提供的接口可能无法返回我们需要的信息，故提供自定义 API，高级用户可以自定义返回内容。

## 鉴权（可选）

| 配置项   | 位置           | 键             | 说明 |
| -------- | -------------- | -------------- | ---- |
| 授权信息 | Request Header | Authorization |      |

## 接口列表

### 获取歌词

请求方式：GET

| 配置项           | 位置       | 键       | 说明                                                                                                          |
| ---------------- | ---------- | -------- | ------------------------------------------------------------------------------------------------------------- |
| 基础地址         | URL        | -        | 示例：https://example.com/lyrics                                                                              |
| 歌曲标题         | URL Params | title    | 最终组装地址：https://example.com/lyrics?title=歌曲标题                                                       |
| 歌手名           | URL Params | artist   |                                                                                                               |
| 专辑名           | URL Params | album    |                                                                                                               |
| 文件路径（可选） | URL Params | path     | 目前 Subsonic 和 Navidrome 都可以获取到文件路径，但不排除之后支持的协议中无法取得的情况，因此这个值可能为空。 |
| 时长（可选）     | URL Params | duration | 单位：秒，1.1.3 版本以上支持。                                                                                |
| 偏移（可选）     | URL Params | offset   | 起始查询行，从 0 开始。1.1.6 版本以上支持，目前固定为 0 。                                                    |
| 每页数量（可选）                 |    URL Params        |    limit      |   1.1.6 版本以上支持，目前固定为 10 。                                                                                                            |

**响应体**

如果有歌词，直接返回歌词内容，没有时返回空，或设置响应状态码为 404.

从 1.1.6 版本开始支持分页获取歌词，在响应类型 `content-type` 设置为 `application/json` 后，将尝试把响应内容解析为 json 列表，结构如下：

```json
[
    {
        "id": "<歌词id，用于与其他歌词去重>",
        "title": "<标题，可能与查询的标题不一致>",
        "artist": "<歌手，可能与查询的歌手不一致>",
        "lyrics": "<歌词文件内容>"
    },
    ...
]
```

### 确认歌词

适用于 1.2.0 及以上版本。

在用户手动点击歌词切换界面的**保存**按钮后触发。

请求方式：POST

| 配置项   | 位置    | 键           | 说明                                     |
| -------- | ------- | ------------ | ---------------------------------------- |
| 基础地址 | URL     | -            | 示例：https://example.com/lyrics/confirm |
| 内容类型 | headers | content-type | application/json                         |

请求体：

```json
{
    "path": "文件路径",
    "title": "歌曲标题",
    "artist": "歌手",
    "album": "专辑",
    "lyrics": "待确认歌词内容",
    "lyricsId": "歌词id，可能为null"
}
```

响应码：若响应码不是`20x`，则提示用户「歌词确认异常」，没有异常则不提示信息。

### 获取封面

请求方式：GET

| 配置项           | 位置       | 键     | 说明                                                    |
| ---------------- | ---------- | ------ | ------------------------------------------------------- |
| 基础地址         | URL        | -      | 示例：https://example.com/covers                        |
| 歌曲标题（可选） | URL Params | title  | 最终组装地址：https://example.com/covers?title=歌曲标题 |
| 歌手名           | URL Params | artist |                                                         |
| 专辑名（可选）   | URL Params | album  |                                                         |

通过此接口，音流可控制传递的参数尝试获取不同类型的封面：

- 三者都传：获取歌曲封面
- 不传歌曲标题：获取专辑封面
- 只传歌手名：获取歌手图片

**响应体**

文件流。


### 歌曲详情

适用于 1.2.4 及以上版本，用于在浏览器中跳转到音乐服务对应的歌曲链接。

| 配置项           | 位置       | 键     | 说明                                                    |
| ---------------- | ---------- | ------ | ------------------------------------------------------- |
| 基础地址         | URL        | -      | 示例：https://example.com/details                        |
| 歌曲路径 | URL Params | title  | 最终组装地址：https://example.com/details?path=歌曲路径 |
| 目标           | URL Params | target |  目前固定为`detail`  |


示例配置：

![](https://oss.aqzscn.cn/resource/blog/img/2024/891a6-5de6d34514b48759827b9e08e0236602.png)

路径替换的作用是当您的音乐服务在 Docker 部署时，识别到的路径可能和音乐文件实际路径是不同的，通过**路径替换**可以将第一个匹配到的字符串替换为 docker 服务可以识别的，即：

```
// 实际路径
/volume1/music/ff.flac
// 替换后路径
/app/media/ff.flac
```

## 简易服务

### 搭配 Nginx 加载同目录下 Lrc 文件 `@ZaneYork`

APP 内直接配置 API 地址为 `你的服务器地址 + /lyrics/` 即可。

```conf title="default.conf"
    # 对于flac和mp3格式的资源请求，直接重定向到对应的lrc
    location ~* \.(flac|mp3)$ {
        rewrite ^/(.*)\.(flac|mp3)$ https://$host:8443/$1.lrc redirect;
    }
    location /lyrics/ {
      # 解决请求路径中空格变成加号的问题
      if ($args ~ ^(?&lt;first&gt;.*)\+(?&lt;second&gt;.*)$) {
        rewrite ^(.*)$ &quot;$1?$first%20$second?&quot; last;
      }
      # 此处的 %2Fmusic%2F 为你的Navidrome的歌曲根目录%2F为 / 的urlencode形式
      if ($query_string ~* &quot;path=%2Fmusic%2F(.+)\.(mp3|flac)$&quot;) {
        set $argv1 $1;
        rewrite .* https://$host:8443/lyrics/$argv1.lrc? redirect;
      }

      #  nginx 代理歌曲目录下静态资源逻辑省略
   }
```

### 搭配 php 返回同名 Lrc 文件 `@lingluos`

在Linux系统上使用php方法返回lrc文件 要求lrc文件和歌曲文件名称完全相同

假设你的这个index.php放在 `/var/www/html/lyrics` 文件夹下，lrc文件放在 `/var/www/html/lyrics/lrc` 中

```php title="index.php"
<?php
if (isset($_GET[&#39;path&#39;])) {
    $path = $_GET[&#39;path&#39;];
    $lrcName = rawurlencode(substr($path, strrpos($path, &#39;/&#39;) + 1, -5) . &#39;.lrc&#39;);

    // 这里域名后面填你端口进nginx时默认到的文件夹 我这里是/var/www/html 故只需要填写/lyrics/lrc
    $apiUrl = &quot;http://这里填写域名/lyrics/lrc/{$lrcName}&quot;;

    // 打印api请求的URL  如果一直返回400可以把下面的header跳转给注释掉并去掉echo $apiUrl;的注释
    // 来看看$apiUrl这个链接是否能直接访问lrc文件
    // echo $apiUrl;

    header(&quot;Location: $apiUrl&quot;);
    exit;
} else {
    echo &#39;400 缺少文件路径&#39;;
}
?>
```

那么理论上你只要在自定义api歌词接口中输入 `http://域名/lyrics/` 就可以显示出歌词了

顺路提一嘴 如果发现歌词显示出来是乱码 可以尝试把lrc文件的编码改成utf-8