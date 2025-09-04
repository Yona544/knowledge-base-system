Examples




Advantage Database Server 12  

Examples

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Examples  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - Examples Advantage Client Engine ace\_Examples Advantage Client Engine > Example Code > Examples / Dear Support Staff, |  |
| Examples  Advantage Client Engine |  |  |  |  |

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoUpdates

\* API's Used : AdsOpenTable

\* AdsCloseTable

\* AdsGetLong

\* AdsSetLong

\* AdsLockTable

\* AdsUnlockTable

\* AdsIsTableLocked

\* AdsAtEOF

\* AdsIsRecordLocked

\* AdsShowError

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoUpdates( void )

{

UNSIGNED32 ulRetVal;

ADSHANDLE hTable;

UNSIGNED32 ulVal;

UNSIGNED16 bLocked;

UNSIGNED16 bEof;

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_NTX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_DEFAULT, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* Lock the file to make sure we can update it

\*/

while ( (ulRetVal = AdsLockTable( hTable )) == AE\_LOCK\_FAILED );

 

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "Table lock attempt failed" );

 

/\* Check if the table is really locked \*/

ulRetVal = AdsIsTableLocked( hTable, &bLocked );

if (ulRetVal)

AdsShowError( "Table Lock check failed" );

 

if ( bLocked != TRUE )

MessageBox( NULL, "Table not locked when it should have", "ACE Test", MB\_OK );

 

ulRetVal = AdsGotoTop( hTable );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "GotoTop failed" );

 

/\* Update all records \*/

do {

ulRetVal = AdsGetLong( hTable, "EMPID", &ulVal );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

ulRetVal = AdsSetLong( hTable, "EMPID", ulVal + 1 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

ulRetVal = AdsSkip ( hTable 1 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* Check if at EOF \*/

ulRetVal = AdsAtEOF( hTable, &bEof );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

} while ( !bEof );

 

/\* Unlock the table and check if it got unlocked \*/

ulRetVal = AdsUnlockTable( hTable );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "Table unlock" );

 

/\* Check if the table is unlocked \*/

ulRetVal = AdsIsTableLocked( hTable, &bLocked );

if (ulRetVal)

AdsShowError( "Table Lock check failed" );

 

if ( !bLocked )

MessageBox( NULL, "Table not unlocked when it should have", "ACE Test", MB\_OK );

 

/\* find out if the current record is locked \*/

AdsIsRecordLocked( hTable, 0, &bLocked );

if ( !bLocked )

MessageBox( NULL, "Record should not be locked", "ACE Test", MB\_OK );

 

ulRetVal = AdsCloseTable( hTable );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

return AE\_SUCCESS;

} /\* DoUpdates \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoZap

\* API's Used : AdsOpenTable

\* AdsCloseTable

\* AdsZapTable

\* AdsGetTableOpenOptions

\* AdsGetRecordCount

\* AdsAtEOF

\* AdsShowError

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoZap( void )

{

UNSIGNED32 ulRetVal;

ADSHANDLE hTable;

UNSIGNED32 ulNumRecs;

UNSIGNED32 ulOptions;

UNSIGNED16 bEof;

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_NTX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal != AE\_SUCCESS )

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

MessageBox( NULL, "Table not open exclusive when it should have", "ACE Test", MB\_OK );

 

/\* Remove all records \*/

ulRetVal = AdsZapTable( hTable );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

ulRetVal = AdsGetRecordCount( hTable, ADS\_IGNOREFILTERS, &ulNumRecs );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE GetNumRecords" );

 

/\* the table better be empty \*/

if ( ulNumRecs != 0 )

MessageBox( NULL, "Number of records wrong", "ACE Test", MB\_OK );

 

/\* We should be at EOF \*/

ulRetVal = AdsAtEOF( hTable, &bEof );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

if ( !bEof )

MessageBox( NULL, "Not at EOF on an empty table", "ACE Test", MB\_OK );

 

ulRetVal = AdsCloseTable( hTable );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

return AE\_SUCCESS;

} /\* DoZap \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoWrites

\* API's Used : AdsOpenTable

\* AdsCloseTable

\* AdsCloseAllTables

\* AdsCreateIndex

\* AdsCloseIndex

\* AdsLockRecord

\* AdsUnlockRecord

\* AdsGotoRecord

\* AdsGetNumFields

\* AdsGetFieldName

\* AdsGetField

\* AdsSetField

\* AdsGetRecordCount

\* AdsGetLong

\* AdsSetLong

\* AdsWriteRecord

\* AdsWriteAllRecords

\* AdsShowError

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

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

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TABLE1", ADS\_NTX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_DEFAULT, &hTable1 );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open first table" );

return ulRetVal;

}

 

/\* open the second table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO1000.DBF", "TABLE2", ADS\_CDX,

ADS\_ANSI, ADS\_PROPRIETARY\_LOCKING, ADS\_CHECKRIGHTS, ADS\_DEFAULT, &hTable2 );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open second table" );

return ulRetVal;

}

 

/\* Create an index on Table 1 \*/

ulRetVal = AdsCreateIndex( hTable1, NULL, NULL, "EMPID", NULL,

 NULL, ADS\_DEFAULT, &hIndex );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "Create Index failed on Table 1" );

return ulRetVal;

}

 

/\* Go to the 5th record of Table 1 and 15 record of Table 2 \*/

ulRetVal = AdsGotoRecord( hTable1, 5 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "Goto failed on Table 1" );

return ulRetVal;

}

 

ulRetVal = AdsGotoRecord( hTable2, 15 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "Goto failed on Table 2" );

return ulRetVal;

}

 

ulRetVal = AdsLockRecord( hTable2, 15 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* Copy table 1, record 5 to table 2, record 15 \*/

ulRetVal = AdsGetNumFields( hTable1, &usCount );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "GetNumFields failed on Table 1" );

return ulRetVal;

}

 

for ( i = 1; i <= usCount; i++ )

{

usLength = 20;

ulRetVal = AdsGetFieldName( hTable1, i, aucName, &usLength );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "GetFieldName failed on Table 1" );

return ulRetVal;

}

 

ulLength = 256;

ulRetVal = AdsGetField( hTable1, aucName, aucValue, &ulLength, ADS\_NONE );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "GetField failed on Table 1" );

return ulRetVal;

}

 

ulRetVal = AdsSetField( hTable2, aucName, aucValue, ulLength );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "SetField failed on Table 2" );

return ulRetVal;

}

}

 

/\* Now go through and increment the Employee ID

\* column by 10 for all records in Table 1

\*/

ulRetVal = AdsGetRecordCount( hTable1, ADS\_IGNOREFILTERS, &ulCount );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "GetRecordCount failed on Table 2" );

return ulRetVal;

}

 

for ( i = 1; i <= ulCount; i++ )

{

ulRetVal = AdsGotoRecord( hTable1, i );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* lock the current record \*/

while ( (ulRetVal = AdsLockRecord( hTable1, 0 )) == AE\_LOCK\_FAILED );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

ulRetVal = AdsGetLong( hTable1, "Empid", &ulValue );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

ulValue += 10;

 

ulRetVal = AdsSetLong( hTable1, "Empid", ulValue );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* This write will update the index, as well \*/

ulRetVal = AdsWriteRecord( hTable1 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

}

 

/\* Make sure all updated records are flushed for all tables \*/

ulRetVal = AdsWriteAllRecords();

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* unlock the record in Table 2 \*/

ulRetVal = AdsUnlockRecord( hTable2, 0 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

ulRetVal = AdsCloseIndex( hIndex );

 

ulRetVal = AdsCloseAllTables( );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

return AE\_SUCCESS;

} /\* DoWrites \*/

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

\* Function : DoSeeksAndSkips

\*

\* API's Used : AdsOpenTable

\* AdsCloseTable

\* AdsCreateIndex

\* AdsCloseAllIndexes

\* AdsSeek

\* AdsAtEOF

\* AdsGetString

\* AdsSkip

\* AdsSetScope

\* AdsGotoTop

\* AdsShowError

\* AdsInitRawKey

\* AdsBuildRawKey

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

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

UNSIGNED8 aucKey[ADS\_MAX\_KEY\_LENGTH];

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO1000.DBF", "TABLE1", ADS\_CDX,

ADS\_ANSI, ADS\_PROPRIETARY\_LOCKING, ADS\_CHECKRIGHTS,

ADS\_DEFAULT, &hTable1 );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* Create a numeric index \*/

ulRetVal = AdsCreateIndex( hTable1, "Index1", "EMPID", "EMPID",

NULL, NULL, ADS\_DEFAULT | ADS\_COMPOUND, &hIndex1 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "Create Index 1 failed on table" );

return ulRetVal;

 

}

 

/\* Create a complex expression character index \*/

ulRetVal = AdsCreateIndex( hTable1, "Index1", "TAG2",

"Lastname+firstname+if(married, 'T', 'F')",

"Branch = 'Chicago'", NULL,

ADS\_DESCENDING | ADS\_COMPOUND, &hIndex2 );

 

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "Create Index 2 failed on table" );

return ulRetVal;

}

 

/\* Create a simple index based on hire date \*/

ulRetVal = AdsCreateIndex( hTable1, "Index1", "Hire\_Date",

"DTOS(doh)", NULL, NULL,

ADS\_DEFAULT | ADS\_COMPOUND, &hIndex3 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "Create Index 3 failed on table" );

return ulRetVal;

 

}

 

/\*

\* Find everyone with the last name of Jefferson at the Chicago

\* branch.

\*/

usLength = strlen( "Jefferson" );

ulRetVal = AdsSeek( hIndex2, "Jefferson", usLength, ADS\_STRINGKEY,

ADS\_HARDSEEK, &bFound );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "Seek failed" );

return ulRetVal;

}

 

if ( !bFound )

MessageBox( NULL, "Did not find any Jeffersons", "ACE Test", MB\_OK );

 

usCount = 0;

AdsAtEOF( hTable1, &bEof );

while ( !bEof )

{

ulLength = 20;

ulRetVal = AdsGetString( hTable1, "Lastname", aucLName, &ulLength,

ADS\_RTRIM );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

if ( strcmp( "Jefferson", aucLName ) == 0 )

usCount++;

else

break;

 

ulRetVal = AdsSkip( hIndex2, 1 );

if ( ulRetVal != AE\_SUCCESS )

 

return ulRetVal;

 

AdsAtEOF( hTable1, &bEof );

}

 

 

printf( "There are %d Jeffersons at the Chicago Branch\n", usCount );

 

/\* Now do the same operation with a scope \*/

usLength = strlen( "Jefferson" );

ulRetVal = AdsSetScope( hIndex2, ADS\_TOP, "Jefferson", usLength,

ADS\_STRINGKEY );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

