Using JSON.NET




Advantage Database Server 12  

Using JSON.NET

Advantage Web Platform

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using JSON.NET  Advantage Web Platform |  |  | Feedback on: Advantage Database Server 12 - Using JSON.NET Advantage Web Platform web\_Using\_JSON.NET Advantage Web Development > Advantage Web Platform > Using JSON.NET / Dear Support Staff, |  |
| Using JSON.NET  Advantage Web Platform |  |  |  |  |

By default, JSON.NET generates a Microsoft-specific date representation (as the JSON spec does not specify how dates are to be represented). See <http://weblogs.asp.net/bleroy/archive/2008/01/18/dates-and-json.aspx> for details and their motivation.

The Advantage Web Platform uses the ISO 8601 specification. JSON.NET supports different formatters to easily handle these kinds of differences. To serialize an object to JSON and get ISO 8601 dates, simply specify you want to use a new instance of the IsoDateTimeConverter:

string json\_row = JsonConvert.SerializeObject( list.d.results[0], new IsoDateTimeConverter() );

You will need to add Newtonsoft.Json.Converters to your uses clause in order to resolve the IsoDateTimeConverter.

Note that if a field name in the data being retrieved contains spaces, you will need to refer to the name using underscores in place of spaces. The server replaces spaces in field names with underscores prior to returning the data to the client.

More details can be found on James' blog here: <http://james.newtonking.com/archive/2009/02/20/good-date-times-with-json-net.aspx>