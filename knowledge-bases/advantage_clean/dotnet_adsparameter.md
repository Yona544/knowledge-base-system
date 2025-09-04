---
title: Dotnet Adsparameter
slug: dotnet_adsparameter
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsparameter.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 49c833f07ab10a2bbea0055574447d389537ea45
---

# Dotnet Adsparameter

AdsParameter

AdsParameter

Advantage .NET Data Provider

| AdsParameter  Advantage .NET Data Provider |  |  |  |  |

Full name: Advantage.Data.Provider.AdsParameter

Implements: System.Data.IDbDataParameter, System.Data.IDataParameter

[Constructors](dotnet_adsparameter_constructors.md)

[Properties](dotnet_adsparameter_properties.md)

An AdsParameter object represents a parameter to an [AdsCommand](dotnet_adscommand.md), and optionally, its mapping to DataSet columns.

Named parameters in Advantage SQL statements must be prefixed with a colon. For example "select \* from mytable where id = :id". This is different than some SQL engines, which use the @ symbol as a named parameter prefix.

See Also

[AdsCommand.DeriveParameters](dotnet_adscommand_deriveparameters.md)
