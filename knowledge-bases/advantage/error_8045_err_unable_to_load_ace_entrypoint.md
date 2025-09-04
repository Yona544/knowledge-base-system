8045 ERR\_UNABLE\_TO\_LOAD\_ACE\_ENTRYPOINT




Advantage Database Server 12  

8045 ERR\_UNABLE\_TO\_LOAD\_ACE\_ENTRYPOINT

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 8045 ERR\_UNABLE\_TO\_LOAD\_ACE\_ENTRYPOINT  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 8045 ERR\_UNABLE\_TO\_LOAD\_ACE\_ENTRYPOINT Advantage Error Guide error\_8045\_err\_unable\_to\_load\_ace\_entrypoint Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 8045 ERR\_UNABLE\_TO\_LOAD\_ACE\_ENTRYPOINT  Advantage Error Guide |  |  |  |  |

Problem: Advantage Database Server was unable to find a required entrypoint function in the dynamically loaded Advantage Client Engine library. This error is never returned to a client application; it is only logged to the Advantage error log. When Advantage Database Server starts, it attempts to load the Advantage Client Engine, which is required for replication. It then verifies that all the necessary external entrypoint functions are available. Advantage will be unable to replicate data to the target database if this occurs. If replication is enabled, though, the updates will be stored in the replication queue and will be processed when Advantage is restarted with a valid copy of the Advantage Client Engine.

Solution: Make sure that the necessary library files are available to Advantage Database Server. In Windows environments, make sure the latest versions of ACE32.DLL and AXCWS32.DLL are available. In Linux, make sure the latest libace.so.X.YY.Z is available. You will need to stop and restart Advantage Database Server in order to load the Advantage client library.