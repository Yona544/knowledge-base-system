StoreConnected




Advantage Database Server 12  

TAdsConnection.StoreConnected

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.StoreConnected  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.StoreConnected Advantage TDataSet Descendant ade\_Storeconnected Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.StoreConnected  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Syntax

property StoreConnected : Boolean read FbStoreConnected write FbStoreConnected default TRUE;

Description

The StoreConnected property specifies whether or not the TAdsConnection.IsConnected property is written to the DFM file when the form is saved.

The default value of the StoreConnected property is True.

If you prefer the IsConnected property never be saved with a form, create a TAdsConnection descendant and set the FbStoreConnected member variable to False in the constructor.

See Also

[StoreActive](ade_storeactive.htm)