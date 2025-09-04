AdsDDAddIndexFile




Advantage Database Server 12  

AdsDDAddIndexFile

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDAddIndexFile  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDAddIndexFile Advantage Client Engine ace\_Adsddaddindexfile Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDAddIndexFile  Advantage Client Engine |  |  |  |  |

Associates an index file with a [database table](javascript:hhpopuplink.TextPopup(popid_2121602366X,FontFace,-1,-1,-1,-1)) in the data dictionary.

Syntax

UNSIGNED32 AdsDDAddIndexFile( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucTableName,

UNSIGNED8 \*pucIndexFilePath,

UNSIGNED8 \*pucComment );

Parameters

|  |  |
| --- | --- |
| hAdminConn (I) | Handle of a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |
| pucTableName (I) | Name of the table to associate the index file. |
| pucIndexFilePath (I) | File path of the index file. If the path given is not a fully qualified path, the index file is assumed to be in the same directory as the table. Once the index file is successfully added in the data dictionary and associated with the table, the base filename of the index file including the extension can be used to identify the index file in the data dictionary. |
| pucComment (I) | Optional description of the index file to store in the data dictionary. This parameter can be NULL. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | The table specified by pucTableName cannot be located in the data dictionary. |
| AE\_INDEX\_ALREADY\_OPEN | The index files is already associated with the specified table. |

Remarks

AdsDDAddIndexFile associates the specified index file with a [database table](javascript:hhpopuplink.TextPopup(popid_2121602366X,FontFace,-1,-1,-1,-1)). After calling this function, all index orders in the specified index file will be automatically available for the table when the table is opened.

ALTER permissions on the associated table are required to add an index to a data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Note AdsDDAddIndexFile requires an exclusive open of the table. An error will be returned if the table cannot be opened exclusively.

 

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

After making a connection to the database,, add a DBF table into the data dictionary and associate three NTX index files with it (two in the AdsDDAddTable API and one in the AdsDDAddIndexFile API).

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

AdsDDAddTable( hDD, "Customer Information", "n:\\mydata\\customer.dbf", ADS\_NTX,

ADS\_ANSI, "Lastname.ntx;Cust\_id.ntx", NULL );

AdsDDAddIndexFile( hDD, "Customer Information", "InvoiceDate.ntx", NULL );

 

AdsDisconnect( hDD );

See Also

[AdsConnect60](ace_adsconnect60.htm)

[AdsDDDeleteIndex](ace_adsdddeleteindex.htm)

[AdsDDRemoveIndexFile](ace_adsddremoveindexfile.htm)

[AdsDDAddTable](ace_adsddaddtable.htm)

[AdsOpenTable](ace_adsopentable.htm)

[sp\_AddIndexFileToDatabase](master_sp_addindexfiletodatabase.htm)