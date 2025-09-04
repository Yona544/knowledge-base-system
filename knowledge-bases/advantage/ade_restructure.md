Restructure




Advantage Database Server 12  

TAdsTable.Restructure

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.Restructure  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.Restructure Advantage TDataSet Descendant ade\_Restructure Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.Restructure  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm)

Adds, removes, or changes field definitions for a table

Syntax

procedure Restructure( const strAddFields, strDeleteFields, strChangeFields :

string );

Parameters

|  |  |
| --- | --- |
| strAddFields | Field descriptions of the form: fieldname,type,length,decimals,(order);. For example: EMPID,Numeric,5,0;DEPT,Char,20,(3) |
| strDeleteFields | Field descriptions of the form: fieldname;. For example: EMPID,LASTNAME |
| strChangeFields | Field descriptions of the form: oldfieldname,newfieldname,type,length,decimals,;. For example: EMPID,Employee ID,Numeric,5,0;DEPT, Department, Char,20 , (1) |

Description

CAUTION Restructure significantly modifies existing tables and may result in data loss. Prior to using this function, the table to be modified should be backed up. If the table is part of a data dictionary, then the entire database should be backed up. The original table file, memo file, and index files will be renamed by the Advantage Client Engine and left in the same directory. Multiple calls to this function will cause the previously renamed files to be overwritten.

Restructure provides the capability to add, delete, or change field definitions within a table. The table may be in a free table or a database table. If the table is associated with a database, then this TAdsTable instance must be associated with a TAdsConnection component that is connected to the Advantage data dictionary using the Administrator account.

This function will open the table exclusively, so the table may not be opened elsewhere. If the table is part of a database, then all tables interlinked with referential integrity rules will also be opened exclusively.

Restructure will fail if:

|  |  |
| --- | --- |
| · | A field to be deleted is used in any index. |

|  |  |
| --- | --- |
| · | A field to be deleted is used in the record level constraint. |

|  |  |
| --- | --- |
| · | A field change includes altering the width or type of the field that is part of any index used as a primary or foreign key in a referential integrity constraint. |

|  |  |
| --- | --- |
| · | Any indexes exist for the table that were built using the ADS\_CUSTOM value in the options parameter. |

|  |  |
| --- | --- |
| · | The table is part of a dictionary and the current user does not have ALTER permissions for the specified table. |

|  |  |
| --- | --- |
| · | The table cannot be opened exclusively. |

If any of these limitations exist, you may delete the offending indexes or constraint and try again.

The parameters named strAddFields, strDeleteFields, and strChangeFields are comprised of semicolon delimited lists of fields to be manipulated. The strAddFields is identical to the field definitions passed into AdsCreateTable with one optional, additional parameter. If desired, the field definition can be appended with a comma followed with an integer within parentheses (ex ,(3)). That integer will indicate the position of the field within the table. For example, lastname, char, 20, (2); employee id, autoinc, (3) will add two fields into the second and third positions within sequence of fields in the table. The strDeleteFields parameter is simply a list of existing fields to be deleted. An example to delete two fields is customer;date. The last parameter, strChangeFields, is the same as a field definition that is passed to AdsCreateTable except that it is preceded with the original field name. The second field name is the renamed field name. Regardless of what is being changed in the field (the name, size, or type). All values are required. An example that changes the field name lastname to the new name last name is: lastname, last name, char, 20. If desired, the field definition can be appended with a comma followed with an integer within parentheses (ex ,(3)). That integer will indicate the position of the field within the table. For example, Lastname, Lastname, char, 20, (5) will move the field Lastname to the fifth position in the field list.

Note This function is illegal in a transaction.

Supported Data Types

For information about supported data types, see [ADT Field Types and Specifications](master_adt_field_types_and_specifications.htm) and

[DBF Field Types and Specifications](master_dbf_field_types_and_specifications.htm)

Example

Restructure( NewCharField,ch,30,(3);NewIntField,integer,(4);,

Date; Time,

doublefield,NewNameForDouble,double,10,2 );

Remarks

When restructuring a table and changing an integer field to an auto increment (autoinc) field type, Advantage does not verify the uniqueness of the existing integer values. It preserves the existing values and sets the next auto increment value (for the next appended record) to be the maximum existing integer value plus one. You can test the uniqueness of integer field values prior to changing the structure of the table by building a unique index on the field.