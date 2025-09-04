Advantage Client Engine API TPS Examples




Advantage Database Server 12  

Advantage Client Engine API TPS Examples

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Client Engine API TPS Examples  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - Advantage Client Engine API TPS Examples Advantage Client Engine ace\_Advantage\_client\_engine\_api\_tps\_examples Advantage Client Engine > Example Code > Advantage Client Engine API TPS Examples / Dear Support Staff, |  |
| Advantage Client Engine API TPS Examples  Advantage Client Engine |  |  |  |  |

To maintain brevity, the following examples do not check many return codes. It is normally a good idea to verify the return value of each call.

Example 1

The first example demonstrates how a basic money transfer would occur WITHOUT Advantage Transaction Processing.

// Transfer $100 from Bill's account to Sally's account

// WITHOUT Advantage Transaction Processing. If any error occurs

// on the workstation, the network, or the server between Bill's

// UNLOCK and Sally's UNLOCK, the money will be lost and the

// database will be logically corrupt.

ulRetVal = AdsSeek( hIndex, "Bill", 4, ADS\_STRINGKEY, ADS\_HARDSEEK,

&usFound);

 

// make sure we found Bill

if ( !usFound )

{

MessageBox( 0, "Seek on 'Bill' failed!", "ACE Error", MB\_OK );

return -1;

}

 

// lock this record

ulRetVal = AdsLockRecord( hTable, 0 );

if ( ulRetVal != AE\_SUCCESS )

// unable to lock the record

return ulRetVal;

 

ulRetVal = AdsGetRecordNum( hTable, ADS\_IGNOREFILTERS,

&ulBillsRec );

 

ulRetVal = AdsSeek( hIndex, "Sally", 5, ADS\_STRINGKEY, ADS\_HARDSEEK,

&usFound);

 

// make sure we found Sally now

if ( !usFound )

{

AdsUnlockRecord( hTable, ulBillsRec );

MessageBox( 0, "Seek on 'Sally' failed!", "ACE Error", MB\_OK );

return -1;

}

 

// lock this record

ulRetVal = AdsLockRecord( hTable, 0 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsUnlockRecord( hTable, ulBillsRec );

return ulRetVal;

}

 

ulRetVal = AdsGetRecordNum( hTable, ADS\_IGNOREFILTERS,

&ulSallysRec );

 

 

// Update Bill's acct. The AdsUnlockRecord() flushes Bill's update

// to disk

ulRetVal = AdsGotoRecord( hTable, ulBillsRec );

ulRetVal = AdsGetDouble( hTable, "balance", &dBalance );

ulRetVal = AdsSetDouble( hTable, "balance", dBalance - 100.0 );

ulRetVal = AdsUnlockRecord( hTable, 0 );

 

 

// Update Sally's acct. The UNLOCK flushes Sally's update to disk

// Note: A failure after this point should actually attempt to

// put the money back into Bill's account.

ulRetVal = AdsGotoRecord( hTable, ulSallysRec );

ulRetVal = AdsGetDouble( hTable, "balance", &dBalance );

ulRetVal = AdsSetDouble( hTable, "balance", dBalance + 100.0 );

ulRetVal = AdsUnlockRecord( hTable, 0 );

Figure 2 demonstrates the same basic money transfer as in Figure 1, but is implemented as an Advantage transaction.

Example 2

// Transfer $100 from Bill's account to Sally's account

// WITH Advantage Transaction Processing. If any error occurs

// on the workstation, the network, or the server after the BEGIN

// TRANSACTION statement and until the COMMIT TRANSACTION completes,

// the transaction will be automatically rolled back. That is, the

// updates will not occur and the database will be left as it was

// before the transaction started.

// NOTE: This example does the locking and unlocking outside

// the transaction to avoid unnecessary transaction rollbacks.

ulRetVal = AdsSeek( hIndex, "Bill", 4, ADS\_STRINGKEY, ADS\_HARDSEEK,

&usFound);

 

// make sure we found Bill

if ( !usFound )

{

MessageBox( 0, "Seek on 'Bill' failed!", "ACE Error", MB\_OK );

return -1;

}

 

// lock this record

ulRetVal = AdsLockRecord( hTable, 0 );

if ( ulRetVal != AE\_SUCCESS )

return ulRetVal;

 

