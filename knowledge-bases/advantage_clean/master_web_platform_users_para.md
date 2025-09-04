---
title: Master Web Platform Users Para
slug: master_web_platform_users_para
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_web_platform_users_para.htm
source: Advantage CHM
tags:
  - master
checksum: 93224774a7348cf6f4040b319e3f4474b062b55a
---

# Master Web Platform Users Para

Web\_Platform\_Users Configuration Value

Web\_Platform\_Users

Advantage Database Server

| Web\_Platform\_Users  Advantage Database Server |  |  |  |  |

Default = 0, Range 0 - Purchased User Count

The WEB\_PLATFORM\_USERS configuration parameter can be used to specify the maximum number of concurrently active users allowed for use by the Advantage Web Platform. See [Web Platform Users](master_web_platform_users.md) for more information. The value is should be specified as a numeric (REG\_DWORD in the Windows registry). If the value is specified equal to the user count option (the purchased number of users), then it means all Advantage users could be consumed by the Advantage Web Platform.
