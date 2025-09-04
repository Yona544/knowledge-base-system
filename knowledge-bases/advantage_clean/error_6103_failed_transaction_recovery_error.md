---
title: Error 6103 Failed Transaction Recovery Error
slug: error_6103_failed_transaction_recovery_error
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6103_failed_transaction_recovery_error.htm
source: Advantage CHM
tags:
  - error
checksum: 3f3b0f37482680517e6834e840175017fa44fbf3
---

# Error 6103 Failed Transaction Recovery Error

6103 Failed transaction recovery error

6103 Failed transaction recovery error

Advantage Error Guide

| 6103 Failed transaction recovery error  Advantage Error Guide |  |  |  |  |

Problem: The AX\_TPSCleanup() function failed to complete a failed transaction recovery.

Solution: Make sure the table or index files associated with the failed transaction were not opened by another application. This error can also occur if the transaction log file could not be opened. Refer to the error log file, ADS\_ERROR.ADT or ADS\_ERR.DBF, for more specific errors related to this failure.
