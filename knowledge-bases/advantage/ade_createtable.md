CreateTable




Advantage Database Server 12  

TAdsDataSet.CreateTable

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDataSet.CreateTable  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDataSet.CreateTable Advantage TDataSet Descendant ade\_Createtable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDataSet.CreateTable  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm)

Creates a new table.

Syntax

type TAdsCreateTableOptions = set of ( ctFreeTable, ctDictionaryTable );

 

procedure CreateTable();

procedure CreateTable( eOptions : TAdsCreateTableOptions );

Parameters (optional)

|  |  |
| --- | --- |
| eOptions | ctFreeTable creates a free table |
|  | ctDictionaryTable creates a table and adds it to the dictionary associated with the TAdsTable's connection. |

Description

CreateTable is used to create a new table defined by the current dataset's field definitions. If the table already exists, CreateTable will overwrite the tables data and structure. To avoid overwriting an existing table, check the Exists property before calling CreateTable. If the name of the table begins with the # character, the newly created table will be a [temporary table](master_temporary_tables.htm) that is only visible on the current connection.

If the FieldDefs property is populated, these values are used to create field definitions. Otherwise the Fields property is used. One or both of these properties be populated in order to create a table.

If the IndexDefs property is populated, its values are used to create indexes for the table.

The overloaded version of CreateTable allows the user to specify if the table should be added to an Advantage Data Dictionary or not. To add the table to a dictionary requires the user to have CREATE TABLE permissions or be the ADSSYS user. Using the regular CreateTable procedure or not specifying either ctFreeTable or ctDictionaryTable will default to the regular CreateTable behavior (ADSSYS automatically adds the table to a dictionary, normal users do not). Both ctFreeTable and ctDictionaryTable options cannot be specified together. Also, the ctDictionaryTable option is only valid when used on a dictionary connection and the ctDictionaryTable cannot be specified if the table is going to be a temporary table.

Note These methods cannot create tables with case insensitive character fields (cicharacter). The TFieldDef structures do not provide a mechanism for you to specify if you would like a ftString field to be case insensitive. To create a table with case insensitive fields at run-time either execute a CREATE TABLE statement via SQL, or call the extended method [AdsCreateTable](ade_adscreatetable.htm).