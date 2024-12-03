# 🥸 Random GIF
daily random **technology GIF** every **5 mins**

![image](https://raw.githubusercontent.com/Onyx-Nostalgia/random-gif/refs/heads/master/outputs/technology.gif)
## 🤪 How to use

### Use by URL link: 
**`https://raw.githubusercontent.com/Onyx-Nostalgia/random-gif/refs/heads/master/outputs/technology.gif`**

### Use in markdown
```md
![image](https://raw.githubusercontent.com/Onyx-Nostalgia/random-gif/refs/heads/master/outputs/technology.gif)
```
### Use in HTML
```html
<img src="https://raw.githubusercontent.com/Onyx-Nostalgia/random-gif/refs/heads/master/outputs/technology.gif"/>
```

## 🚥Command 

default search key is **technology**
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

### Help description
```
Usage: main.py [OPTIONS]

  Downloads a random GIF matching the given search term from Tenor and saves
  it to a file named after the search term in the "outputs" directory.

Options:
  -k, --api-key TEXT  API key for Tenor  [required]
  -q, --search TEXT   Search term for GIFs  [default: technology]
  --help              Show this message and exit.
```