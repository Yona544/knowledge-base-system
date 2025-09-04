AX\_SetSQLTablePasswords()




Advantage Database Server 12  

AX\_SetSQLTablePasswords()

Advantage Visual Objects and Vulcan.NET RDD

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AX\_SetSQLTablePasswords()  Advantage Visual Objects and Vulcan.NET RDD |  |  | Feedback on: Advantage Database Server 12 - AX\_SetSQLTablePasswords() Advantage Visual Objects and Vulcan.NET RDD vo\_Ax\_setsqltablepasswords\_ Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Advanced  Functions > AX\_SetSQLTablePasswords() / Dear Support Staff, |  |
| AX\_SetSQLTablePasswords()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Sets passwords for encrypted tables for use with the AXSQL RDDs.

Syntax

AX\_SetSQLTablePasswords ( [<aPasswords>] )

|  |  |
| --- | --- |
| <aPasswords> | A two dimensional array containing table/password string pairs. For example: {{ "customers", "password" }} or {{ "employees", "password1" }, {"accounts", "password2" }} |

Description

Sets the table passwords for any encrypted tables used in an SQL query. Once set, all subsequent queries will use the provided passwords. To un-set the passwords, simply call the function with an empty array. For example:

AX\_SetSQLTablePasswords( {} )

If the statement handle was created on a database connection, setting the encryption password for database tables is ignored. The database tables encryption password is stored in the database and automatically available to the authenticated users.

See Also

[AdsStmtSetTablePassword](ace_adsstmtsettablepassword.htm)