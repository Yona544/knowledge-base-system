CREATE FUNCTION




Advantage Database Server 12  

CREATE FUNCTION

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CREATE FUNCTION  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - CREATE FUNCTION Advantage SQL Engine master\_Create\_function Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| CREATE FUNCTION  Advantage SQL Engine |  |  |  |  |

Creates a new function in the database.

Syntax

CREATE FUNCTION [package\_name.]function\_name( [parameter, ] )

RETURNS data-type

[DESCRIPTION function\_description]

BEGIN sql-script END

 

package\_name ::= identifier

function\_name ::= identifier

parameter ::= identifier data-type

function\_description ::= string-literal

sql-script ::= declare\_statements;statement\_block | statement\_block

 

Remark

The CREATE FUNCTION statement can be used to create a [User Defined Function](master_user_defined_function.htm) (UDF) in the database. The function is stored entirely inside the Advantage Data Dictionary file.

The connected user must have the CREATE FUNCTION permission to create a function (see [GRANT](master_grant.htm)).

The optional package\_name can be used to put the function in the specified package or function group. Packages provide independent name spaces for the functions, allowing functions with identical name to exist in different packages. To create the function in the specified package, the package must exist in the database (see [CREATE PACKAGE](master_create_package.htm)) and the connected user must have the ALTER permission over the package (see [GRANT](master_grant.htm)). Functions in a package do not have individual permissions. A users permission on the functions in the package is derived from the users permission on the package.

The parameters can be any data type that is supported in an SQL script (see [DECLARE](master_declare.htm)) except the cursor type.

The RETURNS clause is used to specify the type of the returned data.

The optional DESCRIPTION clause can be used to store additional comments about the function in the data dictionary.

In the sql-script, the [RETURN](master_return.htm) statement may be used to return the result to the caller.

A UDF, once defined, may be used in the SQL engine like any other native scalar functions supported by the Advantage SQL engine. The only difference in the usage between a UDF and a native function is that the user must have the execute permission on the UDF to evaluate it.

Example

|  |  |
| --- | --- |
| 1. | A simple function that returns a concatenated full name. |

CREATE FUNCTION FullName( lastname char(15), firstname char(15))

RETURNS char(31)

DESCRIPTION 'This function constructs comma separated name with blanks trimmed'

BEGIN

RETURN Trim(lastname)+','+Trim(firstname);

END;

 

Sample usage of the function:

SELECT FullName( lastname, firstname ) FROM customers

 

|  |  |
| --- | --- |
| 2. | Creating functions in a package. |

CREATE PACKAGE Local

DESCRIPTION 'Functions returning locally formatted string.';

 

// pad the string with zero or truncate it so it's length is

// equal to the specified length

CREATE FUNCTION local.ZeroPadI2Str( i Integer, len integer )

RETURNS String

BEGIN

DECLARE curr\_len Integer;

DECLARE str String;

 

Str = Trim( Convert( i, SQL\_CHAR ));

curr\_len = length( str );

 

if curr\_len < len then

return repeat( '0', len - curr\_len ) + str;

elseif curr\_len > len then

return left( str, len );

end;

 

return str;

end;

 

// This function returns a date in a string format that is

// traditionally used in the United State

CREATE FUNCTION Local.strDate( dDate Date )

RETURNS Char( 10 )

BEGIN

RETURN Local.ZeroPadI2Str( Month( dDate ), 2 ) + '/' +

Local.ZeroPadI2Str( DayOfMonth( dDate ), 2 ) + '/' +

Local.ZeroPadI2Str( Year( dDate ), 4 );

END

 

Sample usage of the function:

SELECT Local.StrDate( CURDATE() ) FROM system.iota

See Also

[ALTER FUNCTION](master_alter_function.htm)

[CREATE PACKAGE](master_create_package.htm)

[DROP FUNCTION](master_drop_function.htm)

[DROP PACKAGE](master_drop_package.htm)

[Effective Permissions](master_effective_permissions_vs_explicit_permissions.htm)