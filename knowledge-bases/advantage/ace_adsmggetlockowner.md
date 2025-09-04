AdsMgGetLockOwner




Advantage Database Server 12  

AdsMgGetLockOwner

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsMgGetLockOwner  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsMgGetLockOwner Advantage Client Engine ace\_Adsmggetlockowner Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsMgGetLockOwner  Advantage Client Engine |  |  |  |  |

Returns the user that has the given record locked in the given table on the Advantage Database Server

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsMgGetLockOwner (ADSHANDLE hMgmtConnect,  UNSIGNED8 \*pucTableName,  UNSIGNED32 ulRecordNumber,  ADS\_MGMT\_USER\_INFO \*pstUserInfo,  UNSIGNED16 \*pusStructSize,  UNSIGNED16 \*pusLockType); |

Parameters

|  |  |
| --- | --- |
| hMgmtConnect (I) | Management API connection handle of server to get lock owner information. |
| pucTableName (I) | Table name that must include a fully qualified path to that table, i.e. it must contain a drive letter and path or must contain a UNC path that includes the server name and volume/share. |
| ulRecordNumber (I) | Record number that is locked or zero. If zero, then will only check for a table lock on the given table. |
| pstUserInfo (O) | Returned user information structure. |
| pusStructSize (I/O) | Size (in bytes) of pstUserInfo structure on input. On output, size of ADS\_MGMT\_USER\_INFO structure on the Advantage Database Server. |
| pusLockType (O) | Returned value indicates if the specified record was locked, the specified table was locked, or if no lock exists on the given record or table. |

Remarks

AdsMgGetLockOwner returns a structure containing the user who has the specified table locked or who has the specified record in the specified table locked. If the table is locked, pusLockType will contain ADS\_MGMT\_FILE\_LOCK. If the record is locked, pusLockType will contain ADS\_MGMT\_RECORD\_LOCK. If the table is not locked or the record in the specified table is not locked, pstUserInfo will be empty and pusLockType will contain the value ADS\_MGMT\_NO\_LOCK.

If ulRecordNumber is passed with the value zero, then only the existence for a table lock on the specified table will be checked.

It is possible that the size of the ADS\_MGMT\_USER\_INFO structure will increase in future releases of Advantage. Since it is possible to use a newer version of the Advantage Database Server with an older version of the Advantage Client Engine, any new and additional user information that may exist if using a newer version of the Advantage Database Server will not be returned in pstUserInfo. The pstUserInfo structure will only be filled with the amount of data specified in pusStructSize. The value returned in the pusStructSize parameter is the size of the ADS\_MGMT\_USER\_INFO structure in the current version of the Advantage Database Server. If the size of the pstUserInfo structure input in pusStructSize is the same as the size returned in pusStructSize, then the Advantage client has received all possible user information.

Since it is possible that the size of the ADS\_MGMT\_USER\_INFO structure will increase in future releases of Advantage, it is highly recommended that on input the pusStructSize parameter is literally initialized with sizeof( ADS\_MGMT\_USER\_INFO ) rather than being initialized with a literal value.

The aucUserName member of ADS\_MGMT\_USER\_INFO is the Advantage clients computer name and the aucOSUserLoginName member of ADS\_MGMT\_USER\_INFO is the Advantage client's operating system user login name.

If the connection to the Advantage Database Server originated from a Terminal Server, the aucTSAddress member of ADS\_MGMT\_USER\_INFO will contain the IP address of the Terminal Server client computer. For non-Terminal Services connections, this field will contain the IP address 0.0.0.0.

Note With the Advantage Local Server, AdsMgGetLockOwner will only return information, if the lock was instantiated by the instance of Advantage Local Server currently loaded into memory. It is not possible to determine the owner of a lock instantiated from other instances of the Advantage Local Server.

Example

[Click Here](ace_advantage_management_api_examples.htm#adsmggetlockowner_example)

See Also

[AdsMgConnect](ace_adsmgconnect.htm)

[AdsMgDisconnect](ace_adsmgdisconnect.htm)

[ADS\_MGMT\_USER\_INFO](ace_ads_mgmt_user_info.htm)