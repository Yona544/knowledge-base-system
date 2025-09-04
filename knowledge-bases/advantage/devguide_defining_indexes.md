Defining Indexes




Advantage Database Server 12  

     Defining Indexes

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Defining Indexes  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Defining Indexes Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Defining\_Indexes Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 3 - Defining Indexes > Defining Indexes / Dear Support Staff, |  |
| Defining Indexes  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

While a tables structure defines what kind of data it can hold, its a tables index files that influence how that data is accessed. Except in the most trivial of databases, a major design issue in most applications involves the definition of indexes. Done properly, index files can give your applications unparalleled speed and advanced features.

This chapter provides you with an overview of index files. It begins with an introduction to the terms used to describe indexes. It continues with a look at the various types of indexes supported by Advantage, as well as how to create and test indexes for your tables.

Towards the end of this chapter, you will find a detailed discussion of a special type of index called an FTS index. FTS stands for full text search, and these indexes permit you to quickly locate records based on the contents of text fields, including memo and binary fields.