ADS\_MGMT\_CONFIG\_PARAMS




Advantage Database Server 12  

ADS\_MGMT\_CONFIG\_PARAMS

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADS\_MGMT\_CONFIG\_PARAMS  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - ADS\_MGMT\_CONFIG\_PARAMS Advantage TDataSet Descendant ade\_Ads\_mgmt\_config\_params Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ADS\_MGMT\_CONFIG\_PARAMS  Advantage TDataSet Descendant |  |  |  |  |

ADS\_MAX\_CFG\_PATH = 256;  
   
ADS\_MGMT\_CONFIG\_PARAMS = record  
  ulNumConnections: UNSIGNED32; { number of connections }   
  ulNumWorkAreas: UNSIGNED32; { number of work areas }   
  ulNumTables: UNSIGNED32; { number of tables }   
  ulNumIndexes: UNSIGNED32; { number of indexes }   
  ulNumLocks: UNSIGNED32; { number of locks }   
  ulUserBufferSize: UNSIGNED32; { user buffer }   
  ulStatDumpInterval: UNSIGNED32; { statistics dump interval }   
  ulErrorLogMax: UNSIGNED32; { max size of error log }   
  ulNumTPSHeaderElems: UNSIGNED32; { number of TPS header elems }   
  ulNumTPSVisibilityElems: UNSIGNED32; { number of TPS vis elems }   
  ulNumTPSMemoTransElems: UNSIGNED32; { number of TPS memo elems }   
  usNumRcvECBs: UNSIGNED16; { number of rcv ECBs (NLM only) }   
  usNumSendECBs: UNSIGNED16; { number of send ECBs (NLM only) }   
  usNumBurstPackets: UNSIGNED16; { number of packets per burst }   
  usNumWorkerThreads: UNSIGNED16; { number of worker threads }   
  usSortBuffSize: UNSIGNED16; { index sort buffer size }   
  ucReserved1: UNSIGNED8 ; { reserved }   
  ucReserved2: UNSIGNED8 ; { reserved }   
  aucErrorLog: array[0..ADS\_MAX\_CFG\_PATH - 1] of char; { error log path }   
  aucSemaphore: array[0..ADS\_MAX\_CFG\_PATH - 1] of char; { sema4 file path }   
  aucTransaction: array[0..ADS\_MAX\_CFG\_PATH - 1] of char; { TPS log file path }   
   
  ucReserved3: UNSIGNED8 ; { reserved }   
  ucReserved4: UNSIGNED8 ; { reserved }   
  usSendIPPort: UNSIGNED16; { NT Service IP send port # }   
  usReceiveIPPort: UNSIGNED16; { NT Service IP receive port # }   
  ucUseIPProtocol: UNSIGNED8; { Win9x only. Which protocol to use. }   
  ucFlushEveryUpdate: UNSIGNED8; { Win9x specific }   
   
  ulGhostTimeout: UNSIGNED32; { Diconnection time for partial connections }   
  ulFlushFrequency: UNSIGNED32; { local server }   
   
  ulKeepAliveTimeOut: UNSIGNED32; { When not using semaphore files. In milli-secs }   
  ucDisplayNWLoginNames: UNSIGNED8; { Display connections using user names. }   
  ucUseSemaphoreFiles: UNSIGNED8; { Whether or not to use semaphore files. }   
  ucUseDynamicAOFs: UNSIGNED8;   
  ucUseInternet: UNSIGNED8; { 0 if an Internet port is not specified. }   
   
  usInternetPort: UNSIGNED16; { Internet Port }   
  usMaxConnFailures: UNSIGNED16; { Maximum Internet connection failures allowed. }   
  ulInternetKeepAlive: UNSIGNED32; { In milli-secs }   
   
  usCompressionLevel: UNSIGNED16; {ADS\_COMPRESS\_NEVER, ADS\_COMPRESS\_INTERNET, or ADS\_COMPRESS\_ALWAYS }   
  usReserved5: UNSIGNED16; { reserved }   
  ulReserved6: UNSIGNED32; { reserved }   
end;