Advantage Data Dictionary User Permissions




Advantage Database Server 12  

Advantage Data Dictionary User Permissions

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Data Dictionary User Permissions  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Advantage Data Dictionary User Permissions Advantage Concepts master\_Advantage\_data\_dictionary\_user\_permissions Advantage Concepts > Advantage Functionality > Advantage Data Dictionary User Permissions / Dear Support Staff, |  |
| Advantage Data Dictionary User Permissions  Advantage Concepts |  |  |  |  |

The Advantage Data Dictionary implements its own level of user permissions. Each user added to the Advantage Data Dictionary can be granted or revoked permissions to access, update, remove, or create objects such as tables, stored procedures, referential integrity, etc. User groups (roles) can be defined in the database to give users effective permissions based on their user group membership (see [Effective Permissions vs Explicit Permissions](master_effective_permissions_vs_explicit_permissions.htm)).

Note To enforce user permissions, the ADS\_DD\_VERIFY\_ACCESS\_RIGHTS database property must be set to TRUE. This property can be set using the AdsDDSetDatabaseProperty API or using the Advantage Database Manager in Advantage Data Architect (see the Check User Rights check box on the database properties screen). See AdsDDSetDatabaseProperty for more information.

ADSSYS

All Advantage data dictionaries contain an administrative user called ADSSYS. This user has permissions to perform any operation or update on the dictionary. Be aware that if the ADSSYS password is lost, it cannot be recovered or reset.

Normal User Permissions

Most users only need permissions to perform basic operations on a database object (table, stored procedure, dictionary link, etc). These permissions include READ, UPDATE, INSERT, DELETE, EXECUTE, LINK\_ACCESS and INHERIT. See the table below to determine which permission applies to each database object.

Administrative Permissions

Normal users can be granted ALTER, CREATE, DROP, and WITH GRANT permissions to be able to perform administrative operations on an Advantage Data Dictionary. Only a user with the WITH GRANT permission can grant the permission to another user. For example:

User A can only grant READ permissions to user B if User A already have both READ and WITH GRANT permissions on the specific database object.

WITH GRANT permissions can only be granted to a user or group in addition to another permission. For example, if a user is given READ WITH GRANT permissions, by default the user will have READ permissions whether they did before or not.

Database Permissions

Listed here are all available permissions for users and user groups. See [AdsDDGrantPermission](ace_adsddgrantpermission.htm) or SQL [GRANT](master_grant.htm)/[REVOKE](master_revoke.htm) for more information about each permission.

Users and User Groups

|  |  |
| --- | --- |
| Permisssion | Description |
| ADS\_PERMISSION\_READ | Allows users to read records from the specified table. |
| ADS\_PERMISSION\_UPDATE | Allows users to update records in the specified table. |
| ADS\_PERMISSION\_EXECUTE | Allows users to execute the specified stored procedure. |
| ADS\_PERMISSION\_INHERIT | Allows permissions granted to groups to be inherited by the group member. User inherits the permission from the user groups by default but the inheritance to a specific database object may be granted or revoked by the ADSSYS user or members of the DB:Admin group. |
| ADS\_PERMISSION\_INSERT | Allows users to insert records into the specified table. |
| ADS\_PERMISSION\_DELETE | Allows users to delete records from the specified table. |
| ADS\_PERMISSION\_LINK\_ACCESS | Allows users to access the specified data dictionary link. |
| ADS\_PERMISSION\_CREATE | Allows users to create objects of the specified type. |
| ADS\_PERMISSION\_ALTER | Allows users to alter the specified database object. |
| ADS\_PERMISSION\_DROP | Allows users to drop or remove the specified database object. |
| ADS\_PERMISSION\_WITH\_GRANT | Allows users to grant the specified permission to other users. |
| ADS\_PERMISSION\_ALL\_WITH\_GRANT | Specifies all applicable permissions along with WITH GRANT. |
| ADS\_PERMISSION\_ALL | Specifies all applicable permissions for the database object. |

Administrative Operation

The table below shows what permissions are required to perform administrative operations on the database or database objects.

