Task 3: Define Your AEP EntryPoint




Advantage Database Server 12  

Task 3: Define Your AEP EntryPoint

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Task 3: Define Your AEP EntryPoint  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Task 3: Define Your AEP EntryPoint Advantage Concepts master\_Task\_3\_define\_your\_aep\_entrypoint Advantage Concepts > Advantage Functionality > Advantage Extended Procedures > TDataSet Descendant Tutorial > Task 3:  Define Your AEP EntryPoint / Dear Support Staff, |  |
| Task 3: Define Your AEP EntryPoint  Advantage Concepts |  |  |  |  |

Every AEP has a pre-defined function prototype:

function NameOfAEP( ulConnectionID: UNSIGNED32;

hConnection: ADSHANDLE;

pulNumRowsAffected: PUNSIGNED32 ): UNSIGNED32;

begin

 

end;

Each parameter is described in detail in the general [Advantage Extended Procedures](master_advantage_extended_procedures.htm) documentation. We wont describe each parameter here; well address these parameters as they are used throughout the rest of the tutorial.

The AEP template that was created for you already contains one procedure entrypoint, MyProcedure. We will enhance this existing procedure in later sections.