Quick Start




Advantage Database Server 12  

Quick Start

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Quick Start  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - Quick Start Advantage .NET Data Provider dotnet\_Quick\_start Advantage .NET Data Provider > Introduction > Quick Start / Dear Support Staff, |  |
| Quick Start  Advantage .NET Data Provider |  |  |  |  |

|  |  |
| --- | --- |
| · | If you are using Microsoft Visual Studio, you can access the Advantage .NET Data Provider components visually from the Toolbox. After installing the provider and starting Visual Studio, open the Toolbox (available under the View menu if it is not visible) and expand the Data category. Right click and select "Choose Items" This will open a dialog that allows you to select which components should be displayed in the Toolbox. You can select the Advantage components (AdsCommand, AdsConnection, and AdsDataAdapter). |

|  |  |
| --- | --- |
| · | In your project, Add a reference to Advantage.Data.Provider. For example, from Visual Studio .NET, choose "Add Reference" from the Project menu. Advantage.Data.Provider should be available in the .NET component list. If it is not, you may need to run the Advantage .NET Data Provider installation. Note that if you drag one of the visual components from the Toolbox onto a form, a reference to Advantage.Data.Provider will be added automatically. |

|  |  |
| --- | --- |
| · | Specify the name space at the top of the source file prior to any declarations. For example, with C#, include this statement: |

using Advantage.Data.Provider;

Within Visual Basic .NET, use this statement:

Imports Advantage.Data.Provider

|  |  |
| --- | --- |
| · | Declare and use the Advantage .NET Data Provider classes. |

The following is a simple example that connects to Advantage Database Server, runs a SELECT statement and prints the field values to the console.

C# Example:

// create a connection object

AdsConnection conn = new AdsConnection( "data source=c:\\data;" +

"ServerType=remote|local; TableType=ADT" );

AdsCommand cmd;

AdsDataReader reader;

int iField;

 

try

{

 

// make the connection to the server

conn.Open();

 

// create a command object

cmd = conn.CreateCommand();

 

// specify a simple SELECT statement

cmd.CommandText = "select \* from departments";

 

// execute the statement and create a reader

reader = cmd.ExecuteReader();

 

// dump the results of the query to the console

while ( reader.Read() )

{

for ( iField = 0; iField < reader.FieldCount; iField++ )

Console.Write( reader.GetValue(iField) + " ");

Console.WriteLine();

}

 

conn.Close();

}

catch ( AdsException e )

{

// print the exception message

Console.WriteLine( e.Message );

}

The following is the equivalent example written in Visual Basic:

' create a connection object

Dim conn As New AdsConnection("data source = c:\data; " & \_

"ServerType=remote|local; TableType=ADT")

Dim cmd As AdsCommand

Dim reader As AdsDataReader

Dim iField As Integer

 

Try

 

'make the connection to the server

conn.Open()

 

'create a command object

cmd = conn.CreateCommand()

 

'specify a simple SELECT statement

cmd.CommandText = "select \* from departments"

 

'execute the statement and create a reader to read the results

reader = cmd.ExecuteReader()

 

'dump the results of the query to the console

While reader.Read()

For iField = 0 To reader.FieldCount - 1

Console.Write(reader.GetValue(iField) & " ")

Next

Console.WriteLine()

End While

 

conn.Close()

 

Catch e As AdsException

'print the exception message

Console.WriteLine(e.Message)

End Try