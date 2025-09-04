Effects of Upgrading to Version 11




Advantage Database Server 12  

Effects of Upgrading to Version 11

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Effects of Upgrading to Version 11  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Effects of Upgrading to Version 11 Advantage Database Server master\_Effect\_of\_Upgrading\_to\_Version11 Advantage Database Server > Introduction > Effects of Upgrading to Version 11 / Dear Support Staff, |  |
| Effects of Upgrading to Version 11  Advantage Database Server |  |  |  |  |

Changing Current User Password Now Requires Existing Password

The default behavior for changing current user password has been changed to require existing user password. A new system stored procedure, [sp\_ChangeCurrentUserPassword](master_sp_changecurrentuserpassword.htm), is provided to facilitate this this new behavior. This change in behavior provides additional security to user accounts. For backward compatibility, a new user property is available to return the user account to the pre-version 11.0 behavior.

The % character is now considered to be a special character in SQL engine

The % character is now the modulo operator in the SQL engine. If an identifier, such as table name or column name, contains the % character, the identifier must now be delimited with either double quotes or square brackets in the SQL statement.

The \_ character is no longer allowed to be the leading character for stored procedure input parameter name

The \_ (underscore) character was not allowed as the leading character of the name of declared variable, however, the input parameters of stored procedure were allowed to have the leading underscore for the names. In version 11, when creating new stored procedure, the leading underscore will no longer be allowed in the input parameter names. Existing stored procedure with such input parameter names will still function correctly except when the names are \_errcode, \_errclass, or \_errtext. If the stored procedure has input parameters named \_errcode, \_errclass, or \_errtext, an error will be returned when trying to execute the stored procedure.

Potential 2229 error being returned from existing SQL script procedure when there is an explicit reference to a table column with name beginning with the \_ (underscore) character

As a result of changes to allow accessing the stored procedure input parameters using implicitly declared variables, the use of table column names begin with the \_ character may become ambiguous in the SQL script. When the column name is in the form \_xxx and there is an input parameter named xxx, the 2229 error will be returned. This is caused by the implicitly declared input parameter variable having the name \_xxx as well. Changing the input parameter name to @xxx or yyy to avoid the problem.

Changes to System Procedures

|  |  |
| --- | --- |
| · | [sp\_GetSQLStatements](master_sp_getsqlstatements.htm) now requires [DB:Admin](master_database_base_roles.htm) membership and only retrieves statements for the current dictionary. |

|  |  |
| --- | --- |
| · | [sp\_mgKillUser](master_sp_mgkilluser.htm) and AdsMgKillUser now require [DB:Admin or SERVER:Admin](master_database_base_roles.htm) membership. |

NetWare no Longer Supported

The v11.0 release of Advantage does not include support for Novell NetWare.

AdsNullTerminateStrings API is no Longer Supported

The Advantage Client Engine API AdsNullTerminateStrings is no longer supported.