5054 AE\_PERMISSION\_DENIED




Advantage Database Server 12  

5054 AE\_PERMISSION\_DENIED

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5054 AE\_PERMISSION\_DENIED  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5054 AE\_PERMISSION\_DENIED Advantage Error Guide error\_5054\_ae\_permission\_denied Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5054 AE\_PERMISSION\_DENIED  Advantage Error Guide |  |  |  |  |

The command cannot be completed with the current user permissions. If using [Advantage Data Dictionary](master_advantage_data_dictionary.htm), this error is returned if the current connected user was not granted the permission to performed the specific operation. For example, when creating a new user in the database, the user performing the operation must be granted the CREATE permission for the USER object type in the database. See AdsDDGrantPermission in the Advantage Client Engine Help documentation (ACE.hlp or ace.htm) for additional information.

Note If using the Advantage TDataSet Descendant TAdsQuery component, verify the RequestLive property is set to True.