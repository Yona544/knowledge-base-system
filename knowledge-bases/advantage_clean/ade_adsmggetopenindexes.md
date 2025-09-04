---
title: Ade Adsmggetopenindexes
slug: ade_adsmggetopenindexes
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsmggetopenindexes.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: fe685d08e50c92291ba72fc56d21222c50bce92a
---

# Ade Adsmggetopenindexes

AdsMgGetOpenIndexes

AdsMgGetOpenIndexes

Advantage TDataSet Descendant

| AdsMgGetOpenIndexes  Advantage TDataSet Descendant |  |  |  |  |

Returns an array of information about indexes that are currently opened on the Advantage Database Server

Syntax

function AdsMgGetOpenIndexes( hMgmtHandle : ADSHANDLE;

pucTableName : pChar;

pucUserName : pChar;

usConnNumber : UNSIGNED16;

astOpenIndexInfo : PADSMgIndexArray;

pusArrayLen : pWord;

pusStructSize : pWord ):UNSIGNED32;

Parameters

| hMgmtHandle (I) | Management API connection handle of server to get index information. |
| pucTableName (I) | Either a table name or NULL. If pucTableName contains a table name, it must include a fully qualified path to that table, i.e. it must contain a drive letter and path or must contain a UNC path that includes the server name and volume/share. |
| pucUserName (I) | Either a user name or NULL. The user name of an Advantage client is the client computer name or the client computer name then the client OS user login name separated by a backslash '\'. |
| usConnNumber (I) | NetWare connection number. Deprecated and ignored. |
| astOpenIndexInfo (O) | Returned array of index information structures. |
| pusArrayLen (I/O) | Number of array elements in astOpenIndexInfo on input. On output, number of astOpenIndexInfo array elements filled with index information by the Advantage Database Server. |
| pusStructSize (I/O) | Size (in bytes) of each astOpenIndexInfo array element structure on input. On output, size of ADS\_MGMT\_INDEX\_INFO structure on the Advantage Database Server. |

Remarks

AdsMgGetOpenIndexes returns an array of structures containing information about indexes that: 1) the specified user has open for the specified table, 2) the specified user has open for all tables, 3) that are open for the specified table by any user, or 4) that are open by any user for any table. If pucUserName contains an Advantage client's user name or if usConnNumber is non-zero, and if pucTableName contains a table name, then astOpenIndexInfo will contain a list of information about indexes opened by that Advantage user for that table. If pucUserName contains an Advantage client's user name or if usConnNumber is non-zero, and if pucTableName is NULL, then astOpenIndexInfo will contain a list of information about all indexes opened by that Advantage user. If pucUserName is NULL and usConnNumber is zero, and if pucTableName contains a table name, then astOpenIndexInfo will contain a list of information about indexes opened for that table by any Advantage users. If pucUserName is NULL, usConnNumber is zero, and pucTableName is NULL, then astOpenIndexInfo will contain a list of information about all indexes that are opened on the Advantage Database Server. If both pucUserName contains a user name and usConnNumber is non-zero, then usConnNumber will be ignored.

The number of elements declared in the astOpenIndexInfo array, which is the value to be input in pusArrayLen, needs to be large enough to hold all possible indexes that are open for the given user and/or table or for all indexes open. If more indexes are open than is specified in pusArrayLen, then only information about the first pusArrayLen number of indexes will be returned in astOpenIndexInfo. Information about the remaining indexes will not be returned, and pusArrayLen will be returned with the same value that was input. If fewer indexes are open than is specified in pusArrayLen, then not all elements in the astOpenIndexInfo array will be filled. The value returned in pusArrayLen will indicate how many elements in the astOpenIndexInfo array were filled. The remaining, unfilled elements at the end of the astOpenIndexInfo array will be left unchanged.

It is possible that the size of the ADS\_MGMT\_INDEX\_INFO structure will increase in future releases of Advantage. Since it is possible to use a newer version of the Advantage Database Server with an older version of the Advantage Client Engine, any new and additional index information that may exist if using a newer version of the Advantage Database Server will not be returned in each element of the astOpenIndexInfo array. Each element in the array of astOpenIndexInfo structures will only be filled with the amount of data specified in pusStructSize. The value returned in the pusStructSize parameter is the size of the ADS\_MGMT\_INDEX\_INFO structure in the current version of the Advantage Database Server. If the size of each element in the astOpenIndexInfo structure input in pusStructSize is the same as the size returned in pusStructSize, then the Advantage client has received all possible index information.

Since it is possible that the size of the ADS\_MGMT\_INDEX\_INFO structure will increase in future releases of Advantage, it is highly recommended that on input the pusStructSize parameter is literally initialized with size of ( ADS\_MGMT\_INDEX\_INFO ) rather than being initialized with a literal value.

The aucIndexName member in ADS\_MGMT\_INDEX\_INFO includes a fully qualified path. If running against the Advantage Database Server for Windows, aucIndexName will contain the NT drive letter, the full path, and the index name. For the Advantage Database Server for Linux, aucIndexName will contain the full path and the index name.

Note AdsMgGetOpenIndexes will only return information about indexes open on the Advantage Database Server. Information about any indexes opened by non-Advantage users will not be returned.

Example

var

hMgmtHandle : ADSHANDLE;

ulRetVal : UNSIGNED32;

astOpenIndexInfo : ADSMgIndexArray;

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

 

usArrayLen := ADS\_INDEX\_ARRAY\_SIZE - 1;

usSize := sizeof( ADS\_MGMT\_INDEX\_INFO );

ulRetVal := ACE.AdsMgGetOpenIndexes( hMgmtHandle,

pchar(AdsTable1.TableName),

'Fred',

0,

@astOpenIndexInfo,

@usArrayLen,

@usSize );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not determine how many indexes Fred has opened.',

'Error', ID\_OK );

exit;

end

else

begin

Application.MessageBox( pchar('The number of indexes open by Fred is: '

+ pchar( IntToStr (usArrayLen ))),

'Informtaion',

ID\_OK );

end;

See Also

[AdsMgConnect](ade_adsmgconnect.md)

[AdsMgGetUserNames](ade_adsmggetusernames.md)

[AdsMgGetOpenTables](ade_adsmggetopentables.md)

[ADS\_MGMT\_INDEX\_INFO](ade_ads_mgmt_index_info.md)
