NULL Values




Advantage Database Server 12  

NULL Values

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| NULL Values  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - NULL Values Advantage SQL Engine master\_Null\_values Advantage SQL > SQL Functionality > NULL Values / Dear Support Staff, |  |
| NULL Values  Advantage SQL Engine |  |  |  |  |

The Advantage SQL engine provides for traditional Xbase style handling of DBF empty fields. The SQL engine does not treat empty fields in DBF tables as standard SQL NULL values. The CDX and NTX field types generally do not have a representation for NULL values, thus the Advantage SQL engine treats empty DBF fields in a manner consistent with most Xbase applications. For example, suppose "test" is a DBF table opened with the ADS\_CDX or ADS\_NTX table type and "N" is a DBF numeric field. If so, then the queries "SELECT \* FROM test WHERE N IS NULL" and "SELECT \* FROM test WHERE N = 0" will be equivalent. Also note that the query "SELECT N+1 FROM test" will produce a result of "1" for each row where N is either 0 or empty.

When using the Visual FoxPro (ADS\_VFP) table type, empty is not treated the same as NULL. VFP tables support true NULL fields. When creating a VFP table, individual fields can be created so that they can store NULL values. Thus, for VFP tables, traditional empty fields (such as a numeric 0) are not considered to be the same as NULL. A query of the form "SELECT \* FROM test WHERE N IS NULL" will only return records if the field N can store the NULL value and some records actually have NULL. To return records with the traditional Xbase empty value, use the EMPTY() scalar function.

ADT tables also provide standard SQL NULL support. For example, NULL and 0 in ADT integer fields have distinctly different internal representations. For example, the WHERE clauses "integerfield = 0" and "integerfield IS NULL" do not return the same rows. Also, a query of the form "SELECT integerfield+1 FROM ..." will return "1" for rows where integerfield has a value of 0 and NULL for rows where integerfield is NULL. This is consistent with SQL handling of NULLs. Aside from the "IS [NOT] NULL" clause and the IFNULL() and ISNULL() scalar functions, any expression that contains a NULL value returns a NULL result.

The primary difference between VFP and ADT handling of NULLs is the fact that VFP fields must be specifically created to store NULL whereas all non-auto-updating ADT fields are automatically able to store NULL values.