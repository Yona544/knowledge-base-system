Working with Cursor Handles




Advantage Database Server 12  

Working with Cursor Handles

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Working with Cursor Handles  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - Working with Cursor Handles Advantage Client Engine ace\_Working\_with\_cursor\_handles Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Working with Cursor Handles  Advantage Client Engine |  |  |  |  |

Once the SQL statement that starts with the SELECT keyword has been executed, a cursor handle will be returned. This cursor handle provides access to the rowset returned. Aside from the few select APIs in the table below, this cursor handle and a table handle are interchangeable in any Advantage Client Engine API. For example, the API AdsGetField is documented as accepting a table handle for its first parameter. This table handle can be replaced with a cursor handle to obtain data from the row set:

AdsGetField( hCursor, "lastname", aucBuffer,

&ulLen, ADS\_TRIM );

Another example would be to use the AdsSkip function to reference the next or previous row in the row set.

APIs not compatible with cursor handles:

AdsDecryptTable

AdsEncryptTable

AdsDecryptRecord

AdsEncryptRecord

AdsPackTable

AdsZapTable

AdsReindex

AdsLockTable

AdsUnlockTable