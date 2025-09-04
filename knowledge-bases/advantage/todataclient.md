TODataClient




Advantage Database Server 12  

TODataClient

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TODataClient |  |  | Feedback on: Advantage Database Server 12 - TODataClient TODataClient Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataClient / Dear Support Staff, |  |
| TODataClient |  |  |  |  |

To create a new instance of TODataClient drag and drop TODataClient on form in RAD Studio or by instantiating an instance in the code. You can modify the Authenticator property to a HTTPBasicAuthenticator and also add a BaseURL to which you can send the request and get the response. The credentials of the databse provided in the Base URL can be given using HTTPBasicAuthenticator Then modify TODataRequest and TODataSet to be associated with this client by setting its Client property to reference this new TODataClient component.