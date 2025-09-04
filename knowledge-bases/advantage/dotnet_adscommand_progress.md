AdsCommand.Progress




Advantage Database Server 12  

AdsCommand.Progress

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCommand.Progress  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsCommand.Progress Advantage .NET Data Provider dotnet\_Adscommand\_progress Advantage .NET Data Provider > AdsCommand Class > AdsCommand Properties > AdsCommand.Progress / Dear Support Staff, |  |
| AdsCommand.Progress  Advantage .NET Data Provider |  |  |  |  |

Gets the current progress of a currently executing SQL statement.

public int Progress {get;}

Remarks

This retrieves the current progress estimate of a running SQL statement. It can be retrieved by another thread to provide some kind of visual feedback (e.g., a progress bar). The value returned will range from 0 to 100.

Example

This example creates a second thread that monitors the progress of an SQL statement. It then calls the AdsCommand.Cancel method to cancel the statement.

// CancelClass for use with CallBackTest. Monitors progress

// and cancels the query after a while

public class CancelClass

{

// store reference to the command to monitor

private AdsCommand mCmd;

 

public CancelClass( AdsCommand cmd )

{

mCmd = cmd;

}

 

public void Cancel()

{

// loop a few times before cancelling the query

for ( int i = 0; i < 10 && !mCmd.TimedOut; i++ )

{

Console.WriteLine( "Current progress is " + mCmd.Progress );

 

// hang around - do whatever this thread does

Thread.Sleep( new TimeSpan( 0, 0, 0, 0, 500 ));

}

 

// cancel the query

mCmd.Cancel();

}

}

 

static public void CallBackTest()

{

AdsConnection conn = null;

AdsCommand cmd = null;

Thread CancelThread;

CancelClass fCancelProc;

AdsTransaction txn = null;

 

try

{

// get a connection and begin a transaction

conn = new AdsConnection( "data source = c:\\data" );

conn.Open();

txn = conn.BeginTransaction();

 

// use a statement that takes a while to finish

cmd = new AdsCommand( "UPDATE bigtable SET deptnum = 7", conn );

 

// create an instance of our cancel class (for the 2nd thread)

fCancelProc = new CancelClass( cmd );

 

// create a new thread to monitor the SQL progress and cancel

// the query after a while.

CancelThread = new Thread( new ThreadStart( fCancelProc.Cancel ) );

 

// start the cancel thread

CancelThread.Start();

 

// execute the statement.

// It will get an exception when the 2nd thread cancels it

Console.WriteLine( cmd.ExecuteNonQuery() + " Records Affected" );

 

// completed without being cancelled

txn.Commit();

}

catch ( Exception e )

{

if ( txn != null )

txn.Rollback();

Console.WriteLine( e.Message );

}

finally

{

if ( conn != null )

conn.Close();

}

}

See Also

[Cancel](dotnet_adscommand_cancel.htm)

[CommandTimeout](dotnet_adscommand_commandtimeout.htm)

[ProgressMessage](dotnet_adscommand_progressmessage.htm)