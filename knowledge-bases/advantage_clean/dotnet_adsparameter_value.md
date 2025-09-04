---
title: Dotnet Adsparameter Value
slug: dotnet_adsparameter_value
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsparameter_value.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 24c6b8fad388f2d0bfe476b48ed80f85ef186c1b
---

# Dotnet Adsparameter Value

AdsParameter.Value

AdsParameter.Value

Advantage .NET Data Provider

| AdsParameter.Value  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the value of the parameter.

public object Value {get; set;}

Remarks

The default value is null. For input parameters, the value is bound to the AdsCommand that is sent to the server. For output value parameters, the value is set after any successful execution of the command.

Null parameter values can be specified by setting the Value property to null or DBNull.Value.

When the value is set, the [AdsParameter.DbType](dotnet_adsparameter_dbtype.md) is inferred from the value if the type has not already been explicitly assigned.

See Also

[DbType](dotnet_adsparameter_dbtype.md)
