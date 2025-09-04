---
title: Ade Adsclearscope
slug: ade_adsclearscope
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsclearscope.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 4a728a595a96fbf75d72e60f7d50d0904970c156
---

# Ade Adsclearscope

AdsClearScope

TAdsTable.AdsClearScope

Advantage TDataSet Descendant

| TAdsTable.AdsClearScope  Advantage TDataSet Descendant |  |  |  |  |

Clears scope on the given index order.

Syntax

type TAdsScopeOptions = ( soTOP, soBOTTOM );

 

procedure AdsClearScope( eScopeOption : TAdsScopeOption );

Parameter

| eScopeOption | Enumerated type for the scope option. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: CancelRange. See your Delphi documentation for more information about this native Delphi method.

Example

AdsTable1.SetRange( [Adams], [Smith] );

 

AdsTable1.CancelRange;

Description

If the top or bottom scope is cleared, any other scope settings remain. If currently positioned at EOF or BOF and a scope is cleared, it is necessary to reposition by performing a movement to see any records.

See Also

[AdsClearAllScopes](ade_adsclearallscopes.md)

[AdsGetScope](ade_adsgetscope.md)

[AdsGotoBottom](ade_adsgotobottom.md)

[AdsGotoTop](ade_adsgototop.md)

[AdsSeek](ade_adsseek.md)

[AdsSetScope](ade_adssetscope.md)

[AdsSkip](ade_adsskip.md)
