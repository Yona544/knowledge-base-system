6102 XXXXXX is illegal during a transaction




Advantage Database Server 12  

6102 XXXXXX is illegal during a transaction

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6102 XXXXXX is illegal during a transaction  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6102 XXXXXX is illegal during a transaction Advantage Error Guide error\_6102\_xxxxxx\_is\_illegal\_during\_a\_transaction Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6102 XXXXXX is illegal during a transaction  Advantage Error Guide |  |  |  |  |

Problem: The application issued an illegal command (where XXXXXX is the illegal command) during a transaction.

Solution: The following commands and their associated functions are illegal and will not be performed when used within a transaction:

|  |  |
| --- | --- |
| · | UNLOCK, AX\_Unlock(), dbUnlock(), dbUnlockAll(), dbRUnlock(), AX\_IsLocked() |

|  |  |
| --- | --- |
| · | PACK, ZAP |

|  |  |
| --- | --- |
| · | REINDEX, dbReindex() |

|  |  |
| --- | --- |
| · | DELETE TAG, AX\_KillTag(), ordDestroy() |

|  |  |
| --- | --- |
| · | AX\_DBFEncrypt(), AX\_DBFDecrypt() |

|  |  |
| --- | --- |
| · | AX\_File2BLOB() |

|  |  |
| --- | --- |
| · | CLOSE, CLOSE INDEXES, AX\_ClearOrder(), dbCloseArea(), dbClearIndex() |

Note A CLOSE command will not only cause an error, it will actually close the table and any open indexes in the work area and then rollback the current transaction.