AdsDataAdapter.MissingMappingAction




Advantage Database Server 12  

AdsDataAdapter.MissingMappingAction

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataAdapter.MissingMappingAction  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataAdapter.MissingMappingAction Advantage .NET Data Provider dotnet\_Adsdataadapter\_missingmappingaction Advantage .NET Data Provider > AdsDataAdapter Class > AdsDataAdapter Properties > AdsDataAdapter.MissingMappingAction / Dear Support Staff, |  |
| AdsDataAdapter.MissingMappingAction  Advantage .NET Data Provider |  |  |  |  |

Indicates or specifies whether unmapped source tables or columns are passed with their source names in order to be filtered or to raise an error.

public MissingMappingAction MissingMappingAction {get; set;}

Remarks

The valid values are shown in the following table. The default is PassThrough. The [AdsDataAdapter.TableMappings](dotnet_adsdataadapter_tablemappings.htm) property provides the master mapping between the returned records and the DataSet.

|  |  |
| --- | --- |
| Member Name | Description |
| Error | A SystemException is generated. |
| Ignore | The column or table not having a mapping is ignored. Returns a null reference (Nothing in Visual Basic). |
| Passthrough | The source column or source table created and added to the DataSet using its original name. |

See Also

[TableMappings](dotnet_adsdataadapter_tablemappings.htm)