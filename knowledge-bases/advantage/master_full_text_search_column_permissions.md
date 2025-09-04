Full Text Search Column Permissions




Advantage Database Server 12  

Full Text Search Column Permissions

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Full Text Search Column Permissions  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Full Text Search Column Permissions Advantage Concepts master\_Full\_text\_search\_column\_permissions Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Full Text Search Column Permissions  Advantage Concepts |  |  |  |  |

In general, the CONTAINS, SCORE, and SCOREDISTINCT scalar functions obey column level permissions the same as other functions. In one case, however, they are stricter. Normally with level 1 permissions (ADS\_DD\_TABLE\_PERMISSION\_LEVEL\_1), it is possible to search columns that do not have read permissions. When using the form of the FTS scalar functions with the asterisk (\*) as the first parameter, only fields with read permissions will be searched.