SQL




Advantage Database Server 12  

TAdsQuery.SQL

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsQuery.SQL  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsQuery.SQL Advantage TDataSet Descendant ade\_Sql Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsQuery.SQL  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.htm)

The Advantage SQL parameter is used much like the Delphi TQuery.SQL property. There are, however, subtle differences. When a date or timestamp parameter value is being supplied in a string format, then the date must be in either the SQL 92 standard format of CCYY-MM-DD or in the global date format (see [TAdsSettings.DateFormat](ade_dateformat.htm)).

Example

AdsQuery1.SQL.Add( select \* from DataFile where DateField < 1999-02-14 );

The date format in the Delphi ShortDateFormat may not be used. If the string is in the Delphi ShortDateFormat, then you may consider replace the date constant with a named parameter and supplying the parameter value as date value as in this example:

AdsQuery1.SQL.Add( select \* from DataFile where DateField < :DateVal);

AdsQuery1.ParamByName('DateVal').AsDateTime := StrToDate( 2/14/99 );