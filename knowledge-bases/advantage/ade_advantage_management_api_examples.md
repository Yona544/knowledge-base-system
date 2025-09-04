Advantage Management API Examples




Advantage Database Server 12  

Advantage Management API Examples

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Management API Examples  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Advantage Management API Examples Advantage TDataSet Descendant ade\_Advantage\_management\_api\_examples Advantage TDataSet Descendant > Adding Management Capabilities > Advantage Management API Examples / Dear Support Staff, |  |
| Advantage Management API Examples  Advantage TDataSet Descendant |  |  |  |  |

This is a simple example that uses every Advantage management API. To see sample management API code in an actual working Advantage Delphi application, refer to the source code shipped with the Advantage Data Architect that is a separate product shipped with the Advantage TDataSet Descendant .

unit mgmtapi;

 

interface

 

procedure DoManagementAPIs;

 

const

{ The MAX constants can be defined to whatever size is needed }

MAX\_NUM\_USERS = 50;

MAX\_NUM\_TABLES = 50;

MAX\_NUM\_INDEXES = 50;

MAX\_NUM\_RECORDS = 100;

 

{ 1024 is the maximum number of worker threads available }

MAX\_NUM\_THREADS = 1024;

 

ERR\_ADS\_FILE\_NOT\_OPEN = 7051;

ERR\_USER\_NOT\_FOUND = 7050;

 

 

implementation

 

{ Refer to ACE.PAS for type descriptions and structure definitions }

Uses ACE, Dialogs, SysUtils;

 

 

{\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Procedure : DoManagementAPIs

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

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*}

procedure DoManagementAPIs;

var

hMgmtHandle : ADSHANDLE;

stCommStats : ADS\_MGMT\_COMM\_STATS;

stConfigValues : ADS\_MGMT\_CONFIG\_PARAMS;

stConfigMemory : ADS\_MGMT\_CONFIG\_MEMORY;

stInstallInfo : ADS\_MGMT\_INSTALL\_INFO;

stActivityInfo : ADS\_MGMT\_ACTIVITY\_INFO;

astOpenTableInfo : array[0..MAX\_NUM\_TABLES] of ADS\_MGMT\_TABLE\_INFO;

astUserInfo : array[0..MAX\_NUM\_USERS] of ADS\_MGMT\_USER\_INFO;

 

astOpenIndexInfo : array[0..MAX\_NUM\_INDEXES] of ADS\_MGMT\_INDEX\_INFO;

astRecordInfo : array[0..MAX\_NUM\_RECORDS] of ADS\_MGMT\_RECORD\_INFO;

astWorkerThreadActivity : array[0..MAX\_NUM\_THREADS] of ADS\_MGMT\_THREAD\_ACTIVITY;

stUserInfo : ADS\_MGMT\_USER\_INFO;

ulRetVal : UNSIGNED32;

ulLockedRecord : UNSIGNED32;

usLockType : UNSIGNED16;

usServerType : UNSIGNED16;

usConfigValuesStructSize : UNSIGNED16;

usConfigMemoryStructSize : UNSIGNED16;

usStructSize : UNSIGNED16;

usArrayLen : UNSIGNED16;

usCount : UNSIGNED16;

begin

 

{\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgConnect - Get a Management Connection Handle. The

\* user name and password parameters are currently not supported.

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*}

 

ulRetVal := ACE.AdsMgConnect( '\\server\volume:', nil, nil, @hMgmtHandle );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

ShowMessage( 'Connection Error' );

exit;

end;

 

 

{\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetCommStats

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*}

 

usStructSize := sizeof( ADS\_MGMT\_COMM\_STATS );

ulRetVal := ACE.AdsMgGetCommStats( hMgmtHandle, @stCommStats, @usStructSize );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

ShowMessage( 'Get Comm Stats Error' );

exit;

end;

 

{\*

\* if usStructSize returned is bigger than what was submitted then the

\* version of the server is newer and is relaying that more data is

\* possible to retrieve. The client just needs the most recent ACE.PAS

\* header.

\*}

if ( sizeof( ADS\_MGMT\_COMM\_STATS ) < usStructSize ) then

begin

{ Print warning }