ulRetVal = AdsSetScope( hIndex2, ADS\_BOTTOM, "Jefferson", usLength,

 

ADS\_STRINGKEY );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

ulRetVal = AdsGotoTop( hIndex2 );

 

usCount2 = 0;

 

do

{

usCount2++;

 

ulRetVal = AdsSkip( hIndex2, 1 );

 

AdsAtEOF( hTable1, &bEof );

 

} while ( !bEof );

 

/\* The counts should be the same \*/

if ( usCount != usCount2 )

MessageBox( NULL, "Different answers with and without a scope",

"ACE Test", MB\_OK );

 

 

ulRetVal = AdsClearAllScopes( hTable1 );

 

 

/\*

\* Use AdsInitRawKey and AdsBuildRawKey to create seek keys

\*/

 

/\* Initialize creation of a key for this index \*/

ulRetVal = AdsInitRawKey( hIndex2 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* fill in the fields needed for the key \*/

ulRetVal = AdsSetString( hIndex2, "lastname", "Jefferson", 9 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

ulRetVal = AdsSetString( hIndex2, "firstname", "Ron", 3 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

ulRetVal = AdsSetLogical( hIndex2, "married", FALSE );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\*

\* build the key - it will use the fields set since the most recent call

\* to AdsInitRawKey for this index.

\*/

usLength = sizeof( aucKey );

ulRetVal = AdsBuildRawKey( hIndex2, aucKey, &usLength );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\*

\* Do the seek. Note that we use ADS\_RAWKEY because the result of

\* AdsBuildRawKey produces a key that needs no translation.

\*/

ulRetVal = AdsSeek( hIndex2, aucKey, usLength, ADS\_RAWKEY,

ADS\_HARDSEEK, &bFound );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

if ( bFound )

printf( "Found an unmarried Ron Jefferson at the Chicago Branch\n" );

else

printf( "Did not find an unmarried Ron Jefferson\n" );

 

/\*

\* Do the seek again but just change the married status for the seek.

\* This works fine if all the fields used in the original seek are still

\* desired. To start a new key, you can call AdsInitRawKey again to make

\* sure that only the new fields set are used.

\*/

ulRetVal = AdsSetLogical( hIndex2, "married", TRUE );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

usLength = sizeof( aucKey );

ulRetVal = AdsBuildRawKey( hIndex2, aucKey, &usLength );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

ulRetVal = AdsSeek( hIndex2, aucKey, usLength, ADS\_RAWKEY,

ADS\_HARDSEEK, &bFound );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

if ( bFound )

printf( "Found a married Ron Jefferson\n" );

else

printf( "Did not find a married Ron Jefferson\n" );

 

/\*

\* Create a partial seek key for the index. This example will create

\* a key using only the first and last names (and ignore the married field).

\*/

 

/\*

\* Initialize the logical record buffer for this index again. Note that

\* if we did not do this, the married field would still be set from the

\* above call, and the resulting key would be 'Coles Jeff T'.

\*/

ulRetVal = AdsInitRawKey( hIndex2 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* set first and last name \*/

ulRetVal = AdsSetString( hIndex2, "lastname", "Coles", 5 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

ulRetVal = AdsSetString( hIndex2, "firstname", "Jeff", 4 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\*

\* Now build the key. Since we did not set the married field for the

\* index, the resulting key will be 'Coles Jeff'. This means that

\* the seek will find the first record matching that key, which may

\* include a record like 'Coles Jeffrey'. If you want to excludes

\* records like that, then set the full field for the firstname value.

\* For example: AdsSetString( hIndex2, "firstname", "Jeff ", 12 );

\*/

usLength = sizeof( aucKey );

ulRetVal = AdsBuildRawKey( hIndex2, aucKey, &usLength );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

 

/\* do the seek \*/

ulRetVal = AdsSeek( hIndex2, aucKey, usLength, ADS\_RAWKEY,

ADS\_HARDSEEK, &bFound );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

if ( bFound )

printf( "Found a Jeff Coles\n" );

 

 

 

ulRetVal = AdsCloseAllIndexes( hTable1 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

ulRetVal = AdsCloseTable( hTable1 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

return AE\_SUCCESS;

} /\* DoSeeksAndSkips \*/

 

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoRelation

\* API's Used : AdsOpenTable

\* AdsCloseAllTables

\* AdsCreateIndex

\* AdsGetString

\* AdsGetRecordCount

\* AdsGotoRecord

\* AdsSetRelation

\* AdsSetScopedRelation

\* AdsShowError

\* AdsClearRelation

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoRelation( void )

{

ADSHANDLE hTable1;

ADSHANDLE hTable2;

ADSHANDLE hIndex2;

UNSIGNED32 ulCount;

UNSIGNED32 ulTotalCount;

UNSIGNED32 ulRetVal;

UNSIGNED32 ulBuf1;

UNSIGNED32 ulBuf2;

UNSIGNED8 aucRes1[50];

UNSIGNED8 aucRes2[50];

 

/\* open the first table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TABLE1", ADS\_CDX,

ADS\_ANSI, ADS\_PROPRIETARY\_LOCKING, ADS\_CHECKRIGHTS, ADS\_DEFAULT, &hTable1 );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open first table" );

return ulRetVal;

}

 

/\* open the second table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO1000.DBF", "TABLE2", ADS\_CDX,

ADS\_ANSI, ADS\_PROPRIETARY\_LOCKING, ADS\_CHECKRIGHTS, ADS\_DEFAULT, &hTable2 );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open second table" );

return ulRetVal;

}

 

/\* Create an index on the second table for the relation\*/

ulRetVal = AdsCreateIndex( hTable2, "Index1", "LAST",

 "Lastname", NULL, NULL,

ADS\_DESCENDING | ADS\_COMPOUND, &hIndex2 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "Create Index failed on table" );

return ulRetVal;

}

 

/\* Set a normal relation on the second table, based on the first table \*/

ulRetVal = AdsSetRelation( hTable1, hIndex2, "LASTNAME" );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "Error setting relation" );

return ulRetVal;

}

 

/\* Now, if the parent moves, the child should be positioned on the first

\* occurance of that key.

\*/

ulRetVal = AdsGotoRecord( hTable1, 5 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "Error going to record in parent" );

return ulRetVal;

}

 

/\* Get the relation value \*/

ulBuf1 = 50;

ulRetVal = AdsGetString( hTable1, "LastName", aucRes1, &ulBuf1, ADS\_TRIM );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "Error getting field value in parent" );

return ulRetVal;

}

 

/\* See if the child is on a record that matches \*/

ulBuf2 = 50;

ulRetVal = AdsGetString( hTable2, "LastName", aucRes2, &ulBuf2, ADS\_TRIM );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "Error getting field value in child" );

return ulRetVal;

}

 

if ( strcmp( aucRes1, aucRes2 ) != 0 && ulBuf1 != ulBuf2 )

{

MessageBox( 0, "Child field did not match parent field",

"ACE ERROR", MB\_OK | MB\_ICONWARNING );

return -1;

}

 

/\* clear the relation \*/

AdsClearRelation( hTable1 );

 

/\* now use a scoped relation to just look at the records that match \*/

ulRetVal = AdsSetScopedRelation( hTable1, hIndex2, "LASTNAME" );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "Error setting relation" );

return ulRetVal;

}

 

/\* The number of records visible on the child should be less than

\* the whole.

\*/

ulRetVal = AdsGotoRecord( hTable1, 7 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "Error going to record in parent" );

return ulRetVal;

}

 

ulRetVal = AdsGetRecordCount( hIndex2, ADS\_RESPECTFILTERS, &ulCount );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "Error getting record count in child" );

return ulRetVal;

}

 

/\* Now get the total record count \*/

ulRetVal = AdsGetRecordCount( hIndex2, ADS\_IGNOREFILTERS, &ulTotalCount );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "Error getting record count in child" );

return ulRetVal;

}

 

if ( ulCount >= ulTotalCount )

{

MessageBox( 0, "Scoped relation showed all records in the count",

"ACE ERROR", MB\_OK | MB\_ICONWARNING );

return -1;

}

 

 

/\* close all the tables \*/

AdsCloseAllTables();

 

 

return AE\_SUCCESS;

} /\* DoRelation \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoMoreSeeks

\* API's Used : AdsOpenTable

\* AdsCreateIndex

\* AdsSeek

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoMoreSeeks( void )

