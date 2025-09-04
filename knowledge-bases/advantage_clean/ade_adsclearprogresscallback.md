---
title: Ade Adsclearprogresscallback
slug: ade_adsclearprogresscallback
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsclearprogresscallback.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 478a1a0b8fc05b9430eace18241172cdb7bf99ba
---

# Ade Adsclearprogresscallback

AdsClearProgressCallback

TAdsTable/TAdsQuery.AdsClearProgressCallback

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsClearProgressCallback  Advantage TDataSet Descendant |  |  |  |  |

Clears the progress callback registered using AdsRegisterProgressCallback.

Note This API still functions as before, but is now obsolete. It is suggested that you use [AdsRegisterCallbackFunction](ade_adsregistercallbackfunction.md) and [AdsClearCallbackFunction](ade_adsclearcallbackfunction.md) instead, as they work better with threads and have more complete functionality.

Syntax

procedure AdsClearProgressCallback;

Description

AdsClearProgressCallback will make the Advantage Client Engine stop calling the registered callback function. The progress callback is used to indicate progress while an Advantage server is building an index.

Example

function MyCallbackFunc( usPercent: Word ): Longint ; stdcall;

begin

if ( gbCancelRequested ) then

Result := 1

else

Result := 0;

end;

 

procedure TForm1.RegisterButtonClick(Sender: TObject);

begin

AdsTable1.AdsRegisterProgressCallback( @MyCallbackFunc );

end;

 

procedure TForm1.ClearButtonClick(Sender: TObject);

begin

AdsTable1.AdsClearProgressCallback;

end;

See Also

[AdsRegisterCallbackFunction](ade_adsregistercallbackfunction.md)

[AdsClearCallbackFunction](ade_adsclearcallbackfunction.md)

[AdsCreateIndex](ade_adscreateindex.md)

[AdsReindex](ade_adsreindex.md)
