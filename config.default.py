import sys

from typing import Optional, Union


# Duolingo username.
username: str = ""

# Duolingo password.
password: str = ""

# Language name, as recognized by Duolingo.
language: str = "Chinese"

# Whether to include phrases from the Duolingo "vocabulary".  The vocabulary
# consists of all phrases practiced in Duolingo (single- and multiple-word).  It
# does *not* include parts of phrases that were not practiced individually.
include_vocabulary: bool = True

# Whether to include the phrases under the Duolingo "learned words".  The
# learned words include most vocabulary phrases, but some are missing.  They
# additionally include parts of phrases that were not practiced individually.
include_words: bool = False

# Name of flashcard category to have all phrases under.
#
# If None, no category is specifed for any of the phrases.
category: Optional[str] = "duo"

# File to write flashcard output to.
#
# If object, it is treated as a file-like stream object.
#
# If str, it is treated as a filename; the file is overwritten.
out_file: Union[object, str] = sys.stdout

# File to save Duolingo authentication token in to avoid having to
# re-authenticate on each new execution.
#
# If str, it is treated as a filename.
#
# If None, no token file is used.
token_file: Optional[str] = "token.json"
