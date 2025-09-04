AdsConnection




Advantage Database Server 12  

TAdsTable/TAdsQuery.AdsConnection

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.AdsConnection  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.AdsConnection Advantage TDataSet Descendant ade\_Adsconnection Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.AdsConnection  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm) [TAdsQuery](ade_tadsquery.htm)

A reference to a TAdsConnection component instance.

Syntax

property AdsConnection: TAdsConnection;

Description

The AdsConnection property is used to associate a TAdsTable or TAdsQuery component with a TAdsConnection component, which is used to manage Advantage server connections.

This property can be used in place of the [DatabaseName](ade_databasename.htm) property. It is more efficient and it is thread-safe.

When writing multi-threaded applications, or libraries that will be consumed by multi-threaded applications, it is more efficient and thread-safe to use the AdsConnection property instead of the DatabaseName property. Assigning the pointer to the AdsConnection directly is safer than relying on the name resolution logic used when setting the DatabaseName property.