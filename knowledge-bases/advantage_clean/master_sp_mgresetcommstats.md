---
title: Master Sp Mgresetcommstats
slug: master_sp_mgresetcommstats
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_mgresetcommstats.htm
source: Advantage CHM
tags:
  - master
checksum: 3092b2a90e419db5f3fe773086f723e13b0d8adf
---

# Master Sp Mgresetcommstats

sp\_mgResetCommStats

sp\_mgResetCommStats

Advantage SQL Engine

| sp\_mgResetCommStats  Advantage SQL Engine |  |  |  |  |

Resets all Advantage Database Server communication statistics to zero.

Syntax

EXECUTE PROCEDURE sp\_mgResetCommStats()

Parameters

NONE

Remarks

This procedure resets all Advantage Database Server communication statistics to zero. This Advantage Management Procedure is useful when used in conjunction with sp\_mgGetCommStats to determine how often corrupted packets are being discovered.

Example

EXECUTE PROCEDURE sp\_mgResetCommStats();

See Also

[sp\_mgGetCommStats](master_sp_mggetcommstats.md)
