Result Sets




Advantage Database Server 12  

Result Sets

Advantage JDBC Driver

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Result Sets  Advantage JDBC Driver |  |  | Feedback on: Advantage Database Server 12 - Result Sets Advantage JDBC Driver jdbc\_Result\_sets Advantage JDBC Driver > About the JDBC Driver > Result Sets / Dear Support Staff, |  |
| Result Sets  Advantage JDBC Driver |  |  |  |  |

The Advantage JDBC Driver supports scroll-insensitive, scroll-sensitive, updateable and read only result sets. The type and concurrency of the result set corresponds the type of cursor returned by the Advantage SQL engine. Advantage SQL engine returns 2 types of cursors, live and static. Their corresponding JDBC result set type and concurrency is listed in the following table. For more information on Advantage cursor type, see [Live versus Static Cursors](master_live_versus_static_cursors.htm).

|  |  |
| --- | --- |
| Advantage Cursor Type | JDBC Result Set |
| Live | scroll-sensitive, updatable/readonly |
| Static | scroll-insensitive, readonly |

When the Advantage JDBC driver cannot support the requested result set type or concurrency, it automatically downgrades the result set and generates one or more SQLWarnings with additional information.