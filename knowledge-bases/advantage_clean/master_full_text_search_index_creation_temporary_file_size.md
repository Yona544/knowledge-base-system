---
title: Master Full Text Search Index Creation Temporary File Size
slug: master_full_text_search_index_creation_temporary_file_size
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_full_text_search_index_creation_temporary_file_size.htm
source: Advantage CHM
tags:
  - master
checksum: 5c65bcc5c4f033d966dd09620ad43d016872b7a7
---

# Master Full Text Search Index Creation Temporary File Size

Full Text Search Index Creation: Temporary File Size

Full Text Search Index Creation: Temporary File Size

Advantage Concepts

| Full Text Search Index Creation: Temporary File Size  Advantage Concepts |  |  |  |  |

While creating FTS indexes, Advantage may create very large temporary files. The temporary sort file will have one key for every word in the information being indexed. This includes duplicate words as well. The space that is required for each key in the temporary file is the maximum word length plus 4 bytes of overhead per key. If the index is for a Unicode column, the key size is roughly 3 times maximum word length using the default options. As the actual index is built, duplicates are removed and key compression is used, so the final index size can be quite small. Consider an example:

- Information being indexed is 1 MB.

- Data being indexed consists of words with an average length of 5 characters with one space (delimiter) between each word (6 bytes per word).

- Maximum word size is specified as 60 bytes.

- Noise word list is empty and minimum word size is 0. This means that all words (including 1 letter words) will be included in the index.

- For ANSI field types, the actual space needed to hold the keys prior to the actual index creation then will be:

(1048576 / 6)\* 64 = 11,184,810 (about 11 MB)

- If the same index is being build on a Unicode field, the required space will be about 33 MB

In the above example using ANSI field type, the temporary file size has a 10:1 ratio in size with the data. The final index size is completely dependent on the data. In one test case, the total data was 84 MB, the temporary sort file was 400 MB, and the final index size was 2 MB. Another test case included 2.3 MB of data, 8 MB of temporary space, and a final index size of 0.25 MB.
