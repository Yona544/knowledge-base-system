AdsDDGetIndexFileProperty




Advantage Database Server 12  

AdsDDGetIndexFileProperty

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDGetIndexFileProperty  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDGetIndexFileProperty Advantage Client Engine ace\_Adsddgetindexfileproperty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDGetIndexFileProperty  Advantage Client Engine |  |  |  |  |

Retrieves a property of an index file of a database table from the data dictionary.

Syntax

UNSIGNED32 AdsDDGetIndexFileProperty( ADSHANDLE hDBConn,

UNSIGNED8 \*pucTableName,

UNSIGNED8 \*pucIndexFileName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 \*pusPropertyLen );

Parameters

|  |  |
| --- | --- |
| hDBConn (I) | Handle of a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |
| pucTableName (I) | Name of the table in the database with the specified index. |
| pucIndexFileName (I) | Name of the index file associated with the table to retrieve the specified property. |
| usPropertyID (I) | Index of the property to retrieve. See Remarks for allowed values. |
| pvProperty (O) | Pointer to the buffer where the property is to be copied into. |
| \*pusPropertyLen (I/O) | On input, specifies the size of the buffer pointed to by pvProperty. On output, returns the length of the property copied into the buffer. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid index property, or the specified property cannot be retrieved. |
| AE\_INSUFFICIENT\_BUFFER | The size of the property to be copied into pvProperty is larger than the buffer size specified by \*pusPropertyLen. The required buffer length is returned in \*pusPropertyLen when this error occurs. |

Remarks

AdsDDGetIndexFileProperty retrieves a property of the specified index file associated with the specified table from the data dictionary. The following are the valid values of usPropertyID and the expected return value in pvProperty and \*pusPropertyLen.

|  |  |
| --- | --- |
| usPropertyID | Description |
| ADS\_DD\_INDEX\_FILE\_PATH | The function returns the absolute path of the index file. The path is the full path including directory and it is returned as a NULL terminated string in pvProperty. This property can only be retrieved by users with read permissions to the parent table. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information. |
| ADS\_DD\_INDEX\_FILE\_PAGESIZE | The function returns the index page size of the specified index file. This property is returned as a 4-byte integer in the buffer pointed to by pvProperty. \*pusPropertyLen must be 4 on input when calling this function with this property id. See [AdsCreateIndex](ace_adscreateindex.htm) for more information on index page size. Since configurable index page size is a new functionality introduced in the 6.1 release, an AE\_PROPERTY\_NOT\_SET error may be returned when trying to retrieve this property on a data dictionary created prior to the 6.1 release. This property can only be retrieved by users with read permissions to the parent table. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.htm) for more information. |

Example

After making a connection to the database, find out the location of the "Customer Information.ADI" index in the "Customer Information" table.

UNSIGNED8  aucIndexPath[260];

UNSIGNED16  usBufferSize;

 

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS",

NULL, ADS\_DEFAULT, &hDD );

usBufferSize = (UNSIGNED16)sizeof( aucIndexPath );

AdsDDGetIndexProperty( hDD, "Customer Information", "Customer

Information.ADI", ADS\_DD\_INDEX\_FILE\_PATH,

aucIndexPath, &usBuffSize );

AdsDisconnect( hDD );

 

See Also

[AdsConnect60](ace_adsconnect60.htm)

[AdsDDAddIndexFile](ace_adsddaddindexfile.htm)

[AdsDDAddTable](ace_adsddaddtable.htm)

[AdsDDFindFirstObject](ace_adsddfindfirstobject.htm)

[AdsDDFindNextObject](ace_adsddfindnextobject.htm)

[system.indexfiles](master_system_indexfiles.htm)