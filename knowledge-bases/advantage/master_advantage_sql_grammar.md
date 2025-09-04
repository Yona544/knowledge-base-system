Advantage SQL Grammar




Advantage Database Server 12  

Advantage SQL Grammar

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage SQL Grammar  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Advantage SQL Grammar Advantage SQL Engine master\_Advantage\_sql\_grammar Advantage SQL > Supported SQL Grammar > Advantage SQL Grammar / Dear Support Staff, |  |
| Advantage SQL Grammar  Advantage SQL Engine |  |  |  |  |

The following is the defined grammar for the Advantage SQL engine, which is the core SQL engine available to all Advantage Windows and Linux clients.

statement ::= CREATE create | DROP drop | SELECT select orderby |

SELECT selectinto orderby | SELECT top select orderby |

INSERT insert | DELETE delete | UPDATE update |

MERGE merge |

ALTER alter | unionstatement |

EXECUTE execute |

SET setstmt |

BEGIN TRAN[SACTION] | COMMIT [ WORK ] | ROLLBACK [ WORK ] |

GRANT grant |

REVOKE revoke

top ::= TOP integer [START AT offset] | TOP integer PERCENT

offset ::= integer

create ::= TABLE tablename ( table-elements ) |

[ONLINE] [UNIQUE] INDEX indexname ON tablename ( indexcolumns ) [ index-options ] |

VIEW viewname AS SELECT select |

DATABASE databasename [PASSWORD string] [DESCRIPTION string] [ ENCRYPT TRUE | ENCRYPT FALSE ]

                 [ ENCRYPTIONTYPE AES128 | AES256 | RC4 ] [ DDPASSWORD string ] |

PROCEDURE procedurename procedure-params FUNCTION function-name IN LIBRARY library-name |

TRIGGER triggername ON tablename trigger-type trigger-event trigger-container [ trigger-options ]

alter ::= [ONLINE | ONLINE\_WITH\_TRANSITION] TABLE tablename alter-specs

alter-specs ::= alter-spec, alter-specs | alter-spec

alter-spec ::= ADD [COLUMN] createcol [<position-info>] |

ALTER [COLUMN] origcol createcol [<position-info>] |

ALTER [COLUMN] columnname DROP drop-column-constraint |

DROP [COLUMN] columnname |

DROP drop-table-constraint  |

MEMOBLOCKSIZE <blocksize> |

[IGNORE | RESPECT] TRANSACTIONS

table-elements ::= table-element , table-elements | table-element

table-element ::= createcol | table-constraint

createcol ::= columnname datatype [ vfp-options ] [ column-constraints ]

position-info ::= [ POSITION integer ]

vfp-options ::= vfp-option vfp-options | vfp-option

vfp-option ::= NULL | NOT NULL | NOCPTRANS

column-constraints ::= column-constraint column-constraints | column-constraint

column-constraint ::= CONSTRAINT NOT NULL |

CONSTRAINT MINIMUM max-column-value |

CONSTRAINT MAXIMUM min-column-value |

CONSTRAINT ERROR MESSAGE error-message |

DEFAULT default-column-value |

[CONSTRAINT indexname] PRIMARY KEY

table-constraint ::= [CONSTRAINT indexname] PRIMARY KEY ( indexcolumns )

drop-column-constraint ::= NOT NULL | MINIMUM | MAXIMUM | ERROR MESSAGE | DEFAULT

drop-table-constraint ::= [CONSTRAINT] PRIMARY KEY

indexcolumns ::= indexcolumn | indexcolumn , indexcolumns

indexcolumn ::= columnname asc

index-options ::= index-option index-options | index-option

index-option ::= CONTENT |

IN FILE filename |

PAGESIZE integer |

MIN WORD integer |

MAX WORD integer |

[NEW] DELIMITERS string |

[NEW] DROPCHARS string |

[NEW] NOISE string |

[NEW] CONDITIONALS string |

NOTMAINTAINED |

CASESENSITIVE

KEEPSCORE |

PROTECTNUMBERS

procedure-params ::= () | ( procedure-param-list )

procedure-param-list ::= procedure-param | procedure-param , procedure-param-list

procedure-param ::= identifier datatype [ OUTPUT ]

trigger-type ::= BEFORE | INSTEAD OF | AFTER

trigger-event ::= INSERT | UPDATE | DELETE

trigger-container ::= library-container | script-container

library-container ::= FUNCTION function-name IN library-type library-name

function-name ::= A user-defined function name. Name of the function in the library that holds the trigger or stored procedure code.

library-type ::= LIBRARY | ASSEMBLY

library-name ::= identifier (A user-defined library name such as a DLL, COM object, .Net assembly, etc. See the documentation for the triggers and stored procedures.)

