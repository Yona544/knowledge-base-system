ScopeEnd




Advantage Database Server 12  

TAdsTable/TAdsQuery.ScopeEnd

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.ScopeEnd  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.ScopeEnd Advantage TDataSet Descendant ade\_Scopeend Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.ScopeEnd  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm) [TAdsQuery](ade_tadsquery.htm)

Specifies the text of the ending scope for a dataset.

Syntax

property ScopeEnd: string;

Description

Use ScopeEnd to specify an indexed dataset filter. When ScopeEnd is applied to a dataset, only those records prior to the ScopeEnd are available to an application. ScopeEnd contains the string that is the value for the index. For example, the following ScopeEnd string displays only those records and prior where the indexed State field is anything before CA.

AdsTable1.ScopeEnd := CA;

To set a scope on indexes built on date, time, or timestamp fields, the date and time values must be formatted as text. The date should be formatted according to [DateFormat](ade_dateformat.htm). For example, to set a scope on a date index, an application might use "2/25/1997" as the value. To set a scope on a timestamp index, the value could be "2/25/1997 3:25pm".

ScopeEnd can be used in conjunction with [ScopeBegin](ade_scopebegin.htm).

Note Ranges are implemented internally as scopes. Ranges provide a very useful means to automatically produce the value necessary to set the scope. For this reason, use of ranges is easier and more versatile.