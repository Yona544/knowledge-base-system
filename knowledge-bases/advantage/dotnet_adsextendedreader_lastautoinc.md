AdsExtendedReader.LastAutoinc




Advantage Database Server 12  

AdsExtendedReader.LastAutoinc

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.LastAutoinc  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.LastAutoinc Advantage .NET Data Provider dotnet\_Adsextendedreader\_lastautoinc Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Properties > AdsExtendedReader.LastAutoinc / Dear Support Staff, |  |
| AdsExtendedReader.LastAutoinc  Advantage .NET Data Provider |  |  |  |  |

Retrieves the last inserted autoinc value after an SQL INSERT or table append.

public int LastAutoinc{ get; }

Remarks

Returns the last inserted Autoinc value for the given handle. If no Autoinc value has been inserted or the table does not contain an Autoinc field then 0 is returned.

Note The autoinc value returned is client-specific, and because of concurrent database access, is not guaranteed to be the absolute last autoinc value in the table.