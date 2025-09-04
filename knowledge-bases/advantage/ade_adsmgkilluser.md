AdsMgKillUser




Advantage Database Server 12  

AdsMgKillUser

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsMgKillUser  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsMgKillUser Advantage TDataSet Descendant ade\_Adsmgkilluser Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsMgKillUser  Advantage TDataSet Descendant |  |  |  |  |

Disconnects the specified user from the Advantage Database Server

Syntax

function AdsMgKillUser( hMgmtHandle : ADSHANDLE;

pucUserName : pChar;

usConnNumber : UNSIGNED16 ):UNSIGNED32;

Parameters

|  |  |
| --- | --- |
| hMgmtHandle (I) | Management API connection handle of server which contains user to kill. |
| pucUserName (I) | The user name of the user to kill. The user name of an Advantage client is the client computer name or the client computer name then the client OS user login name separated by a backslash '\'. When connected to the [root dictionary](master_root_dictionary.htm) as [SERVER:Admin](master_database_base_roles.htm), this parameter can be an asterisk (\*) to indicate that all connections be disconnected. |
| usConnNumber (I) | NetWare connection number. Deprecated and ignored. |

Remarks

AdsMgKillUser will disconnect the specified Advantage user from the Advantage Database Server. AdsMgKillUser is a potentially dangerous operation and should be used with extreme caution. AdsMgKillUser will cause the specified user to be abnormally disconnected from the Advantage Database Server. If the user is currently in the midst of an operation, that operation may not be able to run to completion. If the specified user is currently in a transaction, that transaction will be rolled back before the user is disconnected. All records locked by the specified user will be unlocked. All files open by the specified user will be closed. The specified user will then be disconnected. Unpredictable Advantage errors may be received by the Advantage application immediately after it has been "killed".

AdsMgKillUser should NOT be used to disconnect the current application from the Advantage Database Server. AdsDisconnect should be used in this instance.

If more that one Advantage client that is connected to the Advantage Database Server has the specified user name, they will all be disconnected from the Advantage Database Server. That is, if two users named "BRAD" are connected to the Advantage Database Server, then a call to AdsMgKillUser( nHandle, "BRAD", 0 ) will disconnect both BRAD users. To be more specific with the pucUserName parameter, the operating system user login name can be specified along with the regular user name (i.e., client's computer name). For example, if BRAD and SUZY are logged into two different computers with the same name (WORKSTATION), their connections can be killed individually by specifying "WORKSTATION\BRAD" or "WORKSTATION\SUZY" for the pucUserName parameter. Trailing backslash characters on the regular user name are ignored. For example, the backslash character is ignored in "WORKSTATION\" or "BRAD\", but not in "WORKSTATION\BRAD\".

Beginning with v11 of Advantage, additional restrictions have been added. This procedure requires [DB:Admin](master_database_base_roles.htm) membership when connected to a data dictionary, and only other users connected to the same dictionary can be killed. When connected with a free connection, it can be used to remove other free connections. When connected to the [root dictionary](master_root_dictionary.htm) as [SERVER:Admin](master_database_base_roles.htm), it is possible to remove any connection (similar to pre-v11 behavior).

Note In a future release of Advantage, the user name and password passed to the AdsMgConnect API may be checked to verify the application has sufficient management API privileges to access this dangerous management API.

Example

var

hMgmtHandle : ADSHANDLE;

ulRetVal : UNSIGNED32;

begin

ulRetVal := ACE.AdsMgConnect( '\\MyExample\Server', nil, nil, @hMgmtHandle );

 

// If there was an error then show it and exit

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not connect to server.', 'Connection Error', ID\_OK );

exit;

end;

 

ulRetVal := ACE.AdsMgKillUser( hMgmtHandle, 'Fred', 0);

 

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not disconnect Fred from the database.',

'Error', ID\_OK );

exit;

end

else

begin

Application.MessageBox( pchar('Fred is disconnected from the database.'),

'Informtaion',

ID\_OK );

end;

See Also

[AdsMgConnect](ade_adsmgconnect.htm)

[AdsMgDisconnect](ade_adsmgdisconnect.htm)

[AdsMgGetUserNames](ade_adsmggetusernames.htm)

[AdsMgGetOpenTables](ade_adsmggetopentables.htm)

[AdsMgGetOpenIndexes](ade_adsmggetopenindexes.htm)

[AdsMgGetLockOwner](ade_adsmggetlockowner.htm)