AdsConnection.ConnectionHandle




Advantage Database Server 12  

AdsConnection.ConnectionHandle

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnection.ConnectionHandle  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnection.ConnectionHandle Advantage .NET Data Provider dotnet\_Adsconnection\_connectionhandle Advantage .NET Data Provider > AdsConnection Class > AdsConnection Properties > AdsConnection.ConnectionHandle / Dear Support Staff, |  |
| AdsConnection.ConnectionHandle  Advantage .NET Data Provider |  |  |  |  |

Returns the internal handle used by the Advantage Client Engine.

public IntPtr ConnectionHandle {get;}

Remarks

This handle is currently only used internally by the Advantage Data Provider. It is publicly accessible for possible future enhancements.

Note The AdsConnection must be open when getting the ConnectionHandle.