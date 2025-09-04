---
title: Master Sql Command Line Supported Commands
slug: master_sql_command_line_supported_commands
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sql_command_line_supported_commands.htm
source: Advantage CHM
tags:
  - master
checksum: 174b8aa865a16783da378a2c46a93d0199a4de01
---

# Master Sql Command Line Supported Commands

Supported Commands

Supported Commands

| Supported Commands |  |  |  |  |

The SQL command line utility supports a set of commands in the script file or during interactive session. These commands are case insensitive; however, each command must be on separate line and must start at the beginning of the line. All commands are prefixed with the colon, ':', character except the GO command. The commands are executed immediately and not placed in the statement cache.

GO [count]

 The SQL statements are cache in the statement buffer until the GO command is encountered, and then they are sent to the server in one batch. The optional count determines the number of times the batch will be executed. If there are "SELECT ..." statements in the batch, the server may execute the "SELECT ..." statement only when it is the last statement in the batch. If the last statement in the batch results in a cursor being returned, the complete result set is printed to the output.

|  | Note: In interactive mode, GO does not clear the statement cache. Only the :reset command clears the statement cache. This makes it possible to examine the statements using the :list command after failure. In batch mode (running from script file, GO does clear the statement cache. |

:reset

 Clear the statement cache. The content of the statement cache are discarded without being executed.

:list

 Print the content of the statement cache to the output.

:connect [protocol:]Path[;username[;password]]

 Make connection to server at the specified path using the optional protocol, user name and password. The valid protocols are: TCP (connecting to ADS using TCP/IP protocol), UDP (connecting to ADS using UDP/IP protocol) or ALS (connecting using Advantage local server DLL). If no protocol is specified, the default is to attempt to connect to remote server using all available protocol.

 Example:

 

 :connect ALS:d:\mydata

 :connect d:\mydata;user1;sample\_password

:cs ConnectionString

 Make connection to the Advantage Database Server or Advantage Local Server using options specified in the connection string. See [AdsConnect101](ace_adsconnect101.md) for connection string format.

 Example:

 

 :cs Data Source=d:\mydata\main.add; ServerType=Remote; User ID=user1; password=sample

 :cs Data Source=d:\mydata; ServerType=Local;

:r <filename>

 

 Load addition batch commands from the specified file. The statements in the file are load and processed immediately. Any GO command in the file will cause statements in the cache to be executed. No implicit GO will be execute after loading the file. SQL statements from the file will stay in the statement cache if GO is not the last statement in the statement cache until a GO command is issued.

:quit

 Exit the program. All unexecuted SQL statement in the statement cache are discarded.

:help

 List the available asqlcmd commands with a short description of each command.

Important Note: When entering SQL statement in either interactive mode or in command script files, each SQL statement should be terminated with a semi-colon. This is necessary even if the statement is the last statement in a script file because execution is not immediate and additional SQL statements may be placed into the statement cache from other files. All SQL statements in the cache are sent to the server in one batch. Advantage SQL engine use semi-colon to determine the end of SQL statement.

Note: The command line utility commands should not be terminated with semi-colon.

Sample Command Script File or Interactive Session Sequence

:connect ALS:d:\mydata

UPDATE table1 SET quantity = quantity + 1 WHERE id = 2;

SELECT \* FROM table1;

GO

INSERT INTO table2 ( id, name ) VALUES ( 22, 'abc' );

GO

:r myscript.sql

GO

:quit

See Also

[Command Line Utility Switches](master_sql_command_line_switches.md)
