7075 The Advantage Local Server version allows a maximum of 5 users to access a file at one time.




Advantage Database Server 12  

7075 The Advantage Local Server version allows a maximum of 5 users to access a file at one time. The limit has been exceeded.

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7075 The Advantage Local Server version allows a maximum of 5 users to access a file at one time. The limit has been exceeded.  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7075 The Advantage Local Server version allows a maximum of 5 users to access a file at one time. The limit has been exceeded. Advantage Error Guide error\_7075\_the\_advantage\_local\_server\_version\_allows\_a\_maximum\_of\_5\_users\_to\_access\_a\_file\_at\_one\_time\_the\_limit\_has\_been\_exceeded\_ Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7075 The Advantage Local Server version allows a maximum of 5 users to access a file at one time. The limit has been exceeded.  Advantage Error Guide |  |  |  |  |

Problem: The maximum of five (5) licensed users for Advantage Local Server has been exceeded.

Solution 1: A maximum of five concurrent users are allowed to access the Advantage Local Server. Have any users not currently using the Advantage Local Server logout to allow access by another user. To allow more than five concurrent users, contact your Advantage Database Server reseller to expand the number of concurrent users.

Solution 2: If an application does not terminate properly and close each table it has open, the tables it had open may be left with an incorrect open count. To resolve this problem, either open and close the table from the same workstation as the application improperly terminated, or open the table exclusively from any workstation to reset the open count to one.