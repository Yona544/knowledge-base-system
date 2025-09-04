Assignment




Advantage Database Server 12  

Assignment

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Assignment  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Assignment Advantage SQL Engine master\_Assignment Advantage SQL > SQL PSM (SCRIPT) > Assignment / Dear Support Staff, |  |
| Assignment  Advantage SQL Engine |  |  |  |  |

The Assignment statement is used to assign a new value to a declared variable.

Syntax

[SET] variable\_name = expr;

Description

The expr is evaluated and the result of the evaluation is assigned to the variable. The SET keyword is optional.

The data type of the expr must match the data type of the variable. The variable\_name must be [declared](master_declare.htm) at the beginning of the script.

Range checking is performed on numeric data. If the value to be assigned to is outside of the range, an ADS\_SCRIPT\_EXCEPTION exception with the error code 2227 (ERR\_SCRIPTOUTOFRANGE) will be raised.

Example

DECLARE strLocal String;

DECLARE str2 String;

DECLARE acVar3 Char(20), dtVal Date;

 

 

strLocal = 'abc';

SET str2 = strLocal + 'def';

acVar3 = str2 + strLocal;

SET dtVal = ( SELECT dob FROM employees WHERE empid = 1 );