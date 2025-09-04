---
title: Dotnet Adsdataadapter Fillerror
slug: dotnet_adsdataadapter_fillerror
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdataadapter_fillerror.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 092b442d02ed183c103b51f0da1444953fb51c13
---

# Dotnet Adsdataadapter Fillerror

AdsDataAdapter.FillError

AdsDataAdapter.FillError

Advantage .NET Data Provider

| AdsDataAdapter.FillError  Advantage .NET Data Provider |  |  |  |  |

Returned when an error occurs during a fill operation.

public event FillErrorEventHandler FillError;

Remarks

The event handler receives an argument of type FillErrorEventArgs containing data related to this event. The following FillErrorEventArgs properties provide information specific to this event.

| Property | Description |
| Continue | Gets or sets a value indicating whether to continue the fill operation despite the error. |
| DataTable | Gets the DataTable being updated when the error occurred. |
| Errors | Gets the errors being handled. |
| Values | Gets the values for the row being updated when the error occurred. |

The FillError event allows a user to determine whether or not the fill operation should continue after the error occurs. Examples of when the FillError event might occur are:

- The data being added to a DataSet cannot be converted to a common language runtime type without losing precision.

- The row being added contains data that violates a Constraint that must be enforced on a DataColumn in the DataSet.