ShowMessage( 'Communication Statistics structure on server is larger. ' +

'More possible info available.' );

end;

 

{ Print out the number of total packets received }

ShowMessage( 'Total packets received is: ' + IntToStr( stCommStats.ulTotalPackets ) );

 

 

{\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgResetCommStats

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*}

 

ulRetVal := ACE.AdsMgResetCommStats( hMgmtHandle );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

ShowMessage( 'Reset Comm Stats Error' );

exit;

end;

 

 

{\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetConfigInfo tests

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*}

usConfigValuesStructSize := sizeof( ADS\_MGMT\_CONFIG\_PARAMS );

usConfigMemoryStructSize := sizeof( ADS\_MGMT\_CONFIG\_MEMORY );

 

ulRetVal := ACE.AdsMgGetConfigInfo( hMgmtHandle, @stConfigValues,

@usConfigValuesStructSize,

@stConfigMemory, @usConfigMemoryStructSize );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

ShowMessage( 'Get Config Info Error' );

exit;

end;

 

{\*

\* if struct sizes returned is bigger than what was submitted then the

\* version of the server is newer and is relaying that more data is

\* possible to retrieve. The client just needs the most recent ACE.PAS

\* header.

\*}

if ( sizeof( ADS\_MGMT\_CONFIG\_PARAMS ) < usConfigValuesStructSize ) then

begin

{ Print warning }

ShowMessage( 'Configuration Values structure on server is larger. ' +

'More possible info available.' );

end;

 

if ( sizeof( ADS\_MGMT\_CONFIG\_MEMORY ) < usConfigMemoryStructSize ) then

begin

{ Print warning }

ShowMessage( 'Configuration Memory structure on server is larger. ' +

'More possible info available.' );

end;

 

{\*

\* Print out the maximum number of connections and the total memory taken by

\* the connections.

\*}

ShowMessage( 'The maximum number of connections is : ' +

IntToStr( stConfigValues.ulNumConnections ) );

ShowMessage( 'The total memory taken by connections is : ' +

IntToStr( stConfigMemory.ulConnectionMem ) );

 

 

{\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetInstallInfo tests

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*}

usStructSize := sizeof( ADS\_MGMT\_INSTALL\_INFO );

 

ulRetVal := ACE.AdsMgGetInstallInfo( hMgmtHandle, @stInstallInfo, @usStructSize );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

ShowMessage( 'Get Install Info Error' );

exit;

end;

 

{\*

\* if usStructSize returned is bigger than what was submitted then the

\* version of the server is newer and is relaying that more data is

\* possible to retrieve. The client just needs the most recent ACE.PAS

\* header.

\*}

if ( sizeof( ADS\_MGMT\_INSTALL\_INFO ) < usStructSize ) then

begin

{ Print warning }

ShowMessage( 'Installation Information structure on server is larger. ' +

'More possible info available.' );

end;

 

{ Print out the registered owner }

ShowMessage( 'The registered owner of the Advantage Database Server is ' +

StrPas( stInstallInfo.aucRegisteredOwner ) );

 

 

{\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetActivityInfo tests

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*}

usStructSize := sizeof( ADS\_MGMT\_ACTIVITY\_INFO );

 

ulRetVal := ACE.AdsMgGetActivityInfo( hMgmtHandle, @stActivityInfo, @usStructSize );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

ShowMessage( 'Get Activity Info Error' );

exit;

end;

 

{\*

\* if usStructSize returned is bigger than what was submitted then the

\* version of the server is newer and is relaying that more data is

\* possible to retrieve. The client just needs the most recent ACE.PAS

\* header.

\*}

if ( sizeof( ADS\_MGMT\_ACTIVITY\_INFO ) < usStructSize ) then

begin

{ Print warning }

ShowMessage( 'Activity Information structure on server is larger. ' +

'More possible info available.' );

end;

 

{ Print out the activity informations up time of the server }

ShowMessage( 'The up time of the server is: ' +

IntToStr( stActivityInfo.stUpTime.usDays ) + ' Days, ' +

IntToStr( stActivityInfo.stUpTime.usHours ) + ' Hours, ' +

IntToStr( stActivityInfo.stUpTime.usMinutes ) + ' Minutes, ' +

IntToStr( stActivityInfo.stUpTime.usSeconds ) + ' Seconds.' );

 

 

