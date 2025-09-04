---
title: Ade Eadsdatabaseerror Create
slug: ade_eadsdatabaseerror_create
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_eadsdatabaseerror_create.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: a928ca81fd637038482a61fbe659914c5c7ed410
---

# Ade Eadsdatabaseerror Create

EADSDatabaseError.Create

EADSDatabaseError.Create

Advantage TDataSet Descendant

| EADSDatabaseError.Create  Advantage TDataSet Descendant |  |  |  |  |

[EADSDatabaseError](ade_eadsdatabaseerror.md)

Creates an instance of an EADSDatabaseError exception.

Syntax

constructor Create( oDataSet : TAdsDataSet;

ulErrCode : UNSIGNED32;

const strMsg : STRING );

Description

Call Create to construct an exception with an error string and extended [EADSDatabaseError Properties](ade_eadsdatabaseerror_properties.md).

oDataSet is a pointer to the dataset generating the exception. If the dataset is not available pass this parameter as nil and the extended [EADSDatabaseError Properties](ade_eadsdatabaseerror_properties.md) will remain empty.

ulErrCode is the Advantage Client Engine (ACE) error code to be associated with this exception.

strMsg is the runtime error message to display, and is also used to fill the EADSDatabaseError.Message property.
