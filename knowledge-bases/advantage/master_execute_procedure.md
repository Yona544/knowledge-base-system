EXECUTE PROCEDURE




Advantage Database Server 12  

EXECUTE PROCEDURE

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| EXECUTE PROCEDURE  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - EXECUTE PROCEDURE Advantage SQL Engine master\_Execute\_procedure Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| EXECUTE PROCEDURE  Advantage SQL Engine |  |  |  |  |

Executes an Advantage Extended Procedure (stored procedure)

Syntax

EXECUTE PROCEDURE <procedure-name> ( [<param-values>[, <param-values>])

 

Examples

EXECUTE PROCEDURE AddRecordToData( Smith, John, 13, TRUE )

 

; note that this example would require the four named parameters to be

; assigned values prior to the statement being executed.

EXECUTE PROCEDURE AddRecordToData( :lname, :fname, :id, :married )

 

;note that this example has no parameters

EXECUTE PROCEDURE BeginTransaction()