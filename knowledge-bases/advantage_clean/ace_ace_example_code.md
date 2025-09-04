---
title: Ace Ace Example Code
slug: ace_ace_example_code
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_ace_example_code.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 9130d88479660e9b2e93a2bc64be1d17287b4c71
---

# Ace Ace Example Code

ACE Example Code

Advantage Client Engine Example Code

Advantage Client Engine

| Advantage Client Engine Example Code  Advantage Client Engine |  |  |  |  |

#include <windows.h>

#include "ace.h"

 

#define MAX\_ALIAS\_LEN 10

#define MAX\_STR\_LEN 255

 

 

/\* function prototypes \*/

 

/\* driver-oriented stuff \*/

UNSIGNED32 DoVersionLoaded( void );

UNSIGNED32 DoTransact( void );

 

/\* table-based stuff \*/

UNSIGNED32 DoTableInfo( void );

UNSIGNED32 DoGetRecord( void );

UNSIGNED32 DoZap( void );

UNSIGNED32 DoWrites( void );

UNSIGNED32 DoCreateTable( void );

UNSIGNED32 DoTable( void );

UNSIGNED32 DoDates( void );

UNSIGNED32 DoNumeric( void );

UNSIGNED32 DoMemos( void );

UNSIGNED32 DoLocking( void );

 

/\* index-geared stuff \*/

UNSIGNED32 DoSeeksAndSkips( void );

UNSIGNED32 DoIndexInfo( void );

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

 

 

UNSIGNED32 DoAppend( SIGNED32 lEmpID,

UNSIGNED8 \*pucLastname,

UNSIGNED8 \*pucFirstname,

UNSIGNED16 bSalaried,

UNSIGNED8 \*pucHireDate )

{

ADSHANDLE hTable;

UNSIGNED32 ulRetVal;

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST",

ADS\_NTX, ADS\_ANSI,

ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS,

ADS\_DEFAULT, &hTable );

if ( ulRetVal )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* append a new record \*/

ulRetVal = AdsAppendRecord( hTable );

if ( ulRetVal )

{

AdsShowError( "ACE Append" );

AdsCloseTable( hTable );

return ulRetVal;

}

 

/\* update the fields \*/

ulRetVal = AdsSetLong( hTable, "EMPID", lEmpID );

if ( ulRetVal )

AdsShowError( "ACE SetLong" );

 

ulRetVal = AdsSetField( hTable, "LASTNAME", pucLastname,

strlen( pucLastname ) );

if ( ulRetVal )

AdsShowError( "ACE SetField" );

 

ulRetVal = AdsSetField( hTable, "FIRSTNAME", pucFirstname,

strlen( pucFirstname ) );

if ( ulRetVal )

AdsShowError( "ACE SetField" );

 

ulRetVal = AdsSetLogical( hTable, "SALARIED", bSalaried );

if ( ulRetVal )

AdsShowError( "ACE SetLogical" );

 

/\* NOTE: The date string passed to AdsSetDate must be formatted

\* according to the current ACE date format setting \*/

ulRetVal = AdsSetDate( hTable, "DOH", pucHireDate,

(UNSIGNED16)strlen( pucHireDate ) );

if ( ulRetVal )

AdsShowError( "ACE SetDate" );

 

/\* write the record and close the dbf \*/

ulRetVal = AdsWriteRecord( hTable );

if ( ulRetVal )

AdsShowError( "ACE WriteRecord" );

 

ulRetVal = AdsCloseTable( hTable );

if ( ulRetVal )

return ulRetVal;

 

return AE\_SUCCESS;

}

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

 

 

UNSIGNED32 DoGetRecord( void )

{

ADSHANDLE hTable;

UNSIGNED32 ulRetVal;

UNSIGNED32 ulRecSize;

UNSIGNED8 \*pucTempRecord;

 

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST",

ADS\_NTX,ADS\_ANSI,

ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS,

ADS\_DEFAULT, &hTable );

