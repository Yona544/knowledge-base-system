---
title: Master Disable Failed Transaction Recovery F
slug: master_disable_failed_transaction_recovery_f_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_disable_failed_transaction_recovery_f_.htm
source: Advantage CHM
tags:
  - master
checksum: 01634aa4e240b7a5e9e7cbfe7fac5d8fb7130b83
---

# Master Disable Failed Transaction Recovery F

Disable Failed Transaction Recovery (-F)

Disable Failed Transaction Recovery (-F)

Advantage Database Server

| Disable Failed Transaction Recovery (-F)  Advantage Database Server |  |  |  |  |

If your application was in the middle of a transaction during a file server crash, your transaction failed and you need to return your database to a known state. File server crashes prevent the Advantage Database Server from completing a transaction. As a default, the Advantage Database Server attempts to complete any failed transaction when the Advantage Database Server is loaded. This parameter is used to disable automatic completion of failed transactions when the Advantage Database Server is loaded.

This parameter should be used only if you do not want your failed transaction to be completed. This will leave your database in an unknown state. By using this parameter, existing failed transaction log files will not be scanned and your database will not be returned to a known state. If you are using transactions in your applications, it is NOT recommended that you use this parameter.

Use this parameter only to view the data in the unknown state. Once you scan the data, it is recommended that you reload the Advantage Database Server without this parameter to complete all failed transactions.
