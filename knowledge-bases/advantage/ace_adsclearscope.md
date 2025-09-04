AdsClearScope




Advantage Database Server 12  

AdsClearScope

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsClearScope  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsClearScope Advantage Client Engine ace\_Adsclearscope Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsClearScope  Advantage Client Engine |  |  |  |  |

Clears scope on the given index order.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsClearScope (ADSHANDLE hIndex,  UNSIGNED16 usScopeOption); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle index order. |
| usScopeOption (I) | Indicates which scope value to clear. Options are ADS\_TOP and ADS\_BOTTOM. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_NO\_SCOPE | No scope was set, so a scope cannot be returned or cleared. |

Remarks

If the top or bottom scope is cleared, any other scope settings remain. If currently positioned at EOF or BOF and a scope is cleared, it is necessary to reposition by performing a movement to see any records.

Example

[Click Here](ace_examples.htm#adsclearscopeexample)

See Also

[AdsSetScope](ace_adssetscope.htm)

[AdsGetScope](ace_adsgetscope.htm)

[AdsSeek](ace_adsseek.htm)

[AdsSkip](ace_adsskip.htm)

[AdsGotoTop](ace_adsgototop.htm)

[AdsGotoBottom](ace_adsgotobottom.htm)

[AdsClearAllScopes](ace_adsclearallscopes.htm)