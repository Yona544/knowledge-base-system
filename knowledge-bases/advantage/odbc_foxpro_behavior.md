FoxPro Behavior




Advantage Database Server 12  

FoxPro Behavior

Advantage ODBC Driver

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| FoxPro Behavior  Advantage ODBC Driver |  |  | Feedback on: Advantage Database Server 12 - FoxPro Behavior Advantage ODBC Driver odbc\_Foxpro\_behavior Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| FoxPro Behavior  Advantage ODBC Driver |  |  |  |  |

If the [Table Type](odbc_table_type.htm) is FoxPro or Visual FoxPro, structural CDX indexes (those indexes which have the same base names as the database files) are opened implicitly. In this case they are automatically selected and no additional Data Source setup is required.

When creating indexes, "tags" (similar to individual index files) are added to the structural index. If a structural index does not exist, one will be created and the tag will be inserted.