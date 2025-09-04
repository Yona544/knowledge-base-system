System Management and Metadata




Advantage Database Server 12  

     System Management and Metadata

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| System Management and Metadata  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      System Management and Metadata Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_System\_Management\_and\_Metadata Advantage Developer's Guide > Part II - Advantage SQL > Chapter 14 - System Management and Metadata > System Management and Metadata / Dear Support Staff, |  |
| System Management and Metadata  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

This chapter concludes the discussion of Advantage SQL with a look at the SQL statements and stored procedures that permit you to create and manage data dictionaries and their related objects. This discussion begins with a look at the system tablesspecial result sets that permit you to quickly obtain information about your data dictionaries. Next, our attention turns to SQL statements that you use to create, destroy, and manage access rights to data dictionaries and their objects. These include the CREATE, DROP, GRANT, and REVOKE statements.

Finally, this chapter discusses a collection of system stored procedures that can be executed using Advantage. You use these system stored procedures to inspect information about server usage and manage data dictionaries and the objects they contain (some even apply to free tables). Importantly, these system stored procedures provide you with capabilities that are not supported by other SQL statements.

This chapter also contains a number of tables that list values that are used in the system tables and system stored procedures. These tables are based on the values that apply to Advantage 8.1. If you are working with a version of Advantage later than 8.1, there may be additional valid values for the listed value categories.

Also, some of these tables associate a name with each code. These names are very similar to those used when you program to the ACE (Advantage Client Engine) API. In those cases, names are variable names that are defined in the header file, VB module, or Delphi unit that you add to your programming project when using the ACE API. See the appropriate source file (ace.h, ace.pas, and so on) that comes with Advantage for a complete list of variable names and values.