script-container ::= BEGIN statement ; statement-list END

statement-list ::= | , statement ; statement-list

trigger-options ::= NO VALUES | NO MEMOS | PRIORITY trigger-priority

trigger-priority ::= integer (A user-defined integer value, specifying the trigger's firing priority.)

drop ::= TABLE tablename [FROM DATABASE [NO\_DELETE]]|

INDEX tablename . indexname |

VIEW viewname |

PROCEDURE procedurename |

TRIGGER tablename . triggername

select ::= {static} selectcols FROM tablelist where groupby having

selectinto ::= selectcols INTO tablename FROM tablelist where groupby having

unionstatement ::= union unionorderby

union ::= unionitem UNION unionitem | unionitem UNION ALL unionitem

unionitem ::= SELECT select | ( union )

unionorderby ::= | ORDER BY unionorderbyterms

unionorderbyterms ::= unionorderbyterm | unionorderbyterm , unionorderbyterms

unionorderbyterm ::= integer asc

delete ::= FROM tablename where

insert ::= INTO tablename [WITH DELETE] insertvals

update ::= tablename [WITH DELETE | WITH RECALL] SET setlist where |

               tablename [WITH DELETE | WITH RECALL] SET setlist FROM tablelist where

merge ::= [INTO] <tableref> [USING <tableref>] ON <boolean>

<WHEN MATCHED THEN <update specification>> |

<WHEN NOT MATCHED THEN <insert specification>>

update specification ::= UPDATE [WITH DELETE | WITH RECALL] SET <setlist>

insert specification ::= INSERT [WITH DELETE] <insertvals>

execute ::= PROCEDURE procedurename () | PROCEDURE procedurename ( valuelist )

setstmt ::= TRAN[SACTION] transaction-mode

transaction-mode ::= AUTOCOMMIT\_ON | AUTOCOMMIT\_OFF | EXPLICIT

grant ::= <permission [, ...n]> [ON <object>] TO <grantee> [WITH GRANT]

revoke ::= [GRANT OPTION FOR] <permission [, n]> [ON <object>] FROM <grantee>

permissions ::= SELECT | SELECT( columnname ) | INSERT | INSERT( columnname ) |

UPDATE | UPDATE( columnname ) | ACCESS | ALL | ALTER [DATABASE] |

DELETE | DROP | EXECUTE | INHERIT [DATABASE] | <create permission>

create permission ::= [INHERIT] CREATE <create object>

create object ::= TABLE | USER [GROUP] | VIEW | PROCEDURE | LINK

object ::= viewname | tablename | procedurename | linkname

setlist ::= set | setlist , set

set ::= columnname = NULL | columnname = expression | columnname = ( SELECT select )

insertvals ::= ( columnlist ) VALUES ( insertvaluelist ) | DEFAULT VALUES |

VALUES ( insertvaluelist ) | ( columnlist ) SELECT select |

SELECT select

insertvaluelist ::= DEFAULT | NULL | expression | DEFAULT, insertvaluelist |

expression, insertvaluelist | NULL, insertvaluelist

columnlist ::= columnname , columnlist | columnname

valuelist ::= NULL , valuelist | expression , valuelist | expression | NULL

selectcols ::= selectallcols \* | selectallcols selectlist

selectallcols ::= | ALL | DISTINCT

selectlist ::= selectlistitem , selectlist | selectlistitem

selectlistitem ::= expression | expression aliasname |

expression AS aliasname | aliasname . \*

where ::= | WHERE boolean

having ::= | HAVING boolean

boolean ::= and | and OR boolean

and ::= not | not AND and

not ::= comparison | NOT comparison

comparison ::= ( boolean ) | expression IS NULL | expression IS NOT NULL |

expression LIKE expression [ESCAPE escape\_char] |

expression NOT LIKE expression [ESCAPE escape\_char] |

expression IN ( valuelist ) | expression NOT IN ( valuelist ) |

expression op expression | EXISTS ( SELECT select ) |

expression op selectop ( SELECT select ) |

expression IN ( SELECT select ) |

expression NOT IN ( SELECT select ) |

expression BETWEEN expression AND expression |

expression NOT BETWEEN expression AND expression

selectop ::= | ALL | ANY

op ::= > | >= | < | <= | = | <> | & | | | ^ | << | >>

pattern ::= string collate | ? | USER

expression ::= expression & addsub | expression | addsub |

 expression ^ addsub | expression << addsub |

 expression >> addsub | addsub

addsub ::= expression + times collate | expression - times | times

times ::= times \* neg | times / neg | times % neg | neg

neg ::= term | + term | - term | ~term

term ::= ( expression ) collate | colref | simpleterm | aggterm | scalar | case

scalar ::= { FN fn collate } | fn collate

fn ::= functionname ( valuelist ) | functionname ( ) |

POSITION ( expression IN expression ) |

EXTRACT ( expression FROM expression ) |

CAST ( expr AS datatype )

aggterm ::= COUNT ( \* ) | AVG ( expression ) | MAX ( expression ) |

MIN ( expression ) | SUM ( expression ) | COUNT ( [ ALL | DISTINCT ] expression )

simpleterm ::= string collate | realnumber | ? | USER | date | time | timestamp

groupby ::= | GROUP BY groupbyterms

groupbyterms ::= colref | colref , groupbyterms

orderby ::= | ORDER BY orderbyterms

orderbyterms ::= orderbyterm | orderbyterm , orderbyterms

orderbyterm ::= colref asc | integer asc

asc ::= | ASC | DESC

collation\_lang ::= ADS\_DEFAULT\_CI | ADS\_DEFAULT\_CS

collate ::= | COLLATE collation\_lang

colref ::= aliasname . columnname collate | columnname collate

tablelist ::= tablelistitem , tablelist | tablelistitem

tablelistitem ::= tableref | join

join ::= tableref jointype tableref ON boolean altjoin |

tableref jointype join ON boolean altjoin

altjoin ::= | jointype tableref ON boolean altjoin

jointype ::= LEFT [ OUTER ] JOIN |

RIGHT [ OUTER ] JOIN |

FULL [ OUTER ] JOIN |

INNER JOIN

tableref ::= tablename | tablename aliasname | databasename.tablename |

databasename.tablename aliasname | execute aliasname

databasename ::= identifier

indexname ::= identifier

functionname ::= identifier

tablename ::= identifier

viewname ::= identifier

columnname ::= identifier

aliasname ::= identifier

filename ::= identifier

procedurename ::= identifier

triggername ::= identifier

grantee ::= identifier

linkname ::= indentifier

datatype ::= type-name | type-name ( integer ) | type-name ( integer , integer )

type-name ::= A supported data type (see Supported Data Types in the Advantage SQL Engine).

identifier ::= an identifier (identifiers that do not start with letters or that contain spaces or other special characters must be enclosed in double quotes or [] (brackets), e.g., "2two", "my name", "x:\datapath\table.abc", [3D], [I/O])

string ::= a string (enclosed in single quotes)

realnumber ::= a non-negative real number (including E notation)

integer ::= a non-negative integer

binary string literal ::= X'[ <space> ] { hexit [ <space> ] hexit [ <space> ] }... ]'

hexit ::= <digit> | A | B | C | D | E | F | a | b | c | d | e | f

date ::= { d dateval } | dateval

dateval ::= a date in the ANSI yyyy-mm-dd format in single quotes (for example, '1996-02-15') or in the default date format specified in your application via the "set date format" operation.

time ::= { t timeval } | timeval

timeval ::= a time in hh:mm:ss format in single quotes (for example, '10:19:48')

timestamp ::= { ts timestampval } | timestampval

timestampval ::= a timestamp in the ANSI yyyy-mm-dd hh:mm:ss[.fff] format in single quotes. Alternatively, the date portion of the timestamp can use the default date format specified in your application via the "set date format" operation.

origcol ::= A string representing an existing column name.

error-message ::= A string literal to be returned as the error message when the column constraints are violated.

max-column-value ::= A string literal that is surrounded by single quotes containing an Advantage expression. The evaluated expression result must be of the same data type as the column data type. The result will be used as the maximum value for the column. For more information about expressions, see Advantage Expression Engine.

min-column-value ::= A string literal that is surrounded by single quotes containing an Advantage expression. The evaluated expression result must be of the same data type as the column data type. The result will be used as the minimum value for the column. For more information about expressions, see Advantage Expression Engine.

default-column-value ::= A string literal that is surrounded by single quotes containing an Advantage expression. The evaluated expression result must be of the same data type as the column data type. The result will be used as default value for the column when new records are added or the ADS\_DD\_RI\_SETDEFAULT rule is used in referential integrity. For more information about expressions, see Advantage Expression Engine.

case ::= simple\_case collate | searched\_case collate

simple\_case ::= CASE expression simple\_when\_clauses [else\_clause] END

searched\_case ::= CASE searched\_when\_clauses [else\_clause] END

simple\_when\_clauses ::= simple\_when\_clause | simple\_when\_clause simple\_when\_clauses

searched\_when\_clauses ::= searched\_when\_clause |

searched\_when\_clause searched\_when\_clauses

simple\_when\_clause ::= WHEN expression THEN result

searched\_when\_clause ::= WHEN boolean THEN result

else\_clause ::= ELSE result

result ::= expression | NULL