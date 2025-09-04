Creating Referential Integrity Objects with the ER Diagramming Tool




Advantage Database Server 12  

Creating Referential Integrity Objects with the ER Diagramming Tool

Advantage Data Architect

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating Referential Integrity Objects with the ER Diagramming Tool  Advantage Data Architect |  |  | Feedback on: Advantage Database Server 12 - Creating Referential Integrity Objects with the ER Diagramming Tool Advantage Data Architect arc\_Creating\_ri\_objects\_with\_the\_er\_diagramming\_tool Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Creating Referential Integrity Objects with the ER Diagramming Tool  Advantage Data Architect |  |  |  |  |

To create an RI object with the ER Diagramming Tool:

|  |  |
| --- | --- |
| 1. | Verify that the child and parent tables are on the ER View sheet. |

|  |  |
| --- | --- |
| 2. | Drag a field from the child table to the parent table. It does not matter which child field you drag to the parent table. |

|  |  |
| --- | --- |
| 3. | [Create a new RI object](arc_creating_or_modifying_an_ri_object.htm). |

|  |  |
| --- | --- |
| 4. | To put all records that do not meet the new constraint into a table, you will need to enter a path for a fail table. If you enter a path to an existing table, make sure it is the same format as the child table. If a path is entered to a table that does not exist, it will be created. |

|  |  |
| --- | --- |
| 5. | Click OK to create the RI object and a line will be drawn between the two tables, representing the relationship. |