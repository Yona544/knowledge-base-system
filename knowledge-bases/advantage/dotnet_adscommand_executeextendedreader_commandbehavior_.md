AdsCommand.ExecuteExtendedReader( CommandBehavior )




Advantage Database Server 12  

AdsCommand.ExecuteExtendedReader( CommandBehavior )

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommand.ExecuteExtendedReader( CommandBehavior )  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommand.ExecuteExtendedReader( CommandBehavior ) Advantage .NET Data Provider dotnet\_Adscommand\_executeextendedreader\_commandbehavior\_ Advantage .NET Data Provider > AdsCommand Class > AdsCommand Methods > AdsCommand.ExecuteExtendedReader( CommandBehavior ) / Dear Support Staff, |  |
| AdsCommand.ExecuteExtendedReader( CommandBehavior )  Advantage .NET Data Provider |  |  |  |  |

Executes [AdsCommand.CommandText](dotnet_adscommand_commandtext.htm) and returns an AdsExtendedReader with the result set based on the CommandBehavior value.

public AdsExtendedReader ExecuteReader( CommandBehavior behavior );

Remarks

Depending on the CommandBehavior value, this method executes the SQL statement or stored procedure, or opens the table that is specified in the [CommandText](dotnet_adscommand_commandtext.htm) property.

[AdsExtendedReader](dotnet_adsextendedreader.htm) is derived from AdsDataReader and offers an extended feature set that includes advanced table navigation, indexed searches, scopes, filters, locks and direct data manipulation. Use [ExecuteExtendedReader](dotnet_adscommand_executeextendedreader.htm) to obtain an AdsExtendedReader object. Use [ExecuteReader](dotnet_adscommand_executereader.htm) to obtain a standard AdsDataReader object.

The CommandBehavior values that affect the AdsExtendedReader are shown in the following table. Bitwise combinations of these values can be used.

|  |  |
| --- | --- |
| Member Name | Description |
| CloseConnection | When the command is executed, the associated Connection object is closed when the associated DataReader object is closed. |
| Default | Default sets no CommandBehavior flags, so calling ExecuteReader(CommandBehavior.Default) is functionally equivalent to calling ExecuteExtendedReader(). |
| KeyInfo | The query returns column and primary key information. |
| SchemaOnly | The query returns column information only. No result set is returned. |
| SingleRow | The query is expected to return a single row. The Advantage .NET Data Provider will return multiple rows if requested by Read operations, but it will not be as efficient because the provider will use a smaller read cache size when this option is specified. |

Example

See [ExecuteReader(CommandBehavior)](dotnet_adscommand_executereader_commandbehavior_.htm)

See Also

[ExecuteExtendedReader](dotnet_adscommand_executeextendedreader.htm)

[ExecuteReader( CommandBehavior )](dotnet_adscommand_executereader_commandbehavior_.htm)

[CommandText](dotnet_adscommand_commandtext.htm)

[AdsDataReader](dotnet_adsdatareader.htm)

[AdsExtendedReader](dotnet_adsextendedreader.htm)

[AdsDataReader.GetSchemaTable](dotnet_adsdatareader_getschematable.htm)