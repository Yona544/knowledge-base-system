---
title: Ace Aof And Encryption Examples
slug: ace_aof_and_encryption_examples
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_aof_and_encryption_examples.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: b65c118dabc3af2d939ee73edc1f4809c0efd608
---

# Ace Aof And Encryption Examples

AOF and Encryption Examples

AOF and Encryption Examples

Advantage Client Engine

| AOF and Encryption Examples  Advantage Client Engine |  |  |  |  |

#include <windows.h>

#include "Ace.h"

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoAof

\* API's Used : AdsSetAOF

\* AdsClearAOF

\* AdsRefreshAOF

\* AdsGetAOF

\* AdsGetAOFOptLevel

\* AdsEvalAOF

\*

\* AdsOpenTable

\* AdsCloseTable

\* AdsCreateIndex

\* AdsCloseAllIndexes

\* AdsShowError

\* AdsGetRecordCount

\* AdsGotoTop

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoAof( void )

{

UNSIGNED32 ulRetVal;

 

ADSHANDLE hTable1;

ADSHANDLE hIndex1;

 

UNSIGNED8 aucNonOpt[64];

UNSIGNED8 aucAOF[64];

 

UNSIGNED16 usOptLevel;

UNSIGNED16 usLength;

 

UNSIGNED32 ulRecCount0;

UNSIGNED32 ulRecCount1;

UNSIGNED32 ulRecCount2;

 

UNSIGNED32 ulRecCount3;

UNSIGNED32 ulRecCount4;

UNSIGNED32 ulRecCount5;

 

UNSIGNED32 aulRecords[10];

UNSIGNED16 bIsInAOF;

 

 

 

/\* open the table \*/

 

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO1000.DBF", "TABLE1",

ADS\_CDX, ADS\_ANSI, ADS\_PROPRIETARY\_LOCKING,

ADS\_CHECKRIGHTS,

ADS\_DEFAULT, &hTable1 );

 

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

/\* Create a simple character index \*/

ulRetVal = AdsCreateIndex( hTable1, "Index1", "TAG1",

"Lastname", NULL, NULL,

ADS\_COMPOUND, &hIndex1 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "Create Index failed on table" );

return ulRetVal;

}

 

 

 

/\* Check how AOF's are optimized \*/

ulRetVal = AdsEvalAOF( hTable1,

"LASTNAME < 'Smith' AND LASTNAME >

Jefferson'", &usOptLevel );

 

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsEvalAOF 1 failed on table" );

return ulRetVal;

}

 

/\*

\* The index and the expression are both on LASTNAME,

\* so it should be fully optimized.

\*/

if ( usOptLevel != ADS\_OPTIMIZED\_FULL )

MessageBox( NULL, "AdsEvalAOF 1 returned wrong result", "DoAof",

MB\_OK );

 

ulRetVal = AdsEvalAOF( hTable1, "LASTNAME < 'Smith' AND FIRSTNAME >

'Mark'", &usOptLevel );

 

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsEvalAOF 2 failed on table" );

return ulRetVal;

}

 

/\* ADS\_OPTIMIZED\_FULL && ADS\_OPTIMIZED\_NONE == ADS\_OPTIMIZED\_PART \*/

if ( usOptLevel != ADS\_OPTIMIZED\_PART )

MessageBox( NULL, "AdsEvalAOF 2 returned wrong result", "DoAof",

MB\_OK );

 

ulRetVal = AdsEvalAOF( hTable1, "LASTNAME < 'Smith' OR FIRSTNAME >

'Mark'", &usOptLevel );

 

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsEvalAOF 3 failed on table" );

return ulRetVal;

}

 

/\* ADS\_OPTIMIZED\_FULL || ADS\_OPTIMIZED\_NONE == ADS\_OPTIMIZED\_NONE \*/

if ( usOptLevel != ADS\_OPTIMIZED\_NONE )

MessageBox( NULL, "AdsEvalAOF 3 returned wrong result", "DoAof",

MB\_OK );

 

 

/\* Set an Advantage Optimized Filter \*/

 

ulRetVal = AdsSetAOF( hTable1, "LASTNAME < 'Smith' AND FIRSTNAME >

'Mark'", ADS\_RESOLVE\_DYNAMIC );

 

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsSetAOF failed" );

return ulRetVal;

}

 

/\* Save the full Record count for later \*/

 

