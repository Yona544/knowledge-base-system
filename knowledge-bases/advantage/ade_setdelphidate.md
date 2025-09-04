SetDelphiDate




Advantage Database Server 12  

TAdsSettings.SetDelphiDate

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsSettings.SetDelphiDate  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsSettings.SetDelphiDate Advantage TDataSet Descendant ade\_Setdelphidate Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsSettings.SetDelphiDate  Advantage TDataSet Descendant |  |  |  |  |

[TAdsSettings](ade_tadssettings_7.htm)

Defines whether the TAdsSettings component sets Delphi's global ShortDateFormat variable to match the TAdsSettings.DateFormat.

Syntax

property SetDelphiDate : Boolean;

Description

If True, the TAdsSettings component will set the Delphi global variable ShortDateFormat to match the TAdsSettings.DateFormat property.

It is often not desirable to have the TAdsSettings component modifying the ShortDateFormat variable. The default value of the SetDelphiDate property is TRUE only to support backwards-compatibility.