AdsCommand.ExecuteExtendedReader




Advantage Database Server 12  

AdsCommand.ExecuteExtendedReader

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommand.ExecuteExtendedReader  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommand.ExecuteExtendedReader Advantage .NET Data Provider dotnet\_Adscommand\_executeextendedreader Advantage .NET Data Provider > AdsCommand Class > AdsCommand Methods > AdsCommand.ExecuteExtendedReader / Dear Support Staff, |  |
| AdsCommand.ExecuteExtendedReader  Advantage .NET Data Provider |  |  |  |  |

Executes the AdsCommand.CommandText and returns an AdsExtendedReader with the result set.

public AdsExtendedReader ExecuteExtendedReader();

Remarks

ExecuteExtendedReader executes the SQL statement or stored procedure or opens the table that is specified in the AdsCommand.CommandText property.

[AdsExtendedReader](dotnet_adsextendedreader.htm) is derived from AdsDataReader and offers an extended feature set that includes advanced table navigation, indexed searches, scopes, filters, locks and direct data manipulation. Use [ExecuteExtendedReader](dotnet_adscommand_executeextendedreader.htm) to obtain an AdsExtendedReader object. Use [ExecuteReader](dotnet_adscommand_executereader.htm) to obtain a standard AdsDataReader object.

Example

See [ExecuteReader](dotnet_adscommand_executereader.htm)

See Also

[ExecuteReader](dotnet_adscommand_executereader.htm)

[ExecuteReader( CommandBehavior )](dotnet_adscommand_executereader_commandbehavior_.htm)

ExecuteExtendedReader( CommandBehavior )

[CommandText](dotnet_adscommand_commandtext.htm)

[AdsDataReader](dotnet_adsdatareader.htm)

[AdsExtendedReader](dotnet_adsextendedreader.htm)