{\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetUserNames

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*}

usArrayLen := MAX\_NUM\_USERS;

usStructSize := sizeof( ADS\_MGMT\_USER\_INFO );

 

ulRetVal := ACE.AdsMgGetUserNames( hMgmtHandle, nil, @astUserInfo,

@usArrayLen, @usStructSize );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

ShowMessage( 'Get User Names Error' );

exit;

end;

 

{\*

\* if usStructSize returned is bigger than what was submitted then the

\* version of the server is newer and is relaying that more data is

\* possible to retrieve. The client just needs the most recent ACE.PAS

\* header.

\*}

if ( sizeof( ADS\_MGMT\_USER\_INFO ) < usStructSize ) then

begin

{ Print warning }

ShowMessage( 'User Information structure on server is larger. ' +

'More possible info available.' );

end;

 

{ Print the number of users returned }

ShowMessage( 'The number of connected users is ' + IntToStr( usArrayLen ) );

 

{ Print out the connected users }

for usCount := 0 to usArrayLen - 1 do

begin

ShowMessage( 'User ' + StrPas( astUserInfo[usCount].aucUserName ) +

' is connected' );

end;

 

 

{\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetOpenTables tests

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*}

usArrayLen := MAX\_NUM\_USERS;

usStructSize := sizeof( ADS\_MGMT\_TABLE\_INFO );

 

ulRetVal := ACE.AdsMgGetOpenTables( hMgmtHandle,

nil,

0,

@astOpenTableInfo,

@usArrayLen,

@usStructSize );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

ShowMessage( 'Get Open Tables Error' );

exit;

end;

 

{\*

\* if usStructSize returned is bigger than what was submitted then the

\* version of the server is newer and is relaying that more data is

\* possible to retrieve. The client just needs the most recent ACE.PAS

\* header.

\*}

if ( sizeof( ADS\_MGMT\_TABLE\_INFO ) < usStructSize ) then

begin

{ Print warning }

ShowMessage( 'Table Information structure on server is larger. ' +

'More possible info available.' );

end;

 

{ Print the number of open tables returned }

ShowMessage( 'The number of open tables is: ' + IntToStr( usArrayLen ) );

 

{ Print out the open tables }

for usCount := 0 to usArrayLen - 1 do

begin

ShowMessage( 'Table ' + StrPas( astOpenTableInfo[usCount].aucTableName ) +

' is open.' );

end;

 

 

{\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetOpenIndexes tests

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*}

usArrayLen := MAX\_NUM\_USERS;

usStructSize := sizeof( ADS\_MGMT\_INDEX\_INFO );

 

ulRetVal := ACE.AdsMgGetOpenIndexes( hMgmtHandle,

'\\server\volume\data\employee.dbf',

nil,

0,

@astOpenIndexInfo,

@usArrayLen,

@usStructSize );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

ShowMessage( 'Get Open Indexes Error' );

exit;

end;

 

{\*

\* if usStructSize returned is bigger than what was submitted then the

\* version of the server is newer and is relaying that more data is

\* possible to retrieve. The client just needs the most recent ACE.PAS

\* header.

\*}

if ( sizeof( ADS\_MGMT\_INDEX\_INFO ) < usStructSize ) then

begin

{ Print warning }

ShowMessage( 'Index Information structure on server is larger. ' +

'More possible info available.' );

end;

 

{ Print the number of open indexes returned }

ShowMessage( 'The number of open indexes is: ' + IntToStr( usArrayLen ) );

 

{ Print out the open Indexes }

for usCount := 0 to usArrayLen - 1 do

begin

ShowMessage( 'Index ' + StrPas( astOpenIndexInfo[usCount].aucIndexName ) +

' is open' );

end;

 

 

{\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetLocks tests

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*}

usArrayLen := MAX\_NUM\_USERS;

usStructSize := sizeof( ADS\_MGMT\_RECORD\_INFO );

 

ulRetVal := ACE.AdsMgGetLocks( hMgmtHandle,

'\\server\volume\data\employee.dbf',

nil,

0,

@astRecordInfo,

@usArrayLen,

@usStructSize );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

