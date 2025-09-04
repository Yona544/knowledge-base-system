AdsExtendedReader.ClearRange




Advantage Database Server 12  

AdsExtendedReader.ClearRange

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.ClearRange  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.ClearRange Advantage .NET Data Provider dotnet\_Adsextendedreader\_clearrange Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.ClearRange / Dear Support Staff, |  |
| AdsExtendedReader.ClearRange  Advantage .NET Data Provider |  |  |  |  |

Clears top and bottom range values on the index order.

public void ClearRange();

Remarks

This method clears both the top and bottom range values on the active index order. After calling this method, the reader will be positioned at BOF (beginning of file) so that a call to Read() will then go to the first record.

See Also

[SetRange](dotnet_adsextendedreader_setrange.htm)