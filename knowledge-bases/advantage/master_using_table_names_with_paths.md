Using Table Names with Paths




Advantage Database Server 12  

Using Table Names with Paths

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using Table Names with Paths  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Using Table Names with Paths Advantage SQL Engine master\_Using\_table\_names\_with\_paths Advantage SQL > SQL Functionality > Using Table Names with Paths / Dear Support Staff, |  |
| Using Table Names with Paths  Advantage SQL Engine |  |  |  |  |

Drive letters in paths of table names can only be used with Advantage Local Server. When using Advantage Database Server for NT, fully qualified paths must use UNC (e.g., "\\server\volume\path\table"), because the SQL statement is parsed at the server where client-side drive letters are not meaningful. Note that tables referenced like this must be enclosed in double quotes or [] (brackets) because they contain non-standard characters (see [Use of Non-Standard Characters in Names](master_use_of_non_standard_characters_in_names.htm)).

If relative paths are used in SQL statements, the path is considered to be relative to the connection path. For example, a table referenced as "..\alternate\info" would refer to a directory named "alternate" that would be expected to be parallel to the original connection path directory.