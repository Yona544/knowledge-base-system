TRIM




Advantage Database Server 12  

TRIM

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TRIM  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - TRIM Advantage SQL Engine master\_Trim\_sql\_scalar Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TRIM  Advantage SQL Engine |  |  |  |  |

Trims a given string of characters from a given string.

Syntax

TRIM( [[ LEADING | TRAILING | BOTH [ str1 ] FROM ] | [ str1 FROM ]] str2 )

Arguments

|  |  |
| --- | --- |
| str1 | String of characters to trim off (Default is a single space). |
| str2 | Source string from which to trim characters. |

Remarks

TRIM removes occurrences of str1 from the beginning or end of str2. When passed no trim options, TRIM removes all leading or trailing white space from str2. By specifying LEADING or TRAILING as the trim option, TRIM will remove all leading or trailing occurrences of str1 from str2. The default option is BOTH. If str1 or a trim option is specified, the FROM keyword must precede str2. If either str1 or str2 evaluates to NULL, TRIM returns NULL.

TRIM removes multiple occurrences of str1 from str2. For example:

SELECT TRIM( 'xy' FROM 'xyxyxAyxxy' ) FROM system.iota

would return:

'xAyx'

Examples

SELECT TRIM( lastname ) from customers

SELECT TRIM( LEADING FROM lastname ) FROM customers

SELECT TRIM( '.' FROM address ) FROM customers