String Functions




Advantage Database Server 12  

String Functions

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| String Functions  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - String Functions Advantage SQL Engine master\_String\_functions Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| String Functions  Advantage SQL Engine |  |  |  |  |

collation\_lang = Either ads\_default\_cs (case sensitive) or ads\_default\_ci (case insensitive)

 

|  |  |
| --- | --- |
| [ASCII](master_ascii.htm)( str ) | Returns integer ASCII value for single character at start of str. |
| [AT](master_at.htm)( str1, str2[, start] ) | Return integer location (1-based) of str1 in str2, with optional start starting point.  If str1 is not found in str2, 0 is returned. |
| [BIT\_LENGTH](master_bit_length.htm)( str ) | Returns length of str in bits (assumes 8-bit characters). |
| [CHAR](master_char.htm)( int ) | Converts an ASCII value to its character value. |
| [CHAR\_LENGTH](master_char_length.htm)( str [USING <unit>] ) | Returns the length of string in the specified units.The <unit> may be CHARACTERS, OCTETS, or CODE\_POINTS. If there is no unit specification, the default is CHARACTERS which is the number of character for non-Unicode string input or number of code units (UTF16 characters) for Unicode string input. For non-Unicode string input, the result is the same regardless of the units. For Unicode string input, if the unit is OCTETS, the function returns the length of the string in number of bytes. If the unit is CODE\_POINTS, the function returns the number of code points in the string. |
| [CHARACTER\_LENGTH](master_char_length.htm)( str [USING <unit>] ) | Returns the length of string in characters. It is identical to CHAR\_LENGTH() above. |
| [CHAR2HEX](master_char2hex.htm)( str ) | Returns a binary value from a hexadecimal string.  See [Functions To Convert Hexadecimal Values](master_functions_to_convert_hexadecim.htm). |
| [CHR](master_chr.htm)( int ) | Converts an ASCII value to its character value. |
| [COLLATE](master_collate.htm) collation\_lang | Coerces the preceding value to the specified collation language. Note: COLLATE is a clause, not a scalar function. It can be used after column references, string literals, scalar functions, and expressions. See [Comparison Operators and Coercion](master_case_insensitive_field_type.htm#comparison_operators_and_coercion). |
| [CONCAT](master_concat.htm)( str1, str2 ) | Returns a string that is the result of concatenating str2 to str1. |
| [ENDSWITH](master_endswith.htm)( str1, str2 ) | Returns True if str1 ends with str2, and False otherwise. |
| [HEX2CHAR](master_hex2char.htm)( binary ) | Returns a hexadecimal string representation of a binary value. See [Functions To Convert Hexadecimal Values](master_functions_to_convert_hexadecim.htm). |
| [INSERT](master_insert_scalar.htm)( str1, start, length, str2 ) | Returns a character string where length characters have been deleted from str1, beginning at start, and where str2 has been inserted into str1, beginning at start. |
| [LCASE](master_lower.htm)( str ) | Returns string with all uppercase characters converted to lowercase. |
| [LEFT](master_left.htm)( str, count ) | Return the left part of string str up to count characters. |
| [LEN](master_len.htm)( str ) | Returns the number of characters in str, including trailing blanks. For non-Unicode string input, the result is the number of characters or bytes. For Unicode string input, the result is the number of UTF16 code units of the string. |
| [LENGTH](master_length.htm)( str ) | Returns the number of characters in str, excluding trailing blanks. For non-Unicode string input, the result is the number of characters or bytes. For Unicode string input, the result is the number of UTF16 code units of the string. |
| [LOCATE](master_at.htm)( str1, str2[, start] ) | Return integer location (1-based) of str1 in str2, with optional start starting point.  If str1 is not found in str2, 0 is returned. |
| [LOWER](master_lower.htm)( str ) | Returns a string with all uppercase characters converted to lowercase. |
| [LTRIM](master_ltrim.htm)( str ) | Returns string with leading spaces from <removed> left side of string. |
| [OCTET\_LENGTH](master_octet_length.htm)( str ) | Returns length of string in octets (i.e., bytes). |
| [PAD](master_pad.htm)( str, len [, fillchar ] ) | Pads a value with spaces or an optional fill character. |
| [POSITION](master_position.htm)( str1 IN str2 ) | Returns the position of str1 in str2. |
| [RAT](master_rat.htm)( str1, str2 ) | Return integer location (1-based) of last occurrence of str1 in str2  If str1 is not found in str2, 0 is returned. |
| [REPEAT](master_repeat.htm)( str, cnt ) | Returns a string consisting of str repeated up to cnt times. |
| [REPLACE](master_replace.htm)( str1, str2, str3 ) | Replace all occurrences of str2 in str1 with str3. |
| [REVERSE](master_reverse.htm)( str ) | Reverse the order of characters in a string. |
| [RIGHT](master_right.htm)( str, count ) | Returns a string of count characters of right part of str. |
| [RTRIM](master_rtrim.htm)( str ) | Returns a string with trailing spaces removed from the right side of string. |
| [SPACE](master_space.htm)( count ) | Returns a string of space repeated up to count times. |
| [STARTSWITH](master_startswith.htm)( str1, str2 ) | Returns true if str1 starts with str2, and False otherwise. |
| [STR](master_str.htm)( number, length, decimals ) | Convert a numeric value to a character string. |
| [STRZERO](master_strzero.htm)( number, length, decimals ) | Convert a numeric value to a character string and pad with leading zeros. |
| [SUBSTRING](master_substring.htm)( str, pos, len ) | Returns a portion of str starting at pos, up to length len. |
| [SUBSTRINGOF](master_substringof.htm)( str1, str2 ) | Returns True if str1 is a substring str2, and False otherwise. |
| [TRIM](master_trim.htm)( [[ LEADING | TRAILING | BOTH [ str1 ] FROM ] | [ str1 FROM ]] str2 ) | Returns a string that has trimmed leading or trailing (or both) occurrences of str1 from str2. Returns NULL if either str1 or str2 is NULL. See [TRIM](master_trim_sql_scalar.htm) for more information. |
| [UCASE](master_upper.htm)( str ) | Returns a string with all lowercase characters converted to uppercase. |
| [UPPER](master_upper.htm)( str ) | Returns a string with all lowercase characters converted to uppercase. |
| [VAL](master_val.htm)( str ) | Convert a string to a numeric value. |

 

See Also

[Supported Scalar Functions](master_supported_scalar_functions.htm)

[Math Functions](master_math_functions.htm)

[Date/Time Functions](master_date_time_functions.htm)

[Miscellaneous Functions](master_miscellaneous_functions.htm)