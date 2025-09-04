AdsGetNumActiveLinks




Advantage Database Server 12  

AdsGetNumActiveLinks

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetNumActiveLinks  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetNumActiveLinks Advantage Client Engine ace\_Adsgetnumactivelinks Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetNumActiveLinks  Advantage Client Engine |  |  |  |  |

Retrieves the number of links active on the current connection.

Syntax

UNSIGNED32 AdsGetNumActiveLinks( ADSHANDLE hDBConn,

UNSIGNED16 \*pusNumLinks );

Parameters

|  |  |
| --- | --- |
| hDBConn (I) | Handle of a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |
| pusNumLinks (O) | Returns the number of links that are active on the current connection. |

Remarks

This function is used to retrieve the number of active links on the current connection. A global link that is stored in the data dictionary is not active until it is used in an SQL statement on the current connection.

Example

The execution of the following SQL statement creates an implicit link to the ARCHIVE database so the AdsGetNumActiveLinks should return 1 in the output.

AdsConnect60( "n:\\MyData\\MASTER.ADD", ADS\_REMOTE\_SERVER, "User1",

"password", ADS\_DEFAULT, &hDBConn );

 

AdsCreateSQLStatement( hDBConn, &hStmt );

 

AdsExecuteSQLDirect( hStmt, "SELECT Max(LastDate) FROM \"n:\\MyData\\ARCHIVE\\ARCHIVE.ADD\".Table1",

&hCursor );

 

// usNumLinks should be 1

AdsGetNumActiveLinks( hDBConn, &usNumLinks );

See Also

[AdsDDCreateLink](ace_adsddcreatelink.htm)

[AdsDDDropLink](ace_adsdddroplink.htm)

[AdsDDGrantPermission](ace_adsddgrantpermission.htm)

[AdsDDRevokePermission](ace_adsddrevokepermission.htm)

[AdsDDFindFirstObject](ace_adsddfindfirstobject.htm)

[AdsDDFindNextObject](ace_adsddfindnextobject.htm)

[AdsDDGetLinkProperty](ace_adsddgetlinkproperty.htm)

[AdsDDModifyLink](ace_adsddmodifylink.htm)

[AdsGetActiveLinkInfo](ace_adsgetactivelinkinfo.htm)