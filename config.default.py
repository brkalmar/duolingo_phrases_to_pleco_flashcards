from typing import Optional


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
category: Optional[str] = "Duolingo"