ulRetVal = AdsGetRecordNum( hTable, ADS\_IGNOREFILTERS,

&ulBillsRec );

 

// find Sally's record

ulRetVal = AdsSeek( hIndex, "Sally", 5, ADS\_STRINGKEY, ADS\_HARDSEEK,

&usFound);

 

// make sure we found Sally now

if ( !usFound )

{

AdsUnlockRecord( hTable, ulBillsRec );

MessageBox( 0, "Seek on 'Sally' failed!", "ACE Error", MB\_OK );

return -1;

}

 

// lock this record

ulRetVal = AdsLockRecord( hTable, 0 );

if ( ulRetVal != AE\_SUCCESS )

{

AdsUnlockRecord( hTable, ulBillsRec );

return ulRetVal;

}

 

ulRetVal = AdsGetRecordNum( hTable, ADS\_IGNOREFILTERS,

&ulSallysRec );

 

ulRetVal = AdsBeginTransaction( 0 );

if ( ulRetVal )

{

AdsUnlockTable( hTable ); // unlock all records

return ulRetVal;

}

 

// Update Bill's acct.

ulRetVal = AdsGotoRecord( hTable, ulBillsRec );

ulRetVal = AdsGetDouble( hTable, "balance", &dBalance );

ulRetVal = AdsSetDouble( hTable, "balance", dBalance - 100.0 );

 

// Update Sally's acct.

ulRetVal = AdsGotoRecord( hTable, ulSallysRec );

ulRetVal = AdsGetDouble( hTable, "balance", &dBalance );

ulRetVal = AdsSetDouble( hTable, "balance", dBalance + 100.0 );

 

 

// This COMMIT TRANSACTION will cause the updates to Bill's and

// Sally's accounts to actually be performed. When the commit

// transaction is completed, the updates will become visible to

// all other users at one time.

ulRetVal = AdsCommitTransaction( 0 );

 

// Finally, unlock the records used during the transaction

AdsUnlockRecord( hTable, ulBillsRec );

AdsUnlockRecord( hTable, ulSallysRec );

Example 3

// Another version using transaction processing. This one uses

// implicit locking and relies on the rollback in case of a lock

// failure due to contention.

 

// begin the transaction

ulRetVal = AdsBeginTransaction( 0 );

if ( ulRetVal )

{

AdsUnlockTable( hTable ); // unlock all records

return ulRetVal;

}

 

// Find Bill's record

ulRetVal = AdsSeek( hIndex, "Bill", 4, ADS\_STRINGKEY, ADS\_HARDSEEK,

&usFound);

 

// make sure we found Bill

if ( !usFound )

{

AdsRollbackTransaction( 0 );

MessageBox( 0, "Seek on 'Bill' failed!", "ACE Error", MB\_OK );

return -1;

}

 

// Update Bill's acct.

ulRetVal = AdsGetDouble( hTable, "balance", &dBalance );

ulRetVal = AdsSetDouble( hTable, "balance", dBalance - 100.0 );

 

// if the call failed for some reason, rollback and bail out. The

// primary reason it might fail is if the lock could not be

// obtained.

if ( ulRetVal )

{

AdsRollbackTransaction( 0 );

return -1;

}

 

// find Sally's record

ulRetVal = AdsSeek( hIndex, "Sally", 5, ADS\_STRINGKEY, ADS\_HARDSEEK,

&usFound );

 

// make sure we found Sally now

if ( !usFound )

{

AdsRollbackTransaction( 0 );

MessageBox( 0, "Seek on 'Sally' failed!", "ACE Error", MB\_OK );

return -1;

}

 

// Update Sally's acct. The UNLOCK flushes Sally's update to disk

ulRetVal = AdsGetDouble( hTable, "balance", &dBalance );

ulRetVal = AdsSetDouble( hTable, "balance", dBalance + 100.0 );

 

// if the call failed for some reason, rollback and bail out. The

// primary reason it might fail is if the lock could not be

// obtained.

if ( ulRetVal )

{

AdsRollbackTransaction( 0 );

return -1;

}

 

// This COMMIT TRANSACTION will cause the updates to Bill's and

// Sally's accounts to actually be performed. When the commit

// transaction is completed, the updates will become visible to

// all other users at one time. Because implicit locks were

// obtained, the locks will be released automatically after the

// transaction has been committed.

ulRetVal = AdsCommitTransaction( 0 );