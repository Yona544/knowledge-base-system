Providing an External Advantage Connection Handle to the Advantage Crystal Reports Driver




Advantage Database Server 12  

Providing an External Advantage Connection Handle to the Advantage Crystal Reports Driver

Crystal Reports

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Providing an External Advantage Connection Handle to the Advantage Crystal Reports Driver  Crystal Reports |  |  | Feedback on: Advantage Database Server 12 - Providing an External Advantage Connection Handle to the Advantage Crystal Reports Driver Crystal Reports crystal\_Providing\_an\_external\_advantage\_connection\_handle\_to\_the\_advantage\_crystal\_reports\_driver Advantage Crystal Reports > Using the Advantage Crystal Reports Driver > Providing an External Advantage Connection Handle > Providing an External Advantage Connection Handle to the Advantage Crystal Reports Driver / Dear Support Staff, |  |
| Providing an External Advantage Connection Handle to the Advantage Crystal Reports Driver  Crystal Reports |  |  |  |  |

Note Passing an external connection to the Advantage Crystal Reports Driver is only supported with Crystal Reports version 9 and newer.

The following information describes how an Advantage connection can be provided to the Advantage Crystal Reports Driver for use in running reports. The default behavior of the Advantage Crystal Reports Driver is to create a new connection for each report. Using a single connection shared between an application and the Advantage Crystal Reports Driver has the following benefits:

Benefits

|  |  |
| --- | --- |
| · | Performance Normally, the Advantage Crystal Reports Driver creates and destroys a new connection to the Advantage server each time a report is run. Depending on the speed of the report and the frequency in which an application runs the report, this can be a significant performance issue. By providing an established connection to the Advantage Crystal Reports Driver, the time required to create the new connection and destroy it can be eliminated. |

|  |  |
| --- | --- |
| · | Resource Conservation For each connection made to the Advantage server, memory resources are consumed both on the client and server. Although the maximum number of connections is configurable on the server, exceeding the maximum amount is not allowed. If the Advantage server reaches maximum connection capacity, subsequent connection attempts are denied. By providing an established connection to the Advantage Crystal Reports Driver, memory resources can be conserved and connection denied errors minimized. |

|  |  |
| --- | --- |
| · | Availability of Connection Specific Resources Some resources, such as temporary tables and the application ID, are available on a per connection basis. This means that only the connection that created them can access them. By providing an established connection to the Advantage Crystal Reports Driver, connection specific resources can be used by reports. For example, temporary tables created on the connection can be referenced by reports when the connection that created the tables is passed to the report. |

Creating an External Connection to the Advantage Crystal Reports Driver

Advantage connection handles are simply 32-bit integer values. Any application module can use these handles, as long as the handle is used within the same process space as the application that created it. This is precisely how the Advantage Crystal Reports Driver can use an external Advantage connection.

First, the application must connect to the Advantage server. A simple way to make this connection is with the AdsConnect60 ACE API. Once the connection is established, its integer value is converted into a string form, then provided to the Advantage Crystal Reports Driver via an ODBC style connection option.

Note Do not disconnect the connection provided to the Advantage Crystal Reports Driver while the report is running. This can produce unexpected results and undesirable behavior.

Designing Crystal Reports to use External Connections

When reports are designed from within the Crystal Reports IDE, the Advantage Crystal Reports Driver creates its own connection based on the selected alias found in the ads.ini file. This means that at design time, an alias must exist for the report to use. It also means that per-connection items such as temp tables are not available at design time. This makes designing reports based on temporary items difficult. Two solutions exist to get around this issue:

|  |  |
| --- | --- |
| 1. | Create a static version of the item for use during the design of the report. If the report is meant to extract data from a temporary table, create a normal table with the same table structure for use when creating the report. When the report is finished, delete the normal table. Then when the report is run, change the name of the table used by the report at runtime. Finally, pass in the connection handle which contains the temporary table to the report at runtime. |

