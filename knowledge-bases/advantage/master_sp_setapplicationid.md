sp\_SetApplicationID




Advantage Database Server 12  

sp\_SetApplicationID

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_SetApplicationID  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_SetApplicationID Advantage SQL Engine master\_Sp\_setapplicationid Advantage SQL > System Procedures > Procedures > sp\_SetApplicationID / Dear Support Staff, |  |
| sp\_SetApplicationID  Advantage SQL Engine |  |  |  |  |

Set the current connection's Application ID.

Syntax

sp\_SetApplicationID( ApplicationID, MEMO )

Parameters

|  |  |
| --- | --- |
| ApplicationID (I) | New Application ID to be used for the current connection. |

Output

None

Remarks

The sp\_SetApplicationID system procedure sets the Application ID of the connection that executed it. The Application ID is initialized to be the file name of the application (executable) that created the connection.

Note Only ACE based clients initialize the Application ID.

See Also

[sp\_GetApplicationID](master_sp_getapplicationid.htm)