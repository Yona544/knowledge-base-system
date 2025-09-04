Full Text Search Index Options




Advantage Database Server 12  

Full Text Search Index Options

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Full Text Search Index Options  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Full Text Search Index Options Advantage Concepts master\_Full\_text\_search\_index\_options\_fts Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Full Text Search Index Options  Advantage Concepts |  |  |  |  |

When you create an FTS index, it is possible to specify a number of options that can be used to customize the index to meet your specific needs. The full text search engine breaks field information into words for searching. A word generally is considered to be space-delimited text such as is found in many text-based documents. It is possible, however, to define an FTS index so that the word recognition is very specific to a certain application.

In the following sections, some character values are given with their hexadecimal values in parentheses and prefixed by "0x". For example character value decimal 32 is shown as (0x20).

Minimum Word Length

SQL syntax: MIN WORD integer

AdsCreateFTSIndex Parameter: ulMinWordLen

This option specifies a minimum cut-off point for word recognition. Any word that is shorter than the specified minimum length is simply ignored; these words will not be in the FTS index nor will they be used if they are given in a search condition. When creating an FTS index via SQL, the default minimum word length is 3.

Maximum Word Length

SQL syntax: MAX WORD integer

AdsCreateFTSIndex Parameter: ulMaxWordLen

The maximum word length specifies the maximum word size that can be stored in the FTS index. This is effectively the key length of the index. In general, you should try to choose a length that is longer than most or all words that are in the information being indexed. Choosing a longer maximum word length increases the size of the resulting index file somewhat, but the increase is not large due to the compression techniques used. For example, increasing the maximum word length from 30 to 60 may only increase the size of the index file by 10% (the actual increase is data-dependant). The larger key size, though, can have a significant impact on the temporary file size during index creation (see the section below titled FTS Index Creation).

If a word exceeds the maximum word length, a portion of the word will still be in the index but any search for that word will need to examine the resulting record set for the word to determine if it is a match. This search is performed only on the records that pass the initial optimized search (for the partial word length). For example, if the maximum word length were specified as 5, then a search for the word "applesauce" would be able to use the index to find all records that contain words beginning with the first five letters ("apple") and then search that subset of records for the entire word.

When creating an FTS index via SQL, the default maximum word length is 30.

Delimiters

SQL syntax: [NEW] DELIMITERS characters

AdsCreateFTSIndex Parameters: usUseDefaultDelim, pucDelimiters

Delimiters are the set of characters that define word boundaries. The default set of delimiters includes the white space characters, which are the space (0x20), backspace (0x08), tab (0x09), newline (0x0A), vertical tab (0x0B), formfeed (0x0C), and carriage return (0x0D). This works for most standard text documents.

The default delimiters can be changed for a data dictionary with the ADS\_DD\_FTS\_DELIMITERS property in the Advantage Client Engine API AdsSetDatabaseProperty or the TDataSet Descendant method TAdsDictionary.SetDatabaseProperty. They can also be set in Advantage Data Architect by choosing the "FTS Defaults" button on the Database property screen.

Delimiters are always case sensitive. If, for example, you want to use "x" (0x78) and "X" (0x58) as delimiters, then you must specify both characters as delimiters regardless of the case sensitivity option.

The optional NEW keyword specifies that the given delimiters are to be used instead of the default delimiters. If the NEW keyword is not specified, then the given delimiters are used in addition to the default delimiters.

Character value 0x00 is always treated as a delimiter. It is not possible to change this behavior.

Drop Characters

SQL syntax: [NEW] DROPCHARS characters

AdsCreateFTSIndex Parameters: usUseDefaultDrop, pucDropChars

Drop characters are a set of characters that are simply ignored by the FTS engine. Drop characters are ignored in both the text and in search strings. The default drop characters are the double quote (0x22), the single quote (0x27), and the back quote (0x60). For example, if the defaults are used and a name such as OMalley is in the text, the FTS engine will store OMalley (without the quote) as the key value. A search word of either OMalley or OMalley will find it because the quote would be stripped out of the search word too.

The default drop characters can be changed for a data dictionary with the ADS\_DD\_FTS\_DROP\_CHARS property in the Advantage Client Engine API AdsSetDatabaseProperty or the TDataSet Descendant method TAdsDictionary.SetDatabaseProperty. They can also be set in Advantage Data Architect by choosing the "FTS Defaults" button on the Database property screen.

The optional NEW keyword specifies that the given drop characters are to be used instead of the default drop characters. If the NEW keyword is not specified, then the given drop characters are used in addition to the default drop characters.

Conditional Drop Characters

SQL syntax: [NEW] CONDITIONALS characters

AdsCreateFTSIndex Parameters: usUseDefaultConditionals, pucConditionalChars

Conditional drop characters are a special type of drop character. These characters are dropped only if they are at the beginning or the end of a word. This provides a mechanism for allowing certain characters to be maintained if they appear inside words. For example, one of the default conditional characters is the period. This means that periods on the ends of words will be stripped from the text, but if they are in the middle of a word (e.g., in a number such as 48.5), then they will be maintained.

