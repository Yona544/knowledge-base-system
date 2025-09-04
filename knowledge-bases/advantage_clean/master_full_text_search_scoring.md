---
title: Master Full Text Search Scoring
slug: master_full_text_search_scoring
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_full_text_search_scoring.htm
source: Advantage CHM
tags:
  - master
checksum: 566d5f12825fa19061bab6ca0e9e40f3febbdce2
---

# Master Full Text Search Scoring

Full Text Search Scoring

Full Text Search Scoring

Advantage Concepts

| Full Text Search Scoring  Advantage Concepts |  |  |  |  |

The score values are computed simply by summing the score for each word that is in the search condition. The scoring makes no differentiation between AND, OR, and NEAR operators. The score for each of the following search conditions is identical. Each search condition contains two words that are scored individually and then summed.

medical and doctor\*

medical or doctor\*

medical near doctor\*

"medical doctors"

The SCORE() value for a given record in the examples above can be any value 0 or greater. For example, the text Both medical doctors and doctors of veterinary medicine require extensive schooling. would have a SCORE() of 3 for each of the conditions above because the word "doctors" appears twice and the word "medical" appears once.

SCOREDISTINCT() assigns a score of 1 for each word in the search condition that appears at least once in the text. So the maximum value it would return for each of the search conditions above is 2.

Words that are part of a logical NOT operator are not counted in the scoring process. In the following search condition, the word "doctor" would not be counted by a score function.

medical and not doctor
