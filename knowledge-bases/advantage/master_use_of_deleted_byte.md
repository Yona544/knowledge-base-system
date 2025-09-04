Use of Deleted Byte




Advantage Database Server 12  

Use of Deleted Byte

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Use of Deleted Byte  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Use of Deleted Byte Advantage Concepts master\_Use\_of\_deleted\_byte Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Use of Deleted Byte  Advantage Concepts |  |  |  |  |

Advantage TPS, as a default, uses the "deleted" byte in a DBF table record to indicate that the record has an update or insert pending within a transaction. This does not affect the deletion status of the record. If you would like to keep the "deleted" byte from being temporarily altered, a one byte character field with the name "AXS\_TPS" can be added to any DBF table being used with TPS. The AXS\_TPS field would then be used by the Advantage TPS rather than the "deleted" byte.

Note Use of the "deleted" byte and the optional "AXS\_TPS" field only applies to DBF tables. Advantage proprietary ADT tables do not have the same concept of a "deleted" byte.