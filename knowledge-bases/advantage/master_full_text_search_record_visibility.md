Full Text Search Record Visibility




Advantage Database Server 12  

Full Text Search Record Visibility

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Full Text Search Record Visibility  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Full Text Search Record Visibility Advantage Concepts master\_Full\_text\_search\_record\_visibility Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Full Text Search Record Visibility  Advantage Concepts |  |  |  |  |

The CONTAINS() function is only evaluated at the server; it is never evaluated at the client. This primarily affects the Advantage TDataSet Descendant, which normally checks visibility of records at the client to keep result sets completely accurate. For example, if a TAdsTable instance has a filter of the form "lastname = Smith" and you edit a lastname value and change it from "Smith" to "Jones", that record will be removed from the result set because it no longer passes the filter condition. The most obvious case of this is when you edit the record in a grid; it will be removed from the grid after the edit.

Because the CONTAINS() function is only evaluated at the server, however, the record visibility will not be checked for that function. So, for example, if a filter (or SQL WHERE clause) has the expression "CONTAINS( lastname, Smith )" and you change "Smith" to "Jones" in the grid, that record will still be visible until you re-execute the filter or query.