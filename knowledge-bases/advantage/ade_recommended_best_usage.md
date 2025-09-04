Recommended Best Usage




Advantage Database Server 12  

Recommended Best Usage

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Recommended Best Usage  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Recommended Best Usage Advantage TDataSet Descendant ade\_Recommended\_best\_usage Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Recommended Best Usage  Advantage TDataSet Descendant |  |  |  |  |

When programming with the Advantage TDataSet Descendant, our goal is for the developer to use standard Delphi TTable, TQuery, and TStoredProc programming techniques. There are extended TAdsTable methods provided as a wrapper to the Advantage Client Engine API, however these should be used only when the equivalent functionality is not available with TDataSet methods. For example, if when using a standard TTable you included the statement Table.First, when accessing an Advantage table you would use the same method, AdvantageTable.First.

The Advantage Technical Services team maintains an application available from the download area of the Advantage Developer Zone Web site (http://DevZone.AdvantageDatabase.com) that covers the most common topics in Advantage/Delphi programming. The application is intended to be an example of best programming techniques and is updated on a regular basis. The following are some of the topics addressed by this example application:

|  |  |
| --- | --- |
| · | Filters and how they can be used for extremely fast data manipulation |

|  |  |
| --- | --- |
| · | Creating tables and indexes programmatically |

|  |  |
| --- | --- |
| · | Ranges versus scopes |

|  |  |
| --- | --- |
| · | Master/detail relationships |

|  |  |
| --- | --- |
| · | Transaction processing |

|  |  |
| --- | --- |
| · | Encryption |

|  |  |
| --- | --- |
| · | Finding data via FindKey, FindNearest, GotoKey, GotoNearest, Locate and Lookup methods |

|  |  |
| --- | --- |
| · | How to gracefully handle record locking |

|  |  |
| --- | --- |
| · | Multi-threaded Advantage database applications |