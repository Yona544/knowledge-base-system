AdsCommandBuilder.GetInsertCommand




Advantage Database Server 12  

AdsCommandBuilder.GetInsertCommand

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommandBuilder.GetInsertCommand  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommandBuilder.GetInsertCommand Advantage .NET Data Provider dotnet\_Adscommandbuilder\_getinsertcommand Advantage .NET Data Provider > AdsCommandBuilder Class > AdsCommandBuilder Methods > AdsCommandBuilder.GetInsertCommand / Dear Support Staff, |  |
| AdsCommandBuilder.GetInsertCommand  Advantage .NET Data Provider |  |  |  |  |

Gets the automatically generated AdsCommand object required to perform inserts on the database when an application calls [AdsDataAdapter.Update](dotnet_adsdataadapter_update.htm).

public AdsCommand GetInsertCommand();

Remarks

An application can use the GetInsertCommand method for informational or troubleshooting purposes because it returns the AdsCommand object to be executed.

You can also use GetInsertCommand as the basis of a modified command. For example, you might call GetInsertCommand during development to quickly produce an INSERT statement and then use that statement directly in your application rather than using the AdsCommandBuilder in the released application.

After the SQL statement is first generated, the application must explicitly call [AdsCommandBuilder.RefreshSchema](dotnet_adscommandbuilder_refreshschema.htm) if it changes the statement in any way. Otherwise, the GetInsertCommand will be still be using information from the previous statement, which might not be correct. The SQL statements are first generated either when the application calls [AdsDataAdapter.Update](dotnet_adsdataadapter_update.htm) or [GetInsertCommand](dotnet_adscommandbuilder_getinsertcommand.htm).