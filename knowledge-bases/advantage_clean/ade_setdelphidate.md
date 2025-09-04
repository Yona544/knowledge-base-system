---
title: Ade Setdelphidate
slug: ade_setdelphidate
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_setdelphidate.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 52982b77888077b07b797a32730d492e59a50364
---

# Ade Setdelphidate

SetDelphiDate

TAdsSettings.SetDelphiDate

Advantage TDataSet Descendant

| TAdsSettings.SetDelphiDate  Advantage TDataSet Descendant |  |  |  |  |

[TAdsSettings](ade_tadssettings_7.md)

Defines whether the TAdsSettings component sets Delphi's global ShortDateFormat variable to match the TAdsSettings.DateFormat.

Syntax

property SetDelphiDate : Boolean;

Description

If True, the TAdsSettings component will set the Delphi global variable ShortDateFormat to match the TAdsSettings.DateFormat property.

It is often not desirable to have the TAdsSettings component modifying the ShortDateFormat variable. The default value of the SetDelphiDate property is TRUE only to support backwards-compatibility.
