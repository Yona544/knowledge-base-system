Differences Between AOFs and Traditional Record Filters




Advantage Database Server 12  

Differences Between AOFs and Traditional Record Filters

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Differences Between AOFs and Traditional Record Filters  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Differences Between AOFs and Traditional Record Filters Advantage Concepts master\_Differences\_between\_aofs\_and\_traditional\_record\_filters Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Differences Between AOFs and Traditional Record Filters  Advantage Concepts |  |  |  |  |

There are three primary differences between AOFs and traditional record filters. The first is the speed. When using an AOF, it is usually very fast because records that do not pass the filter condition do not have to be read from the disk. Traditional record filters, on the other hand, must always read each record to determine if it passes the filter condition.

The second difference between AOFs and traditional record filters is the freshness of the data when using the Advantage Local Server. Traditional record filters are evaluated each time a record is requested. Therefore, they always provide an up-to-date view of the data. Once a fully optimized AOF has been built, it contains the bookmarks of the records that are in the filter. In general, the Advantage Database Server keeps the filter up-to-date whenever changes are made to the records in the table. There are two cases, however, where the filter can become out of date with respect to the actual data in the tables. The first is with Advantage Local Server. Any record change made by an application will cause all AOFs associated with that table within the application to be updated, but the change will not be propagated to other applications using the same table. The second case where an AOF could be out of date is with Advantage Database Server when using DBF tables and using compatibility locking mode. In that case, it would be possible for a third-party application to make a record update to a DBF that would not be detected by Advantage Database Server. Otherwise, AOFs and traditional record filters will be consistent with each other.

The third and final difference between AOFs and traditional record filters is AOFs can be set with different visibility options. Advantage supports three different types of AOFs:

|  |  |
| --- | --- |
| · | Dynamic AOFs: Filter membership is affected by modifications all users make to record data. |

|  |  |
| --- | --- |
| · | Keyset-Driven AOFs: Filter membership is only affected by updates from the filter owner (the table instance that set the filter). Updates made by other users will not affect a records membership in the filter. |

|  |  |
| --- | --- |
| · | Fixed AOFs: Filter membership does not change. If other users modify records they will always remain visible within this fixed filter, even if the changes have modified field values such that the record no longer passes the original filter expression. |

Note Dynamic filters are only supported when connected to the Advantage Database Server. If using the Advantage Local Server, dynamic filters will behave like keyset filters.

Relative speeds between the two types of filters depend on the number of records in a table, the number of records that pass a filter condition, the optimization level of the filter, and server speed. It is common, though, for fully optimized AOFs to return data sets 10 to 100 times faster than traditional record filters. The largest relative speed difference between the two types of filters will be seen when a small percentage of records pass the filter condition. For example, if a filter condition passes 1% of the records in a large table, a fully optimized AOF may be 10 times faster than a traditional record filter. With a filter condition that passes 99% of the records in a table, a fully optimized AOF will be only slightly faster than a traditional record filter.