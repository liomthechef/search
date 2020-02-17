# search

## Solution has been implemented using simple hashmaps and JSON library, along with Panda for formatting along with some minor utilities.

## Usage:
- Install Python 3
- python3 -m pip install --upgrade pip
- pip3 install virtualenv
- ./run.sh (will install deps in venv)
- ./tests.sh will run tests/linting

## Criteria:
- Simplicity, I went with a simple three hashmap instead of building something relational, because time.
- Test coverage, search module is mostly covered, the input module was a bit tougher but if you break the data parsing, the tests will fail.
- Performance, it's in memory, and python is a bit loop happy and very single threaded but it should run reasonably considering the scope of the task, could easily put the hashmaps in a key value database and go horizontally in a lambda
- Robustness, exception handling is one of those things... i've put a reasonable amount of input sanitization, keeping the input options simple helps with that, but i'm not keen on throwing exceptions in the users face; maybe with something financial.
- Extensibility, it's a light app but you could fairly easily bolt the input module onto a different backend module, see my sql branch for an early rabbit hole

## Enhancements:
- There's a need for relational style querying or better indexing in general to properly do relational searching
- if I was to invest a bit more time i'd clean up functions a little to handle testing more gracefully. (TDD)
- It does need mock inputs for tests to call this complete.

## Notes:
- blank field searching should work
- cross table querying only works with key based fields, but I think that was intended.
- I tried to keep the printing to inbuilt libraries and without colours as much as I wanted to I know it can break on windows.
