More Examples




Advantage Database Server 12  

More Examples

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| More Examples  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - More Examples Advantage Client Engine ace\_More\_examples Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| More Examples  Advantage Client Engine |  |  |  |  |

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoADTTypes

\* API's Used : AdsSetDateFormat

AdsCreateTable

AdsAppendRecord

AdsSetShort

AdsSetMilliseconds

AdsSetTime

AdsSetDate

AdsSetField

AdsGotoTop

AdsGetShort

AdsGetMilliseconds

AdsGetTime

AdsGetDate

AdsGetLong

AdsGetField

AdsCreateIndex

AdsLookupKey

AdsConvertTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoADTTypes( void )

{

UNSIGNED32 ulRetVal;

UNSIGNED32 ulLen;

UNSIGNED16 usLen;

UNSIGNED16 bFound;

UNSIGNED8 aucNewADTTable[260];

UNSIGNED8 aucNewDBFTable[260];

UNSIGNED8 aucFieldDesc[256];

UNSIGNED8 aucBuf[256];

ADSHANDLE hTable;

ADSHANDLE hIndex;

short sVal;

SIGNED32 lVal;

 

/\* Setup new ADT and DBF table paths \*/

strcpy( aucNewADTTable, "x:\\dbf\\demo.adt" );

strcpy( aucNewDBFTable, "x:\\dbf\\demo.dbf" );

 

/\* Field description for new ADT table \*/

strcpy( aucFieldDesc, "Short int field,shortint;" );

strcat( aucFieldDesc, "Time field,time;" );

strcat( aucFieldDesc, "Timestamp field,timestamp;" );

strcat( aucFieldDesc, "Autoinc field,autoinc;" );

strcat( aucFieldDesc, "Raw field,raw,100;" );

 

ulRetVal = AdsSetDateFormat( "MM/DD/YYYY" );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE could not set date format" );

return ulRetVal;

}

 

ulRetVal = AdsCreateTable( 0,

aucNewADTTable,

NULL,

ADS\_ADT,

ADS\_ANSI,

ADS\_PROPRIETARY\_LOCKING,

ADS\_CHECKRIGHTS,

0,

aucFieldDesc,

&hTable );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE could not create ADT table" );

return ulRetVal;

}

 

ulRetVal = AdsAppendRecord( hTable );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE could not append record" );

return ulRetVal;

}

 

/\* Set ADS\_SHORTINT field \*/

ulRetVal = AdsSetShort( hTable, "short int field", 37 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE could not set field" );

return ulRetVal;

}

 

/\* Set ADS\_TIME field \*/

ulRetVal = AdsSetMilliseconds( hTable, "time field", 340000 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE could not set field" );

return ulRetVal;

}

 

/\* Set ADS\_TIMESTAMP field \*/

ulRetVal = AdsSetTime( hTable, "timestamp field", "12:37:34 PM", 11 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE could not set field" );

return ulRetVal;

}

ulRetVal = AdsSetDate( hTable, "timestamp field", "10/31/1998", 10 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE could not set field" );

return ulRetVal;

}

 

/\* Cannot set ADS\_AUTOINC field \*/

 

/\* Set ADS\_RAW field \*/

ulRetVal = AdsSetField( hTable, "raw field", "This can be any raw data", 24 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE could not set field" );

return ulRetVal;

}

 

/\* Verify field data \*/

ulRetVal = AdsGotoTop( hTable );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE could not go top on ADT table" );

return ulRetVal;

}

 

ulRetVal = AdsGetShort( hTable, "short int field", &sVal );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE could not get field data" );

return ulRetVal;

}

if ( sVal != 37 )

{

AdsShowError( "Actual field value and returned field value"

"do not compare" );

return ulRetVal;

}

 

ulRetVal = AdsGetMilliseconds( hTable, "time field", &lVal );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE could not get field data" );

return ulRetVal;

}

if ( lVal != 340000 )

{

AdsShowError( "Actual field value and returned field value"

"do not compare" );

return ulRetVal;

}

 

usLen = sizeof( aucBuf );

ulRetVal = AdsGetTime( hTable, "timestamp field", aucBuf, &usLen );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE could not get field data" );

