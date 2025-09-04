AdsCommand.ExecuteScalar




Advantage Database Server 12  

AdsCommand.ExecuteScalar

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommand.ExecuteScalar  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommand.ExecuteScalar Advantage .NET Data Provider dotnet\_Adscommand\_executescalar Advantage .NET Data Provider > AdsCommand Class > AdsCommand Methods > AdsCommand.ExecuteScalar / Dear Support Staff, |  |
| AdsCommand.ExecuteScalar  Advantage .NET Data Provider |  |  |  |  |

Executes the query, and returns the first column of the first row in the result set returned by the query. Extra columns or rows are ignored.

public object ExecuteScalar();

Remarks

Use the ExecuteScalar method to retrieve a single value (for example, an aggregate value) from a database. This requires less code than using the [AdsCommand.ExecuteReader](dotnet_adscommand_executereader.htm) method and the associated calls to the AdsDataReader.

Example

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

 

// open the connection

conn.Open();

// create a new command object

cmd = conn.CreateCommand();

// specify a query

cmd.CommandText = "select now() from system.iota";

// execute the query

Console.WriteLine( cmd.ExecuteScalar().ToString() );

 

// find number of rows in a table

cmd.CommandText = "select count(\*) from departments";

// execute the query

Console.WriteLine( cmd.ExecuteScalar().ToString() );

See Also

[ExecuteReader](dotnet_adscommand_executereader.htm)

[ExecuteNonQuery](dotnet_adscommand_executenonquery.htm)