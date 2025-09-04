AdsParameter.SourceVersion




Advantage Database Server 12  

AdsParameter.SourceVersion

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsParameter.SourceVersion  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsParameter.SourceVersion Advantage .NET Data Provider dotnet\_Adsparameter\_sourceversion Advantage .NET Data Provider > AdsParameter Class > AdsParameter Properties > AdsParameter.SourceVersion / Dear Support Staff, |  |
| AdsParameter.SourceVersion  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the DataRowVersion to use when loading Value.

public DataRowVersion SourceVersion {get; set;}

Remarks

The SourceVersion property is used by the [AdsDataAdapter.UpdateCommand](dotnet_adsdataadapter_updatecommand.htm) during the Update to determine whether the original or current value is used for a parameter value. This allows primary keys to be updated. This property is ignored by the [AdsDataAdapter.InsertCommand](dotnet_adsdataadapter_insertcommand.htm) and [AdsDataAdapter.DeleteCommand](dotnet_adsdataadapter_deletecommand.htm). The default value is DataRowVersion.Current.