{

 

DOUBLE dVal;

ADSHANDLE hTable;

ADSHANDLE hIndex1;

ADSHANDLE hIndex2;

ADSHANDLE hIndex3;

ADSHANDLE hIndex4;

UNSIGNED32 ulRetVal;

UNSIGNED16 bFound;

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_CDX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* create some indexes \*/

ulRetVal = AdsCreateIndex( hTable, "X:\\DATA\\INDEX1", "INDEX1",

 "LASTNAME", NULL, NULL, ADS\_DEFAULT, &hIndex1 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

ulRetVal = AdsCreateIndex( hTable, "X:\\DATA\\INDEX2", "INDEX2",

 "DEPTNUM", NULL, NULL, ADS\_DEFAULT, &hIndex2 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

ulRetVal = AdsCreateIndex( hTable, "X:\\DATA\\INDEX3", "INDEX3",

 "DOB", NULL, NULL, ADS\_DEFAULT, &hIndex3 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

ulRetVal = AdsCreateIndex( hTable, "X:\\DATA\\INDEX4", "INDEX4",

 "SALARIED", NULL, NULL, ADS\_DEFAULT, &hIndex4 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

 

/\* seek on a char index using ADS\_STRINGKEY \*/

AdsSeek( hIndex1, "Coles", 5, ADS\_STRINGKEY, ADS\_HARDSEEK, &bFound );

 

/\* seek on a numeric, using ADS\_DOUBLEKEY \*/

dVal = 5;

AdsSeek( hIndex2, (UNSIGNED8\*)&dVal, 8, ADS\_DOUBLEKEY, ADS\_SOFTSEEK, &bFound );

 

/\* seek on a date, the date must be formatted according to the

\* current ACE date format \*/

AdsSeek( hIndex3, "08/24/76", 8, ADS\_STRINGKEY, ADS\_HARDSEEK, &bFound );

 

/\* seek on a logical \*/

AdsSeek( hIndex4, "F", 1, ADS\_STRINGKEY, ADS\_HARDSEEK, &bFound );

 

AdsCloseTable( hTable );

 

return AE\_SUCCESS;

 

} /\* DoMoreSeeks \*/

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoCancelRefresh

\* API's Used : AdsOpenTable

\* AdsSetField

\* AdsCancelUpdate

\* AdsRefreshRecord

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoCancelRefresh( void )

{

 

ADSHANDLE hTable;

UNSIGNED32 ulRetVal;

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_CDX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

AdsGotoTop( hTable );

 

/\* update the record \*/

AdsSetField( hTable, "EMPID", "5", 1 );

 

/\* cancel this pending update \*/

AdsCancelUpdate( hTable );

 

/\* force ACE to refresh it's record buffer, this would be helpful

\* if the app had been left for a while, when other users working concurrently

\* would have had the opportunity to make changes \*/

AdsRefreshRecord( hTable );

 

AdsCloseTable( hTable );

 

return AE\_SUCCESS;

 

} /\* DoCancelRefresh \*/

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoTrans

\* API's Used : AdsOpenTable

\* AdsBeginTransaction

\* AdsInTransaction

\* AdsRollbackTransaction

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoTrans( void )

{

 

ADSHANDLE hTable;

UNSIGNED32 ulRetVal;

UNSIGNED16 bInTrans;

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_CDX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* begin a transaction \*/

AdsBeginTransaction( 0 );

 

/\* make sure we're in an active transaction \*/

AdsInTransaction( 0, &bInTrans );

if ( !bInTrans )

MessageBox( 0, "Should be in transaction!", "ACE ERROR",

MB\_OK | MB\_ICONSTOP );

 

/\* we're just demonstrating AdsInTransaction, so we'll

\* roll back the transaction \*/

AdsRollbackTransaction( 0 );

 

AdsCloseTable( hTable );

 

return AE\_SUCCESS;

 

} /\* DoTrans \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoSeekLast

\* API's Used : AdsOpenTable

\* AdsSeekLast

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoSeekLast( void )

{

 

ADSHANDLE hTable;

ADSHANDLE hIndex;

UNSIGNED32 ulRetVal;

UNSIGNED16 bFound;

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_CDX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* create an index \*/

ulRetVal = AdsCreateIndex( hTable, "X:\\DATA\\INDEX1", "INDEX1",

 "LASTNAME", NULL, NULL, ADS\_DEFAULT, &hIndex );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* find the last 'Jones' in the index \*/

AdsSeekLast( hIndex, "Jones", 5, ADS\_STRINGKEY, &bFound );

 

AdsCloseTable( hTable );

 

return AE\_SUCCESS;

 

} /\* DoSeekLast \*/

 

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoHandles

\* API's Used : AdsOpenTable

\* AdsSetHandleLong

\* AdsGetHandleLong

\* AdsShowError

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoHandles( void )

{

 

ADSHANDLE hTable;

UNSIGNED32 ulRetVal;

UNSIGNED8 aucTableNotes[MAX\_STR\_LEN+1];

UNSIGNED8 \*pucDescription;

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_CDX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* attach a pointer to a string to this table handle \*/

strcpy( aucTableNotes, "This is table1, a test table" );

AdsSetHandleLong( hTable, (UNSIGNED32)aucTableNotes );

 

/\* now later we could get this pointer from ACE and retrieve

\* a description of the table \*/

AdsGetHandleLong( hTable, &(UNSIGNED32)pucDescription );

printf( "%s\n", pucDescription );

 

/\* NOTE: This long value associated with the handle could be any

\* long value or pointer. Another nice use might be to attach

\* a pointer to an array of indexes that go with this table \*/

 

AdsCloseTable( hTable );

 

return AE\_SUCCESS;

 

} /\* DoHandles \*/

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoConnect

\* API's Used : AdsOpenTable

\* AdsConnect

\* AdsDisconnect

\* AdsFindConnection

\* AdsGetServerName

\* AdsThreadExit

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoConnect( void )

{

 

ADSHANDLE hTable;

ADSHANDLE hConnection1;

ADSHANDLE hConnection2;

UNSIGNED32 ulRetVal;

UNSIGNED16 usLength;

UNSIGNED8 aucServerName[MAX\_STR\_LEN+1];

 

/\* get a connection to the server \*/

ulRetVal = AdsConnect( "x:", &hConnection1 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* open the table on this new connection \*/

ulRetVal = AdsOpenTable( hConnection1, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_CDX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* if we didn't store the connection handle, or didn't have access

\* to it in this module we could search for one. AdsFindConnection25

\* will return AE\_SUCCESS if it finds a connection to the exact path

\* given in the first parameter. \*/

 

if ( AE\_SUCCESS != AdsFindConnection25( "X:\\DATA\\SUBDIR", &hConnection2 ))

{

/\* a connection to the exact path failed, use any connection to the same

\* server

\*/

AdsFindConnection( "x:", &hConnection2 );

}

 

 

/\* get the server name from the connection handle \*/

usLength = MAX\_STR\_LEN+1;

AdsGetServerName( hConnection1, aucServerName, &usLength );

 

/\* close the table \*/

AdsCloseTable( hTable );

 

/\* disconnect hConnection1 from the server \*/

 

 

AdsDisconnect( hConnection1 );

 

/\* call AdsThreadExit to finish clean-up

\* NOTE: AdsThreadExit is for 32bit apps only, and does nothing

\* in 16bit apps \*/

AdsThreadExit();

 

return AE\_SUCCESS;

 

} /\* DoConnect \*/

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoKeyPos

\* API's Used : AdsOpenTable

\* AdsSetScope

\* AdsGetRelKeyPos

\* AdsSetRelKeyPos

\* AdsGetScope

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoKeyPos( void )

{

 

DOUBLE dKeyPos;

UNSIGNED32 ulRetVal;

ADSHANDLE hTable;

ADSHANDLE hIndex;

UNSIGNED16 usLength;

UNSIGNED8 aucScopeTop[MAX\_STR\_LEN+1];

 

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_CDX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* create an index \*/

ulRetVal = AdsCreateIndex( hTable, "X:\\DATA\\INDEX1", "INDEX1",

 "LASTNAME", NULL, NULL, ADS\_DEFAULT, &hIndex );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* set a scope \*/

AdsSetScope( hIndex, ADS\_TOP, "Daniels", 7, ADS\_STRINGKEY );

AdsSetScope( hIndex, ADS\_BOTTOM, "Mullin", 6, ADS\_STRINGKEY );

 

AdsGotoTop( hIndex );

 

/\* get the key position \*/

AdsGetRelKeyPos( hIndex, &dKeyPos );

 

/\* get the top scope value \*/

usLength = MAX\_STR\_LEN+1;

AdsGetScope( hIndex, ADS\_TOP, aucScopeTop, &usLength );

 

/\* set the key position \*/

AdsSetRelKeyPos( hIndex, .90 );

 

AdsCloseTable( hTable );

 

return AE\_SUCCESS;

 

} /\* DoKeyPos \*/

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoLogicalEmpty

\* API's Used : AdsOpenTable

\* AdsGetLocical

\* AdsGotoTop

\* AdsIsEmpty

\* AdsSetEmpty

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoLogicalEmpty( void )

{

 

UNSIGNED32 ulRetVal;

ADSHANDLE hTable;

UNSIGNED16 bSalaried;

UNSIGNED16 bEmpty;

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\EMP.DBF", "TEST", ADS\_CDX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

AdsGotoTop( hTable );

 

/\* find out if this employee is salaried \*/

AdsGetLogical( hTable, "SALARIED", &bSalaried );

 

/\* if so then clear the "perhour" field \*/

if ( bSalaried )

{

/\* see if the field is already empty \*/

AdsIsEmpty( hTable, "PERHOUR", &bEmpty );

if ( !bEmpty )

{

printf( "Salaried employee should not have hourly rate.\n" );

AdsSetEmpty( hTable, "PERHOUR" );

}

}

 

AdsCloseTable( hTable );

 

return AE\_SUCCESS;

 

} /\* DoLogicalEmpty \*/

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoRecno

\* API's Used : AdsOpenTable

\* AdsLocate

\* AdsContinue

\* AdsGetRecordNum

\* AdsGotoRecord

\* AdsGotoBottom

\* AdsIsFound

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoRecno( void )

{

 

UNSIGNED32 ulRetVal;

UNSIGNED32 ulMark1;

UNSIGNED32 ulMark2;

ADSHANDLE hTable;

UNSIGNED16 bFound;

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_CDX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

AdsGotoTop( hTable );

 

/\* find the first record with lastname = "Jones" \*/

AdsLocate( hTable, "LASTNAME='Jones'", TRUE /\* go forward \*/, &bFound );

 

/\* you can also check the found flag with an ACE call \*/

AdsIsFound( hTable, &bFound );

 

if ( bFound )

AdsGetRecordNum( hTable, ADS\_IGNOREFILTERS, &ulMark1 );

 

/\* find another record with the lastname "Jones" \*/

AdsContinue( hTable, &bFound );

 

if ( bFound )

AdsGetRecordNum( hTable, ADS\_IGNOREFILTERS, &ulMark2 );

 

/\* quickly get back to the first "Jones" \*/

AdsGotoRecord( hTable, ulMark1 );

 

/\* go to the last record \*/

AdsGotoBottom( hTable );

 

 

AdsCloseTable( hTable );

 

return AE\_SUCCESS;

 

} /\* DoRecno \*/

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoFieldNum

\* API's Used : AdsGetFieldNum

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoFieldNum( ADSHANDLE hTable, UNSIGNED8 \*pucFieldName )

{

 

UNSIGNED32 ulRetVal;

UNSIGNED16 usFieldNum;

UNSIGNED16 usNumFields;

 

/\* get the number of fields \*/

AdsGetNumFields( hTable, &usNumFields );

 

/\* get the field number from the name passed in \*/

ulRetVal = AdsGetFieldNum( hTable, pucFieldName, &usFieldNum );

if ( ulRetVal != AE\_SUCCESS )

return 0;

else

return usFieldNum;

 

} /\* DoFieldNum \*/

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoError

\* API's Used : AdsOpenTable

\* AdsGetErrorString

\* AdsGetLastError

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoError( void )

{

 

ADSHANDLE hTable;

UNSIGNED32 ulRetVal;

UNSIGNED32 ulLastErr;

UNSIGNED16 usLength;

UNSIGNED8 aucError[MAX\_STR\_LEN+1];

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO1.DBF", "TEST", ADS\_NTX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, print this to the console \*/

usLength = sizeof ( aucError) ;

AdsGetErrorString( ulRetVal, aucError, &usLength );

printf( "%s\n", aucError );

return ulRetVal;

}

 

usLength = sizeof ( aucError) ;

AdsGetLastError( &ulLastErr, aucError, &usLength );

 

return AE\_SUCCESS;

 

} /\* DoError \*/

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoDouble

\* API's Used : AdsOpenTable

\* AdsGotoTop

\* AdsGetDouble

\* AdsSetDouble

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoDouble( void )

{

 

DOUBLE dVal;

UNSIGNED32 ulRetVal;

ADSHANDLE hTable;

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\NUMBER.DBF", "TEST", ADS\_NTX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

AdsGotoTop( hTable );

 

/\* get a field with decimals \*/

AdsGetDouble( hTable, "C10\_3", &dVal );

 

/\* set this field to a new value \*/

AdsSetDouble( hTable, "C10\_3", 14.5521 );

 

AdsCloseTable( hTable );

 

return AE\_SUCCESS;

 

} /\* DoDouble \*/

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoBookmark

\* API's Used : AdsOpenTable

\* AdsLocate

\* AdsContinue

\* AdsGetBookmark

\* AdsGotoBookmark

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoBookmark( void )

{

 

UNSIGNED32 ulRetVal;

ADSHANDLE hTable;

ADSHANDLE hMark1;

ADSHANDLE hMark2;

UNSIGNED16 bFound;

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_CDX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

AdsGotoTop( hTable );

 

/\* find the first record with lastname = "Jones" \*/

AdsLocate( hTable, "LASTNAME='Jones'", TRUE, &bFound );

 

if ( bFound )

AdsGetBookmark( hTable, &hMark1 );

 

/\* find another record with the lastname "Jones" \*/

AdsContinue( hTable, &bFound );

 

if ( bFound )

AdsGetBookmark( hTable, &hMark2 );

 

/\* quickly get back to the first "Jones" \*/

AdsGotoBookmark( hTable, hMark1 );

 

 

AdsCloseTable( hTable );

 

return AE\_SUCCESS;

 

} /\* DoBookmark \*/

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoGetAllTables

\* API's Used : AdsGetAllTables

\* AdsGetNumOpenTables

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoGetAllTables( void )

{

 

UNSIGNED32 ulRetVal;

ADSHANDLE ahTables[50];

UNSIGNED16 usArrayLength;

UNSIGNED16 usNumTables;

 

usArrayLength = 50;

ulRetVal = AdsGetAllTables( ahTables, &usArrayLength );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* get the number of open tables \*/

AdsGetNumOpenTables( &usNumTables );

 

/\* the number of open tables returned should match the

\* array length returned in the AdsGetAllTables call \*/

if ( usArrayLength != usNumTables )

return -1;

 

return AE\_SUCCESS;

 

} /\* DoGetAllTables \*/

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoGetAllLocks

\* API's Used : AdsGetAllLocks

\* AdsGetNumLocks

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoGetAllLocks( ADSHANDLE hTable )

{

 

UNSIGNED32 ulRetVal;

UNSIGNED32 aulLocks[50];

UNSIGNED16 usArrayLength;

UNSIGNED16 usNumLocks;

 

usArrayLength = 50;

ulRetVal = AdsGetAllLocks( hTable, aulLocks, &usArrayLength );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* get the number of locks on this table \*/

AdsGetNumLocks( hTable, &usNumLocks );

 

/\* the number of locks should match the array length

\* returned from AdsGetAllLocks \*/

if ( usArrayLength != usNumLocks )

return -1;

 

 

return AE\_SUCCESS;

 

} /\* DoGetAllLocks \*/

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoRecover

\* API's Used : AdsFailedTransactionRecovery

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoRecover( void )

{

 

UNSIGNED32 ulRetVal;

 

/\* send the recover command to all connected servers \*/

ulRetVal = AdsFailedTransactionRecovery( NULL );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

return AE\_SUCCESS;

 

} /\* DoRecover \*/

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoDeleteRec

\* API's Used : AdsOpenTable

\* AdsGotoTop

\* AdsDeleteRecord

\* AdsSkip

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoDeleteRec( void )

{

 

UNSIGNED32 ulRetVal;

ADSHANDLE hTable;

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_CDX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

AdsGotoTop( hTable );

 

/\* delete every other record \*/

while ( !AxEOF( hTable ) )

{

AdsDeleteRecord( hTable );

 

ulRetVal = AdsSkip( hTable, 2 );

if ( ulRetVal != AE\_SUCCESS )

break;

}

 

 

AdsCloseTable( hTable );

 

return AE\_SUCCESS;

 

} /\* DoDeleteRec \*/

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoCreateTable

\* API's Used : AdsCreateTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoCreateTable( void )

{

 

UNSIGNED32 ulRetVal;

ADSHANDLE hTable;

UNSIGNED8 aucFieldDefs[256];

 

 

/\* build up a string with the field definitions we'll use in

\* the AdsCreateTable call \*/

strcpy( aucFieldDefs, "DEPTNUM,N,4,0;" );

strcat( aucFieldDefs, "LASTNAME,C,20;" );

strcat( aucFieldDefs, "FIRSTNAME,C,20;" );

strcat( aucFieldDefs, "SALARIED,L;" );

strcat( aucFieldDefs, "DOH,D;" );

 

 

ulRetVal = AdsCreateTable( 0, "X:\\DATA\\TEST1.DBF", "FIRSTTEST", ADS\_NTX,

ADS\_ANSI, ADS\_PROPRIETARY\_LOCKING, ADS\_CHECKRIGHTS,

512, aucFieldDefs, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

AdsCloseTable( hTable );

 

return AE\_SUCCESS;

 

} /\* DoCreateTables \*/

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : CreateFieldInfo

\* API's Used : AdsGetFieldName

\* AdsGetFieldDecimals

\* AdsGetFieldLength

\* AdsGetFieldOffset

\* AdsGetFieldType

\* Description : This function fills a struct with info about the field

\* in question and returns a pointer to this new struct

\* to the user.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 CreateFieldInfo( ADSHANDLE hTable,

UNSIGNED16 usFieldNum,

FIELDINFO \*\*pstFieldStruct )

{

 

UNSIGNED32 ulRetVal;

UNSIGNED16 usLength;

FIELDINFO \*pstNewStruct;

 

/\* check our parameters \*/

if ( usFieldNum < 1 )

return -1;

if ( !pstFieldStruct )

return -1;

 

/\* allocate memory for this new struct \*/

pstNewStruct = malloc( sizeof( FIELDINFO ) );

if ( !pstNewStruct )

return -1;

 

/\* place the field number we already have into the struct \*/

pstNewStruct->usNumber = usFieldNum;

 

/\* now use the ACE functions to fill this struct with field information \*/

usLength = MAX\_FIELDNAME\_LEN+1;

ulRetVal = AdsGetFieldName( hTable, usFieldNum, pstNewStruct->aucName, &usLength );

if ( ulRetVal != AE\_SUCCESS )

{

free( pstNewStruct );

/\* place a NULL in the return parameter \*/

pstFieldStruct = NULL;

return ulRetVal;

}

 

ulRetVal = AdsGetFieldType( hTable, pstNewStruct->aucName, &pstNewStruct->usType );

if ( ulRetVal != AE\_SUCCESS )

{

free( pstNewStruct );

/\* place a NULL in the return parameter \*/

pstFieldStruct = NULL;

return ulRetVal;

}

 

ulRetVal = AdsGetFieldOffset( hTable, pstNewStruct->aucName, &pstNewStruct->ulOffset );

if ( ulRetVal != AE\_SUCCESS )

{

free( pstNewStruct );

/\* place a NULL in the return parameter \*/

pstFieldStruct = NULL;

return ulRetVal;

}

 

ulRetVal = AdsGetFieldLength( hTable, pstNewStruct->aucName, &pstNewStruct->ulLength );

if ( ulRetVal != AE\_SUCCESS )

{

free( pstNewStruct );

/\* place a NULL in the return parameter \*/

pstFieldStruct = NULL;

return ulRetVal;

}

 

ulRetVal = AdsGetFieldDecimals( hTable, pstNewStruct->aucName, &pstNewStruct->usDecimals );

if ( ulRetVal != AE\_SUCCESS )

{

free( pstNewStruct );

/\* place a NULL in the return parameter \*/

pstFieldStruct = NULL;

return ulRetVal;

}

 

/\* if we got this far then everything went OK, so we'll place a copy

\* of the struct pointer in the return parameter \*/

\*pstFieldStruct = pstNewStruct;

/\* and return success \*/

return AE\_SUCCESS;

 

/\* NOTE: it would now be the calling modules responsibilty to free

\* the memory associated with pstNewStruct/pstFieldStruct \*/

 

 

} /\* CreateFieldInfo \*/

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : AxEvalExpression

\* API's Used : AdsEvalTestExpr

\* AdsEvalNumericExpr

\* AdsEvalStringExpr

\* AdsEvalLogicalExpr

\* Description : This function evaluates any expression type ( STRING, DATE,

\* LOGICAL, OR NUMERIC ) and returns the value as a string

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 AxEvalExpressionToString( ADSHANDLE hTable,

UNSIGNED8 \*pucExpression,

UNSIGNED8 \*pucBuffer,

UNSIGNED16 usLength )

{

 

UNSIGNED32 ulRetVal;

UNSIGNED16 usExprType;

UNSIGNED16 usDecimals = 2;

UNSIGNED16 bResult;

UNSIGNED16 bValidExpr;

DOUBLE dResult;

 

bResult = FALSE;

 

/\* make sure the parameters are valid \*/

if ( (!pucExpression) || (\*pucExpression == '\0') )

return -1;

 

if ( (!pucBuffer) || (\*pucBuffer == '\0') )

return -1;

 

/\* find out if this is a valid expression \*/

AdsIsExprValid( hTable, pucExpression, &bValidExpr );

 

if ( bValidExpr )

{

/\* now find out what type of expression this is \*/

ulRetVal = AdsEvalTestExpr( hTable, pucExpression, &usExprType );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

switch( usExprType )

{

case ADS\_LOGICAL:

ulRetVal = AdsEvalLogicalExpr( hTable, pucExpression, &bResult );

/\* not going to worry about the return code here, we'll handle

\* it below the switch block. If there was a problem the user

\* would recieve the letter 'F' in the buffer, because we

\* initialized bResult to FALSE. They would also recieve an

\* error code as the return value \*/

 

/\* make sure the output buffer is big enough \*/

if ( usLength < 2 )

return -1;

 

if ( bResult )

strcpy( pucBuffer, "T" );

else

strcpy( pucBuffer, "F" );

break;

 

case ADS\_STRING:

ulRetVal = AdsEvalStringExpr( hTable, pucExpression, pucBuffer, &usLength );

/\* we'll handle the return code below the switch block \*/

break;

 

case ADS\_NUMERIC:

ulRetVal = AdsEvalNumericExpr( hTable, pucExpression, &dResult );

/\* because we're calling another function we'll want to check

\* the return code from this API right away \*/

if ( ulRetVal != AE\_SUCCESS );

return ulRetVal;

/\* NOTE: ConvertDtoA is a user defined function \*/

ConvertDToA( dResult, pucBuffer, usLength, usDecimals );

break;

 

default:

/\* unknown type returned from AdsEvalTestExpr, return an error (-1) \*/

return -1;

 

} /\* end switch \*/

 

 

/\* handle any errors that may have occured \*/

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

else

return AE\_SUCCESS;

 

} /\* if valid expression \*/

 

else

return -1;

 

} /\* AxEvalExpression \*/

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoCollation

\* API's Used : AdsSetCollationLang

\* AdsGetCollationLang

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoCollation( void )

{

UNSIGNED16 usLength;

UNSIGNED8 aucLanguage[MAX\_BUFFER\_SIZE+1];

 

/\* set collation language to Spanish \*/

AdsSetCollationLang( ADS\_LANG\_SPANISH );

 

/\* get collation language \*/

usLength = MAX\_BUFFER\_SIZE+1;

AdsGetCollationLang( aucLanguage, &usLength );

 

return AE\_SUCCESS;

} /\* DoCollation \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoProgress

\* API's Used : AdsOpenTable

\* AdsCreateIndex

\* AdsRegisterProgressCallback

\* AdsClearProgressCallback

\* AdsReindex

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

 

/\* this is the function we will register with ACE

\* for progress information \*/

WINAPI ShowPercentage( UNSIGNED16 usPercentDone )

{

 

printf( "Percent Complete: %d\n", usPercentDone );

return 0;

 

} /\* ShowPercentage \*/

 

 

UNSIGNED32 DoProgress( void )

{

 

ADSHANDLE hTable;

ADSHANDLE hIndex;

UNSIGNED32 ulRetVal;

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO2M.DBF", "TEST", ADS\_CDX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* create an index \*/

 

ulRetVal = AdsCreateIndex( hTable, "X:\\DATA\\TEST", "TEST",

"FIRSTNAME", NULL, NULL, ADS\_DEFAULT, &hIndex );

if ( ulRetVal != AE\_SUCCESS )

{

AdsCloseTable( hTable );

return ulRetVal;

}

 

/\* register a callback function, this function will be called with progress

\* information during long indexing operations \*/

ulRetVal = AdsRegisterProgressCallback( ShowPercentage );

if ( ulRetVal != AE\_SUCCESS )

printf( "Error %d when attempting to register callback function.\n", ulRetVal );

 

/\* reindex all indexes associated with this table \*/

AdsReindex( hTable );

 

/\* clear the progress callback \*/

AdsClearProgressCallback();

 

AdsCloseTable( hTable );

 

 

} /\* DoProgress \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoCustom

\* API's Used : AdsOpenTable

\* AdsCreateIndex

\* AdsGotoTop

\* AdsGetLong

\* AdsSkip

\* AdsSeek

\* AdsAddCustomKey

\* AdsDeleteCustomKey

\* AdsGetKeyCount

\* AdsGetKeyNum

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoCustom( void )

{

 

ADSHANDLE hTable;

ADSHANDLE hIndex;

UNSIGNED32 ulRetVal; UNSIGNED32 ulKeyCount;

UNSIGNED32 ulKeyNum;

SIGNED32 lFieldVal;

UNSIGNED16 bFound;

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\NUMBER.DBF", "TEST", ADS\_CDX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_DEFAULT, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* create a custom index \*/

ulRetVal = AdsCreateIndex( hTable, "X:\\DATA\\PRIMES", NULL, "USRINPUT",

   NULL, NULL, ADS\_CUSTOM, &hIndex );

if ( ulRetVal != AE\_SUCCESS )

{

AdsCloseTable( hTable );

return ulRetVal;

}

 

/\* add all prime numbers in the USRINPUT field to a custom index using

\* our own UDF IsPrime() and the ACE function AdsAddCustomKey \*/

AdsGotoTop( hTable );

while( !AxEOF( hTable ) )

{

AdsGetLong( hTable, "USRINPUT", &lFieldVal );

if ( IsPrime( lFieldVal ) )

AdsAddCustomKey( hIndex );

AdsSkip( hTable, 1 );

}

 

/\* remove all 7's from the index with AdsDeleteCustomKey \*/

AdsGotoTop( hIndex );

AdsSeek( hIndex, "7", 1, ADS\_STRINGKEY, ADS\_HARDSEEK, &bFound );

if ( bFound )

{

AdsDeleteCustomKey( hIndex );

AdsSkip( hIndex, 1 );

AdsGetLong( hTable, "USRINPUT", &lFieldVal );

while( lFieldVal == 7 )

{

AdsDeleteCustomKey( hIndex );

AdsSkip( hIndex, 1 );

AdsGetLong( hTable, "USRINPUT", &lFieldVal );

}

}

 

 

/\* get the number of keys in this index \*/

AdsGetKeyCount( hIndex, ADS\_IGNOREFILTERS, &ulKeyCount );

 

/\* get the current key number \*/

AdsGetKeyNum( hIndex, ADS\_RESPECTFILTERS, &ulKeyNum );

 

AdsCloseTable( hTable );

 

 

} /\* DoCustom \*/

 

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoInitialize

\* API's Used : AdsCacheOpenTables

\* AdsSetSearchPath

\* AdsGetSearchPath

\* AdsSetDefault

\* AdsGetDefault

\* AdsSetDecimals

\* AdsGetDecimals

\* AdsNullTerminateStrings

\* AdsIsServerLoaded

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoInitialize( void )

{

UNSIGNED32 ulRetVal;

UNSIGNED16 usServerLoaded;

UNSIGNED16 usLength;

UNSIGNED16 usNumDecimals;

UNSIGNED8 aucSearchPath[MAX\_STR\_LEN+1];

UNSIGNED8 aucDefaultPath[MAX\_STR\_LEN+1];

 

 

/\* allow for 5 cached tables \*/

AdsCacheOpenTables( 5 );

 

/\* append to the search path for opening tables and indexes \*/

usLength = MAX\_STR\_LEN+1;

AdsGetSearchPath( aucSearchPath, &usLength );

strcat( aucSearchPath,

"X:\\MYDATA\\TESTS;\\\\MYSERVER\\MYVOLUME\\MYDATA\\TESTS;" );

AdsSetSearchPath( aucSearchPath );

 

/\* get the default path \*/

usLength = MAX\_STR\_LEN+1;

AdsGetDefault( aucDefaultPath, &usLength );

 

/\* set the default path to search for tables/indexes \*/

AdsSetDefault( "X:\\DATA" );

 

/\* get the current decimals setting \*/

AdsGetDecimals( &usNumDecimals );

 

/\* set the number of decimals we want to see from numeric functions

\* and calculations \*/

AdsSetDecimals( 2 );

 

/\* set NULL termination off \*/

AdsNullTerminateStrings( FALSE );

 

/\* make sure the server is loaded \*/

ulRetVal = AdsIsServerLoaded( "X:", &usServerLoaded );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

if ( usServerLoaded == ADS\_REMOTE\_SERVER )

return AE\_SUCCESS;

else

return -1;

 

} /\* DoInitialize \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoScopes

\* API's Tested : AdsOpenTable

\* AdsCreateIndex

\* AdsCloseTable

\* AdsGotoTop

\* AdsSetScope

\* AdsCreateIndex

\* AdsExtractKey

\* AdsSeek

\* AdsClearScope

\* AdsClearAllScopes

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoScopes( void )

{

ADSHANDLE hTable;

ADSHANDLE hIndex1;

ADSHANDLE hIndex2;

UNSIGNED32 ulRetVal;

UNSIGNED16 bFound;

UNSIGNED16 usLength;

UNSIGNED8 aucBuffer[MAX\_BUFFER\_SIZE+1];

 

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_CDX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_DEFAULT, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* create a couple of indexes \*/

ulRetVal = AdsCreateIndex( hTable , "X:\\DATA\\IDX1", NULL, "LASTNAME",

   NULL, NULL, ADS\_DEFAULT, &hIndex1 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsCloseTable( hTable );

return ulRetVal;

}

 

/\* NOTE: This index is descending, this we be important when setting

\* a scope later \*/

ulRetVal = AdsCreateIndex( hTable , "X:\\DATA\\IDX2", NULL, "DEPTNUM",

   NULL, NULL, ADS\_DESCENDING, &hIndex2 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsCloseTable( hTable );

return ulRetVal;

}

 

/\* save a value to seek on later \*/

AdsGotoTop( hIndex2 );

usLength = MAX\_BUFFER\_SIZE+1;

AdsExtractKey( hIndex2, aucBuffer, &usLength );

/\* we'll use the returned length in the seek later also \*/

 

/\* set a scope on the first index \*/

AdsSetScope( hIndex1, ADS\_TOP, "Daley", 5, ADS\_STRINGKEY );

AdsSetScope( hIndex1, ADS\_BOTTOM, "Peterson", 8, ADS\_STRINGKEY );

 

/\* set a scope on the second index, remember this is a descending index,

\* so the scope top and bottom must be adjusted accordingly \*/

AdsSetScope( hIndex2, ADS\_TOP, "12", 2, ADS\_STRINGKEY );

AdsSetScope( hIndex2, ADS\_BOTTOM, "5", 1, ADS\_STRINGKEY );

 

/\* seek using the second index, ADS\_RAWKEY, and the key we extracted earlier \*/

ulRetVal = AdsSeek( hIndex2, aucBuffer, usLength, ADS\_RAWKEY, ADS\_HARDSEEK, &bFound );

if ( !bFound )

{

/\* clear the scope and search again

\* NOTE: this only clears the scope on index #2 \*/

AdsClearScope( hIndex2, ADS\_TOP );

AdsClearScope( hIndex2, ADS\_BOTTOM );

AdsSeek( hIndex2, aucBuffer, usLength, ADS\_RAWKEY, ADS\_HARDSEEK, &bFound );

if ( !bFound )

{

MessageBox( 0, "Seek failed on a key extracted from the index!",

"ACE ERROR", MB\_OK | MB\_ICONERROR );

AdsCloseTable( hTable );

return -1;

}

}

 

/\* clear all scopes on all indexes \*/

AdsClearAllScopes( hTable );

 

AdsCloseTable( hTable );

return 0;

 

} /\* DoScopes \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : AxEOF

\* API's Used : AdsAtEOF

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

SIGNED16 AxEOF( ADSHANDLE hTable )

{

UNSIGNED32 ulRetVal;

SIGNED16 bEOF;

 

ulRetVal = AdsAtEOF( hTable, &bEOF );

if ( ulRetVal != AE\_SUCCESS )

{

MessageBox( NULL, "Call to AdsAtEOF failed!",

"Advantage Client Engine", MB\_OK | MB\_ICONSTOP );

// return true to avoid any loops an error like this might cause

return TRUE;

}

else

return bEOF;

} // AxEOF

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : AxBOF

\* API's Used : AdsAtBOF

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

SIGNED16 AxBOF( ADSHANDLE hTable )

{

UNSIGNED32 ulRetVal;

SIGNED16 bBOF;

 

ulRetVal = AdsAtBOF( hTable, &bBOF );

if ( ulRetVal != AE\_SUCCESS )

{

MessageBox( NULL, "Call to AdsAtBOF failed!",

"Advantage Client Engine", MB\_OK | MB\_ICONSTOP);

// return true to avoid any loops an error like this might cause

return TRUE;

}

else

return bBOF;

} // AxBOF

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoRemoveIndex

\* API's Used : AdsOpenTable

\* AdsOpenIndex

\* AdsShowError

\* AdsDeleteIndex

\* AdsGetAllIndexes

\* AdsGetIndexHandle

\* AdsApplicationExit

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoRemoveIndex( void )

{

ADSHANDLE hTable;

ADSHANDLE ahIndexes[50];

ADSHANDLE hIndex;

UNSIGNED32 ulRetVal;

UNSIGNED16 usLength;

UNSIGNED16 usNumIndexes;

 

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_CDX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* open a cdx index, the AdsOpenIndex call will return an array of

\* index handles, one for each tag in the cdx \*/

usLength = 50;

ulRetVal = AdsOpenIndex( hTable, "X:\\DATA\\TEST.CDX", ahIndexes, &usLength);

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE OpenIndex" );

return ulRetVal;

}

 

/\* open an idx index \*/

usLength = 50;

ulRetVal = AdsOpenIndex( hTable, "X:\\DATA\\TEST.IDX", ahIndexes, &usLength);

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE OpenIndex" );

return ulRetVal;

}

 

/\* NOTE: we just corrupted our array of indexes, but we can get an array

\* of all indexes associated with this table by calling AdsGetAllIndexes \*/

usLength = 50;

ulRetVal = AdsGetAllIndexes( hTable, ahIndexes, &usLength );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE GetAllIndexes" );

return ulRetVal;

}

 

/\* now the ahIndexes array contains the handles to each tag in the .cdx

\* and the .idx \*/

 

/\* remove the LASTNAME tag from the cdx \*/

AdsGetIndexHandle( hTable, "LAST", &hIndex );

ulRetVal = AdsDeleteIndex( hIndex );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE DeleteIndex" );

return ulRetVal;

}

 

/\* now the number of indexes should be one less than the

\* length returned from AdsGetAllIndexes \*/

AdsGetNumIndexes( hTable, &usNumIndexes );

 

if ( usNumIndexes != usLength )

return -1;

 

AdsCloseTable( hTable );

 

/\* let ACE know that this is the end of the application \*/

AdsApplicationExit();

 

return 0;

 

} /\* DoRemoveIndex \*/

 

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoTableStruct

\* API's Used : AdsOpenTable

\* AdsShowError

\* AdsCopyTable

\* AdsCopyTableContents

\* AdsCopyTableStructure

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoTableStruct( void )

{

ADSHANDLE hTable;

ADSHANDLE hTable2;

UNSIGNED32 ulRetVal;

 

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_NTX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_DEFAULT, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* make a copy of this table \*/

ulRetVal = AdsCopyTable( hTable, ADS\_IGNOREFILTERS, "X:\\COPY.DBF" );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE CopyTable" );

return ulRetVal;

}

 

/\* copy this table's struture to a new( empty ) file \*/

ulRetVal = AdsCopyTableStructure( hTable, "X:\\NEW.DBF" );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE CopyTableStructure" );

return ulRetVal;

}

 

/\* open the new structure and copy the contents of demo10.dbf into

\* this new table \*/

ulRetVal = AdsOpenTable( 0, "X:\\NEW.DBF", "NEW1", ADS\_NTX, ADS\_ANSI,

ADS\_PROPRIETARY\_LOCKING, ADS\_CHECKRIGHTS, ADS\_DEFAULT, &hTable2 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE OpenTable" );

return ulRetVal;

}

 

/\* Copy the contents of hTable to hTable2. After this call, new.dbf and

\* copy.dbf will have the same contents \*/

ulRetVal = AdsCopyTableContents( hTable, hTable2, ADS\_IGNOREFILTERS );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE CopyTableContents" );

return ulRetVal;

}

 