|  |  |
| --- | --- |
| 2. | Create the temporary item at design time from within the Crystal Reports IDE. Begin by designing the report to select data from an existing table or system table (i.e., system.iota). Once the report is created, open the Database Expert utility and locate the command which the report is using. Right-click on the command and select Edit Command. Then from within the Modify Command dialog, enter an SQL statement to create the temporary item (for example CREATE TABLE #temp ). Click the OK button and an error will be returned. This is expected. The SQL statement will be run by the Advantage Crystal Reports Driver and as a result, the temporary item will now exist on the Advantage Crystal Reports driver connection. Finally, change the SQL statement to the desired SELECT statement using the temporary item. |

Changing the Report to use a Different Table at Runtime

There are two methods for changing the table(s) which a report is run against. First, you can change just the table name(s) directly using the TCrpeTablesItem.Name and TCrpeTablesItem.SubName properties. Second, you can change the SQL query the report is based on by replacing the existing table name(s) in the query text.

|  |  |
| --- | --- |
| 1. | Changing the Name and SubName properties. Changing just the table name(s) the report was designed for is probably the most simple and natural way to run a report against a table the report was not designed with (a temporary table for instance). Simply change the TCrpeTablesItem.Name and TCrpeTablesItem.SubName properties of the tables in the report to that of the new table name(s). If the new tables are temporary tables, remember that you must also pass to the Advantage Crystal Reports driver the connection handle in which the temporary tables were created on. See the Delphi TCrpe example titled "Delphi, using the TCrpe components to change the table name at runtime" below for a code sample. |

|  |  |
| --- | --- |
| 2. | Changing the SQL query text. Using the Crystal Reports API, you can change the SQL query stored in the report to reference different tables than what the report was created with. According to the Crystal Reports help documentation, changes to the query are allowed in the FROM, WHERE, and ORDER BY clauses but are not allowed in the SELECT clause. So by changing the table names in the FROM clause, the query can be executed on different tables (temporary tables for instance). See the Delphi TCRpe example titled "Delphi, using the TCRpe components" below for a code sample. |

Examples

Delphi, using COM:

procedure COMTest( hConnect : ADSHANDLE );

var

oCRReport : OleVariant;

oCRApplication : OleVariant;

oCRDatabase : OleVariant;

oCRTable : OleVariant;

i : Integer;

begin

 

oCRApplication := CreateOleObject( 'crystalruntime.application.11' );

oCRReport := oCRApplication.OpenReport( 'C:\test\_report.rpt' );

oCRDatabase := oCRReport.Database;

 

// If the report has multiple tables, we need to set the connection

// handle for each table.

if oCRDatabase.Tables.Count > 1 then

for i := 1 to oCRDatabase.Tables.Count do

begin

oCRTable := oCRDatabase.Tables.Item[ i ];

oCRTable.SetLogOnInfo( 'ADS\_ADT', // Alias name used by the report

'ConnectionHandle = ' + IntToStr( hConnect ) + ';',

'', '' )

end

else

oCRDatabase.LogOnServer( 'crdb\_ads.dll',

'ADS\_ADT', // Alias name used by the report

'ConnectionHandle = ' + IntToStr( hConnect ) + ';',

'', '' );

 

oCRReport.DiscardSavedData;

oCRReport.ExportOptions.DestinationType := 1; // file

oCRReport.ExportOptions.DiskFileName := 'C:\test\_report.txt';

oCRReport.ExportOptions.FormatType := 10; // paginated text

 

// Run (export) the report

oCRReport.Export( FALSE );

 

// Clean up the OLE variables

oCRTable := Unassigned;

oCRDatabase := Unassigned;

oCRReport := Unassigned;

oCRApplication := Unassigned;

end;

 

Delphi, using the TCRpe components:

procedure CrystalTest( AdsConn : TAdsConnection );

var

Crpe1 : TCRpe;

begin

try

Crpe1 := TCRpe.Create( NIL );

Crpe1.DiscardSavedData;

Crpe1.ReportName := 'C:\test\_report.rpt';

Crpe1.Connect.DatabaseName := 'ConnectionHandle=' + IntToStr( AdsConn.Handle ) + ';';

Crpe1.SQL.Query.Text := 'SELECT "CustTable"."id", "CustTable"."Name" FROM "#TempCustTable" "CustTable"';

Crpe1.Show;

 

finally

Crpe1.CloseWindow;

Crpe1.CloseJob;

Crpe1.Destroy;

end;

end;

 

Delphi, using the TCrpe components to change the table name at runtime:

procedure TableNameExample;

var

Crpe: TCrpe;

hConn : ADSHANDLE;

hStmt : ADSHANDLE;

ulRetVal : UNSIGNED32;

begin

ulRetVal := AdsConnect60( 'X:\data', ADS\_REMOTE\_SERVER, NIL, NIL, 0, @hConn );

ulRetVal := AdsCreateSQLStatement( hConn, @hStmt );

ulRetVal := AdsExecuteSQLDirect( hStmt, pChar( 'CREATE TABLE #mytab ( id integer, name char(50));' +

'INSERT INTO #mytab VALUES ( 57, ''temp data'' );' ), NIL );

crpe := TCrpe.Create( NIL );

crpe.ReportName := 'C:\Report1.rpt';

crpe.connect.DatabaseName :='ConnectionHandle='+IntToStr(hConn)+';';

crpe.DiscardSavedData;

crpe.Tables[0].Name := '#mytab';

crpe.Tables[0].SubName := '#mytab';

crpe.Show;

crpe.Clear;

crpe.Destroy();

AdsDisconnect( hConn );

end;

Visual Basic .NET:

Private Sub ReportTest(ByVal hConnect As UInt32)

Dim tbCurrent As CrystalDecisions.CrystalReports.Engine.Table

Dim tliCurrent As CrystalDecisions.Shared.TableLogOnInfo

Dim rptCustomersOrders As New CrystalDecisions.CrystalReports.Engine.ReportDocument

 

Try

' Load the report file

rptCustomersOrders.Load("C:\test\_report.rpt")

 

' Refresh the report's data

rptCustomersOrders.Refresh()

 

' Set the DatabaseName for each of the report's tables

tliCurrent = New CrystalDecisions.Shared.TableLogOnInfo

For Each tbCurrent In rptCustomersOrders.Database.Tables

tliCurrent.ConnectionInfo.DatabaseName = "ConnectionHandle = " + Convert.ToString(hConnect) + ";"

tbCurrent.ApplyLogOnInfo(tliCurrent)

Next tbCurrent

 

' Pass the report to the report viewer control

crvReportViewer.ReportSource = rptCustomersOrders

 

Catch Exp As CrystalDecisions.CrystalReports.Engine.LoadSaveReportException

MsgBox("Incorrect path for loading report.", MsgBoxStyle.Critical, "Load Report Error")

Catch Exp As Exception

MsgBox(Exp.Message, MsgBoxStyle.Critical, "General Error")

End Try

End Sub