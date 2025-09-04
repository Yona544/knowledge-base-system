AdsException




Advantage Database Server 12  

AdsException

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsException  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsException Advantage .NET Data Provider dotnet\_Adsexception Advantage .NET Data Provider > AdsException Class > Overview / Dear Support Staff, |  |
| AdsException  Advantage .NET Data Provider |  |  |  |  |

Full name: Advantage.Data.Provider.AdsException

Inherits: System.SystemException

[Properties](dotnet_adsexception_properties.htm)

The Advantage .NET Data Provider throws AdsException exceptions when errors specific to the provider are generated. For example, if an error is returned by the Advantage Database Server when executing an SQL statement, the Advantage .NET Data Provider will throw an AdsException.

Example

try

{

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

 

conn.Open();

// create a command with a syntax error

cmd = new AdsCommand( "update bad statement", conn );

// execute the query (will throw an exception)

Console.WriteLine( "Records affected: " + cmd.ExecuteNonQuery() );

 

}

catch ( AdsException e )

{

// print the exception information

Console.WriteLine( "Error Number: " + e.Number );

Console.WriteLine( "Error State: " + e.State );

Console.WriteLine( "Message: " + e.Message );

}

catch ( Exception e )

{

// handle non-Advantage-specific exceptions

Console.WriteLine( e.Message );

}

See Also

[AdsInfoMessageEventArgs](dotnet_adsinfomessageeventargs.htm)