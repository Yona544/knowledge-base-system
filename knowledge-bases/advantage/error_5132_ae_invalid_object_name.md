5132 AE\_INVALID\_OBJECT\_NAME




Advantage Database Server 12  

5132 AE\_INVALID\_OBJECT\_NAME

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5132 AE\_INVALID\_OBJECT\_NAME  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5132 AE\_INVALID\_OBJECT\_NAME Advantage Error Guide error\_5132\_ae\_invalid\_object\_name Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5132 AE\_INVALID\_OBJECT\_NAME  Advantage Error Guide |  |  |  |  |

The specified database object name is not valid.

If you are getting this error when attempting to use the [Advantage Web Administrator utility](web_administrator_utility.htm) to view database and server information, it could be because the dictionary that you are connecting to is not a [root dictionary](master_root_dictionary.htm).  The web administrator utility uses system procedure requests to retrieve information from the server, and system procedures through the Advantage Web Platform can only be run when connected to the root dictionary. If it is not a root dictionary, the web platform attempts to treat the system procedure name as a table object in the dictionary, which results in a 5132 error.