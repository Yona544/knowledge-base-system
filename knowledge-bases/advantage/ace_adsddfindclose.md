AdsDDFindClose




Advantage Database Server 12  

AdsDDFindClose

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDDFindClose  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDDFindClose Advantage Client Engine ace\_Adsddfindclose Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDDFindClose  Advantage Client Engine |  |  |  |  |

Terminates an active search in the data dictionary and free the resources that was allocated for the search.

Syntax

UNSIGNED32 AdsDDFindClose( ADSHANDLE hDBConn, ADSHANDLE hFindHandle );

Parameters

|  |  |
| --- | --- |
| hDBConn (I) | Handle of a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)). |
| hFindHandle (I) | Find handle that was returned by [AdsDDFindFirstObject](ace_adsddfindfirstobject.htm). |

Special Return Codes

None.

Remarks

AdsDDFindClose is used to terminate a search initiated by [AdsDDFindFirstObject](ace_adsddfindfirstobject.htm).

Example

Find all index files that are associated with the "Customer Information" table.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

usBufferSize = sizeof( aucFileName );

if ( AE\_SUCCESS == AdsDDFindFirstObject( hDD, ADS\_DD\_INDEX\_FILE\_OBJECT,

"Customer Information", aucFileName,

&usBufferSize ))

{

do

{

printf( "%s\n", aucFileName );

usBufferSize = sizeof( aucFileName );

}

while ( AE\_SUCCESS == AdsDDFindNextObject( hDD, aucFileName, &usBufferSize ));

AdsDDFindClose( hDD );

}

See Also

[AdsDDFindFirstObject](ace_adsddfindfirstobject.htm)

[AdsDDFindNextObject](ace_adsddfindnextobject.htm)

[AdsConnect60](ace_adsconnect60.htm)