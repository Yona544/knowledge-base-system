Connecting to an Advantage Data Dictionary with CA-Visual Objects




Advantage Database Server 12  

Connecting to an Advantage Data Dictionary with Visual Objects and Vulcan.NET

Advantage Visual Objects and Vulcan.NET RDD

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Connecting to an Advantage Data Dictionary with Visual Objects and Vulcan.NET  Advantage Visual Objects and Vulcan.NET RDD |  |  | Feedback on: Advantage Database Server 12 - Connecting to an Advantage Data Dictionary with Visual Objects and Vulcan.NET Advantage Visual Objects and Vulcan.NET RDD vo\_Connecting\_to\_an\_advantage\_data\_dictionary\_with\_ca\_visual\_objects Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Connecting to an Advantage Data Dictionary with Visual Objects and Vulcan.NET / Dear Support Staff, |  |
| Connecting to an Advantage Data Dictionary with Visual Objects and Vulcan.NET  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

With Advantage versions 6.0 and higher, establishing a connection to an Advantage Data Dictionary can be made by first calling the Advantage Client Engine API AdsConnect60() and then setting this connection as the work area connection using [AX\_SetConnectionHandle()](vo_ax_setconnectionhandle.htm). Once this is completed successfully, a DBServer object can be used to access individual tables and indexes within the data dictionary.

Note The ACE.AEF and DBFAXS.AEF libraries must be included in the project.

VO Example

LOCAL oDB AS DBServer

LOCAL dwError AS DWORD

LOCAL pacError AS PSZ

LOCAL wLen AS WORD

LOCAL lReturn AS LONGINT

LOCAL hConnect AS LONGINT

 

pacError := MemAlloc( 200 )

wLen := 200

dwError := AE\_SUCCESS

 

HandleErrors( AdsConnect60( String2Psz( "X:\DATA\TEST.ADD" ), ADS\_REMOTE\_SERVER, ;

String2Psz( "UserName" ), String2Psz( "Password" ), ADS\_INC\_USERCOUNT, @hConnect ))

 

/\* Set the connection handle \*/

AX\_SetConnectionHandle( hConnect )

 

/\*

\* Since a database path is specified in the connection, it does not need

\* to be specied here. No extension to the table name is needed unless the

\* table name in the Data Dictionary includes an extension.

\*/

oDB := DBServer {"MYTABLE", DBShared,, "ADSADT"}

 

/\* Clipper commands could also be used, be sure to include STD.UDC in the project's UDCs \*/

/\* USE MYTABLE SHARED NEW VIA "ADSADT" \*/

 

AdsGetLastError( @dwError, pacError, @wLen)

IF dwError != AE\_SUCCESS

ErrorBox{ , " Advantage error = " + Psz2String(pacError) }:Show()

ELSE

ErrorBox{ , " SUCCESS" }:Show()

ENDIF

 

MemFree( pacError )

 

/\* Clear the connection handle \*/

AX\_SetConnectionHandle( 0 )

 

/\* close for Clipper style \*/

/\* CLOSE \*/

 

oDB:Close()