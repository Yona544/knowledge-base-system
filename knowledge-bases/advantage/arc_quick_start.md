Quick Start




Advantage Database Server 12  

Quick Start

Advantage Data Architect

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Quick Start  Advantage Data Architect |  |  | Feedback on: Advantage Database Server 12 - Quick Start Advantage Data Architect arc\_Quick\_start Advantage Data Architect > Quick Start / Dear Support Staff, |  |
| Quick Start  Advantage Data Architect |  |  |  |  |

This topic is intended to provide a few steps to quickly familiarize you with the Connection Repository and the Table Designer, the two portions of the Advantage Data Architect (ARC) in which you will likely spend most of your time.

The following tasks are covered below:

|  |  |
| --- | --- |
| · | Creating a new connection and dictionary |

|  |  |
| --- | --- |
| · | Using the Connection Repository |

|  |  |
| --- | --- |
| · | Creating a new table and index |

|  |  |
| --- | --- |
| · | Restructuring a table |

|  |  |
| --- | --- |
| · | Creating a multi-field (multi-segment) index |

|  |  |
| --- | --- |
| · | Modifying connection properties |

Create a new connection

|  |  |
| --- | --- |
| 1. | Select File, Create New Data Dictionary from the main menu. |

|  |  |
| --- | --- |
| 2. | The bold fields are required, so fill in a name for your dictionary, select a server type, and enter a database path. |

|  |  |
| --- | --- |
| 3. | Click OK. A new connection will appear in the tree view on the left side of the application (the Connection Repository). |

Note You can also create a connection to a directory of free tables, if you do not want to use a data dictionary. To do this either use the New Connection Wizard (in the File menu), or select Connection, Create New Connection from the main menu.

Using the Connection Repository

Most functionality provided by the Connection Repository is accessed via quick menus. To activate a quick menu, right-click the object you want to work on. You can also right-click in the general tree view area to see the general Connection Repository menu.

For example, if you want to create a new view, right-click on the VIEWS node in the tree view, and select Create from the quick menu.

Creating a new table

|  |  |
| --- | --- |
| 1. | Type CTRL-N, or right-click on the TABLES node and select Create. You will be presented with the table designer. |

|  |  |
| --- | --- |
| 2. | To add new fields to the table, either start typing a field name immediately, or click the Add Field button, or type ALT-A. |

|  |  |
| --- | --- |
| 3. | For this example enter a field name of ID. |

|  |  |
| --- | --- |
| 4. | You can either TAB over to the field properties, or use your mouse. |

|  |  |
| --- | --- |
| 5. | Next, change the Data Type to integer. You can do this by typing the letter "i", or by dropping down the combo box and selecting integer from the list of field types. |

|  |  |
| --- | --- |
| 6. | To create an index on this new field, simply set the Index property to Primary. Take a moment to drop down the combo box and see the other options for the index property. Selecting Yes will create a simple single field index on this field. Unique will create a single field unique index on this field, etc. |

|  |  |
| --- | --- |
| 7. | Configure field-specific data dictionary properties, such as the fields maximum and minimum values. |

|  |  |
| --- | --- |
| 8. | To add another field, type ALT-A, or click the Add Field button. |

|  |  |
| --- | --- |
| 9. | Add a new field called mychar. Leave the default field properties (leave this as a character field of length 50), we will modify this field in the next example. |

|  |  |
| --- | --- |
| 10. | When you are finished defining your table, click the OK button. |

|  |  |
| --- | --- |
| 11. | Enter a name for the new table. |

|  |  |
| --- | --- |
| 12. | At this point, you will be prompted to open the new table. Feel free to open the table and add some data. |

Restructuring a table

|  |  |
| --- | --- |
| 1. | Lets change the length of the mychar field we defined in the previous example. There are two ways to activate the Table Designer on an existing table. If the table is already open, right-click in the grid area and select Properties from the quick menu. If the table is not open, right-click the table in the Connection Repository and select Properties from the quick menu. |

|  |  |
| --- | --- |
| 2. | Select the mychar field and change the Size property to 100. |

|  |  |
| --- | --- |
| 3. | Click OK. The table will be restructured. |

Adding a multi-field (multi-segment) index

|  |  |
| --- | --- |
| 1. | Right-click the table in the Connection Repository and select Properties from the quick menu. |

|  |  |
| --- | --- |
| 2. | Select the Additional Index Definitions tab. |

|  |  |
| --- | --- |
| 3. | Click the Add Index button. |

|  |  |
| --- | --- |
| 4. | Name your new index. |

|  |  |
| --- | --- |
| 5. | In the Index Fields or Expression property, enter id;mychar, which will create a new index based on the concatenation of the id and mychar fields. |

|  |  |
| --- | --- |
| 6. | Click OK. |

Modifying Connection Settings

|  |  |
| --- | --- |
| 1. | Right-click the database icon in the Connection Repository. This is the icon with the name you gave your data dictionary in the first example above. |

|  |  |
| --- | --- |
| 2. | Select Connection Properties from the quick menu. You will be presented with all connection-specific properties for this Connection Repository entry. |

|  |  |
| --- | --- |
| 3. | Change the BlankPassword property to yes. This property is very handy when developing new databases. If you leave your database password empty and set the BlankPassword property, you will not have to log in each time you open the database in ARC. |

|  |  |
| --- | --- |
| 4. | Click OK. |