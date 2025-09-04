Using RDDSetDefault to Specify the Advantage RDD




Advantage Database Server 12  

Using RDDSetDefault to Specify the Advantage RDD

Advantage Visual Objects and Vulcan.NET RDD

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using RDDSetDefault to Specify the Advantage RDD  Advantage Visual Objects and Vulcan.NET RDD |  |  | Feedback on: Advantage Database Server 12 - Using RDDSetDefault to Specify the Advantage RDD Advantage Visual Objects and Vulcan.NET RDD vo\_Using\_rddsetdefault\_to\_specify\_the\_advantage\_rdd Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Using RDDSetDefault to Specify the Advantage RDD / Dear Support Staff, |  |
| Using RDDSetDefault to Specify the Advantage RDD  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

To make the Advantage RDD the default RDD for your application, use the function RDDSetDefault() to specify the RDD. This function is compatible in both the object-oriented and procedural code methods.

Note The default RDD will only be used when a specific RDD is not chosen for a work area or data server.

The DBServer Editor does not allow you to automatically specify the Advantage RDD as a default RDD. You may, however, use the [DBServer Editor](vo_db_server_editor.htm) to create a class then modify it to reference the Advantage RDD.