AdsCloseTable( hTable );

return 0;

 

} /\* DoTableStruct \*/

 

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoBinary

\* API's Used : AdsOpenTable

\* AdsGotoTop

\* AdsGetMemoLength

\* AdsBinaryToFile

\* AdsAppendRecord

\* AdsSetField

\* AdsFileToBinary

\* AdsGetBinaryLength

\* AdsGetBinary

\* AdsSetBinary

\* AdsWriteRecord

\* AdsSetString

\* AdsGetMemoDataType

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoBinary( void )

{

ADSHANDLE hTable;

UNSIGNED32 ulRetVal;

UNSIGNED32 ulLength;

UNSIGNED16 usMemoType;

UNSIGNED8 \*pucPhotoBuffer;

 

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\EXTENDED.DBF", "TEST", ADS\_NTX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_DEFAULT, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

AdsGotoTop( hTable );

 

/\* write the PHOTO field from this record to an image file on disk \*/

ulRetVal = AdsBinaryToFile( hTable, "PHOTO", "C:\\EMPLOYEES\\BILL.BMP" );

if ( ulRetVal != AE\_SUCCESS )

{

MessageBox( 0, "Error saving Bill's photo to disk!",

"ACE Error", MB\_OK | MB\_ICONWARNING );

return ulRetVal;

}

 

/\* append a new record \*/

ulRetVal = AdsAppendRecord( hTable );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

/\* fill some of the fields \*/

AdsSetField( hTable, "ID", "6", 1 );

AdsSetField( hTable, "AGE", "32", 2 );

AdsSetField( hTable, "SALARY", "42000.00", 8 );

/\* NOTE: this date must be formatted acording to the current ACE date format \*/

AdsSetField( hTable, "DOH", "01/16/97", 8 );

AdsSetString( hTable, "NOTES", "This is a new employee.", 23 );

 

/\* get the size of the memo \*/

AdsGetMemoLength( hTable, "NOTES", &ulLength );

 

/\* now copy a resume document to a binary field \*/

ulRetVal = AdsFileToBinary( hTable, "RESUME", ADS\_BINARY, "C:\\NEWEMPS\\SALLY.DOC" );

if ( ulRetVal != AE\_SUCCESS )

{

MessageBox( 0, "Error copying Sally's resume into the table!",

"ACE Error", MB\_OK | MB\_ICONWARNING );

return ulRetVal;

}

 

/\* when a binary field is empty it is still considered a memo field, you

\* can use AdsGetMemoDataType to determine what kind of data is in a

\* memo field. \*/

AdsGetMemoDataType( hTable, "RESUME", &usMemoType );

/\* since we put Sally's resume into this field it should now be considered

\* a binary field \*/

if ( usMemoType != ADS\_BINARY )

MessageBox( 0,

"AdsGetMemoDataType did not return ADS\_BINARY after writing data to it",

"ACE Error", MB\_OK | MB\_ICONWARNING );

 

/\* and copy Sally's photo into an image field \*/

ulRetVal = AdsFileToBinary( hTable, "PHOTO", ADS\_IMAGE, "C:\\NEWEMPS\\SALLY.BMP" );

if ( ulRetVal != AE\_SUCCESS )

{

MessageBox( 0, "Error copying Sally's photo into the table!",

"ACE Error", MB\_OK | MB\_ICONWARNING );

return ulRetVal;

}

 

/\* write this record to disk \*/

AdsWriteRecord( hTable );

 

/\* allocate memory for Sally's photo, retrieve the data, and write a

\* copy to the clipboard \*/

ulRetVal =AdsGetBinaryLength( hTable, "PHOTO", &ulLength );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

pucPhotoBuffer = malloc( ulLength );

if ( pucPhotoBuffer == NULL )

{

MessageBox( 0, "Error allocating memory.", "ERROR", MB\_OK | MB\_ICONWARNING );

return -1;

}

 

ulRetVal = AdsGetBinary( hTable, "PHOTO", 0, pucPhotoBuffer, &ulLength );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE GetBinary" );

return ulRetVal;

}

 

