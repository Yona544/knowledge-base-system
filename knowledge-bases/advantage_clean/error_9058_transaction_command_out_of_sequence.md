---
title: Error 9058 Transaction Command Out Of Sequence
slug: error_9058_transaction_command_out_of_sequence
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_9058_transaction_command_out_of_sequence.htm
source: Advantage CHM
tags:
  - error
checksum: ef3022466521ce5e5efb458923b2aa31a59a63f8
---

# Error 9058 Transaction Command Out Of Sequence

9058 Transaction command out of sequence

9058 Transaction command out of sequence

Advantage Error Guide

| 9058 Transaction command out of sequence  Advantage Error Guide |  |  |  |  |

A BEGIN TRANSACTION occurred while a transaction was already in progress. Or, a COMMIT TRANSACTION or a ROLLBACK TRANSACTION occurred when no transaction was in progress.

In general, 9000 class errors indicate an internal problem within the Advantage server.

On the Windows platform, when Advantage logs a 9000 class error it will also generate a crash dump file. This file will be placed in the error log path (default is c:\), and the filename will be prefixed with "adsdump". Please send this crash dump file, along with all ads\_err error log files to Advantage Technical Support.

For other platforms, please send a small re-creation, along with all ads\_err error log files to Advantage Technical Support.
