AdsDataAdapter Constructor( String, AdsConnection )




Advantage Database Server 12  

AdsDataAdapter Constructor( String, AdsConnection )

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataAdapter Constructor( String, AdsConnection )  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataAdapter Constructor( String, AdsConnection ) Advantage .NET Data Provider dotnet\_Adsdataadapter\_constructor\_string\_adsconnection\_ Advantage .NET Data Provider > AdsDataAdapter Class > AdsDataAdapter Constructors > AdsDataAdapter Constructor( String, AdsConnection ) / Dear Support Staff, |  |
| AdsDataAdapter Constructor( String, AdsConnection )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of an AdsDataAdapter object with a given SQL statement and a connection to associate with the command.

public AdsDataAdapter( string selectCommand,

AdsConnection connection );

Remarks

The selectCommand string is expected to be a valid SQL SELECT statement or stored procedure to be used as the [CommandText](dotnet_adscommand_commandtext.htm) of the [SelectCommand](dotnet_adsdataadapter_selectcommand.htm) property of the AdsDataAdapter.