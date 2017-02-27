# wordsearch
Wordsearch is used to search a directory for word documents (.doc and .docx) 
and then search for phrases in the documents.  The phrase matches are then output 
to an external csv file.

Built against Python 3.5.2

## Setup
Clone the repo
```
git clone https://github.com/scottamartin/wordsearch.git
```
Install the 'wordsearch' module (in the repo directory)
```
pip install .
```

## Usage
After cloning and installing the module, run
```
wordsearch --help
```
This will display the usage
```
Usage: wordsearch [OPTIONS] PATH

Options:
  -m, --match TEXT     Phrase to search for in files
  -o, --output PATH    Path and filename for the csv to create
  -c, --chars INTEGER  Number of characters to include before and after a
                       match (default:30)
  --ignore-case
  --help               Show this message and exit.
```

Example
```
wordsearch path/to/docs -m FindMe -m 'Find this too' -c 15 -o path/to/save/file.csv --ignore-case
```

### Arguments
Required Arguments

#### PATH
The path/directory that you would liked scanned for word documents

### Options
Option definitions

#### Match
Phrases to search for in files
* Required
* Multiple params accepted

#### Output
Path and filename for the csv to create
* Defaults to current directory/wordsearch-output.csv
* If specified, it must include the path, filename, file extension

#### Chars
Number of characters to include before and after a match
* Defaults to 30
* The count starts at the begining of the match and the end of the match

#### Ignore case
Flag to determine if the phrase matches should ignore case
* Defaults to false