|  |  |  |  |
| --- | --- | --- | --- |
| Object Type | Create | Delete | Modify |
| Table | CREATE TABLE | DROP on the table | ALTER on the table |
| Relation | ALTER on related tables | ALTER on related tables | ALTER on related tables |
| Index File | ALTER on parent table | ALTER on parent table | ALTER on parent table |
| Field | ALTER on parent table | ALTER on parent table | ALTER on parent table |
| Index | ALTER on parent table | ALTER on parent table | ALTER on parent table |
| View | CREATE VIEW | DROP on the view | ALTER on the view |
| User | CREATE USER | DROP on the user | ALTER on the user |
| User Group | CREATE USER GROUP | DROP on the group | ALTER on the group |
| Procedure | CREATE PROCEDURE | DROP on the procedure | ALTER on the procedure |
| Function | CREATE FUNCTION | DROP on the function | ALTER on the function or ALTER on the package containing the function |
| Package | CREATE PACKAGE | DROP on the package | ALTER on the package |
| Database |  |  | ALTER DATABASE |
| Link | CREATE LINK | DROP on the link | ALTER on the link |
| Trigger | ALTER on parent table and  CREATE PROCEDURE | ATLER on parent table | ALTER on parent table and  CREATE PROCEDURE |
| Publication | CREATE PUBLICATION | DROP on the publication | ALTER on the publication |
| Article | ALTER on the parent publication | ALTER on the parent publication | ALTER on the parent publication |
| Subscription | CREATE SUBSCRIPTION | DROP on the subscription | ALTER on the subscription |

Object Properties

Below are tables that show what permissions are required to read or update database object properties.

Database Properties

|  |  |  |
| --- | --- | --- |
| Property | Read | Update |
| ADS\_DD\_COMMENT |  | ALTER |
| ADS\_DD\_VERSION\_MAJOR |  | ALTER |
| ADS\_DD\_VERSION\_MINOR |  | ALTER |
| ADS\_DD\_USER\_DEFINED\_PROP |  | ALTER |
| ADS\_DD\_DEFAULT\_TABLE\_PATH |  | ALTER |
| ADS\_DD\_TEMP\_TABLE\_PATH |  | ALTER |
| ADS\_DD\_FTS\_DELIMITERS |  | ALTER |
| ADS\_DD\_FTS\_NOISE |  | ALTER |
| ADS\_DD\_FTS\_DROP\_CHARS |  | ALTER |
| ADS\_DD\_FTS\_CONDITIONAL\_CHARS |  | ALTER |
| ADS\_DD\_ENCRYPTED | ALTER | ALTER |
| ADS\_DD\_LOG\_IN\_REQUIRED | ALTER | ALTER |
| ADS\_DD\_VERIFY\_ACCESS\_RIGHTS | ALTER | ALTER |
| ADS\_DD\_ENCRYPT\_TABLE\_PASSWORD | ALTER | ALTER |
| ADS\_DD\_ENCRYPT\_NEW\_TABLE | ALTER | ALTER |
| ADS\_DD\_ADMIN\_PASSWORD | ADSSYS only | ADSSYS only |
| ADS\_DD\_ALLOW\_ADSSYS\_NET\_ACCESS | ADSSYS only | ADSSYS only |
| ADS\_DD\_ENABLE\_INTERNET | ALTER | ALTER |
| ADS\_DD\_INTERNET\_SECURITY\_LEVEL | ALTER | ALTER |
| ADS\_DD\_MAX\_FAILED\_ATTEMPTS | ALTER | ALTER |
| ADS\_DD\_LOGINS\_DISABLED | ALTER | ALTER |
| ADS\_DD\_LOGINS\_DISABLED\_ERRSTR | ATLER | ALTER |

Table Properties

|  |  |  |
| --- | --- | --- |
| Property | Read | Update |
| ADS\_DD\_COMMENT | READ, UPDATE, INSERT, or DELETE (any or all columns) | ALTER |
| ADS\_DD\_USER\_DEFINED\_PROP | READ, UPDATE, INSERT, or DELETE (any or all columns) | ALTER |
| ADS\_DD\_TABLE\_PRIMARY\_KEY | READ, UPDATE, INSERT, or DELETE (any or all columns) | ALTER |
| ADS\_DD\_TABLE\_ENCRYPTION | READ, UPDATE, INSERT, or DELETE (any or all columns) | ALTER |
| ADS\_DD\_TABLE\_DEFAULT\_INDEX | READ, UPDATE, INSERT, or DELETE (any or all columns) | ALTER |
| ADS\_DD\_TABLE\_TYPE | READ, UPDATE, INSERT, or DELETE (any or all columns) | NA |
| ADS\_DD\_TABLE\_FIELD\_COUNT | READ, UPDATE, INSERT, or DELETE (any or all columns) | NA |
| ADS\_DD\_TABLE\_VALIDATION\_EXPR | ALTER, UPDATE, or INSERT | ALTER |
| ADS\_DD\_TABLE\_VALIDATION\_MSG | ALTER, UPDATE, or INSERT | ALTER |
| ADS\_DD\_TABLE\_IS\_RI\_PARENT | ALTER | ALTER |
| ADS\_DD\_TABLE\_AUTO\_CREATE | ALTER | ALTER |
| ADS\_DD\_TABLE\_PERMISSION\_LEVEL | ALTER | ALTER |
| ADS\_DD\_TABLE\_MEMO\_BLOCK\_SIZE | ALTER | ALTER |
| ADS\_DD\_TABLE\_IS\_RI\_PARENT | ALTER | NA |

