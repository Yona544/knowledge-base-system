AdsDDRemoveIndexFile




Advantage Database Server 12  

AdsDDRemoveIndexFile

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDRemoveIndexFile  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDRemoveIndexFile Advantage Client Engine ace\_Adsddremoveindexfile Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDRemoveIndexFile  Advantage Client Engine |  |  |  |  |

Disassociates an index file with a [database table](javascript:hhpopuplink.TextPopup(popid_2121602366X,FontFace,-1,-1,-1,-1)) and optionally deletes the index file permanently.

Syntax

UNSIGNED32 AdsDDRemoveIndexFile( ADSHANDLE hAdminConn,

UNSIGNED8 \*pucTableName,

UNSIGNED8 \*pucIndexFileName,

UNSIGNED16 usDeleteFile );

Parameters

|  |  |
| --- | --- |
| hAdminConn (I) | Handle of a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |
| pucTableName (I) | Name of the table with the associated index file. |
| pucIndexFileName (I) | Base name including the extension of the index file to disassociate with the table. |
| usDeleteFile (I) | Non-zero value to physically delete the index file from the storage device. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | Either the table specified by pucTableName cannot be located in the data dictionary, or the index file specified by pucIndexFileName is not associated with the table. |

Remarks

AdsDDRemoveIndexFile disassociates the specified index file with the table. After calling this function, the indexes in the specified index file will not be automatically available when the table is opened. If usDeleteFile is True, the index file is physically deleted and lost permanently.

ALTER permissions on the parent table are required to remove an index from a data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information.

Note AdsDDRemoveIndexFile requires exclusive open of the table. An error will be returned if the table cannot be opened exclusively.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

After making a connection to the database, find the first index file associated with the "Customer Information" table and disassociate it with the table.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

usBufferSize = (UNSIGNED16)sizeof( aucIndexFileName );

if ( AE\_SUCCESS == AdsDDFindFirstObject( hDD, ADS\_DD\_INDEX\_FILE\_OBJECT,

"Customer Information", aucIndexfileName,

&usBufferSize, &hFindHandle ))

{

AdsDDRemoveIndexFile( hDD, "Customer Information", aucIndexFileName, FALSE ) ;

}

 

/\* No need to close the find handle since we are closing the DD now. \*/

AdsDisconnect( hDD );

See Also

[AdsConnect60](ace_adsconnect60.htm)

[AdsDDDeleteIndex](ace_adsdddeleteindex.htm)

[AdsDDAddIndexFile](ace_adsddaddindexfile.htm)

[AdsDDAddTable](ace_adsddaddtable.htm)

[AdsDDFindFirstObject](ace_adsddfindfirstobject.htm)

[AdsDDFindNextObject](ace_adsddfindnextobject.htm)

[AdsDDFindClose](ace_adsddfindclose.htm)