ulRetVal = AdsGetRecordCount( hTable1, ADS\_IGNOREFILTERS,

&ulRecCount0 );

 

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsGetRecordCount 0 failed" );

return ulRetVal;

}

 

 

 

/\* You can always find out what AOF is set \*/

usLength = sizeof(aucAOF);

ulRetVal = AdsGetAOF( hTable1, aucAOF, &usLength );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsGetAOF failed" );

return ulRetVal;

}

if ( strcmp( "LASTNAME < 'Smith' AND FIRSTNAME > 'Mark'", aucAOF ) )

MessageBox( NULL, "AdsGetAOF returned wrong string", "DoAof",

MB\_OK );

 

/\* Find out what part of our expression is not optimized \*/

usLength = sizeof(aucNonOpt);

 

ulRetVal = AdsGetAOFOptLevel( hTable1, &usOptLevel, aucNonOpt,

&usLength );

 

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsGetAOFOptLevel failed on table" );

return ulRetVal;

}

if ( usOptLevel != ADS\_OPTIMIZED\_PART )

MessageBox( NULL, "AdsGetAOFOptLevel returned wrong Level",

"DoAof", MB\_OK );

 

if ( strcmp( "FIRSTNAME>'Mark'", aucNonOpt ) )

MessageBox( NULL, "AdsGetAOFOptLevel returned wrong string",

"DoAof", MB\_OK );

 

/\* How many records pass the filter \*/

 

ulRetVal = AdsGetRecordCount( hTable1, ADS\_RESPECTFILTERS,

&ulRecCount1 );

 

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsGetRecordCount 1 failed" );

return ulRetVal;

}

if ( ulRecCount1 >= ulRecCount0 )

MessageBox( NULL, "AdsGetRecordCount did not decrease.", "DoAof",

MB\_OK );

 

 

 

/\*

\* Remove one record from the optimized portion of the filter

\* The record will still pass the filter until the filter is Refreshed

\*/

ulRetVal = AdsGotoTop( hTable1 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsGotoTop failed" );

return ulRetVal;

}

 

ulRetVal = AdsSetField( hTable1, "LASTNAME", "Smith", 5 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "SetField failed" );

return ulRetVal;

 

}

 

/\* The same number of records should pass the filter \*/

ulRetVal = AdsGetRecordCount( hTable1, ADS\_RESPECTFILTERS,

&ulRecCount2 );

 

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsGetRecordCount 2 failed" );

return ulRetVal;

}

if ( ulRecCount1 != ulRecCount2 )

MessageBox( NULL, "AdsGetRecordCount returned a different result",

"DoAof", MB\_OK );

 

/\* Refresh the AOF and the record should be removed from the filter \*/

ulRetVal = AdsRefreshAOF( hTable1 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsRefreshAOF failed" );

return ulRetVal;

}

 

 

ulRetVal = AdsGetRecordCount( hTable1, ADS\_RESPECTFILTERS,

&ulRecCount3 );

 

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsGetRecordCount 3 failed" );

return ulRetVal;

}

if ( ( ulRecCount1 - 1 ) != ulRecCount3 )

MessageBox( NULL, "AdsGetRecordCount 3 is not one less", "DoAof",

MB\_OK );

 

 

/\* Remove one record from the non-optimized portion of the filter

\* The record will be removed right away because ADS\_RESOLVE\_DYNAMIC

\* is specified.

\*

\* If ADS\_RESOLVE\_IMMEDIATE had been specified, it would not be

\* removed until the AOF was refreshed (just like the optimized

\* portion).

\*

\* ADS\_RESOLVE\_IMMEDIATE will also cause AdsGetRecordCount to be

\* faster.

\*/

ulRetVal = AdsGotoTop( hTable1 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsGotoTop failed" );

return ulRetVal;

}

 

ulRetVal = AdsSetField( hTable1, "FIRSTNAME", "Aaron", 5 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "SetField 2 failed" );

return ulRetVal;

}

 

/\* The record should be removed \*/

 

ulRetVal = AdsGetRecordCount( hTable1, ADS\_RESPECTFILTERS,

&ulRecCount4 );

 

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsGetRecordCount 4 failed" );

return ulRetVal;

}

if ( ( ulRecCount3 - 1 ) != ulRecCount4 )

MessageBox( NULL, "AdsGetRecordCount 4 is not one less", "DoAof",

MB\_OK );

 

/\* Clear the AOF and the record count should be restored \*/

