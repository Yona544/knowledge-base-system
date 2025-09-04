AdsInitRawKey




Advantage Database Server 12  

AdsInitRawKey

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsInitRawKey  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsInitRawKey Advantage Client Engine ace\_Adsinitrawkey Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsInitRawKey  Advantage Client Engine |  |  |  |  |

Initializes the creation of a raw key that can be used with the ADS\_RAWKEY data type in calls to [AdsSeek](ace_adsseek.htm), [AdsSeekLast](ace_adsseeklast.htm), [AdsLookupKey](ace_adslookupkey.htm), and [AdsSetScope](ace_adssetscope.htm).

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsInitRawKey(ADSHANDLE hIndex); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order. |

Remarks

After calling AdsInitRawKey, make calls to the "AdsSet" APIs to set field values for the key with an hIndex handle instead of the usual hTable handle. After the desired fields have been set, call [AdsBuildRawKey](ace_adsbuildrawkey.htm). For example, the following sequence of calls might be used to build a raw seek key for an index built on "lastname+firstname":

ulRet = AdsInitRawKey( hIndex );

ulRet = AdsSetString( hIndex, "lastname", "Adams", 5 );

ulRet = AdsSetString( hIndex, "firstname", "John", 4 );

usKeyLen = sizeof( aucKey );

ulRet = AdsBuildRawKey( hIndex, aucKey, &usKeyLen );

ulRet = AdsSeek( hIndex, aucKey, usKeyLen, ADS\_RAWKEY, ADS\_HARDSEEK, &pbFound);

Note that any fields that are not set, will be "empty". The right-most field that is set determines the actual key length. If in the above example both lastname and firstname fields are 20 characters long, then the key created above would be 24 characters long. If an index is "f1;f2;f3" and only fields f1 and f3 were set, then the final key will include "blanks" for f2.

Example

[Click Here](ace_examples.htm#adsinitrawkeyexample)

See Also

[AdsBuildRawKey](ace_adsbuildrawkey.htm)

[AdsSeek](ace_adsseek.htm)

[AdsSeekLast](ace_adsseeklast.htm)

[AdsSetScope](ace_adssetscope.htm)

[AdsLookupKey](ace_adslookupkey.htm)

[AdsSetDate](ace_adssetdate.htm)

[AdsSetDouble](ace_adssetdouble.htm)

[AdsSetEmpty](ace_adssetempty.htm)

[AdsSetField](ace_adssetfield.htm)

[AdsSetJulian](ace_adssetjulian.htm)

[AdsSetLogical](ace_adssetlogical.htm)

[AdsSetLong](ace_adssetlong.htm)

[AdsSetMilliseconds](ace_adssetmilliseconds.htm)

[AdsSetRecord](ace_adssetrecord.htm)

[AdsSetShort](ace_adssetshort.htm)

[AdsSetString](ace_adssetstring.htm)

[AdsSetTime](ace_adssettime.htm)