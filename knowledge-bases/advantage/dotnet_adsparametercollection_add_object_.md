AdsParameterCollection.Add( object )




Advantage Database Server 12  

AdsParameterCollection.Add( object )

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsParameterCollection.Add( object )  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsParameterCollection.Add( object ) Advantage .NET Data Provider dotnet\_Adsparametercollection\_add\_object\_ Advantage .NET Data Provider > AdsParameterCollection Class > AdsParameterCollection Methods > AdsParameterCollection.Add( object ) / Dear Support Staff, |  |
| AdsParameterCollection.Add( object )  Advantage .NET Data Provider |  |  |  |  |

Adds the given [AdsParameter](dotnet_adsparameter.htm) to the collection.

public int Add( object value );

Remarks

The method returns the collection index of the newly added parameter. If the value is not of type AdsParameter, an InvalidCastException will be thrown.