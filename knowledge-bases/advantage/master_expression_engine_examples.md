Expression Engine Examples




Advantage Database Server 12  

Expression Engine Examples

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Expression Engine Examples  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Expression Engine Examples Advantage Concepts master\_Expression\_engine\_examples Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Expression Engine Examples  Advantage Concepts |  |  |  |  |

// Expression where lastname begins with 'Col'

// or where characters 2-4 in lastname are 'ost'

LEFT(lastname, 3) == "Col" .OR. SUBSTR(lastname, 2, 3) == "ost"

 

// Expression for records that do not have a '-' in the

// fourth position of the phone field.

AT( "-", phone ) <> 4'

 

// Expression for records where the date of birth (dob)

// field is before Jan 21, 1945. Note that CTOD expects the date to be

// specified according to the current date format.

dob < CTOD( "01/21/1945" )'

 

// Expression for lastname and employee id (empid). Include a

// condition so that only records included are those who are not

// deleted and were born after Dec 31, 1950

lastname+STR(empid)

 

// Expression for records that are not

// deleted and were born after Dec 31, 1950

.NOT. DELETED() .AND. dob > CTOD( "12/31/1950" )

 

// Expression with many fields of different types. The semi-colon operator

// concatenates unlike data types in a binary manner. It can only be used with

// the ADT file format. Note that lastname is a character field, empid is a

// numeric field, dateofhire is a date field, and married is a logical field.

lastname;empid;dateofhire;married