return ulRetVal;

}

if ( stricmp( aucBuf, "12:37:34 PM" ) != 0 )

{

AdsShowError( "Actual field value and returned field value"

"do not compare" );

return ulRetVal;

}

 

usLen = sizeof( aucBuf );

ulRetVal = AdsGetDate( hTable, "timestamp field", aucBuf, &usLen );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE could not get field data" );

return ulRetVal;

}

if ( stricmp( aucBuf, "10/31/1998" ) != 0 )

{

AdsShowError( "Actual field value and returned field value"

"do not compare" );

return ulRetVal;

}

 

ulRetVal = AdsGetLong( hTable, "autoinc field", &lVal );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE could not get field data" );

return ulRetVal;

}

if ( lVal != 1 )

{

AdsShowError( "Actual field value and returned field value"

"do not compare" );

return ulRetVal;

}

 

ulLen = sizeof( aucBuf );

ulRetVal = AdsGetField( hTable, "raw field", aucBuf, &ulLen, ADS\_TRIM );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE could not get field data" );

return ulRetVal;

}

if ( strcmp( aucBuf, "This can be any raw data" ) != 0 )

{

AdsShowError( "Actual field value and returned field value"

"do not compare" );

return ulRetVal;

}

 

/\* Create an unique index on \*/

ulRetVal = AdsCreateIndex( hTable,

NULL,

"autoinc",

"autoinc field",

NULL,

NULL,

ADS\_UNIQUE,

&hIndex );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE could not create unique index" );

return ulRetVal;

}

 

/\* Lookup an existing key \*/

ulRetVal = AdsLookupKey( hIndex, "1", 1, ADS\_STRINGKEY, &bFound );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE could not create ADT table" );

return ulRetVal;

}

if ( !bFound )

{

AdsShowError( "ACE could not find existing key value in index" );

return ulRetVal;

}

 

/\* Lookup a key that does not exist \*/

ulRetVal = AdsLookupKey( hIndex, "2", 1, ADS\_STRINGKEY, &bFound );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE could not create ADT table" );

return ulRetVal;

}

if ( bFound )

{

AdsShowError( "ACE returned FOUND for a key value that does"

"not exist in the table" );

return ulRetVal;

}

 

/\* Convert this ADT to DBF \*/

ulRetVal = AdsConvertTable( hTable,

ADS\_IGNOREFILTERS,

aucNewDBFTable,

ADS\_CDX );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "ACE could not convert ADT table" );

return ulRetVal;

}

 

}

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoSQL

\* API's Used : AdsCreateSQLStatement

\* AdsPrepareSQL

\* AdsExecuteSQL

\* AdsExecuteSQLDirect

\* AdsCloseSQLStatement

\* AdsStmtSetTableRights

\* AdsStmtSetTableLockType

\* AdsStmtSetTableCharType

\* AdsStmtSetTableType

\* AdsStmtConstrainUpdates

\* AdsClearSQLParams

\* AdsCacheOpenCursors

\* AdsSetTimeStamp

\* AdsCloseTable

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

 

UNSIGNED32 DoSQL( void )

{

ADSHANDLE hConnect;

ADSHANDLE hCursor;

ADSHANDLE hSQL;

UNSIGNED32 ulRetVal;

UNSIGNED32 ulLength;

UNSIGNED8 aucFieldVal;

 

/\* Allow 25 cursors to be cached\*/

ulRetVal = AdsCacheOpenCursors( 25 );

 

/\* Connect to the Server \*/

ulRetVal = AdsConnect( "X:\\DATA", &hConnect );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't connect to the Server" );

 

return ulRetVal;

}

 

/\* Create SQL Statement Handle to be used \*/

ulRetVal = AdsCreateSQLStatement( hConnect, &hSQL );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Create SQL Statement" );

 

return ulRetVal;

}

 

 

/\* Set the Statement Handle's Table Type to ADT \*/

ulRetVal = AdsStmtSetTableType( hSQL, ADS\_ADT );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Set The Table Type to ADT" );

 

return ulRetVal;

}

 

/\* Set the Statement Handle's Rights to Ignore rights \*/

