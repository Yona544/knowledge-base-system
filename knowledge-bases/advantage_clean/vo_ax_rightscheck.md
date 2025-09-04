---
title: Vo Ax Rightscheck
slug: vo_ax_rightscheck
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: vo_ax_rightscheck.htm
source: Advantage CHM
tags:
  - vo
checksum: 17028c23421f471df61bffd4997bc006a68920de
---

# Vo Ax Rightscheck

AX\_RightsCheck()

AX\_RightsCheck()

Advantage Visual Objects and Vulcan.NET RDD

| AX\_RightsCheck()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Sets the security method used to open or create files.

Beginning with version 10.0, the client no longer performs rights checking by default. See [Check Rights](master_check_rights.md).

Syntax

AX\_RightsCheck( [.T.|.F.] ) -> logical

 

[.T.|.F.] A logical value used to set the Advantage security methods.

Returns

If no parameter is passed to AX\_RightsCheck(), then returns the current Advantage security method, (i.e., .T. for security based on file/directory rights or .F. for security based on Advantage application access.) If a parameter is passed to AX\_RightsCheck(), then returns previous security setting.

Description

AX\_RightsCheck(.T.) causes any newly opened work areas to use the file/directory rights form of security. That is, it verifies that the user has the necessary access rights before allowing the user to create or open the specified file. This is the default.

AX\_RightsCheck(.F.) causes any newly opened work areas to access files through the Advantage server without checking file/directory rights. This allows the network administrator to "hide" Xbase data files from users who are not accessing data through an Advantage application. The Xbase data is secure by removing all the appropriate access rights to the directories in which the data files are located. Only Advantage applications using this security method may access the data files. The Advantage server will create, open, and/or update these "hidden" files with its Advantage server "supervisor" privileges.

Note A change in the AX\_RightsCheck() setting only affects those work areas opened or created AFTER the AX\_RightsCheck() setting is changed. Thus, the method of security can be set on a per work area basis.

Object-oriented Example

See [CLASS AxDBServer](vo_class_axdbserver.md) for code sample for the AxDBServer class.

| // Assume user does not have READ and WRITE priviledges to the |
| // x:\norights directory but has sufficient rights to the |
| // x:\hasright directory. |
| AX\_RightsCheck(.T.)  // Obey file server rights |
| oDB1 := DBServer{ "x:\hasright\FILE1", .F., .F., "DBFNTX" } // Will succeed |
| oDB2 := DBServer{ "x:\hasright\FILE2", .F., .F., "DBFNTXAX" } // Will succeed |
| oDB3 := DBServer{ "x:\noright\FILE3", .F., .F., "DBFNTX" }  // Will fail |
| oDB4 := DBServer{ "x:\noright\FILE4", .F., .F., "DBFNTXAX" } // Will fail |
| // Ignore file server rights. Hides files from non-Advantage workareas |
| AX\_RightsCheck(.F.) |
| oDB1 := DBServer{ "x:\hasright\FILE1", .F., .F., "DBFNTX" } // Will succeed |
| oDB2 := DBServer{ "x:\hasright\FILE2", .F., .F., "DBFNTXAX" } // Will succeed |
| oDB3 := DBServer{ "x:\noright\FILE3", .F., .F., "DBFNTX" } // Will fail |
| oDB4 := DBServer{ "x:\noright\FILE4", .F., .F., "DBFNTXAX" } // WILL SUCCEED! |

Procedural Example

| // Assume user does not have READ and WRITE priviledges to the |
| // X:\NORIGHTS directory but has sufficient access rights to the |
| // X:\HASRIGHT directory. |
| AX\_RightsCheck(.T.) // Obey file server rights |
| USE X:\HASRIGHT\FILE1.DBF VIA "DBFNTX" // Will succeed |
| USE X:\HASRIGHT\FILE2.DBF VIA "DBFNTXAX" // Will succeed |
| USE X:\NORIGHTS\FILE3.DBF VIA "DBFNTX" // Will fail |
| USE X:\NORIGHTS\FILE4.DBF VIA "DBFNTXAX" // Will fail |
| CLOSE ALL |
| // Ignore file server rights. Effectively hides files from  // non- Advantage workareas |
| AX\_RightsCheck(.F.) |
| USE X:\HASRIGHT\FILE1.DBF VIA "DBFNTX" // Will succeed |
| USE X:\HASRIGHT\FILE2.DBF VIA "DBFNTXAX" // Will succeed |
| USE X:\NORIGHTS\FILE3.DBF VIA "DBFNTX" // Will fail |
| USE X:\NORIGHTS\FILE4.DBF VIA "DBFNTXAX" // WILL SUCCEED! |
| CLOSE ALL |