/\* call a User Defined Function to copy this data to a

\* DIB( Device Independent Bitmap) structure and place it

\* on the clipboard \*/

WriteToClipboard( pucPhotoBuffer, DIB, ulLength );

 

/\* to show the usage of AdsSetBinary we'll also write a copy of this

\* photo to a new record \*/

ulRetVal = AdsAppendRecord( hTable );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

ulRetVal = AdsSetBinary( hTable,

"PHOTO",

ADS\_IMAGE, // binary type

ulLength, // total length

0, // offset

pucPhotoBuffer, // the data

ulLength ); // length of this buffer

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE SetBinary" );

return ulRetVal;

}

AdsWriteRecord( hTable );

 

/\* free the memory \*/

free( pucPhotoBuffer );

 

AdsCloseTable( hTable );

return 0;

 

} /\* DoBinary \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoExact

\* API's Used : AdsOpenTable

\* AdsShowError

\* AdsGotoTop

\* AdsCloseTable

\* AdsGetExact

\* AdsSetExact

\* AdsEvalLogicalExpr

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoExact( void )

{

ADSHANDLE hTable;

UNSIGNED32 ulRetVal;

UNSIGNED16 bResult;

UNSIGNED16 bIgnoreSpaces;

 

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_NTX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING,

ADS\_CHECKRIGHTS, ADS\_DEFAULT, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* Some kind of error. Tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

AdsGetExact( &bIgnoreSpaces );

if ( !bIgnoreSpaces )

{

/\* In general, if the AdsSetExact setting is TRUE, trailing spaces

\* are ignored during the comparison. The AdsSetExact setting is

\* not that simple, however. It is somewhat complex and affects

\* the various relational operators differently. See the

\* Expression Engine Operators for detailed information on how

\* the AdsSetExact setting affects relational operators.

\*/

AdsSetExact( TRUE );

}

 

/\* The first record in this table has a lastname field of 'Coles ' \*/

AdsGotoTop( hTable );

 

/\*

\* After trailing spaces are truncated, this will do an exact

\* comparison, and will thus succeed.

\*/

AdsEvalLogicalExpr( hTable, "'Coles' = LASTNAME", &bResult ); // bResult: TRUE

 

/\*

\* After trailing spaces are truncated, this will do an exact

\* comparison, and will thus fail.

\*/

AdsEvalLogicalExpr( hTable, "LASTNAME = 'C'", &bResult ); // bResult: FALSE

 

AdsSetExact( FALSE );

 

/\* Trailing spaces are NOT truncated, so this will not succeed \*/

AdsEvalLogicalExpr( hTable, "'Coles' = LASTNAME", &bResult ); // bResult: FALSE

 

/\*

\* After trailing spaces are truncated, this will NOT do an exact

\* comparison, and will thus succeed.

\*/

AdsEvalLogicalExpr( hTable, "LASTNAME = 'C'", &bResult ); // bResult: TRUE

 

 

AdsCloseTable( hTable );

return 0;

 

} /\* DoExact \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoFilter

