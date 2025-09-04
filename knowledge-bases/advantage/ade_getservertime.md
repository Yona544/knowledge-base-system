GetServerTime




Advantage Database Server 12  

TAdsConnection.GetServerTime

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.GetServerTime  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.GetServerTime Advantage TDataSet Descendant ade\_Getservertime Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.GetServerTime  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Retrieves the current time and date from the server via the Advantage Database Server

Syntax

function GetServerTime: TDateTime;

Description

GetServerTime returns the current date and time from the server, which is useful if the Advantage client application is running at a site that is in a different time zone than where the data is located and is being accessed by the Advantage Database Server. When Advantage is used in a WAN environment or is being used with the Advantage Internet Server, the Advantage client and Advantage server will often be located in different time zones. This function allows time, date, and timestamp fields to be populated with a consistent date and time, that is, the date and time of the server location.

Example

procedure TForm1.Test();

var

dtDateTime : TDateTime;

begin

 

{\* Get the server date and time \*}

dtDateTime := MyConnection1.GetServerTime();

 

{\* Display the current server time \*}

lbServerTime.Caption := DateTimeToStr( dtDateTime );

 

end;