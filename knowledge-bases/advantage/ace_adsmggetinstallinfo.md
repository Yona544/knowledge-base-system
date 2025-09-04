AdsMgGetInstallInfo




Advantage Database Server 12  

AdsMgGetInstallInfo

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsMgGetInstallInfo  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsMgGetInstallInfo Advantage Client Engine ace\_Adsmggetinstallinfo Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsMgGetInstallInfo  Advantage Client Engine |  |  |  |  |

Returns Advantage Database Server installation information

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsMgGetInstallInfo ( ADSHANDLE hMgmtConnect,  ADS\_MGMT\_INSTALL\_INFO \*pstInstallInfo,  UNSIGNED16 \*pusStructSize ); |

Parameters

|  |  |
| --- | --- |
| hMgmtConnect (I) | Management API connection handle of server to get installation information. |
| pstInstallInfo (O) | Returned installation information structure. |
| pusStructSize (I/O) | Size (in bytes) of pstInstallInfo structure on input. On output, size of ADS\_MGMT\_INSTALL\_INFO structure on the Advantage Database Server. |

Remarks

AdsMgGetInstallInfo returns a structure containing Advantage Database Server installation information such as the Advantage Database Server version and the installation date.

It is possible that the size of the ADS\_MGMT\_INSTALL\_INFO structure will increase in future releases of Advantage. Since it is possible to use a newer version of the Advantage Database Server with an older version of the Advantage Client Engine, any new and additional installation data that may exist if using a newer version of the Advantage Database Server will not be returned in pstInstallInfo. The pstInstallInfo structure will only be filled with the amount of data specified in pusStructSize. The value returned in the pusStructSize parameter is the size of the ADS\_MGMT\_INSTALL\_INFO structure in the current version of the Advantage Database Server. If the size of the pstInstallInfo structure input in pusStructSize is the same as the size returned in pusStructSize, then the Advantage client has received all possible installation information.

Since it is possible that the size of the ADS\_MGMT\_INSTALL\_INFO structure will increase in future releases of Advantage, it is highly recommended that on input the pusStructSize parameter is literally initialized with sizeof( ADS\_MGMT\_INSTALL\_INFO ) rather than being initialized with a literal value.

Example

[Click Here](ace_advantage_management_api_examples.htm#adsmggetinstallinfor_example)

See Also

[AdsMgConnect](ace_adsmgconnect.htm)

[ADS\_MGMT\_INSTALL\_INFO](ace_ads_mgmt_install_info.htm)