if ( ulRetVal )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* use AdsGetRecordLength to allocate a buffer \*/

ulRetVal = AdsGetRecordLength( hTable, &ulRecSize );

if ( ulRetVal )

{

AdsShowError( "ACE GetRecordSize" );

AdsCloseTable( hTable );

return ulRetVal;

}

pucTempRecord = malloc( ulRecSize + 1 );

 

/\* now fill this buffer \*/

ulRetVal = AdsGetRecord( hTable, pucTempRecord, &ulRecSize );

if ( ulRetVal )

AdsShowError( "ACE GetRecord" );

 

free( pucTempRecord );

ulRetVal = AdsCloseTable( hTable );

if ( ulRetVal )

return ulRetVal;

 

return AE\_SUCCESS;

} /\* DoGetFields \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

 

 

UNSIGNED32 DoTableInfo( void )

{

ADSHANDLE hTable;

ADSHANDLE hTableCheck;

UNSIGNED32 ulRetVal;

UNSIGNED32 ulOptions;

UNSIGNED16 usBufferLen;

UNSIGNED16 usCharType;

UNSIGNED16 usLockType;

UNSIGNED16 usRights;

UNSIGNED16 usTableType;

UNSIGNED8 aucFilename[ADS\_MAX\_TABLE\_NAME + 1];

UNSIGNED8 aucAlias[MAX\_ALIAS\_LEN + 1];

 

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST",

ADS\_NTX, ADS\_ANSI,

ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS,

ADS\_DEFAULT, &hTable );

if ( ulRetVal )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

 

/\* verify table alias

\*/

usBufferLen = MAX\_ALIAS\_LEN + 1;

ulRetVal = AdsGetTableAlias( hTable, aucAlias, &usBufferLen );

if ( ulRetVal )

AdsShowError( "ACE GetTableAlias" );

else

/\* make sure this is the alias we assigned \*/

if ( strcmp( aucAlias, "TEST" ) != 0 )

MessageBox( NULL, "Alias wrong!", "ACE Test", MB\_OK );

 

 

/\* verify table chartype \*/

ulRetVal = AdsGetTableCharType( hTable, &usCharType );

if ( ulRetVal )

AdsShowError( "ACE GetTableCharType" );

else

/\* make sure this is the character type we assigned \*/

if ( usCharType != ADS\_ANSI )

MessageBox( NULL, "CharType wrong!", "ACE Test", MB\_OK );

 

 

/\* verify table filename

\*/

usBufferLen = ADS\_MAX\_TABLE\_NAME + 1;

ulRetVal = AdsGetTableFilename( hTable, ADS\_BASENAMEANDEXT,

aucFilename, &usBufferLen );

if ( ulRetVal )

AdsShowError( "ACE GetTableFilename" );

else

/\* make sure this is the file we opened \*/

if ( strcmp( aucFilename, "DEMO10.DBF" ) != 0 )

MessageBox( NULL, "Filename wrong!", "ACE Test", MB\_OK );

 

 

/\* verify table handle \*/

ulRetVal = AdsGetTableHandle( "TEST", &hTableCheck );

if ( ulRetVal )

AdsShowError( "ACE GetTableHandle" );

else

/\* make sure this handle matches the handle returned from

\* AdsOpenTable

\*/

if ( hTable != hTableCheck )

MessageBox( NULL, "Table handle wrong!", "ACE Test",

MB\_OK );

 

 

/\* verify table locktype \*/

ulRetVal = AdsGetTableLockType( hTable, &usLockType );

if ( ulRetVal )

AdsShowError( "ACE GetTableLockType " );

else

/\* make sure this is the locking type we assigned \*/

if ( usLockType != ADS\_COMPATIBLE\_LOCKING )

MessageBox( NULL, "LockType wrong!", "ACE Test", MB\_OK );

 

 

/\* verify table open options

