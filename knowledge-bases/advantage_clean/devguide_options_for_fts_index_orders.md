---
title: Devguide Options For Fts Index Orders
slug: devguide_options_for_fts_index_orders
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_options_for_fts_index_orders.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: c017f8a3c7fa491dad75412d58caeee62afe3bb7
---

# Devguide Options For Fts Index Orders

Options for FTS Index Orders

     Options for FTS Index Orders

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Options for FTS Index Orders  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The Notes FTS index order created in the earlier section "Creating FTS Index Orders" used the default settings for FTS indexes. There are many different options, and they can dramatically influence what keys are included in the FTS index. Each of the options associated with FTS index orders is discussed briefly in this section. Note, however, that some of these options have somewhat complicated implications. For a complete discussion of FTS index order options, please refer to the Advantage documentation.

After an FTS index is created, you can view its options by selecting the index in the FTS Index Names list on the Full Text Search Index Definitions page of the Table Designer dialog box. The options for the Notes index created earlier for the CUSTOMER table are shown in Figure 3-9. You should refer to this Full Text Search Index Definitions page if you want to view the default values for an FTS index.

Figure 3-9: The default settings used for the Notes FTS index order are visible on the Full Text Search Index Definitions page

Minimum Word Length

Keys in an FTS index are not created for any words shorter than the minimum word length. The default minimum word length is 3.

Maximum Word Length

The maximum word length value identifies the longest key that will be stored in an FTS index order. If your text field contains a word longer than the maximum word length, that value is truncated to the maximum word length. Consequently, words longer than the maximum word length affect an FTS index, but only up to the maximum word length. The default maximum word length is 30.

Delimiters

Delimiters are the ANSI characters that separate words in a text-based field. For example, if you stored Java language code segments in a memo field, and wanted to search for specific Java class members, you would want to include the period (.) as a delimiter, since a period separates member references in Javas dot notation.

The default delimiters are a backspace, tab, newline, vertical tab, form feed, carriage return, and space.

Noise Words

Noise words are common words that you do not want to appear as keys in an FTS index order. For example, it is extremely unlikely that you would search a text field for the word the. In order to prevent this word from being treated as a content word, it is included as a default noise word.

The default noise words are as follows:

about after all also and another any are because been before being between both but came can come could did does each else for from get got had has have her here him himself his how into its just like make many might more most much must never now only other our out over said same see should since some still such take than that the their them then there these they this those through too under use very want was way well were what when where which while who will with would you your

Drop Characters

Drop characters are those that are unconditionally ignored when the index is being created. The default drop characters are the double-quote, single quote, and apostrophe characters.
