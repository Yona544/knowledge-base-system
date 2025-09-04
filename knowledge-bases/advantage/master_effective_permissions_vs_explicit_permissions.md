Effective Permissions vs Explicit Permissions




Advantage Database Server 12  

Effective Permissions vs Explicit Permissions

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Effective Permissions vs Explicit Permissions  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Effective Permissions vs Explicit Permissions Advantage Concepts master\_Effective\_permissions\_vs\_explicit\_permissions Advantage Concepts > Advantage Functionality > Effective Permissions vs Explicit Permissions / Dear Support Staff, |  |
| Effective Permissions vs Explicit Permissions  Advantage Concepts |  |  |  |  |

A users effective permissions to a specific object in the database consist of the permissions explicitly granted to the user and the permissions derived from the user groups that the user belongs to. The concept is illustrated by the following example:

User1 is a member of GroupA

User2 is a member of GroupA and GroupB

 

GroupA has SELECT (i.e., READ) permission to Table1

GroupB has INSERT permission to Table1

 

If no permission is granted explicitly to User1 and User2, their explicit permissions to the Table1 object is none. However, their effective permissions to the Table1 object are different:

User1 has effective SELECT permission to Table1 inherited from GroupA.

User2 has effective SELECT and INSERT permissions to Table1 inherited from GroupA and GroupB respectively.

The inheritance of the permissions from the user group to specific objects is the default behavior. In rare situation, if it is desirable to prevent the inheritance, it can be achieved by revoking the users inherit permission to the specific object. Using the sample described above, if User2s inherit permission to the Table1 object has been revoked, it will have no permission to the Table1 object even though it belongs to two groups that do have permissions to Table1.