ulRetVal = AdsClearAOF( hTable1 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsClearAOF failed" );

return ulRetVal;

}

 

ulRetVal = AdsGetRecordCount( hTable1, ADS\_RESPECTFILTERS,

&ulRecCount5 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsGetRecordCount 5 failed" );

return ulRetVal;

}

if ( ulRecCount5 != ulRecCount0 )

MessageBox( NULL, "AdsGetRecordCount is not restored.", "DoAof",

MB\_OK );

 

 

/\*

\* Try out a customized AOF. Start with a completely empty filter and

\* add some records to it. Using ".F." as the filter expression creates

\* a fully optimized empty filter.

\*/

ulRetVal = AdsSetAOF( hTable1, ".F.", ADS\_RESOLVE\_DYNAMIC );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsSetAOF failed" );

return ulRetVal;

}

 

/\* add 4 records to the AOF \*/

aulRecords[0] = 25;

aulRecords[1] = 50;

aulRecords[2] = 75;

aulRecords[3] = 100;

 

ulRetVal = AdsCustomizeAOF( hTable1, 4, /\* 4 records in the array \*/

aulRecords, ADS\_AOF\_ADD\_RECORD );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsCustomizeAOF failed" );

return ulRetVal;

}

 

/\*

\* Verify that one of the records is in the AOF bitmap. Note that this

\* call results in a server request. The work done on the server is very

\* minimal, but the network can be a bottleneck if this function is used

\* indiscriminately,

\*/

ulRetVal = AdsIsRecordInAOF( hTable1, 25, &bIsInAOF );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsIsRecordInOAF failed" );

return ulRetVal;

}

 

if ( !bIsInAOF )

MessageBox( NULL, "Record 25 should have been in the AOF", "DoAof", MB\_OK );

 

/\* count the records - should be 4 records only \*/

ulRetVal = AdsGetRecordCount( hTable1, ADS\_RESPECTFILTERS, &ulRecCount0 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsGetRecordCount 0 failed" );

return ulRetVal;

}

 

if ( ulRecCount0 != 4 )

MessageBox( NULL, "Expected to find 4 records in the AOF",

"DoAof", MB\_OK );

 

 

/\* Cleanup \*/

ulRetVal = AdsCloseAllIndexes( hTable1 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

ulRetVal = AdsCloseTable( hTable1 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

return AE\_SUCCESS;

} /\* DoAof \*/

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoEncrypt

\* API's Used : AdsDecryptRecord

\* AdsDecryptTable

\* AdsDisableEncryption

 

\* AdsEnableEncryption

\* AdsEncrypRecord

\* AdsEncryptTable

\* AdsIsRecordEncrypted

\* AdsIsTableEncrypted

\* AdsIsEncryptionEnabled

\*

\* AdsOpenTable

\* AdsCloseTable

\* AdsShowError

\* AdsGotoRecord

\* AdsSetField

\* AdsGetField

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

 

UNSIGNED32 DoEncrypt( void )

{

UNSIGNED32 ulRetVal;

 

ADSHANDLE hTable1;

 

UNSIGNED8 aucBuffer[64];

 

UNSIGNED32 ulLength;

 

UNSIGNED16 usIsEncrypted;

UNSIGNED16 usIsEnabled;

 

 

 

/\* open the table \*/

 

ulRetVal = AdsOpenTable( 0, "X:\\DATA\\DEMO1000.DBF", "TABLE1", ADS\_CDX, ADS\_ANSI, ADS\_PROPRIETARY\_LOCKING, ADS\_CHECKRIGHTS, ADS\_EXCLUSIVE, &hTable1 );

 

if ( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't open table" );

return ulRetVal;

}

 

 

/\* Enable encryption

\* Write to record 1; This should be written in encryped form

\*/

ulRetVal = AdsEnableEncryption( hTable1, "secret" );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsEnableEncryption 1 failed" );

return ulRetVal;

}

 

ulRetVal = AdsGotoRecord( hTable1, 1 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsGotoRecord( 1 ) failed" );

return ulRetVal;

}

 

ulRetVal = AdsSetField( hTable1, "LASTNAME", "Smith", 5 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "SetField 1 failed" );

return ulRetVal;

}

 

/\*

\* You may encrypt a single record without changing the

\* content of the record

\*/

ulRetVal = AdsGotoRecord( hTable1, 2 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsGotoRecord( 2 ) failed" );

return ulRetVal;

}

 

