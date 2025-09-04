---
title: Master Alter Table
slug: master_alter_table
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_alter_table.htm
source: Advantage CHM
tags:
  - master
checksum: 3b1b444b47e7061bd2c34b54f86196073d369110
---

# Master Alter Table

ALTER TABLE

ALTER TABLE

Advantage SQL Engine

| ALTER TABLE  Advantage SQL Engine |  |  |  |  |

Modifies the structure of a table and adds or deletes column constraints

Syntax

ALTER [ONLINE | ONLINE\_WITH\_TRANSITION] TABLE <table-name><action>[<action>]

action ::= ADD [COLUMN] <column-info> [<position-info>] |

ALTER [COLUMN] <original-column-identifier> <column-info> [<position-info>] |

ALTER [COLUMN] <column-identifier> DROP <drop-column-constraint> |

DROP [COLUMN] <column-identifier> |

DROP <drop-table-constraint> |

MEMOBLOCKSIZE <blocksize> |

[IGNORE | RESPECT] TRANSACTIONS

column-identifier ::= A user defined column name.

original-column-identifier ::= The existing (or original) user-defined column name.

column-info ::= <column-identifier> <data-type> [<vfp-option>] [<column-constraints> ]

data-type ::= type-name | type-name (integer) | type-name (integer, integer)

type-name ::= A supported data type (see the next section Supported Data Types).

position-info ::= [ POSITION integer ] A 1 based index of the columns position in the table after the restructure.

blocksize ::= An integer value specifying the memo block size for the altered table.

| column constraints ::= | [CONSTRAINT NOT NULL] |  [CONSTRAINT MINIMUM <max-column-value>] |  [CONSTRAINT MAXIMUM <min-column-value>] |  [CONSTRAINT ERROR MESSAGE <error-message>] |  [DEFAULT <default-column-value>] |
| vfp-option ::= | NULL | NOT NULL | NOCPTRANS  These options apply to Visual FoxPro tables (ADS\_VFP) and can be used with free tables) and data dictionary tables). The NULL (and NOT NULL) option indicate whether the column will be able to physically hold a NULL value. This is different from a NOT NULL constraint. If a Visual FoxPro column is created without the NULL option, then an error will be generated if an attempt is made to store a NULL in that column. The NOCPTRANS option applies to Visual FoxPro character and memo field types. If this option is provided, the data will not be translated across codepages (ANSI/OEM conversions). |

drop-column-constraint::= NOT NULL | MINIMUM | MAXIMUM | ERROR MESSAGE | DEFAULT

drop-table-constraint ::= [CONSTRAINT] PRIMARY KEY

error-message ::= A string literal to be returned as the error message when the column constraints are violated.

max-column-value ::= A string literal (i.e., surrounded by single quotes) containing an Advantage expression. The evaluated expression result must be of the same type as the column type. The result will be used as the maximum value for the column. (For more information about expressions, see [Advantage Expression Engine](master_advantage_expression_engine.md).)

min-column-value ::= A string literal (i.e., surrounded by single quotes) containing an Advantage expression. The evaluated expression result must be of the same type as the column type. The result will be used as the minimum value for the column. (For more information about expressions, see [Advantage Expression Engine](master_advantage_expression_engine.md).)

default-column-value::= A string literal (i.e., surrounded by single quotes) containing an Advantage expression. The evaluated expression result must be of the same type as the column type. The result will be used as default value for the column when new records are added or the ADS\_DD\_RI\_SETDEFAULT rule is used in referential integrity. (For more information about expressions, see [Advantage Expression Engine](master_advantage_expression_engine.md).)

Remarks

If the table is a database table), that is, if the table is associated with an [Advantage Data Dictionary](master_advantage_data_dictionary.md), the table can only be altered by users with ALTER permissions for that specific table. If the table is free table), the table can only be altered on a free connection).

If dropping a primary key table-constraint, the primary key setting for the associated index will be set to False. The index will still remain, however. Should the index need to be removed, use the [DROP INDEX](master_drop_index.md) statement.

The ONLINE and ONLINE\_WITH\_TRANSITION keywords perform the alter of the table while the table is opened shared.  This operation is only supported on remote server connections.  If the table is already opened by another user it must be opened using proprietary locking.  If the table is not already open, Advantage will open it with proprietary locking and any requests to open it during the alter must use proprietary locking.  See [Online Table Maintenance](master_online_table_maintenance.md) for important information about how online alter works.

The MEMOBLOCKSIZE clause allows a new memo block size to be specified when altering the table. Valid sizes for ADT tables are 8 - 32768. Valid memo block sizes for CDX and VFP table types are 33 - 1024.

The IGNORE or RESPECT TRANSACTIONS clause turns on or off the [transaction-free](master_transaction_free_tables.md) setting of the table.

Note When restructuring a table and changing an integer field to an auto increment (autoinc) field type, Advantage does not verify the uniqueness of the existing integer values. It preserves the existing values and sets the next auto increment value (for the next appended record) to be the maximum existing integer value plus one. You can test the uniqueness of integer field values prior to changing the structure of the table by building a unique index on the field.

Example

ALTER TABLE salesreps ADD COLUMN region char(40);

ALTER ONLINE TABLE customers ADD address3 char(40) ADD COLUMN refund integer;

ALTER TABLE orders ALTER COLUMN price price curdouble;

ALTER ONLINE TABLE offices ALTER COLUMN mgr mgr integer DEFAULT '104';

ALTER TABLE salesreps ALTER name name char(40) CONSTRAINT NOT NULL;

 

ALTER TABLE demo10

ADD COLUMN test char(20)

 DEFAULT abcde

 CONSTRAINT MINIMUM A

 CONSTRAINT MAXIMUM z

 CONSTRAINT NOT NULL

CONSTRAINT error message A bad value was input for the column named test

ADD COLUMN test2 SHORT

 DEFAULT 45

 CONSTRAINT MINIMUM 2

 CONSTRAINT MAXIMUM 169

 CONSTRAINT NOT NULL

 CONSTRAINT error message An invalid values was set in the column named test2

ALTER COLUMN lastname lastnamechanged char(40)

 DEFAULT Donahue

 CONSTRAINT MINIMUM A

 CONSTRAINT MAXIMUM Z

 CONSTRAINT error message An invalid lastnamechanged was input

ALTER COLUMN firstname firstnamechanged char(30)

DROP deptnum

DROP dateofhire;

 

ALTER table demo10

 ALTER COLUMN lastnamechanged DROP DEFAULT

 ALTER COLUMN lastnamechanged DROP MINIMUM

 ALTER COLUMN lastnamechanged DROP MAXIMUM

 ALTER COLUMN lastnamechanged DROP error message

 ALTER COLUMN lastnamechanged DROP NOT NULL

 ALTER TABLE table1 DROP CONSTRAINT PRIMAY KEY

 ALTER TABLE table1 DROP PRIMARY KEY;

 

ALTER ONLINE TABLE salesreps ALTER COLUMN region region char(60)

 MEMOBLOCKSIZE 512;

 

ALTER TABLE audit\_log IGNORE TRANSACTIONS;
