AdsCommandBuilder.UsePKOnlyInWhereClause




Advantage Database Server 12  

AdsCommandBuilder.UsePKOnlyInWhereClause

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommandBuilder.UsePKOnlyInWhereClause  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommandBuilder.UsePKOnlyInWhereClause Advantage .NET Data Provider dotnet\_Adscommandbuilder\_usepkonlyinwhereclause Advantage .NET Data Provider > AdsCommandBuilder Class > AdsCommandBuilder Properties > AdsCommandBuilder.UsePKOnlyInWhereClause / Dear Support Staff, |  |
| AdsCommandBuilder.UsePKOnlyInWhereClause  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the flag that controls whether the WHERE clause automatically generated for UPDATE and DELETE statements includes all fields or just the primary key field.

public bool UsePKOnlyInWhereClause {get; set;}

Remarks

By default, this value is False, which means that automatically generated UPDATE and DELETE statements will contain all searchable fields in the WHERE clause. This provides the best concurrency control. If you know in certain cases that it is safe to only reference the primary key in the where clause, you can set this property to True. Note that this can cause concurrency problems if a different user has changed other fields.

If you try to set this property to True when [RequirePrimaryKey](dotnet_adscommandbuilder_requireprimarykey.htm) property is False, the Advantage .NET Data Provider will throw an InvalidOperationException exception.

See Also

[RequirePrimaryKey](dotnet_adscommandbuilder_requireprimarykey.htm)