\*/

ulRetVal = AdsGetTableOpenOptions( hTable, &ulOptions );

if ( ulRetVal )

AdsShowError( "ACE GetTableOpenOptions" );

else

/\* make sure these are the options we assigned \*/

if ( ulOptions != ADS\_DEFAULT )

MessageBox( NULL, "OpenOptions wrong!", "ACE Test",

MB\_OK );

 

 

/\* verify rights checking \*/

ulRetVal = AdsGetTableRights( hTable, &usRights );

if ( ulRetVal )

AdsShowError( "ACE GetTableRights" );

else

/\* make sure this is the rights option we assigned \*/

if ( usRights != ADS\_CHECKRIGHTS )

MessageBox( NULL, "TableRights wrong!", "ACE Test",

MB\_OK );

 

 

/\* verify table type \*/

ulRetVal = AdsGetTableType( hTable, &usTableType );

if ( ulRetVal )

AdsShowError( "ACE GetTableType" );

else

/\* make sure this is the table type we assigned \*/

if ( usTableType != ADS\_NTX )

MessageBox( NULL, "TableRights wrong!", "ACE Test",

MB\_OK );

 

 

ulRetVal = AdsCloseTable( hTable );

if ( ulRetVal )

return ulRetVal;

 

return AE\_SUCCESS;

} /\* DoTableInfo \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

 

 

UNSIGNED32 DoIndexInfo( void )

{

ADSHANDLE hTable;

ADSHANDLE hIndex;

ADSHANDLE hIndexCheck;

UNSIGNED32 ulRetVal;

UNSIGNED16 bBoolean;

UNSIGNED16 usBufferLen;

UNSIGNED8 aucBuffer[MAX\_STR\_LEN + 1];

 

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST",

ADS\_CDX, ADS\_ANSI,

ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS,

ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

ulRetVal = AdsCreateIndex( hTable, &hIndex, NULL, "LAST",

"LASTNAME", "LASTNAME < 'JONES'",

NULL, ADS\_COMPOUND|ADS\_DESCENDING );

if ( ulRetVal )

{

/\* tell the user about the error and close the table \*/

AdsShowError( "ACE Index creation failed" );

AdsCloseTable( hTable );

return ulRetVal;

}

 

/\* make sure the index is a compound(cdx) index \*/

ulRetVal = AdsIsIndexCompound( hIndex, &bBoolean );

if ( ulRetVal )

AdsShowError( "ACE IsIndexCompound" );

else

if ( bBoolean != TRUE )

MessageBox( NULL, "AdsIsIndexCompound value is wrong!",

"ACE Test", MB\_OK );

 

/\* make sure the index is not a custom index \*/

ulRetVal = AdsIsIndexCustom( hIndex, &bBoolean );

if ( ulRetVal )

AdsShowError( "ACE IsIndexCustom" );

else

if ( bBoolean != FALSE )

MessageBox( NULL, "AdsIsIndexCustom value is wrong!",

"ACE Test", MB\_OK );

 

/\* make sure the index is a descending index \*/

ulRetVal = AdsIsIndexDescending( hIndex, &bBoolean );

if ( ulRetVal )

AdsShowError( "ACE IsIndexDescending" );

else

if ( bBoolean != TRUE )

MessageBox( NULL, "AdsIsIndexDescending value is wrong!",

"ACE Test", MB\_OK );

 

/\* make sure the index is not a unique index \*/

ulRetVal = AdsIsIndexUnique( hIndex, &bBoolean );

if ( ulRetVal )

AdsShowError( "ACE IsIndexUnique" );

else

if ( bBoolean != FALSE )

MessageBox( NULL, "AdsIsIndexUnique value is wrong!",

"ACE Test", MB\_OK );

 

/\* check the index condition \*/

usBufferLen = MAX\_STR\_LEN + 1;

ulRetVal = AdsGetIndexCondition( hIndex, aucBuffer,

&usBufferLen );

if ( ulRetVal )

AdsShowError( "ACE GetIndexCondition" );

else

if ( strcmp( aucBuffer, "LASTNAME < 'JONES'" ) != 0 )

MessageBox( NULL, "Index condition string is wrong!",

"ACE Test", MB\_OK );

 

/\* check the index expression \*/

usBufferLen = MAX\_STR\_LEN + 1;

ulRetVal = AdsGetIndexExpr( hIndex, aucBuffer, &usBufferLen );

if ( ulRetVal )

AdsShowError( "ACE GetIndexExpr" );

else

if ( strcmp( aucBuffer, "LASTNAME" ) != 0 )

MessageBox( NULL, "Index expression string is wrong!",

"ACE Test", MB\_OK );

 

/\* check the index filename \*/

usBufferLen = MAX\_STR\_LEN + 1;

ulRetVal = AdsGetIndexFilename( hIndex, aucBuffer,

&usBufferLen );

if ( ulRetVal )

AdsShowError( "ACE GetIndexFilename" );

else

if ( strcmp( aucBuffer, "\\\\WORF\\SYS\\DATA\\DEMO10.CDX" )

!= 0 )

MessageBox( NULL, "Index condition string is wrong!",

"ACE Test", MB\_OK );

 

/\* check the index name \*/

usBufferLen = MAX\_STR\_LEN + 1;

ulRetVal = AdsGetIndexName( hIndex, aucBuffer, &usBufferLen );

if ( ulRetVal )

AdsShowError( "ACE GetIndexName" );

else

if ( strcmp( aucBuffer, "LAST" ) != 0 )

MessageBox( NULL, "Index condition string is wrong!",

"ACE Test", MB\_OK );

 

/\* check the index handle \*/

ulRetVal = AdsGetIndexHandle( hTable, "LAST", &hIndexCheck );

if ( ulRetVal )

AdsShowError( "ACE GetIndexHandle" );

else

if ( hIndex != hIndexCheck )

MessageBox( NULL, "Index handle is wrong!", "ACE Test",

MB\_OK );

 

 

/\* This will close all indexes associated with the table also \*/

ulRetVal = AdsCloseTable( hTable );

if ( ulRetVal )

return ulRetVal;

 

return AE\_SUCCESS;

} /\* DoIndexInfo \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

 

 

