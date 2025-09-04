---
title: Master Effects Of Upgrading To Version 9 1
slug: master_effects_of_upgrading_to_version_9_1
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_effects_of_upgrading_to_version_9_1.htm
source: Advantage CHM
tags:
  - master
checksum: f904a604ac9d4ff99d075e11ad798d11a10da9ad
---

# Master Effects Of Upgrading To Version 9 1

Effects of Upgrading to Version 9.1

Effects of Upgrading to Version 9.1

Advantage Database Server

| Effects of Upgrading to Version 9.1  Advantage Database Server |  |  |  |  |

In addition to the [Effects of Upgrading to Version 9.0,](master_effects_of_upgrading_to_9_0.md) the following Advantage functionality changes may affect your applications if you upgrade to Advantage version 9.1.

Effects of Upgrading

General

In older versions of Advantage, proprietary locking did not open files using an exclusive mode, instead it used a "deny write" open mode. While this would allow non-Advantage applications access to the data files, it could also lead to index corruption. Non-Advantage applications could still lock bytes in the files causing Advantage read and write operations to fail. For this reason the default proprietary open mode was changed. If, however, you require other non-Advantage enabled applications (such as backup software or reporting software) to open files in a shared, read-only mode, a server option is available to revert to older behavior. For details, see the [Non-Exclusive Proprietary Locking](master_non_exclusive_proprietary_locking.md) configuration option.

Version 9.1 fixes an issue where differential backups were not correctly managing recycled memo pages, which could lead to memo corruption in a restored database image. It is recommended that anyone using differential backups re-initialize their backup image after installing this service update.