\* API's Used : AdsOpenTable

\* AdsGetFilter

\* AdsSetFilter

\* AdsShowError

\* AdsGotoTop

\* AdsAtEOF

\* AdsSkip

\* AdsClearFilter

\* AdsEvalStringExpr

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoFilter( void )

{

ADSHANDLE hTable;

UNSIGNED32 ulRetVal;

UNSIGNED16 bEOF;

UNSIGNED16 usLength;

UNSIGNED8 aucFilter[MAX\_STR\_LEN+1];

UNSIGNED8 aucBuffer[MAX\_STR\_LEN+1];

 

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_NTX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_DEFAULT, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* the filter expression should be empty \*/

usLength = MAX\_STR\_LEN+1;

ulRetVal = AdsGetFilter( hTable, aucFilter, &usLength );

if ( ulRetVal != AE\_NO\_FILTER )

{

MessageBox( 0, "Filter expression should have been empty!", "ACE Error", MB\_OK );

return -1;

}

 

ulRetVal = AdsSetFilter( hTable, "LASTNAME < 'Myers'" );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE SetFilter" );

return ulRetVal;

}

 

/\* skip through the table and print the names \*/

AdsGotoTop( hTable );

AdsAtEOF( hTable, &bEOF );

while ( !bEOF )

{

usLength = MAX\_STR\_LEN+1;

AdsEvalStringExpr( hTable, "LASTNAME+FIRSTNAME", aucBuffer, &usLength );

printf( "%s\n", aucBuffer );

 

ulRetVal = AdsSkip( hTable, 1 );

/\* checking the error code here will prevent an infinite loop \*/

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE Skip" );

return ulRetVal;

}

