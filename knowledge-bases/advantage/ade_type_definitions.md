Type Definitions




Advantage Database Server 12  

Type Definitions

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Type Definitions  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - Type Definitions Advantage TDataSet Descendant ade\_Type\_definitions Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Type Definitions  Advantage TDataSet Descendant |  |  |  |  |

{ Set of creation index options }

TAdsIndexOption = ( optCOMPOUND, optUNIQUE, optDESCENDING, optCUSTOM );

TAdsIndexOptions = set of TAdsIndexOption;

 

{ Set of expression types }

TAdsExpressionTypes = ( etLOGICAL, etNUMERIC, etDATE, etSTRING, etRAW );

 

{ Set of expression types }

TAdsBinaryTypes = ( btBINARY, btIMAGE );

 

{ enumerated list of trim options }

TAdsTrimOptions = ( optNONE, optLTRIM, optRTRIM, optTRIM );

 

{ enumerated list of field types }

TAdsFieldTypes = ( AdsfldLOGICAL, AdsfldNUMERIC, AdsfldDATE, AdsfldSTRING,

AdsfldMEMO, AdsfldVARCHAR, AdsfldCOMPACTDATE,

AdsfldDOUBLE, AdsfldINTEGER, AdsfldSHORTINT, AdsfldTIME,

AdsfldTIMESTAMP, AdsfldAUTOINC, AdsfldRAW,

AdsfldCURDOUBLE, AdsfldMONEY, AdsfldCISTRING );

 

{ enumerated list of memo data types }

TAdsMemoDataTypes = ( mdtMEMO, mdtBINARY, mdtIMAGE );

 

{ enumerated list of what to return for the filename }

TAdsFilenameOptions = ( foBASENAME, foBASENAMEANDEXT, foFULLPATHNAME );

 

{ enumerated list of what to return for the filename }

TAdsHandleTypes = ( htTABLE, htINDEX );

 

{ enumerated list of seek type }

TAdsSeekTypes = ( stSOFT, stHARD );

 

{ enumerated list of scope options }

TAdsScopeOptions = ( soTOP, soBOTTOM );

 

{ enumerated list of filter optimization levels }

TAdsAOFOptimizeLevel = ( olFULL, olPart, olNone );