ulRetVal = AdsStmtSetTableRights( hSQL, ADS\_IGNORERIGHTS );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Set The Table Rights to Ignore Rights" );

 

return ulRetVal;

}

 

 

/\* Set the Statement Handle's Lock Type to Properietary Locking \*/

ulRetVal = AdsStmtSetTableLockType( hSQL, ADS\_PROPRIETARY\_LOCKING );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Set The Lock Type to Properietary Locking" );

 

return ulRetVal;

}

 

 

/\* Set the Statement Handle's Character Type to use ANSI characters \*/

ulRetVal = AdsStmtSetTableCharType( hSQL, ADS\_ANSI );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Set The Charater Type to ANSI" );

 

return ulRetVal;

}

 

 

/\* Set the Statement Handle to Constrain Updates \*/

ulRetVal = AdsStmtConstrainUpdates( hSQL, ADS\_CONSTRAIN );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Set SQL Statement Handle to Constrain Updates" );

 

return ulRetVal;

}

 

 

/\* Set the Statement Handle to allow updates \*/

ulRetVal = AdsStmtSetTableReadOnly( hSQL, ADS\_CURSOR\_READWRITE );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Set SQL Statement Handle to ReadWrite" );

 

return ulRetVal;

}

 

/\* Prepare a statement handle to be executed with a named parameter \*/

ulRetVal = AdsPrepareSQL( hSQL, "SELECT \* FROM plane WHERE arrival = :ArrivalParam" );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Prepare Statement to be Executed" );

 

return ulRetVal;

}

 

 

/\* Set the value of the name parameter \*/

ulRetVal = AdsSetTimeStamp( hStatement, "ArrivalParam", "04/18/1999 7:00 AM",

strlen("04/18/1999 7:00 AM" ) );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Set the Parameter" );

 

return ulRetVal;

}

 

/\* Execute the SQL statment \*/

ulRetVal = AdsExecuteSQL( hSQL, &hCursor );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Execute the Statement" );

 

return ulRetVal;

}

 

 

/\* Close the Cursor Handle to free the SQL statement handle\*/

ulRetVal = AdsCloseTable( hCursor );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Close the Cursor Handle" );

 

return ulRetVal;

}

 

 

/\* Clear the parameter \*/

ulRetVal = AdsClearSQLParams( hSQL );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Clear the Parameter" );

 

return ulRetVal;

}

 

 

/\* Prepare a statement handle to be executed with an unnamed parameter\*/

ulRetVal = AdsPrepareSQL( hSQL, "SELECT \* FROM plane WHERE arrival = ?" );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Prepare Statement to be Executed" );

 

return ulRetVal;

}

 

 

/\* Set the value of the unnamed parameter \*/

ulRetVal = AdsSetTimeStamp( hStatement, ADSFIELD( 1 ), "04/18/1999 7:00 AM",

strlen("04/18/1999 7:00 AM" ) );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Set the Parameter" );

 

return ulRetVal;

}

 

/\* Execute the SQL statment \*/

ulRetVal = AdsExecuteSQL( hSQL, &hCursor );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Execute the Statement" );

 

return ulRetVal;

}

 

 

/\* Close the Cursor Handle to free the SQL statement handle\*/

ulRetVal = AdsCloseTable( hCursor );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Close the Cursor Handle" );

 

return ulRetVal;

}

 

 

/\* Clear the parameter \*/

ulRetVal = AdsClearSQLParams( hSQL );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Clear the Parameter" );

 

return ulRetVal;

}

 

/\* Direct execute an SQL statement with no parameters \*/

ulRetVal = AdsExecuteSQLDirect( hSQL, "Select lastname from Demo10", &hCursor );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Execute the Statement" );

 

return ulRetVal;

}

 

AdsGotoTop( hCursor );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Go to Top" );

 

return ulRetVal;

}

 

AdsSkip( hCursor, 1 );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Skip to Next Record" );

 

return ulRetVal;

}

 

ulLength = 257;

 

AdsGetString( hCursor, "Lastname", aucFieldVal, &ulLength, ADS\_NONE );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't get the value of Lastname" );

 

return ulRetVal;

}

 

 

