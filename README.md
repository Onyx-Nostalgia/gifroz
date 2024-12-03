# Random GIF

## Command 

### example
```
python main.py --api-key <TENOR_API_KEY> 
```
output: replace new gif to `outputs/technology.gif`

### example with search word

```
python main.py --api-key <TENOR_API_KEY> -q cat
```
output: replace new gif to `outputs/cat.gif`

```
Usage: main.py [OPTIONS]

  Downloads a random GIF matching the given search term from Tenor and saves
  it to a file named after the search term in the "outputs" directory.

Options:
  -k, --api-key TEXT  API key for Tenor  [required]
  -q, --search TEXT   Search term for GIFs  [default: technology]
  --help              Show this message and exit.
```

Workflow Steps

- use ubuntu
- use python 3.12
- load requirement
- run command: 
    python main.py --search ${{ vars.SEARCH_KEY }} --api-key ${{ secrets.TENOR_API_KEY }}
- commit