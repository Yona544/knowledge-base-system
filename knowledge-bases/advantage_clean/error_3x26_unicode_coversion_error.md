---
title: Error 3X26 Unicode Coversion Error
slug: error_3x26_unicode_coversion_error
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3x26_unicode_coversion_error.htm
source: Advantage CHM
tags:
  - error
checksum: cd27bfbc706441ca8d83836075bb0e5a69833610
---

# Error 3X26 Unicode Coversion Error

error 3x26 Unicode Coversion Error

3x26 Unicode Conversion Error

Advantage Error Guide

| 3x26 Unicode Conversion Error  Advantage Error Guide |  |  |  |  |

3026, 3126, 3226, 3326, 3426, 3526

Problem: There was a problem converting ANSI/OEM character string in the expression to Unicode string, or vice versa.

Solution: Make sure that the correct adscollate.adt is installed. On non-Windows platform, verify that the Advantage ICU components (aicu.so and icudt40l.dat) are installed.
