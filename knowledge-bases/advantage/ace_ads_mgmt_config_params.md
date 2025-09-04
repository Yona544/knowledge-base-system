ADS\_MGMT\_CONFIG\_PARAMS




Advantage Database Server 12  

ADS\_MGMT\_CONFIG\_PARAMS

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADS\_MGMT\_CONFIG\_PARAMS  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - ADS\_MGMT\_CONFIG\_PARAMS Advantage Client Engine ace\_Ads\_mgmt\_config\_params Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ADS\_MGMT\_CONFIG\_PARAMS  Advantage Client Engine |  |  |  |  |

#define ADS\_MAX\_CFG\_PATH 256

 

typedef struct

{

UNSIGNED32 ulNumConnections; /\* number connections \*/

UNSIGNED32 ulNumWorkAreas; /\* number work areas \*/

UNSIGNED32 ulNumTables; /\* number tables \*/

UNSIGNED32 ulNumIndexes; /\* number indexes \*/

UNSIGNED32 ulNumLocks; /\* number locks \*/

UNSIGNED32 ulUserBufferSize; /\* user buffer \*/

UNSIGNED32 ulStatDumpInterval; /\* statistics dump interval \*/

UNSIGNED32 ulErrorLogMax; /\* max size of error log \*/

UNSIGNED32 ulNumTPSHeaderElems; /\* number TPS header elems \*/

UNSIGNED32 ulNumTPSVisibilityElems; /\* number TPS vis elems \*/

UNSIGNED32 ulNumTPSMemoTransElems; /\* number TPS memo elems \*/

UNSIGNED16 usNumReceiveECBs; /\* number rcv ECBs (NLM only) \*/

UNSIGNED16 usNumSendECBs; /\* number send ECBs (NLM only) \*/

UNSIGNED16 usNumBurstPackets; /\* number packets per burst \*/

UNSIGNED16 usNumWorkerThreads; /\* number worker threads \*/

UNSIGNED16 usSortBuffSize; /\* index sort buffer size \*/

UNSIGNED8 ucReserved1; /\* reserved \*/

UNSIGNED8 ucReserved2; /\* reserved \*/

UNSIGNED8 aucErrorLog[ADS\_MAX\_CFG\_PATH]; /\* error log path \*/

UNSIGNED8 aucSemaphore[ADS\_MAX\_CFG\_PATH]; /\* semaphore file path \*/

UNSIGNED8 aucTransaction[ADS\_MAX\_CFG\_PATH]; /\* TPS log file path \*/

UNSIGNED8 ucReserved3; /\* reserved \*/

UNSIGNED8 ucReserved4; /\* reserved \*/

UNSIGNED16 usSendIPPort; /\* IP send port number \*/

UNSIGNED16 usReceiveIPPort; /\* IP receive port number \*/

 

UNSIGNED8 ucUseIPProtocol; /\* Win9x only. Which protocol to use \*/

UNSIGNED8 ucFlushEveryUpdate; /\* Win9x specific \*/

 

UNSIGNED32 ulGhostTimeout; /\* Disconnection time for partial

connections \*/

UNSIGNED32 ulFlushFrequency; /\* For local server only \*/

 

UNSIGNED32 ulKeepAliveTimeOut; /\* When not using semaophore files. In

milliseconds \*/

UNSIGNED8 ucDisplayNWLoginNames; /\* Display connections using user names. \*/

UNSIGNED8 ucUseSemaphoreFiles; /\* Whether or not to use semaphore files \*/

UNSIGNED8 ucUseDynamicAOFs;

UNSIGNED8 ucUseInternet; /\* 0 if an Internet port is not

specified. (For ver. 6.1) \*/

 

UNSIGNED16 usInternetPort; /\* Internet Port (For ver. 6.1\*/) \*/

UNSIGNED16 usMaxConnFailures; /\* Maximum Internet connection failures

allowed. (For ver. 6.1\*/) \*/

UNSIGNED32 ulInternetKeepAlive; /\* In Milliseconds (For ver. 6.1\*/) \*/

 

UNSIGNED16 usCompressionLevel; /\* Compression option at server. ADS\_COMPRESS\_NEVER,

\* ADS\_COMPRESS\_INTERNET, or ADS\_COMPRESS\_ALWAYS \*/

UNSIGNED32 ulNumQueries; /\* number of queries \*/

UNSIGNED16 usReserved5; /\* reserved \*/

 

} ADS\_MGMT\_CONFIG\_PARAMS;