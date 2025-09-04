AdsDataReader.IsStatic




Advantage Database Server 12  

AdsDataReader.IsStatic

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.IsStatic  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.IsStatic Advantage .NET Data Provider dotnet\_Adsdatareader\_isstatic Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Properties > AdsDataReader.IsStatic / Dear Support Staff, |  |
| AdsDataReader.IsStatic  Advantage .NET Data Provider |  |  |  |  |

Indicates whether or not a result set is static (read-only) or live (updateable).

public bool IsStatic { get; }

Remarks

The IsStatic property reflects the type of cursor returned by the SQL statement (or direct table open). There is a one-to-one correlation between this property and the capability to use the [AdsCommandBuilder](dotnet_adscommandbuilder.htm) to automatically generate commands for updating a result set. If this property returns False, it is not possible to use AdsCommandBuilder to generate the update commands for the statement. For information about these cursor types, see [Live versus Static Cursors](master_live_versus_static_cursors.htm) in the Advantage Help file.

See Also

[AdsCommandBuilder](dotnet_adscommandbuilder.htm)