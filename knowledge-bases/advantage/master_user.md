USER()




Advantage Database Server 12  

USER()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| USER()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - USER() Advantage Concepts master\_user Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| USER()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function that returns the user name of the current connection.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

USER() à cUser

Parameters

|  |  |
| --- | --- |
| None |  |

Return Value

The database user name of the connected user

Remarks

For database connections, this function returns the name of the logged in user on the current connection. For free connections, the name returned is the client computer name.

See Also

[APPLICATIONID()](master_applicationid.htm)

[DATABASE()](master_database.htm)