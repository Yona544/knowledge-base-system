Locking Mode




Advantage Database Server 12  

Locking Mode

Crystal Reports

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Locking Mode  Crystal Reports |  |  | Feedback on: Advantage Database Server 12 - Locking Mode Crystal Reports crystal\_Locking\_mode Advantage Crystal Reports > Configuration > Locking Mode / Dear Support Staff, |  |
| Locking Mode  Crystal Reports |  |  |  |  |

By default, the Advantage Crystal Reports Driver uses the Advantage Proprietary Locking mode. If other Advantage applications are accessing your .DBF data using compatibility locking mode, or non-Advantage applications have your .DBF data opened in a writable mode when attempting to open data files or execute reports with the Advantage Crystal Reports Driver, an error will occur when using the default proprietary locking mode. To force the Advantage Crystal Reports Driver to use the Advantage Compatible Locking mode with .DBF tables, add the following two lines to your ads.ini file:

 

 [Crystal]

 LockingMode=0 ; Proprietary locking = 1, Compatible locking = 0

If specified in the [Crystal] section of the ads.ini file, the setting will be global for use by all reports. If instead you would like to add a per-alias Locking Mode, the following syntax can be used (and often will already exist in your ads.ini file, as this is the format the Advantage Data Architect uses to store additional alias information):

 

 [<YourAliasName>\_info]

 LockingMode=proprietary

Note when using a per-alias LockingMode, the strings "proprietary" and "compatible" are used, as opposed to 1 and 0 which are used in the global [Crystal] section.

 

Note The LockingMode setting only applies to .DBF tables, not .ADT tables.