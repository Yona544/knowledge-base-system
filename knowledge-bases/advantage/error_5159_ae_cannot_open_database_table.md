5159 AE\_CANNOT\_OPEN\_DATABASE\_TABLE




Advantage Database Server 12  

5159 AE\_CANNOT\_OPEN\_DATABASE\_TABLE

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5159 AE\_CANNOT\_OPEN\_DATABASE\_TABLE  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5159 AE\_CANNOT\_OPEN\_DATABASE\_TABLE Advantage Error Guide error\_5159\_ae\_cannot\_open\_database\_table Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5159 AE\_CANNOT\_OPEN\_DATABASE\_TABLE  Advantage Error Guide |  |  |  |  |

Problem: An error was encountered when trying to open a database table. This error can occur when attempting to open a [database table](javascript:hhpopuplink.TextPopup(popid_174150351X,FontFace,-1,-1,-1,-1)) as a [free table](javascript:hhpopuplink.TextPopup(popid_273202014X,FontFace,-1,-1,-1,-1)).

Solution for Advantage Client Engine API: When opening a database table using the Advantage Client Engine API, make sure ADS\_DEFAULT is specified as the table type. When opening a free table with the Advantage Client Engine API, the table type must be ADS\_ADT, ADS\_CDX, ADS\_VFP, or ADS\_NTX.

Solution for Advantage TDataSet Descendant: When opening a database table using the Advantage TDataSet Descendant, make sure to specify the full path to the Advantage Data Dictionary .ADD file in the TAdsConnection.ConnectPath property (for example, "x:\data\sampledd.add").

Solution for Advantage OLE DB Provider (for ADO): When opening a database table using the Advantage OLE DB Provider (for ADO), make sure to specify the full path to the Advantage Data Dictionary .ADD file for the Data Source key word in the ADO connection string (for example, "Data Source=x:\data\sampledd.add").

Solution for Advantage ODBC Driver: When opening a database table using the Advantage ODBC Driver, make sure to check the "Data Dictionary" check box and to specify the full path to the Advantage Data Dictionary .ADD file for the "Database or Data Dictionary Path" edit in the Data Source Setup Screen (for example, "x:\data\sampledd.add").