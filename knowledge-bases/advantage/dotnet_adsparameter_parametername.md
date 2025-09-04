AdsParameter.ParameterName




Advantage Database Server 12  

AdsParameter.ParameterName

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsParameter.ParameterName  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsParameter.ParameterName Advantage .NET Data Provider dotnet\_Adsparameter\_parametername Advantage .NET Data Provider > AdsParameter Class > AdsParameter Properties > AdsParameter.ParameterName / Dear Support Staff, |  |
| AdsParameter.ParameterName  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the name of the AdsParameter.

public string ParameterName {get; set;}

Remarks

The default value is an empty string. If the name is not set, the Advantage .NET Data Provider will use the [AdsParameter.Index](dotnet_adsparameter_index.htm) value to associate the parameter with a parameter in the SQL statement. If the name is set and the SQL statement has named parameters, then the ParameterName value will be used to associate the parameter value with the appropriate parameter in the SQL statement. If, however, the SQL statement does not contain named parameters, then ParameterName will be ignored.

See Also

[Index](dotnet_adsparameter_index.htm)