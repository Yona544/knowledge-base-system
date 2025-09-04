AdsDataAdapter.SelectCommand




Advantage Database Server 12  

AdsDataAdapter.SelectCommand

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataAdapter.SelectCommand  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataAdapter.SelectCommand Advantage .NET Data Provider dotnet\_Adsdataadapter\_selectcommand Advantage .NET Data Provider > AdsDataAdapter Class > AdsDataAdapter Properties > AdsDataAdapter.SelectCommand / Dear Support Staff, |  |
| AdsDataAdapter.SelectCommand  Advantage .NET Data Provider |  |  |  |  |

Gets or sets an SQL statement, stored procedure, or table name used to select records in the data source.

public AdsCommand SelectCommand { get; set; }

Remarks

This command is used by the [AdsDataAdapter.Fill](dotnet_adsdataadapter_fill.htm) call to select the data that is put into the DataSet.

When SelectCommand is assigned to a previously created [AdsCommand](dotnet_adscommand.htm), the AdsCommand is not cloned. The SelectCommand maintains a reference to the previously created AdsCommand object.

If the SelectCommand does not return any rows, no tables are added to the DataSet, and no exception is raised.

The SelectCommand must be set before and [AdsCommandBuilder](dotnet_adscommandbuilder.htm) can be used with this AdsDataAdapter.

See Also

[AdsCommandBuilder](dotnet_adscommandbuilder.htm)