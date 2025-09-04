APPLICATIONID()




Advantage Database Server 12  

APPLICATIONID()

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| APPLICATIONID()  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - APPLICATIONID() Advantage Concepts master\_applicationid Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| APPLICATIONID()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.htm) function to retrieve the Application ID of the connection.

|  |  |
| --- | --- |
| Supported in SQL: | Yes |
| Supported in Navigational: | No |

Syntax

APPLICATIONID( ) à cAppID

Parameters

|  |  |
| --- | --- |
| None |  |

Return Value

The application ID for the current connection.

Remarks

The Application ID is initialized by default to the file name of the application (executable) that connected to the Advantage Database Server (only for ACE based clients). The Application ID can be set and retrieved using the sp\_SetApplicationID and sp\_GetApplicationID system procedures.

See Also

[sp\_SetApplicationID](master_sp_setapplicationid.htm)

[sp\_GetApplicationID](master_sp_getapplicationid.htm)

[DATABASE()](master_database.htm)

[USER()](master_user.htm)