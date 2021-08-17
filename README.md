# Duolingo phrases to Pleco flashcards

A simple script to download your learned phrases from [Duolingo](https://www.duolingo.com) and convert them to a flashcard list importable by [Pleco Chinese Dictionary](https://www.pleco.com).

## Usage

### Dependencies

This project uses `pipenv` for package management: [install pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today).

To set up the virtualenv and install the required dependencies, run:
```shell
pipenv install
```

### Configuration

The script expects a config file under `config.py`.
To set this up, copy the default `config.default.py` to a new file `config.py`, and fill in the `username` and `password` values in the file with your credentials.
Customize the other config values in the file to your liking.

### Running

To run the script:
```shell
pipenv run main.py
```
This prints logging statements to standard error, and writes the flashcards to standard out, in [Pleco flashcard text file format](https://android.pleco.com/manual/240/flash.html#textformat).

You can for example save the flashcards to a file `cards.txt`:
```shell
pipenv run main.py > cards.txt
```

You can then copy this file to your phone and import it into Pleco.
See the Pleco documentation ([for Android](http://www.pleco.com/anmanual) and [for iOS](http://www.pleco.com/ipmanual)) for options you might want to change when importing.
