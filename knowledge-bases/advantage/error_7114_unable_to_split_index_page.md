7114 Unable to split index page




Advantage Database Server 12  

7114 Unable to split index page

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7114 Unable to split index page  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7114 Unable to split index page Advantage Error Guide error\_7114\_unable\_to\_split\_index\_page Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7114 Unable to split index page  Advantage Error Guide |  |  |  |  |

Problem: The current update operation required an index page split, but it was not possible to split the page.

Solution: This problem can occur if the key size is close (within a few bytes) of the maximum possible key size for the [index page size](master_index_page_size.htm) and the key data cannot be compressed. If this error occurs with the ADT table type, rebuild the index with a larger page size.