ulRetVal = AdsEncryptRecord( hTable1 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsEncryptRecord( 2 ) failed" );

}

 

/\* Disable encryption

\* Write to record 3; This should be written in plain text.

\*/

ulRetVal = AdsGotoRecord( hTable1, 3 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsGotoRecord( 3 ) failed" );

return ulRetVal;

}

 

ulRetVal = AdsDisableEncryption( hTable1 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsDisableEncryption failed" );

return ulRetVal;

}

 

ulRetVal = AdsSetField( hTable1, "LASTNAME", "Smith", 5 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "SetField 3 failed" );

return ulRetVal;

}

 

/\*

\* The table should not be encrypted

\* Only record 1 and 2 should be encrypted

\*/

ulRetVal = AdsIsTableEncrypted( hTable1, &usIsEncrypted );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsIsTableEncrypted 1 failed" );

return ulRetVal;

}

 

if ( usIsEncrypted != FALSE )

MessageBox( NULL, "AdsIsTableEncrypted 1 returned wrong result",

"DoEncrypt", MB\_OK );

 

/\* Check record 1 \*/

ulRetVal = AdsGotoRecord( hTable1, 1 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsGotoRecord( 1 ) failed" );

return ulRetVal;

}

 

ulRetVal = AdsIsRecordEncrypted( hTable1, &usIsEncrypted );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsIsRecordEncrypted 1 failed" );

return ulRetVal;

}

 

if ( usIsEncrypted == FALSE )

MessageBox( NULL, "AdsIsRecordEncrypted 1 returned wrong result",

"DoEncrypt", MB\_OK );

 

ulRetVal = AdsSetField( hTable1, "LASTNAME", "Wong", 4 );

if ( ulRetVal == AE\_SUCCESS )

{

AdsShowError( "SetField 1 on encrypted record should not succeed without enabling encryption" );

return ulRetVal;

}

 

/\* Read field should give us garbage \*/

ulLength = sizeof( aucBuffer );

ulRetVal = AdsGetField( hTable1, "LASTNAME", aucBuffer, &ulLength, ADS\_NONE );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "GetField 1 on encrypted record failed" );

return ulRetVal;

}

 

if ( strncmp( aucBuffer, "Smith", 5 ) == 0 )

MessageBox( NULL, "Record 1 does not appear to be encrypted",

"DoEncrypt", MB\_OK );

 

/\* Check record 2 \*/

ulRetVal = AdsGotoRecord( hTable1, 2 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsGotoRecord( 2 ) failed" );

return ulRetVal;

}

ulRetVal = AdsIsRecordEncrypted( hTable1, &usIsEncrypted );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsIsRecordEncrypted 2 failed" );

return ulRetVal;

}

 

if ( usIsEncrypted == FALSE )

MessageBox( NULL, "AdsIsRecordEncrypted 2 returned wrong result",

"DoEncrypt", MB\_OK );

 

/\* Check record 3 \*/

ulRetVal = AdsGotoRecord( hTable1, 3 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsGotoRecord( 3 ) failed" );

return ulRetVal;

}

 

ulRetVal = AdsIsRecordEncrypted( hTable1, &usIsEncrypted );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsIsRecordEncrypted 3 failed" );

return ulRetVal;

}

 

if ( usIsEncrypted != FALSE )

MessageBox( NULL, "AdsIsRecordEncrypted 3 returned wrong result",

"DoEncrypt", MB\_OK );

 

 

 

 

ulRetVal = AdsEnableEncryption( hTable1, "secret" );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsEnableEncryption 2 failed" );

return ulRetVal;

}

 

/\* You can test the current encryption status \*/

ulRetVal = AdsIsEncryptionEnabled( hTable1, &usIsEnabled );

if ( ulRetVal != AE\_SUCCESS )

 

{

AdsShowError( "AdsIsEncryptionEnabled 1 failed" );

return ulRetVal;

}

if ( usIsEnabled == FALSE )

MessageBox( NULL, "AdsIsEncryptionEnabled 1 returned wrong result",

"DoEncrypt", MB\_OK );

 

/\* Read field automatically decrypts the record when encryption is enabled \*/

/\* Check record 1 \*/

ulRetVal = AdsGotoRecord( hTable1, 1 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsGotoRecord( 1 ) failed" );

return ulRetVal;

}

 

ulLength = sizeof( aucBuffer );

