DROP FUNCTION




Advantage Database Server 12  

DROP FUNCTION

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DROP FUNCTION  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - DROP FUNCTION Advantage SQL Engine master\_Drop\_function Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| DROP FUNCTION  Advantage SQL Engine |  |  |  |  |

Removes a function from the database.

Syntax

DROP FUNCTION [package\_name.]function\_name

 

package\_name ::= identifier

function\_name ::= identifier

 

Remark

The DROP FUNCTION statement is used to remove a function from the database.

To remove a function that is not owned by any package, the user must have the DROP permission over the function. To remove a function that is owned by a package, the user must have the ALTER permission over the package.

Example

DROP FUNCTION test1;

DROP FUNCTION TestPack.test1;

 

See Also

[ALTER FUNCTION](master_alter_function.htm)

[CREATE FUNCTION](master_create_function.htm)

[CREATE PACKAGE](master_create_package.htm)

[DROP PACKAGE](master_drop_package.htm)

[Effective Permissions](master_effective_permissions_vs_explicit_permissions.htm)