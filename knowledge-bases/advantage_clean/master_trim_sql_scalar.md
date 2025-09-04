---
title: Master Trim Sql Scalar
slug: master_trim_sql_scalar
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_trim_sql_scalar.htm
source: Advantage CHM
tags:
  - master
checksum: 5839695bd8c08d8c26a0b9b5557489080d2131f5
---

# Master Trim Sql Scalar

TRIM

TRIM

Advantage SQL Engine

| TRIM  Advantage SQL Engine |  |  |  |  |

Trims a given string of characters from a given string.

Syntax

TRIM( [[ LEADING | TRAILING | BOTH [ str1 ] FROM ] | [ str1 FROM ]] str2 )

Arguments

| str1 | String of characters to trim off (Default is a single space). |
| str2 | Source string from which to trim characters. |

Remarks

TRIM removes occurrences of str1 from the beginning or end of str2. When passed no trim options, TRIM removes all leading or trailing white space from str2. By specifying LEADING or TRAILING as the trim option, TRIM will remove all leading or trailing occurrences of str1 from str2. The default option is BOTH. If str1 or a trim option is specified, the FROM keyword must precede str2. If either str1 or str2 evaluates to NULL, TRIM returns NULL.

TRIM removes multiple occurrences of str1 from str2. For example:

SELECT TRIM( 'xy' FROM 'xyxyxAyxxy' ) FROM system.iota

would return:

'xAyx'

Examples

SELECT TRIM( lastname ) from customers

SELECT TRIM( LEADING FROM lastname ) FROM customers

SELECT TRIM( '.' FROM address ) FROM customers
