AX\_SetConnectionHandle()




Advantage Database Server 12  

AX\_SetConnectionHandle()

Advantage Visual Objects and Vulcan.NET RDD

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AX\_SetConnectionHandle()  Advantage Visual Objects and Vulcan.NET RDD |  |  | Feedback on: Advantage Database Server 12 - AX\_SetConnectionHandle() Advantage Visual Objects and Vulcan.NET RDD vo\_Ax\_setconnectionhandle Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Advanced  Functions > AX\_SetConnectionHandle() / Dear Support Staff, |  |
| AX\_SetConnectionHandle()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Sets the connection handle for all successive table opens.

Syntax

AX\_SetConnectionHandle( <hConnection> ) -> nil

|  |  |
| --- | --- |
| <hConnection> | A long integer that is a connection handle obtained from a call to AdsConnect, AdsConnect26, or AdsConnect60. A value of 0 clears the handle. |

Returns

This function always succeeds. Nil is always returned.

Description

AX\_SetConnectionHandle sets the Advantage connection handle that will be used by the Advantage RDD for all future operations that cause a table to be opened. If no connection handle has been set (i.e., this function has never been called with a specific Advantage connection handle, or this function has been called with a parameter value of 0 to clear the connection handle), all future operations that cause a table to be opened will use an existing connection if one to the same server type exists. In cases where a connection to the server doesn't exist or can't be used, a new connection will be created. For example, an existing connection to the Advantage Internet Server will not be used when opening a table via the Advantage Database server. Instead, a new connection will be created and used. This is due to the server types of the existing connection and the requested connection being different.

The only way to open a [database table](javascript:hhpopuplink.TextPopup(popid_1693948312,FontFace,-1,-1,-1,-1)) is to use this function with a connection handle to the appropriate Advantage Data Dictionary file. Use of this function is also required when connecting to the Advantage Internet Server. This connection handle can be used along with the [AX\_Transaction](vo_ax_transaction.htm) function.

Object-oriented Example

LOCAL oDB AS DBServer

LOCAL dwError AS DWORD

LOCAL pacError AS PSZ

LOCAL wLen AS WORD

LOCAL lReturn AS LONGINT

LOCAL hConnect AS LONGINT

 

pacError := MemAlloc( 200 )

wLen := 200

dwError := AE\_SUCCESS

 

/\*

\* HandleErrors is a function you may write to catch and handle connection errors.

\*/

HandleErrors( AdsConnect60( "X:\DATA\TEST.ADD", ADS\_REMOTE\_SERVER, ;

"UserName", "Password", ADS\_INC\_USERCOUNT, @hConnect ))

 

/\* Set the connection handle \*/

AX\_SetConnectionHandle( hConnect )

 

/\*

\* Since a database path is specified in the connection, it does not need

\* to be specified here. No extension to the table name is needed unless the

\* table name in the Data Dictionary includes an extension.

\*/

oDB := DBServer {"MYTABLE", DBShared,, "ADSADT"}

 

AdsGetLastError( @dwError, pacError, @wLen)

IF dwError != AE\_SUCCESS

ErrorBox{ , " Advantage error = " + Psz2String(pacError) }:Show()

ENDIF

ErrorBox{ , " SUCCESS" }:Show()

 

/\* Clear the connection handle. It is not required to clear the connection handle unless

\* you no longer want to use hConnect as the connection handle for future table opens.

\*/

AX\_SetConnectionHandle( 0 )

 

oDB:Close()