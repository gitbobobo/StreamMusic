---
sidebar_position: 2
---

# Detection and Deletion of Duplicate Songs {#detect}

As your music library grows, duplicate tracks inevitably appear, which can be frustrating for perfectionists who struggle to decide which version to keep.  

After connecting via **[Library Mode](../guides/sync_mode#library-mode)** and fully syncing server data, a **Duplicate Song Detection** entry will appear on the artist details page if duplicates exist.  

This feature allows you to view and compare duplicate versions of a song, then delete unwanted copies based on provided metadata.  

:::info Developer’s Note

Library Mode may perform poorly with large libraries. Use it only when necessary; stick to **Direct Mode** for daily use.  

:::

What if the [connected server lacks file deletion support](../services#comparison)? 

**Solution 1**: If Stream Music retrieves the actual file path, copy the deletion command from the page and execute it via SSH in another tool.  
*Note: This method involves cross-software/device operations and is not ideal.*  

**Solution 2**: Deploy a Docker-based server that supports file deletion. Switch to this server in Stream Music when detecting duplicates, sync data, and perform deletions.  
*(See [Focused Audio Management](./focus_specific_audio) for similar workflows.)*  