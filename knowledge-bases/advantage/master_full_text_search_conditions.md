Full Text Search Conditions




Advantage Database Server 12  

Full Text Search Conditions

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Full Text Search Conditions  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Full Text Search Conditions Advantage Concepts master\_Full\_text\_search\_conditions Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Full Text Search Conditions  Advantage Concepts |  |  |  |  |

The search conditions used for full text searches are character strings composed of words, phrases, logical operators, and parentheses for grouping precedence.

Aside from white space characters, which are considered to be delimiters in search strings, special characters include the double quote (0x22) used for delimiting phrases, the asterisk (0x2A) used for prefix, postfix, and substring matching, and parentheses (0x28 and 0x29). The reserved words include the logical operators OR, AND, NOT, NEAR.

The precedence of the logical operators from lowest to highest is OR, AND, NOT, NEAR. You can use parentheses to change the precedence grouping. For example, the search condition meeting and request or changelog finds records that have both the words "meeting" and "request" or the word "changelog". Changing the precedence with parentheses to meeting and (request or changelog) causes the search condition to find records that have the word "meeting" and either of the words "request" or "changelong".

The logical OR operator produces a "true" result when either operand evaluates to true. The logical AND operator produces a true result only when both of its operands evaluate to true. The logical NOT operator produces a true result when its single operand has a false result. The NEAR operator (proximity operator) is similar to the AND operator in that both of its operands must be found. In addition, it requires that its operands be within a certain physical distance of each other for it to return a true result. The default distance for the NEAR operator is 8 words. To use a proximity value other than the default, specify the distance as a parameter to the NEAR operator. For example medical near(15) doctor will evaluate to true for records where the word "medical" is within 15 words of "doctor".

Search words that do not have logical operators specified are assumed to have an implied AND operator between them. For example, the following two search conditions are equivalent:

mechanical engineer

mechanical AND engineer

And the following two are equivalent:

computer programmer or software developer

(computer AND programmer) OR (software AND developer)

Individual search words that are not enclosed in double quotes can be searched for as exact matches, prefix matches, postfix matches, or substring matches. This behavior is controlled through the use of the asterisk (\*) character.

|  |  |
| --- | --- |
| · | Exact match. Simply specify the word in the search condition. The word will be matched if it is found exactly as given in the text. For example, the search word "special" will match only "special" in the text (or upper case versions if it is not a case sensitive index). |

|  |  |
| --- | --- |
| · | Prefix match. Place an asterisk at the end of the word to match all words that begin with the given characters. For example, the search word "special\*" will match "special", "specialty", "specialization", etc. |

|  |  |
| --- | --- |
| · | Postfix match. Place an asterisk at the beginning of the word to match all words that end with the given characters. For example, the search word "\*ation" will match words "station", "specialization", "citation", etc. |

|  |  |
| --- | --- |
| · | Substring match. Place an asterisk at both the beginning and end of the word to match all words that contain the given characters. For example, the search word "\*lock\*" will match the words "locker", "antilock", "blocking", etc. |

Important Note Exact matches and prefix matches provide the best performance. Both postfix and substring matches require that the entire FTS index be scanned in order to satisfy the search. This is still much more efficient than searching the actual data, but it is less efficient than prefix and exact matches, which can be resolved with O(Log N) searches.

Double quotes are used as phrase delimiters. In addition, special characters can be enclosed inside double quotes to ensure that they are unchanged by the search condition parser. For example, to search for a parenthesis, it is necessary to enclose it in double quotes in order to keep it from being treated as a precedence operator in the search condition itself. To search for a physical double quote, use two of them in a row.

Single quotes are not treated as a special case by the FTS parser, but they are the text delimiter in SQL statements. This means that if you use single quotes inside FTS search conditions in an SQL statement, you must include two of them in a row.

Spaces are considered to be delimiters in search conditions. If you have a special situation in which spaces are not delimiters in the text and are part of search words, then it may be necessary to enclose the search words in double quotes in order to preserve the spaces.

Multi-word phrases in search conditions match identical phrases in the text being searched. For example, the search condition "alpine skiing" will match only records that have the exact words "alpine" and "skiing" in that order in the text with no other non-noise words between them.

If you use the NEAR operator with sub-expressions, you may need to use the optional form of the operator with the parentheses after it to avoid ambiguity in the expression. For example, the condition "a near (b and c)" is not valid because the left parenthesis is interpreted as the opening of the NEAR proximity parameter. The condition would need to be written as "a near() (b and c)". The empty parentheses after the NEAR operator remove the ambiguity; because they are empty, the default proximity value is used. You can also specify a proximity value: "a near(25) (b and c)".

The following is a more formal grammar definition for the search conditions. The square brackets indicate optional items.

search-condition ::= <and-term> | <and-term> OR <search-condition>

and-term ::= <not-term> | <not-term> [AND] <and-term>

not-term ::= <near-term> | NOT <near-term>

near-term ::= <value-term> | <value-term> NEAR [<near-distance>] <near-term>

near-distance ::= ( [integer] )

value-term ::= ( <condition> ) | <simple-term>

simple-term ::= text | text\* | \*text | \*text\* | "phrase"