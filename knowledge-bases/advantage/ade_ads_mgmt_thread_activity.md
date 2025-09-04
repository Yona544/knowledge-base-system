ADS\_MGMT\_THREAD\_ACTIVITY




Advantage Database Server 12  

ADS\_MGMT\_THREAD\_ACTIVITY

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADS\_MGMT\_THREAD\_ACTIVITY  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - ADS\_MGMT\_THREAD\_ACTIVITY Advantage TDataSet Descendant ade\_Ads\_mgmt\_thread\_activity Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ADS\_MGMT\_THREAD\_ACTIVITY  Advantage TDataSet Descendant |  |  |  |  |

ADS\_MAX\_USER\_NAME = 50;  
   
ADS\_MGMT\_THREAD\_ACTIVITY = record  
  ulThreadNumber: UNSIGNED32; { Thread Number }   
  usOpCode: UNSIGNED16; { Operation in progress }   
  aucUserName: array[0..ADS\_MAX\_USER\_NAME - 1] of char; { Name of user }   
  usConnNumber: UNSIGNED16; { NetWare conn num (Deprecated) }   
  usReserved1: UNSIGNED16; { Reserved }   
  aucOSUserLoginName: array[0..ADS\_MAX\_USER\_NAME - 1] of char; { OS User Login Name }   
end;