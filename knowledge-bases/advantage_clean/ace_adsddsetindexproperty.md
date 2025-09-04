---
title: Ace Adsddsetindexproperty
slug: ace_adsddsetindexproperty
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddsetindexproperty.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: f82481408ca81727420906104ea61a18ee37fd1b
---

# Ace Adsddsetindexproperty

AdsDDSetIndexProperty

AdsDDSetIndexProperty

Advantage Client Engine

| AdsDDSetIndexProperty  Advantage Client Engine |  |  |  |  |

Sets one property associated with a specified index key in the data dictionary.

Syntax

UNSIGNED32 AdsDDSetIndexProperty( ADSHANDLE hDBConn,

UNSIGNED8 \*pucTableName,

UNSIGNED8 \*pucIndexName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 usPropertyLen );

Parameters

| hDBConn (I) | Handle of a database connection). |
| pucTableName (I) | Name of the table on which the index has been built. |
| pucIndexName (I) | Name of the index object to set the associated property. |
| usPropertyID (I) | Index of an Index property to set. See Remarks for allowed values. |
| pvProperty (I) | Pointer to the buffer where the property value is stored. |
| usPropertyLen (I) | The size of the property specified by the pvProperty. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | Possible cause for the error is that the pucTableName or pucIndexName does not refer a valid object in the database. |
| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid property ID for an index, or the specified property cannot be set. |

Remarks

AdsDDSetIndexProperty sets one property associated with the specified index. The new property overwrites the existing property in the data dictionary. The following are the valid values of usPropertyID and the expected value in pvProperty and usPropertyLen.

ALTER permission on the table containing the index is required to modify data dictionary index properties. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

| usPropertyID | Description |
| ADS\_DD\_COMMENT | Stores a new description for the index. The pvProperty parameter is expected to be a NULL terminated string. usPropertyLen is the length of the string including the NULL terminator. If pvProperty is NULL or an empty string, the index description is removed. |

Example

After making a connection to the database, set a new index description for the index "Field1" in table "Table1".

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

sprintf( aucDesc, "This is an index description" );

ulReturnCode = AdsDDSetIndexProperty( hDD, "Table1", "Field1", ADS\_DD\_COMMENT, aucDesc,

(UNSIGNED16)( strlen(aucDesc) + 1 ));

 

See Also

[AdsDDGetIndexProperty](ace_adsddgetindexproperty.md)

[sp\_ModifyIndexProperty](master_sp_modifyindexproperty.md)
