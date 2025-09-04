ADS\_MGMT\_INSTALL\_INFO




Advantage Database Server 12  

ADS\_MGMT\_INSTALL\_INFO

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADS\_MGMT\_INSTALL\_INFO  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - ADS\_MGMT\_INSTALL\_INFO Advantage Client Engine ace\_Ads\_mgmt\_install\_info Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ADS\_MGMT\_INSTALL\_INFO  Advantage Client Engine |  |  |  |  |

#define ADS\_REG\_OWNER\_LEN 36

#define ADS\_REVISION\_LEN 16

#define ADS\_INST\_DATE\_LEN 16

#define ADS\_OEM\_CHAR\_NAME\_LEN 16

#define ADS\_ANSI\_CHAR\_NAME\_LEN 16

#define ADS\_SERIAL\_NUM\_LEN 16

 

typedef struct

{

UNSIGNED32 ulUserOption; /\* For ADS, user option purchased. For ALS, max users that can have any given table open \*/

UNSIGNED8 aucRegisteredOwner[ADS\_REG\_OWNER\_LEN]; /\* Registered owner \*/

UNSIGNED8 aucVersionStr[ADS\_REVISION\_LEN]; /\* Advantage Database Server version \*/

UNSIGNED8 aucInstallDate[ADS\_INST\_DATE\_LEN]; /\* Install date string \*/

UNSIGNED8 aucOemCharName[ADS\_OEM\_CHAR\_NAME\_LEN]; /\* OEM char language \*/

UNSIGNED8 aucAnsiCharName[ADS\_ANSI\_CHAR\_NAME\_LEN];/\* ANSI char language \*/

UNSIGNED8 aucEvalExpireDate[ADS\_INST\_DATE\_LEN]; /\* Eval expiration date \*/

UNSIGNED8 aucSerialNumber[ADS\_SERIAL\_NUM\_LEN]; /\* Serial number string \*/

UNSIGNED32  ulMaxStatefulUsers; /\* How many stateful connections allowed \*/

UNSIGNED32  ulMaxStatelessUsers; /\* How many stateless (web platform) connections allowed \*/

} ADS\_MGMT\_INSTALL\_INFO;