sp\_DropReferentialIntegrity




Advantage Database Server 12  

sp\_DropReferentialIntegrity

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_DropReferentialIntegrity  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_DropReferentialIntegrity Advantage SQL Engine master\_Sp\_dropreferentialintegrity Advantage SQL > System Procedures > Procedures > sp\_DropReferentialIntegrity / Dear Support Staff, |  |
| sp\_DropReferentialIntegrity  Advantage SQL Engine |  |  |  |  |

Removes a referential integrity (RI) constraint from the data dictionary.

Syntax

sp\_DropReferentialIntegrity( Name,CHARACTER,200 )

Parameters

|  |  |
| --- | --- |
| Name (I) | Name of the RI constraint in the data dictionary to be removed. |

Remarks

sp\_DropReferentialIntegrity will remove a RI constraint from the data dictionary.

The parent and child table must not be opened, so that the Advantage Database Server can temporarily open the parent and the child tables exclusively. This function will temporarily open all tables exclusively that are in the data dictionary and that interlink with these tables through other RI constraints

Example

EXECUTE PROCEDURE sp\_DropReferentialIntegrity( salesreps\_has\_office );

See Also

[system.relations](master_system_relations.htm)

[sp\_CreateReferentialIntegrity](master_sp_createreferentialintegrity.htm)