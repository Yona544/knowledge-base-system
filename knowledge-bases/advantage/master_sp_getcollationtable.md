sp\_GetCollationTable




Advantage Database Server 12  

sp\_GetCollationTable

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_GetCollationTable |  |  | Feedback on: Advantage Database Server 12 - sp\_GetCollationTable master\_Sp\_getcollationtable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| sp\_GetCollationTable |  |  |  |  |

Advantage SQL Engine

Retrieve all information for the named dynamic collation.

Syntax

sp\_GetCollationTable(

Name,CiCharacter,100,

ShortName,CiCharacter,8,

CodePage,Integer )

Parameters

|  |  |
| --- | --- |
| Name (I) | The unique long name of the collation (e.g., GENERAL\_VFP\_CI\_AS\_1252). If this name is given, the ShortName and CodePage parameters are given. If this name is NULL or empty, the ShortName and CodePage must be given. |
| ShortName (I) | Instead of sending the long name, the short Visual FoxPro name (GENERAL) can be passed in this parameter. If this is given, then the desired codepage must also be supplied. |
| CodePage (I) | If ShortName is given instead of the long unique name, then the desired codepage (e.g., 1252) must be supplied to make the search unique. |

Output

The sp\_GetCollationTable procedure will return a result set with a single row.

|  |  |  |  |
| --- | --- | --- | --- |
| Field Name | Field Type | Field Size | Description |
| CollationID | Integer | 4 | This is the ID of the collation on the server. It is for internal use. |
| Name | CiCharacter | 100 | The long unique collation name. |
| ShortName | CiCharacter | 8 | The short collation name. This is the name that is used directly in Visual FoxPro. |
| Version | Integer | 4 | The version number of the collation table. |
| CodePage | Integer | 4 | The codepage for which the collation was created. |
| CE | Blob | 9 | This contains the collation information. |
| Upper | Blob | 9 | The upper case conversion table. |
| Lower | Blob | 9 | The lower case conversion table. |
| NumContractions | Integer | 4 | The number of contraction pairs that exist in the collation. |
| Contractions | Blob | 9 | The contraction information if applicable. |
| AllowMultiple | Logical | 1 | Flag that indicates whether the collation table can be used at the same time as other collation tables on a given DBF or ADT table. |

Remarks

sp\_GetCollationTable retrieves a single collation table entry from adscollate.adt. It is primarily intended for internal usage. An application should not need to use this procedure. At this time, the collation information that is returned is not documented.

See Also

[sp\_GetCollations](master_sp_getcollations.htm)

[Dynamic Collation Support](master_collation_support.htm)