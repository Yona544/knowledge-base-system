---
title: Master Create Table
slug: master_create_table
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_create_table.htm
source: Advantage CHM
tags:
  - master
checksum: 356ee40bd34a6b699232533285279c32173b2290
---

# Master Create Table

CREATE TABLE

CREATE TABLE

Advantage SQL Engine

| CREATE TABLE  Advantage SQL Engine |  |  |  |  |

Creates a new table in the database

Syntax

CREATE TABLE <table-name> ( <column-info> [,<column-info>...] )

 [IN DATABASE | AS FREE TABLE]

 [IGNORE TRANSACTIONS]

 [MEMOBLOCKSIZE <blocksize>]

column-info ::= <column-identifier> <data-type> [<option>] [<column-constraint>] |

<table-constraint>

data-type ::= type-name | type-name (integer) | type-name (integer, integer)

type-name ::= a supported data type (see [Supported Data Types](master_supported_data_types_in_the_advantage_sql_engine.md))

blocksize ::= An integer value specifying the memo block size for the new table.

 

| column constraint ::= | CONSTRAINT NOT NULL |  CONSTRAINT MINIMUM <max-column-value> |  CONSTRAINT MAXIMUM <min-column-value> |  CONSTRAINT ERROR MESSAGE <error-message> |  DEFAULT <default-column-value> |  [CONSTRAINT <index-name>] PRIMARY KEY |
| option ::= | <vfp-option> | <adt-option>    <vfp-option> ::= NULL | NOT NULL | NOCPTRANS  These options apply to Visual FoxPro tables (ADS\_VFP) and can be used with free tables) and data dictionary tables). The NULL (and NOT NULL) option indicate whether the column will be able to physically hold a NULL value. This is different from a NOT NULL constraint. If a Visual FoxPro column is created without the NULL option, then an error will be generated if an attempt is made to store a NULL in that column. The NOCPTRANS option applies to Visual FoxPro character and memo field types. If this option is provided, the data will not be translated across codepages (ANSI/OEM conversions).  <adt-option> ::= COMPRESSED  This option applies to ADT tables (ADS\_ADT) and can be used with free tables) and data dictionary tables). The option is only valid with data type MEMO, NMEMO and BLOB. When this option is specified, the data for the field will be stored on disk in compressed format. |
| table-constraint ::= | [CONSTRAINT <index-name>] PRIMARY KEY  ( <column-identifier> [DESC|ASC] [,<column-identifier> [DESC|ASC]] ) |
| index-name ::= | A user-defined index name. |

 

error-message ::= A string literal to be returned as the error message when the column constraints are violated.

max-column-value ::= A string literal (i.e., surrounded by single quotes) containing an Advantage expression. The evaluated expression result must be of the same type as the column type. The result will be used as the maximum value for the column. (For more information about expressions, see [Advantage Expression Engine](master_advantage_expression_engine.md).)

min-column-value ::= A string literal (i.e., surrounded by single quotes) containing an Advantage expression. The evaluated expression result must be of the same type as the column type. The result will be used as the minimum value for the column. (For more information about expressions, see [Advantage Expression Engine](master_advantage_expression_engine.md).)

default-column-value::= A string literal (i.e., surrounded by single quotes) containing an Advantage expression. The evaluated expression result must be of the same type as the column type. The result will be used as default value for the column when new records are added or the ADS\_DD\_RI\_SETDEFAULT rule is used in referential integrity. (For more information about expressions, see [Advantage Expression Engine](master_advantage_expression_engine.md).)

Remarks

UNIQUE columns are supported through a unique index.

The IN DATABASE and AS FREE TABLE clauses specify whether or not the new table is to be added to the current database. These modifiers only apply to database connections). Furthermore, the current user must have CREATE TABLE permissions to add a table to a database. If neither one is specified and the current user is the dictionary administrator (ADSSYS), the newly created table will become part of the database. Conversely, if the current user is a regular user, the newly created table will be a free table.

The optional IGNORE TRANSACTIONS clause specifies that the table should be created as a [transaction-free table](master_transaction_free_tables.md), which will be excluded from the scope of any active transaction.

The optional MEMOBLOCKSIZE clause allows a memo block size other than the default to be specified when creating a new table. Valid sizes for ADT tables are 8 - 32768. Valid memo block sizes for CDX and VFP table types are 33 - 1024.

The column level constraints can only be specified if the statement is executed by a user with CREATE TABLE permissions on a database connection. An error will be returned if column level constraints are specified and the current user does not have the CREATE TABLE permissions.

Defining a primary key is only supported with ADT and Visual FoxPro (VFP) table types and can be accomplished in two ways: as a column-constraint that is defined per column, or as a table-constraint that is defined as a separate item in the list of column definitions. When a primary key is defined, a unique index is built using the field or fields designated and then added to an auto-open index file. If the query is using a database connection, the index is added to the data dictionary and designated as the primary key. If a free connection) was used, the resulting table will be a free table and the index will be created, but no primary key can be designated, as that functionality is supported only within a data dictionary. If using the optional constraint syntax (CONSTRAINT <index-name>) in front of the PRIMARY KEY keywords, the index being added to the auto-open index file will be named <index-name>. If the optional syntax is not used, Advantage will name it "pk\_<table-name>" where <table-name> is the name of the table being created.

For a list of data types supported by the Advantage SQL engine, see [Supported Data Types in the Advantage SQL Engine](master_supported_data_types_in_the_advantage_sql_engine.md).

Examples:

CREATE TABLE sal (emp\_id short, salary double, dept char(20));

 

CREATE TABLE emp (emp\_id short, name char(50), hire\_date date, married logical);

 

CREATE TABLE test (

 field1 INTEGER

 DEFAULT 45

 CONSTRAINT MINIMUM 2

 CONSTRAINT MAXIMUM 169

 CONSTRAINT NOT NULL

 CONSTRAINT ERROR MESSAGE you entered a bad value.,

 field2 CHAR(2) );

 

CREATE TABLE table1 ( field1 CHAR(10),

 field2 INTEGER PRIMARY KEY );

 

CREATE TABLE table1 ( field1 CHAR(10),

 field2 INTEGER,

 PRIMARY KEY( field1, field2 DESC ) );

 

CREATE TABLE table1 ( field1 INTEGER CONSTRAINT index1 PRIMARY KEY );

 

CREATE TABLE table1 ( field1 INTEGER,

 CONSTRAINT index1 PRIMARY KEY( field1 ASC ) );

 

// Create a table that (when using VFP table type) will allow the

// columns to be nullable and prevent codepage translations from being

// performed on the character field.

CREATE TABLE vfptable ( field1 CHAR(10) NULL NOCPTRANS, field2 INTEGER NULL );

 

CREATE TABLE test (i INTEGER, m MEMO )

 MEMOBLOCKSIZE 512;
