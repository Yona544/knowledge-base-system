---
title: Error 2102 Data Truncated
slug: error_2102_data_truncated
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2102_data_truncated.htm
source: Advantage CHM
tags:
  - error
checksum: 898ab5076fd3b9f2bf0805a1cf65e3fcdca9b887
---

# Error 2102 Data Truncated

2102 Data truncated

2102 Data truncated

Advantage Error Guide

| 2102 Data truncated  Advantage Error Guide |  |  |  |  |

Problem: An internal buffer within the SQL engine was too small, and data was truncated when copied into it. The most likely cause of this error is the result of data conversions. For example if you set a DBF numeric field parameter with a double or a character value, it might overflow the field width or precision. The SQL engine returns this code as a warning. All updates still occur when this code is returned. For example, if an UPDATE statement is executed that assigns too many digits of precision to a numeric field, the 2102 code will be returned, but all updates on all applicable rows will still be performed.

Solution: Verify that the statement is using compatible data types.
