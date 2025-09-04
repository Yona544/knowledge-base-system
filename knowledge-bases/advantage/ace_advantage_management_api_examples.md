Advantage Management API Examples




Advantage Database Server 12  

Advantage Management API Examples

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Management API Examples  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - Advantage Management API Examples Advantage Client Engine ace\_Advantage\_management\_api\_examples Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Advantage Management API Examples  Advantage Client Engine |  |  |  |  |

#include <windows.h>

#include <assert.h>

#include <stdio.h>

#include "ace.h"

 

 

/\* The MAX constants can be defined to whatever size is needed \*/

#define MAX\_NUM\_USERS 50

#define MAX\_NUM\_TABLES 50

#define MAX\_NUM\_INDEXES 50

#define MAX\_NUM\_RECORDS 100

 

/\* 1024 is the maximum number of worker threads available \*/

#define MAX\_NUM\_THREADS 1024

 

#define ERR\_ADS\_FILE\_NOT\_OPEN 7051

#define ERR\_USER\_NOT\_FOUND 7050

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Function : DoManagementAPIs

\* APIs used :

\* AdsMgConnect

\* AdsMgDisconnect

\* AdsMgGetInstallInfo

\* AdsMgGetActivityInfo

\* AdsMgGetCommStats

\* AdsMgResetCommStats

\* AdsMgGetConfigInfo

\* AdsMgGetUserNames

\* AdsMgGetOpenTables

\* AdsMgGetOpenIndexes

\* AdsMgGetLocks

\* AdsMgGetServerType

\* AdsMgGetWorkerThreadActivity

\* AdsMgGetLockOwner

\* AdsMgKillUser

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

UNSIGNED32 DoManagementAPIs( void )

