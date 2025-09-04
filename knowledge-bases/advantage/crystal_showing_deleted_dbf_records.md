Showing Deleted DBF Records




Advantage Database Server 12  

Showing Deleted DBF Records

Crystal Reports

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Showing Deleted DBF Records  Crystal Reports |  |  | Feedback on: Advantage Database Server 12 - Showing Deleted DBF Records Crystal Reports crystal\_Showing\_deleted\_dbf\_records Advantage Crystal Reports > Configuration > Showing Deleted DBF Records / Dear Support Staff, |  |
| Showing Deleted DBF Records  Crystal Reports |  |  |  |  |

The Advantage Crystal Reports Driver filters out deleted DBF records by default. To force the driver to show deleted records, add the following two lines to your ads.ini file:

 [Crystal]

 ShowDeleted=1

If specified in the [Crystal] section of the ads.ini file, the setting will be global for use by all reports. If instead you would like to add a per-alias ShowDeleted setting, the following syntax can be used (and often will already exist in your ads.ini file, as this is the format the Advantage Data Architect uses to store additional alias information):

 

 [<YourAliasName>\_info]

 ShowDeleted=yes

Note when using a per-alias ShowDeleted setting, the strings "yes" and "no" are used, as opposed to 1 and 0 which are used in the global [Crystal] section.

Note This setting is only available in Crystal version 9 and newer.