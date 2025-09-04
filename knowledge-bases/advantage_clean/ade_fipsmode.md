---
title: Ade Fipsmode
slug: ade_fipsmode
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_fipsmode.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 2f0339a503568102fa429193a3dce62835aaeb6a
---

# Ade Fipsmode

FIPSMode

TAdsConnection.EncryptionOptions.FIPSMode

Advantage TDataSet Descendant

| TAdsConnection.EncryptionOptions.FIPSMode  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Specifies whether the client should be in [FIPS mode](master_fips.md).

Syntax

property EncryptionOptions.FIPSMode: Boolean;

Description

Specifies whether or not the client should run in [FIPS mode](master_fips.md). This setting must be the same as the server to which the connection is made. All connections must use the same value in an application. It is not allowed to mix FIPS mode connections and non-FIPS mode connections.
