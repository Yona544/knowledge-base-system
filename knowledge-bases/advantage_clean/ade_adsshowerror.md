---
title: Ade Adsshowerror
slug: ade_adsshowerror
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsshowerror.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: f970360c53d8a411f2788e245d7e1816e70974a6
---

# Ade Adsshowerror

AdsShowError

TAdsTable.AdsShowError

Advantage TDataSet Descendant

| TAdsTable.AdsShowError  Advantage TDataSet Descendant |  |  |  |  |

Displays a message box for the last error (if there was one).

Syntax

procedure AdsShowError( strCaption : String );

Parameter

| strCaption | The title for the message box. Can be an empty string. |

Description

AdsShowError will display a message box containing the last error message. The message displayed is identical to the error message available from AdsGetErrorString. This function is useful during development or debugging for viewing error messages immediately after the error occurred.

Example

procedure TForm1.Button5Click(Sender: TObject);

begin

try

AdsTable2.open;

except

{$ifdef DEBUG}

AdsTable2.AdsShowError( 'table open' );

{$else}

{\* put your release code error handling here \*}

{$endif}

end;

end;

See Also

[AdsGetErrorString](ade_adsgeterrorstring.md)

[AdsGetLastError](ade_adsgetlasterror.md)
