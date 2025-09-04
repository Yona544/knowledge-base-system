---
title: Error 6619 Client Comm Layer Was Already Busy With One Database Operation When A Second Database Operation Was Requested
slug: error_6619_client_comm_layer_was_already_busy_with_one_database_operation_when_a_second_database_operation_was_requested
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6619_client_comm_layer_was_already_busy_with_one_database_operation_when_a_second_database_operation_was_requested.htm
source: Advantage CHM
tags:
  - error
checksum: d9feb4b34115716ecc8a4edbfffac502c3826bd0
---

# Error 6619 Client Comm Layer Was Already Busy With One Database Operation When A Second Database Operation Was Requested

6619 Client comm layer was already busy with one database operation when a second database operation was requested

6619 Client comm layer was already busy with one database operation when a second database operation was requested

Advantage Error Guide

| 6619 Client comm layer was already busy with one database operation when a second database operation was requested  Advantage Error Guide |  |  |  |  |

Advantage clients support functionality to call a "progress" function during index creation and reindexing. If this progress function makes a call to the Advantage Database Server, such as to AdsGetRecordCount() or LastRec(), a 6619 error will occur. A call cannot be made to the Advantage server at this time because the communication layer is busy with the creation of the index. Only one call can be using the communication layer at a time. Only use functions that do not require a call to the Advantage Database Server in the index creation progress function. If the number of records in the table is needed by the index creation progress function, retrieve that information before the index creation operation and store the results in a variable for use in the index creation progress function.

Note It is possible to get a 6619 error when executing database operations in an [Advantage Extended Procedure](master_advantage_extended_procedures.md) (AEP). If using Advantage Local Server the client application and the AEP must use the same "ShowDeleted" setting. If both the client and AEP are written in the same language this is usually not a problem. If the settings are mismatched you may receive a 6619 (comm layer was busy) error.
