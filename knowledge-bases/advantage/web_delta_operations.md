Advantage Web Platform Delta Operations




Advantage Database Server 12  

Delta Operations

Advantage Web Platform

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Delta Operations  Advantage Web Platform |  |  | Feedback on: Advantage Database Server 12 - Delta Operations Advantage Web Platform web\_delta\_operations Advantage Web Development > Advantage Web Platform > Delta / Dear Support Staff, |  |
| Delta Operations  Advantage Web Platform |  |  |  |  |

The delta feature allows the client to retrieve only changes to a query result. This feature is described in <http://www.odata.org/blog/2011/3/16/reference-data-caching>. To enable the delta feature, the collection must be a table in a data dictionary, it must have a rowversion column and the primary key or a unique index defined. The table must have the web delta property enabled. See [AdsDDSetTableProperty](ace_adsddsettableproperty.htm) or [sp\_ModifyTableProperty](master_sp_modifytableproperty.htm) for additional information. Once the table is set up to track changes, the result of the table query will include a \_\_delta member which can be used in the subsequent queries to retrieve the changes to the result. The changes will include deleted rows and updated/inserted rows.

The following is an example response to the query "https://myserver.com:6282/adsweb/example/v1/demo10?$deltatoken=130" in JSON format:

{

 "d": {

   "results": [

     {

       "\_\_metadata": {

         "uri": "https://myserver.com:6282/adsweb/example/v1/demo10(8)",

         "key\_fields": "EMPID",

         "rows\_affected": 0,

         "last\_autoinc": 0,

         "deleted\_entry": true

       }

     },

     {

       "\_\_metadata": {

         "uri": "https://myserver.com:6282/adsweb/example/v1/demo10(97)",

         "key\_fields": "EMPID",

         "rows\_affected": 0,

         "last\_autoinc": 0,

         "deleted\_entry": true

       }

     },

     {

       "\_\_metadata": {

         "uri": "https://myserver.com:6282/adsweb/example/v1/demo10(101)",

         "key\_fields": "EMPID",

         "rows\_affected": 0,

         "last\_autoinc": 0

       },

       "DEPTNUM": 11,

       "LASTNAME": "bb",

       "FIRSTNAME": "cccc",

       "DOH": null,

       "SALARIED": null,

       "EMPID": 101,

       "PHONE": "12",

       "DOB": null,

       "EXTENSION": 3333,

       "SOC\_SEC\_NU": "123-45-678",

       "MARRIED": true,

       "DIVISION": "Idle",

       "BRANCH": "Boise",

       "rv": 136

     }

   ],

   "\_\_delta": "https://myserver.com:6282/adsweb/example/v1/demo10?$deltatoken=138"

 }

}

 

Note that the first two rows in the results are deleted rows because the deleted\_entry of the \_\_metadata is true. The last row in the result is either a changed rows or a newly inserted row. The client application should use the predicate in the \_\_metadata.uri to update the cached data. One caveat about the deleted\_entry is that the specified row may not be in the client cache because the row may be inserted and deleted between the clients request for changes. The client application is expected to handle this case.

Note also the \_\_delta reference in result above. It is to be used to by the client to query for further changes in the table. The client is responsible for using the URI to retrieve the changes to update the cached resultset.

The $filter option may be used with delta query, however, changes may not be retrieved if the changes are made to the columns used in the filter. For example, the request https://myserver.com:6282/adsweb/example/v1/demo10?$filter=lastname eq 'Mark'" may return rows with a delta link. If the lastname column of one of the rows is update to be different, requesting using the delta link will not return the changes because the changes is filtered out by the $filter. It is thus best to only use $filter on immutable columns when using the delta functionality.

Important Note When the results are to be returned in multiple pages, the delta link will only appear on the first page of the result. The first page will have both the Next page link and the Delta link. According to at least one unofficial OData standard, this response is not in conformance and it will likely be changed in the future.

Important Note If the $orderby options is specified in a request with $deltatoken option, the result may not be sorted according to the $orderby option. The standard is still evolving but it is most likely that the rows in the delta query should always be returned ordered by when the change occurred.