AdsParameter




Advantage Database Server 12  

AdsParameter

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsParameter  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsParameter Advantage .NET Data Provider dotnet\_Adsparameter Advantage .NET Data Provider > AdsParameter Class > Overview / Dear Support Staff, |  |
| AdsParameter  Advantage .NET Data Provider |  |  |  |  |

Full name: Advantage.Data.Provider.AdsParameter

Implements: System.Data.IDbDataParameter, System.Data.IDataParameter

[Constructors](dotnet_adsparameter_constructors.htm)

[Properties](dotnet_adsparameter_properties.htm)

An AdsParameter object represents a parameter to an [AdsCommand](dotnet_adscommand.htm), and optionally, its mapping to DataSet columns.

Named parameters in Advantage SQL statements must be prefixed with a colon. For example "select \* from mytable where id = :id". This is different than some SQL engines, which use the @ symbol as a named parameter prefix.

See Also

[AdsCommand.DeriveParameters](dotnet_adscommand_deriveparameters.htm)