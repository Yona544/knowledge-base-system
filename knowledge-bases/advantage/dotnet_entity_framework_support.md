Entity Framework Support




Advantage Database Server 12  

Entity Framework Support

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Entity Framework Support  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - Entity Framework Support Advantage .NET Data Provider dotnet\_Entity\_Framework\_Support Advantage .NET Data Provider > Entity Framework Support > Entity Framework Support / Dear Support Staff, |  |
| Entity Framework Support  Advantage .NET Data Provider |  |  |  |  |

The ADO.NET Entity Framework provides a model for mapping objects to data and extends the ADO.NET Data Providers.  Advantage has implemented an Entity Framework Data Provider to facilitate use of the Entity Framework.

Provider Namespace Name

Entity Framework Data Providers are required to specify a namespace.  The namespace for the Advantage Database Server Entity Framework Data provider is Advantage.

Types

The Advantage Entity Framework maps Entity Data Model (EDM) types to Advantage Database Server types in the following manner:

| Provider type name | EDM type name |
| --- | --- |
| Character | String |
| CICharacter | String |
| Memo | String |
| VarChar | String |
| NChar | String |
| NMemo | String |
| NVarChar | String |
| Date | DateTime |
| Time | Time |
| TimeStamp | DateTime |
| ModTime | DateTime |
| Logical | Boolean |
| ShortInt | Int16 |
| Integer | Int32 |
| AutoIncrement | Int32 |
| Money | Decimal |
| Numeric | Decimal |
| Double | Double |
| CurDouble | Double |
| RowVersion | Binary |
| Raw | Binary |
| VarBinary | Binary |
| Binary | Binary |
| Image | Binary |

See Also

[Unsupported Entity Framework Functionality](dotnet_unsupported_entity_framework_f.htm)

[Limitations of the Automated Entity Framework Tools](dotnet_limitations_of_the_automated_e.htm)