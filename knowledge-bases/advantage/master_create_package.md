CREATE PACKAGE




Advantage Database Server 12  

CREATE PACKAGE

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CREATE PACKAGE  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - CREATE PACKAGE Advantage SQL Engine master\_Create\_package Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| CREATE PACKAGE  Advantage SQL Engine |  |  |  |  |

Creates a new package in the database.

Syntax

CREATE PACKAGE package\_name [DESCRIPTION package\_description]

 

package\_name ::= identifier

package\_description ::= string-literal

 

Remark

The CREATE PACKAGE statement creates a package in the database. Packages provide independent name spaces for the functions in the database. Functions with identical names may exists in the database as long as they are own by different package (see [CREATE FUNCTION](master_create_function.htm)).

The user must have the CREATE PACKAGE permission to create a package in the database (see [GRANT](master_grant.htm)).

Functions in a package do not have individual permissions. A users permission on the functions in the package is derived from the users permission on the package.

Example

 

CREATE PACKAGE StringFunctions;

CREATE PACKAGE MyFunc DESCRIPTION 'My functions';

See Also

[ALTER FUNCTION](master_alter_function.htm)

[CREATE FUNCTION](master_create_function.htm)

[DROP FUNCTION](master_drop_function.htm)

[DROP PACKAGE](master_drop_package.htm)

[Effective Permissions](master_effective_permissions_vs_explicit_permissions.htm)