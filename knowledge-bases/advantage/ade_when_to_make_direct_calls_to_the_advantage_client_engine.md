When to Make Direct Calls to the Advantage Client Engine




Advantage Database Server 12  

When to Make Direct Calls to the Advantage Client Engine

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| When to Make Direct Calls to the Advantage Client Engine  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - When to Make Direct Calls to the Advantage Client Engine Advantage TDataSet Descendant ade\_When\_to\_make\_direct\_calls\_to\_the\_advantage\_client\_engine Advantage TDataSet Descendant > Directly Accessing the Advantage Client Engine > When to Make Direct Calls to the Advantage Client Engine / Dear Support Staff, |  |
| When to Make Direct Calls to the Advantage Client Engine  Advantage TDataSet Descendant |  |  |  |  |

Most likely you will not need to access the Advantage Client Engine directly. On occasion, when developing Advantage-enabled Delphi applications, you may find that the functionality provided by the Advantage TDataSet Descendant is not exactly what you need.

It is sometimes easier to call the Advantage Client Engine directly to modify environmental settings such as the Advantage server type when building DLLs or other non-visual applications. For example, calling the Advantage Client Engine API AdsSetServerType() to change the Advantage server type may be simpler than creating an instance of a TAdsSettings class and changing the AdsServerTypes property on the fly.

Using the Advantage Client Engine from within an Advantage-enabled Delphi application is equivalent to calling the BDE directly from a regular Delphi application. Since Delphi version 3, this practice is almost never necessary.

The TAdsTable methods and properties wrap most functionality provided by the Advantage Client Engine. Only in rare circumstances will it be necessary to circumvent the component methods and call the engine directly. Since the Advantage Client Engine API is the lowest interface that can be used to access the Advantage functionality, it is more versatile and more complex.