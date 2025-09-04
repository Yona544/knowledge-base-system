AdsExtendedReader.ActiveIndex




Advantage Database Server 12  

AdsExtendedReader.ActiveIndex

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.ActiveIndex  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.ActiveIndex Advantage .NET Data Provider dotnet\_Adsextendedreader\_activeindex Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Properties > AdsExtendedReader.ActiveIndex / Dear Support Staff, |  |
| AdsExtendedReader.ActiveIndex  Advantage .NET Data Provider |  |  |  |  |

Gets or sets the index order by name.

public string ActiveIndex{ get; set; }

Remarks

This property can be used to retrieve or set the index order. For non-compound indexes, the index order name is the base of the filename (up to 8 characters). For compound indexes, the index order name is the tag name (up to 10 characters).

An exception will be thrown if trying to retrieve an ActiveIndex name when the active handle is not an index handle.

If a null or empty string is given, the order will revert to the natural order.

After setting or clearing the active index, the reader will be positioned at BOF (beginning of file) so that a call to Read() will then go to the first record.