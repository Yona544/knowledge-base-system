ADS\_MGMT\_CONFIG\_MEMORY




Advantage Database Server 12  

ADS\_MGMT\_CONFIG\_MEMORY

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADS\_MGMT\_CONFIG\_MEMORY  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - ADS\_MGMT\_CONFIG\_MEMORY Advantage TDataSet Descendant ade\_Ads\_mgmt\_config\_memory Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ADS\_MGMT\_CONFIG\_MEMORY  Advantage TDataSet Descendant |  |  |  |  |

ADS\_MGMT\_CONFIG\_MEMORY = record  
  ulTotalConfigMem: UNSIGNED32; { total mem used by cfg params }   
  ulConnectionMem: UNSIGNED32; { memory taken by connections }   
  ulWorkAreaMem: UNSIGNED32; { memory taken by work areas }   
  ulTableMem: UNSIGNED32; { memory taken by tables }   
  ulIndexMem: UNSIGNED32; { memory taken by indexes }   
  ulLockMem: UNSIGNED32; { memory taken by locks }   
  ulUserBufferMem: UNSIGNED32; { memory taken by user buffer }   
  ulTPSHeaderElemMem: UNSIGNED32; { memory taken by TPS hdr elems }   
  ulTPSVisibilityElemMem:UNSIGNED32; { memory taken by TPS vis elems }   
  ulTPSMemoTransElemMem: UNSIGNED32; { mem taken by TPS memo elems }   
  ulRcvEcbMem: UNSIGNED32; { mem taken by rcv ECBs (NLM) }   
  ulSendEcbMem: UNSIGNED32; { mem taken by send ECBs (NLM) }   
  ulWorkerThreadMem: UNSIGNED32; { mem taken by worker threads }   
end;