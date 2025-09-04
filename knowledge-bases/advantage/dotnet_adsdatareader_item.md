AdsDataReader.Item




Advantage Database Server 12  

AdsDataReader.Item

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDataReader.Item  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsDataReader.Item Advantage .NET Data Provider dotnet\_Adsdatareader\_item Advantage .NET Data Provider > AdsDataReader Class > AdsDataReader Properties > AdsDataReader.Item / Dear Support Staff, |  |
| AdsDataReader.Item  Advantage .NET Data Provider |  |  |  |  |

Gets the value of the specified column in its native format given the column name or number.

public object this[ string name ] {get;}

 

public object this[ int i ] {get;}

Remarks

In C#, this property is the indexer for the AdsDataReader class. The column name or the zero-based column ordinal can be used to retrieve the value.

Example

AdsConnection conn = new AdsConnection( "data source=c:\\data;" );

AdsCommand cmd;

AdsDataReader reader;

 

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

 

reader.Read();

 

// print column with both versions of indexer

Console.WriteLine( reader[0].ToString() );

Console.WriteLine( reader["department code"].ToString() );

 

conn.Close();

}

catch ( AdsException e )

{

// print the exception message

Console.WriteLine( e.Message );

}

See Also

[GetValue](dotnet_adsdatareader_getvalue.htm)