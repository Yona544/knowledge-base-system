---
title: Master Transaction Log Files Path
slug: master_transaction_log_files_path
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_transaction_log_files_path.htm
source: Advantage CHM
tags:
  - master
checksum: 874cbe98b400e76d157428fb580c078627f12039
---

# Master Transaction Log Files Path

Transaction Log Files Path

Transaction Log Files Path

Advantage Database Server

| Transaction Log Files Path  Advantage Database Server |  |  |  |  |

Transaction log files are created by the Advantage Transaction Processing System to aid in recording all database operations executed within a transaction. These files allow the Advantage Database Server to properly track data changes; updates, appends, and other operations which write to the database. Once a transaction is committed or rolled back, the log files for the transaction are deleted.

The location of the TPS log files is configurable. A non-default transaction file path may be desirable so that all transaction files are maintained in a single location. All applications with transactions will store their information in these files. The transaction log files are named as \_T-#####.TPS, where ##### if a four or five digit number.

Windows

Default = Root of the C: drive

Example: C:\ADSTPS

Linux

Default = /var/log/advantage

Example: /usr/local/advantage
