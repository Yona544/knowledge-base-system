---
title: Error 5054 Ae Permission Denied
slug: error_5054_ae_permission_denied
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5054_ae_permission_denied.htm
source: Advantage CHM
tags:
  - error
checksum: 53d30d1c5121cce20b9106768a5b3d77b837035f
---

# Error 5054 Ae Permission Denied

5054 AE\_PERMISSION\_DENIED

5054 AE\_PERMISSION\_DENIED

Advantage Error Guide

| 5054 AE\_PERMISSION\_DENIED  Advantage Error Guide |  |  |  |  |

The command cannot be completed with the current user permissions. If using [Advantage Data Dictionary](master_advantage_data_dictionary.md), this error is returned if the current connected user was not granted the permission to performed the specific operation. For example, when creating a new user in the database, the user performing the operation must be granted the CREATE permission for the USER object type in the database. See AdsDDGrantPermission in the Advantage Client Engine Help documentation (ACE.hlp or ace.htm) for additional information.

Note If using the Advantage TDataSet Descendant TAdsQuery component, verify the RequestLive property is set to True.
