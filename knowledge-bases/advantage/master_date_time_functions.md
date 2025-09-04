Date/Time Functions




Advantage Database Server 12  

Date/Time Functions

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Date/Time Functions  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - Date/Time Functions Advantage SQL Engine master\_Date\_time\_functions Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Date/Time Functions  Advantage SQL Engine |  |  |  |  |

DATE = Year, Month, Day.

TIME = hour, minute, second.

date = Expression or literal resulting in a date value.

time = Expression or literal resulting in a time value.

timestamp = Expression or literal resulting in a timestamp value.

timestampdiff = Expression or literal resulting in a timestamp value.

int = Expression or literal resulting in an integer value.

 

|  |  |
| --- | --- |
| [CREATETIMESTAMP](master_createtimestamp.htm)( year, month, day, hour, minute, second, millisecond ) | Creates a timestamp literal from the given integer parameter values. |
| [CTOD](master_ctod.htm)( str ) | Converts a date string to a date value. |
| [CTOT](master_ctot.htm)( str ) | Converts a string to a time value. |
| [CTOTS](master_ctots.htm)( str ) | Converts a string to a timestamp value. |
| [CURDATE](master_date.htm)() | Returns DATE for current date with 1-based month. |
| [CURRENT\_DATE](master_date.htm)() | Same as CURDATE. |
| [CURRENT\_TIME](master_curtime.htm)() | Same as CURTIME |
| [CURRENT\_TIMESTAMP](master_current_timestamp.htm)([ precision ]) | Returns TIMESTAMP for current local time, with optional precision. The optional parameter can be a value from 0 to 3 and specifies the precision of the fractional portion of seconds returned. |
| [CURRENT\_TIMESTAMP\_UTC](master_current_timestamp_utc.htm)([ precision ]) | Returns TIMESTAMP for current UTC (GMT) time, with optional precision.  The optional parameter can be a value from 0 to 3 and specifies the precision of the fractional portion of the seconds returned. |
| [CURTIME](master_curtime.htm)() | Returns TIME for current local time. |
| [DATE](master_date.htm)() | Returns the current local date. |
| [DAY](master_day.htm)( date ) | Returns integer day of month from a DATE or TIMESTAMP. |
| [DAYNAME](master_dayname.htm)( date ) | Returns weekday name string from a CHAR, DATE, or TIMESTAMP. |
| [DAYOFMONTH](master_day.htm)( date ) | Returns integer day of month (1-based) from CHAR, DATE, or TIMESTAMP. |
| [DAYOFWEEK](master_dayofweek.htm)( date ) | Returns integer day of week (1-based, where 1 means Sunday) from CHAR, DATE, or TIMESTAMP. |
| [DAYOFYEAR](master_dayofyear.htm)( date ) | Returns integer day of year (1-based) from CHAR, DATE, or TIMESTAMP. |
| [DTOC](master_dtoc.htm)( date [, format ] ) | Convert a date value to a character string. |
| [DTOS](master_dtos.htm)( date ) | Converts a date value to a character string formatted as yyyymmdd |
| [EXTRACT](master_extract.htm)( time-value FROM time-date ) | Extract year, month, day, hour, minute, or second from TIMESTAMP. |
| [FRAC\_SECOND](master_frac_second.htm)( timestamp ) | Returns integer millisecond from TIMESTAMP. |
| [HOUR](master_hour.htm)( time ) | Returns integer of hour (0-based) from CHAR, TIME, or TIMESTAMP. |
| [ISOWEEK](master_isoweek.htm)( date ) | Returns the ISO 8601 week number from CHAR, DATE, or TIMESTAMP. |
| [MINUTE](master_minute.htm)( time ) | Returns integer minute (0-based) from CHAR, DATE, or TIMESTAMP. |
| [MONTH](master_month.htm)( date ) | Returns integer of month (1-based) from CHAR, DATE, or TIMESTAMP. |
| [MONTHNAME](master_monthname.htm)( date ) | Returns string month name from CHAR, DATE, or TIMESTAMP. |
| [NOW](master_now.htm)() | Returns TIMESTAMP for current date and time (1-based month). |
| [NOW\_UTC](master_now_utc.htm)() | Returns TIMESTAMP for current UTC (GMT) time. |
| [QUARTER](master_quarter.htm)( date ) | Returns integer quarter number (1-4) from CHAR, DATE, or TIMESTAMP. |
| [SECOND](master_second.htm)( time ) | Returns integer second (0-based) from CHAR, DATE, or TIMESTAMP. |
| [STOD](master_stod.htm)( str ) | Converts a character string formatted as YYYYMMDD to a date value. |
| [STOTS](master_stots.htm)( str ) | Converts a character string formatted as 'YYYYMMDD HH:MM:SS.mmm' to a timestamp value. |
| [TIME](master_time.htm)() | Returns current system time as a string. |
| [TIMESTAMPADD](master_timestampadd.htm)( interval, int, timestamp ) | Returns TIMESTAMP calculated by adding int intervals to timestamp. Interval values supported are: SQL\_TSI\_FRAC\_SECOND, SQL\_TSI\_SECOND, SQL\_TSI\_MINUTE, SQL\_TSI\_HOUR, SQL\_TSI\_DAY, SQL\_TSI\_WEEK, SQL\_TSI\_MONTH, SQL\_TSI\_QUARTER, SQL\_TSI\_YEAR. |
| [TIMESTAMPDIFF](master_timestampdiff.htm)( interval, timestamp1, timestamp2 ) | Returns number of integer intervals based on subtracting timestamp1 from timestamp2. Interval values supported are: SQL\_TSI\_FRAC\_SECOND, SQL\_TSI\_SECOND, SQL\_TSI\_MINUTE, SQL\_TSI\_HOUR, SQL\_TSI\_DAY, SQL\_TSI\_WEEK, SQL\_TSI\_MONTH, SQL\_TSI\_QUARTER, SQL\_TSI\_YEAR. |
| [TODAY](master_today.htm)() | Returns the current local date. |
| [TSTOD](master_tstod.htm)( timestamp ) | Extract the date from a timestamp. |
| [TTOC](master_ttoc.htm)( timestamp, format ) | Convert a timestamp to a character string. |
| [WEEK](master_week.htm)( date ) | Returns integer week number (1-based) in year from CHAR, DATE, or TIMESTAMP. |
| [YEAR](master_year.htm)( date ) | Returns integer year number from CHAR, DATE, or TIMESTAMP. |

See Also

[Supported Scalar Functions](master_supported_scalar_functions.htm)

[String Functions](master_string_functions.htm)

[Math Functions](master_math_functions.htm)

[Miscellaneous Functions](master_miscellaneous_functions.htm)