The default conditional drop characters are (,.?!;:@#$%^&()-\_). Specifically, they are the comma (0x2C), period (0x2E), question mark (0x3F), exclamation mark (0x21), semicolon (0x3B), colon (0x3A), at symbol (0x40), number symbol (0x23), dollar sign (0x24), percent sign (0x25), caret (0x5E), ampersand (0x26), left parenthesis (0x28), right parenthesis (0x29), dash (0x2D), and underscore (0x5F).

The default conditional drop characters can be changed for a data dictionary with the ADS\_DD\_FTS\_CONDITIONAL\_CHARS property in the Advantage Client Engine API AdsSetDatabaseProperty or the TDataSet Descendant method TAdsDictionary.SetDatabaseProperty. They can also be set in Advantage Data Architect by choosing the "FTS Defaults" button on the Database property screen.

The optional NEW keyword specifies that the given conditional drop characters are to be used instead of the default conditional drop characters. If the NEW keyword is not specified, then the given conditional drop characters are used in addition to the default conditional drop characters.

Noise Words

SQL syntax: [NEW] NOISE word1 word2

AdsCreateFTSIndex Parameters: usUseDefaultNoise, pucNoiseWords

The noise words are words that are ignored by the FTS engine. Once a word is recognized according to the other rules (after obeying delimiters, drop characters, minimum word length, etc.), the word is checked against the noise word list and is ignored if it is found in that list. The default noise word list includes the following words:

about after all also and another any are because been before being between both but came can come could did does each else for from get got had has have her here him himself his how into its just like make many might more most much must never now only other our out over said same see should since some still such take than that the their them then there these they this those through too under use very want was way well were what when where which while who will with would you your

The default noise words can be changed for a data dictionary with the ADS\_DD\_FTS\_NOISE property in the Advantage Client Engine API AdsSetDatabaseProperty or the TDataSet Descendant method TAdsDictionary.SetDatabaseProperty. They can also be set in Advantage Data Architect by choosing the "FTS Defaults" button on the Database property screen.

The optional NEW keyword specifies that the given noise words are to be used instead of the default noise words. If the NEW keyword is not specified, then the given noise words are used in addition to the default noise words.

Keep Score Option

SQL syntax: KEEPSCORE

AdsCreateFTSIndex ulOptions value: ADS\_FTS\_KEEP\_SCORE

This option specifies whether or not Advantage will keep track of word counts in the FTS index. The score information is used only when the SCORE() scalar function is used either to display word counts or for ordering result sets based on word counts. Note that the SCORE() function can be used regardless of whether Advantage is maintaining word counts in the index, but it must count the words in a brute force fashion for each record returned. The decision on whether or not to use this option depends on whether you will use the SCORE() function and how often.

The scoring (word count) information requires 2 bytes per word per record. The actual increased size of the index is data-dependent but a common size increase is 30%. In addition, there is increased cost in maintaining the index during record updates if scoring information is kept. For example, suppose the text changes from "test case1" to "test case1 and test case2". If score information is not being kept, then the only update (assuming "and" is a noise word) is to add "case2" to the index. If scoring information is being maintained, then Advantage must also make an update for the word "test" because its word count increased.

There is also a final consideration when deciding if scoring information should be maintained. In general, if the average data length of a field is small, then there is probably no benefit in using the option to maintain score information. For example, keeping scoring information on a fixed length character field probably will not be beneficial. The index scoring information is the most useful when larger memo and BLOB values are being scored. You should test your specific application and data to determine if there is benefit in keeping score information in the index.

Note that if your application only uses the SCOREDISTINCT() function, then there is no need to use the option to maintain scoring information. The word counts are not needed to compute results for SCOREDISTINCT().

By default, this option is off.

Case Sensitive Option

SQL syntax: CASESENSITIVE

AdsCreateFTSIndex ulOptions value: ADS\_FTS\_CASE\_SENSITIVE

If this option is used, Advantage will create a case sensitive FTS index. This means that the search words must match the case of the words in the text for the search to be successful. In other words, a search word of "Arbitrary" will not find the word "arbitrary" in the text.

By default, this option is off.

This options is ignored when creating FTS index on a Unicode field. Unicode FTS indexes are always case insensitive and diacritical difference insensitive.

Fixed Option

SQL syntax: NOTMAINTAINED

AdsCreateFTSIndex ulOptions value: ADS\_FTS\_FIXED

This option indicates that Advantage should not maintain the FTS index once it has been built. This means that the index will be logically corrupt once updates have been made to the field that is indexed. Any searches made with a fixed index may return an incorrect result set (it may return records that do not actually meet the search criteria and/or it may fail to return records that do meet the search criteria).

This option may be useful in cases where huge numbers of updates are being made to a table and fast performance is required at the trade-off of some potentially incorrect searches. For most situations, however, this option probably is not necessary. The updates to FTS indexes are generally quite fast. If this option is used, the index should be rebuilt periodically.

Note there is one case where the index will not be maintained even if this option is not given. If BLOB (binary or image) data is written in partial sections, the index will not be updated. See the section titled FTS Index Updates below.

By default, this option is off.

Protect Numbers Option

SQL syntax: PROTECTNUMBERS

AdsCreateFTSIndex ulOptions value: ADS\_FTS\_PROTECT\_NUMBERS

This option covers a very specific situation. If it is given and the comma (0x2C) and/or period (0x2E) is given as a delimiter character, then numbers that contain commas and/or periods will not be broken into multiple words on those delimiters.

With "normal" text, the default delimiters and conditional drop characters will suffice. Using all default settings, the comma and period are not delimiter characters (they are conditional drop characters). Text such as "1,423.99" would be treated as a single word. If you created an FTS index with the period and comma as delimiter characters, then that text would be broken up into three words "1, 423, and 99". If you use the PROTECTNUMBERS option, then this would not occur. This option may be useful, for example, if the text contains words that have only commas between them (with no other delimiters). In that case, it may be desirable to treat the comma as a delimiter.

An SQL statement that might make use of this option is:

CREATE INDEX testfts ON thetable ( thefield ) CONTENT

delimiters ,.

protectnumbers

By default, this option is off.