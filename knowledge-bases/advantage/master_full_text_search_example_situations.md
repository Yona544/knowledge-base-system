Full Text Search Example Situations




Advantage Database Server 12  

Full Text Search Example Situations

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Full Text Search Example Situations  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Full Text Search Example Situations Advantage Concepts master\_Full\_text\_search\_example\_situations Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Full Text Search Example Situations  Advantage Concepts |  |  |  |  |

The following are some specific situations and the corresponding settings that might be used to address them.

Numbers Only

Suppose you wanted to create an FTS index that tracked only numbers. This might be useful if you only plan to search for numbers in the field. The resulting index would take less disk space.

Solution #1

Add all other potential characters to the delimiter set. For example, the following statement will create an FTS index that uses the default delimiters (white space) plus additional characters. In addition, it sets the minimum word length to 2.

CREATE INDEX numbers ON thetable (thefield) CONTENT

min word 2

delimiters 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

Solution #2

Add the additional characters as DROP CHARACTERS. Semantically, this provides different functionality, however. For example, in the solution above, the text "123abc456" would result in two numbers "123" and "456". If the characters were used as drop characters, that text would result in a single number "123456".

Markup Languages

It is possible to create meaningful indexes on fields that store documents in various markup languages. For example, the following statement is a simplified version of one that might be used to create an index on a field that stores HTML text.

CREATE INDEX html ON thetable (thefield) CONTENT

 max word 50

 delimiters '<>{}=-:/|%?&'

 noise 'font family href html http https'