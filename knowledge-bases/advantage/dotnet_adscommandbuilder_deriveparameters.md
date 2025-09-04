AdsCommandBuilder.DeriveParameters




Advantage Database Server 12  

AdsCommandBuilder.DeriveParameters

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommandBuilder.DeriveParameters  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommandBuilder.DeriveParameters Advantage .NET Data Provider dotnet\_Adscommandbuilder\_deriveparameters Advantage .NET Data Provider > AdsCommandBuilder Class > AdsCommandBuilder Methods > AdsCommandBuilder.DeriveParameters / Dear Support Staff, |  |
| AdsCommandBuilder.DeriveParameters  Advantage .NET Data Provider |  |  |  |  |

Populates the [AdsCommand.Parameters](dotnet_adscommand_parameters.htm) collection with the parameter information for the stored procedure specified in the SelectCommand CommandText property.

public static void DeriveParameters( AdsCommand command );

Remarks

This method provides a simple method for populating the Parameters collection of the given command prior to executing a stored procedure. If [AdsCommand.CommandType](dotnet_adscommand_commandtype.htm) is not set to StoredProcedure, this method throws an ArgumentException.

This call requires a round trip to the server to retrieve the parameter information for the named stored procedure. Therefore it is more efficient to set the parameter information explicitly.

Calling this method is equivalent to calling the [AdsCommand.DeriveParameters](dotnet_adscommand_deriveparameters.htm) method directly.

See Also

[AdsCommand.Parameters](dotnet_adscommand_parameters.htm)

[AdsCommand.DeriveParameters](dotnet_adscommand_deriveparameters.htm)