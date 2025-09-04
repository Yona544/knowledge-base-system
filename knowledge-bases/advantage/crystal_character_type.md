Character Type




Advantage Database Server 12  

Character Type

Crystal Reports

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Character Type  Crystal Reports |  |  | Feedback on: Advantage Database Server 12 - Character Type Crystal Reports crystal\_Character\_type Advantage Crystal Reports > Configuration > Character Type / Dear Support Staff, |  |
| Character Type  Crystal Reports |  |  |  |  |

By default, the Advantage Crystal Reports Driver uses the ADS\_ANSI character type when opening .DBF tables. To force the Advantage Crystal Reports Driver to use the ADS\_OEM character type, add the following two lines to your ads.ini file:

 [Crystal]

 CharType=2 ; ADS\_ANSI=1 ADS\_OEM=2

If specified in the [Crystal] section of the ads.ini file, the setting will be global for use by all reports. If instead you would like to add a per-alias Character Type, the following syntax can be used (and often will already exist in your ads.ini file, as this is the format the Advantage Data Architect uses to store additional alias information):

 

 [<YourAliasName>\_info]

 CharType=ansi

Note when using a per-alias CharType, a string format is used, as opposed to 1 and 2 which are used in the global [Crystal] section.