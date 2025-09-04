---
title: Ace Adsddfindfirstobject
slug: ace_adsddfindfirstobject
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddfindfirstobject.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: c7cd1873311333a46f6ce0392b3046ce5761ec98
---

# Ace Adsddfindfirstobject

AdsDDFindFirstObject

AdsDDFindFirstObject

Advantage Client Engine

| AdsDDFindFirstObject  Advantage Client Engine |  |  |  |  |

Retrieves the name of the first object of the specified type from the data dictionary.

Syntax

UNSIGNED32 AdsDDFindFirstObject( ADSHANDLE hDBConn,

UNSIGNED16 usFindObjectType,

UNSIGNED8 \*pucParentName,

UNSIGNED8 \*pucObjectName,

UNSIGNED16 \*pusObjectNameLen,

ADSHANDLE \*phFindHandle );

Parameters

| hDBConn (I) | Handle of a database connection). |
| usFindObjectType (I) | Type of objects to search for. See Remarks below for allowed values. |
| pucParentName (I) | Name of the object that is the parent or owner of the object searched for. This parameter is ignored when searching for table, view, user group or referential integrity objects. When searching for an index file, an index order or a field object, this parameter should supply the name of the associated table object. When searching for a user, this parameter can optionally supply the name of the user group to limit the search result to users who are members of the user group. |
| pucObjectName (O) | Returns the name of first object in the data dictionary matching the search condition. The length of the object name has a maximum length of ADS\_MAX\_OBJECT\_NAME\_LEN. |
| pusObjectNameLen (I/O) | On input, specifies the size of the buffer pointed to by the pucObjectName. On output, returns the length of the object name returned in pucObjectName. The maximum size of the object name in the data dictionary is defined by the constant ADS\_DD\_MAX\_OBJECT\_NAME\_LEN. |
| phFindHandle (O) | Returns a find handle that must be used in subsequent calls to [AdsDDFindNextObject](ace_adsddfindnextobject.md) to iterate the list of objects. The find handle is valid until it is closed by [AdsDDFindClose](ace_adsddfindclose.md) or until the data dictionary handle is closed. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | The name specified by pucParentName is not a valid object in the data dictionary. |
| AE\_NO\_OBJECT\_FOUND | No object matching the specified condition was found in the data dictionary. |

Remarks

AdsDDFindFirstObject finds an object in the data dictionary matching the specified condition and returns the name of the object. After calling this function, AdsDDFindNext can be called to iterate through all objects that match the specified search condition.

| usFindObjectType | Description |
| ADS\_DD\_TABLE\_OBJECT | Retrieves the name of a table object. The pucParentName is ignored and assumed to be the database. |
| ADS\_DD\_VIEW\_OBJECT | Retrieves the name of a view object. The pucParentName is ignored and assumed to be the database. |
| ADS\_DD\_VIEW\_OR\_TABLE\_OBJECT | Retrieves the name of either a view or a table object. The pucParentName is ignored and assumed to be the database. |
| ADS\_DD\_RELATION\_OBJECT | Retrieves the name of a referential integrity definition. The pucParentName is ignored and assumed to be the database. |
| ADS\_DD\_INDEX\_FILE\_OBJECT | Retrieves the name of an index file object that is associated with the table object specified by the pucParentName. |
| ADS\_DD\_INDEX\_OBJECT | Retrieves the name of an index order that has been defined in any index file associated with the table specified by the pucParentName. |
| ADS\_DD\_FIELD\_OBJECT | Retrieves the name of the first field in the table specified by the pucParentName. The order of the returned field name is the order that the fields appear in the table. |
| ADS\_DD\_USER\_OBJECT | Retrieves the name of a user object. If pucParentName is NULL or empty string, this function, together with AdsDDFindNextObject, will iterate through all users in the database. If the pucParentName is no NULL or empty string, it must specify a user group name. In such case, this function, together with AdsDDFindNextObject, will iterate through all users who are members of the specified user group. |
| ADS\_DD\_USER\_GROUP\_OBJECT | Retrieves the name of a user group. The pucParentName is ignored and assumed to be the database. |
| ADS\_DD\_PROCEDURE\_OBJECT | Retrieves the name of a stored procedure. The pucParentName is ignored and assumed to be the database. |
| ADS\_DD\_LINK\_OBJECT | Retrieves the name of a link object. The pucParentName is ignored and assumed to be the database. |
| ADS\_DD\_TRIGGER\_OBJECT | Retrieves the name of a trigger object. |
| ADS\_DD\_QUALIFIED\_TRIGGER\_OBJ | Retrieves the qualified name of a trigger object. The qualified name includes the table name prefix, followed by two colon characters ( :: ), followed by the trigger name. |
| ADS\_DD\_PUBLICATION\_OBJECT | Retrieves the name of a publication object. The pucParentName is currently ignored and assumed to be the database. |
| ADS\_DD\_ARTICLE\_OBJECT | Retrieves the name of a published article associated with the publication specified by pucParentName. |
| ADS\_DD\_SUBSCRIPTION\_OBJECT | Retrieves the name of a subscription object. The pucParentName is currently ignored and assumed to be the database. |
| ADS\_DD\_DATABASE\_TRIGGER\_OBJ | Retrieves the name of [database trigger objects](master_database_triggers.md). |

Example

Find all index files that are associated with the "Customer Information" table.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

usBufferSize = (UNSIGNED16)sizeof( aucFileName );

if ( AE\_SUCCESS == AdsDDFindFirstObject( hDD, ADS\_DD\_INDEX\_FILE\_OBJECT,

"Customer Information", aucFileName,

&usBufferSize, &hFindHandle ))

{

do

{

printf( "%s\n", aucFileName );

usBufferSize = (UNSIGNED16)sizeof( aucFileName );

}

while ( AE\_SUCCESS == AdsDDFindNextObject( hDD, hFindHandle, aucFileName, &usBufferSize ));

}

 

/\* No need to call AdsDDFindClose since we are closing the DD. \*/

AdsDisconnect( hDD );

See Also

[AdsDDFindNextObject](ace_adsddfindnextobject.md)

[AdsDDFindClose](ace_adsddfindclose.md)

[AdsConnect60](ace_adsconnect60.md)
