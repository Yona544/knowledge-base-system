AdsCommandBuilder.GetDeleteCommand




Advantage Database Server 12  

AdsCommandBuilder.GetDeleteCommand

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommandBuilder.GetDeleteCommand  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommandBuilder.GetDeleteCommand Advantage .NET Data Provider dotnet\_Adscommandbuilder\_getdeletecommand Advantage .NET Data Provider > AdsCommandBuilder Class > AdsCommandBuilder Methods > AdsCommandBuilder.GetDeleteCommand / Dear Support Staff, |  |
| AdsCommandBuilder.GetDeleteCommand  Advantage .NET Data Provider |  |  |  |  |

Gets the automatically generated AdsCommand object required to perform deletions on the database when an application calls [AdsDataAdapter.Update](dotnet_adsdataadapter_update.htm).

public AdsCommand GetDeleteCommand();

Remarks

An application can use the GetDeleteCommand method for informational or troubleshooting purposes because it returns the AdsCommand object to be executed.

You can also use GetDeleteCommand as the basis of a modified command. For example, you might call GetDeleteCommand during development to quickly produce a DELETE statement and then use that statement directly in your application rather than using the AdsCommandBuilder in the released application.

After the SQL statement is first generated, the application must explicitly call [AdsCommandBuilder.RefreshSchema](dotnet_adscommandbuilder_refreshschema.htm) if it changes the statement in any way. Otherwise, the GetDeleteCommand will be still be using information from the previous statement, which might not be correct. The SQL statements are first generated either when the application calls Update or GetDeleteCommand.