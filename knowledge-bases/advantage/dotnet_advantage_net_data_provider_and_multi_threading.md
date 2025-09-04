Advantage .NET Data Provider and Multi-Threading




Advantage Database Server 12  

Advantage .NET Data Provider and Multi-Threading

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage .NET Data Provider and Multi-Threading  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - Advantage .NET Data Provider and Multi-Threading Advantage .NET Data Provider dotnet\_Advantage\_net\_data\_provider\_and\_multi\_threading Advantage .NET Data Provider > Developing .NET Applications > Advantage .NET Data Provider and Multi-Threading / Dear Support Staff, |  |
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