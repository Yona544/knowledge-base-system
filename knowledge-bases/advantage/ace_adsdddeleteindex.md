AdsDDDeleteIndex




Advantage Database Server 12  

AdsDDDeleteIndex

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDDeleteIndex  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDDeleteIndex Advantage Client Engine ace\_Adsdddeleteindex Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDDeleteIndex  Advantage Client Engine |  |  |  |  |

Delete an index order associated with a table in the data dictionary.

Syntax

UNSIGNED32 AdsDDDeleteIndex( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucTableName,

UNSIGNED8 \*pucIndexName );

Parameters

|  |  |
| --- | --- |
| hAdminConn (I) | Handle of a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |
| pucTableName (I) | Name of the table with the index associated with it. |
| pucIndexName (I) | Name of the index to delete. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | Either the table specified by pucTableName cannot be located in the data dictionary or the index specified by pucIndexName is not part of the table. |

Remarks

AdsDDDeleteIndex deletes the specified index from the index file that is associated with the table. If the index is the only one in the index file, the index file will be deleted. If the index is used by any of the tables referential integrity, it will not be deleted and an error will be returned by the function.

ALTER permissions are required on the parent table to delete a data dictionary index. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Note AdsDDDeleteIndex requires an exclusive open of the table. An error will be returned if the table cannot be opened exclusively.

 

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

After making a connection to the database, find the first index associated with the "Customer Information" table and delete it from the index file.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

usBufferSize = (UNSIGNED16)sizeof( aucIndexName );

if ( AE\_SUCCESS == AdsDDFindFirstObject( hDD, ADS\_DD\_INDEX\_OBJECT,

"Customer Information", aucIndexName,

&usBufferSize, &hFindHandle ))

{

AdsDDDeleteIndex( hDD, "Customer Information", aucIndexName );

AdsDDFindClose( hDD, hFindHandle );

}

See Also

[AdsDDRemoveIndexFile](ace_adsddremoveindexfile.htm)

[AdsDDAddIndexFile](ace_adsddaddindexfile.htm)

[AdsDDAddTable](ace_adsddaddtable.htm)