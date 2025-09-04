Advantage TDataSet Descendant Architecture




Advantage Database Server 12  

Advantage TDataSet Descendant Architecture

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage TDataSet Descendant Architecture  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Advantage TDataSet Descendant Architecture Advantage TDataSet Descendant ade\_Advantage\_tdataset\_descendant\_architecture Advantage TDataSet Descendant > Developing and Distributing Applications > Advantage TDataSet Descendant Architecture / Dear Support Staff, |  |
| Advantage TDataSet Descendant Architecture  Advantage TDataSet Descendant |  |  |  |  |

The TDataSet component Delph and C++Builder is an abstract class that does not access the BDE or dbExpress directly. Instead, this class relies on descendants to provide concrete methods. For example, TTable is a concrete descendant. TTable completely encapsulates access to the BDE. The Advantage TAdsTable component is also a concrete descendant, but does not require the BDE.

Advantage TDataSet Descendant for Delphi and C++Builder

The Advantage TDataSet Descendant solution provides four key components, [TAdsQuery](ade_tadsquery.htm), [TAdsTable](ade_tadstable_7.htm), [TAdsStoredProc](ade_tadsstoredproc.htm), and [TAdsConnection](ade_tadsconnection_7.htm). TAdsQuery, TAdsTable, TAdsStoredProc, and TAdsConnection are TDataSet descendants similar to Delphi's TQuery, TTable, TStoredProc, and TDatabase components. Because these components are similar, you can use TAdsQuery, TAdsTable, TAdsStoredProc, and TAdsConnection exactly as you would TQuery, TTable, TStoredProc, and TDatabase. In fact, your application will have to change very little except it will now have the benefit of using Advantage technology. Application deployment can be as simple as including the required Advantage DLLs in your application directory. The architecture of TAdsQuery, TAdsTable, TAdsStoredProc, and TAdsConnection allows the use of Delphi native data aware components plus any third-party components that are TDataSet descendant compatible.

The Advantage TDataSet Descendant solution also provides components such as the [TAdsSettings](ade_tadssettings_7.htm) component for environmental settings such as date format, and the [TAdsDictionary](ade_tadsdictionary.htm) component to provide administrative access to Advantage Data Dictionaries.

Note The Advantage TDataSet Descendant does not need a component equivalent to TSession. It is simply not required. The Advantage table and query components used in your applications can be referenced or created in the TThread.Execute body.

A connection manager is included in a stand-alone utility called [Advantage Data Architect](ade_advantage_data_architect.htm) (ARC). This functionality in ARC allows you to set up aliases similar to Delphi database aliases. The ARC utility is a separate install that is located on the Advantage Product CD and also available for download from the Advantage Developer's Zone at <http://DevZone.AdvantageDatabase.com>