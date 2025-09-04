---
title: Web Using Json Net
slug: web_using_json_net
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: web_using_json_net.htm
source: Advantage CHM
tags:
  - web
checksum: 1260baf01fb7d6ff8592b4c715281950c09fe278
---

# Web Using Json Net

Using JSON.NET

Using JSON.NET

Advantage Web Platform

| Using JSON.NET  Advantage Web Platform |  |  |  |  |

By default, JSON.NET generates a Microsoft-specific date representation (as the JSON spec does not specify how dates are to be represented). See <http://weblogs.asp.net/bleroy/archive/2008/01/18/dates-and-json.aspx> for details and their motivation.

The Advantage Web Platform uses the ISO 8601 specification. JSON.NET supports different formatters to easily handle these kinds of differences. To serialize an object to JSON and get ISO 8601 dates, simply specify you want to use a new instance of the IsoDateTimeConverter:

string json\_row = JsonConvert.SerializeObject( list.d.results[0], new IsoDateTimeConverter() );

You will need to add Newtonsoft.Json.Converters to your uses clause in order to resolve the IsoDateTimeConverter.

Note that if a field name in the data being retrieved contains spaces, you will need to refer to the name using underscores in place of spaces. The server replaces spaces in field names with underscores prior to returning the data to the client.

More details can be found on James' blog here: <http://james.newtonking.com/archive/2009/02/20/good-date-times-with-json-net.aspx>
