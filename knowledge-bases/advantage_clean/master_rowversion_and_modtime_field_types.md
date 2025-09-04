---
title: Master Rowversion And Modtime Field Types
slug: master_rowversion_and_modtime_field_types
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_rowversion_and_modtime_field_types.htm
source: Advantage CHM
tags:
  - master
checksum: cb255cd64f2949dc377792ed0eeb5b706c0273a6
---

# Master Rowversion And Modtime Field Types

RowVersion and ModTime Field Types

RowVersion and ModTime Field Types

Advantage Concepts

| RowVersion and ModTime Field Types  Advantage Concepts |  |  |  |  |

The RowVersion and ModTime field types are field types that are automatically updated by the Advantage Database Server. For simplicity's sake, these field types are not read-only, however, values written to these fields by the client will not be stored in the table. Rather, the Advantage Database Server will create new values when a record is updated just before the record is written to the table.

RowVersion

The RowVersion field type is a 64-bit unsigned auto-incrementing integer that is incremented each time a record is updated. The RowVersion field value is unique to the entire table with the last updated record containing the largest RowVersion value. The primary purpose of the RowVersion field type is for use with optimistic concurrency. Optimistic concurrency is a mechanism used to guarantee record updates are not overwritten in a multi-user environment. Take for example, two users of a database:

User1 and User2 are viewing the same record of a table. User1 updates the record. If User2 updates the same record, User1's updates will be lost.

To implement optimistic concurrency using the RowVersion field type, User2 would first verify that the current RowVersion value in the record is the same as the value in the record it is viewing before performing the update. This is usually implemented using an SQL update statement. An example update statement might be:

UPDATE customers SET acctBalance = :newbalance WHERE rowver = :oldRowVersion

where the oldRowVersion parameter is the RowVersion value in the record that the user is viewing. If the RowVersion values don't match, no update is performed. The application can then tell no update was performed by checking number of affected rows of the update statement and act accordingly.

ModTime

The ModTime field type is a timestamp type field which is automatically updated with the current date and time when a record is updated.

Development Notes

- Conditional indexes will not respect the new RowVersion or ModTime values because the index condition is evaluated before the new RowVersion or ModTime values are created. It is recommended that conditional index expressions not contain references to either of these field types.

- Minimum, maximum, and default field values are not allowed on either of these field types.

- Record level validation expressions will be evaluated using the RowVersion and ModTime values stored in the client. These values will likely change as the server will compute new ones prior to writing the record to the table.

- Performing a zap on a table will reset the RowVersion value in the table header to zero.

- Because RowVersion and ModTime field values are updated by the Advantage Database Server, the client will not show the new record data until the record is refreshed.

- A slight performance hit will be incurred with both of these field types, as the Advantage Database Server will need to compute new values and modify the record and index keys as necessary. For ModTime fields, the performance hit will be extremely small. For RowVersion fields, more work is needed to maintain the correct RowVersion value for all users of the table. This involves writing extra data to the table header at update time. Advantage Local Server will incur a bigger performance hit as it reads and writes to the table header more often to maintain data integrity.

- The timestamp value used by the ModTime field type is computed using the server's operating system C Library time functions. Depending on the platform's implementation of these functions, the granularity of the timestamp value may vary.
