---
title: Error 7036 Failed Transaction Recovery Error
slug: error_7036_failed_transaction_recovery_error
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7036_failed_transaction_recovery_error.htm
source: Advantage CHM
tags:
  - error
checksum: 62305cba134380df2f183196cb4d0592999792cd
---

# Error 7036 Failed Transaction Recovery Error

7036 Failed transaction recovery error

7036 Failed transaction recovery error

Advantage Error Guide

| 7036 Failed transaction recovery error  Advantage Error Guide |  |  |  |  |

Problem: A failed transaction recovery was not successful.

Solution: Make sure the table or index files associated with the failed transaction were not opened by another application. This error can also occur if the transaction log file could not be opened. Refer to the error log file (ADS\_ERR.ADT or ADS\_ERR.DBF) for more specific errors related to this failure.
