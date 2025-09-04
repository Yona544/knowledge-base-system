Using SQL to Retrieve Metadata




Advantage Database Server 12  

Using SQL to Retrieve Metadata

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using SQL to Retrieve Metadata  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Using SQL to Retrieve Metadata Advantage SQL Engine master\_Using\_sql\_to\_retrieve\_metadata Advantage SQL > System Views > Using SQL to Retrieve Metadata / Dear Support Staff, |  |
| Using SQL to Retrieve Metadata  Advantage SQL Engine |  |  |  |  |

Database information is available through system views that can be accessed using SQL statements. All system views are automatically available when the Advantage Data Dictionary is created. System views are static and can be used in the same manner as views created by the administrative user. All users have read permissions for system views.

To access a system, views prefix the view name with "system" using dot notation. For example, for a list of all system views, the following SQL statement would be used:

SELECT \* FROM system.objects

Some of the values returned in system views are a numeric representation of some constant value. For example, the table type is returned as an integer with the following possible values:

ADS\_NTX = 1

ADS\_CDX = 2

ADS\_ADT = 3

ADS\_VFP = 4

The values of these numeric constants, often helpful in determining what functionality the property provides, can be found in the Advantage Client Engine (ACE) headers (ace.h, ace.pas) or in the dictionary-specific API documentation.