UNSIGNED32 DoUpdates( void )

{

UNSIGNED32 ulRetVal;

ADSHANDLE hTable;

UNSIGNED32 ulVal;

UNSIGNED16 bLocked;

UNSIGNED16 bEof;

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST",

ADS\_NTX, ADS\_ANSI,

ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS,

ADS\_DEFAULT, &hTable );

if ( ulRetVal )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* Lock the file to make sure we can update it \*/

while ( (ulRetVal = AdsLockTable( hTable )) == AE\_LOCK\_FAILED );

 

if ( ulRetVal )

AdsShowError( "Table lock attempt failed" );

 

/\* Check if the table is really locked \*/

ulRetVal = AdsIsTableLocked( hTable, &bLocked );

if (ulRetVal)

AdsShowError( "Table Lock check failed" );

 

if ( bLocked != TRUE )

MessageBox( NULL, "Table not locked when it should have",

"ACE Test", MB\_OK );

 

ulRetVal = AdsGotoTop( hTable );

if ( ulRetVal )

AdsShowError( "GotoTop failed" );

 

/\* Update all records \*/

do {

ulRetVal = AdsGetLong( hTable, "EMPID", &ulVal );

if ( ulRetVal )

return ulRetVal;

 

ulRetVal = AdsSetLong( hTable, "EMPID", ulVal + 1 );

if ( ulRetVal )

return ulRetVal;

 

/\* Check if at EOF \*/

ulRetVal = AdsAtEOF( hTable, &bEof );

if ( ulRetVal )

return ulRetVal;

 

} while ( bEof != TRUE );

 

