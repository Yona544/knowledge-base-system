DROP PACKAGE




Advantage Database Server 12  

DROP PACKAGE

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DROP PACKAGE  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - DROP PACKAGE Advantage SQL Engine master\_Drop\_package Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| DROP PACKAGE  Advantage SQL Engine |  |  |  |  |

Removes a package and its functions from the database.

Syntax

DROP PACKAGE package\_name

 

package\_name ::= identifier

 

Remark

The DROP PACKAGE statement removes the specified package from the database the database. All functions owned by the package are also removed.

The user must have the DROP permission on the specified package (see [GRANT](master_grant.htm)).

Example

DROP PACKAGE StringFunctions;

 

See Also

[ALTER FUNCTION](master_alter_function.htm)

[CREATE FUNCTION](master_create_function.htm)

[CREATE PACKAGE](master_create_package.htm)

[DROP FUNCTION](master_drop_function.htm)

[Effective Permissions](master_effective_permissions_vs_explicit_permissions.htm)