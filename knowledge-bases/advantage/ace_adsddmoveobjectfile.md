AdsDDMoveObjectFile




Advantage Database Server 12  

AdsDDMoveObjectFile

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDMoveObjectFile  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDMoveObjectFile Advantage Client Engine ace\_Adsddmoveobjectfile Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDMoveObjectFile  Advantage Client Engine |  |  |  |  |

Moves the physical file or files associated with a dictionary object.

Syntax

UNSIGNED32 AdsDDMoveObjectFile( ADSHANDLE hDictionary,

UNSIGNED16 usObjectType,

UNSIGNED8 \*pucObjectName,

UNSIGNED8 \*pucNewPath,

UNSIGNED8 \*pucIndexFiles,

UNSIGNED8 \*pucParent,

UNSIGNED32 ulOptions );

Parameters

|  |  |
| --- | --- |
| hDictionary (I) | Handle of a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |
| usObjectType (I) | Object type of the object to move. Only ADS\_DD\_TABLE\_OBJECT and ADS\_DD\_INDEX\_FILE\_OBJECT are supported at this time. |
| pucObjectName (I) | Name of the object to move. |
| pucNewPath (I) | Fully qualified path to move the object file(s) to. |
| pucIndexFiles (I) | List of index files to move with a table file. Only used with table objects. |
| pucParent (I) | Name of parent object. Name of Only used with index file objects. |
| ulOptions (I) | Must be zero. Reserved for future use. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_OBJECT\_NAME | The object specified by pucObjectName cannot be located in the data dictionary. |
| AE\_TABLE\_NOT\_EXCLUSIVE | The object's file cannot be moved if it is already open. |

Remarks

AdsDDMoveObjectFile can be used to move a database object's file or associated files to a new location on the server. If usObjectType is ADS\_DD\_TABLE\_OBJECT, pucObjectName must be the database object name of a table. To move a table's index files along with the table, pucIndexFiles must contain a semi-colon delimited list of the index file's database object names (filename plus extension).

If usObjectType is ADS\_DD\_INDEX\_FILE\_OBJECT, pucObject name must be the database object name of an index file (filename plus extension). pucIndexFiles will be ignored, but pucParent must be the database object name of the index file's table.

Note The destination directory specified by pucNewPath must exist prior to calling AdsDDMoveObjectFile.

Note ALTER TABLE permissions are required to move a table or a table's index file.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Examples

ulRetCode = AdsDDMoveObjectFile( hConnect,

ADS\_DD\_TABLE\_TYPE,

"customers",

"D:\data\newdirectory",

"business\_name.adi;business\_ID.adi;",

NULL,

0 );

ulRetCode = AdsDDMoveObjectFile( hConnect,

ADS\_DD\_INDEX\_FILE\_TYPE,

"business\_ID.adi",

"\\adsserver\data\newdirectory",

NULL,

"customers",

0 );

See Also

[AdsDDRenameObject](ace_adsddrenameobject.htm)