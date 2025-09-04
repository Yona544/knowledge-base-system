AdsGetLastAutoinc




Advantage Database Server 12  

AdsGetLastAutoinc

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetLastAutoinc  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetLastAutoinc Advantage Client Engine ace\_Adsgetlastautoinc Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetLastAutoinc  Advantage Client Engine |  |  |  |  |

Retrieves the last inserted autoinc value after an SQL INSERT or table append

Syntax

UNSIGNED32 AdsGetLastAutoinc( ADSHANDLE hObj,

UNSIGNED32 \*pulAutoincVal );

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table or statement. |
| pulAutoIncVal (O) | Return the autoinc value. |

Remarks

Returns the last inserted Autoinc value for the given handle. If no Autoinc value has been inserted or the table does not contain an Autoinc field then 0 is returned in pulAutoincVal. The autoinc value is stored per handle.

Note The autoinc value returned is client-specific, and because of concurrent database access, is not guaranteed to be the absolute last autoinc value in the table.

Example

To get the last autoinc value from a table named autoinctest with the following field definitions:

Key = Autoinc

Name = Character

Deptnum = Integer

ADSHANDLE  hSQL, hCursor;

UNSIGNED32  ulAutoincVal, ulRetVal;

 

ulRetVal =

AdsExecuteSQLDirect( hSQL,

"INSERT INTO autoinctest( name, deptnum ) VALUES( 'John', 7 )",

   &hCursor );

if( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Execute the Statement" );

return ulRetVal;

}

 

ulRetVal = AdsGetLastAutoinc( hSQL, &ulAutoincVal );

if( ulRetVal != AE\_SUCCESS )

{

/\* some kind of error, tell the user what happened \*/

AdsShowError( "ACE Couldn't Retrieve the AutoincVal" );

return ulRetVal;

}