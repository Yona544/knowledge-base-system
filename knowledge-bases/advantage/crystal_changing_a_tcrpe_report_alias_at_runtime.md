Changing a TCrpe Report Alias at Runtime




Advantage Database Server 12  

Changing a TCrpe Report Alias at Runtime

Crystal Reports

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Changing a TCrpe Report Alias at Runtime  Crystal Reports |  |  | Feedback on: Advantage Database Server 12 - Changing a TCrpe Report Alias at Runtime Crystal Reports crystal\_Changing\_a\_tcrpe\_report\_alias\_at\_runtime Advantage Crystal Reports > Using the Advantage Crystal Reports Driver > Changing a TCrpe Report Alias at Runtime > Changing a TCrpe Report Alias at Runtime / Dear Support Staff, |  |
| Changing a TCrpe Report Alias at Runtime  Crystal Reports |  |  |  |  |

The following code is an example of how to change the alias a report is using at run-time when using Crystals Delphi/Kylix/C++Builder TCrpe component:

// show report with alias it was designed with

crpe1.DiscardSavedData;

crpe1.show;

 

// set a different alias

crpe1.closejob;

crpe1.Connect.servername := 'worktest';

 

// show the report with the new alias

crpe1.DiscardSavedData;

crpe1.show;