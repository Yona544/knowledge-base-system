---
title: Ade Adsclearallscopes
slug: ade_adsclearallscopes
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsclearallscopes.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 0049b7d39721b2c1221db284c7cf0fccbdc665b8
---

# Ade Adsclearallscopes

AdsClearAllScopes

TAdsTable.AdsClearAllScopes

Advantage TDataSet Descendant

| TAdsTable.AdsClearAllScopes  Advantage TDataSet Descendant |  |  |  |  |

Clears scopes on all indexes open for the given table.

Syntax

procedure AdsClearAllScopes;

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: CancelRange. See your Delphi documentation for more information about this native Delphi method.

Description

This function will clear both top and bottom scopes for all index orders open for this table.

Example

AdsTable1.SetRange( [Adams], [Smith] );

AdsTable1.CancelRange;

See Also

[AdsClearScope](ade_adsclearscope.md)

[AdsGetScope](ade_adsgetscope.md)

[AdsSetScope](ade_adssetscope.md)
