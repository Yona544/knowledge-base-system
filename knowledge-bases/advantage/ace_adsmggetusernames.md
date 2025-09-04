AdsMgGetUserNames




Advantage Database Server 12  

AdsMgGetUserNames

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsMgGetUserNames  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsMgGetUserNames Advantage Client Engine ace\_Adsmggetusernames Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsMgGetUserNames  Advantage Client Engine |  |  |  |  |

Returns an array of information about users currently connected to the Advantage Database Server

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsMgGetUserNames ( ADSHANDLE hMgmtConnect,  UNSIGNED8 \*pucFileName,  ADS\_MGMT\_USER\_INFO astUserInfo[],  UNSIGNED16 \*pusArrayLen,  UNSIGNED16 \*pusStructSize ); |

Parameters

|  |  |
| --- | --- |
| hMgmtConnect (I) | Management API connection handle of server to get user information. |
| pucFileName (I) | Either a table name, index name, or NULL. If pucFileName contains a table name or index name, it must include a fully qualified path to that file, i.e. it must contain a drive letter and path or must contain a UNC path that includes the server name and volume/share. |
| astUserInfo (O) | Returned array of user information structures. |
| pusArrayLen (I/O) | Number of array elements in astUserInfo on input. On output, number of astUserInfo array elements filled with user information by the Advantage Database Server. |
| pusStructSize (I/O) | Size (in bytes) of each astUserInfo array element structure on input. On output, size of ADS\_MGMT\_USER\_INFO structure on the Advantage Database Server. |

Remarks

AdsMgGetUserNames returns an array of structures containing information about users who either have the specified table open, who have the specified index open, or who are connected. If pucFileName contains a fully qualified table name, then astUserInfo will contain a list of information about Advantage users that have that table open. If pucFileName contains a fully qualified index name, then astUserInfo will contain a list of information about Advantage users that have that index open. If pucFileName is NULL, then astUserInfo will contain a list of information about all users that are connected to the Advantage Database Server.

The number of elements declared in the astUserInfo array, which is the value to be input in pusArrayLen, needs to be large enough to hold all possible users that have the given table open, the given index open, or who are connected to the Advantage Database Server (depending upon what is input in pucFileName). If more users have the given table open, the given index open, or are connected than is specified in pusArrayLen, then only information about the first pusArrayLen number of users will be returned in astUserInfo. Information about the remaining users will not be returned, and pusArrayLen will be returned with the same value that was input. If fewer users have the given table open, the given index open, or are connected than is specified in pusArrayLen, then not all elements in the astUserInfo array will be filled. The value returned in pusArrayLen will indicate how many elements in the astUserInfo array were filled. The remaining elements at the end of the astUserInfo array will be left unchanged.

It is possible that the size of the ADS\_MGMT\_USER\_INFO structure will increase in future releases of Advantage. Since it is possible to use a newer version of the Advantage Database Server with an older version of the Advantage Client Engine, any new and additional user information that may exist if using a newer version of the Advantage Database Server will not be returned in each element of the astUserInfo array. Each element in the array of astUserInfo structures will only be filled with the amount of data specified in pusStructSize. The value returned in the pusStructSize parameter is the size of the ADS\_MGMT\_USER\_INFO structure in the current version of the Advantage Database Server. If the size of each element in the astUserInfo structure input in pusStructSize is the same as the size returned in pusStructSize, then the Advantage client has received all possible user information.

Since it is possible that the size of the ADS\_MGMT\_USER\_INFO structure will increase in future releases of Advantage, it is highly recommended that on input the pusStructSize parameter is literally initialized with sizeof( ADS\_MGMT\_USER\_INFO ) rather than being initialized with a literal value.

The aucUserName member of ADS\_MGMT\_USER\_INFO is the Advantage clients computer name.

The aucOSUserLoginName member of ADS\_MGMT\_USER\_INFO is the Advantage client's operating system user login name.

If the user has obtained a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)) to an Advantage Data Dictionary, aucAuthUserName member of ADS\_MGMT\_USER\_INFO will contain the authenticated user name for that user. If the user has obtained a [free connection](javascript:hhpopuplink.TextPopup(popid_7577555X,FontFace,-1,-1,-1,-1)), aucAuthUserName will be empty.

The aucAddress member of ADS\_MGMT\_USER\_INFO will contain the IP or IPX address of the client computer that is connected to the Advantage Database Server.

If the connection to the Advantage Database Server originated from a Terminal Server, the aucTSAddress member of ADS\_MGMT\_USER\_INFO will contain the IP address of the Terminal Server client computer. For non-Terminal Services connections, this field will contain the IP address 0.0.0.0.

Note AdsMgGetUserNames will only return information about users who are using the Advantage Database Server. Information about any non-Advantage users that have the specified table or index open, will not be returned.

Note With Advantage Local Server, AdsMgGetUserNames will only return information about users of the instance of Advantage Local Server currently loaded into memory. Information about users from other instances of the Advantage Local Server will not be returned.

Example

[Click Here](ace_advantage_management_api_examples.htm#adsmggetusernames_example)

See Also

[AdsMgConnect](ace_adsmgconnect.htm)

[AdsMgGetOpenTables](ace_adsmggetopentables.htm)

[AdsMgGetOpenIndexes](ace_adsmggetopenindexes.htm)

[ADS\_MGMT\_USER\_INFO](ace_ads_mgmt_user_info.htm)