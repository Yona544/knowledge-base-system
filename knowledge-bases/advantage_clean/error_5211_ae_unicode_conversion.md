---
title: Error 5211 Ae Unicode Conversion
slug: error_5211_ae_unicode_conversion
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5211_ae_unicode_conversion.htm
source: Advantage CHM
tags:
  - error
checksum: 157e5c83d8553f06238fe72736c4b29b516efa59
---

# Error 5211 Ae Unicode Conversion

5211 AE\_UNICODE\_CONVERSION

5211 AE\_UNICODE\_CONVERSION

Advantage Error Guide

| 5211 AE\_UNICODE\_CONVERSION  Advantage Error Guide |  |  |  |  |

Problem: There was an error when attempting to convert a Unicode character string into ANSI/OEM code page string, or vice versa.

Solution: When this error occurs, retrieve the text error message that accompanies the error. Some causes of this problem are:

- When trying to store Unicode character data into non-Unicode column, some Unicode characters cannot be converted into the ANSI/OEM code page characters.

- An invalid code page is specified when trying to convert Unicode character data into ANSI/OEM code page character. A possible cause for this situation is that an older version of the adscollate.adt is loaded by the server.