Field Properties

Note Field permissions are derived from table permissions. To update field properties, the user must have ALTER permissions on the table that contains the field.

|  |  |  |
| --- | --- | --- |
| Property | Read | Update |
| ADS\_DD\_COMMENT | READ, UPDATE, INSERT, or DELETE on the field | ALTER on the table |
| ADS\_DD\_USER\_DEFINED\_PROP | READ, UPDATE, INSERT, or DELETE on the field | ALTER on the table |
| ADS\_DD\_FIELD\_LENGTH | READ, UPDATE, INSERT, or DELETE on the field | NA |
| ADS\_DD\_FIELD\_TYPE | READ, UPDATE, INSERT, or DELETE on the field | NA |
| ADS\_DD\_FIELD\_DECIMAL | READ, UPDATE, INSERT, or DELETE on the field | NA |
| ADS\_DD\_FIELD\_OPTIONS | READ, UPDATE, INSERT, or DELETE on the field | NA |
| ADS\_DD\_FIELD\_DEFAULT\_VALUE | ALTER on the table, or UPDATE or INSERT on the field | ALTER on the table |
| ADS\_DD\_FIELD\_CAN\_NULL | ALTER on the table, or UPDATE or INSERT on the field | ALTER on the table |
| ADS\_DD\_FIELD\_MIN\_VALUE | ALTER on the table, or UPDATE or INSERT on the field | ALTER on the table |
| ADS\_DD\_FIELD\_MAX\_VALUE | ALTER on the table, or UPDATE or INSERT on the field | ALTER on the table |
| ADS\_DD\_FIELD\_VALIDATION\_MSG | ALTER on the table, or UPDATE or INSERT on the field | ALTER on the table |

Index File Properties

Note Index file permissions are derived from table permissions. To update index file properties, the user must have ALTER permissions on the table that the index file is associated.

|  |  |  |
| --- | --- | --- |
| Property | Read | Update |
| ADS\_DD\_INDEX\_FILE\_PATH | READ, UPDATE, INSERT, or DELETE (any or all columns) | NA |
| ADS\_DD\_INDEX\_FILE\_PAGESIZE | READ, UPDATE, INSERT, or DELETE (any or all columns) | NA |

Index Properties

Note Index permissions are derived from table permissions. To update index properties, the user must have ALTER permissions on the table that the index is associated.

|  |  |  |
| --- | --- | --- |
| Property | Read | Update |
| ADS\_DD\_INDEX\_FILE\_NAME | READ, UPDATE, INSERT, or DELETE (any or all columns) | NA |
| ADS\_DD\_INDEX\_KEY\_LENGTH | READ, UPDATE, INSERT, or DELETE (any or all columns) | NA |
| ADS\_DD\_INDEX\_KEY\_TYPE | READ, UPDATE, INSERT, or DELETE (any or all columns) | NA |
| ADS\_DD\_INDEX\_EXPRESSION | ALTER on the table | NA |
| ADS\_DD\_INDEX\_CONDITION | ALTER on the table | NA |
| ADS\_DD\_INDEX\_OPTIONS | ALTER on the table | NA |

Link Properties

|  |  |  |
| --- | --- | --- |
| Property | Read | Update |
| ADS\_DD\_LINK\_PATH | ALTER | ALTER |
| ADS\_DD\_LINK\_OPTIONS | ALTER | ALTER |
| ADS\_DD\_LINK\_USERNAME | ALTER | ALTER |

Procedure Properties

|  |  |  |
| --- | --- | --- |
| Property | Read | Update |
| ADS\_DD\_COMMENT | EXECUTE | ALTER |
| ADS\_DD\_PROC\_INPUT | EXECUTE | ALTER |
| ADS\_DD\_PROC\_OUTPUT | EXECUTE | ALTER |
| ADS\_DD\_PROC\_DLL\_NAME | ALTER | ALTER |
| ADS\_DD\_PROC\_DLL\_FUNCTION\_NAME | ALTER | ALTER |
| ADS\_DD\_PROC\_INVOKE\_OPTION | ALTER | ALTER |

Function Properties (via system.functions)

|  |  |  |
| --- | --- | --- |
| Property | Read | Update |
| Comment | EXECUTE | ALTER |
| Input Parameters | EXECUTE | ALTER |
| Return Type | EXECUTE | ALTER |
| Implementation | ALTER | ALTER |
| Package | EXECUTE | ALTER |

Referential Integrity Properties

Note Referential integrity permissions are derived from table permissions. To update referential integrity properties, the user must have ALTER permissions on the table that the referential integrity is associated.

