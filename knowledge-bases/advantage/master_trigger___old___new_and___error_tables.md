Trigger \_\_old, \_\_new, and \_\_error tables




Advantage Database Server 12  

Trigger \_\_old, \_\_new, and \_\_error tables

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Trigger \_\_old, \_\_new, and \_\_error tables  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Trigger \_\_old, \_\_new, and \_\_error tables Advantage Concepts master\_Trigger\_\_\_old\_\_\_new\_and\_\_\_error\_tables Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Trigger \_\_old, \_\_new, and \_\_error tables  Advantage Concepts |  |  |  |  |

Three special in-memory tables are used by triggers; \_\_old, \_\_new, and \_\_error. These tables can be referenced using just their base names (i.e., \_\_new). For example, to read a value from the \_\_new table the following SQL statement can be executed:

SELECT empid FROM \_\_new

The \_\_new table is used when firing an INSERT or UPDATE trigger. It contains one row with the same field definitions as the base table on which the update was performed. The field values are the values that are about to be (in case of a BEFORE, or INSTEAD OF, or CONFLICT trigger) or were already (in case of an AFTER trigger) written to the table.

The \_\_old table is used when firing an UPDATE or DELETE trigger. It contains one row with the same field definitions as the base table on which the update was performed. The field values are the values that used to be in the table (immediately before the current update was performed).

The \_\_error table is used to return an error code and/or error string from inside of a trigger. The \_\_error table has the following table definition:

|  |  |
| --- | --- |
| INTEGER | errno |
| MEMO | message |

If your trigger code writes a row to this table, the Advantage server will read the error number and message from the \_\_error table and return them to the client as a native exception or error code (depending on which client you are using). The errno field is optional, and if left empty, a default trigger failure error code will be returned to the client.

You can make changes to the data values in the \_\_new and \_\_old tables but these changes will not be reflected in the record update or insert operation. To make changes to the values provided by the client, use an INSTEAD OF trigger, change any data values in the \_\_new table you wish to modify, then post the \_\_new record manually. The example below is an INSTEAD OF INSERT trigger that modifies the date\_inserted field and puts the current date and time into that field:

UPDATE \_\_new SET date\_inserted = (SELECT now() FROM system.iota);

INSERT INTO mytable SELECT \* FROM \_\_new;