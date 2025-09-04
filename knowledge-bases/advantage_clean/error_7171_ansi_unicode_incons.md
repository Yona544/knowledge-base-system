---
title: Error 7171 Ansi Unicode Incons
slug: error_7171_ansi_unicode_incons
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7171_ansi_unicode_incons.htm
source: Advantage CHM
tags:
  - error
checksum: d3612031792516ed33f83edb56dcea218f13a698
---

# Error 7171 Ansi Unicode Incons

error\_7171\_ANSI\_UNICODE\_INCONSISTENT

7171 Inconsistent ANSI/Unicode FTS Word Count

Advantage Error Guide

| 7171 Inconsistent ANSI/Unicode FTS Word Count  Advantage Error Guide |  |  |  |  |

Problem: When using wild card in FTS filter expression, i.e. searching in multiple fields, the words to be searched must be the same for all ANSI and Unicode fields. 7171 error is returned when the number of words when parsed using Unicode collation is different from the number of words when parsed in ANSI collation. For example, the expression "Contains( \*, 'КНДР')" where КНДР is encoded in Unicode and is parsed as one word in Unicode. However, in ANSI collation, the same string literal may not be able to translate directly and cannot be parsed into an valid word. If the table contains both ANSI and Unicode fields, the 7171 error will returned.

Solution: Avoid searching both ANSI and Unicode fields for Unicode words that cannot be translated into ANSI encoding.
