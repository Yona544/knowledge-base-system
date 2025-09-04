AdsConnection.DDVersionMajor




Advantage Database Server 12  

AdsConnection.DDVersionMajor

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsConnection.DDVersionMajor  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsConnection.DDVersionMajor Advantage .NET Data Provider dotnet\_Adsconnection\_ddversionmajor Advantage .NET Data Provider > AdsConnection Class > AdsConnection Properties > AdsConnection.DDVersionMajor / Dear Support Staff, |  |
| AdsConnection.DDVersionMajor  Advantage .NET Data Provider |  |  |  |  |

Get or set the database major version.

public int DDVersionMajor{ get; set; }

Remarks

Gets or sets the user major version property of the data dictionary. This property is intended for storing a value associated with the major version of the user's dictionary. The user version property is set, read, and interpreted by the application. The Advantage Database Server does not currently use it internally. This allows developers to ship version "1.0" of a database defined in a data dictionary, then later ship version "1.1" of the data dictionary. The default value for this property, if it has never been set, is 0. If set to NULL, the user version property value will be removed.

See Also

[DDVersionMinor](dotnet_adsconnection_ddversionminor.htm)