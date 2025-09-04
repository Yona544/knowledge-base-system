ALTER FUNCTION




Advantage Database Server 12  

ALTER FUNCTION

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ALTER FUNCTION  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - ALTER FUNCTION Advantage SQL Engine master\_Alter\_function Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ALTER FUNCTION  Advantage SQL Engine |  |  |  |  |

Modifies the name or definition of a function. The existing permissions on the function are maintained.

Syntax

ALTER FUNCTION [package\_name.]function\_name [new\_function\_name]

( [parameter, ] )

[RETURNS data-type | NULL]

[DESCRIPTION string]

BEGIN sql-script END

 

package\_name ::= identifier

function\_name ::= identifier

new\_function\_name ::= function\_name | package\_name.function\_name

parameter ::= identifier data-type

sql-script ::= declare\_statements;statement\_block | statement\_block

 

Remark

The ALTER FUNCTION statement has the identical syntax as the [CREATE FUNCTION](master_create_function.htm) statement except for the first word and the optional new\_function\_name.

It allows the function to be modified without having to re-grant the permissions to users. If the function is dropped and recreated, then the permissions must be re-granted to the user who had permission on the function.

The optional new\_function\_name may be used to change the name of the function. A package\_name may be specified as part of the new\_function\_name but it must match the existing package name. ALTER FUNCTION cannot be used to change the package ownership of the function.

To alter a function that is not owned by any package, the user must have the ALTER permission over the function. To alter a function that is owned by a package, the user must have the ALTER permission over the package.

Example

|  |  |
| --- | --- |
| 1. | ALTER FUNCTION without changing the function name |

ALTER FUNCTION FullName( lastname char(15), firstname char(15))

RETURNS char(31)

DESCRIPTION 'This function constructs a conventional name with blanks trimmed'

BEGIN

RETURN Trim(firstname) + ' ' + Trim(lastname);

END;

 

|  |  |
| --- | --- |
| 2. | Changing the name of a function |

// Correct the spelling of the function name

ALTER FUNCTION local.squar square( i Integer )

RETURNS integer

BEGIN

return i \* i;

end;

See Also

[CREATE FUNCTION](master_create_function.htm)

[CREATE PACKAGE](master_create_package.htm)

[DROP FUNCTION](master_drop_function.htm)

[DROP PACKAGE](master_drop_package.htm)

[Effective Permissions](master_effective_permissions_vs_explicit_permissions.htm)