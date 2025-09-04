---
title: Ace Adssetdefault
slug: ace_adssetdefault
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssetdefault.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 5d91bbdd4257bf0cac74be5527bab41f30412628
---

# Ace Adssetdefault

AdsSetDefault

AdsSetDefault

Advantage Client Engine

| AdsSetDefault  Advantage Client Engine |  |  |  |  |

Sets the default search directory for opening and creating tables

Syntax

| UNSIGNED32 | AdsSetDefault (UNSIGNED8 \*pucDefault); |

Parameters

| pucDefault (I) | Default directory. Can be in the form of drive letter and path (f:\path) or UNC (\\server\vol\path). If an empty or NULL string is given, then the default path is cleared. |

Remarks

If a path is given, then subsequent AdsCreateTable or AdsOpenTable calls will look first in the given path (if no path is provided with the table name). This setting affects open/creation of indexes in the same manner. AdsSetDefault does not result in a connection to the server, nor does this routine verify the existence of the server on the given path.

The default path is used for path resolution when opening and creating tables. If an application creates or opens a table (AdsOpenTable), and it does not supply a path with the table name, then the default path is used as the path for opening the table. If the table name has no path, no default path, or no search path (see [AdsSetSearchPath](ace_adssetsearchpath.md)), then the current working directory of the application is used. Only a single path can be used.

AdsSetDefault is a global setting that affects the behavior of the entire application.

Example

[Click Here](ace_examples.md#adssetdefaultexample)

See Also

[AdsGetDefault](ace_adsgetdefault.md)

[AdsSetSearchPath](ace_adssetsearchpath.md)

[AdsOpenTable](ace_adsopentable.md)

[AdsCreateTable](ace_adscreatetable.md)

[AdsGetTableHandle](ace_adsgettablehandle.md)
