---
title: Ade Adsmggetopentables
slug: ade_adsmggetopentables
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsmggetopentables.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: e9ebd7dd92dd504a802382450985733b622b3d42
---

# Ade Adsmggetopentables

AdsMgGetOpenTables

AdsMgGetOpenTables

Advantage TDataSet Descendant

| AdsMgGetOpenTables  Advantage TDataSet Descendant |  |  |  |  |

Returns an array of information about tables that are currently opened on the Advantage Database Server

Syntax

function AdsMgGetOpenTables( hMgmtHandle : ADSHANDLE;

pucUserName : pChar;

usConnNumber : UNSIGNED16;

astOpenTableInfo : PADSMgTableArray;

pusArrayLen : pWord;

pusStructSize : pWord ):UNSIGNED32;

Parameters

| hMgmtHandle (I) | Management API connection handle of server to get table information. |
| pucUserName (I) | Either a user name or NULL. The user name of an Advantage client is the client computer name or the client computer name then the client OS user login name separated by a backslash '\'. |
| usConnNumber (I) | NetWare connection number. Deprecated and ignored. |
| astOpenTableInfo (O) | Returned array of table information structures. |
| pusArrayLen (I/O) | Number of array elements in astOpenTableInfo on input. On output, number of astOpenTableInfo array elements filled with table information by the Advantage Database Server. |
| pusStructSize (I/O) | Size (in bytes) of each astOpenTableInfo array element structure on input. On output, size (in bytes) of data returned. |

Remarks

AdsMgGetOpenTables returns an array of structures containing information about tables the specified user has open or all tables that are open (depending upon the pucUserName or usConnNumber parameters). If pucUserName contains an Advantage client's user name or if usConnNumber is non-zero, then astOpenTableInfo will contain a list of information about tables opened by that Advantage user. If pucUserName is NULL and usConnNumber is zero, then astOpenTableInfo will contain a list of information about all tables that are opened on the Advantage Database Server. If both pucUserName contains a user name and usConnNumber is non-zero, then usConnNumber will be ignored.

The number of elements in astOpenTableInfo, which is the value to be input in pusArrayLen, needs to be large enough to hold all possible tables that the given user has open or that are opened by the Advantage Database Server (depending upon what is input in pucUserName or usConnNumber). If more tables are open than is specified in pusArrayLen, then only information about the first pusArrayLen number of tables will be returned in astOpenTableInfo. Information about the remaining tables will not be returned, and pusArrayLen will be returned with the same value that was input. If fewer tables are open than is specified in pusArrayLen, then not all elements in the astOpenTableInfo array will be filled. The value returned in pusArrayLen will indicate how many elements in the astOpenTableInfo array were filled. The remaining, unfilled elements at the end of the astOpenTableInfo array will be left unchanged.

It is possible that the size of the ADS\_MGMT\_TABLE\_INFO structure will increase in future releases of Advantage. Since it is possible to use a newer version of the Advantage Database Server with an older version of the Advantage Client Engine, any new and additional table information that may exist if using a newer version of the Advantage Database Server will not be returned in each element of the astOpenTableInfo array. Each element in the array of astOpenTableInfo structures will only be filled with the amount of data specified in pusStructSize. The value returned in the pusStructSize parameter is the size of the ADS\_MGMT\_TABLE\_INFO structure in the current version of the Advantage Database Server. If the size of each element in the astOpenTableInfo structure input in pusStructSize is the same as the size returned in pusStructSize, then the Advantage client has received all possible table information.

Since it is possible that the size of the ADS\_MGMT\_TABLE\_INFO structure will increase in future releases of Advantage, it is highly recommended that on input the pusStructSize parameter is literally initialized with sizeof( ADS\_MGMT\_TABLE\_INFO ) rather than being initialized with a literal value.

The aucTableName member in ADS\_MGMT\_TABLE\_INFO includes a fully qualified path. If running against the Advantage Database Server for Windows, aucTableName will contain the Windows drive letter, the full path, and the table name. For the Advantage Database Server for Linux, aucTableName will contain the full path and the table name.

The usLockType member in ADS\_MGMT\_TABLE\_INFO is the Advantage locking mode in which the table is opened. If the table is using Advantage's proprietary locking mode, ADS\_MGMT\_PROPRIETARY\_LOCKING will be returned. If the table is using Advantage's compatible locking mode, and the table was opened with the CDX index type, then ADS\_MGMT\_CDX\_LOCKING will be returned. A table opened with the NTX index type will result in ADS\_MGMT\_NTX\_LOCKING being returned. An Advantage ADT table with the ADI index type will result in ADS\_MGMT\_ADI\_LOCKING being returned.

Note AdsMgGetOpenTables will only return information about tables open on the Advantage Database Server. Information about any tables opened by non-Advantage users will not be returned.

Example

var

hMgmtHandle : ADSHANDLE;

ulRetVal : UNSIGNED32;

astOpenTableInfo : ADSMgTableArray;

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

 

usArrayLen := ADS\_TABLE\_ARRAY\_SIZE - 1;

usSize := sizeof( ADS\_MGMT\_TABLE\_INFO );

ulRetVal := ACE.AdsMgGetOpenTables( hMgmtHandle,

'Fred',

0,

@astOpenTableInfo,

@usArrayLen,

@usSize );

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not determine how many tables Fred has opened.',

'Error', ID\_OK );

exit;

end

else

begin

Application.MessageBox( pchar('The number of tables opened by Fred is: '

+ pchar( IntToStr (usArrayLen ))),

'Informtaion',

ID\_OK );

end;

See Also

[AdsMgConnect](ade_adsmgconnect.md)

[AdsMgGetUserNames](ade_adsmggetusernames.md)

[AdsMgGetOpenIndexes](ade_adsmggetopenindexes.md)

[ADS\_MGMT\_TABLE\_INFO](ade_ads_mgmt_table_info.md)
