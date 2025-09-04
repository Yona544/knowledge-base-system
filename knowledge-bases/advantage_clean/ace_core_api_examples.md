---
title: Ace Core Api Examples
slug: ace_core_api_examples
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_core_api_examples.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 3941fdf48d0b349198ce0dbfc14297967df16801
---

# Ace Core Api Examples

Core API Examples

Core API Examples

Advantage Client Engine

| Core API Examples  Advantage Client Engine |  |  |  |  |

The following is a set of simple examples that demonstrate some of the core APIs using C.  The code is written to compile and run on a Windows machine that has a Visual Studio compiler installed. Due to the connection and table open APIs that it uses, it requires Advantage version 10.1 or greater. Those calls (AdsConnect101 and AdsCreateTable101) could be changed to older APIs, and the rest of the code would work with older versions of Advantage.

The example code is meant to show how to use the Advantage Client Engine (ACE) API to accomplish some basic tasks including creating and indexing tables, adding data to tables, searching for data with indexes, filtering data, reading data, and traversing result sets. Tasks are accomplished using both table-based and SQL-based approaches.

To run this example on your own system, make sure that the DB\_PATH macro points to a valid folder. To build and step through the code:

- Create a new Win32 console application with Visual Studio

- Add a source file with the code below to the project

- Put ace.h in the same folder as the source file (or change the #include to reference it in another location).

- Add ace32.lib to linker input options.

You should also be able to build it from the command line if you have the Visual Studio compiler in your path:

   [c:\example]cl ACEExamples.c ace32.lib

#include <windows.h>

#include <stdio.h>

#include <string.h>

#include <assert.h>

#include "ace.h"

// Define a base path to use

#define DB\_PATH  "c:\\examples\\"

// Define a macro for some generic error handling logic.  The CreateSampleTable

// function shows some possible error handling a little more explicitly.  The

// remaining functions (for brevity) use this macro for bailing out and handling

// cleanup.

#define CHECK\_ERROR( ulRet )            \

    if ( ulRet != AE\_SUCCESS )         \

       {                               \

          DisplayLastError();          \

          goto FunctionExit;           \

       }

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*  Module       : DisplayLastError

\*  Return       : none

\*  Desc         : Show the ACE error from the most recent API call.  Note that

\*                 the "last" error is cleared in the entry code of every ACE API

\*                 (except for AdsGetLastError).

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

void DisplayLastError( void )

{

  UNSIGNED32 ulRet;

  UNSIGNED8  aucError[ADS\_MAX\_ERROR\_LEN];

  UNSIGNED16 usLen;

  // Retrieve the most recent error.

  usLen = sizeof( aucError );

  AdsGetLastError( &ulRet, aucError, &usLen );

  if ( ulRet != AE\_SUCCESS )

     // there was an error.  Print it out

     printf( "%s\n", aucError );

}

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*  Module   : CreateSampleTable

\*  Return   : AE\_SUCCESS or ACE error code

\*  Desc     : Create a simple table and put a couple indexes on it.

\*             This example function handles each error specifically for

\*             demonstration purposes.  The other samples use an "assert" style

\*             macro to attempt to make the code more readable.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 CreateSampleTable( void )

{

  UNSIGNED32 ulRet;

  ADSHANDLE  hConn = 0;

  ADSHANDLE  hTable;

  ADSHANDLE  hIndex;

  ADSHANDLE  hStmt;

  /\*

   \* Connect to the "database".  In this example, the database is a connection to

   \* a directory of free tables (tables that are not in a data dictionary).  Using

   \* a dictionary provides additional capabilities (referential integrity, stored

   \* procedures, triggers, field constraints, etc.).

   \* In this connect call, specify the server type as "local", which uses the

   \* in-process Advantage database engine (adsloc32.dll in a 32-bit process).

   \* Specifying "remote" would attempt to connect to Advantage Database Server

   \* (client/server).

   \*/

  ulRet = AdsConnect101( "Data source = " DB\_PATH ";"

                         "ServerType=local;", NULL, &hConn );

  if ( ulRet != AE\_SUCCESS )

     {

     DisplayLastError();

     return ulRet;

     }

  /\*

   \* Create a simple table to use in the examples. One of the 17 basic laws of the

   \* universe requires that at least 87.6% of all sample DB applications use a

   \* "customer" table and/or an "employee" table. This sample will follow suit in

   \* order to help prevent the cosmos from winking out of existence.

   \*

   \* NOTE: AdsCreateTable90 will overwrite an existing table.  The equivalent SQL

   \* CREATE TABLE statement will not overwrite an existing table.

   \*/

  ulRet = AdsCreateTable90( hConn, DB\_PATH "employees.adt",

                            NULL,            // not applicable to free connections

                            ADS\_ADT,         // table type

                            ADS\_ANSI,        // character type (for non-unicode fields0

                            ADS\_PROPRIETARY\_LOCKING,

                            ADS\_IGNORERIGHTS,// This parameter is obsolete

                            32,              // memo block size (default is 8)

                            // field definitions.  General format is "name, type, size;"

                            "Empid, AutoInc; DeptNum, int;"

                            "LastName, char,20; FirstName, char,20;"

                            "HireDate, date;"

                            "Salary, Money;"

                            "Notes,memo;"    // general notes.  Memos are stored in separate .adm file

                            "Photo,Binary;", // binary (blob) field contents also stored in the .adm

                            ADS\_DEFAULT,     // no specific table options

                            NULL,            // additional collation possibilities

                            &hTable );

  if ( ulRet != AE\_SUCCESS )

     {

     DisplayLastError();

     goto CreateExit;

     }

  /\*

   \* Create some indexes on the table.  Indexes are stored in a separate file from

   \* the table.  The simplest is to use a "structural" (auto-open) index file,

   \* which is an index file that shares the same base name as the table.  It will

   \* be opened automatically when the table is opened.  Using multiple physically

   \* separate index files is rarely necessary.

   \*/

  // Create a unique index.  Unique is probably not really necessary in this case

  // since the autoincrement field is unique by definition.

  ulRet = AdsCreateIndex90( hTable, NULL, // specify NULL for file name to create auto-open index

                            "empid",      // index (tag) name

                            "empid",      // field name (indexes on simple fields are typically

                                          // the most useful)

                            NULL, NULL,   // no condition or while clause (rarely needed)

                            ADS\_UNIQUE,   // multiple options can be OR'd together

                            1024,         // page size.  Default is 512.  For larger tables

                                          // a larger page size may be good.

                            NULL,         // use default collation

                            &hIndex );

  if ( ulRet != AE\_SUCCESS )

     {

     DisplayLastError();

     goto CreateExit;

     }

  ulRet = AdsCreateIndex90( hTable, NULL,

                            "deptnum",  "deptnum",

                            NULL, NULL,  ADS\_DEFAULT,

                            ADS\_DEFAULT,  // page size can only be specified for first

                                          // tag created in an index file.  It applies

                                          // to the entire file.

                            NULL, &hIndex );

  if ( ulRet != AE\_SUCCESS )

     {

     DisplayLastError();

     goto CreateExit;

     }

  // Create a composite index on lastname and firstname.

  ulRet = AdsCreateIndex90( hTable, NULL,

                            "name",  "LastName;FirstName",

                            NULL, NULL,  ADS\_DEFAULT,

                            ADS\_DEFAULT,  NULL, &hIndex );

  if ( ulRet != AE\_SUCCESS )

     {

     DisplayLastError();

     goto CreateExit;

     }

  /\*

   \* Create a binary index that can help with optimization.  For small tables,

   \* this is not really useful.  For larger tables, this binary index is used by

   \* Advantage to quickly filter out deleted records.  With ADT tables, deleted

   \* records are put into a recycle list and reused when a new record is inserted.

   \* This binary index is a bitmap index (one bit per record) indicating if a

   \* record is deleted.  Some operations can benefit from this.  For example, if a

   \* table has a number deleted records at the top of the table, Advantage will

   \* use this binary index to locate the first non-deleted record when the table

   \* is opened (or when AdsGotoTop is used).  It also helps in AOF (Advantage

   \* Optimized Filter) processing.  Once an AOF bitmap filter is created, this

   \* binary index can be used to efficiently remove deleted records from the

   \* filter.

   \*/

  ulRet = AdsCreateIndex90( hTable, NULL,

                            "deleted", "deleted()",

                            NULL, NULL, ADS\_BINARY\_INDEX,

                            ADS\_DEFAULT, NULL, &hIndex );

  if ( ulRet != AE\_SUCCESS )

     {

     DisplayLastError();

     goto CreateExit;

     }

  // Close the table for completeness.  The AdsDisconnect call below would close it.

  ulRet = AdsCloseTable( hTable );

  // Create a second table using SQL.  It takes a little less typing.

  ulRet = AdsCreateSQLStatement( hConn, &hStmt );

  if ( ulRet != AE\_SUCCESS )

     {

     DisplayLastError();

     goto CreateExit;

     }

  ulRet = AdsExecuteSQLDirect( hStmt,

                               // make sure the table doesn't exist first

                               "try drop table departments; catch all end; "

                               // Create the table

                               "create table departments( DeptNum integer, DeptName char(25));"

                               // and a couple of indexes

                               "create unique index DeptNum on departments( DeptNum );"

                               "create index DeptName on departments( DeptName );",

                               NULL );

  if ( ulRet != AE\_SUCCESS )

     {

     DisplayLastError();

     goto CreateExit;

     }

  // close the SQL statement handle (disconnect would also do this)

  ulRet = AdsCloseSQLStatement( hStmt );

CreateExit:

  if ( hConn != 0 )

     // Disconnect will close any tables open on this connection

     AdsDisconnect( hConn );

  return ulRet;

} /\* CreateSampleTable \*/

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*  Module   : PopulateTable

\*  Return   : AE\_SUCCESS or ACE error code

\*  Desc     : Add some records to the sample tables

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 PopulateTable( void )

{

  UNSIGNED32 ulRet;

  ADSHANDLE  hConn = 0;

  ADSHANDLE  hTable;

  ADSHANDLE  hStmt;

  UNSIGNED8  aucBuf[100];

  ulRet = AdsConnect101( "Data source = " DB\_PATH "; ServerType=local;"

                         "DateFormat=mm/dd/yyyy;", NULL, &hConn );

  CHECK\_ERROR( ulRet );

  ulRet = AdsOpenTable101( hConn, "Employees", &hTable );

  CHECK\_ERROR( ulRet );

  // Add a record using the API calls directly

  ulRet = AdsAppendRecord( hTable );

  CHECK\_ERROR( ulRet );

  ulRet = AdsSetLong( hTable, "DeptNum", 1 );

  CHECK\_ERROR( ulRet );

  strcpy( aucBuf, "Smith" );

  ulRet = AdsSetString( hTable, "LastName", aucBuf, strlen( aucBuf ));

  CHECK\_ERROR( ulRet );

  strcpy( aucBuf, "John" );

  ulRet = AdsSetString( hTable, "FirstName", aucBuf, strlen( aucBuf ));

  CHECK\_ERROR( ulRet );

  // The date format was specified in the connection string above

  strcpy( aucBuf, "10/15/2003" );

  ulRet = AdsSetDate( hTable, "HireDate", aucBuf, strlen( aucBuf ));

  CHECK\_ERROR( ulRet );

  ulRet = AdsSetMoney( hTable, "Salary",

                       705000000 );  // money field has 4 implied decimal places

  CHECK\_ERROR( ulRet );

  strcpy( aucBuf, "Some notes about this employee." );

  ulRet = AdsSetString( hTable, "notes", aucBuf, strlen( aucBuf ));

  CHECK\_ERROR( ulRet );

  // If a photo is available on disk, an easy way to add it would be to use the

  // following API call to store it into the blob field.  If you have it in memory

  // the AdsSetBinary API can be used.

  // ulRet = AdsFileToBinary( hTable, "photo", ADS\_IMAGE, "c:\\photos\\JohnSmith.jpg" );

  /\*

   \* Explicitly write the record. The above calls store the information in buffers

   \* on the client.  This call will send it to the server (if using client/server)

   \* and write it to disk.  It also unlocks the record (the AdsAppendRecord call

   \* leaves the new record locked). If you don't call this function, any operation

   \* that causes record movement will write the record prior to the movement

   \* (closing the table also writes it out).

   \*/

  ulRet = AdsWriteRecord( hTable );

  CHECK\_ERROR( ulRet );

  /\*

   \* Now insert a few more records with SQL.  The table opened directly can be

   \* shared with SQL statements without any problem.  The SQL engine opens its own

   \* copy, so there is no conflict unless the AdsOpenTable call above opened the

   \* table exclusively.

   \*/

  ulRet = AdsCreateSQLStatement( hConn, &hStmt );

  CHECK\_ERROR( ulRet );

  /\*

   \* If you were reading the data from some other source and adding multiple

   \* records it would probably make sense to use AdsPrepareSQL and use a

   \* parameterized SQL statement and then set the parameter values for each record

   \* with calls to AdsSetString, AdsSetLong, etc. (just like above but use hStmt

   \* as the handle).

   \*/

  ulRet = AdsExecuteSQLDirect( hStmt,

        // The date format here could be the same as the one specified in the

        // connection string above, but it is probably better to use SQL standard

        "insert into employees (deptnum, lastname, firstname, hiredate, salary, notes) values "

                              "(1, 'Moore', 'Robert', '1999-05-01', 49600.00, 'Notes about Mr. Jones' );"

        "insert into employees (deptnum, lastname, firstname, hiredate, salary ) values "

                               "(5, 'Castleman', 'Ellen', '1995-07-21', 80000 );"

        "insert into employees (deptnum, lastname, firstname, hiredate, salary ) values "

                               "(3, 'Spear', 'Shelly', '2008-12-10', 45000 );"

        "insert into employees (deptnum, lastname, firstname, hiredate, salary ) values "

                               "(1, 'Granger', 'Timothy', '2002-02-01', 75000 );"

        "insert into departments values (1, 'Engineering' );"

        "insert into departments values (2, 'Marketing' );"

        "insert into departments values (3, 'Sales' );"

        "insert into departments values (4, 'Black Ops' );"

        "insert into departments values (5, 'Research' );"

                               , NULL );

  CHECK\_ERROR( ulRet );

FunctionExit:

  if ( hConn != 0 )

     AdsDisconnect( hConn );

  return ulRet;

} /\* CreateSampleTable \*/

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*  Module   : PrintRecord

\*  Return   : error code

\*  Desc     : Print out the current record in the given table.  This shows a

\*             couple ways to retrieve data.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 PrintRecord( ADSHANDLE hTable )

{

  UNSIGNED16 usField, usFields, usType;

  UNSIGNED32 ulRet;

  UNSIGNED8  aucBuf[500];

  UNSIGNED32 ulLen;

  UNSIGNED32 ulRec;

  SIGNED32   lValue;

  UNSIGNED8  \*pucSep = "";

  ulRet = AdsGetRecordNum( hTable, ADS\_IGNOREFILTERS, &ulRec );

  CHECK\_ERROR( ulRet );

  printf( "Record %4lu: ", ulRec );

  ulRet = AdsGetNumFields( hTable, &usFields );

  CHECK\_ERROR( ulRet );

  for ( usField = 1; usField <= usFields; usField++ )

     {

     // Most of the ACE APIs that refer to a specific field accept either a field

     // name or field number.  Use the ADSFIELD() macro when giving a field number.

     ulRet = AdsGetFieldType( hTable, ADSFIELD( usField ), &usType );

     switch ( usType )

        {

        case ADS\_BINARY:

        case ADS\_IMAGE:

           printf( " BLOB " );

           break;

        case ADS\_INTEGER:

           // It is possible to use type-specific AdsGet\* functions.

           ulRet = AdsGetLong( hTable, ADSFIELD( usField ), &lValue );

           CHECK\_ERROR( ulRet );

           printf( "%s%d", pucSep, lValue );

           break;

        default:

           // AdsGetField is a generic retrieval function that works well for many types

           ulLen = sizeof( aucBuf );

           ulRet = AdsGetField( hTable, ADSFIELD( usField ), aucBuf, &ulLen, ADS\_TRIM );

           CHECK\_ERROR( ulRet );

           printf( "%s%s", pucSep, aucBuf );

           break;

        }

     pucSep = ", ";

     }

  printf( "\n" );

FunctionExit:

  return ulRet;

}  /\* PrintRecord \*/

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*  Module   : PrintRecords

\*  Return   : error code

\*  Desc     : Print all records (respecting any filter that is set)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 PrintRecords

(

  ADSHANDLE hTable,    // table of interest

  ADSHANDLE hIndex     // optional index handle.  If given, traverse in this order

)

{

  UNSIGNED16 bEof;

  UNSIGNED32 ulRet;

  ADSHANDLE  hSkipOrder;

  if ( hIndex )

     // skip in index order

     hSkipOrder = hIndex;

  else

     // skip in natural record order

     hSkipOrder = hTable;

  // Go to the top of the table (respecting the filter).

  ulRet = AdsGotoTop( hSkipOrder );

  while ( 1 )

     {

     ulRet = AdsAtEOF( hTable, &bEof );

     CHECK\_ERROR( ulRet );

     if ( bEof )

        // done

        break;

     PrintRecord( hTable );

     // skip to next record

     ulRet = AdsSkip( hSkipOrder, 1 );

     CHECK\_ERROR( ulRet );

     }

FunctionExit:

  return ulRet;

}

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*  Module   : SearchForData

\*  Return   : AE\_SUCCESS or ACE error code

\*  Desc     : Show various ways to search for data and read it

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 SearchForData( void )

{

  UNSIGNED32 ulRet;

  ADSHANDLE  hConn = 0;

  ADSHANDLE  hTable;

  ADSHANDLE  hIndex;

  ADSHANDLE  hStmt;

  UNSIGNED16 bFound;

  double     dEmpid;

  UNSIGNED8  aucBuf[100];

  UNSIGNED16 usLen;

  ulRet = AdsConnect101( "Data source = " DB\_PATH "; ServerType=local;"

                         "DateFormat=mm/dd/yyyy;", NULL, &hConn );

  CHECK\_ERROR( ulRet );

  ulRet = AdsOpenTable101( hConn, "Employees", &hTable );

  CHECK\_ERROR( ulRet );

  // Use an index to seek for an employee ID

  ulRet = AdsGetIndexHandle( hTable, "empid", &hIndex );

  CHECK\_ERROR( ulRet );

  // You can use a double value to seek for numeric keys

  dEmpid = 3;

  ulRet = AdsSeek( hIndex, (UNSIGNED8\*)&dEmpid, sizeof( dEmpid ), ADS\_DOUBLEKEY,

                   ADS\_HARDSEEK, &bFound );

  CHECK\_ERROR( ulRet );

  if ( !bFound )

     printf( "Failed to find employee %d\n", (int)dEmpid );

  else

     // print info from this record

     PrintRecord( hTable );

  // A simple way to seek using character data is to just pass the text string

  // to seek, and it will convert it to the key type correctly.

  ulRet = AdsGetIndexHandle( hTable, "name", &hIndex );

  CHECK\_ERROR( ulRet );

  // Find "Jones" or next biggest key (soft seek).  This uses the composite

  // key but we can use it for searching for the lastname field.

  ulRet = AdsSeek( hIndex, "Jones", 5, ADS\_STRINGKEY, ADS\_SOFTSEEK, &bFound );

  CHECK\_ERROR( ulRet );

  printf( "Found Jones? %s\n", bFound ? "Yes" : "No" );

  PrintRecord( hTable );

  /\*

   \* To use a composite key with seeks, the seek key must match the actual key

   \* format (e.g., it would need the correct padding between values).  And if the

   \* key contained multiple data types, it would be difficult to construct such a

   \* key.  For these cases, you can use AdsBuildRawKey.  This call sequence shows

   \* one example using the composite name key.

   \*

   \* Note the use of hIndex (as opposed to hTable) in the AdsSet\* calls. Those

   \* calls result in setting the data in a logical record buffer that stores the

   \* data for the subsequent AdsBuildRawKey call.

   \*/

  ulRet = AdsInitRawKey( hIndex );

  ulRet = AdsSetString( hIndex, "Lastname", "Spear", 5 );

  ulRet = AdsSetString( hIndex, "Firstname", "Shelly", 6 );

  ulRet = AdsBuildRawKey( hIndex, aucBuf, &usLen );

  // We now have a raw key for a seek operation

  ulRet = AdsSeek( hIndex, aucBuf, usLen, ADS\_RAWKEY, ADS\_HARDSEEK, &bFound );

  printf( "Found Shelly? %s\n", bFound ? "Yes" : "No" );

  PrintRecord( hTable );

  /\*

   \* It may be simpler to use filters when searching for data.  Seek operations

   \* shown above may provide the best possible performance.  However, using

   \* Advantage Optimized Filters (AOFs) can provide nearly the same performance.

   \* The AOF engine uses indexes as appropriate to satisfy the conditions.  The

   \* following example will find the same entry as above using the same composite

   \* index to locate the matching record(s).

   \*/

  // Note: You can check to see if an AOF is optimized by calling AdsGetAOFOptLevel

  ulRet = AdsSetAOF( hTable, "lastname='Spear' and firstname = 'Shelly'",

                     ADS\_RESOLVE\_DYNAMIC );

  CHECK\_ERROR( ulRet );

  // After setting a filter, use AdsGotoTop and a skip operation to skip through

  // records that satisfy the filter.

  printf( "\nFilter results:\n" );

  PrintRecords( hTable, 0 );

  /\*

   \* Set a filter that uses two different indexes.  The AOF engine in this case

   \* will do two seek operations and use the intersection of the results.  It is

   \* extremely efficient and is nice because it does not require a composite index

   \* with the two fields.

   \*/

  ulRet = AdsSetAOF( hTable, "lastname > 'Granger' and deptnum = 1",

                     ADS\_RESOLVE\_DYNAMIC );

  CHECK\_ERROR( ulRet );

  /\*

   \* Print these results.  Pass in the name index handle so that it traverses the

   \* results in that index order.  Note that traversing a filtered result set in

   \* index order is more expensive than natural order because it must scan through

   \* the index.  For example, if the AOF selected one record out of a million,

   \* scanning the results in index order will cause Advantage to read through the

   \* entire index and read only the one record from disk.  It would be more

   \* efficient in that case to use natural order to read the results.

   \*/

  printf( "\nFilter results:\n" );

  PrintRecords( hTable, hIndex );

  ulRet = AdsCloseTable( hTable );

  CHECK\_ERROR( ulRet );

  // Show a couple SQL queries to retrieve data

  ulRet = AdsCreateSQLStatement( hConn, &hStmt );

  CHECK\_ERROR( ulRet );

  /\*

   \* This will use the AOF engine to optimize the result.  It is largely

   \* equivalent to opening the table and setting an AOF of the form "empid = 5"

   \* This results in a "Live" result set.  The result set handle is a table handle

   \* to the employees table in this case.  It would be possible to update records

   \* using this table handle by calling AdsSet\* functions.

   \*/

  ulRet = AdsExecuteSQLDirect( hStmt,

                               "select \* from employees where empid = 5", &hTable );

  CHECK\_ERROR( ulRet );

  printf( "\nSQL Result:\n" );

  PrintRecords( hTable, 0 );

  // Close the SQL result.

  ulRet = AdsCloseTable( hTable );

  CHECK\_ERROR( ulRet );

  /\*

   \* This query shows a simple join to get the department name with each employee

   \* this results in a static cursor.  It is essentially temporary table created

   \* by the sql engine (it may be contained entirely in memory).

   \*/

  ulRet = AdsExecuteSQLDirect( hStmt,

                 "select lastname, firstname, deptname from employees, departments "

                 "where employees.deptnum = departments.deptnum", &hTable );

  CHECK\_ERROR( ulRet );

  printf( "\nSQL Result:\n" );

  PrintRecords( hTable, 0 );

  // Close the SQL result.

  ulRet = AdsCloseTable( hTable );

  CHECK\_ERROR( ulRet );

FunctionExit:

  if ( hConn != 0 )

     AdsDisconnect( hConn );

  return ulRet;

}  /\* SearchForData \*/

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*  Module   : UpdateData

\*  Return   : AE\_SUCCESS or ACE error code

\*  Desc     : Show a couple of ways to make updates to data

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 UpdateData( void )

{

  UNSIGNED32 ulRet;

  ADSHANDLE  hConn = 0;

  ADSHANDLE  hTable;

  ADSHANDLE  hTable2;

  ADSHANDLE  hIndex;

  ADSHANDLE  hIndex2;

  ADSHANDLE  hStmt;

  UNSIGNED16 bFound;

  double     dEmpid;

  SIGNED64   qSalary;

  UNSIGNED8  aucBuf[100];

  ulRet = AdsConnect101( "Data source = " DB\_PATH "; ServerType=local;"

                         "DateFormat=mm/dd/yyyy;", NULL, &hConn );

  CHECK\_ERROR( ulRet );

  ulRet = AdsOpenTable101( hConn, "Employees", &hTable );

  CHECK\_ERROR( ulRet );

  ulRet = AdsGetIndexHandle( hTable, "empid", &hIndex );

  CHECK\_ERROR( ulRet );

  dEmpid = 4;

  ulRet = AdsSeek( hIndex, (UNSIGNED8\*)&dEmpid, sizeof( dEmpid ), ADS\_DOUBLEKEY,

                   ADS\_HARDSEEK, &bFound );

  CHECK\_ERROR( ulRet );

  if ( !bFound )

     printf( "Failed to find employee %d\n", (int)dEmpid );

  else

     {

     // This employee just married into money

     strcpy( aucBuf, "Mouton-Rothschild" );

     ulRet = AdsSetString( hTable, "Lastname", aucBuf, strlen( aucBuf ));

     CHECK\_ERROR( ulRet );

     // Update the salary in a hopeless effort to retain employee

     // Note that the AdsSetString call above resulted in locking the record.  This

     // guarantees that we get a consistent read and write.  If we had not set the

     // name field, we should lock the record explicitly first (see below).

     ulRet = AdsGetMoney( hTable, "Salary", &qSalary );

     CHECK\_ERROR( ulRet );

     // 7% raise

     qSalary += (UNSIGNED64)(qSalary \* .07);

     ulRet = AdsSetMoney( hTable, "Salary", qSalary );

     CHECK\_ERROR( ulRet );

     // save the results

     ulRet = AdsWriteRecord( hTable );

     CHECK\_ERROR( ulRet );

     }

  /\*

   \* The above example of updating a record uses implicit locking.  The first call

   \* to set a field (AdsSet\*) gets a lock on the record.  The call to AdsWriteRecord

   \* unlocks the record after it is successfully written.  You can use

   \* AdsLockRecord to explicitly lock a record.  The lock will be held until you

   \* call AdsUnlockRecord or close the table instance.

   \*/

  dEmpid = 1;

  ulRet = AdsSeek( hIndex, (UNSIGNED8\*)&dEmpid, sizeof( dEmpid ), ADS\_DOUBLEKEY,

                   ADS\_HARDSEEK, &bFound );

  CHECK\_ERROR( ulRet );

  ulRet = AdsLockRecord( hTable, 0 );  // 0 means lock current record

  CHECK\_ERROR( ulRet );

  /\*

   \* Open another instance of the table.  You can open multiple instances of the

   \* same table on a connection.  Or you could open it on a separate connection.

   \*/

  ulRet = AdsOpenTable101( hConn, "Employees", &hTable2 );

  CHECK\_ERROR( ulRet );

  ulRet = AdsGetIndexHandle( hTable, "empid", &hIndex2 );

  CHECK\_ERROR( ulRet );

  // Verify that this instance cannot update the locked record

  ulRet = AdsSeek( hIndex, (UNSIGNED8\*)&dEmpid, sizeof( dEmpid ), ADS\_DOUBLEKEY,

                   ADS\_HARDSEEK, &bFound );

  CHECK\_ERROR( ulRet );

  ulRet = AdsSetLong( hTable2, "DeptNum", 234 );

  assert( ulRet != AE\_SUCCESS );

  printf( "\nThis should display a 5035 error:\n" );

  DisplayLastError();

  // Unlock the record

  ulRet = AdsUnlockRecord( hTable,  0 );

  CHECK\_ERROR( ulRet );

  ulRet = AdsSetLong( hTable2, "DeptNum", 234 );

  CHECK\_ERROR( ulRet );

  // But don't write this update

  ulRet = AdsCancelUpdate( hTable2 );

  CHECK\_ERROR( ulRet );

  // Show how to use SQL to make a couple of updates

  ulRet = AdsCreateSQLStatement( hConn, &hStmt );

  CHECK\_ERROR( ulRet );

  // Rename a department

  ulRet = AdsExecuteSQLDirect( hStmt,

                               "update departments "

                               "   set DeptName = 'Plausible Deniability' "

                               "   where DeptNum = 4;", NULL );

  CHECK\_ERROR( ulRet );

  /\*

   \* And delete a record.  This is similar to seeking to the record and then

   \* calling AdsDeleteRecord followed by AdsWriteRecord. Our newly moneyed

   \* employee is leaving

   \*/

  ulRet = AdsExecuteSQLDirect( hStmt,

                               "delete from employees where empid = 4;", NULL );

  CHECK\_ERROR( ulRet );

FunctionExit:

  if ( hConn != 0 )

     AdsDisconnect( hConn );

  return ulRet;

}  /\* UpdateData \*/

int main(int argc, char\* argv[])

{

  UNSIGNED32 ulRet;

  ulRet = CreateSampleTable();

  if ( ulRet == AE\_SUCCESS )

     {

     ulRet = PopulateTable();

     ulRet = SearchForData();

     ulRet = UpdateData();

     }

 return 0;

}
