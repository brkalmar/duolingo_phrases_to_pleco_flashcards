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

duo = duolingo.Duolingo(
    username=config.username,
    password=config.password,
    session_file=config.token_file,
)

language_abbr = duo.get_abbreviation_of(config.language)

phrases = set()

if config.include_vocabulary:
    vocabulary = duo.get_vocabulary(language_abbr)
    phrases.update(v["word_string"] for v in vocabulary["vocab_overview"])

if config.include_words:
    words = duo.get_known_words(language_abbr)
    phrases.update(words)

phrases = sorted(phrases)

# Print phrases to out stream in Pleco flashcard text file format:
# https://android.pleco.com/manual/240/flash.html#textformat

if isinstance(config.out_file, str):
    out = open(config.out_file, "w")
else:
    out = config.out_file

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
