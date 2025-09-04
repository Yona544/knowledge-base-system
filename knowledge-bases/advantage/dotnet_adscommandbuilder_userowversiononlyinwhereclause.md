AdsCommandBuilder.UseRowversionOnlyInWhereClause




Advantage Database Server 12  

AdsCommandBuilder.UseRowversionOnlyInWhereClause

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommandBuilder.UseRowversionOnlyInWhereClause  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommandBuilder.UseRowversionOnlyInWhereClause Advantage .NET Data Provider dotnet\_Adscommandbuilder\_userowversiononlyinwhereclause Advantage .NET Data Provider > AdsCommandBuilder Class > AdsCommandBuilder Properties > AdsCommandBuilder.UseRowversionOnlyInWhereClause / Dear Support Staff, |  |
| AdsCommandBuilder.UseRowversionOnlyInWhereClause  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the flag that controls whether the WHERE clause automatically generated for UPDATE and DELETE statements includes all fields or just the rowversion field.

public bool UseRowversionOnlyInWhereClause {get; set;}

Remarks

By default, this value is False, which means that automatically generated UPDATE and DELETE statements will contain all searchable fields in the WHERE clause. Because rowversion fields are automatically incremented each time a record is updated and guaranteed to be unique within the entire table, using just a rowversion field in the WHERE clause of an UPDATE or DELETE statement is safe. It is also advantageous in that only the rowversion field value will be sent to the server within the query parameters, as opposed to the default behavior which would send all the searchable field data to the server.

See Also

UsePKOnlyInWhereClauseAdsCommandBuilder\_UsePKOnlyInWhereClause