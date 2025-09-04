AdsIsRecordInAOF




Advantage Database Server 12  

AdsIsRecordInAOF

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsRecordInAOF  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsRecordInAOF Advantage Client Engine ace\_Adsisrecordinaof Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsRecordInAOF  Advantage Client Engine |  |  |  |  |

Determine if a specific record is in an Advantage Optimized Filter (AOF).

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsIsRecordInAOF (ADSHANDLE hTable,  UNSIGNED32 ulRecordNumber,  UNSIGNED16 \*pbIsInAOF ); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor with existing AOF. |
| ulRecordNumber (I) | Record number to check. If this is 0, then the current record number is checked. |
| \*pbIsInAOF (O) | Return True if the specified record number is in the AOF, False if not. |

Remarks

AdsIsRecordInAOF can be used to determine if an Advantage Optimized Filter (AOF) on the server contains a specific record. If the call is made while using [Advantage Local Server](master_advantage_local_server.htm), the value returned by this API does not guarantee that the actual record value matches the AOF's view of that record. This is because another client could have updated the record and those changes would not be reflected in other clients' AOFs. Also, if an AOF is not fully optimized, it is possible for a record to be included in the AOF initially but not to pass the filter. Records that fit this description are dynamically removed from the filter as the records are read. A call to AdsIsRecordInAOF can indicate that a given record is in the AOF, but it is possible for that record to be filtered out when it is read. Therefore, this API is best used with fully optimized AOFs or with AOFs that have been created with the ADS\_RESOLVE\_IMMEDIATE option (see [AdsSetAOF](ace_adssetaof.htm) ).

Example

[Click Here](ace_aof_and_encryption_examples.htm#adsisrecordinaof_example)

See Also

[AdsSetAOF](ace_adssetaof.htm)

[AdsGetAOFOptLevel](ace_adsgetaofoptlevel.htm)

[AdsCustomizeAOF](ace_adscustomizeaof.htm)