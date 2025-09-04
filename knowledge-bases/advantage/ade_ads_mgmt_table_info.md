ADS\_MGMT\_TABLE\_INFO




Advantage Database Server 12  

ADS\_MGMT\_TABLE\_INFO

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADS\_MGMT\_TABLE\_INFO  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - ADS\_MGMT\_TABLE\_INFO Advantage TDataSet Descendant ade\_Ads\_mgmt\_table\_info Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ADS\_MGMT\_TABLE\_INFO  Advantage TDataSet Descendant |  |  |  |  |

ADS\_MGMT\_MAX\_PATH = 260;  
   
ADS\_MGMT\_TABLE\_INFO = record  
  aucTableName: array[0..ADS\_MGMT\_MAX\_PATH - 1] of char; { Fully qualified table name }   
  usLockType: UNSIGNED16; { Advantage locking mode }   
end;