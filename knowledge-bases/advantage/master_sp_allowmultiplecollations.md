sp\_AllowMultipleCollations




Advantage Database Server 12  

sp\_AllowMultipleCollations

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_AllowMultipleCollations  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_AllowMultipleCollations Advantage SQL Engine master\_Sp\_allowmultiplecollations Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| sp\_AllowMultipleCollations  Advantage SQL Engine |  |  |  |  |

Specify whether multiple collations are allowed in an index.

Syntax

sp\_AllowMultipleCollations(

Pattern,CICHARACTER,100,

AllowMultiple,Logical )

Parameters

|  |  |
| --- | --- |
| Pattern (I) | Name pattern that can be used to restrict the operation. For example, if the parameter is general%, all of the collations beginning with the word general would be updated by this function. If an empty string or NULL is given, all collations are updated. |
| AllowMultiple (I) | Indicate whether the specified collation(s) can be opened concurrently in an index with other collations. |

Output

The sp\_AllowMultipleCollations procedure returns a single row result set with a column named Result that indicates the results of the call.

Remarks

sp\_AllowMultipleCollations provides a mechanism to turn off the [5209](error_5209_ae_collations_do_not_match.htm) error that is generated if a table is opened that has indexes built from collations that do not match the currently specified collation.

If an application has already used a collation that is modified by this procedure, it will need to reconnect in order for the change to take affect. This procedure does not modify the collation information that the client has already retrieved from the server.

Because this changes a field in the collation repository (adscollate.adt), it may affect all applications that use that repository. The 5209 error that this procedure affects, though, is primarily intended for developers to alert them to the potential optimization issues that can occur as a result of using multiple collations. Please see the topic on [dynamic collation support](master_collation_support.htm) for more information.

Example

The following calls turn off the 5209 error for two collations:

EXECUTE PROCEDURE sp\_AllowMultipleCollations( 'Spanish\_vfp\_ci\_as\_1252', true )

EXECUTE PROCEDURE sp\_AllowMultipleCollations( 'German\_vfp\_ci\_as\_1252', true )

See Also

[Dynamic Collation Support](master_collation_support.htm)