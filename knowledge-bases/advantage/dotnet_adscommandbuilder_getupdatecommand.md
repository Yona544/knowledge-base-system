AdsCommandBuilder.GetUpdateCommand




Advantage Database Server 12  

AdsCommandBuilder.GetUpdateCommand

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommandBuilder.GetUpdateCommand  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommandBuilder.GetUpdateCommand Advantage .NET Data Provider dotnet\_Adscommandbuilder\_getupdatecommand Advantage .NET Data Provider > AdsCommandBuilder Class > AdsCommandBuilder Methods > AdsCommandBuilder.GetUpdateCommand / Dear Support Staff, |  |
| AdsCommandBuilder.GetUpdateCommand  Advantage .NET Data Provider |  |  |  |  |

Gets the automatically generated AdsCommand object required to perform updates on the database when an application calls [AdsDataAdapter.Update](dotnet_adsdataadapter_update.htm).

public AdsCommand GetUpdateCommand();

Remarks

An application can use the GetUpdateCommand method for informational or troubleshooting purposes because it returns the AdsCommand object to be executed.

You can also use GetUpdateCommand as the basis of a modified command. For example, you might call GetUpdateCommand during development to quickly produce an UPDATE statement and then use that statement directly in your application rather than using the AdsCommandBuilder in the released application.

After the SQL statement is first generated, the application must explicitly call [AdsCommandBuilder.RefreshSchema](dotnet_adscommandbuilder_refreshschema.htm) if it changes the statement in any way. Otherwise, the GetUpdateCommand will be still be using information from the previous statement, which might not be correct. The SQL statements are first generated either when the application calls [AdsDataAdapter.Update](dotnet_adsdataadapter_update.htm) or GetUpdateCommand.