AdsGetConnectionProperty




Advantage Database Server 12  

AdsGetConnectionProperty

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetConnectionProperty  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetConnectionProperty Advantage Client Engine ace\_Adsgetconnectionproperty Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetConnectionProperty  Advantage Client Engine |  |  |  |  |

Returns data about an active connection.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetConnectionProperty( ADSHANDLE hConnect,  UNSIGNED16 usPropertyID,  VOID \*pvProperty,  UNSIGNED32 \*pulPropertyLen ); |

Parameters

|  |  |
| --- | --- |
| hConnect (I) | Connection handle. |
| usPropertyID (I) | Constant identifying what property to retrieve. |
| pvProperty (O) | Pointer to a buffer in which the returned value will be placed. |
| pulPropertyLen (I/O) | On input, the size of the buffer pointed to by pvProperty. On output, the length of data returned in pvProperty. |

Remarks

The following values can be passed in the usPropertyID parameter:

ADS\_CONNECTIONPROP\_USERNAME

Retrieve a null-terminated string representation of the username. If the connection is a [free connection](javascript:hhpopuplink.TextPopup(popid_7577555X,FontFace,-1,-1,-1,-1)) (as opposed to a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1))), an empty string will be returned.

ADS\_CONNECTIONPROP\_PASSWORD

Retrieve a null-terminated string representation of the password in the pvProperty buffer. If the connection is a [free connection](javascript:hhpopuplink.TextPopup(popid_7577555X,FontFace,-1,-1,-1,-1)) (as opposed to a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1))), an empty string will be returned.

ADS\_CONNECTIONPROP\_PROTOCOL

Retrieve a 4-byte integer value representing the communications type with Advantage Database Server. The values are 0 (local server), 1 (TCP/IP), 2 (UDP), 3 (IPX), 4 (Shared Memory), or 5 (SSL/TLS).

ADS\_CONNECTIONPROP\_ENCRYPTION\_TYPE

Retrieve a null-terminated string with the current encryption type. The values can be AES128, AES256, or RC4.

ADS\_CONNECTIONPROP\_FIPS\_MODE

Retrieve a 2-byte value indicating if FIPS mode is active. The value will be 1 (TRUE) or 0 (FALSE).

ADS\_CONNECTIONPROP\_CERTIFICATE\_FILE

Retrieve a null-terminated string with the name of the the certificate file specified for TLS communications (if applicable).

ADS\_CONNECTIONPROP\_CIPHER\_SUITE

Retrieve a null-terminated string with the cipher suite specified for TLS communications (if applicable).

ADS\_CONNECTIONPROP\_COMMON\_NAME

Retrieve a null-terminated string with the common name specified for TLS communications (if applicable).