---
title: Dotnet Adsconnection Statechange
slug: dotnet_adsconnection_statechange
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnection_statechange.htm
source: Advantage CHM
tags:
  - dotnet
checksum: f1c579035d0ff081b6bca0b6c84091c3d38d3c28
---

# Dotnet Adsconnection Statechange

AdsConnection.StateChange

AdsConnection.StateChange

Advantage .NET Data Provider

| AdsConnection.StateChange  Advantage .NET Data Provider |  |  |  |  |

Occurs when the state of the AdsConnection object changes.

public event StateChangeEventHandler StateChange;

Remarks

You can use this event to detect when a connection object is opened or closed.

Event Data

The event handler receives an argument of type StateChangeEventArgs containing data related to this event. StateChangeEventArgs contains a CurrentState property that indicates the new state of the connection object and an OriginalState property that indicates the previous state.

Example

static void OnConnectionStateChange( object sender, StateChangeEventArgs args )

{

Console.WriteLine( "Original State: " + args.OriginalState.ToString() );

Console.WriteLine( "Current State: " + args.CurrentState.ToString() );

}

 

public static void StateChangeTest()

{

try

{

AdsConnection conn = new AdsConnection( "data source = c:\\data" );

 

conn.StateChange += new StateChangeEventHandler( OnConnectionStateChange );

 

// cause event to fire for the change from Closed to Open

conn.Open();

// ...

 

// cause event to fire for the change from Open to Closed

conn.Close();

}

catch (Exception e)

{

Console.WriteLine( e.Message );

}

 

}

See Also

[AdsConnection.State](dotnet_adsconnection_state.md)
