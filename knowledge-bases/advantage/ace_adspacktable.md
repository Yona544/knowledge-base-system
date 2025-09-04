AdsPackTable




Advantage Database Server 12  

AdsPackTable

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsPackTable  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsPackTable Advantage Client Engine ace\_Adspacktable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsPackTable  Advantage Client Engine |  |  |  |  |

Removes deleted records from the given table and re-indexes the table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsPackTable ( ADSHANDLE hTable ); |

|  |  |
| --- | --- |
| UNSIGNED32 | AdsPackTable120 ( ADSHANDLE hTable,                   UNSIGNED32 ulMemoBlockSize,                   UNSIGNED32 ulOptions ); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table. |
| ulMemoBlockSize (I) | New memo block size to use for the memo file. If the value 0 (ADS\_DEFAULT) is specified, the memo block size will be unchanged. |
| ulOptions (I) | Reserved for future use. Must be zero (0). |

Remarks

AdsPackTable will remove all deleted records from the specified table. Internal fragmentation in memo files will also be eliminated. The table is then re-indexed. If a progress callback function is available, it will be called during the reindexing. The indexes must be opened during the pack or they will become logically invalid. This operation requires exclusive access to the table, specified during the open. The AdsPackTable120 version of this API can be used to change the memo block size of an existing table. See [AdsCreateTable](ace_adscreatetable.htm) for information about valid memo block sizes.

Note that if encryption was ever enabled on the table, the table cannot be packed unless the encryption is enabled with the correct password.

Note This API only accepts table handles. The use of a cursor handle with this API is illegal and will result in an error. See [AdsExecuteSQL](ace_adsexecutesql.htm) for more details.

 

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.htm).

Example

[Click Here](ace_examples.htm#adspacktableexample)

See Also

[AdsRegisterCallbackFunction](ace_adsregistercallbackfunction.htm)

[AdsZapTable](ace_adszaptable.htm)

[AdsOpenTable](ace_adsopentable.htm)

[AdsEnableEncryption](ace_adsenableencryption.htm)

[AdsDecryptTable](ace_adsdecrypttable.htm)