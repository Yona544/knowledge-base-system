Additional methods available to the ADSStatement object




Advantage Database Server 12  

Additional methods available to the ADSStatement object

Advantage JDBC Driver

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Additional methods available to the ADSStatement object  Advantage JDBC Driver |  |  | Feedback on: Advantage Database Server 12 - Additional methods available to the ADSStatement object Advantage JDBC Driver jdbc\_Additional\_methods\_available\_to\_the\_adsstatement\_object Advantage JDBC Driver > Supported Functionality > Additional methods available to the ADSStatement object / Dear Support Staff, |  |
| Additional methods available to the ADSStatement object  Advantage JDBC Driver |  |  |  |  |

By casting the Statement, PreparedStatement or CallableStatement object obtained from the Advantage JDBC Driver to ADSStatement object, the application can access additional methods that are specific to the Advantage JDBC Driver. These additional methods are described in the following table. To be useful, these methods should be called on a separate thread while the thread executing the query is waiting the result of the query execution.

|  |  |
| --- | --- |
| Methods | Comments |
| void cancel() | This function instructs the Advantage Database Server to abort the execution of the current statement. |
| int getProgressInfo() | While the statement is being executed by the Advantage Database Server, calling this function will returned the estimated completion percentage. The number returned is an integer between 0 and 100. The progress information is updated roughly every second. If the query takes less than one second to execute, the returned value will not be meaningful. |

Example:

// This example demonstrate the use of the cancel() and the getProgressInfo() methods

// to monitor the progress of a statement being executed by Advantage Server. The

// example abort the query execution if it does not finish in 30 seconds.

class ProgressThread extends Thread {

 

ADSStatement mStmt;

boolean bRun = true;

 

public ProgressThread( ADSStatement stmt ) {

mStmt = stmt;

}

 

public void run() {

try {

int iElapsedTime = 0;

 

while ( bRun ) {

try {

sleep( 1000 ); // 1 second

}

catch ( InterruptedException ei ) {

}

 

++iElapsedTime;

 

// Report the progress

System.out.println( mStmt.getProgressInfo() );

 

// Abort the execution if it has been more than 30 seconds

if ( iElapsedTime >= 30 ) {

mStmt.cancel();

iElapsedTime = 0;

}

}

}

catch ( SQLException e ) {

System.err.println( e.getMessage() );

}

}

 

public void stopThread() {

bRun = false;

}

} // ProgressThread

 

 

// In the main function that executes the query

Statement stmt = conn.createStatement( ResultSet.TYPE\_SCROLL\_SENSITIVE,

ResultSet.CONCUR\_UPDATABLE );

 

ProgressThread pt = new ProgressThread( (ADSStatement)stmt );

pt.start();

try {

ResultSet rs = stmt.executeQuery( "SELECT \* FROM demo1000 a, demo1000 b order by 1" );

rs.close();

pt.stopThread();

 

stmt.close();

}

catch ( SQLException e ) {

System.out.println( e.getErrorCode() );

System.out.println( e.getMessage() );

}