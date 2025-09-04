ExtraConnectString




Advantage Database Server 12  

TAdsConnection.ExtraConnectString

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.ExtraConnectString  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.ExtraConnectString Advantage TDataSet Descendant ade\_extraconnectstring\_tadscon Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.ExtraConnectString  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

A supplemental connection string that, if specified, will be appended to the end of the automatically-generated connection string (that is built based on the other configured settings in the Connection component).  This provides a flexible way to specify additional settings that are not currently exposed as properties on the TAdsConnection component, like [DateFormat](ade_dateformat_tadsconnection.htm), Decimals, ShowDeleted, and Connection Pooling options.

Syntax

property ExtraConnectString: String;

Description

Use ExtraConnectString to specify a set of additional connection string options that will be used when connecting.  See [AdsConnect101](ace_adsconnect101.htm) help file topic for information on the connection string options that are available.

Remarks

The ExtraConnectString parameter allows a wide variety of options to be specified -- some of which are not directly related to making a connection.  Users wishing to avoid the use of the AdsSettings component should consider specifying connection-level options that will eliminate the need for the AdsSettings component.  (Specifically, the Decimals, ShowDeleted, and DateFormat properties of the connection string can replace the corresponding settings in the AdsSettings component.)

Example

ExtraConnectString := 'Epoch=2000;TableType=CDX;ShowDeleted=FALSE;DateFormat=DD/MM/YYYY;'

See Also

[AdsConnect101](ace_adsconnect101.htm)

[TAdsSettings](ade_tadssettings_7.htm)