---
title: Ade Adsmggetlocks
slug: ade_adsmggetlocks
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsmggetlocks.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: aa08fa0752d94873f31b436f7c9b7335ebacf770
---

# Ade Adsmggetlocks

AdsMgGetLocks

AdsMgGetLocks

Advantage TDataSet Descendant

| AdsMgGetLocks  Advantage TDataSet Descendant |  |  |  |  |

Returns an array of information about records that are currently locked on the Advantage Database Server

Syntax

function AdsMgGetLocks( hMgmtHandle : ADSHANDLE;

pucTableName : pChar;

pucUserName : pChar;

usConnNumber : UNSIGNED16;

astRecordInfo : PADSMgLocksArray;

pusArrayLen : pWord;

pusStructSize : pWord ):UNSIGNED32;

Parameters

| hMgmtHandle (I) | Management API connection handle of server to get lock information. |
| pucTableName (I) | Table name that must include a fully qualified path to that table, i.e. it must contain a drive letter and path or must contain a UNC path that includes the server name and volume/share. |
| pucUserName (I) | Either a user name or NULL. The user name of an Advantage client is the client computer name or the client computer name then the client OS user login name separated by a backslash '\'. |
| usConnNumber (I) | NetWare connection number. Deprecated and ignored. |
| astRecordInfo (O) | Returned array of record lock information structures. |
| pusArrayLen (I/O) | Number of array elements in astRecordInfo on input. On output, number of astRecordInfo array elements filled with record lock information by the Advantage Database Server. |
| pusStructSize (I/O) | Size (in bytes) of each astRecordInfo array element structure on input. On output, size (in bytes) of data returned. |

Remarks

AdsMgGetLocks returns an array of structures containing information about records in the given table that the specified user has locked or that are locked by any user. If pucUserName contains an Advantage client's user name or if usConnNumber is non-zero, then astRecordInfo will contain a list of information about records that are locked in the given table by the specified user. If pucUserName is NULL and usConnNumber is zero, then astRecordInfo will contain a list of information about all records that are locked in the given table by any user. If both pucUserName contains a user name and usConnNumber is non-zero, then usConnNumber will be ignored.

The number of elements in astRecordInfo, which is the value to be input in pusArrayLen, needs to be large enough to hold all possible records in the given table that are locked for the given user or for all users. If more records are locked than is specified in pusArrayLen, then only information about the first pusArrayLen number of locked records will be returned in astRecordInfo. Information about the remaining record locks will not be returned, and pusArrayLen will be returned with the same value that was input. If fewer records are locked than is specified in pusArrayLen, then not all elements in the astRecordInfo array will be filled. The value returned in pusArrayLen will indicate how many elements in the astRecordInfo array were filled. The remaining, unfilled elements at the end of the astRecordInfo array will be left unchanged.

It is possible that the size of the ADS\_MGMT\_RECORD\_INFO structure will increase in future releases of Advantage. Since it is possible to use a newer version of the Advantage Database Server with an older version of the Advantage Client Engine, any new and additional record information that may exist if using a newer version of the Advantage Database Server will not be returned in each element of the astRecordInfo array. Each element in the array of astRecordInfo structures will only be filled with the amount of data specified in pusStructSize. The value returned in the pusStructSize parameter is the size of the ADS\_MGMT\_RECORD\_INFO structure in the current version of the Advantage Database Server. If the size of each element in the astRecordInfo structure input in pusStructSize is the same as the size returned in pusStructSize, then the Advantage client has received all possible record information.

Since it is possible that the size of the ADS\_MGMT\_RECORD\_INFO structure will increase in future releases of Advantage, it is highly recommended that on input the pusStructSize parameter is literally initialized with sizeof( ADS\_MGMT\_RECORD\_INFO ) rather than being initialized with a literal value.

If the specified table name is locked, then only the first element in astRecordInfo will be filled. The record number in that lone astRecordInfo element will be 0. pusArrayLen will be returned with the value one.

Note AdsMgGetLocks will only return information about records locked on the Advantage Database Server. Information about any records locked by non-Advantage users will not be returned.

Example

var

hMgmtHandle : ADSHANDLE;

ulRetVal : UNSIGNED32;

astRecordInfo : ADSMgLocksArray;

usSize : UNSIGNED16;

usArrayLen : UNSIGNED16;

begin

ulRetVal := ACE.AdsMgConnect( '\\MyExample\Server', nil, nil, @hMgmtHandle );

 

// If there was an error then show it and exit

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not connect to server.', 'Connection Error', ID\_OK );

exit;

end;

 

usArrayLen := ADS\_LOCK\_ARRAY\_SIZE - 1;

usSize := sizeof( ADS\_MGMT\_RECORD\_INFO );

ulRetVal := ACE.AdsMgGetLocks( hMgmtHandle,

pchar(AdsTable1.TableName),

'Fred',

0,

@astRecordInfo,

@usArrayLen,

@usSize );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not determine how many records Fred has locked.',

'Error', ID\_OK );

exit;

end

else

begin

Application.MessageBox( pchar('The number of records locked by Fred is: '

+ pchar( IntToStr (usArrayLen ))),

'Informtaion',

ID\_OK );

end;

See Also

[AdsMgConnect](ade_adsmgconnect.md)

[AdsMgGetUserNames](ade_adsmggetusernames.md)

[AdsMgGetOpenTables](ade_adsmggetopentables.md)

[ADS\_MGMT\_RECORD\_INFO](ade_ads_mgmt_record_info.md)
