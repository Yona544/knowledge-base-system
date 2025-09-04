DateFormat




Advantage Database Server 12  

TAdsSettings.DateFormat

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsSettings.DateFormat  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsSettings.DateFormat Advantage TDataSet Descendant ade\_Dateformat Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsSettings.DateFormat  Advantage TDataSet Descendant |  |  |  |  |

[TAdsSettings](ade_tadssettings_7.htm)

Specifies the date format. The date format must contain two or more occurrences of the letters D, M, and Y respectively (e.g., "MM-DD-YYYY"). The default DateFormat is set from the Delphi global ShortDateFormat. If Advantage does not recognize the format of the ShortDateFormat variable, the DateFormat property will default to MM/DD/CCYY.

Syntax

property DateFormat: String;

Description

DateFormat is a global setting that affects the behavior of dates throughout a program. This allows the programmer to control date formatting for applications.

This setting affects how the Advantage Database Server interprets all date strings. It also defines how all dates are passed back to the calling application. DateFormat can also be used to specify separators in the date format. For example, "DD/MM/YYYY" and "DD-MM-YYYY" are both valid date formats.