Collation




Advantage Database Server 12  

Collation

Crystal Reports

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Collation  Crystal Reports |  |  | Feedback on: Advantage Database Server 12 - Collation Crystal Reports crystal\_Collation Advantage Crystal Reports > Configuration > Collation / Dear Support Staff, |  |
| Collation  Crystal Reports |  |  |  |  |

The Collation setting can be used to specify both a Character Type and the Unicode locale in a single setting. To specify a global collation for the Advantage Crystal Reports Driver to use, add the following two lines to your ads.ini file (specifying any valid character type and Unicode locale):

 

 [Crystal]

 Collation=ansi:en\_US

If specified in the [Crystal] section of the ads.ini file, the setting will be global for use by all reports. If instead you would like to add a per-alias setting, the following syntax can be used (and often will already exist in your ads.ini file, as this is the format the Advantage Data Architect uses to store additional alias information):

 

 [<YourAliasName>\_info]

 Collation=oem:de\_DE