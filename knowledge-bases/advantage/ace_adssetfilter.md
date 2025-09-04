AdsSetFilter




Advantage Database Server 12  

AdsSetFilter / AdsSetFilter100

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetFilter / AdsSetFilter100  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetFilter / AdsSetFilter100 Advantage Client Engine ace\_Adssetfilter Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetFilter / AdsSetFilter100  Advantage Client Engine |  |  |  |  |

Sets a filter on the given table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetFilter ( ADSHANDLE hTable,                UNSIGNED8 \*pucFilter); |
| UNSIGNED32 | AdsSetFilter100( ADSHANDLE hTable,                  VOID        \*pvFilter                  UNSIGNED32  ulOptions ); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucFilter (I) | Filter expression given as a null terminated ANSI/OEM code page encoded string. If there is an existing filter on the given table, it is replaced with the new filter. This affects subsequent record movements other than AdsGotoRecord. |
| pvFilter (I) | Filter expression given as a null terminated string that is encoded based on the ulOptions. |
| ulOptions (I) | This is a bit field for defining the options for the filter. The options are:    ADS\_ENCODE\_UTF8: The string specified by pvFilter is encoded in UTF8. This option is mutually exclusive with the ADS\_ENCODE\_UTF16 option.    ADS\_ENCODE\_UTF16: The string specified by pvFilter is encoded in UTF-16LE. This option is mutually exclusive with the ADS\_ENCODE\_UTF8 option. |

Remarks

Setting a filter through AdsSetFilter  or AdsSetFilter100 allows only the records that pass the filter expression to be visible. The filter expression must result in a boolean True or False. After setting a filter, the table may still be positioned on a record that does not pass the filter. To activate the filter, perform an [AdsGotoTop](ace_adsgototop.htm) or some other movement function.

For AdsSetFilter100, if neither ADS\_ENCODE\_UTF8 nor ADS\_ENCODE\_UTF16 is specified in the ulOptions, the pvFilter should be encoded using ANSI/OEM code page of the table.

See [Advantage Expression Engine](master_advantage_expression_engine.htm) for a list of functions supported by the Advantage Expression Engine.

AdsSetFilter and AdsSetFilter100 do not utilize the Advantage Optimized Filters functionality. It is recommended you use the [AdsSetAOF](ace_adssetaof.htm) or [AdsSetAOF100](ace_adssetaof.htm) function.

Example

[Click Here](ace_examples.htm#adssetfilterexample)

See Also

[AdsGetFilter](ace_adsgetfilter.htm)

[AdsClearFilter](ace_adsclearfilter.htm)

[AdsSetAOF](ace_adssetaof.htm)

[AdsSetAOF100](ace_adssetaof.htm)