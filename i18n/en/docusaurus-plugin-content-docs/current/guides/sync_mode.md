---
sidebar_position: 2
---

# Sync Modes {#sync}

## Library Mode {#library-mode}

In **Library Mode**, Stream Music fully synchronizes server-side song lists, album lists, and artist lists to the local device, enabling access to complete music library data.

This mode allows Stream Music to implement features not supported by the server, such as folder views, playlist imports, and advanced filtering.  

**However**, if your music library is large, the initial sync process may take significant time.

### Automatic Sync {#auto}

On app startup, Stream Music detects if the server has more songs than the local copy and performs an **incremental sync** for missing data.  

:::warning

Incremental sync relies on querying songs by their creation time in reverse order. If songs are deleted or modified on the server, manually trigger a full sync via the sync button.

:::

After login, the app initializes the player to restore the last playback session. If you see a "**Player initializing**" message, wait briefly.

### Manual Sync {#manual}

If automatic sync fails, click the **"Sync Now"** button in the music library to force a full update.  

:::info

Manual sync is a full update. If interrupted, incremental sync resumes on the next launch.

:::

## Direct Mode {#direct}

In **Direct Mode**, Stream Music fetches data directly from the server without local synchronization. This improves initial app performance for large libraries.  

**Limitations** due to server API dependencies:  

- **Daily Mix** may include long audio tracks without duration filtering.  
- No duplicate song detection.  
- Folder views (for Subsonic/Navidrome/Jellyfin) only display locally cached data (manually queried folders).  
- Some sorting/filtering features are unavailable.  

:::info Work in Progress...

As someone with a growing music library, I find Direct Mode effective despite minor feature gaps. **Future optimizations will focus on Direct Mode**.  

However, functionality depends on server APIs. A long-term vision is to develop a dedicated Stream Music server for enhanced compatibility.  

:::