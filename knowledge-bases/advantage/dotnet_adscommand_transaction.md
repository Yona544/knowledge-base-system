AdsCommand.Transaction




Advantage Database Server 12  

AdsCommand.Transaction

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommand.Transaction  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommand.Transaction Advantage .NET Data Provider dotnet\_Adscommand\_transaction Advantage .NET Data Provider > AdsCommand Class > AdsCommand Properties > AdsCommand.Transaction / Dear Support Staff, |  |
| AdsCommand.Transaction  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the transaction in which the AdsCommand executes.

public AdsTransaction Transaction {get; set;}

Remarks

This property can be used to store a transaction object. With the Advantage .NET Data Provider, it is not necessary to assign this property in order to use the AdsCommand object within a transaction. With Advantage Database Server, all commands executed on an AdsConnection while that connection has a transaction active are automatically run in that transaction.

Advantage Local Server does not support transactions. To use transactions, it is necessary to use Advantage Database Server.

Example

This example performs an update statement within a transaction. It uses the Transaction property of the command object to store the transaction object and retrieves it after the UPDATE statement to perform the commit.

// create a connection object

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

 

// open the connection

conn.Open();

// create a new command object and start a new transaction

cmd = new AdsCommand( "update departments set budget = budget \* 1.05",

conn, conn.BeginTransaction() );

// execute the query

cmd.ExecuteNonQuery();

// commit the transaction

cmd.Transaction.Commit();

// close the connection.

conn.Close();

See Also

[AdsConnection.BeginTransaction](dotnet_adsconnection_begintransaction_.htm)

[AdsTransaction](dotnet_adstransaction.htm)