{

ADSHANDLE hMgmtHandle;

ADSHANDLE hTable;

ADSHANDLE hConnect;

ADS\_MGMT\_COMM\_STATS stCommStats;

ADS\_MGMT\_CONFIG\_PARAMS stConfigValues;

ADS\_MGMT\_CONFIG\_MEMORY stConfigMemory;

ADS\_MGMT\_INSTALL\_INFO stInstallInfo;

ADS\_MGMT\_ACTIVITY\_INFO stActivityInfo;

ADS\_MGMT\_TABLE\_INFO astOpenTableInfo[MAX\_NUM\_TABLES];

ADS\_MGMT\_USER\_INFO astUserInfo[MAX\_NUM\_USERS];

ADS\_MGMT\_INDEX\_INFO astOpenIndexInfo[MAX\_NUM\_INDEXES];

ADS\_MGMT\_RECORD\_INFO astRecordInfo[MAX\_NUM\_RECORDS];

ADS\_MGMT\_THREAD\_ACTIVITY astWorkerThreadActivity[MAX\_NUM\_THREADS];

ADS\_MGMT\_USER\_INFO stUserInfo;

UNSIGNED32 ulRetVal = AE\_SUCCESS;

UNSIGNED32 ulLockedRecord;

 

UNSIGNED16 usLockType;

UNSIGNED16 usServerType;

UNSIGNED16 usConfigValuesStructSize;

UNSIGNED16 usConfigMemoryStructSize;

UNSIGNED16  usStructSize;

UNSIGNED16 usArrayLen;

UNSIGNED16 usCount;

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgConnect - Get a Management Connection Handle. The

\* user name and password parameters are currently not supported.

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

 

ulRetVal = AdsMgConnect( "\\\\server\\volume:", NULL, NULL, &hMgmtHandle );

assert( ulRetVal == AE\_SUCCESS );

 

/\* Open a table to work with \*/

/\* open the DBF \*/

hConnect = 0;

ulRetVal = AdsOpenTable( hConnect, "\\\\server\\volume\\data\\employee.dbf",

"test1",

ADS\_CDX,

ADS\_ANSI,

ADS\_PROPRIETARY\_LOCKING,

ADS\_CHECKRIGHTS,

ADS\_DEFAULT,

&hTable );

 

if ( ulRetVal != AE\_SUCCESS )

{

MessageBox( (HWND)NULL, "Connection Error", "Test", MB\_OK );

return -1;

}

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetCommStats

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

 

usStructSize = sizeof( ADS\_MGMT\_COMM\_STATS );

ulRetVal = AdsMgGetCommStats( hMgmtHandle, &stCommStats, &usStructSize );

assert( ulRetVal == AE\_SUCCESS );

 

/\* If usStructSize returned is bigger than what was submitted then the

\* version of the server is newer and is relaying that more data is

\* possible to retrieve. The client just needs the most recent ACE.H

\* header.

\*/

if ( sizeof( ADS\_MGMT\_COMM\_STATS ) < usStructSize )

{

/\* Print warning \*/

printf( "\nCommunication Statistics structure on server is larger." );

printf( "\nMore possible info available." );

}

 

/\* Print out the number of total packets received \*/

printf( "\nTotal packets received is %ld", stCommStats.ulTotalPackets );

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgResetCommStats

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

 

ulRetVal = AdsMgResetCommStats( hMgmtHandle );

assert( ulRetVal == AE\_SUCCESS );

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetConfigInfo tests

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

usConfigValuesStructSize = sizeof( ADS\_MGMT\_CONFIG\_PARAMS );

usConfigMemoryStructSize = sizeof( ADS\_MGMT\_CONFIG\_MEMORY );

 

ulRetVal = AdsMgGetConfigInfo( hMgmtHandle, &stConfigValues,

&usConfigValuesStructSize,

&stConfigMemory, &usConfigMemoryStructSize );

assert( ulRetVal == AE\_SUCCESS );

 

/\* Print out the maximum number of connections and the total memory taken

\* by the connections

\*/

printf( "\nThe maximum number of connections is %ld",

stConfigValues.ulNumConnections );

printf( "\nThe total memory taken by connections is %ld",

stConfigMemory.ulConnectionMem );

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetInstallInfo tests

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

usStructSize = sizeof( ADS\_MGMT\_INSTALL\_INFO );

ulRetVal = AdsMgGetInstallInfo( hMgmtHandle, &stInstallInfo, &usStructSize );

assert( ulRetVal == AE\_SUCCESS );

 

/\* If usStructSize returned is bigger than what was submitted then the

\* version of the server is newer and is relaying that more data is

\* possible to retrieve. The client just needs the most recent ACE.H

\* header.

\*/

if ( sizeof( ADS\_MGMT\_INSTALL\_INFO ) < usStructSize )

{

/\* Print warning \*/

printf( "\nInstallation Information structure on server is larger." );

printf( "\nMore possible info available." );

}

 

/\* Print out the registered owner \*/

printf( "\nThe registered owner of the Advantage Database Server is '%s'",

stInstallInfo.aucRegisteredOwner );

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetActivityInfo tests

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

usStructSize = sizeof( ADS\_MGMT\_ACTIVITY\_INFO );

 

ulRetVal = AdsMgGetActivityInfo( hMgmtHandle, &stActivityInfo, &usStructSize );

assert( ulRetVal == AE\_SUCCESS );

 

/\* if usStructSize returned is bigger than what was submitted then the

\* version of the server is newer and is relaying that more data is

\* possible to retrieve. The client just needs the most recent ACE.H

\* header.

\*/

if ( sizeof( ADS\_MGMT\_ACTIVITY\_INFO ) < usStructSize )

{

/\* Print warning \*/

printf( "\nActivity Information structure on server is larger." );

printf( "\nMore possible info available." );

}

 

/\* Print out the activity informations up time of the server \*/

printf( "\nThe up time of the server is %d Days %d Hours %d Minutes %d Seconds.",

stActivityInfo.stUpTime.usDays, stActivityInfo.stUpTime.usHours,

stActivityInfo.stUpTime.usMinutes,

stActivityInfo.stUpTime.usSeconds );

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetUserNames

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

usArrayLen = MAX\_NUM\_USERS;

usStructSize = sizeof( ADS\_MGMT\_USER\_INFO );

 

ulRetVal = AdsMgGetUserNames( hMgmtHandle, NULL, astUserInfo,

&usArrayLen, &usStructSize );

assert( ulRetVal == AE\_SUCCESS );

 

/\* if usStructSize returned is bigger than what was submitted then the

\* version of the server is newer and is relaying that more data is

\* possible to retrieve. The client just needs the most recent ACE.H

\* header.

\*/

if ( sizeof( ADS\_MGMT\_USER\_INFO ) < usStructSize )

{

/\* Print warning \*/

printf( "\nUser Information structure on server is larger." );

printf( "\nMore possible info available." );

}

 

/\* Print the number of users returned \*/

printf( "\nThe number of connected users is %d", usArrayLen );

 

/\* Print out the connected users \*/

for ( usCount = 0; usCount < usArrayLen; usCount++ )

{

printf( "\nUser %s is connected", astUserInfo[usCount].aucUserName );

}

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetOpenTables tests

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

usArrayLen = MAX\_NUM\_USERS;

usStructSize = sizeof( ADS\_MGMT\_TABLE\_INFO );

 

ulRetVal = AdsMgGetOpenTables( hMgmtHandle,

NULL,

0,

astOpenTableInfo,

&usArrayLen,

&usStructSize );

assert( ulRetVal == AE\_SUCCESS );

 

/\* if usStructSize returned is bigger than what was submitted then the

\* version of the server is newer and is relaying that more data is

\* possible to retrieve. The client just needs the most recent ACE.H

\* header.

\*/

if ( sizeof( ADS\_MGMT\_TABLE\_INFO ) < usStructSize )

{

/\* Print warning \*/

printf( "\nTable Information structure on server is larger." );

printf( "\nMore possible info available." );

}

 

/\* Print the number of open tables returned \*/

printf( "\nThe number of open tables is %d", usArrayLen );

 

/\* Print out the open tables \*/

for ( usCount = 0; usCount < usArrayLen; usCount++ )

{

printf( "\nTable %s is open.", astOpenTableInfo[usCount].aucTableName );

}

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetOpenIndexes tests

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

usArrayLen = MAX\_NUM\_USERS;

usStructSize = sizeof( ADS\_MGMT\_INDEX\_INFO );

 

ulRetVal = AdsMgGetOpenIndexes( hMgmtHandle,

"\\\\server\\volume\\data\\employee.dbf",

NULL,

0,

astOpenIndexInfo,

&usArrayLen,

&usStructSize );

assert( ulRetVal == AE\_SUCCESS );

 

/\* if usStructSize returned is bigger than what was submitted then the

\* version of the server is newer and is relaying that more data is

\* possible to retrieve. The client just needs the most recent ACE.H

\* header.

\*/

if ( sizeof( ADS\_MGMT\_INDEX\_INFO ) < usStructSize )

{

/\* Print warning \*/

printf( "\nIndex Information structure on server is larger." );

printf( "\nMore possible info available." );

}

 

/\* Print the number of open indexes returned \*/

printf( "\nThe number of open indexes is %d", usArrayLen );

 

/\* Print out the open Indexes \*/

for ( usCount = 0; usCount < usArrayLen; usCount++ )

{

printf( "\nIndex %s is open", astOpenIndexInfo[usCount].aucIndexName );

}

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetLocks tests

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

ulLockedRecord = 5;

ulRetVal = AdsLockRecord( hTable, ulLockedRecord );

assert( ulRetVal == AE\_SUCCESS );

 

usArrayLen = MAX\_NUM\_USERS;

usStructSize = sizeof( ADS\_MGMT\_RECORD\_INFO );

 

ulRetVal = AdsMgGetLocks( hMgmtHandle,

"\\\\server\\volume\\data\\employee.dbf",

NULL,

0,

astRecordInfo,

&usArrayLen,

&usStructSize );

assert( ulRetVal == AE\_SUCCESS );

 

/\* if usStructSize returned is bigger than what was submitted then the

\* version of the server is newer and is relaying that more data is

\* possible to retrieve. The client just needs the most recent ACE.H

\* header.

\*/

if ( sizeof( ADS\_MGMT\_RECORD\_INFO ) < usStructSize )

{

/\* Print warning \*/

printf( "\nRecord Information structure on server is larger." );

printf( "\nMore possible info available." );

}

 

/\* Print the number of locks returned \*/

printf( "\nThe number of locks is %d", usArrayLen );

 

/\* Print out the locks \*/

for ( usCount = 0; usCount < usArrayLen; usCount++ )

{

/\* Take care of the file lock case \*/

if ( astRecordInfo[usCount].ulRecordNumber == 0 )

{

printf( "\nFile is locked" );

break;

}

else

printf( "\nLock on record %ld", astRecordInfo[usCount].ulRecordNumber );

}

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetServerType

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

 

ulRetVal = AdsMgGetServerType( hMgmtHandle, &usServerType );

assert( ulRetVal == AE\_SUCCESS );

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetWorkerThreadActivity

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

usArrayLen = MAX\_NUM\_THREADS;

usStructSize = sizeof( ADS\_MGMT\_THREAD\_ACTIVITY );

 

ulRetVal = AdsMgGetWorkerThreadActivity( hMgmtHandle,

astWorkerThreadActivity,

&usArrayLen,

&usStructSize );

assert( ulRetVal == AE\_SUCCESS );

 

/\* if usStructSize returned is bigger than what was submitted then the

\* version of the server is newer and is relaying that more data is

\* possible to retrieve. The client just needs the most recent ACE.H

\* header.

\*/

if ( sizeof( ADS\_MGMT\_THREAD\_ACTIVITY ) < usStructSize )

{

/\* Print warning \*/

printf( "\nWorker Thread Activity structure on server is larger." );

printf( "\nMore possible info available." );

}

 

/\* Print the number of threads returned \*/

printf( "\nThe number of threads is %d", usArrayLen );

 

/\* Print out the worker threads \*/

for ( usCount = 0; usCount < usArrayLen; usCount++ )

{

printf( "\nThread %ld is in use by %s",

astWorkerThreadActivity[usCount].ulThreadNumber,

astWorkerThreadActivity[usCount].aucUserName );

}

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetLockOwner

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

usStructSize = sizeof( ADS\_MGMT\_USER\_INFO );

 

ulRetVal = AdsMgGetLockOwner( hMgmtHandle,

"\\\\server\\volume\\data\\employee.dbf",

ulLockedRecord,

&stUserInfo,

&usStructSize,

&usLockType );

assert( ulRetVal == AE\_SUCCESS );

 

/\* if usStructSize returned is bigger than what was submitted then the

\* version of the server is newer and is relaying that more data is

\* possible to retrieve. The client just needs the most recent ACE.H

\* header.

\*/

if ( sizeof( ADS\_MGMT\_USER\_INFO ) < usStructSize )

{

/\* Print warning \*/

printf( "\nUser Information structure on server is larger." );

printf( "\nMore possible info available." );

}

 

/\* Print out the owner of the lock \*/

printf( "\nUser %s has record %ld locked", stUserInfo.aucUserName, ulLockedRecord );

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgKillUser

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

 

ulRetVal = AdsMgKillUser( hMgmtHandle,

"JohnDoe",

0 );

assert( ulRetVal == AE\_SUCCESS );

 

 

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgDisconnect - Close a Management Connection Handle.

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

 

/\* close the table \*/

ulRetVal = AdsCloseTable( hTable );

assert( ulRetVal == AE\_SUCCESS );

 

ulRetVal = AdsMgDisconnect( hMgmtHandle );

assert( ulRetVal == AE\_SUCCESS );

 

 

return ( ulRetVal );

 

} /\* DoManagementAPIs \*/