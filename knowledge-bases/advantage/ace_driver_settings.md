Driver Settings




Advantage Database Server 12  

Driver Settings

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Driver Settings  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - Driver Settings Advantage Client Engine ace\_Driver\_settings Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Driver Settings  Advantage Client Engine |  |  |  |  |

There are several driver setting options that are set globally for the Advantage Client Engine process. These include settings such as the epoch, whether to show deleted records, and the date format. These settings apply to all connections, tables, and indexes in the process.

Note that these functions AdsSetLastError, AdsGetLastError, AdsRegisterCallbackFunction, and AdsClearCallbackFunction work on a thread level rather than globally. For example, if thread A calls an Advantage Client Engine API and an error occurs, only thread A may call AdsGetLastError to retrieve the information for that error.