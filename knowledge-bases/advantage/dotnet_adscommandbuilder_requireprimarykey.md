AdsCommandBuilder.RequirePrimaryKey




Advantage Database Server 12  

AdsCommandBuilder.RequirePrimaryKey

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommandBuilder.RequirePrimaryKey  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommandBuilder.RequirePrimaryKey Advantage .NET Data Provider dotnet\_Adscommandbuilder\_requireprimarykey Advantage .NET Data Provider > AdsCommandBuilder Class > AdsCommandBuilder Properties > AdsCommandBuilder.RequirePrimaryKey / Dear Support Staff, |  |
| AdsCommandBuilder.RequirePrimaryKey  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the flag that controls whether the AdsCommandBuilder object will automatically generate the commands even if there is no primary key.

public bool RequirePrimaryKey {get; set;}

Remarks

By default, this value is True, which means that a primary key is required in order for the AdsCommandBuilder to generate the statements. If you know that the available searchable fields provide sufficient information to uniquely identify a given row in the WHERE clause, then you can set this property to False. Note that if there is no primary key and the searchable fields do not uniquely identify a row, then an UPDATE or DELETE statement may affect multiple rows, and the AdsDataAdapter will throw a DBConcurrencyException.

If you try to set this property to False when the [AdsCommandBuilder.UsePKOnlyInWhereClause](dotnet_adscommandbuilder_usepkonlyinwhereclause.htm) is True, the Advantage .NET Data Provider will throw an InvalidOperationException exception.

This property may be useful for generating statements for DBF tables. It is not possible to create primary keys on DBF tables, so it is necessary to either set this flag to False or to specify the UPDATE and DELETE commands explicitly.

See Also

[UsePKOnlyInWhereClause](dotnet_adscommandbuilder_usepkonlyinwhereclause.htm)