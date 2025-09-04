AdsIsRecordEncrypted




Advantage Database Server 12  

TAdsTable/TAdsQuery.AdsIsRecordEncrypted

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.AdsIsRecordEncrypted  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.AdsIsRecordEncrypted Advantage TDataSet Descendant ade\_Adsisrecordencrypted Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.AdsIsRecordEncrypted  Advantage TDataSet Descendant |  |  |  |  |

Returns the encrypted status of the current record.

Syntax

function AdsIsRecordEncrypted (ulRecNum : Longint) : boolean;

Parameter

|  |  |
| --- | --- |
| ulRecNum | Physical record number to check if encrypted, or 0 for active record. |

Description

AdsIsRecordEncrypted will return True if the given record is encrypted. It will return False if the record is not encrypted.

Example

AdsTable1.FindKey( [Smith] );

if ( AdsTable1.AdsIsRecordEncrypted( 0 ) ) then

AdsTable1.AdsEnableEncryption( 'secret' );

 

See Also

[AdsDisableEncryption](ade_adsdisableencryption.htm)

[AdsEnableEncryption](ade_adsenableencryption.htm)

[AdsDecryptRecord](ade_adsdecryptrecord.htm)

[AdsEncryptRecord](ade_adsencryptrecord.htm)