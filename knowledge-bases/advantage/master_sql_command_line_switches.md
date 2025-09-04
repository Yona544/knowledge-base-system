Command Line Switches




Advantage Database Server 12  

Command Line Switches

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Command Line Switches |  |  | Feedback on: Advantage Database Server 12 - Command Line Switches master\_sql\_Command\_Line\_Switches Advantage SQL > Command Line Utility > Command Line Switches / Dear Support Staff, |  |
| Command Line Switches |  |  |  |  |

The following switches are supported when starting the asqlcmd.exe utility. The switches are case sensitive.

-CS connection\_string

 

 Connecting to the Advantage Database Server or Advantage Local Server using the options specified in the connection\_string. See [AdsConnect101](ace_adsconnect101.htm) for format of the connection string. this switch overwrite the -S, -U and -P switches.

 -S [protocol:]connection\_path

 

 Connecting to the Advantage Database Server (ADS) or Advantage Local Server (ALS) at the specified path using the optional protocol. The valid protocols are: TCP (connecting to ADS using TCP/IP protocol), UDP (connecting to ADS using UDP/IP protocol) or ALS (connecting using Advantage local server DLL). If no protocol is specified, the default is to attempt to connect to remote server using all available protocol. This switch is ignored if the -CS switch is used.

 -U login\_id

 -P password

 

 If using the -S switch to connect to an Advantage Data Dictionary, these two switches are used to specify the user name and password for authentication. These switches are ignored if the -CS switch is used

-q "cmdline query"

-Q "cmdline query" and exit

 Executes the query or script specified by the "cmdline query" after making successful connection the Advantage server. The "cmdline\_query" should contain SQL statement only. It is sent to the server directly with no processing done by the command line utility. With the -q option, the utility will stay in interactive mode after executing the query. If -Q is used, the utility will exit after finish executing the query and all script files specified with the -i switches.

-i input\_files

 

 Process command line scripts in the input\_files. The script files are processed after the executing the queries from the -q/-Q switches. Multiple files may be included either using comma separated list or multiple -i switches. The utility will open all files first before processing. If there is a failure when opening a file, an error will be returned. An implicit [GO](master_sql_command_line_supported_commands.htm) will be executed to  send all SQL statements in the statement cache to the server for processing. The following samples are all equivalent:

 

 asqlcmd.exe -i file1.sql -i file2.sql -i file3.sql

 asqlcmd.exe -i file1.sql,file2.sql -i file3.sql

 asqlcmd.exe -i file1.sql,file2.sql,file3.sql

 The -i switch will cause the program to exit after all files are processed. The utility will not go into interactive mode if -i switch is used.

-?

 show usage. Print a brief description of these switches to the output.

Examples

rem Using the connection string option, execute the query and done

asqlcmd.exe -CS "Data Source=d:\mydata\main.add; ServerType=Remote; User ID=user1; password=sample" -Q "SELECT \* FROM table1"

rem Using the connection path option, execute the query and stay in interactive mode

asqlcmd.exe -S ALS:d:\mydata\main.add -U user1 -P sample -q "SELECT \* FROM table1"

rem Using the connection path option, and process the script files after making the connection.

rem The program will terminate after processing all files

asqlcmd.exe -S ALS:d:\mydata\main.add -U user1 -P sample -i myscript.sql

See Also

[Command Line Utility Commands](master_sql_command_line_supported_commands.htm)