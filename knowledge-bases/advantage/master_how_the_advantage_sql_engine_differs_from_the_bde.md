How the Advantage SQL Engine Differs from the BDE




Advantage Database Server 12  

How the Advantage SQL Engine Differs from the BDE

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| How the Advantage SQL Engine Differs from the BDE  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - How the Advantage SQL Engine Differs from the BDE Advantage SQL Engine master\_How\_the\_advantage\_sql\_engine\_differs\_from\_the\_bde Advantage SQL > SQL Functionality > How the Advantage SQL Engine Differs from the BDE / Dear Support Staff, |  |
| How the Advantage SQL Engine Differs from the BDE  Advantage SQL Engine |  |  |  |  |

The following table shows how the Advantage SQL engine differs from Borland Database Engine (BDE) Local SQL.

|  |  |  |
| --- | --- | --- |
| SQL Construct | BDE Local SQL | Advantage SQL Engine |
| Concatenation Operator | Supported by the "||" operator. Strings are automatically trimmed. | Supported by the "+" operator. Strings are not automatically trimmed. |
| SOME keyword | Supported | Not Supported |
| FROM | Support BDE alias in the FROM clause. For example: FROM ":DBDemos:Orders". | Does not support database alias in the FROM clause. |
| ORDER BY | Support ORDER BY using ASCENDING/DESCENDING keywords. | Support ORDER BY using ASC/DESC keywords. |
| Quoted Strings | Supports single and double quotes interchangeably. | Single quotes are used for character string literals. Double quotes and square brackets are used for delimiting table and field names. |
| Comparison to NULL | "field = NULL" is supported. | Supported through the standard syntax "field IS NULL". |
| Not Equal Comparison | Supports "!=" operator | Does not support "!=" operator. Only "<>" operator is supported. |
| Named parameter | Any character except white spaces. | If the name is not quoted with ", only characters A-Za-z and \_ is allowed in the name. If other character is to appear in the parameter name, the name must be quoted with ". For example, :"Last+First" |
| Numeric value | Can be enclosed in quotes. For example: IntField = '2' or IntField = 3 | Must not be enclosed in quotes. For example:  IntField = 2 or IntField = 3 |