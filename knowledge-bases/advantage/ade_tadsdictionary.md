TAdsDictionary




Advantage Database Server 12  

TAdsDictionary

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDictionary  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDictionary Advantage TDataSet Descendant ade\_Tadsdictionary Advantage TDataSet Descendant > Advantage Components > TAdsDictionary / Dear Support Staff, |  |
| TAdsDictionary  Advantage TDataSet Descendant |  |  |  |  |

|  |  |  |
| --- | --- | --- |
| [Properties](ade_tadsdictionary_properties.htm) | [Methods](ade_tadsdictionary_methods.htm) | [Events](ade_tadsdictionary_events.htm) |

 

The TAdsDictionary component has been deprecated.  The majority of the functionality this component provides can be retrieved in an easier fashion through the use of the system tables ([system.dictionary](master_system_dictionary.htm), [system.tables](master_system_tables.htm), etc.) and canned stored procedures ([sp\_ModifyDatabase](master_sp_modifydatabase.htm), [sp\_ModifyTableProperty](master_sp_modifytableproperty.htm), etc).

Unit

AdsDictionary

Description

Use TAdsDictionary to gain administrative access to an Advantage Data Dictionary. You have the ability to add and delete tables, set table, and record level constraints, construct Referential Integrity, create views, and get all available information about the data dictionary.

Delphi 6 and greater If using the default login dialog, you must add the DBLogDlg (or QDBLogDlg if using CLX) unit to the uses clause of the unit that declares the connection component. See the Delphi "Controlling Server Login" documentation for more details.