Replicating to Older Servers




Advantage Database Server 12  

Replicating to Older Servers

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Replicating to Older Servers  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Replicating to Older Servers Advantage Concepts master\_replicating\_to\_older\_servers Advantage Concepts > Advantage Functionality > Replication > Replicating to Older Servers / Dear Support Staff, |  |
| Replicating to Older Servers  Advantage Concepts |  |  |  |  |

Beginning with v11, it is possible to replicate from a newer version of the server to an older version.  For example, it is possible to replicate from v11.x to either v9.x or v10.x.  Prior to this, the target server had to be the same version as the source or newer than the source. This meant that any kind of scenario involving two way replication meant that both servers had to always be the same version. Advantage Database Server uses the Advantage Client Engine library for handling the client aspect of replicating to another server.

One of the requirements for Advantage clients is that they cannot be newer than the server to which they are communicating. This restriction was the basis for replication limitation. With v11, it is now possible to provide an older version of the Advantage Client Engine library for the replication engine to use. By default, Advantage Database Server attempts to load ACE32.DLL (or ACE64.DLL) using the default search path beginning with the default folder from which the ADS binary is loaded. To use a different Advantage client library for the replication engine, specify a value for the [REPLICATION\_LIBRARY](master_replication_library.htm) configuration parameter. Note that it may be a good idea to rename the DLL (e.g., from ace32.dll to ace329x.dll) and place it in its own folder. The reason for renaming the ACE library is to avoid problems with other features such as AEPs that may depend on the newer version of the client library.

To summarize:

|  |  |
| --- | --- |
| · | Copy the desired version of ace32.dll and axcws32.dll (or ace64.dll and axcws64.dll) to their own folder.  Rename ace32.dll to a unique name. |

|  |  |
| --- | --- |
| · | Add a string configuration parameter named [REPLICATION\_LIBRARY](master_replication_library.htm) and specify the path to the renamed client library as the value. |

Note that obvious limitations exist when replicating to an older server. It is not possible to replicate a field type introduced in the newer server to the older server. For example, it would not be possible to replicate Unicode data to a 9.x server; the server would not understand the data and the client library does not support the necessary entrypoints.