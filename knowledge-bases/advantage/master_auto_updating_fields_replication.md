Auto-Updating Fields




Advantage Database Server 12  

Auto-Updating Fields

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Auto-Updating Fields  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Auto-Updating Fields Advantage Concepts master\_Auto\_updating\_fields\_replication Advantage Concepts > Advantage Functionality > Replication > Auto-Updating Fields / Dear Support Staff, |  |
| Auto-Updating Fields  Advantage Concepts |  |  |  |  |

The use of auto-updating fields (autoinc, rowversion, and modtime) requires some special care with replication.

Auto-Increment Fields

When replicating a table with an autoinc field, Advantage disables enforcement of the autoinc field at the target. This means that if the source table has more records (and a higher auto-increment value) than the target and a new record is inserted, then the corresponding target record that is created through replication will have the same auto-increment value as the source table. This is the desirable behavior in most cases, however, it has some side effects you should consider:

|  |  |
| --- | --- |
| · | If the target table already has the same auto-increment value that is newly created in the source, the record may be added to the target with the duplicate auto-increment value. To prevent this possibility, create a unique index on the auto-increment field in the target table. |

|  |  |
| --- | --- |
| · | If two-way replication is being used and a record is appended at both the source and target at the same time, it is possible for the same auto-increment value to be generated at both the source and target and then be propagated to the corresponding source/target table. This will result in duplicate auto-increment values in both tables. Again, this can be prevented with a unique index. |

RowVersion and ModTime Fields

These field types are similar to autoinc fields in that Advantage automatically generates these values, but their usage in replication is different. Any update to the target table independent of the source table can cause the next rowversion value to get out of sync with the source. And because the modtime value is generated at the target, when the update occurs, there is very little chance that the modtime value of source and target tables will match. Because of this, modtime and rowversion values are not included in the computation of the CRC for detecting replication conflicts.

Likewise, it is probably not a good idea to use either of these types as any of the identification columns for replication. If the API AdsDDCreateArticle is used with the ADS\_IDENTIFY\_BY\_ALL option, it will not include modtime and rowversion columns.

See Also

[Replication Behind the Scenes](master_how_replication_works_internally.htm)