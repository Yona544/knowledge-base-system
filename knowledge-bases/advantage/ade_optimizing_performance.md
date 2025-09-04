Optimizing Performance




Advantage Database Server 12  

Optimizing Performance

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Optimizing Performance  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Optimizing Performance Advantage TDataSet Descendant ade\_Optimizing\_performance Advantage TDataSet Descendant > Developing and Distributing Applications > Optimizing Performance / Dear Support Staff, |  |
| Optimizing Performance  Advantage TDataSet Descendant |  |  |  |  |

Setting Advantage Optimized Filters

Use of Advantage Optimized Filters (AOFs) rather than traditional record filters is the default filter type used by the Filter property inherited from native Delphi in TAdsTable. For more informtion see [Advantage Optimized Filters](master_advantage_optimized_filters.htm). The optimization of a filter occurs by setting up the correct indexes. To setup indexes properly for optimization, create single column indexes on each segment of the filter expression. For example, using a filter on a field LastName and DateOfBirth, to see how many people with the last name "Smith" were born after 11/20/1945, use the following filter:

AdsTable1.Filter := 'LastName = "Smith" And DateOfBirth > ctod("11/20/1945")';

AdsTable1.Filtered := True;

In order for the AOF to be fully optimized, an index would need to be built on LastName and an index on DateOfBirth. For example:

|  |  |
| --- | --- |
| Index Order Name | Index Key Expression |
| LName | LastName |
| DOB | DateOfBirth |

The server will use both of the index orders to fully optimize the filter.

Keep in mind that changes made by other users to records in the table that affect inclusion in the AOF are not automatically reflected in the AOF. To use traditional record filters with the TAdsTable.Filter property rather than AOFs, set the [AdsOptimizedFilters](ade_adsoptimizedfilters.htm) subproperty to False.

Setting Indexes

It is recommended to set the active index by setting the property IndexName to the index order name of the appropriate file. Setting the property IndexFieldNames will also work, but knowing the index order name seems more intuitive especially for multiple field index expressions.

Note If an active index is set and a filter operation seems slow, clearing the index before the operation and resetting the index after the operation is recommended. An example of increased performance by clearing the active index is in getting a record count on a filtered dataset when using the Advantage Optimized Filters. If an active index is set, the count will have to skip through the index pages as well as the bitmap for the Advantage Optimized Filter to determine the result. If there is no active index, no index pages need to be read.

Opening Tables at Startup

It is recommended to open all tables at the start of each application. Opening and closing tables can cause performance degradation while the application is running. Since the Advantage Database Server actually opens the tables, there are few file handles used on the client. Thus, number of file handles used is also not an issue.

Speed Strategies for Data-Aware Controls

In order to improve performance when doing intensive database engine work, it may be necessary to break some data aware control links to the dataset. This may increase performance by up to 50%. This performance increase is due to the graphical update to the controls not having to take place. Below is a code example that was tested on a table with 1000 records, with 65 of those records matching the filter criteria. This filter is fully optimized because an index has been built on the field DEPTNUM.

procedure TForm1.Button1Click(Sender: TObject);

var

iCount, kCount : integer;

bFound : boolean;

dStart, dStop : Double;

begin

AdsTable1.Filtered := False;

AdsTable1.Filter := 'DEPTNUM = 14';

// AdsTable1.DisableControls;

dStart := GetTickCount;

for iCount := 0 to 30 do

begin

kCount := 0;

AdsTable1.First;

bFound := AdsTable1.FindFirst;

while ( bFound ) and Not( AdsTable1.EOF ) do

begin

bFound := AdsTable1.FindNext;

kCount := kCount + 1;

end;

end;

dStop := GetTickCount;

showmessage('Time Elapsed is = ' + FloatToStr( dStop - dStart ) );

end;

This code was tested in three different scenarios.

|  |  |
| --- | --- |
| 1. | The DBGrid and DataSource components were linked together and the DataSource component was linked to the AdsTable |

|  |  |
| --- | --- |
| 2. | The same situation as the first except a line of code was added ( "AdsTable1.DisableControls") before the timings began. |

|  |  |
| --- | --- |
| 3. | The DBGrid and DataSource components were still linked together, but the DataSource link to the AdsTable component was dropped. The line "AdsTable1.DisableControls" was removed for test three. |

The following test results were observed:

|  |  |
| --- | --- |
| · | Test #1 - 11.5 sec. |

|  |  |
| --- | --- |
| · | Test #2 - 10 sec. |

|  |  |
| --- | --- |
| · | Test #3 - 5.5 sec. |

The greatest performance increase results from removing the link from any DataSource components to the dataset. This is faster than simply disabling controls because although the graphics are not getting updated, the internal buffers are still allocated in the dataset and are being updated with every refresh. A problem with removing the link is that the controls will seem to be empty. To overcome this, hide the form and display that some type of processing is taking place. It would probably take just as much time for this example to work around the issues of removing the link from the DataSource component to the dataset, but in a much larger setting this is still very applicable.

Why Deleted Records Slow Down Access

Advantage implements not showing deleted records in DBF tables via record filtering performed on the server. In a very large DBF table with many deleted records, movement operations will be slower than if there were no deleted records. There are a few ways to help performance when not showing deleted records in DBF tables:

|  |  |
| --- | --- |
| 1. | Periodically Pack your tables |

|  |  |
| --- | --- |
| 2. | Add the FOR clause "NOT Deleted" to all index orders |

|  |  |
| --- | --- |
| 3. | If filtering records and using Advantage Optimized Filters (AOFs), it is recommended to create an index with the key expression "Not Deleted()" or "Deleted()". This will cause the AOF to automatically filter out records that are marked for deletion. |

If the ShowDeleted setting is set to show deleted records, these slow performance issues are not a factor. By default the deleted records are not shown.

Note Deleted record performance problems are not an issue with ADT tables due to the record reuse algorithms used by Advantage with ADT tables, and because keys for deleted records are not stored in ADI indexes.