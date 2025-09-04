Comments




Advantage Database Server 12  

Comments

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Comments  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Comments Advantage SQL Engine master\_Comments Advantage SQL > Supported SQL Grammar > Comments / Dear Support Staff, |  |
| Comments  Advantage SQL Engine |  |  |  |  |

Comment text can be embedded in the SQL statements. Advantage SQL engine supports 3 types of comment text:

|  |  |
| --- | --- |
| · | Comments starting with the "/\*" delimiter and ending with the "\*/" delimiter. Example: |

SELECT Lastname, Firstname FROM Employee ORDER BY 1, 2 /\* sort on the lastname and firstname \*/

|  |  |
| --- | --- |
| · | Comments starting with the "--" delimiter and ending at the next new-line character or at the end of the statement. Example: |

SELECT \* FROM Employees -- Employee information table

WHERE Lastname > 'W'

|  |  |
| --- | --- |
| · | Comments starting with the "//" delimiter and ending at the next new-line character or at the end of the statement. Example: |

SELECT \* FROM Employees // Employee information table

WHERE Lastname > 'W'