---
title: Master Sp Moveddobjectfile
slug: master_sp_moveddobjectfile
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_moveddobjectfile.htm
source: Advantage CHM
tags:
  - master
checksum: 660d79b12185078d6e27f2bf5244a79e39c17ef8
---

# Master Sp Moveddobjectfile

sp\_MoveDDObjectFile

sp\_MoveDDObjectFile

Advantage SQL Engine

| sp\_MoveDDObjectFile  Advantage SQL Engine |  |  |  |  |

Moves the physical file or files associated with a dictionary object.

Syntax

sp\_MoveDDObjectFile(

ObjectType,Integer;

ObjectName,Character,200,

NewFilePath,Character,260,

IndexFiles,MEMO,

Parent,Character,260,

Options,Integer )

Parameters

| ObjectType (I) | Object type of the object to move. Only ADS\_DD\_TABLE\_OBJECT and ADS\_DD\_INDEX\_FILE\_OBJECT are supported at this time. |
| ObjectName (I) | Name of the object to move. |
| NewFilePath (I) | Fully qualified path to move the object file(s) to. |
| IndexFiles (I) | List of index files to move with a table file. Only used with table objects. |
| Parent (I) | Name of parent object. Name of Only used with index file objects. |
| Options (I) | Must be zero. Reserved for future use. |

Remarks

sp\_MoveDDObjectFile can be used to move a database object's file or associated files to a new location on the server. If ObjectType is 1 (ADS\_DD\_TABLE\_OBJECT), ObjectName must be the database object name of a table. To move a table's index files along with the table, IndexFiles must contain a semicolon-delimited list of the index file's database object names (filename plus extension).

If ObjectType is 3 (ADS\_DD\_INDEX\_FILE\_OBJECT), ObjectName must be the database object name of an index file (filename plus extension). IndexFiles will be ignored, but the Parent must be the database object name of the index file's table.

Note The destination directory specified by NewFilePath must exist prior to calling sp\_MoveDDObjectFile.

Note ALTER TABLE permissions are required to move a table or a table's index file.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Examples

EXECUTE PROCEDURE sp\_MoveDDObjectFile( 1 /\* ADS\_DD\_TABLE\_OBJECT \*/, 'customers', '\\adsserver\data\newdirectory', 'business\_ID.adi;business\_name.adi', NULL, 0 )

EXECUTE PROCEDURE sp\_MoveDDObjectFile( 3 /\* ADS\_DD\_INDEX\_FILE\_OBJECT \*/, 'business\_ID.adi', '\\adsserver\data\newdirectory', NULL, 'customers', 0 )

See Also

[sp\_RenameDDObject](master_sp_renameddobject.md)
