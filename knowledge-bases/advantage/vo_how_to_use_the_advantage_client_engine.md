How to use the Advantage Client Engine




Advantage Database Server 12  

How to use the Advantage Client Engine

Advantage Visual Objects and Vulcan.NET RDD

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| How to use the Advantage Client Engine  Advantage Visual Objects and Vulcan.NET RDD |  |  | Feedback on: Advantage Database Server 12 - How to use the Advantage Client Engine Advantage Visual Objects and Vulcan.NET RDD vo\_How\_to\_use\_the\_advantage\_client\_engine Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Directly Accessing the Advantage Client Engine > How to use the Advantage Client Engine / Dear Support Staff, |  |
| How to use the Advantage Client Engine  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

The Advantage Client Engine uses handles to identify every connection, table, and index. The Advantage Visual Objects and Vulcan.NET RDDs wrap the handle values. Therefore, you do not need to access the handles unless you plan to call the Advantage Client Engine directly. To retrieve the handle for a specific object, use the Advantage functions [AX\_GetAceTableHandle](vo_ax_getacetablehandle.htm) or [AX\_GetAceIndexHandle](vo_ax_getaceindexhandle.htm). These methods return table or index handles associated with the currently selected work area. Once these handles are obtained, they can be used to call Advantage Client Engine APIs directly.

All available Advantage Client Engine APIs are documented in the Advantage Help documentation.

The prototype syntax in this Help file is in 'C'. To see the prototype syntax in VO, find the function prototype in the Functions module of ACE.AEF, which is installed with the Advantage Visual Objects RDDs.

To use Advantage Client Engine APIs directly in your code, include the ACE library (from ACE.AEF) in your application.

The source code for the Advantage AX\_\* functions is provided in the DBFAXS.AEF library. This source code is an excellent example of how to use the Advantage Client Engine API.

Note It is possible to change the state of the Advantage Client Engine by calling the Advantage Client Engine APIs directly. The Advantage RDDs may make certain assumptions about the state of the Advantage Client Engine that can cause problems. Use caution when modifying the state of the Advantage Client Engine directly through its APIs.

Below is an example VO application that uses ACE directly.

FUNCTION APIExample()

LOCAL dwError AS DWORD

LOCAL dwRetCode AS DWORD

LOCAL pacError AS PSZ

LOCAL wErrLen AS WORD

LOCAL oDB AS DBServer

LOCAL hMgConnect AS DWORD

LOCAL stInstallInfo AS ADS\_MGMT\_INSTALL\_INFO

LOCAL wInstallStSize AS WORD

 

pacError := MemAlloc( 512 )

wErrLen := 512

 

oDB := DBServer{ "c:\test\test.dbf", , , "AXDBFCDX" }

 

// Use AdsGetLastError to check for any errors during the table open

dwRetCode := AdsGetLastError( @dwError, pacError, @wErrLen )

IF ( dwRetCode != AE\_SUCCESS )

ErrorBox{ , "Failed to get last error" }:Show()

ELSEIF ( dwError != AE\_SUCCESS )

ErrorBox{ , "Advantage error = " + Psz2String( pacError )}:Show()

ELSE

// Select oDB as the currect work area (necessary for AX\_GetAceTableHandle)

SELECT( oDB:Alias )

 

// Adjust record caching to minimize network traffic (usually set to a browser window size, default is 10)

dwRetCode := AdsCacheRecords( AX\_GetAceTableHandle(), 50 )

IF ( dwRetCode != AE\_SUCCESS )

ErrorBox{ , "AdsCacheRecords failed WITH error: " + Str( dwRetCode )}:Show()

ENDIF

 

oDB:Close()

ENDIF

 

// Use the AdsMg\* APIs to obtain management information about the ADS server

wInstallStSize := \_SizeOf( ADS\_MGMT\_INSTALL\_INFO )

stInstallInfo := MemAlloc( \_SizeOf( ADS\_MGMT\_INSTALL\_INFO ))

 

dwRetCode := AdsMgConnect( String2Psz( "x:\" ), NULL\_PSZ, NULL\_PSZ, @hMgConnect )

IF dwRetCode != AE\_SUCCESS

ErrorBox{ , "AdsMgConnect returned error: " + Str( dwRetCode )}:Show()

ELSE

dwRetCode := AdsMgGetInstallInfo( hMgConnect, stInstallInfo, @wInstallStSize )

IF dwRetCode != AE\_SUCCESS

ErrorBox{ , "AdsMgGetInstallInfo returned error: " + Str( dwRetCode )}:Show()

ENDIF

 

dwRetCode := AdsDisconnect( hMgConnect )

ENDIF

 

? "ADS Version: "

?? Psz2String( @stInstallInfo.aucVersionStr )

WAIT

 

// Use AdsDisconnect( 0 ) to clear any dangling connections

AdsDisconnect( 0 )

 

// Free any allocated memory

MemFree( pacError )

MemFree( stInstallInfo )