AdsAtEOF( hTable, &bEOF );

}

 

/\* clear the filter \*/

AdsClearFilter( hTable );

 

/\* print the names again, this time all 10 records will be visible \*/

AdsGotoTop( hTable );

AdsAtEOF( hTable, &bEOF );

while ( !bEOF )

{

usLength = MAX\_STR\_LEN+1;

AdsEvalStringExpr( hTable, "LASTNAME+FIRSTNAME", aucBuffer, &usLength );

printf( "%s\n", aucBuffer );

 

ulRetVal = AdsSkip( hTable, 1 );

/\* checking the error code here will prevent an infinite loop \*/

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE Skip" );

return ulRetVal;

}

AdsAtEOF( hTable, &bEOF );

}

 

AdsCloseTable( hTable );

return 0;

 

} /\* DoFilter \*/

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoDates

\* API's Used : AdsSetEpoch

\* AdsGetEpoch

\* AdsSetDateFormat

\* AdsGetDateFormat

\* AdsGetDate

\* AdsSetDate

\* AdsGetJulian

\* AdsSetJulian

\* AdsOpenTable

\* AdsCloseTable

\* AdsLockRecord

\* AdsUnlockRecord

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoDates( void )

{

ADSHANDLE hTable;

UNSIGNED32 ulRetVal;

SIGNED32 lJulianDate;

UNSIGNED16 usLength;

UNSIGNED16 usCurrentEpoch;

UNSIGNED8 aucOriginalFormat[MAX\_STR\_LEN+1];

UNSIGNED8 aucDOB[MAX\_STR\_LEN+1];

 

/\* save the current date format \*/

usLength = MAX\_STR\_LEN+1;

AdsGetDateFormat( aucOriginalFormat, &usLength );

 

/\* set the format we want to work with \*/

AdsSetDateFormat( "DD.MM.YY" );

AdsGetEpoch( &usCurrentEpoch );

if ( usCurrentEpoch != 2000 )

AdsSetEpoch( 2000 );

 

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO1000.DBF", "TEST", ADS\_NTX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_DEFAULT, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

AdsGotoTop( hTable );

 

/\* update the 'Date of Hire' and 'Date of Birth' fields \*/

ulRetVal = AdsLockRecord( hTable, 0 );

if ( ulRetVal != AE\_SUCCESS )

{

MessageBox( 0, "Unable to lock the current record.", "ACE Error", MB\_OK );

return ulRetVal;

}

AdsSetDate( hTable, "DOH", "30.06.02", 8 );

AdsSetJulian( hTable, "DOB", 2443015 );

/\* unlocking the record write this new data to disk \*/

AdsUnlockRecord( hTable, 0 );

 

/\* get these new values \*/

AdsGetJulian( hTable, "DOH", &lJulianDate );

if ( lJulianDate != 2452456 )

MessageBox( 0, "AdsGetJulian returned the incorrect date!", "ACE Error", MB\_OK );

usLength = MAX\_STR\_LEN+1;

AdsGetDate( hTable, "DOB", aucDOB, &usLength );

if ( strcmp( aucDOB, "24.08.76" ) != 0 )

MessageBox( 0, "AdsGetDate returned the incorrect date!", "ACE Error", MB\_OK );

 

AdsCloseTable( hTable );

return 0;

 

} /\* DoDates \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoVersionInfo

\* API's Used : AdsGetVersion

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoVersionInfo( void )

{

UNSIGNED32 ulMajor;

UNSIGNED32 ulMinor;

UNSIGNED16 usLength;

UNSIGNED8 ucLetter;

UNSIGNED8 aucDescription[MAX\_STR\_LEN+1];

 

usLength = MAX\_STR\_LEN+1;

AdsGetVersion( &ulMajor, &ulMinor, &ucLetter, aucDescription, &usLength );

 

printf( "%s version %lu.%lu%c\n", aucDescription, ulMajor, ulMinor, ucLetter );

return 0;

 

} /\* DoVersionInfo \*/

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoDelete

\* API's Used : AdsIsServerLoaded

\* AdsRecallRecord

\* AdsGotoTop

\* AdsAtEOF

\* AdsGetString

\* AdsSkip

\* AdsShowError

\* AdsOpenTable

\* AdsCloseTable

\* AdsPackTable

\* AdsShowDeleted

\* AdsGetDeleted

\* AdsIsRecordDeleted

\* AdsIsServerLoaded

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoDelete( void )

{

ADSHANDLE hTable;

UNSIGNED32 ulRetVal;

UNSIGNED32 ulLength;

UNSIGNED16 bEOF;

UNSIGNED16 usCount;

UNSIGNED16 bDeleted;

UNSIGNED16 bDeletedSetting;

UNSIGNED16 bServerLoaded;

UNSIGNED8 aucDivision[MAX\_STR\_LEN+1];

 

/\* see if the server is loaded \*/

AdsIsServerLoaded( "X:", &bServerLoaded );

if ( !bServerLoaded )

return -1;

 

/\* get the current AdsShowDeleted setting \*/

AdsGetDeleted( &bDeletedSetting );

 

if ( bDeletedSetting == FALSE )

/\* change this setting to including those records already

\* marked for deletion \*/

AdsShowDeleted( TRUE );

 

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO1000.DBF", "TEST", ADS\_NTX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

 

/\* skip through the table - count the number of records marked

\* for deletion and recall all records from the 'R and D' division \*/

usCount = 0;

AdsGotoTop( hTable );

AdsAtEOF( hTable, &bEOF );

while( !bEOF )

{

AdsIsRecordDeleted( hTable, &bDeleted );

if ( bDeleted )

{

ulLength = MAX\_STR\_LEN+1;

AdsGetString( hTable, "DIVISION", aucDivision, &ulLength, ADS\_RTRIM );

if ( strcmp( aucDivision, "R and D" ) == 0 )

AdsRecallRecord( hTable );

else

usCount++;

} /\* if bDeleted \*/

 

/\* check the return code on this skip to eliminate the chance of getting

\* stuck in this loop \*/

ulRetVal = AdsSkip( hTable, 1 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE Skip" );

return ulRetVal;

}

AdsAtEOF( hTable, &bEOF );

}

 

/\* now remove all deleted records by packing the table

\* note the table was opened exclusive \*/

ulRetVal = AdsPackTable( hTable );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

printf( "AdsPackTable: %d records were removed from the table\n", usCount );

 

AdsCloseTable( hTable );

return 0;

 

} // DoDelete

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoLocate

\* API's Used : AdsOpenTable

\* AdsLocate

\* AdsContinue

\* AdsGetString

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoLocate( void )

{

ADSHANDLE hTable;

UNSIGNED32 ulRetVal;

UNSIGNED32 ulLength;

UNSIGNED16 bFound;

UNSIGNED8 aucFirstname[MAX\_STR\_LEN+1];

UNSIGNED8 aucExtension[MAX\_STR\_LEN+1];

 

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO1000.DBF", "TEST", ADS\_NTX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_DEFAULT, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* Find the first record that matches the condition. \*/

ulRetVal = AdsLocate( hTable, "DEPTNUM = 11 AND LASTNAME = 'Young'", TRUE, &bFound );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

while ( bFound )

{

ulLength = MAX\_STR\_LEN+1;

AdsGetString( hTable, "FIRSTNAME", aucFirstname, &ulLength, ADS\_RTRIM );

ulLength = MAX\_STR\_LEN+1;

AdsGetString( hTable, "EXTENSION", aucExtension, &ulLength, ADS\_LTRIM );

printf( "%s %s\n", aucFirstname, aucExtension );

 

/\* Find the next record that matches the condition. \*/

AdsContinue( hTable, &bFound );

}

 

AdsCloseTable( hTable );

return 0;

 

} // DoLocate

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoAppend

\* API's Used : AdsOpenTable

\* AdsAppendRecord

\* AdsShowError

\* AdsSetLong

\* AdsSetLogical

\* AdsSetField

\* AdsWriteRecord

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoAppend( SIGNED32 lEmpID,

UNSIGNED8 \*pucLastname,

UNSIGNED8 \*pucFirstname,

UNSIGNED16 bSalaried,

UNSIGNED8 \*pucHireDate )

{

ADSHANDLE hTable;

UNSIGNED32 ulRetVal;

 

/\* NOTE: In most cases the table would already be open, and it would

\* be best to pass a function like this a table handle \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_NTX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_DEFAULT, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* append a new record \*/

ulRetVal = AdsAppendRecord( hTable );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE Append" );

AdsCloseTable( hTable );

return ulRetVal;

}

 

