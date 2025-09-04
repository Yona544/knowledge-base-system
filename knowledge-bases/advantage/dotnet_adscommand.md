AdsCommand




Advantage Database Server 12  

AdsCommand

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommand  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommand Advantage .NET Data Provider dotnet\_Adscommand Advantage .NET Data Provider > AdsCommand Class > Overview / Dear Support Staff, |  |
| AdsCommand  Advantage .NET Data Provider |  |  |  |  |

Full name: Advantage.Data.Provider.AdsCommand

Implements: System.Data.IDbCommand

[Constructors](dotnet_adscommand_constructors.htm)

[Properties](dotnet_adscommand_properties.htm)

[Methods](dotnet_adscommand_methods.htm)

[Events](dotnet_adscommand_progressmessage.htm)

An AdsCommand object represents an SQL statement or stored procedure to execute or a table to directly open on Advantage Database Server or Advantage Local Server.

To use an AdsCommand object, the application must associate the command with the AdsConnection object. This can be done in one of three ways. If you use the [AdsConnection.CreateCommand()](dotnet_adsconnection_createcommand.htm) method to create a new command object, the command object will be associated with the connection from which it was created automatically. Alternatively, you can use one of the AdsCommand constructors that accepts an AdsConnection object. Or lastly, you can assign the AdsConnection object to the [AdsCommand.Connection](dotnet_adscommand_connection.htm) property after the command object has been created.