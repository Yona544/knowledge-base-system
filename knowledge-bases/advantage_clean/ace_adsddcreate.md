---
title: Ace Adsddcreate
slug: ace_adsddcreate
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddcreate.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 3df1411530abf9468f32b157e84d8de27768bb89
---

# Ace Adsddcreate

AdsDDCreate

AdsDDCreate

Advantage Client Engine

| AdsDDCreate  Advantage Client Engine |  |  |  |  |

Creates a data dictionary.

Syntax

UNSIGNED32 AdsDDCreate( UNSIGNED8 \*pucDictionaryPath,

UNSIGNED16 usEncrypt,

UNSIGNED8 \*pucDescription,

ADSHANDLE \*phAdminConn );

Parameters

| pucDictonaryPath (I) | Full file path of the data dictionary to create. |
| usEncrypt (I) | A non-zero value will cause the data dictionary data file to be encrypted. |
| pucDescription (I) | An optional description of the database in the data dictionary. If NULL, no database description is stored in the data dictionary. The database description can be added or changed later with [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.md). |
| phAdminConn (O) | Returns a database connection) handle if the data dictionary is created successfully. |

Special Return Codes

| AE\_NO\_DRIVE\_CONNECTION | An Advantage server could not be located for the indicated path. |
| AE\_DICTIONARY\_ALREADY\_EXISTS | An Advantage data dictionary already exists at the indicated path. |

Remarks

AdsDDCreate connects to the Advantage Database Server or Advantage Local Server at the supplied path and creates the Advantage Data Dictionary file. It returns a database connection) if it succeeds. The returned database connection) handle has the administrative access of the ADSSYS user and can be used to modify the contents of the Advantage Data Dictionary. Examples of APIs that modify the data dictionary are all AdsDDSet\*\*\*\*\* functions, [AdsDDAddUserToGroup](ace_adsddaddusertogroup.md), and [AdsDDDeleteIndex](ace_adsdddeleteindex.md).

This call obeys the default server types that may have been set by the ADS.INI file or by calling [AdsSetServerType](ace_adssetservertype.md).

If a non-zero value is specified in the usEncrypt parameter, an encrypted data dictionary file is created. If the usEncrypt is zero, the data dictionary is not encrypted. Even if the data dictionary file is not encrypted, all security related information in the data dictionary, such as user and table passwords are automatically encrypted using 160-bit encryption. An encrypted data dictionary file provides extra security by also storing the uncritical information such as table names and user names in scrambled format. However, there may be some performance degradation when using an encrypted data dictionary file. If security of the information in the data dictionary is a high priority, it is recommended that the data dictionary file be placed in a location that is only accessible by authorized personnel.

If successful, the data dictionary is created with no administrative password and no user access control. The administrative password can be defined later by calling the function [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.md). See [AdsConnect60](ace_adsconnect60.md) for information about data dictionary administrative passwords. User authentication and access control can be added by defining users in the data dictionary and setting the database properties, ADS\_DD\_LOG\_IN\_REQUIRED and ADS\_DD\_VERIFY\_ACCESS\_RIGHTS, to appropriate values. See [AdsDDAddUserToGroup](ace_adsddaddusertogroup.md), [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.md), [AdsDDGrantPermission](ace_adsddgrantpermission.md), [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md), and [AdsConnect60](ace_adsconnect60.md) for information on how user access control works with data dictionary. A data dictionary with no administrative password or user access control is useful if the security of the data is not of concern, but other advanced database functionality such as referential integrity and using NTX files with the Advantage SQL engine are required.

Note AdsDDCreate can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

Create a data dictionary without encrypting the data dictionary data files, and then add a table to the database.

AdsDDCreate( "n:\\MyData\\myData.ADD", 0, "This is the database of my tables and indexes.", &hDD );

AdsDDAddTable( hDD, "Customer Information", "n:\\MyData\\customer.ADT", ADS\_ADT, "customer.adi;customer2.adi",

"This table contains information on all customers." )

See Also

[AdsDDCreate101](ace_adsddcreate101.md)

[AdsConnect60](ace_adsconnect60.md)

[AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.md)

[AdsDDGetDatabaseProperty](ace_adsddgetdatabaseproperty.md)

[AdsDDAddTable](ace_adsddaddtable.md)

[AdsDDAddIndexFile](ace_adsddaddindexfile.md)

[AdsDDCreateUser](ace_adsddcreateuser.md)

[AdsDDDeleteUser](ace_adsdddeleteuser.md)

[AdsDDCreateUserGroup](ace_adsddcreateusergroup.md)

[AdsDDDeleteUserGroup](ace_adsdddeleteusergroup.md)

[AdsDDAddUserToGroup](ace_adsddaddusertogroup.md)

[AdsDDRemoveUserFromGroup](ace_adsddremoveuserfromgroup.md)

[AdsDDGrantPermission](ace_adsddgrantpermission.md)

[AdsDDRevokePermission](ace_adsddrevokepermission.md)
