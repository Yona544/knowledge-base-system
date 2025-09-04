---
title: Error 5047 Ae Trans Out Of Sequence
slug: error_5047_ae_trans_out_of_sequence
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_5047_ae_trans_out_of_sequence.htm
source: Advantage CHM
tags:
  - error
checksum: dda3fefae31289db16876aece38eb8bd57a57be7
---

# Error 5047 Ae Trans Out Of Sequence

5047 AE\_TRANS\_OUT\_OF\_SEQUENCE

5047 AE\_TRANS\_OUT\_OF\_SEQUENCE

Advantage Error Guide

| 5047 AE\_TRANS\_OUT\_OF\_SEQUENCE  Advantage Error Guide |  |  |  |  |

The transaction command was not in a valid sequence. The following are possible causes:

| 1. | Attempting to commit or rollback a transaction when there is no active transaction. |

| 2. | Attempting to create a savepoint when there is no active transaction. |

| 3. | Trying to commit or rollback a transaction across transaction boundary, i.e. trying to commit or rollback a nested transaction in a subprogram without initiating the transaction . See [Nesting Transactions](master_nesting_transactions.md) for additional information. |
