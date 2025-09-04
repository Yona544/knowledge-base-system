---
title: Dotnet Adscommand Progressmessage
slug: dotnet_adscommand_progressmessage
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_progressmessage.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 23acbe25028a7604406e40df2b4b3de062ac622e
---

# Dotnet Adscommand Progressmessage

AdsCommand.ProgressMessage

AdsCommand.ProgressMessage

Advantage .NET Data Provider

| AdsCommand.ProgressMessage  Advantage .NET Data Provider |  |  |  |  |

Occurs when Advantage .NET Data Provider receives a progress report from the Advantage Database Server on a currently executing SQL statement.

public event AdsInfoMessageEventHandler ProgressMessage;

Remarks

This event provides the ability for an application to register a delegate function to receive progress callbacks during SQL statement execution. This can provide equivalent functionality to the AdsCommand.Progress property but does not require a separate thread to monitor the progress. The provider will fire an event each time it receives a progress update from the server, which is generally every 2 seconds.

Note The delegate (event handler) function should not perform any time-consuming tasks when using Advantage Local Server connections. With Advantage Local Server, the event callback is run on the same thread that is executing the SQL statement, which means that the progress is effectively halted until the delegate function returns. If this is an issue, then the AdsCommand.Progress property should be used instead and accessed from a separate thread.

Event Data

The event handler receives an argument of type AdsInfoMessageEventArgs containing data related to this event. The relevant data is the Number property, which contains the estimated percentage of the execution progress.

Example

// Provide an event handler for InfoMessage events

protected static void OnProgressMessage( object sender, AdsInfoMessageEventArgs args )

{

// Do something with the information

Console.WriteLine( "Progress: " + args.Number.ToString() );

 

// Cancel the execution based on some decision may look like this:

// if ( <cancelcondition> )

// ((AdsCommand)sender).Cancel();

}

 

static public void ProgressMessageTest()

{

AdsConnection conn = null;

AdsCommand cmd = null;

AdsTransaction txn = null;

 

try

{

// get a connection and begin a transaction

conn = new AdsConnection( "data source = c:\\data;" );

conn.Open();

txn = conn.BeginTransaction();

 

// use a statement that takes a while to finish

cmd = new AdsCommand( "UPDATE bigtable SET deptnum = 7", conn );

 

// set command so that it will not time out

cmd.CommandTimeout = 0;

 

// Add our delegate function as a listener for progress events

cmd.ProgressMessage += new AdsInfoMessageEventHandler( OnProgressMessage );

 

// Execute the statement.

Console.WriteLine( cmd.ExecuteNonQuery() + " Records Affected" );

 

// Completed without being cancelled

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

[Progress](dotnet_adscommand_progress.md)

[AdsInfoMessageEventArgs](dotnet_adsinfomessageeventargs.md)
