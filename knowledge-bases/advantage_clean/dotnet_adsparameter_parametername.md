---
title: Dotnet Adsparameter Parametername
slug: dotnet_adsparameter_parametername
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsparameter_parametername.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 7846fc1a310375fee293a7dbb1f8578ce4f1f312
---

# Dotnet Adsparameter Parametername

AdsParameter.ParameterName

AdsParameter.ParameterName

Advantage .NET Data Provider

| AdsParameter.ParameterName  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the name of the AdsParameter.

public string ParameterName {get; set;}

Remarks

The default value is an empty string. If the name is not set, the Advantage .NET Data Provider will use the [AdsParameter.Index](dotnet_adsparameter_index.md) value to associate the parameter with a parameter in the SQL statement. If the name is set and the SQL statement has named parameters, then the ParameterName value will be used to associate the parameter value with the appropriate parameter in the SQL statement. If, however, the SQL statement does not contain named parameters, then ParameterName will be ignored.

See Also

[Index](dotnet_adsparameter_index.md)
