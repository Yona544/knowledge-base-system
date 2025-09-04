Creating a Data Dictionary




Advantage Database Server 12  

     Creating a Data Dictionary

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating a Data Dictionary  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Creating a Data Dictionary Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_a\_Data\_Dictionary\_1 Advantage Developer's Guide > Part II - Advantage SQL > Chapter 14 - System Management and Metadata > Creating a Data Dictionary / Dear Support Staff, |  |
| Creating a Data Dictionary  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You create a data dictionary using the CREATE DATABASE statement. At a minimum, you must supply the name of the data dictionary you are creating. For example, the following statement creates a data dictionary named NEW.ADD:

CREATE DATABASE "NEW.ADD"

This statement created a data dictionary in the directory associated with the connection over which this query is executed. If you are connected to a data dictionary, this will be the data dictionary's default directory. If you are using a free table connection, it will be the directory associated with those free tables.

To specify where the data dictionary is created, qualify the data dictionary name with a valid path. For example, if you want to create NEW.ADD on the DATASERV computer in the directory named AppData in the C$ share, your CREATE DATABASE statement might look something like the following:

CREATE DATABASE "\\DATASERV\C$\AppData\NEW.ADD"

CREATE DATABASE supports three options when creating a new data dictionary. You can assign a password to the ADSSYS user name, you can attach a description to the data dictionary, and you can choose to encrypt the data dictionary. The following statement demonstrates the use of these three options:

CREATE DATABASE "\\DATASERV\C$\AppData\NEW.ADD"  
  PASSWORD 'password'  
  DESCRIPTION 'A data dictionary created using SQL'  
  ENCRYPT True

There is no SQL DROP statement for destroying a data dictionary. If you need to destroy a data dictionary, you need to use your client application development environment's capabilities to delete the data dictionary's .ADD, .AI, and .AM files. However, if there are tables bound to that data dictionary that you want to keep, be sure to release those tables prior to deleting the data dictionary's files.

   
NOTE: You do not need an administrative connection to create a data dictionary.