---
sidebar_position: 4
---

# Custom APIs {#api}

Advanced users can customize API responses when music services lack required features.

## Authentication (Optional) {#auth}

| Configuration | Location       | Key             | Description |
| ------------- | -------------- | --------------- | ----------- |
| Authorization | Request Header | Authorization   |             |

## API List {#list}

### Get Lyrics {#lyrics}

**Method**: GET  

| Configuration          | Location     | Key       | Description                                                                                                          |
| ---------------------- | ------------ | --------- | -------------------------------------------------------------------------------------------------------------------- |
| Base URL               | URL          | -         | Example: `https://example.com/lyrics`                                                                               |
| Track Title            | URL Params   | `title`   | Final URL: `https://example.com/lyrics?title={title}`                                                               |
| Artist                 | URL Params   | `artist`  |                                                                                                                      |
| Album                  | URL Params   | `album`   |                                                                                                                      |
| File Path (Optional)   | URL Params   | `path`    | Available for Subsonic/Navidrome. May be empty for other protocols.                                                 |
| Duration (Optional)    | URL Params   | `duration`| In seconds. Supported since v1.1.3.                                                                                 |
| Offset (Optional)      | URL Params   | `offset`  | Start line index (0-based). Supported since v1.1.6 (fixed to 0).                                                    |
| Limit (Optional)       | URL Params   | `limit`   | Supported since v1.1.6 (fixed to 10).                                                                               |

**Response**  

Return lyrics content directly if found. Return empty or `404` if not found.  

For pagination (v1.1.6+), set `Content-Type: application/json` and return:  

```json
  [
    {
      "id": "<Unique ID for deduplication>",
      "title": "<May differ from query>",
      "artist": "<May differ from query>",
      "lyrics": "<Lyrics content>"
    },
    ...
  ]
```

### Confirm Lyrics {#confirm-lyrics}

Applicable to version 1.2.0 and above.

Triggered ​**after** a user manually clicks the ​**Save** button on the lyrics switching interface.

Request method: POST

| Configuration Item | Location | Key           | Description                                  |
| ------------------- | -------- | ------------- | -------------------------------------------- |
| Base URL            | URL      | -             | Example: `https://example.com/lyrics/confirm` |
| Content Type        | headers  | content-type  | `application/json`                           |

Request Body:
```json
{
    "path": "File path",
    "title": "Song title",
    "artist": "Artist",
    "album": "Album",
    "lyrics": "Lyrics content to confirm",
    "lyricsId": "Lyrics ID (may be null)"
}
```

Response Code: If the response code is not `20x`, display "Lyrics confirmation exception" to the user. No message is shown if there's no exception.

:::note
Starting from v1.3.1, adjusting the lyrics offset and clicking the checkmark button will also trigger the lyrics confirmation interface. In this case, the request data will ​**exclude** the `lyricsId` field.
:::

### Get Cover Art {#cover}

Request method: GET

| Configuration Item       | Location    | Key    | Description                                                                 |
| ------------------------- | ----------- | ------ | ---------------------------------------------------------------------------- |
| Base URL                  | URL         | -      | Example: `https://example.com/covers`                                       |
| Song title (optional)     | URL Params  | title  | Final URL: `https://example.com/covers?title=SongTitle`                      |
| Artist name               | URL Params  | artist |                                                                              |
| Album name (optional)     | URL Params  | album  |                                                                              |
| File path (optional)      | URL Params  | path   | Only exists when querying song cover art. Supported from v1.3.3             |

Through this interface, the app can attempt to obtain different types of cover art by controlling parameters:

- All three parameters: Get song cover art
- No song title: Get album cover art
- Only artist name: Get artist image

**Response Body**  
File stream.

### Song Details {#detail}

Applicable to version 1.2.4 and above. Used to redirect to the music service's song link in the browser.

| Configuration Item       | Location    | Key     | Description                                                                 |
| ------------------------- | ----------- | ------- | ---------------------------------------------------------------------------- |
| Base URL                  | URL         | -       | Example: `https://example.com/details`                                      |
| Song path                 | URL Params  | path    | Final URL: `https://example.com/details?path=SongPath`                       |
| Target                    | URL Params  | target  | Currently fixed as `detail`                                                 |

Example configuration:

![](https://oss2.aqzscn.cn/resource/blog/img/2024/891a6-5de6d34514b48759827b9e08e0236602.png)

**Path Replacement**  
Used when your music service is deployed via Docker: the detected path might differ from the actual music file path. By replacing the first matching string through ​**Path Replacement**, it can be converted to a path recognizable by the Docker service, i.e.:

```
// Actual path
/volume1/music/ff.flac
// Replaced path
/app/media/ff.flac
```

## Simple Service {#example}

### Configuring Nginx to Load LRC Files from Same Directory `@ZaneYork` {#nginx}

Directly configure the API address in the app as `your_server_address + /lyrics/`.

```conf title="default.conf"
    # Redirect requests for flac/mp3 resources to corresponding LRC files
    location ~* \.(flac|mp3)$ {
        rewrite ^/(.*)\.(flac|mp3)$ https://$host:8443/$1.lrc redirect;
    }
    location /lyrics/ {
      # Fix space characters being converted to plus signs in request paths
      if ($args ~ ^(?<first>.*)\+(?<second>.*)$) {
        rewrite ^(.*)$ "$1?$first%20$second?" last;
      }
      # %2Fmusic%2F represents your Navidrome song root directory (URL-encoded /)
      if ($query_string ~* "path=%2Fmusic%2F(.+)\.(mp3|flac)$") {
        set $argv1 $1;
        rewrite .* https://$host:8443/lyrics/$argv1.lrc? redirect;
      }

      # Nginx proxy logic for static resources in song directory omitted
   }
```

### Serving LRC Files with PHP (Same Filename) `@lingluos` {#php}

A PHP-based method to return LRC files on Linux systems. Requires the LRC file to have the exact same name as the audio file.

Assume `index.php` is placed in `/var/www/html/lyrics`, and LRC files are stored in `/var/www/html/lyrics/lrc`.

```php title="index.php"
<?php
if (isset($_GET['path'])) {
    $path = $_GET['path'];
    $lrcName = rawurlencode(substr($path, strrpos($path, '/') + 1, -5) . '.lrc');
    
    // Replace "your_domain" with your domain and path (default folder when accessing via Nginx port)
    $apiUrl = "http://your_domain/lyrics/lrc/{$lrcName}";
    
    // Print the API request URL (uncomment below and comment the header redirect 
    // if consistently getting 400 errors to verify LRC file accessibility)
    // echo $apiUrl;
    
    header("Location: $apiUrl");
    exit;
} else {
    echo '400 Missing file path';
}
?>
```

In theory, simply enter `http://your_domain/lyrics/` in the custom API lyrics interface to display the lyrics.  

As a side note, if the lyrics appear garbled, try converting the LRC file encoding to UTF-8.