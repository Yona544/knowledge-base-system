AdsDDRemoveTable




Advantage Database Server 12  

AdsDDRemoveTable

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDRemoveTable  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDRemoveTable Advantage Client Engine ace\_Adsddremovetable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDRemoveTable  Advantage Client Engine |  |  |  |  |

Disassociates a table with the data dictionary.

Syntax

UNSIGNED32 AdsDDRemoveTable( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucTableName,

UNSIGNED16 usDeleteFiles );

Parameters

|  |  |
| --- | --- |
| hAdminConn (I) | Handle of a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |
| pucTableName (I) | Name of the table identifying the table object in the data dictionary. |
| usDeleteFiles (I) | If this parameter is non-zero, the physical files will be deleted permanently. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | The pucTableName does not identify a table object in the data dictionary. |

Remarks

AdsDDRemoveTable disassociates a table, its memo file and its index files with the database defined in the data dictionary. It can also optionally delete the table, memo and index files permanently. After an ADT table is disassociated with the data dictionary, it becomes a [free table](javascript:hhpopuplink.TextPopup(popid_1731427715,FontFace,-1,-1,-1,-1)) and can then be opened through a regular non-data dictionary bound [free connection](javascript:hhpopuplink.TextPopup(popid_7577555X,FontFace,-1,-1,-1,-1)).

DROP permissions on the table are required to remove a table from a data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Note AdsDDRemoveTable requires an exclusive open of the table. An error will be returned if the table cannot be opened exclusively. If the table is the parent of any referential integrity in the data dictionary, the function will return an error.

 

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

Remove the "Customer Information" table from the data dictionary and delete the files at the same time.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

AdsDDRemoveTable( hDD, "Customer Information", TRUE );

AdsDDClose( hDD );

See Also

[AdsDDAddTable](ace_adsddaddtable.htm)

[AdsOpenTable](ace_adsopentable.htm)

[AdsConnect60](ace_adsconnect60.htm)