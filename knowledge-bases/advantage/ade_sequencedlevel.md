SequencedLevel




Advantage Database Server 12  

TAdsDataSet.SequencedLevel

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsDataSet.SequencedLevel  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsDataSet.SequencedLevel Advantage TDataSet Descendant ade\_Sequencedlevel Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsDataSet.SequencedLevel  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm) [TAdsQuery](ade_tadsquery.htm) [TAdsStoredProc](ade_tadsstoredproc.htm)

Indicates what level of precision should be used when calculating sequenced record numbers.

Syntax

TAdsSequencedLevel = ( slStandard, slExact );

property SequencedLevel: TAdsSequencedLevel default slStandard;

Description

See [TAdsDataSet.Sequenced](ade_sequenced.htm) for details on sequenced record numbers. SequencedLevel is only used when the TAdsDataSet.Sequenced property is set to True.

If the SequencedLevel is set to slStandard, record numbers will be estimated using relative key position (which is the default behavior, and is acceptable for most situations). If the SequencedLevel is set to slExact, record numbers will be calculated using the key number, which will provide a more exact number, but will be much more expensive.

Some third-party components require an exact record number with no duplicates. If you are experiencing problems where you skip a record and the record position jumps around out of order, first try setting the Sequenced property to true and using a SequencedLevel of slStandard. If you still experience problems, try setting the SequencedLevel to slExact. IntraWeb is one set of components that have required the use of slExact. This does not mean it should be used with all IntraWeb applications.

Note The slExact setting is only recommended for situations where it is absolutely necessary. Using slExact can cause a significant loss of performance, depending on index size, if filters are set, etc.