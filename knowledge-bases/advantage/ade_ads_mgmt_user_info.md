ADS\_MGMT\_USER\_INFO




Advantage Database Server 12  

ADS\_MGMT\_USER\_INFO

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADS\_MGMT\_USER\_INFO  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - ADS\_MGMT\_USER\_INFO Advantage TDataSet Descendant ade\_Ads\_mgmt\_user\_info Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ADS\_MGMT\_USER\_INFO  Advantage TDataSet Descendant |  |  |  |  |

ADS\_MAX\_USER\_NAME = 50;  
ADS\_MAX\_ADDRESS\_SIZE = 30;  
ADS\_MAX\_MGMT\_APPID\_SIZE = 70;  
   
ADS\_MGMT\_USER\_INFO = record  
  aucUserName: array[0..ADS\_MAX\_USER\_NAME - 1] of char; { Computer name }   
  usConnNumber: UNSIGNED16; { NetWare connection number (Deprecated) }   
  aucDictionaryName: array[0..ADS\_MAX\_USER\_NAME-1] of char; { Name of user that has authenticated to an Advantage Data Dictionary }   
  aucAddress: array[0..ADS\_MAX\_ADDRESS\_SIZE - 1] of char; { IP or IPX address of connected user }   
  aucOSUserLoginName: array[0..ADS\_MAX\_USER\_NAME - 1] of char; { OS User Login Name }   
  aucApplicationID: array[0..ADS\_MAX\_MGMT\_APPID\_SIZE - 1] of char; { Application ID }  
  ulAveRequestCost: UNSIGNED32; { estimated average cost of each server request }  
end;