/\* Unlock the table and check if it got unlocked \*/

ulRetVal = AdsUnlockTable( hTable );

if ( ulRetVal )

AdsShowError( "Table unlock" );

 

/\* Check if the table is unlocked \*/

ulRetVal = AdsIsTableLocked( hTable, &bLocked );

if (ulRetVal)

AdsShowError( "Table Lock check failed" );

 

if ( bLocked != FALSE )

MessageBox( NULL, "Table not unlocked when it should have",

"ACE Test", MB\_OK );

 

ulRetVal = AdsCloseTable( hTable );

if ( ulRetVal )

return ulRetVal;

 

return AE\_SUCCESS;

} /\* DoUpdates \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

 

 

UNSIGNED32 DoZap( void )

{

UNSIGNED32 ulRetVal;

ADSHANDLE hTable;

UNSIGNED32 ulNumRecs;

UNSIGNED32 ulOptions;

UNSIGNED16 bEof;

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST",

ADS\_NTX, ADS\_ANSI,

ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS,

ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* Check if the table is really opened exclusive \*/

ulRetVal = AdsGetTableOpenOptions( hTable, &ulOptions );

if (ulRetVal)

AdsShowError( "Table Lock check failed" );

 

if ( (ulOptions & ADS\_EXCLUSIVE) == 0 )

MessageBox( NULL,

"Table not open exclusive when it should have",

"ACE Test", MB\_OK );

 

/\* Remove all records \*/

ulRetVal = AdsZapTable( hTable );

if ( ulRetVal )

/\* this is not likely at all to fail \*/

return ulRetVal;

 

ulRetVal = AdsGetRecordCount( hTable, ADS\_IGNOREFILTERS,

&ulNumRecs );

if ( ulRetVal )

AdsShowError( "ACE GetNumRecords" );

 

/\* the table better be empty \*/

if ( ulNumRecs != 0 )

MessageBox( NULL, "Number of records wrong", "ACE Test",

MB\_OK );

 

/\* We should be at EOF \*/

ulRetVal = AdsAtEOF( hTable, &bEof );

if ( ulRetVal )

return ulRetVal;

 

if ( bEof != TRUE )

MessageBox( NULL, "Not at EOF on an empty table", "ACE Test",

MB\_OK );

 

ulRetVal = AdsCloseTable( hTable );

if ( ulRetVal )

return ulRetVal;

 

return AE\_SUCCESS;

} /\* DoZap \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

 

 

UNSIGNED32 DoWrites( void )

{

UNSIGNED32 ulRetVal;

UNSIGNED32 ulLength;

UNSIGNED32 ulValue;

ADSHANDLE hTable1;

ADSHANDLE hTable2;

ADSHANDLE hIndex;

UNSIGNED32 ulCount;

UNSIGNED16 usCount;

UNSIGNED16 i;

UNSIGNED16 usLength;

UNSIGNED8 aucName[20];

UNSIGNED8 aucValue[256];

 

/\* open the first table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TABLE1",

ADS\_NTX, ADS\_ANSI,

ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS,

ADS\_DEFAULT, &hTable1 );

if ( ulRetVal )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open first table" );

return ulRetVal;

}

 

/\* open the second table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO1000.DBF", "TABLE2",

ADS\_CDX, ADS\_ANSI,

ADS\_PROPRIETARY\_LOCKING, ADS\_CHECKRIGHTS,

ADS\_DEFAULT, &hTable2 );

if ( ulRetVal )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open second table" );

return ulRetVal;

}

 

/\* Create an index on Table 1 \*/

ulRetVal = AdsCreateIndex( hTable1, &hIndex, NULL, NULL, "EMPID",

NULL, NULL, ADS\_DEFAULT );

if ( ulRetVal )

{

AdsShowError( "Create Index failed on Table 1" );

return ulRetVal;

}

 

