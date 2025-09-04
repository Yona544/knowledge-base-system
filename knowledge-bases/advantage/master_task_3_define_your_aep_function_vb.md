Task 3: Define Your AEP Function




Advantage Database Server 12  

Task 3: Define Your AEP Function

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Task 3: Define Your AEP Function  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Task 3: Define Your AEP Function Advantage Concepts master\_Task\_3\_define\_your\_aep\_function\_vb Advantage Concepts > Advantage Functionality > Advantage Extended Procedures > Visual Basic Tutorial > Task 3:  Define Your AEP Function / Dear Support Staff, |  |
| Task 3: Define Your AEP Function  Advantage Concepts |  |  |  |  |

Every AEP has a pre-defined function prototype:

Public Function MyProcedure(ByVal ulConnectionID As Int32, \_

ByVal hConnection As Int32, \_

ByRef ulNumRowsAffected As Int32) As Int32

 

Each parameter is described in detail in the general [Advantage Extended Procedures](master_advantage_extended_procedures.htm) documentation. We wont describe each parameter here; well address these parameters as they are used throughout the rest of the tutorial.

The AEP template that was created for you already contains one procedure entrypoint, MyProcedure. We will enhance this existing procedure in later sections.