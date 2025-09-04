---
title: Ade Adssethandlelong
slug: ade_adssethandlelong
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adssethandlelong.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 3309bf09fddcf81c5b80ff0445cb96b6aaa29b9d
---

# Ade Adssethandlelong

AdsSetHandleLong

TAdsTable.AdsSetHandleLong

Advantage TDataSet Descendant

| TAdsTable.AdsSetHandleLong  Advantage TDataSet Descendant |  |  |  |  |

Sets a long value for the given handle

Syntax

procedure AdsSetHandleLong( ulHandle : Longint );

Description

Sets a long value that will be associated with the given handle and available to the user for the life of the handle. The value stored is at the user's discretion. The Advantage Client Engine does not use the value for any operation, but simply stores it. If the value is a memory reference (e.g., a pointer to an application-specific structure), the application is responsible for freeing the memory.

Example

procedure TForm1.RegisterHandle( lNewID : Longint );

begin

AdsTable1.AdsSetHandleLong( lNewID );

end;

See Also

[AdsGetHandleLong](ade_adsgethandlelong.md)
