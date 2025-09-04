---
title: Ace Adsgettablefilename
slug: ace_adsgettablefilename
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgettablefilename.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 31bde1e4a5e5bcd3a821a98d7a5e00e21b4769ff
---

# Ace Adsgettablefilename

AdsGetTableFilename

AdsGetTableFilename

Advantage Client Engine

| AdsGetTableFilename  Advantage Client Engine |  |  |  |  |

Returns the table name as the base name, the base name with extension, or the full path name (UNC format)

Syntax

| UNSIGNED32 | AdsGetTableFilename (ADSHANDLE hTable,  UNSIGNED16 usOption,  UNSIGNED8 \*pucName,  UNSIGNED16 \*pusLen); |

Parameters

| hTable (I) | Handle of table or cursor. |
| usOption (I) | Specifies the portion of the filename desired. Valid options are ADS\_BASENAME (retrieve the name of the file without the extension), ADS\_BASENAMEANDEXT (retrieve the name of the file with the extension), ADS\_FULLPATHNAME (retrieve the fully qualified UNC filename). |
| pucName (O) | Name of table is returned in this buffer. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

If the ADS\_FULLPATHNAME is given as the option, then the fully qualified UNC path name is returned regardless of how the file was opened. For example, even if the file was opened with a drive letter style path (e.g. f:\data\file.dbf), a UNC filename will be returned by this routine (e.g., \\server\volume\data\file.dbf). The UNC path can include connection path information such as the port number if it was included in the connection path.  Also note that if the connection path used a server-side alias, then that alias will be in the path as opposed to the actual folder on the server.

Example

[Click Here](ace_examples.md#adsgettablefilenameexample)

See Also

[AdsCreateTable](ace_adscreatetable.md)

[AdsOpenTable](ace_adsopentable.md)

[AdsGetTableHandle](ace_adsgettablehandle.md)

[AdsGetIndexFilename](ace_adsgetindexfilename.md)
