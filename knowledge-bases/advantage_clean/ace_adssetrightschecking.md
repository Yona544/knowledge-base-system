---
title: Ace Adssetrightschecking
slug: ace_adssetrightschecking
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssetrightschecking.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: dc6a6c285dc15dc76c2bd44ea05eb6127fb94412
---

# Ace Adssetrightschecking

ace\_AdsSetRightsChecking

AdsSetRightsChecking

Advantage Client Engine

| AdsSetRightsChecking  Advantage Client Engine |  |  |  |  |

Defines the rights checking behavior. This API can be used to enable the pre-version 10.0 behavior.

Syntax

| UNSIGNED32 | AdsSetRightsChecking ( UNSIGNED32 ulOptions ); |

Parameters

| ulOptions (I) | Specifies the rights checking behavior.    ADS\_RESPECT\_RIGHTS\_CHECKING (1) indicates that the rights checking options for table open and create operations are obeyed. This is the value to use for the old (pre-version 10.0) behavior.    ADS\_IGNORE\_RIGHTS\_CHECKING (2) is the default value. This defines the new version 10.0 behavior, which is to ignore the rights checking parameter in table opens and table creations. |

Remarks

The default behavior was changed in version 10.0 to [no longer perform rights checking](master_database_security.md) on the client. If your application depends on the old behavior, it is necessary to add a call to this API to re-enable the old behavior. To specify the old behavior, place a call to AdsRightsChecking(ADS\_RESPECT\_RIGHTS\_CHECKING ) in your application startup code. It is a global setting that remains in effect until the Advantage Client Engine DLL is unloaded or the application terminates.

See Also

[Database Security](master_database_security.md)

[Check Rights](master_check_rights.md)

[Ignore Rights](master_ignore_rights.md)
