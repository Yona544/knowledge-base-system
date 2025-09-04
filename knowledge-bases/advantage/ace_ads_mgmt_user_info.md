ADS\_MGMT\_USER\_INFO




Advantage Database Server 12  

ADS\_MGMT\_USER\_INFO

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADS\_MGMT\_USER\_INFO  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - ADS\_MGMT\_USER\_INFO Advantage Client Engine ace\_Ads\_mgmt\_user\_info Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ADS\_MGMT\_USER\_INFO  Advantage Client Engine |  |  |  |  |

#define ADS\_MAX\_USER\_NAME 50

#define ADS\_MAX\_ADDRESS\_SIZE 30

 

|  |  |
| --- | --- |
| typedef struct |  |
| { |  |
| UNSIGNED8 aucUserName[ADS\_MAX\_USER\_NAME]; | // The user's computer name |

|  |  |
| --- | --- |
| UNSIGNED16 usConnNumber; | // NetWare connection number  // (Deprecated)) |

|  |  |
| --- | --- |
| UNSIGNED8 aucAuthUserName[ADS\_MAX\_USER\_NAME]; | // Name of user that has authenticated  // to an Advantage Data Dictionary |

|  |  |
| --- | --- |
| UNSIGNED8 aucAddress[ADS\_MAX\_ADDRESS\_SIZE]; | // IP or IPX address of  // connected user |

|  |  |
| --- | --- |
| UNSIGNED8 aucOSUserLoginName[ADS\_MAX\_USER\_NAME]; | // OS user login name |

|  |  |
| --- | --- |
| UNSIGNED8 aucTSAddress[ADS\_MAX\_ADDRESS\_SIZE]; | // IP Address of Terminal Services  // client if connection is made from a  // Terminal Server. |
| UNSIGNED8 aucApplicationID[ADS\_MAX\_MGMT\_APPID\_SIZE]; | // ApplicationID, see sp\_SetApplicationID |
| UNSIGNED32 ulAveRequestCost; | // estimated average cost of  // each server request |

|  |  |
| --- | --- |
| } ADS\_MGMT\_USER\_INFO; |  |