FIPS




Advantage Database Server 12  

FIPS

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| FIPS  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - FIPS Advantage Database Server Master\_FIPS\_Config Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| FIPS  Advantage Database Server |  |  |  |  |

Default = 0, Range 0 - 1

Setting the FIPS configuration value to 1 causes the server to run in a mode compliant with the Federal Information Processing Standard (FIPS) 140-2. When this is enabled, clients that connect to the server must also be running in FIPS mode.

This option requires the FIPS Encryption Security Option, which is an add-on that can be purchased separately. Please contact your Advantage sales representative or visit www.AdvantageDatabase.com for additional licensing information.

When running in FIPS mode, any attempts by an application to make use of [cryptographic functionality](master_encryption.htm) that is not approved for FIPS usage will result in an error. For example, an attempt to open a table encrypted with the default encryption algorithm will result in an error being returned to the client.

This option can also be specified on the command line when starting the server with the -FIPS option.