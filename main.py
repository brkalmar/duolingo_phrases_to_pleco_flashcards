import duolingo
import logging
import sys


# Set up logging and config.

logging.basicConfig(
    style="{",
    format="{asctime} {levelname:7} {message}",
    datefmt="%H:%M:%S",
    level=logging.INFO,
)

try:
    import config
except ImportError:
    logging.critical("no config found: run `cp config.default.py config.py`")
    sys.exit(1)

## Retreive phrases from Duolingo API.

# File to save authentication token in to avoid having to re-authenticate on
# each new execution.
token_file = "token.json"

logging.info(f"connect to Duolingo API ...")
duo = duolingo.Duolingo(
    username=config.username,
    password=config.password,
    session_file=token_file,
)

logging.info(f"get language abbreviation ...")
language_abbr = duo.get_abbreviation_of(config.language)
logging.info(f"language abbreviation: {language_abbr!r}")

phrases = set()

if config.include_vocabulary:
    logging.info(f"get vocabulary ...")
    vocabulary = duo.get_vocabulary(language_abbr)
    phrases.update(v["word_string"] for v in vocabulary["vocab_overview"])
    logging.info(f"vocabulary phrases: {len(phrases)}")

if config.include_words:
    logging.info(f"get known words ...")
    words = duo.get_known_words(language_abbr)
    phrases.update(words)
    logging.info(f"known words phrases: {len(words)}")

phrases = sorted(phrases)

# Print phrases to out stream in Pleco flashcard text file format:
# https://android.pleco.com/manual/240/flash.html#textformat

logging.info(f"write output ...")
out = sys.stdout

# Switch to the flashcard category, if any.
if config.category is not None:
    # Category line:
    #
    #   "//" SPC category
    print(f"// {config.category}", file=out)

for phrase in phrases:
    # Vocabulary line:
    #
    #   phrase [ TAB pinyin [ TAB definition ] ]
    print(f"{phrase}", file=out)

logging.info(f"total phrases: {len(phrases)}")
