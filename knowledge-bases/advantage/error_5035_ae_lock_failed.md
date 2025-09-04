5035 AE\_LOCK\_FAILED




Advantage Database Server 12  

5035 AE\_LOCK\_FAILED

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5035 AE\_LOCK\_FAILED  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5035 AE\_LOCK\_FAILED Advantage Error Guide error\_5035\_ae\_lock\_failed Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5035 AE\_LOCK\_FAILED  Advantage Error Guide |  |  |  |  |

The requested lock could not be granted.

|  |  |
| --- | --- |
| · | The file or record may be locked by another user. |

|  |  |
| --- | --- |
| · | When using the Advantage proprietary table type (ADTs) and the current record has been deleted. |

|  |  |
| --- | --- |
| · | The record may have been modified within a transaction and the transaction has no been committed or rolled back. See [Advantage Transaction Processing System Limitations](master_advantage_transaction_processing_system_limitations.htm). |

 

Linux Note If using a pre-2.4 kernel, it is possible to get this error because of an incorrect lock offset range. See [USE\_LOW\_LOCK\_OFFSETS](master_advantage_local_server_configuration.htm) for more details.