AdsSetString( hCursor, "Lastname", "Johnson", strlen( "Johnson" ) );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't set the value of Lastname to Johnson" );

 

return ulRetVal;

}

 

 

/\* Close the Cursor Handle to free the SQL statement handle\*/

ulRetVal = AdsCloseTable( hCursor );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Close the Cursor Handle" );

 

return ulRetVal;

}

 

/\* Close the SQL statement handle \*/

ulRetVal = AdsCloseSQLStatement ( hSQL );

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Close the SQL Statement Handle" );

 

return ulRetVal;

}

 

 

AdsDisconnect( hConnect );

 

return 0;

 

} /\* DoSQL \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoExact22

\* API's Used : AdsConnect

\* AdsOpenTable

\* AdsShowError

\* AdsGotoTop

\* AdsCloseTable

\* AdsGetExact22

\* AdsSetExact22

\* AdsEvalLogicalExpr

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoExact22( void )

{

ADSHANDLE hConnection;

ADSHANDLE hTable1;

ADSHANDLE hTable2;

UNSIGNED32 ulRetVal;

UNSIGNED16 bResult;

UNSIGNED16 bIgnoreSpaces;

 

ulRetVal = AdsConnect( "X:\\DATA", &hConnection );

if ( ulRetVal != AE\_SUCCESS )

{

/\* Some kind of error. Tell the user what happened \*/

AdsShowError( "ACE Couldn't connect to server" );

return ulRetVal;

}

 

/\* Set default exactness for all tables opened on the connection \*/

ulRetVal = AdsSetExact22( hConnection, TRUE );

if ( ulRetVal != AE\_SUCCESS )

{

/\* Some kind of error. Tell the user what happened \*/

AdsShowError( "ACE Couldn't set the connection's exact setting" );

return ulRetVal;

}

 

/\* We will open the same table twice and then evaluate a expression with

\* different exact setting.

\*/

ulRetVal = AdsOpenTable( hConnection, "X:\\DATA\\DEMO10.DBF", NULL, ADS\_NTX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS,

ADS\_DEFAULT, &hTable1 );

if ( ulRetVal != AE\_SUCCESS )

{

/\* Some kind of error. Tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

ulRetVal = AdsOpenTable( hConnection, "X:\\DATA\\DEMO10.DBF", NULL, ADS\_NTX,

ADS\_ANSI, ADS\_COMPATIBLE\_LOCKING, ADS\_CHECKRIGHTS,

ADS\_DEFAULT, &hTable2 );

if ( ulRetVal != AE\_SUCCESS )

{

/\* Some kind of error. Tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* Get table's exact setting \*/

ulRetVal = AdsGetExact22( hTable1, &bIgnoreSpaces );

if ( ulRetVal != AE\_SUCCESS )

{

/\* Some kind of error. Tell the user what happened \*/

AdsShowError( "ACE Couldn't get the table's exact setting" );

return ulRetVal;

}

 

if ( !bIgnoreSpaces )

{

/\* This should not happend, the table should inherite the exact

\* setting from the connection.

\*/

return ulRetVal;

}

 

ulRetVal = AdsGetExact22( hTable2, &bIgnoreSpaces );

if ( ulRetVal != AE\_SUCCESS )

{

/\* Some kind of error. Tell the user what happened \*/

AdsShowError( "ACE Couldn't get the table's exact setting" );

return ulRetVal;

}

 

if ( !bIgnoreSpaces )

{

/\* This should not happend, the table should inherite the exact

\* setting from the connection.

\*/

return ulRetVal;

}

 

/\* Set the second table to not ignore space when comparing \*/

ulRetVal = AdsSetExact22( hTable2, FALSE );

if ( ulRetVal != AE\_SUCCESS )

{

/\* Some kind of error. Tell the user what happened \*/

AdsShowError( "ACE Couldn't set the table's exact setting" );

return ulRetVal;

}

 

/\* The first record in this table has a lastname field of 'Coles ' \*/

AdsGotoTop( hTable1 );

AdsGotoTop( hTable2 );

 

/\*

\* After trailing spaces are truncated, this will do an exact

\* comparison, and will thus succeed.

\*/

AdsEvalLogicalExpr( hTable1, "'Coles' = LASTNAME", &bResult ); // bResult: TRUE

 

/\*

\* After trailing spaces are truncated, this will do an exact

\* comparison, and will thus fail.

\*/

AdsEvalLogicalExpr( hTable1, "LASTNAME = 'C'", &bResult ); // bResult: FALSE

 

/\* Trailing spaces are NOT truncated, so this will not succeed \*/

 

AdsEvalLogicalExpr( hTable2, "'Coles' = LASTNAME", &bResult ); // bResult: FALSE

 

/\*

\* After trailing spaces are truncated, this will NOT do an exact

\* comparison, and will thus succeed.

\*/

AdsEvalLogicalExpr( hTable2, "LASTNAME = 'C'", &bResult ); // bResult: TRUE

 

/\* Disconnecting will close all tables for the connection \*/

AdsDisconnect( hConnection );

return 0;

 

} /\* DoExact22 \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoSQLEncryption

\* API's Used : AdsConnect

\* AdsStmtEnableEncryption

\* AdsStmtDisableEncryption

\* AdsStmtSetTablePassword

\* AdsStmtClearTablePasswords

\* AdsCreateSQLStatement

\* AdsExecuteSQLDirect

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoSQLEncryption( void )

{

ADSHANDLE hConnection;

ADSHANDLE hStmt;

ADSHANDLE hCursor;

UNSIGNED32 ulRetVal;

 

ulRetVal = AdsConnect( "X:\\DATA", &hConnection );

if ( ulRetVal != AE\_SUCCESS )

{

/\* Some kind of error. Tell the user what happened \*/

AdsShowError( "ACE Couldn't connect to server" );

return ulRetVal;

}

 

ulRetVal = AdsCreateSQLStatement( hConnection, &hStmt );

if ( ulRetVal != AE\_SUCCESS )

{

/\* Some kind of error. Tell the user what happened \*/

AdsShowError( "ACE Couldn't create statement handle" );

return ulRetVal;

}

 

/\*

\* Assuming:

\* Table1 has records encrypted with password "Hello"

\* Table2 has records encrypted with password "Howdy"

\*/

 

/\* 1) This query will get incorrect/scrambled result set \*/

AdsExecuteSQLDirect( hStmt, "Select \* from Table1 where id > 5", &hCursor );

 

/\* 2) This sequence fails because incorrect password is given. We have the clear

\* the password afterward.

\*/

AdsStmtSetTablePassword( hStmt, "Table1", "HELLO" ); // password is case sensitive

ulRetVal = AdsExecuteSQLDirect( hStmt, "Select \* from Table1 where id > 5", &hCursor );

// ulRetVal should be non-zero

 

AdsStmtClearTablePasswords( hStmt ); // This is not required because setting the table

// password the second time overwrites previous value.

 

/\* 3) This sequence returns a correct updatable cursor \*/

