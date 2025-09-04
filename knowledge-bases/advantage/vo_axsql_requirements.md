AXSQL Requirements




Advantage Database Server 12  

AXSQL Requirements

Advantage AXSQL RDDs

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AXSQL Requirements  Advantage AXSQL RDDs |  |  | Feedback on: Advantage Database Server 12 - AXSQL Requirements Advantage AXSQL RDDs vo\_Axsql\_requirements Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Using the Advantage AXSQL RDDs > AXSQL Requirements / Dear Support Staff, |  |
| AXSQL Requirements  Advantage AXSQL RDDs |  |  |  |  |

With the regular Advantage RDDs (ADSADT/AXDBFCDX/AXDBFNTX/AXDBFVFP), no explicit connection to the Advantage server is necessary. The Advantage driver creates a new connection automatically based on the path of the given table. With SQL, there typically are no table paths given, only table names. For this reason the AXSQL RDDs require you to first connect to an Advantage server (local or remote) before executing a query. This is done using the AdsConnect60 ACE API. Once the connection is made, the connection handle must be given to the RDD using the [AX\_SetConnectionHandle](vo_ax_setconnectionhandle.htm) function in the DBFAXS library. For example:

LOCAL dwRet AS DWORD

LOCAL hConnect AS DWORD

LOCAL oServer AS AdsSQLServer

dwRet := AdsConnect60( String2Psz( "\\server\share" ), ADS\_REMOTE\_SERVER, NULL\_PSZ, NULL\_PSZ, ADS\_DEFAULT, @hConnect )

// Be sure to check dwRet to make sure the connection succeeded

AX\_SetConnectionHandle( hConnect )

oServer := AdsSQLServer{ "SELECT \* FROM customers", , , "AXSQLADT" }