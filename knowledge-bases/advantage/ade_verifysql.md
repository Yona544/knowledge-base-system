VerifySQL




Advantage Database Server 12  

TAdsQuery.VerifySQL

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsQuery.VerifySQL  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsQuery.VerifySQL Advantage TDataSet Descendant ade\_Verifysql Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsQuery.VerifySQL  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.htm)

Verifies the validity of an SQL statement without executing it.

Syntax

procedure VerifySQL;

Description

VerifySQL sends the SQL statement residing in TAdsQuery.SQL to the Advantage Database Server to determine if it is a valid SQL statement. This is useful to call prior to executing a time consuming SQL statement. In the event of an invalid statement, an exception will be raised with the corresponding error message in the exception object.

Example

try

AdsConnection1 := TAdsConnection.Create( nil );

AdsQuery1 := TAdsQuery.Create( nil );

 

AdsConnection1.AdsServerTypes := [stADS\_LOCAL];

AdsConnection1.ConnectPath := 'c:\testdata';

AdsConnection1.Name := 'Conn';

 

AdsQuery1.SourceTableType := ttAdsADT;

AdsQuery1.DatabaseName := 'Conn';

AdsQuery1.SQL.Add('SELECT \* from demo10');

AdsQuery1.VerifySQL;

AdsQuery1.ExecSQL;

 

except

on E: Exception do

Application.MessageBox(PChar(E.Message), 'Error', MB\_OK);

end;