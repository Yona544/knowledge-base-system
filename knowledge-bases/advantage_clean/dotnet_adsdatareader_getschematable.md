---
title: Dotnet Adsdatareader Getschematable
slug: dotnet_adsdatareader_getschematable
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdatareader_getschematable.htm
source: Advantage CHM
tags:
  - dotnet
checksum: d88c40cf2ce553095a0f9250b349e1a3f309a6ee
---

# Dotnet Adsdatareader Getschematable

AdsDataReader.GetSchemaTable

AdsDataReader.GetSchemaTable

Advantage .NET Data Provider

| AdsDataReader.GetSchemaTable  Advantage .NET Data Provider |  |  |  |  |

Returns a DataTable that describes the column metadata of the AdsDataReader.

public DataTable GetSchemaTable();

Remarks

The DataTable object type is implemented in the .NET framework. It represents a single in-memory table. GetSchemaTable creates a new instance of a DataTable and populates it with rows and columns that describe the schema of the AdsDataReader object. The DataTable will contain one row for each column in the AdsDataReader result set. The columns of the DataTable returned by GetSchemaTable are described below.

| Column | Description |
| ColumnName | The name of the column; this might not be unique. If this cannot be determined, a null value is returned. This name always reflects the most recent renaming of the column in the current view or command text. |
| ColumnOrdinal | The zero-based ordinal of the column. |
| ColumnSize | The maximum possible length of a value in the column. For columns that use a fixed-length data type, this is the size of the data type. |
| NumericPrecision | If ProviderType is a numeric data type, this is the maximum precision of the column. The precision depends on the definition of the column. If ProviderType is not a numeric data type, this is a null value. |
| NumericScale | This represents the scale (in general, the number of digits to the right of the decimal point) of the type. For non-numeric types, this will have a null value. |
| DataType | Maps to the .Net Framework type of the column. |
| ProviderType | This is an integer value representing the underlying Advantage type. |
| IsLong | True if the column contains a Binary Long Object (BLOB) or memo data. |
| AllowDBNull | True if the column can be set to a null value. |
| IsReadOnly | True if the column can be modified. |
| IsRowVersion | True if the column contains a persistent row identifier that cannot be written to, and has no meaningful value except to identity the row. This will be TRUE for RowVersion fields and FALSE for all other field types. |
| IsUnique | True if no two rows in the base table-the table returned in BaseTableName-can have the same value in this column. IsUnique is guaranteed to be True if the column constitutes a key by itself. False if the column can contain duplicate values in the base table. |
| IsKeyColumn, or IsKey | True if the column is one of a set of columns in the rowset that, taken together, uniquely identify the row. The set of columns with IsKey set to True must uniquely identify a row in the rowset. If the base table has a primary key defined in the data dictionary, then that column(s) is/are identified by IsKey. Otherwise, IsKey will identify an autoinc or any column with a UNIQUE index built on it. False if the column is not required to uniquely identify the row. For compatibility with the official IDataReader specification, this is named IsKeyColumn. For compatibility with the Microsoft .NET data providers, though, we also support IsKey. |
| IsAutoIncrement | True if the column is an auto-increment field filled in by the server. |
| BaseSchemaName | This is always null with the Advantage .NET Data Provider. |
| BaseCatalogName | The name of the catalog (data dictionary) in the data store that contains the column. This is currently only set for linked tables. It is null for all other tables including free tables and data dictionary bound tables that are not linked. |
| BaseTableName | The name of the table or view in the data store that contains the column. A null value if the base table name cannot be determined. The default of this column is a null value. |
| BaseColumnName | The name of the column in the data store. This might be different than the column name returned in the ColumnName column if an alias was used. A null value if the base column name cannot be determined or if the rowset column is derived, but not identical to, a column in the data store. |
| IsAliased | True if the column name is an alias; otherwise False. |
| CaseSensitive | True if the column is case sensitive, False if the column is case insensitive. |
| ProviderTypeName | This is a string value with the underlying Advantage data type name. It is the name that can be used in an SQL statement to create a field of the represented type. |

Example

This example gets a schema table for a table and prints some of the columns.

// create a connection object

AdsConnection conn = new AdsConnection( "data source=c:\\data;" );

AdsCommand cmd;

AdsDataReader reader;

 

try

{

 

// make the connection to the server

conn.Open();

 

// create a command object

cmd = conn.CreateCommand();

 

// specify an SQL statement

cmd.CommandText = "select \* from departments";

 

// get the schema for the table

reader = cmd.ExecuteReader( CommandBehavior.SchemaOnly );

 

// get the schema table itself

DataTable datatable = reader.GetSchemaTable();

 

// print some schema information

foreach ( DataRow row in datatable.Rows )

{

Console.Write( row["ColumnName"] );

Console.Write( "\t" + row["DataType"].ToString() );

Console.WriteLine( "\t" + row["IsKey"].ToString() );

}

 

conn.Close();
