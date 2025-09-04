---
title: Ade Adsgetversion
slug: ade_adsgetversion
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetversion.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 77a2627197cd09066ad78c60771474e77582889d
---

# Ade Adsgetversion

AdsGetVersion

TAdsTable/TAdsQuery.AdsGetVersion

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsGetVersion  Advantage TDataSet Descendant |  |  |  |  |

Returns the version of the Advantage Client Engine client driver being used.

Syntax

procedure AdsGetVersion( var ulMajor, ulMinor : Longint; var ucLetter : Byte )

Parameter

| ulMajor | Returns the major version number. |
| ulMinor | Returns the minor version number (the number after the dot). This version number is a value out of 100. For example, if ulMajor is 1, and ulMinor is 6, the version is 1.06. If ulMajor is 1, and ulMinor is 60, the version is 1.60. |
| ucLetter | Returns letter version. This is a single character buffer, not an array. |

Description

Windows version information is also included in the Advantage Client Engine DLLs. Use Windows Explorer to view the file properties for version information. Returns a text description.

Example

AdsTable1.AdsGetVersion( ulMajor, ulMinor, ucLetter );

See Also

None.