|  |  |  |
| --- | --- | --- |
| Property | Read | Update |
| ADS\_DD\_RI\_PRIMARY\_TABLE | ALTER on both tables | NA |
| ADS\_DD\_RI\_PRIMARY\_INDEX | ALTER on both tables | NA |
| ADS\_DD\_RI\_FOREIGN\_TABLE | ALTER on both tables | NA |
| ADS\_DD\_RI\_FOREIGN\_INDEX | ALTER on both tables | NA |
| ADS\_DD\_RI\_NO\_PKEY\_ERROR | ALTER on both tables | NA |
| ADS\_DD\_RI\_CASCADE\_ERROR | ALTER on both tables | NA |
| ADS\_DD\_RI\_UPDATERULE | ALTER on both tables | NA |
| ADS\_DD\_RI\_DELETERULE | ALTER on both tables | NA |

User Properties

|  |  |  |
| --- | --- | --- |
| Property | Read | Update |
| ADS\_DD\_COMMENT | Current user or ALTER on user | ALTER |
| ADS\_DD\_USER\_DEFINED\_PROP | Current user or ALTER on user | ALTER |
| ADS\_DD\_USER\_GROUP\_MEMBERSHIP | Current user or ALTER on user | ALTER |
| ADS\_DD\_LOGINS\_DISABLED | Current user or ALTER on user | Current user or ALTER on user |
| ADS\_DD\_USER\_PASSWORD | Current user or ALTER on user | Current user or ALTER on user |
| ADS\_DD\_ENABLE\_INTERNET | Current user or ALTER on user | Current user or ALTER on user |

User Group Properties

|  |  |  |
| --- | --- | --- |
| Property | Read | Update |
| ADS\_DD\_COMMENT | Group member or ALTER on group | ALTER |
| ADS\_DD\_USER\_DEFINED\_PROP | Group member or ALTER on group | ALTER |

View Properties

|  |  |  |
| --- | --- | --- |
| Property | Read | Update |
| ADS\_DD\_COMMENT | READ | ALTER |
| ADS\_DD\_VIEW\_STMT | ALTER | ALTER |
| ADS\_DD\_VIEW\_STMT\_LEN | ALTER | NA |

Trigger Properties

Note Trigger permissions are derived from table permissions. To update a trigger property, the user must have ALTER permissions on the table that the trigger is associated.

|  |  |  |
| --- | --- | --- |
| Property | Read | Update |
| ADS\_DD\_TRIG\_TABLEID | ALTER on the table | NA |
| ADS\_DD\_TRIG\_EVENT\_TYPE | ALTER on the table | NA |
| ADS\_DD\_TRIG\_TRIGGER\_TYPE | ALTER on the table | NA |
| ADS\_DD\_TRIG\_CONTAINER\_TYPE | ALTER on the table | NA |
| ADS\_DD\_TRIG\_CONTAINER | ALTER on the table | NA |
| ADS\_DD\_TRIG\_FUNCTION\_NAME | ALTER on the table | NA |
| ADS\_DD\_TRIG\_PRIORITY | ALTER on the table | NA |
| ADS\_DD\_TRIG\_OPTIONS | ALTER on the table | NA |
| ADS\_DD\_TRIG\_TABLENAME | ALTER on the table | NA |

Publication Properties

|  |  |  |
| --- | --- | --- |
| Property | Read | Update |
| ADS\_DD\_PUBLICATION\_OPTIONS | ALTER | ALTER |

Article Properties

Note Article permissions are derived from publication permissions. To update an article property, the user must have ALTER permissions on the publication that contains the article.

|  |  |  |
| --- | --- | --- |
| Property | Read | Update |
| ADS\_DD\_ARTICLE\_FILTER | ALTER on publication | ALTER on publication |
| ADS\_DD\_ARTICLE\_ID\_COLUMNS | ALTER on publication | ALTER on publication |

Subscription Properties

|  |  |  |
| --- | --- | --- |
| Property | Read | Update |
| ADS\_DD\_SUBSCR\_PUBLICATION\_NAME | ALTER | ALTER |
| ADS\_DD\_SUBSCR\_TARGET | ALTER | ALTER |
| ADS\_DD\_SUBSCR\_USERNAME | ALTER | ALTER |
| ADS\_DD\_SUBSCR\_PASSWORD | ALTER | ALTER |
| ADS\_DD\_SUBSCR\_FORWARD | ALTER | ALTER |
| ADS\_DD\_SUBSCR\_ENABLED | ALTER | ALTER |
| ADS\_DD\_SUBSCR\_QUEUE\_NAME | ALTER | ALTER |
| ADS\_DD\_SUBSCR\_OPTIONS | ALTER | ALTER |

See Also

[Effective Permissions vs Explicit Permissions](master_effective_permissions_vs_explicit_permissions.htm)

[Database Roles](master_database_base_roles.htm)