CREATE INDEX




Advantage Database Server 12  

CREATE INDEX

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CREATE INDEX  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - CREATE INDEX Advantage SQL Engine master\_Create\_index Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| CREATE INDEX  Advantage SQL Engine |  |  |  |  |

Creates an index on a table

Syntax

CREATE [ONLINE] [UNIQUE] INDEX <index-name> ON <table-name>

( <column-identifier>[ ASC | DESC ], ... ) <index-option> <index-option> ASC | DESC ], ... )

 

column-identifier ::= A user-defined column name.

index-name ::= A user-defined index name.

table-name ::= A user-defined table name.

index-option ::=

CANDIDATE |

NOTDELETED |

CONTENT |

IN FILE <filename> |

PAGESIZE <pagesize> |

MIN WORD <minwordlen> |

MAX WORD <maxwordlen> |

[NEW] DELIMITERS <delimiters> |

[NEW] DROPCHARS <dropchars> |

[NEW] NOISE <noisewords> |

[NEW] CONDITIONALS <conditionals> |

NOTMAINTAINED |

CASESENSITIVE

KEEPSCORE |

PROTECTNUMBERS

filename ::= A filename in which the new index will be placed

pagesize ::= 512..8192

minwordlen ::= integer

maxwordlen ::= integer

delimiters ::= character constant

noisewords ::= character constant

dropchars ::= character constant

conditionals ::= character constant

 

Remarks

ASC (ascending) is the default if neither ASC or DESC (descending) is provided.

If the table is a database table, that is, if the table is associated with an [Advantage Data Dictionary](master_advantage_data_dictionary.htm), the CREATE INDEX statement can only be executed by a user with ALTER permissions on the database table. The newly created index will become an auto-open index that is available to all database users.

The CANDIDATE option can be used with Advantage proprietary (ADT) and Visual FoxPro (VFP) tables to create a true unique index that prevents duplicate key values from being created. With ADT tables, the CANDIDATE option is equivalent to using the UNIQUE option. With VFP tables, though, the UNIQUE option does not create a true unique index; it only prevents duplicate keys from being added to the index, which means that if a record is updated to cause a unique key violation, that new record is not added to the index.

If the NOTDELETED option is provided, a condition of the form "!deleted()" will be added to the index to ensure that records marked for deletion are not referenced in the index. This option should be used when creating indexes for primary and foreign key indexes on VFP tables.  The NOTDELETED option has no affect with ADT tables, which do not store deleted records in indexes.

Many of the optional index-option values are used when creating full text search (FTS) indexes. See [Full Text Search Index Options](master_full_text_search_index_options_fts.htm), for the details about FTS indexes. The index-option values that can be used with all index types include <filename> and <pagesize> although <pagesize> is only used when creating indexes on ADT (Advantage proprietary) tables. The "IN FILE" option can only be used when creating tables that belong to data dictionaries. Otherwise the statement would create an index file that would not be opened when the table was used in an SQL statement.

The NEW keyword indicates if the delimiters, noise words, drop characters, and conditional drop characters are to replace or add to the default values. If NEW is provided with an option such as NOISE, then the given noise words will be used instead of the default noise words. If NEW is not provided, then the given noise words are added to the defaults.

The ONLINE keyword instructs the server to build the new index with the table open shared and allow other users to access or update the table during the build.  Without the ONLINE keyword no other user can have the table open during the build.  See [Online Table Maintenance](master_online_table_maintenance.htm) for more information.

Example(s)

Create a two-column ascending index:

CREATE INDEX empndx ON emp ( emp\_addr, emp\_name )

 

Create a descending index with unique key values:

CREATE UNIQUE INDEX empuniq ON emp ( emp\_id DESC)

 

Create a full text search (FTS) index that uses all the defaults and puts the index in the auto-open index file:

CREATE INDEX myindex ON mytable( mydocs ) CONTENT

 

Create a full text search index that specifies a page size and uses a specified index file:

CREATE INDEX myindex ON mytable( mydocs ) CONTENT IN FILE "myftsindex" PAGESIZE 1024

 

Create a full text search index that specifies minimum word length, maximum word length, extra tokenizing information, and tracks word counts:

CREATE INDEX myindex ON mytable ( mydocs ) CONTENT

MIN WORD 3

MAX WORD 20

DELIMITERS '{}()' // use default delims plus {}()

NOISE 'document' // use default noise plus "document"

NEW DROPCHARS ',.' // use only comma and period as drop chars

KEEPSCORE // track scoring information in the index file

Create a true unique index on either a Visual FoxPro table or an Advantage ADT table.

CREATE INDEX myindex ON mytable( emp\_id ) CANDIDATE