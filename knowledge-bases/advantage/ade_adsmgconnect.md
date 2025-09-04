AdsMgConnect




Advantage Database Server 12  

AdsMgConnect

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsMgConnect  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsMgConnect Advantage TDataSet Descendant ade\_Adsmgconnect Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsMgConnect  Advantage TDataSet Descendant |  |  |  |  |

Obtains a management API connection to the given server.

Syntax

function AdsMgConnect( pucServerName : PChar;

pucUserName : PChar;

pucPassword : PChar;

phMgmtHandle : pADSHANDLE ): UNSIGNED32;

Parameters

|  |  |
| --- | --- |
| pucServerName (I) | Server name (or drive letter) to which to obtain a management API connection. If the application uses a server name as the parameter, it must include the share name. For example, use "\\server\share". |
| pucUserName (I) | This parameter is currently ignored. In a future release, pucUserName may be the user name for management API security. Can be NULL if you do not need to make a future call to a management API that requires special security privileges. |
| pucPassword (I) | This parameter is currently ignored. In a future release, pucPassword may be the password for management API security. Can be NULL if you do not need to make a future call to a management API that requires special security privileges or if there is not a password associated with the specified user name. |
| phMgmtHandle (O) | Returned management API connection handle, if successful. |

Remarks

AdsMgConnect currently is stubbed to call AdsConnect. Thus, you must be connected to the Advantage Database Server(s) from which you are retrieving management information. It is recommended you use AdsMgConnect to obtain the connection handle to be used in all subsequent management API calls. A future release of the Advantage Client Engine may not support using a standard connection handle in place of a management API connection handle.

In a future release, AdsMgConnect may obtain a management API connection to the Advantage Database Server on the given server. This management API connection will consume neither a "user" nor a "connection" on the Advantage Database Server. Thus an application that uses no Advantage Client Engine APIs other than management APIs, can be running on a client computer and it will not take up one user towards the user option purchased for that Advantage Database Server.

Currently, the pucUserName and pucPassword parameters are ignored. In a future release, the specified user name and password may be checked to verify the user has sufficient management API privileges to access some potentially dangerous management APIs, such as AdsMgKillUser.

The server name specified can be a drive letter or any valid network path (standard name resolution will be performed). A management API connection handle will be returned, if it succeeds. The management connection handle can be used in subsequent calls to all management APIs such as AdsMgGetActivityInfo and AdsMgGetOpenUsers.

Example

var

hMgmtHandle : ADSHANDLE;

ulRetVal : UNSIGNED32;

begin

ulRetVal := ACE.AdsMgConnect( '\\MyExample\Server', nil, nil, @hMgmtHandle );

 

// If there was an error then show it and exit

if ( ulRetVal <> AE\_SUCCESS ) then

begin

Application.MessageBox( 'Could not connect to Server', 'Connection Error', ID\_OK );

end;

See Also

[AdsMgDisconnect](ade_adsmgdisconnect.htm)