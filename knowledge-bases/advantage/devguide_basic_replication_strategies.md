Basic Replication Strategies




Advantage Database Server 12  

 

     Basic Replication Strategies

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Basic Replication Strategies  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -       Basic Replication Strategies Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Basic\_Replication\_Strategies Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 10 - Replication > Basic Replication Strategies / Dear Support Staff, |  |
| Basic Replication Strategies  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Replication can be quite simple or it can be complex. Which it will be depends on the goal you are attempting to achieve through replication.

If you are simply trying to maintain an up-to-date, offsite copy of your records, replication is pretty simple. On the other hand, if you are trying to coordinate updates from multiple satellite databases while maintaining a master central database, the architecture can be pretty complex.

In most cases, however, replication strategies can be reduced down to three basic architectures. These are unidirectional, bi-directional, and spoke and hub.

While these three approaches represent alternative ways of configuring replication, they are not mutually exclusive. Specifically, based on your needs, your replication strategy might employ a combination of two or all three of these strategies.

Nonetheless, each of these strategies represents a combination of requirements and benefits. As a result, each of them will be considered separately in the following sections.