ulRetVal = AdsGetField( hTable1, "LASTNAME", aucBuffer, &ulLength, ADS\_NONE );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "GetField 1 on encrypted record failed" );

return ulRetVal;

}

 

if ( strncmp( aucBuffer, "Smith", 5 ) != 0 )

MessageBox( NULL, "Record 1 did not decrypt correcct",

"DoEncrypt", MB\_OK );

 

/\* Decrypt a record \*/

ulRetVal = AdsGotoRecord( hTable1, 2 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsGotoRecord( 2 ) failed" );

return ulRetVal;

}

 

ulRetVal = AdsDecryptRecord( hTable1 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsDecryptRecord( 2 ) failed" );

return ulRetVal;

}

 

ulRetVal = AdsIsRecordEncrypted( hTable1, &usIsEncrypted );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsIsRecordEncrypted 2 failed" );

return ulRetVal;

}

 

if ( usIsEncrypted != FALSE )

MessageBox( NULL, "AdsIsRecordEncrypted 2 returned wrong result",

"DoEncrypt", MB\_OK );

 

 

/\* AdsEncryptTable encrypts all non-encrypted records

\* You must have encryption enabled to encrypt a table

 

\* Also notice that the table was opened with ADS\_EXCLUSIVE

\*

\*/

ulRetVal = AdsEncryptTable( hTable1 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsEncryptTable failed" );

return ulRetVal;

}

 

ulRetVal = AdsDisableEncryption( hTable1 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsDisableEncryption 2 failed" );

return ulRetVal;

}

 

/\* You can ask ACE if the current table is encrypted \*/

ulRetVal = AdsIsTableEncrypted( hTable1, &usIsEncrypted );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsIsTableEncrypted 2 failed" );

return ulRetVal;

}

if ( usIsEncrypted == FALSE )

 

MessageBox( NULL, "AdsIsTableEncrypted 2 returned wrong result",

"DoEncrypt", MB\_OK );

 

 

/\* Try to use the wrong password \*/

ulRetVal = AdsEnableEncryption( hTable1, "PassWord" );

if ( ulRetVal == AE\_SUCCESS )

{

AdsShowError( "AdsEnableEncryption 4 should failed" );

return ulRetVal;

}

 

/\* You can test the current encryption status \*/

ulRetVal = AdsIsEncryptionEnabled( hTable1, &usIsEnabled );

if ( ulRetVal != AE\_SUCCESS )

 

{

AdsShowError( "AdsIsEncryptionEnabled 2 failed" );

return ulRetVal;

}

if ( usIsEnabled != FALSE )

MessageBox( NULL, "AdsIsEncryptionEnabled 2 returned wrong result",

"DoEncrypt", MB\_OK );

 

 

/\* AdsDecryptTable decrypts all encrypted records

\* You must have encryption enabled to decrypt a table

\*/

ulRetVal = AdsEnableEncryption( hTable1, "secret" );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsEnableEncryption 5 failed" );

return ulRetVal;

}

 

ulRetVal = AdsDecryptTable( hTable1 );

 

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsDecryptTable failed" );

return ulRetVal;

}

 

/\* After the whole table is decrypted, encryption should be disabled \*/

ulRetVal = AdsIsEncryptionEnabled( hTable1, &usIsEnabled );

if ( ulRetVal != AE\_SUCCESS )

 

{

AdsShowError( "AdsIsEncryptionEnabled 3 failed" );

return ulRetVal;

}

if ( usIsEnabled != FALSE )

MessageBox( NULL, "AdsIsEncryptionEnabled 3 returned wrong result",

"DoEncrypt", MB\_OK );

 

/\* AdsIsTableEncrypted should return FALSE \*/

ulRetVal = AdsIsTableEncrypted( hTable1, &usIsEncrypted );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsIsTableEncrypted 3 failed" );

 

return ulRetVal;

}

if ( usIsEncrypted != FALSE )

MessageBox( NULL, "AdsIsTableEncrypted 3 returned wrong result",

"DoEncrypt", MB\_OK );

 

 

/\* Now it is OK to switch to another password \*/

ulRetVal = AdsEnableEncryption( hTable1, "PassWord" );

if ( ulRetVal != AE\_SUCCESS )

{

AdsShowError( "AdsEnableEncryption 5 failed" );

return ulRetVal;

}

 

 

/\* Cleanup \*/

ulRetVal = AdsCloseTable( hTable1 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

return AE\_SUCCESS;

} /\* DoEncrypt \*/
