---
title: Ade Eadsdatabaseerror Sqlerrorcode
slug: ade_eadsdatabaseerror_sqlerrorcode
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_eadsdatabaseerror_sqlerrorcode.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: b21386ae6e130f96e656ca263de3d2a3c242062d
---

# Ade Eadsdatabaseerror Sqlerrorcode

EADSDatabaseError.SQLErrorCode

EADSDatabaseError.SQLErrorCode

Advantage TDataSet Descendant

| EADSDatabaseError.SQLErrorCode  Advantage TDataSet Descendant |  |  |  |  |

[EADSDatabaseError](ade_eadsdatabaseerror.md)

Native SQL Error code returned inside of the 7200 class error string.

Syntax

property SQLErrorCode : UNSIGNED32;

Description

Use SQLErrorCode for easy access to the native sql error code that is often embedded inside of the error string returned by SQL operations. If the error object in question was not raised by an SQL operation, the SQLErrorCode property will be zero.
