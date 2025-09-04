sp\_CreateReferentialIntegrity




Advantage Database Server 12  

sp\_CreateReferentialIntegrity

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_CreateReferentialIntegrity  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_CreateReferentialIntegrity Advantage SQL Engine master\_Sp\_createreferentialintegrity Advantage SQL > System Procedures > Procedures > sp\_CreateReferentialIntegrity / Dear Support Staff, |  |
| sp\_CreateReferentialIntegrity  Advantage SQL Engine |  |  |  |  |

Adds a new referential integrity (RI) constraint to the data dictionary

Syntax

sp\_CreateReferentialIntegrity(

Name,CHARACTER,200,

PrimaryTable,CHARACTER,200,

ForeignTable,CHARACTER,200,

ForeignKey,CHARACTER,200,

UpdateRule,SHORTINT,

DeleteRule,SHORTINT,

FailTable,CHARACTER,515,

PrimaryKeyError,MEMO,

CascadeError,MEMO )

Parameters

|  |  |
| --- | --- |
| Name (I) | The name of the referential integrity constraint to be created. |
| ParentTable (I) | The data dictionary name of the table to be used as the parent in the RI relationship. |
| ChildTableName (I) | The data dictionary name of the table to be used as the child in the RI relationship. |
| ChildTagName (I) | The name of the existing index to be used as the foreign key in the RI relationship. |
| UpdateRule (I) | The action that the server is to perform when any update to the parent or foreign table does not maintain the referential integrity. The actions are: 1 for Cascade; 2 for Restrict; 3 for Set NULL; and 4 for Set Default. |
| DeleteRule (I) | That action that the server is to perform when a delete in the parent or foreign table does not maintain the referential integrity. The actions are: 1 for Cascade; 2 for Restrict; 3 for Set NULL; and 4 for Set Default. |
| FailTable (I) | The name of the file where records from the child table will be moved to if the foreign key that represents that record does not have a corresponding primary key in the parent table. If a file already exists by the same name, it is overwritten. This parameter is optional, so it may contain an empty string. If this parameter is NULL and if a record in the child key violates the new integrity rule, an error will be returned and the RI rule will not be created. If the child table is also a parent table in other relationships, this parameter will be treated as if it were NULL. |
| PrimaryKeyError (I) | An optional custom error message to return when a primary key violation is encountered. A NULL may be used to indicate you would like the default error message to be used. |
| CascadeError (I) | An optional custom error message to return when an error is encountered during a cascade operation. A NULL may be used to indicate you would like the default error message to be used. |

Remarks

sp\_CreateReferentialIntegrity is used to create a new referential integrity (RI) constraint for two tables in the database. RI ensures that for each row in a foreign key table (child), a corresponding row exists in the primary key table (parent). It also prevents a row in a parent from being deleted when a relationship exists to a child without the rule being enforced provided in either the UpdateRule or DeleteRule parameter. The parent table and the child table may be the same table.

The index expression in the primary key index and the index expression in the foreign key (ChildTagName) must have the identical number of fields. Each field in the primary key index and its corresponding field in the foreign key index must have identical types and sizes, but the names can differ. The primary key index must be denoted in the Advantage Data Dictionary as being the primary index. See AdsDDSetTableProperty when using with the property equal to ADS\_DD\_TABLE\_PRIMARY\_KEY.

Each record in the child table is associated with a key in the foreign index. Each foreign key must correspond to a key in the primary index of the parent table. The foreign index does not need to be unique, so a many to one relationship may exist. If the foreign key value is NULL for a record in the child table, then the record may exist in the child table, yet is not associated to any records of the parent table. If any one field used to produce the foreign key is NULL, then the key is NULL.

During the creation of the new RI constraint, the parent and child tables are open exclusively. Also, all tables that are in the data dictionary and that are interlinked with the child and parent tables through other RI constraints will need to be opened exclusively. Once the tables are opened, verification is performed to determine that all rules are met. If the FailTable parameter contains a filename, then every record in the child table that does not link to a row in the parent table is moved from the child table into a newly created table. If the FailTable parameter is NULL, then an error is returned that indicates the offending record. If the child table is also a parent in another RI constraint, then this operation is not possible. Moving records from the child table would destroy relationships to the children of this child table. If the child table is a parent in another RI constraint, then the FailTable parameter is ignored and treated as if it were set to NULL.

The update and delete rules determine the action performed when a parent record is modified such that the primary key is updated or deleted. The rule Cascade indicates to the Advantage Database Server that any changes to a record in the parent table that affect the primary key are to be performed to each corresponding field of each related record in the child table(s). The rule Restrict indicates that updates to the parent record that affect the primary key will fail and an error will be returned if referencing child records exist.

The rules Set NULL and Set Default are equivalent to Cascade. In the case of a parent record being updated and the primary key is changed, the corresponding fields in the child records must be updated. With Cascade, the fields are set to the same values as the parent record. All child records will continue to reference that exact same parent record although the primary and foreign keys have changed. With Set NULL, the fields in the child record are set to NULL values. With Set Default they are set to the default values that are denoted in the Advantage Data Dictionary. If a default value is not denoted, NULL is used. The rules Set NULL and Set Default result in the child records no longer referencing that parent record.

With the Cascade rule, all related child rows are deleted when a parent row is deleted. The Restrict rule disallows deleting a parent row that has related child rows. The Set NULL and the Set Default rules allow the parent row to be deleted and the fields of all child rows are set to the same values as discussed for update operations.

The entire set of interdependent tables affected by a set of RI rules is considered a graph. The tables are nodes in the graph and the RI rules are directed edges. Whenever any single table is opened by the client and is updated, the Advantage server will open all tables in the graph. When using the remote Advantage Database Server, this will be apparent since the number of server work areas will increase. If the client application opens the table with the ADS\_EXCLUSIVE option, then the entire set of tables will be opened exclusively at the server. No client, including the original one, will be able to open any of those tables.

Once a table is affected by an RI rule, there are a few limitations set. The function AdsCreateIndex may not be used to change the index expression of either the primary or foreign key indexes. The AdsZapTable function is not legal on a table affected by an RI rule. The FailTable parameter of AdsDDSetFieldProperty is ignored for any table that is a parent in an RI constraint. Prior to doing these, the RI rule must be deleted and then re-created.

Example

EXECUTE PROCEDURE sp\_CreateReferentialIntegrity(

salesreps\_has\_office,

offices,

salesreps,

rep\_office,

1,

1,

NULL,

An office does not exist with the specified office ID,

NULL );

See Also

[system.relations](master_system_relations.htm)

[sp\_DropReferentialIntegrity](master_sp_dropreferentialintegrity.htm)