AdsStmtSetTablePassword( hStmt, "Table1", "Hello" );

AdsExecuteSQLDirect( hStmt, "Select \* from Table1 where id > 5", &hCursor );

 

/\* 4) This sequence continues to create a read-only cursor that is NOT encrypted \*/

AdsStmtSetTablePassword( hStmt, "Table2", "Howdy" );

AdsExecuteSQLDirect( hStmt, "Select \* from Table1, Table2 where Table1.id = Table2.id", &hCursor );

 

/\* 5) After enabling encryption on the statement handle, both of the following statement

\* will produce encrypted read only cursor

\*/

AdsStmtEnableEncryption( hStmt, "Hey" );

AdsExecuteSQLDirect( hStmt, "Select \* from Table1, Table2 where Table1.id = Table2.id", &hCursor );

AdsExecuteSQLDirect( hStmt, "Select \* from Table1 where id > 5", &hCursor );

 

/\* 6) After disabling encryption on the statement handle, cursor are create normally \*/

AdsStmtDisableEncryption( hStmt );

AdsExecuteSQLDirect( hStmt, "Select \* from Table2 where id > 5", &hCursor ); // updatable cursor

 

/\* Disconnecting will close all tables for the connection \*/

AdsDisconnect( hConnection );

return 0;

 

} /\* DoSQLEncryption \*/