BatchMove




Advantage Database Server 12  

BatchMove

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| BatchMove  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - BatchMove Advantage TDataSet Descendant ade\_Batchmove Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| BatchMove  Advantage TDataSet Descendant |  |  |  |  |

BatchMove provides a way to move a set of records from one table to another. BatchMove will accomplish the following:

|  |  |
| --- | --- |
| · | Copy records from one table to another |

|  |  |
| --- | --- |
| · | Update records from one table that occur in another table |

|  |  |
| --- | --- |
| · | Append records from one table to the end of another table |

|  |  |
| --- | --- |
| · | Delete records from one table that occur in another table |

The Advantage TDataSet Descendant does not implement the BatchMove function. Through the Advantage Extended Methods, the ability exists to copy the contents of a table completely or append contents of a table to another. The two methods are [AdsCopyTableContents](ade_adscopytablecontents.htm) and [AdsCopyTable](ade_adscopytable.htm). A distinct benefit of these two methods is that all copy operations occur on the server providing a distinct performance gain.

The following operations are not available with the Advantage solution:

|  |  |
| --- | --- |
| · | Update records in this table that occur in another table |

|  |  |
| --- | --- |
| · | Delete records in this table that occur in another table |

An Advantage component, [TAdsBatchMove](ade_tadsbatchmove.htm), is provided to help port applications that use the TBatchMove component.