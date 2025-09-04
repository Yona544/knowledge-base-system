ODBC Data Source Entries for Linux




Advantage Database Server 12  

ODBC Data Source Entries for Linux

Advantage ODBC Driver

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ODBC Data Source Entries for Linux  Advantage ODBC Driver |  |  | Feedback on: Advantage Database Server 12 - ODBC Data Source Entries for Linux Advantage ODBC Driver odbc\_Odbc\_data\_source\_entries\_for\_linux Advantage ODBC Driver > Installation and Distribution > ODBC Data Source Entries for Linux / Dear Support Staff, |  |
| ODBC Data Source Entries for Linux  Advantage ODBC Driver |  |  |  |  |

ODBC data source entries are used by the Advantage ODBC Driver to determine certain driver behaviors and Advantage settings are stored in the odbc.ini file. The odbc.ini file must be located in the directory specified by an environment variable named ODBCINI, in the users home directory, or in the /etc directory. If located in the user home directory the odbc.ini should be named .odbc.ini (note the initial "dot"). For a list of required entries, as well as the list of optional entries and their default values see [ODBC Data Source Keys](odbc_odbc_data_source_keys.htm). All entries in the odbc.ini file are string values.

An example odbc.ini file is shown below:

;

; odbc.ini

;

[ODBC Data Sources]

Odie = Advantage ODBC Driver

 

[Odie]

Driver=/home/odbcuser/lib/libadsodbc.so.6

DataDirectory=\\AdvantageServer\data\w78p1\

Description=Advantage ODBC driver

Rows=False

MemoBlockSize=64

DefaultType=Advantage

MaxTableCloseCache=0

LOCKING=Record

CharSet=OEM

ADVANTAGELOCKING=OFF

ServerTypes=2

TableExtension=