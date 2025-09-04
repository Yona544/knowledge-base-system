---
title: Ace Adsgetindexfilename
slug: ace_adsgetindexfilename
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetindexfilename.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: de2d5b0c0f1bea63e9b343e47e057e9485f701e8
---

# Ace Adsgetindexfilename

AdsGetIndexFilename

AdsGetIndexFilename

Advantage Client Engine

| AdsGetIndexFilename  Advantage Client Engine |  |  |  |  |

Retrieves the full filename of this index order.

Syntax

| UNSIGNED32 | AdsGetIndexFilename (ADSHANDLE hIndex,  UNSIGNED16 usOption,  UNSIGNED8 \*pucName,  UNSIGNED16 \*pusLen); |

Parameters

| hIndex (I) | Handle of index order of interest (either of an index order from an NTX or IDX file or of a tag within a CDX or ADI). |
| usOption (I) | Specifies the portion of the filename desired. Valid option are ADS\_BASENAME (retrieve the name of the file without the extension), ADS\_BASENAMEANDEXT (retrieve the name of the file with the extension), ADS\_FULLPATHNAME (retrieve the fully qualified UNC filename). |
| pucName (O) | Return the name in this buffer. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

AdsGetIndexFilename returns the file name of the index file containing the indicated index order. If ADS\_FULLPATHNAME is given as the option, then the fully qualified UNC path name is returned regardless of how the file was opened. For example, even if the file was opened with a drive letter style path (e.g., f:\data\file.idx), a UNC filename will be returned by this routine (e.g., \\server\volume\data\file.idx). The UNC path can include connection path information such as the port number if it was included in the connection path.  Also note that if the connection path used a server-side alias, then that alias will be in the path as opposed to the actual folder on the server.

Example

[Click Here](ace_examples.md#adsgetindexfilenameexample)

See Also

[AdsCreateIndex](ace_adscreateindex.md)

[AdsOpenIndex](ace_adsopenindex.md)

[AdsGetIndexName](ace_adsgetindexname.md)

[AdsGetTableFilename](ace_adsgettablefilename.md)
