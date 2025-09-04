ADS\_MGMT\_INSTALL\_INFO




Advantage Database Server 12  

ADS\_MGMT\_INSTALL\_INFO

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADS\_MGMT\_INSTALL\_INFO  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - ADS\_MGMT\_INSTALL\_INFO Advantage TDataSet Descendant ade\_Ads\_mgmt\_install\_info Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ADS\_MGMT\_INSTALL\_INFO  Advantage TDataSet Descendant |  |  |  |  |

ADS\_REG\_OWNER\_LEN = 36;  
ADS\_REVISION\_LEN = 16;  
ADS\_INST\_DATE\_LEN = 16;  
ADS\_OEM\_CHAR\_NAME\_LEN = 16;  
ADS\_ANSI\_CHAR\_NAME\_LEN = 16;  
ADS\_SERIAL\_NUM\_LEN = 16;  
   
ADS\_MGMT\_INSTALL\_INFO = record  
  ulUserOption : UNSIGNED32; { For ADS, user option purchased. For ALS, }  
                             { max users that can have any given table open }  
  aucRegisteredOwner: array[0..ADS\_REG\_OWNER\_LEN - 1] of char;   
  aucVersionStr: array[0..ADS\_REVISION\_LEN - 1] of char;   
  aucInstallDate: array[0..ADS\_INST\_DATE\_LEN - 1] of char;   
  aucOemCharName: array[0..ADS\_OEM\_CHAR\_NAME\_LEN - 1] of char;   
  aucAnsiCharName: array[0..ADS\_ANSI\_CHAR\_NAME\_LEN - 1] of char;   
  aucEvalExpireDate: array[0..ADS\_INST\_DATE\_LEN - 1] of char;   
  aucSerialNumber: array[0..ADS\_SERIAL\_NUM\_LEN - 1] of char;

 ulMaxStatefulUsers: UNSIGNED32; { How many stateful connections allowed }

 ulMaxStatelessUsers: UNSIGNED32; { How many stateless (web platform) connections allowed }  
end;