ShowMessage( 'Get Locks Error' );

exit;

end;

 

{\*

\* if usStructSize returned is bigger than what was submitted then the

\* version of the server is newer and is relaying that more data is

\* possible to retrieve. The client just needs the most recent ACE.PAS

\* header.

\*}

if ( sizeof( ADS\_MGMT\_RECORD\_INFO ) < usStructSize ) then

begin

{ Print warning }

ShowMessage( 'Record Information structure on server is larger. ' +

'More possible info available.' );

end;

 

{ Print the number of locks returned }

ShowMessage( 'The number of locks is: ' + IntToStr( usArrayLen ) );

 

{ Print out the locks }

for usCount := 0 to usArrayLen - 1 do

begin

{ Take care of the file lock case }

if ( astRecordInfo[usCount].ulRecordNumber = 0 ) then

ShowMessage( 'File is locked' )

else

ShowMessage( 'Lock on record : ' +

IntToStr( astRecordInfo[usCount].ulRecordNumber ) );

 

end;

 

 

{\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetServerType

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*}

 

ulRetVal := ACE.AdsMgGetServerType( hMgmtHandle, @usServerType );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

ShowMessage( 'Get Server Type Error' );

exit;

end;

 

 

{\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetWorkerThreadActivity

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*}

usArrayLen := MAX\_NUM\_THREADS;

usStructSize := sizeof( ADS\_MGMT\_THREAD\_ACTIVITY );

 

ulRetVal := ACE.AdsMgGetWorkerThreadActivity( hMgmtHandle,

@astWorkerThreadActivity,

@usArrayLen,

@usStructSize );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

ShowMessage( 'Get Worker Thread Info Error' );

exit;

end;

 

{\*

\* if usStructSize returned is bigger than what was submitted then the

\* version of the server is newer and is relaying that more data is

\* possible to retrieve. The client just needs the most recent ACE.PAS

\* header.

\*}

if ( sizeof( ADS\_MGMT\_THREAD\_ACTIVITY ) < usStructSize ) then

begin

{ Print warning }

ShowMessage( 'Worker Thread Activity structure on server is larger. ' +

'More possible info available.' );

end;

 

{ Print the number of threads returned }

ShowMessage( 'The number of threads is: ' + IntToStr( usArrayLen ) );

 

{ Print out the worker threads }

for usCount := 0 to usArrayLen - 1 do

begin

ShowMessage( 'Thread : ' +

IntToStr( astWorkerThreadActivity[usCount].ulThreadNumber ) +

'is in use by ' +

StrPas( astWorkerThreadActivity[usCount].aucUserName ) );

end;

 

 

{\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgGetLockOwner

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*}

usStructSize := sizeof( ADS\_MGMT\_USER\_INFO );

 

ulRetVal := ACE.AdsMgGetLockOwner( hMgmtHandle,

'\\server\volume\data\employee.dbf',

ulLockedRecord,

@stUserInfo,

@usStructSize,

@usLockType );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

ShowMessage( 'Get Lock Owner Error' );

exit;

end;

 

{\*

\* if usStructSize returned is bigger than what was submitted then the

\* version of the server is newer and is relaying that more data is

\* possible to retrieve. The client just needs the most recent ACE.PAS

\* header.

\*}

if ( sizeof( ADS\_MGMT\_USER\_INFO ) < usStructSize ) then

begin

{ Print warning }

ShowMessage( 'User Information structure on server is larger. ' +

'More possible info available.' );

end;

 

{ Print out the owner of the lock }

ShowMessage( 'User ' + StrPas( stUserInfo.aucUserName ) + ' has record ' +

IntToStr( ulLockedRecord ) + 'locked' );

 

 

{\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgKillUser

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*}

 

ulRetVal := ACE.AdsMgKillUser( hMgmtHandle,

'JohnDoe',

0 );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

ShowMessage( 'Kill User Error' );

exit;

end;

 

 

{\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*

\* AdsMgDisconnect - Close a Management Connection Handle.

\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*}

 

ulRetVal := ACE.AdsMgDisconnect( hMgmtHandle );

 

end;

 

end.