---
title: Error 5200 Ae Blurry Snapshot
slug: error_5200_ae_blurry_snapshot
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5200_ae_blurry_snapshot.htm
source: Advantage CHM
tags:
  - error
checksum: 4ee592ff8f45e58850e0f619a38bd1f9caae9498
---

# Error 5200 Ae Blurry Snapshot

5200 AE\_BLURRY\_SNAPSHOT

5200 AE\_BLURRY\_SNAPSHOT

Advantage Error Guide

| 5200 AE\_BLURRY\_SNAPSHOT  Advantage Error Guide |  |  |  |  |

Problem: The server was unable to stage a backup and get a logic snapshot. The backup continued, but with the chance that other worker threads could have changed data and made this a logically inconsistent backup.

Solution: To resolve this issue, run the backup again.

 

If the error persists, contact Advantage Technical Services. Configuration values exist that can be used to extend the period of time the server will wait before continuing.
