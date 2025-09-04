---
title: Php Working With Unicode
slug: php_working_with_unicode
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: php_working_with_unicode.htm
source: Advantage CHM
tags:
  - php
checksum: 7ea637c02c4f71e39a2907325e9edb68c7633c6f
---

# Php Working With Unicode

Working with Unicode

Working with Unicode

Advantage PHP Extension

| Working with Unicode  Advantage PHP Extension |  |  |  |  |

The Advantage PHP Extension can read and write Unicode data encoded in UTF-8.

Reading Unicode data is straightforward, with no code changes necessary.  (Note that correctly displaying UTF-8 data will require the use of the HTML meta tag to specify that the page uses the UTF-8 character set.  For, example, the following HTML head element will properly display UTF-8 data retrieved from Advantage:

  <head>

     <meta http-equiv=Content-Type content="text/html; charset=utf-8"/>

  </head>

Writing Unicode data to Advantage requires the use of parameterized queries.  Moreover, parameterized queries must specify the parameter type for Unicode parameters as SQL\_WCHAR.

Note that Unicode character literals are not yet supported in PHP.
