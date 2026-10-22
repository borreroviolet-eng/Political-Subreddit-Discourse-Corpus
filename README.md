# Political Subreddit Discourse Corpus (PSDC)

A Python tool for building a "web as corpus" dataset from Reddit, plus a corpus linguistics analysis of comments from four political communities.

**Violet Borrero** · ENG 595 senior project, California State University, San Bernardino · 2019

## Overview

Reddit's voting system works as a community filter: the most upvoted posts and comments are, in a sense, the ones each community considers most representative of itself. This project uses that filter to build a corpus of top-voted discussion from four political subreddits. It then compares their language to general English and to each other.

## How the corpus was built

The scraper, written in Python with [PRAW](https://praw.readthedocs.io/) (the Python Reddit API Wrapper), runs the same process for each subreddit:

1. Authenticates through a registered Reddit script app.
2. Pulls the **10 top-voted posts**.
3. Collects up to the **first 1,000 comments** on each post.
4. Saves each post's comments to its own labeled text file, so every subreddit can be treated as a sub-corpus.

## Corpus at a glance

| Sub-corpus | Comments | Tokens | Types |
| --- | --- | --- | --- |
| r/politics | 8,847 | 268,798 | 18,979 |
| r/NeutralPolitics | 3,727 | 230,622 | 14,183 |
| r/Conservative | 3,845 | 166,169 | 13,519 |
| r/Liberal | 1,097 | 33,066 | 5,517 |
| **Total** | **17,516** | **698,655** | **32,456** |

## Analysis

- **Specialized vs. general English.** I compared the 10 most frequent content nouns, normalized per 500,000 words, against the COCA and iWeb reference corpora (Davies). Words like *Trump* (2,917 vs. 51 in COCA), *Russia*, *government*, and *president* appeared far more often, confirming the political character of the discussion.
- **Between communities.** I compared the top nouns in each sub-corpus and looked closely at how a single word, *people*, shifts between excluding an out-group, rallying an in-group, and citing anonymous sources.
- **Register analysis.** Using Biber's situational framework (as presented in Crawford & Csomay, 2016), I characterized Reddit as a register and compared the four communities' participants, relationships, and communicative purposes, drawing on each community's own guidelines.

Tools: Python, PRAW, AntConc.

## Limitations

- **Unbalanced sub-corpora.** r/politics has about 8× the comments of r/Liberal, largely because of differences in subscriber count.
- **Narrow scope.** Four U.S. subreddits, weighted toward election-year activity.
- **No part-of-speech tagging,** which limits grammatical analysis.
- **Metadata gaps.** AntConc revealed missing file tags (dates, URLs, header length) that a larger build would need.

The PSDC works best as a proof of concept for a larger, more balanced corpus. Possible extensions include sentiment analysis, POS tagging, and comparing how different communities discuss the same article.

## Running the scraper

> **Note:** Reddit's API terms and rate limits changed significantly in 2023. This script was written in 2019 and may need updates.

1. Install PRAW: `pip install praw`
2. Register a script app at <https://www.reddit.com/prefs/apps> to get a client ID and secret.
3. Set your credentials as environment variables rather than writing them into the script:
   ```
   client_id=...
   client_secret=...
   user_agent=...
   ```
4. Run `python_comment_grabber.py`. 

## Data availability

Raw comment text isn't included here, out of respect for Reddit users and Reddit's data terms. The scraper can rebuild a comparable corpus, and the summary tables above come from the original data.

## Repository contents

```
├── README.md
├── python_comment_grabber.py                  # corpus-building script
└── Corpus of Online Political Discourse.pdf   # final written report
```

## References

- Crawford, W., & Csomay, E. (2016). *Doing Corpus Linguistics.* Routledge.
- Davies, M. (n.d.). English-Corpora.org. https://www.english-corpora.org/
