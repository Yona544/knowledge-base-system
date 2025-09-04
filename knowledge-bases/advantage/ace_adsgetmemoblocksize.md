AdsGetMemoBlockSize




Advantage Database Server 12  

AdsGetMemoBlockSize

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetMemoBlockSize  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetMemoBlockSize Advantage Client Engine ace\_Adsgetmemoblocksize Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetMemoBlockSize  Advantage Client Engine |  |  |  |  |

Returns the block size of a memo file associated with a table or cursor.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetMemoBlockSize (ADSHANDLE hTable,  UNSIGNED16 \*pusBlockSize); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pusBlockSize (I) | Buffer in which to return the memo block size. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_NO\_MEMO\_FILE | The table or cursor handle must have an associated memo file. |

Remarks

AdsGetMemoBlockSize returns the memo block size of the memo file associated with the table or SQL cursor handle. The memo block size can be configured when creating a table via the [AdsCreateTable](ace_adscreatetable.htm) ACE API. Note that DBF/NTX (ADS\_NTX) type tables and cursors always have a memo block size of 512.

See Also

[AdsGetMemoLength](ace_adsgetmemolength.htm)

[AdsGetMemoDataType](ace_adsgetmemodatatype.htm)

[AdsCreateTable](ace_adscreatetable.htm)