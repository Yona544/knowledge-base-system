---
title: Ace Adsddgetindexproperty
slug: ace_adsddgetindexproperty
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddgetindexproperty.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 3e0ed9de34d81c3866f9c49da9fdbc6a51e6bc0d
---

# Ace Adsddgetindexproperty

AdsDDGetIndexProperty

AdsDDGetIndexProperty

Advantage Client Engine

| AdsDDGetIndexProperty  Advantage Client Engine |  |  |  |  |

Retrieves a property of an index of a database table from the data dictionary.

Syntax

UNSIGNED32 AdsDDGetIndexProperty( ADSHANDLE hDBConn,

UNSIGNED8 \*pucTableName,

UNSIGNED8 \*pucIndexName,

UNSIGNED16 usPropertyID,

VOID \*pvProperty,

UNSIGNED16 \*pusPropertyLen );

Parameters

| hDBConn (I) | Handle of a database connection). |
| pucTableName (I) | Name of the table in the database with the specified index. |
| pucIndexName (I) | Name of the index associated with the table to retrieve the specified property. |
| usPropertyID (I) | Index of the property to retrieve. See Remarks for allowed values. |
| pvProperty (O) | Pointer to the buffer where the property is to be copied into. |
| pusPropertyLen (I/O) | On input, specifies the size of the buffer pointed to by pvProperty. On output, returns the length of the property copied into the buffer. |

Special Return Codes

| AE\_INVALID\_PROPERTY\_ID | Either the value supplied in usPropertyID is not a valid index property, or the specified property cannot be retrieved. |
| AE\_INSUFFICIENT\_BUFFER | The size of the property to be copied into pvProperty is larger than the buffer size specified by \*pusPropertyLen. The required buffer length is returned in \*pusPropertyLen when this error occurs. |
| AE\_PROPERTY\_NOT\_SET | The requested property is not set in the data dictionary. No data is returned in pvProperty and \*pusPropertyLen. |

Remarks

AdsDDGetIndexProperty retrieves a property of the specified index associated with the specified table from the data dictionary. The following are the valid values of usPropertyID and the expected return value in pvProperty and \*pusPropertyLen.

| usPropertyID | Description |
| ADS\_DD\_COMMENT | The function returns the index description as a NULL terminated string in pvProperty. |
| ADS\_DD\_INDEX\_FILE\_NAME | The function returns the name of the index file where the specified index is located. The name is returned as a NULL terminated string in pvProperty. The returned index file name can be used to locate the index file object in the data dictionary. |
| ADS\_DD\_INDEX\_EXPRESSION | The function returns the index expression of the specified index. The expression is returned as a NULL terminated string in pvProperty. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_INDEX\_CONDITION | The function returns the conditional expression of the specified index. The expression is returned as a NULL terminated string in pvProperty. A conditional expression is a logical expression that filters the records placed in an index. Only records that pass the conditional expression are in the index. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_INDEX\_OPTIONS | The function returns a bit field of the optional property of the specified index. This property is returned as a 4-byte integer in the buffer pointed to by pvProperty. \*pusPropertyLen must be 4 on input when calling this function with this property id. The index options are ORed together into the bit field. The possible options in the bit field are ADS\_COMPOUND, ADS\_DESCENDING, ADS\_UNIQUE, and ADS\_CANDIDATE. See [AdsCreateIndex](ace_adscreateindex.md) for additional information on the index options. This property can only be retrieved by users with administrative permissions. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information. |
| ADS\_DD\_INDEX\_KEY\_LENGTH | The function returns the length of the keys in the specified index. The key length is returned as a 2-byte integer in the buffer pointed to by pvProperty. \*pusPropertyLen must be 2 on input when calling this function with this property id. |
| ADS\_DD\_INDEX\_KEY\_TYPE | The function returns the type of the keys of the specified index. The key type is returned as a 2-byte integer in the buffer pointed to by pvProperty. \*pusPropertyLen must be 2 on input when calling this function with this property id. Possible key types are ADS\_STRING, ADS\_NUMERIC, ADS\_DATE, ADS\_LOGICAL, and ADS\_RAW. See [AdsGetKeyType](ace_adsgetkeytype.md) for additional information. |

Example

After making a connection to the database, find out the key type of the "Company Name" index in the "Customer Information" table.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS",

NULL, ADS\_DEFAULT, &hDD );

usBufferSize = (UNSIGNED16)sizeof( usKeyType );

AdsDDGetIndexProperty( hDD, "Customer Information", "Company Name",

ADS\_DD\_INDEX\_KEY\_TYPE, &usKeyTypel,

&usBuffSize );

AdsDisconnect( hDD );

See Also

[AdsConnect60](ace_adsconnect60.md)

[AdsDDAddIndexFile](ace_adsddaddindexfile.md)

[AdsDDAddTable](ace_adsddaddtable.md)

[AdsDDFindFirstObject](ace_adsddfindfirstobject.md)

[AdsDDFindNextObject](ace_adsddfindnextobject.md)

[system\_indexes](master_system_indexes.md)
