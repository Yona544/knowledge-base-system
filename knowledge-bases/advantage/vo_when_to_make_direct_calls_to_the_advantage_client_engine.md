When to Make Direct Calls to the Advantage Client Engine




Advantage Database Server 12  

When to Make Direct Calls to the Advantage Client Engine

Advantage Visual Objects and Vulcan.NET RDD

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| When to Make Direct Calls to the Advantage Client Engine  Advantage Visual Objects and Vulcan.NET RDD |  |  | Feedback on: Advantage Database Server 12 - When to Make Direct Calls to the Advantage Client Engine Advantage Visual Objects and Vulcan.NET RDD vo\_When\_to\_make\_direct\_calls\_to\_the\_advantage\_client\_engine Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Directly Accessing the Advantage Client Engine > When to Make Direct Calls to the Advantage Client Engine / Dear Support Staff, |  |
| When to Make Direct Calls to the Advantage Client Engine  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Most likely you will not need to access the Advantage Client Engine directly. On occasion, however, when developing Advantage-enabled Visual Objects or Vulcan.NET applications, you may find that the functionality provided by the Advantage RDD is not exactly what you need.

It is sometimes easier to call the Advantage Client Engine directly to obtain specific information. For example, the Advantage Client Engine API AdsMgGetUserNames() can report all users that are connected or have a certain file open.

The Advantage RDDs wrap most functionality provided by the Advantage Client Engine. Only in rare circumstances will it be necessary to circumvent the RDD methods and call the engine directly. Because the Advantage Client Engine API is the lowest interface that can be used to access the Advantage functionality, it is more versatile and more complex.

See Also

[How to use the Advantage Client Engine](vo_how_to_use_the_advantage_client_engine.htm)