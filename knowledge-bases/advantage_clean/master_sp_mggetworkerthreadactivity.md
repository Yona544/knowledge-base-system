---
title: Master Sp Mggetworkerthreadactivity
slug: master_sp_mggetworkerthreadactivity
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_mggetworkerthreadactivity.htm
source: Advantage CHM
tags:
  - master
checksum: 686ed96c35436078e56f60789acbd9d5682b9954
---

# Master Sp Mggetworkerthreadactivity

sp\_mgGetWorkerThreadActivity

sp\_mgGetWorkerThreadActivity

Advantage SQL Engine

| sp\_mgGetWorkerThreadActivity  Advantage SQL Engine |  |  |  |  |

Returns a result set containing information about worker threads that are actively processing an operation on the Advantage Database Server.

Syntax

EXECUTE PROCEDURE sp\_mgGetWorkerThreadActivity()

Parameters

| ThreadNumber (O) | Thread number. |
| OpCode (O) | Operation in progress. |
| UserName (O) | Name of user. |
| ConnNumber (O) | NetWare connection number. (Deprecated) |
| OSUserLoginName (O) | Operating system login name of the connected user. |

Remarks

Examples of Advantage of operations include skip, seek, build index, and open table. Most Advantage operations take less than a millisecond to complete on the Advantage Database Server. A few operations, such as build index, may take more than a few milliseconds to complete. Since most Advantage operations take a very short time to complete, the result of this procedure call will often indicate that no worker threads (other than the worker thread currently processing this operation) are busy.

Example

EXECUTE PROCEDURE sp\_mgGetWorkerThreadActivity();

Possible OpCode Values

| CommTest | 0 |
| CreateDbf | 1 |
| OpenDbf | 2 |
| CloseDbf | 3 |
| PackDbf | 4 |
| ZapDbf | 5 |
| ReadDbfHeader | 6 |
| CreateIndex | 7 |
| SetIndex | 8 |
| ClearIndex | 9 |
| AddTag | 10 |
| DeleteTag | 11 |
| AddKey | 12 |
| DeleteKey | 13 |
| ModifyKey | 14 |
| ReadIndexHeader | 15 |
| WriteIndexHeader | 16 |
| ReadIndexPage | 17 |
| WriteIndexPage | 18 |
| Goto | 19 |
| WriteRecord | 20 |
| GoTop | 21 |
| GoBottom | 22 |
| Skip | 23 |
| Seek | 24 |
| GetMemoLength | 25 |
| ReadMemo | 26 |
| WriteMemo | 27 |
| DataLock | 28 |
| DataUnlock | 29 |
| Disconnect | 30 |
| AppendDbf | 31 |
| Update | 32 |
| ReadTagHdr | 33 |
| GoScopeEnd | 34 |
| IdentifyFreeze | 35 |
| FixFoxPtrs | 36 |
| FlushFoxIndex | 37 |
| SetCommand | 38 |
| BuildIndex | 39 |
| GetLockID | 40 |
| ExprValid | 41 |
| GetCurrRecord | 42 |
| Transaction | 43 |
| BlankAppendKey | 44 |
| FailedTransCleanup | 45 |
| BinaryKeyCompare | 46 |
| WriteMemo | 47 |
| BuildIndex | 48 |
| FailedTransCleanup | 49 |
| KeyNumber | 50 |
| GetRelativeKeyPosition | 51 |
| SetRelativeKeyPosition | 52 |
| UpdateDbfVersionByte | 53 |
| InitializeBlob | 54 |
| WriteBlobData | 55 |
| ReadBlobData | 56 |
| CreateDbf | 57 |
| OpenDbf | 58 |
| CreateIndex | 59 |
| ReadBlobData | 60 |
| InitializeBlob | 61 |
| CommTest | 62 |
| SaveTpsLog | 63 |
| TpsLogAvailable | 64 |
| BuildAOF | 65 |
| MgmtApi | 66 |
| SkipEnhanced | 67 |
| GetMemoLength | 68 |
| ReadMemo | 69 |
| Goto | 70 |
| Update | 71 |
| OpenDbf | 72 |
| AppendFrom | 73 |
| CreateDbf | 74 |
| OpenDbf | 75 |
| AppendDbf | 76 |
| InitializeBlob | 77 |
| GetCollationTables | 78 |
| BuildIndex | 79 |
| Sql | 80 |
| ReadRecordCount | 81 |
| GoTop | 82 |
| GoBottom | 83 |
| ServerTime | 84 |
| OpenDbf | 85 |
| AlwaysFlush | 86 |
| OpenDbf | 87 |
| ReadRecordNumbers | 88 |
| QueryDictionary | 89 |
| LockRIIndexes | 90 |
| Update | 91 |
| Update | 92 |
| AuthenticateConn | 93 |
| FlushFileBuffs | 94 |
| GetCollationTables | 95 |
| InitializeBlob | 96 |
| OpenDbf62 | 97 |
| ScopedKeyCount | 98 |
| OpCodeError | 99 |
| OpCodeError | 100 |
| GetFTSScore | 101 |
| GetMemoLength | 102 |
| CalculateRecordCRC | 103 |
| CreateDbf71 | 104 |
| FilteredKeyCount | 105 |
| FilteredRecCount | 106 |
| InternalOp | 107 |
| AppendDbf | 108 |
| ReBuildIndex | 109 |
