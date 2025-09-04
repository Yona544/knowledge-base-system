AdsConnection.DDVersionMinor




Advantage Database Server 12  

AdsConnection.DDVersionMinor

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnection.DDVersionMinor  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnection.DDVersionMinor Advantage .NET Data Provider dotnet\_Adsconnection\_ddversionminor Advantage .NET Data Provider > AdsConnection Class > AdsConnection Properties > AdsConnection.DDVersionMinor / Dear Support Staff, |  |
| AdsConnection.DDVersionMinor  Advantage .NET Data Provider |  |  |  |  |

Get or set the database minor version.

public int DDVersionMinor{ get; set; }

Remarks

Gets or sets the user minor version property of the data dictionary. This property is intended for storing a value associated with the minor version of the user's dictionary. The user version property is set, read, and interpreted by the application. The Advantage Database Server does not currently use it internally. This allows developers to ship version "1.0" of a database defined in a data dictionary, then later ship version "1.1" of the data dictionary. The default value for this property, if it has never been set, is 0. If set to NULL, the user version property value will be removed.

See Also

[DDVersionMajor](dotnet_adsconnection_ddversionmajor.htm)