/\* Go to the 5th record of Table 1 and 15 record of Table 2 \*/

ulRetVal = AdsGotoRecord( hTable1, 5 );

if ( ulRetVal )

{

AdsShowError( "Goto failed on Table 1" );

return ulRetVal;

}

 

ulRetVal = AdsGotoRecord( hTable2, 15 );

if ( ulRetVal )

{

AdsShowError( "Goto failed on Table 2" );

return ulRetVal;

}

 

ulRetVal = AdsLockRecord( hTable2, 15 );

if ( ulRetVal )

return ulRetVal;

 

/\* Copy table 1, record 5 to table 2, record 15 \*/

ulRetVal = AdsGetNumFields( hTable1, &usCount );

if ( ulRetVal )

{

AdsShowError( "GetNumFields failed on Table 1" );

return ulRetVal;

}

 

for ( i = 1; i <= usCount; i++ )

{

usLength = 20;

ulRetVal = AdsGetFieldName( hTable1, i, aucName, &usLength );

if ( ulRetVal )

{

AdsShowError( "GetFieldName failed on Table 1" );

return ulRetVal;

}

 

ulLength = 256;

ulRetVal = AdsGetField( hTable1, aucName, aucValue, &ulLength,

ADS\_NONE );

if ( ulRetVal )

{

AdsShowError( "GetField failed on Table 1" );

return ulRetVal;

}

 

ulRetVal = AdsSetField( hTable2, aucName, aucValue,

ulLength );

if ( ulRetVal )

{

AdsShowError( "SetField failed on Table 2" );

return ulRetVal;

}

}

 

/\* Now go through and increment the Employee ID

\* column by 10 for all records in Table 1

\*/

ulRetVal = AdsGetRecordCount( hTable1, ADS\_IGNOREFILTERS,

&ulCount );

if ( ulRetVal )

{

AdsShowError( "GetRecordCount failed on Table 2" );

return ulRetVal;

}

 

for ( i = 1; i <= ulCount; i++ )

{

ulRetVal = AdsGotoRecord( hTable1, i );

if ( ulRetVal )

return ulRetVal;

 

/\* lock the current record \*/

while ( (ulRetVal = AdsLockRecord( hTable1, 0 )) ==

AE\_LOCK\_FAILED );

if ( ulRetVal )

return ulRetVal;

 

ulRetVal = AdsGetLong( hTable1, "Empid", &ulValue );

if ( ulRetVal )

return ulRetVal;

 

ulValue += 10;

 

ulRetVal = AdsSetLong( hTable1, "Empid", ulValue );

if ( ulRetVal )

return ulRetVal;

 

/\* This write will update the index, as well \*/

ulRetVal = AdsWriteRecord( hTable1 );

if ( ulRetVal )

return ulRetVal;

}

 

/\* Make sure all updated records are flushed for all tables \*/

ulRetVal = AdsWriteAllRecords();

if ( ulRetVal )

return ulRetVal;

 

/\* unlock the record in Table 2 \*/

ulRetVal = AdsUnlockRecord( hTable2, 0 );

if ( ulRetVal )

return ulRetVal;

 

ulRetVal = AdsCloseIndex( hIndex );

 

ulRetVal = AdsCloseAllTables( );

if ( ulRetVal )

return ulRetVal;

 

return AE\_SUCCESS;

} /\* DoWrites \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

 

 

UNSIGNED32 DoSeeksAndSkips( void )

{

UNSIGNED32 ulRetVal;

ADSHANDLE hTable1;

ADSHANDLE hIndex1;

ADSHANDLE hIndex2;

ADSHANDLE hIndex3;

UNSIGNED32 ulLength;

UNSIGNED16 usCount;

UNSIGNED16 usLength;

UNSIGNED16 bEof;

UNSIGNED16 bFound;

UNSIGNED16 usCount2;

UNSIGNED8 aucLName[20];

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO1000.DBF", "TABLE1",

ADS\_CDX, ADS\_ANSI,

ADS\_PROPRIETARY\_LOCKING, ADS\_CHECKRIGHTS,

ADS\_DEFAULT, &hTable1 );

