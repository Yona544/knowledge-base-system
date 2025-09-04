Understanding and Using Data Dictionaries




Advantage Database Server 12  

     Understanding and Using Data Dictionaries

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Understanding and Using Data Dictionaries  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Understanding and Using Data Dictionaries Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Understanding\_and\_Using\_Data\_Dictionaries Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 4 - Understanding Dictionaries > Understanding and Using Data Dictionaries / Dear Support Staff, |  |
| Understanding and Using Data Dictionaries  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

A data dictionary is a special file that serves as the sole access point for database tables. Although the use of a data dictionary is optional, it is hard to imagine anyone creating a serious database without one. This is because a data dictionary provides access to many of the Advantage Database Server's most powerful and advanced features.

This chapter achieves two goals. First, it provides you with an overview of data dictionaries, including a tour of the features that they make available. The second purpose of this chapter is to show you how to set up a data dictionary with tables and security. This dictionary will be used in many of the later chapters of this book to demonstrate some of Advantage's most advanced features, including stored procedures, replication, and triggers.