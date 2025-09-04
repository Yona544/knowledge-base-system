AdsConnection.State




Advantage Database Server 12  

AdsConnection.State

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnection.State  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnection.State Advantage .NET Data Provider dotnet\_Adsconnection\_state Advantage .NET Data Provider > AdsConnection Class > AdsConnection Properties > AdsConnection.State / Dear Support Staff, |  |
| AdsConnection.State  Advantage .NET Data Provider |  |  |  |  |

Gets the current state of the connection.

public ConnectionState State {get;}

Remarks

Gets the current state of the connection. It returns either ConnectionState.Open (if the connection to Advantage Database Server or Advantage Local Server is active) or ConnectionState.Closed if there is no active connection.

This property is defined to return a bitwise combination ConnectionState enumeration values. Currently, the Advantage .NET Data Provider uses only the Open and Closed values; the remaining values are reserved for future use by Microsoft. For best compatibility with future versions, you should check the values as a bitmask.

Example

if (( conn.State & ConnectionState.Open ) == 0 )

// It is not open

conn.Open();

See Also

[AdsConnection.Open](dotnet_adsconnection_open.htm)

[AdsConnection.Close](dotnet_adsconnection_close.htm)