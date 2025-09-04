---
title: Master Backup And Restore Canned Procedure Result Sets
slug: master_backup_and_restore_canned_procedure_result_sets
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_backup_and_restore_canned_procedure_result_sets.htm
source: Advantage CHM
tags:
  - master
checksum: f3e7ae0b8ac8aa0afc6e98a612f2688d75fc8e28
---

# Master Backup And Restore Canned Procedure Result Sets

Backup and Restore Canned Procedure Result Sets

Backup and Restore Canned Procedure Result Sets

Advantage Concepts

| Backup and Restore Canned Procedure Result Sets  Advantage Concepts |  |  |  |  |

The backup and restore canned procedures return a result set with one or more rows of the following format. If an empty set is returned, the operation was a success and there were no warnings or errors to report.

Severity,Integer

Error Code,Integer

Error Message,Memo

Table Name,Memo

Additional Info,Memo

Source File,char,32

Source Line,Integer

 

Severity

An integer representation of the severity of the result set error/warning. The value of this field will range between 0 and 10, with 0 being the lowest severity, and 10 being the highest.

Error Code

The Advantage error code for this entry.

Error Message

A text message for this error or warning.

Table Name

The name of the table that generated this entry.

Additional Info

Additional information (if available) about this entry.

Source File

Internal source file that generated this entry.

Source Line

Internal source line that generated this entry.