/\* update the fields \*/

ulRetVal = AdsSetLong( hTable, "EMPID", lEmpID );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE SetLong" );

 

ulRetVal = AdsSetField( hTable, "LASTNAME", pucLastname, strlen( pucLastname ) );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE SetField" );

 

ulRetVal = AdsSetField( hTable, "FIRSTNAME", pucFirstname, strlen( pucFirstname ) );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE SetField" );

 

ulRetVal = AdsSetLogical( hTable, "SALARIED", bSalaried );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE SetLogical" );

 

/\* NOTE: The date string passed to AdsSetDate must be formatted

\* according to the current ACE date format setting \*/

ulRetVal = AdsSetDate( hTable, "DOH", pucHireDate, (UNSIGNED16)strlen( pucHireDate ) );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE SetDate" );

 

/\* write the record and close the dbf \*/

ulRetVal = AdsWriteRecord( hTable );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE WriteRecord" );

 

ulRetVal = AdsCloseTable( hTable );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

return AE\_SUCCESS;

}

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoGetRecord

\* API's Used : AdsOpenTable

\* AdsShowError

\* AdsGetRecord

\* AdsGetRecordLength

\* AdsSetRecord

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoGetRecord( void )

{

ADSHANDLE hTable;

UNSIGNED32 ulRetVal;

UNSIGNED32 ulRecSize;

UNSIGNED8 \*pucTempRecord;

 

/\* open the table \*/

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_NTX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_DEFAULT, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* use AdsGetRecordLength to allocate a buffer \*/

ulRetVal = AdsGetRecordLength( hTable, &ulRecSize );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE GetRecordLength" );

AdsCloseTable( hTable );

return ulRetVal;

}

pucTempRecord = malloc( ulRecSize );

 

/\* now fill this buffer \*/

ulRetVal = AdsGetRecord( hTable, pucTempRecord, &ulRecSize );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE GetRecord" );

 

/\* because playing with the record buffer like this isn't a

\* smart thing to do, we'll just put the same buffer back

\* into this record \*/

AdsSetRecord( hTable, pucTempRecord, ulRecSize );

 

free( pucTempRecord );

ulRetVal = AdsCloseTable( hTable );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

return AE\_SUCCESS;

} /\* DoGetRecord \*/

 

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoTableInfo

\* API's Used : AdsOpenTable

\* AdsGetTableAlias

\* AdsGetTableCharType

\* AdsGetTableFilename

\* AdsGetTableHandle

\* AdsGetTableLockType

\* AdsGetTableOpenOptions

\* AdsGetTableRights

\* AdsGetTableType

\* AdsShowError

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

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

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_NTX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_DEFAULT, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* verify table alias

\*/

usBufferLen = MAX\_ALIAS\_LEN + 1;

ulRetVal = AdsGetTableAlias( hTable, aucAlias, &usBufferLen );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE GetTableAlias" );

else

/\* make sure this is the alias we assigned \*/

if ( strcmp( aucAlias, "TEST" ) != 0 )

MessageBox( NULL, "Alias wrong!", "ACE Test", MB\_OK );

 

 

/\* verify table chartype

\*/

ulRetVal = AdsGetTableCharType( hTable, &usCharType );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE GetTableCharType" );

else

/\* make sure this is the character type we assigned \*/

if ( usCharType != ADS\_ANSI )

MessageBox( NULL, "CharType wrong!", "ACE Test", MB\_OK );

 

 

/\* verify table filename

\*/

usBufferLen = ADS\_MAX\_TABLE\_NAME + 1;

ulRetVal = AdsGetTableFilename( hTable, ADS\_BASENAMEANDEXT, aucFilename, &usBufferLen );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE GetTableFilename" );

else

/\* make sure this is the file we opened \*/

if ( strcmp( aucFilename, "DEMO10.DBF" ) != 0 )

MessageBox( NULL, "Filename wrong!", "ACE Test", MB\_OK );

 

 

/\* verify table handle

\*/

ulRetVal = AdsGetTableHandle("DEMO10.DBF", &hTableCheck );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE GetTableHandle" );

else

/\* make sure this handle matches the handle returned from AdsOpenTable \*/

if ( hTable != hTableCheck )

MessageBox( NULL, "Table handle wrong!", "ACE Test", MB\_OK );

 

 

/\* verify table locktype

\*/

ulRetVal = AdsGetTableLockType( hTable, &usLockType );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE GetTableLockType " );

else

/\* make sure this is the locking type we assigned \*/

if ( usLockType != ADS\_COMPATIBLE\_LOCKING )

MessageBox( NULL, "LockType wrong!", "ACE Test", MB\_OK );

 

 

/\* verify table open options

\*/

ulRetVal = AdsGetTableOpenOptions( hTable, &ulOptions );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE GetTableOpenOptions" );

else

/\* make sure these are the options we assigned \*/

if ( ulOptions != ADS\_DEFAULT )

MessageBox( NULL, "OpenOptions wrong!", "ACE Test", MB\_OK );

 

 

/\* verify rightschecking

\*/

ulRetVal = AdsGetTableRights( hTable, &usRights );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE GetTableRights" );

else

/\* make sure this is the rights option we assigned \*/

if ( usRights != ADS\_CHECKRIGHTS )

MessageBox( NULL, "TableRights wrong!", "ACE Test", MB\_OK );

 

 

/\* verify table type

\*/

ulRetVal = AdsGetTableType( hTable, &usTableType );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE GetTableType" );

else

/\* make sure this is the table type we assigned \*/

if ( usTableType != ADS\_NTX )

MessageBox( NULL, "TableRights wrong!", "ACE Test", MB\_OK );

 

 

ulRetVal = AdsCloseTable( hTable );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

return AE\_SUCCESS;

} /\* DoTableInfo \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoIndexInfo

\* API's Used : AdsOpenTable

\* AdsCreateIndex

\* AdsIsIndexCompound

\* AdsIsIndexCustom

\* AdsIsIndexDescending

\* AdsIsIndexUnique

\* AdsGetIndexCondition

\* AdsGetIndexExpr

\* AdsGetIndexFilename

\* AdsGetIndexHandle

\* AdsGetIndexName

\* AdsShowError

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

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

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO10.DBF", "TEST", ADS\_CDX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS, ADS\_EXCLUSIVE, &hTable );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

ulRetVal = AdsCreateIndex( hTable, NULL, "LAST", "LASTNAME",

   "LASTNAME < 'JONES'", NULL,

ADS\_COMPOUND | ADS\_DESCENDING, &hIndex );

if ( ulRetVal != AE\_SUCCESS )

{

/\* tell the user about the error and close the table \*/

AdsShowError( "ACE Index creation failed" );

AdsCloseTable( hTable );

return ulRetVal;

}

 

/\* make sure the index is a compound(cdx) index \*/

ulRetVal = AdsIsIndexCompound( hIndex, &bBoolean );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE IsIndexCompound" );

else

if ( bBoolean == FALSE )

MessageBox( NULL, "AdsIsIndexCompound value is wrong!", "ACE Test", MB\_OK );

 

/\* make sure the index is not a custom index \*/

ulRetVal = AdsIsIndexCustom( hIndex, &bBoolean );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE IsIndexCustom" );

else

if ( bBoolean != FALSE )

MessageBox( NULL, "AdsIsIndexCustom value is wrong!", "ACE Test", MB\_OK );

 

/\* make sure the index is a descending index \*/

ulRetVal = AdsIsIndexDescending( hIndex, &bBoolean );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE IsIndexDescending" );

else

if ( bBoolean == FALSE )

MessageBox( NULL, "AdsIsIndexDescending value is wrong!", "ACE Test", MB\_OK );

 

/\* make sure the index is not a unique index \*/

ulRetVal = AdsIsIndexUnique( hIndex, &bBoolean );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE IsIndexUnique" );

else

if ( bBoolean != FALSE )

MessageBox( NULL, "AdsIsIndexUnique value is wrong!", "ACE Test", MB\_OK );

 

/\* check the index condition \*/

usBufferLen = MAX\_STR\_LEN + 1;

ulRetVal = AdsGetIndexCondition( hIndex, aucBuffer, &usBufferLen );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE GetIndexCondition" );

else

if ( strcmp( aucBuffer, "LASTNAME < 'JONES'" ) != 0 )

MessageBox( NULL, "Index condition string is wrong!", "ACE Test", MB\_OK );

 

/\* check the index expression \*/

usBufferLen = MAX\_STR\_LEN + 1;

ulRetVal = AdsGetIndexExpr( hIndex, aucBuffer, &usBufferLen );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE GetIndexExpr" );

else

if ( strcmp( aucBuffer, "LASTNAME" ) != 0 )

MessageBox( NULL, "Index expression string is wrong!", "ACE Test", MB\_OK );

 

/\* check the index filename \*/

usBufferLen = MAX\_STR\_LEN + 1;

ulRetVal = AdsGetIndexFilename( hIndex, ADS\_FULLPATHNAME, aucBuffer,

&usBufferLen );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE GetIndexFilename" );

else

if ( strcmp( aucBuffer, "\\\\WORF\\SYS\\DATA\\DEMO10.CDX" ) != 0 )

MessageBox( NULL, "Index name is wrong!", "ACE Test", MB\_OK );

 

/\* check the index name \*/

usBufferLen = MAX\_STR\_LEN + 1;

ulRetVal = AdsGetIndexName( hIndex, aucBuffer, &usBufferLen );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE GetIndexName" );

else

if ( strcmp( aucBuffer, "LAST" ) != 0 )

MessageBox( NULL, "Index condition string is wrong!", "ACE Test", MB\_OK );

 

/\* check the index handle \*/

ulRetVal = AdsGetIndexHandle( hTable, "LAST", &hIndexCheck );

if ( ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE GetIndexHandle" );

else

if ( hIndex != hIndexCheck )

MessageBox( NULL, "Index handle is wrong!", "ACE Test", MB\_OK );

 

ulRetVal = AdsGetIndexHandleByExpr( hTable, "LASTNAME < 'JONES'",

ADS\_DESCENDING, &hIndexCheck );

if (ulRetVal != AE\_SUCCESS )

AdsShowError( "ACE GetIndexHandlebyExpr" )

else

if ( hIndex != hIndexCheck )

MessageBox( NULL, "Index handle is wrong!", "ACE Test", MB\_OK );

 

 

/\* NOTE: This will close all indexes associated with the table also \*/

ulRetVal = AdsCloseTable( hTable );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

return AE\_SUCCESS;

} /\* DoIndexInfo \*/