if ( ulRetVal )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* Create a numeric index \*/

ulRetVal = AdsCreateIndex( hTable1, &hIndex1, "Index1", "EMPID",

"EMPID",NULL, NULL,

ADS\_DEFAULT | ADS\_COMPOUND );

if ( ulRetVal )

{

AdsShowError( "Create Index 1 failed on table" );

return ulRetVal;

}

 

/\* Create a complex expression character index \*/

ulRetVal = AdsCreateIndex( hTable1, &hIndex2, "Index1", "TAG2",

"Lastname+first+if(married,'T', 'F')",

"Branch = 'Chicago'", NULL, ADS\_DESCENDING |

ADS\_COMPOUND );

if ( ulRetVal )

{

AdsShowError( "Create Index 2 failed on table" );

return ulRetVal;

}

 

/\* Create a simple index based on hire date \*/

ulRetVal = AdsCreateIndex( hTable1, &hIndex3, "Index1",

"Hire\_Date", "DTOS(doh)", NULL, NULL,

ADS\_DEFAULT | ADS\_COMPOUND );

if ( ulRetVal )

{

AdsShowError( "Create Index 3 failed on table" );

return ulRetVal;

}

 

/\* Find everyone with the last name of Jefferson at the Chicago

\* branch.

\*/

usLength = strlen( "Jefferson" );

ulRetVal = AdsSeek( hIndex2, "Jefferson", usLength,

ADS\_STRINGKEY, ADS\_HARDSEEK, &bFound );

if ( ulRetVal )

{

AdsShowError( "Seek failed" );

return ulRetVal;

}

 

if ( bFound != TRUE )

MessageBox( NULL, "Did not find any Jeffersons", "ACE Test",

MB\_OK );

 

usCount = 0;

AdsAtEOF( hTable1, &bEof );

while ( !bEof )

{

ulLength = 20;

ulRetVal = AdsGetString( hTable1, "Lastname", aucLName,

&ulLength, ADS\_RTRIM );

if ( ulRetVal )

return ulRetVal;

 

if ( strcmp( "Jefferson", aucLName ) == 0 )

usCount++;

else

break;

 

ulRetVal = AdsSkip( hIndex2, 1 );

if ( ulRetVal )

return ulRetVal;

 

AdsAtEOF( hTable1, &bEof );

}

 

 

printf( "There are %d Jeffersons at the Chicago Branch",

usCount );

 

/\* Now do the same operation with a scope \*/

usLength = strlen( "Jefferson" );

ulRetVal = AdsSetScope( hIndex2, ADS\_TOP, "Jefferson", usLength,

ADS\_STRINGKEY );

if ( ulRetVal )

return ulRetVal;

 

ulRetVal = AdsSetScope( hIndex2, ADS\_BOTTOM, "Jefferson",

usLength, ADS\_STRINGKEY );

if ( ulRetVal )

return ulRetVal;

 

ulRetVal = AdsGotoTop( hIndex2 );

 

usCount2 = 0;

 

do {

usCount2++;

 

ulRetVal = AdsSkip( hIndex2, 1 );

 

AdsAtEOF( hTable1, &bEof );

 

} while ( !bEof );

 

/\* The counts should be the same \*/

if ( usCount != usCount2 )

MessageBox( NULL, "Different answers with & without a scope",

"ACE Test", MB\_OK );

 

ulRetVal = AdsCloseAllIndexes( hTable1 );

if ( ulRetVal )

return ulRetVal;

 

ulRetVal = AdsCloseTable( hTable1 );

if ( ulRetVal )

return ulRetVal;

 

return AE\_SUCCESS;

} /\* DoSeeksAndSkips \*/
