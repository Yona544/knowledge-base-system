---
title: Ace Adsmggetworkerthreadactivity
slug: ace_adsmggetworkerthreadactivity
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsmggetworkerthreadactivity.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: b5e836e67f64b6c7d96f06cef0de92d4338d67a6
---

# Ace Adsmggetworkerthreadactivity

AdsMgGetWorkerThreadActivity

AdsMgGetWorkerThreadActivity

Advantage Client Engine

| AdsMgGetWorkerThreadActivity  Advantage Client Engine |  |  |  |  |

Returns an array of information about worker threads that are actively processing an operation on the Advantage Database Server

Syntax

| UNSIGNED32 | AdsMgGetWorkerThreadActivity (ADSHANDLE hMgmtConnect,  ADS\_MGMT\_THREAD\_ACTIVITY astWorkerThreadActivity[],  UNSIGNED16 \*pusArrayLen,  UNSIGNED16 \*pusStructSize); |

Parameters

| hMgmtConnect (I) | Management API connection handle of server to get worker thread activity. |
| astWorkerThreadActivity (O) | Returned array of worker thread activity structures. |
| pusArrayLen (I/O) | Number of array elements in astWorkerThreadActivity on input. On output, number of astWorkerThreadActivity array elements filled with worker thread activity information by the Advantage Database Server. |
| pusStructSize (I/O) | Size (in bytes) of each astWorkerThreadActivity array element structure on input. On output, size of ADS\_MGMT\_THREAD\_ACTIVITY structure on the Advantage Database Server. |

Remarks

AdsMgGetWorkerThreadActivity returns an array of structures containing information about worker threads that are currently processing an operation on the Advantage Database Server. Examples Advantage of operations include skip, seek, build index, and open table. Most Advantage operations take almost no time at all to complete on the Advantage Database Server. A few operations, such as build index, may take more than a few milliseconds to complete. Since most Advantage operations take a very short time to complete, the result of an AdsMgGetWorkerThreadActivity call will often indicate that no worker threads (other than the worker thread currently processing this AdsMgGetWorkerThreadActivity operation) are busy.

The number of elements in astWorkerThreadActivity, which is the value to be input in pusArrayLen, needs to be large enough to hold all possible worker threads that could be active. If more worker threads are active than are specified in pusArrayLen, then only information about the first pusArrayLen number of worker threads will be returned in astWorkerThreadActivity. Information about the remaining worker threads will not be returned, and pusArrayLen will be returned with the same value that was input. If fewer worker threads are active than are specified in pusArrayLen, then not all elements in the astWorkerThreadActivity array will be filled. The value returned in pusArrayLen will indicate how many elements in the astWorkerThreadActivity array were filled. The remaining, unfilled elements at the end of the astWorkerThreadActivity array will be left unchanged. The maximum number of worker threads that can be active is equal the number of worker threads configured to be used by the Advantage Database Server. The default number of worker threads that is configured to be used by the Advantage Database Server is 8.

It is possible that the size of the ADS\_MGMT\_THREAD\_ACTIVITY structure will increase in future releases of Advantage. Since it is possible to use a newer version of the Advantage Database Server with an older version of the Advantage Client Engine, any new and additional worker thread activity information that may exist if using a newer version of the Advantage Database Server will not be returned in each element of the astWorkerThreadActivity array. Each element in the array of astWorkerThreadActivity structures will only be filled with the amount of data specified in pusStructSize. The value returned in the pusStructSize parameter is the size of the ADS\_MGMT\_THREAD\_ACTIVITY structure in the current version of the Advantage Database Server. If the size of each element in the astWorkerThreadActivity structure input in pusStructSize is the same as the size returned in pusStructSize, then the Advantage client has received all possible worker thread activity information.

Since it is possible that the size of the ADS\_MGMT\_THREAD\_ACTIVITY structure will increase in future releases of Advantage, it is highly recommended that on input the pusStructSize parameter is literally initialized with sizeof ( ADS\_MGMT\_THREAD\_ACTIVITY ) rather than being initialized with a literal value.

The ulThreadNumber member of ADS\_MGMT\_THREAD\_ACTIVITY is the Advantage Database Server internal thread number.

The usOpcode member of ADS\_MGMT\_THREAD\_ACTIVITY is a value indicating the Advantage operation currently being performed.

The aucUserName member of ADS\_MGMT\_THREAD\_ACTIVITY is the Advantage client's computer name.

The aucOSUserLoginName member of ADS\_MGMT\_THREAD\_ACTIVITY is the Advantage client's operating system login name.

Note AdsMgGetWorkerThreadActivity will not return any information when used with the Advantage Local Server.

Example

[Click Here](ace_advantage_management_api_examples.md#adsmggetworkerthreadactivity_example)

See Also

[AdsMgConnect](ace_adsmgconnect.md)

[ADS\_MGMT\_THREAD\_ACTIVITY](ace_ads_mgmt_thread_activity.md)
