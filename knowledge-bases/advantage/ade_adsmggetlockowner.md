AdsMgGetLockOwner




Advantage Database Server 12  

AdsMgGetLockOwner

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsMgGetLockOwner  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsMgGetLockOwner Advantage TDataSet Descendant ade\_Adsmggetlockowner Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsMgGetLockOwner  Advantage TDataSet Descendant |  |  |  |  |

Returns the user that has the given record locked in the given table on the Advantage Database Server

Syntax

function AdsMgGetLockOwner( hMgmtHandle : ADSHANDLE;

pucTableName : pChar;

ulRecordNumber: UNSIGNED32;

pstUserInfo : pADS\_MGMT\_USER\_INFO;

pusStructSize : pWord;

pusLockType : pWord ):UNSIGNED32;

Parameters

|  |  |
| --- | --- |
| hMgmtHandle (I) | Management API connection handle of server to get lock owner information. |
| pucTableName (I) | Table name that must include a fully qualified path to that table, i.e. it must contain a drive letter and path or must contain a UNC path that includes the server name and volume/share. |
| ulRecordNumber (I) | Record number that is locked or zero. If zero, then will only check for a table lock on the given table. |
| pstUserInfo (O) | Returned user information structure. |
| pusStructSize (I/O) | Size (in bytes) of pstUserInfo structure on input. On output, size of ADS\_MGMT\_USER\_INFO structure on the Advantage Database Server. |
| pusLockType (O) | Returned value indicates if the specified record was locked, the specified table was locked, or if no lock exists on the given record or table. |

Remarks

AdsMgGetLockOwner returns a structure containing the user who has the specified table locked or has the specified record in the specified table locked. If the table is locked, pusLockType will contain ADS\_MGMT\_FILE\_LOCK. If the record is locked, pusLockType will contain ADS\_MGMT\_RECORD\_LOCK. If the table is not locked or the record in the specified table is not locked, pstUserInfo will be empty and pusLockType will contain the value ADS\_MGMT\_NO\_LOCK.

If ulRecordNumber is passed with the value zero, then only the existence for a table lock on the specified table will be checked.

It is possible that the size of the ADS\_MGMT\_USER\_INFO structure will increase in future releases of Advantage. Since it is possible to use a newer version of the Advantage Database Server with an older version of the Advantage Client Engine, any new and additional user information that may exist if using a newer version of the Advantage Database Server will not be returned in pstUserInfo. The pstUserInfo structure will only be filled with the amount of data specified in pusStructSize. The value returned in the pusStructSize parameter is the size of the ADS\_MGMT\_USER\_INFO structure in the current version of the Advantage Database Server. If the size of the pstUserInfo structure input in pusStructSize is the same as the size returned in pusStructSize, then the Advantage client has received all possible user information.

Since it is possible that the size of the ADS\_MGMT\_USER\_INFO structure will increase in future releases of Advantage, it is highly recommended that on input the pusStructSize parameter is literally initialized with sizeof( ADS\_MGMT\_USER\_INFO ) rather than being initialized with a literal value.

The aucUserName member of ADS\_MGMT\_USER\_INFO is the Advantage client's computer name and the aucOSUserLoginName member of ADS\_MGMT\_USER\_INFO is the Advantage client's operating system user login name.

Example

var

hMgmtHandle : ADSHANDLE;

ulRetVal : UNSIGNED32;

stUserInfo : ADS\_MGMT\_USER\_INFO;

usSize : UNSIGNED16;

usLockType : UNSIGNED16;

begin

if AdsTable1.AdsIsRecordLocked( AdsTable1.Recno ) then

begin

ulRetVal := ACE.AdsMgConnect( '\\MyExample\Server', nil, nil, @hMgmtHandle );

 

// If there was an error then show it and exit

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not connect to server.', 'Connection Error', ID\_OK );

exit;

end;

 

usSize := sizeof( ADS\_MGMT\_USER\_INFO );

ulRetVal := ACE.AdsMgGetLockOwner( hMgmtHandle,

pchar(AdsTable1.TableName),

AdsTable1.RecNo,

@stUserInfo,

@usSize,

@usLockType);

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not determine who has the record locked.',

'Error', ID\_OK );

exit;

end

else

begin

Application.MessageBox( pchar('The recorded is locked by: '

+ stUserInfo.aucUserName ),

'Informtaion',

ID\_OK );

end;

See Also

[AdsMgConnect](ade_adsmgconnect.htm)

[AdsMgDisconnect](ade_adsmgdisconnect.htm)

[ADS\_MGMT\_USER\_INFO](ade_ads_mgmt_user_info.htm)