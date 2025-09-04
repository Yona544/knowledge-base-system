REVOKE




Advantage Database Server 12  

REVOKE

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| REVOKE  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - REVOKE Advantage SQL Engine master\_Revoke Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| REVOKE  Advantage SQL Engine |  |  |  |  |

Revoke permissions from a user or user group

Syntax

REVOKE [GRANT OPTION FOR] <permission [, n]> [ON <object>] FROM <grantee>

permission ::= SELECT | SELECT( columnname ) | INSERT | INSERT( columnname ) | UPDATE | UPDATE( columnname ) | ACCESS | ALL | ALTER [DATABASE] | DELETE | DROP | EXECUTE | INHERIT [DATABASE] | <create permission>

create permission ::= [INHERIT] CREATE <create object>

create object ::= TABLE | USER [GROUP] | VIEW | PROCEDURE | LINK | PUBLICATION | SUBSCRIPTION | FUNCTION | PACKAGE

object ::= viewname | tablename | procedurename | linkname | publicationname | subscriptionname | packagename | functionname

grantee ::= username | groupname

Remarks

REVOKE revokes a permission or permissions on a database object from a user or user group.

See [GRANT](master_grant.htm) or AdsDDGrantPermission (in the Advantage Client Engine Help documentation) for more information on database permissions.

Object permissions such as SELECT, ACCESS, and INHERIT require the ON OBJECT clause to specify which object the permissions apply to. Database wide permissions such as CREATE and ALTER DATABASE do not apply to any existing database object and thus must not include the ON OBJECT clause. Furthermore, object and database wide permissions cannot be revoked within the same SQL statement. For example

REVOKE CREATE TABLE, SELECT ON customers FROM sales\_group

is not a valid statement. These permissions must be broken up into two statements such as:

REVOKE CREATE TABLE FROM sales\_group

REVOKE SELECT ON customers FROM sales\_group

The GRANT OPTION FOR clause is used to revoke the WITH GRANT permission from a grantee. Note this will only revoke the WITH GRANT permission, not the object permission itself. To revoke both simply revoke the object permission, which will automatically revoke the WITH GRANT permission as well.

The INHERIT modifier for CREATE permissions will only revoke the INHERIT permission for the specified CREATE permission. It does not affect the grantees CREATE permission itself.

By specifying the WITH GRANT clause in the statement, the grantee will be able to grant the specified permissions to other users.

Note The ALL permission equates to all the permissions for which the current user has WITH GRANT permissions.

The following table describes the available permissions and valid usage in the statement.

|  |  |  |
| --- | --- | --- |
| Permission | Applicable to Object Type | Description |
| SELECT | Table, Table( column, ) or View | This permission allows the grantee to read data from the table or view. If TableName( column, ) is specified, the read access is granted to the specified columns in the table. |
| UPDATE | Table, Table( column, ) or View | This permission allows the grantee to modify existing data in the table or view. If TableName( column, ) is specified, the user is allowed to modify the specified columns in the table. |
| INSERT | Table, Table( column, ) or View | This permission allows the grantee to insert new records into the table or view. If the TableName( column, ) is specified, the user is allowed to provide the initial value to the specified columns in the table. |
| DELETE | Table or View | This permission allows the grantee to delete existing records from the table or view. |
| EXECUTE | Stored Procedure, User Defined Function or Package | This permission allows the grantee to execute the specified stored procedure, function, or functions in the specified package. |
| ACCESS | Data Dictionary Link | This permission allows the grantee to access the specified link. The permissions to the tables in the link are still verified by the target data dictionary against the credential of the linked user. |
| ALTER | Table, view, stored procedure, function, package, data dictionary link, publication, subscription, user or user group | This permission allows the grantee to change the meta data associated with the specified object. It is one the administrative permissions. |
| DROP | Table, view, stored procedure, function, package, data dictionary link, publication, subscription, user or user group | This permission allows the grantee to removed the specified object from the database. It is one of the administrative permissions. |
| INHERIT | Table, view, stored procedure, function, package, data dictionary link, publication, subscription, user or user group | This permission can only be granted to a user. It is granted to the user by default. The permission allows the user to inherit permission on the specified object from the user groups that the user is a member of. See [Effective Permissions](master_effective_permissions_vs_explicit_permissions.htm). |
| CREATE TABLE,  CREATE VIEW,  CREATE USER,  CREATE USER GROUP, CREATE PROCEDURE,  CREATE PUBLICATION,  CREATE SUBSCRIPTION,  CREATE FUNCTION,  CREATE PACKAGE |  | Each permission allows the grantee to create an object of the specified type in the database. These permissions should be considered administrative permissions. |
| ALTER DATABASE |  | This permission allows the grantee to modify the meta data of the database object, i.e., global settings of the database. It does not give permission to modify meta data of the individual objects in the database. |

Example(s)

REVOKE SELECT ON customers FROM sales\_group

REVOKE INSERT( accounts ) ON customers FROM user1

REVOKE ALL ON customers FROM managers

REVOKE GRANT OPTION FOR CREATE TABLE FROM user1

GRANT EXECUTE ON MyFunction TO user1

GRANT EXECUTE, ALTER ON MyConvPack TO super\_users

See Also

[GRANT](master_grant.htm)

[System permissions](master_system_permissions.htm)