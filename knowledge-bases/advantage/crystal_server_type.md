Server Type




Advantage Database Server 12  

Server Type

Crystal Reports

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Server Type  Crystal Reports |  |  | Feedback on: Advantage Database Server 12 - Server Type Crystal Reports crystal\_Server\_type Advantage Crystal Reports > Configuration > Server Type / Dear Support Staff, |  |
| Server Type  Crystal Reports |  |  |  |  |

The Advantage Crystal Reports driver uses remote server connections by default. If you try to use the driver and you do not have the Advantage Database Server installed, you will get 6060 or 6024 errors when trying to connect to your database.

To change the default server type, specify an ADS\_SERVER\_TYPE value in the "settings" section of the ads.ini file.

For example, to set the server type to local server, you would modify your ads.ini file to include the following:

[SETTINGS]

ADS\_SERVER\_TYPE = 1

See [ads.ini File Support](master_ads_ini_file_support.htm) for details on ads.ini settings and valid values for the ADS\_SERVER\_TYPE setting.