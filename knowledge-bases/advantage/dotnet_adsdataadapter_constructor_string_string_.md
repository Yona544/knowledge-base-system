AdsDataAdapter Constructor( String, String )




Advantage Database Server 12  

AdsDataAdapter Constructor( String, String )

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataAdapter Constructor( String, String )  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataAdapter Constructor( String, String ) Advantage .NET Data Provider dotnet\_Adsdataadapter\_constructor\_string\_string\_ Advantage .NET Data Provider > AdsDataAdapter Class > AdsDataAdapter Constructors > AdsDataAdapter Constructor( String, String ) / Dear Support Staff, |  |
| AdsDataAdapter Constructor( String, String )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of an AdsDataAdapter object with a given SQL statement and a connection string to associate with the command.

public AdsDataAdapter( string selectCommand,

string connection );

Remarks

The selectCommand string is expected to be a valid SQL SELECT statement or stored procedure to be used as the [CommandText](dotnet_adscommand_commandtext.htm) of the [SelectCommand](dotnet_adsdataadapter_selectcommand.htm) property of the AdsDataAdapter. A new [AdsConnection](dotnet_adsconnection.htm) object will be created and opened using the given connection string.