AX\_AXSLocking()




Advantage Database Server 12  

AX\_AXSLocking()

Advantage Visual Objects and Vulcan.NET RDD

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AX\_AXSLocking()  Advantage Visual Objects and Vulcan.NET RDD |  |  | Feedback on: Advantage Database Server 12 - AX\_AXSLocking() Advantage Visual Objects and Vulcan.NET RDD vo\_Ax\_axslocking Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Advanced  Functions > AX\_AXSLocking() / Dear Support Staff, |  |
| AX\_AXSLocking()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Returns and sets the AXS locking status

Syntax

AX\_AXSLocking( [.T.|.F.] ) -> logical

[.T.|.F.] A logical value used to turn AXS Locking ON (.T.) or OFF (.F.).

Returns

If no parameter is passed to AX\_AXSLocking(), then returns the current Advantage Locking setting (i.e. returns a .T. if AXS Locking is ON or .F. if AXS Locking is turned OFF). If a parameter is passed to AX\_AXSLocking(), then returns previous Advantage Locking setting.

Description

AX\_AXSLocking() will turn Advantage Locking ON if the logical value .T. is passed in or turn Advantage Locking OFF if the logical value .F. is passed in. If no value is passed in, the current setting of Advantage Locking is returned, and Advantage Locking remains the same.

The current setting is always returned first before being set to ON/OFF.

AX\_AXSLocking()allows you to alter lock management calls. Record and file locking is essential to prevent corruption in a shared environment. In previous versions of Advantage, the locking was managed strictly by Advantage, using proprietary locking schemes. This also required any other applications using the shared files to be Advantage applications. Once AXS Locking is set ON or OFF, it applies to all subsequent work areas opened in the application.

For considerations when using this function, see [Advantage Locking Modes](master_advantage_locking_modes.htm).

Object-oriented Example

See [CLASS AxDBServer](vo_class_axdbserver.htm) for code sample for the AxDBServer class.

|  |
| --- |
| // Set the global flag so that Advantage Locking is OFF. |
| // (Non-Advantage applications can have access.) |
| AX\_AXSLocking( .F. ) |
|  |
| oDB1 := AxDBServer{ "TEST1", .F., .F., "DBFNTXAX" } |
|  |
| // Set the global flag so that Advantage Locking is ON. |
| AX\_AXSLocking( .T. ) |
|  |
| oDB2 := AxDBServer{ "TEST2", .F., .F., "DBFNTXAX" } |
|  |

Procedural Example

|  |
| --- |
| ? "AXS locking is currently," AX\_AXSLocking() |
|  |
| // Turn AXS locking OFF so this workarea will see Visual Objects |
| // DBFNTX locking |
|  |
| AX\_AXSLocking( .F. ) |
|  |
| USE test VIA "DBFNTXAX" SHARED NEW |
|  |
| // This lock will be seen by Visual Objects and will respect |
| // Visual Objects locks |
|  |
| ? Rlock() |