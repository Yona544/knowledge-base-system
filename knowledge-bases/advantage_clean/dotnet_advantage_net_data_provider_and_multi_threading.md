---
title: Dotnet Advantage Net Data Provider And Multi Threading
slug: dotnet_advantage_net_data_provider_and_multi_threading
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_advantage_net_data_provider_and_multi_threading.htm
source: Advantage CHM
tags:
  - dotnet
checksum: bad6eb9f940493c80105463c8fb3ae99bce9b4c1
---

# Dotnet Advantage Net Data Provider And Multi Threading

Advantage .NET Data Provider and Multi-Threading

Advantage .NET Data Provider and Multi-Threading

Advantage .NET Data Provider

| Advantage .NET Data Provider and Multi-Threading  Advantage .NET Data Provider |  |  |  |  |

In general, the .NET objects and object members are not thread-safe. You can use the Advantage .NET Data Provider objects in a multi-threaded environment, but you must protect against concurrent access. For example, if your application creates an AdsDataReader object and then accesses the same object instance from two different threads concurrently without any locking, the results are undefined. It is necessary for your application to use locking to control concurrent access to these objects.

The following example, shows a simple example of the C# lock statement, which marks a statement block as a critical section.

public void DoSomething( AdsDataReader reader )

{

lock ( reader )

{

if ( reader.Read() )

{

// Do something with the data

}

}

}
