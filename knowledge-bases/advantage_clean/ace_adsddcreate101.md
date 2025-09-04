---
title: Ace Adsddcreate101
slug: ace_adsddcreate101
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddcreate101.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: c43ce14248f1bef07934f67381903cdae0b99413
---

# Ace Adsddcreate101

AdsDDCreate101

AdsDDCreate101

Advantage Client Engine

| AdsDDCreate101  Advantage Client Engine |  |  |  |  |

Creates a data dictionary using a connection string.

Syntax

UNSIGNED32 AdsDDCreate101( UNSIGNED8 \*pucConnectString,

ADSHANDLE \*phConnectOptions,

ADSHANDLE \*phAdminConn );

Parameters

| pucConnectString (I) | Connection string specifying the new data dictionary path, among other things.  See [AdsConnect101](ace_adsconnect101.md) for a complete list of supported options. |
| phConnectOptions (O) | The handle of an in-memory table that contains the provided connection string options.  Optional, can be NULL. |
| phAdminConn (O) | Returns a database connection) handle if the data dictionary is created successfully. |

Special Return Codes

| AE\_NO\_DRIVE\_CONNECTION | An Advantage server could not be located for the indicated path. |
| AE\_DICTIONARY\_ALREADY\_EXISTS | An Advantage data dictionary already exists at the indicated path. |

Remarks

AdsDDCreate101 connects to the Advantage Database Server or Advantage Local Server at the supplied Data Source path and creates the Advantage Data Dictionary file. It returns a database connection) if it succeeds. The returned database connection) handle has the administrative access of the ADSSYS user and can be used to modify the contents of the Advantage Data Dictionary. Examples of APIs that modify the data dictionary are all AdsDDSet\*\*\*\*\* functions, [AdsDDAddUserToGroup](ace_adsddaddusertogroup.md), and [AdsDDDeleteIndex](ace_adsdddeleteindex.md).

This call will use the ServerType setting specified in the connection string.  Otherwise it obeys the default server types that may have been set by the ADS.INI file or by calling [AdsSetServerType](ace_adssetservertype.md).

If TRUE is specified for the EncryptDictionary connection string option, an encrypted data dictionary file is created. If the EncryptDictionary option is FALSE or not specified, the data dictionary is not encrypted. Even if the data dictionary file is not encrypted, all security related information in the data dictionary, such as user and table passwords are automatically encrypted using the encryption specified by the EncryptionType option. An encrypted data dictionary file provides extra security by because all data in the dictionary such as table and user names will be encrypted. However, there may be some performance degradation when using an encrypted data dictionary file. If security of the information in the data dictionary is a high priority, it is recommended that the data dictionary file be placed in a location that is only accessible by authorized personnel.

In addition, using [AES encryption](master_encryption.md) provides greatly increased security for the dictionary content because it is encrypted with an externally-provided dictionary password ([DDPassword connection](ace_adsconnect101.md) option). When creating a dictionary with AES encryption, the DDPassword is required. The dictionary password is unrelated to the ADSSYS administrative user password. User passwords are used for authentication to the dictionary and to assign rights. The dictionary password is used for table and data dictionary file encryption. It must be provided to the Advantage Database Server the first time it opens the dictionary. It can be provided via the connection string in calls to [AdsConnect101](ace_adsconnect101.md) but should probably be provided at the server in a production environment via the [SE\_Passwords](master_se_passwords.md) configuration parameter.

If the Password connection string option is not specified, the data dictionary is created with no administrative password.  Otherwise, the password specified by the Password option will be the ADSSYS administrative user password for the new data dictionary.  The administrative password can be defined later by calling the function [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.md). See [AdsConnect101](ace_adsconnect101.md) for information about data dictionary administrative passwords.

If successful, the new data dictionary is created with no user access control. User authentication and access control can be added by defining users in the data dictionary and setting the database properties, ADS\_DD\_LOG\_IN\_REQUIRED and ADS\_DD\_VERIFY\_ACCESS\_RIGHTS, to appropriate values. See [AdsDDAddUserToGroup](ace_adsddaddusertogroup.md), [AdsDDSetDatabaseProperty](ace_adsddsetdatabaseproperty.md), [AdsDDGrantPermission](ace_adsddgrantpermission.md), [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md), and [AdsConnect60](ace_adsconnect60.md) for information on how user access control works with data dictionary. A data dictionary with no administrative password or user access control is useful if the security of the data is not of concern, but other advanced database functionality such as referential integrity and using NTX files with the Advantage SQL engine are required.

Note AdsDDCreate101 can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

Create a data dictionary and encrypt the data dictionary data files. Specifying EncryptionType=AES256 means that any table in the dictionary that is encrypted will use 256-bit AES encryption. The DDPassword option is required when using AES encryption because it is used to generate the key data for encrypting tables and the dictionary itself.After a dictionary has been created with AES encryption and is being used in a production environment, it may make sense to specify the dictionary password via the [SE\_Passwords](master_se_passwords.md) configuration option at the server so that it does not have to be provided by the application or user.

AdsDDCreate101( "Data Source=n:\\MyData\\myData.ADD; Password=admin1; DDPassword=ddpass; Description=This is the database of my tables and indexes.; EncryptDictionary=TRUE;EncryptionType=AES256; ", &hOptions, &hDD );

 

See Also

[AdsConnect101](ace_adsconnect101.md)

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
