---
title: Master Execute Procedure
slug: master_execute_procedure
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_execute_procedure.htm
source: Advantage CHM
tags:
  - master
checksum: f4ec3b537f825d35d882c95a04775d036c65f37e
---

# Master Execute Procedure

EXECUTE PROCEDURE

EXECUTE PROCEDURE

Advantage SQL Engine

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
