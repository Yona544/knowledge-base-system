Caching Script Semantics




Advantage Database Server 12  

     Caching Script Semantics

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Caching Script Semantics  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Caching Script Semantics Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Caching\_Script\_Semantics Advantage Developer's Guide > Part II - Advantage SQL > Chapter 13 - SQL Scripting Language > Caching Script Semantics / Dear Support Staff, |  |
| Caching Script Semantics  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The performance of statements that are going to be executed repeatedly within your Advantage SQL script can be improved through caching. With Advantage SQL scripts, you can influence how aggressively statements are cached using the CACHE PREPARE keywords.

The default state for caching in Advantage SQL scripts is that any statement that does not hold open a table or make use of a string variable is cached. This setting, which is often sufficient for most scripts, provides performance improvements whenever statements are executed repeatedly, such as when they appear in a loop.

The reason that the default setting does not cache statements that hold open tables or use string variables is that these types of statements can sometimes cause problems when cached. For example, if a statement that holds a table open, such as an open cursor, is cached, it is impossible for another user to obtain an exclusive lock on that table until the cache is flushed.

The problem with statements that include string variables is related to the way that Advantage can dynamically resize strings. Since the size of a string variable is included in the information that is cached, if a cached statement is re-executed and the size of the string variable grows larger than the cached size, the statement may not execute correctly. This problem does not arise with Char type variables, as their size is fixed.

You can influence caching by either forcing Advantage to cache the statements in a script, or prohibiting Advantage from doing so. To force Advantage to cache statements, use the following command:

CACHE PREPARE ON;

To prohibit Advantage from caching, use this statement:

CACHE PREPARE OFF;

To return Advantage to its default caching state, use this command:

CACHE PREPARE DEFAULT;

If none of the statements in your Advantage SQL scripts are executed more than once, and therefore caching those statements will provide no benefit, you can use CACHE PREPARE OFF to disable caching for the script. By disabling caching, you reduce overall memory usage.

Using CACHE PREPARE ON is useful if you are using a string variable in a statement that gets executed repeatedly, but you know that the string's length will not change between executions. Another example of where it is useful is when you are holding open a table using a cursor while executing a parameterized query in a loop.

For most applications, the default caching mode is probably best. In those cases where you take explicit control over caching, you will likely do so for only a section of your code, returning caching to its default state once explicit control of the cache is no longer needed.