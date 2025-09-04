sp\_GetApplicationID




Advantage Database Server 12  

sp\_GetApplicationID

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_GetApplicationID  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_GetApplicationID Advantage SQL Engine master\_Sp\_getapplicationid Advantage SQL > System Procedures > Procedures > sp\_GetApplicationID / Dear Support Staff, |  |
| sp\_GetApplicationID  Advantage SQL Engine |  |  |  |  |

Retrieve the current connection's Application ID.

Syntax

sp\_GetApplicationID( )

Parameters

None

Output

The sp\_GetApplicationID procedure returns a result set of one column and one row containing the Application ID in a memo field.

Remarks

The sp\_GetApplicationID system procedure returns the Application ID of the connection that executed it. The Application ID is initialized to be the file name of the application (executable) that created the connection.

Note Only ACE based clients initialize the Application ID.

See Also

[sp\_SetApplicationID](master_sp_setapplicationid.htm)