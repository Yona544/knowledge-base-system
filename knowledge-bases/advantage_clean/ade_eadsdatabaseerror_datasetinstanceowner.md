---
title: Ade Eadsdatabaseerror Datasetinstanceowner
slug: ade_eadsdatabaseerror_datasetinstanceowner
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_eadsdatabaseerror_datasetinstanceowner.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: f9421edf6839979a23648664a285cfb88f6a3040
---

# Ade Eadsdatabaseerror Datasetinstanceowner

EADSDatabaseError.DataSetInstanceOwner

EADSDatabaseError.DataSetInstanceOwner

Advantage TDataSet Descendant

| EADSDatabaseError.DataSetInstanceOwner  Advantage TDataSet Descendant |  |  |  |  |

[EADSDatabaseError](ade_eadsdatabaseerror.md)

String representation of the object owning the dataset that raised the exception.

Syntax

property DataSetInstanceOwner : STRING;

Description

DataSetInstanceOwner contains a string representation of the name of the owner of the dataset that raised the exception (e.g., Form1). This property can be utilized while debugging or in other instances where the name of the owning object could be helpful in determining which form or object owns the table raising the exception.

If the name of the datasets owner was not available to the method raising the exception the DataSetInstanceOwner property will contain an empty string.
