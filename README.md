<div align="center">

# <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Disguised%20Face.png" alt="Disguised Face" width="25" height="25" /> Random GIF <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Partying%20Face.png" alt="Partying Face" width="25" height="25" />

daily random <b>meme</b> GIF every<b> 5 mins⌚ </b>

![image](https://raw.githubusercontent.com/Onyx-Nostalgia/random-gif/master/outputs/meme.gif)

**🪅 Copy & enjoy❗**

`https://raw.githubusercontent.com/Onyx-Nostalgia/random-gif/master/outputs/meme.gif`

</div>


## 🤪 How to use
### Use by URL link
**🪅 Copy & enjoy❗**
```
https://raw.githubusercontent.com/Onyx-Nostalgia/random-gif/master/outputs/meme.gif
```

### Use in markdown
```md
![image](https://raw.githubusercontent.com/Onyx-Nostalgia/random-gif/master/outputs/meme.gif)
```
### Use in HTML
```html
<img src="https://raw.githubusercontent.com/Onyx-Nostalgia/random-gif/master/outputs/meme.gif"/>
```

## 🚥Command 

### default example
> [!TIP] default search key is "meme" from "GIPHY"
```
python main.py --api-key <GIPHY_API_KEY> 
```
output: replace new gif to `outputs/meme.gif`

### example with search word
I want cat gif

```
python main.py --api-key <GIPHY_API_KEY> -q cat
```
output: replace new gif to `outputs/cat.gif`

### example with source option
> [!NOTE]
> Source for GIF [default: GIPHY]: **GIPHY** , **Tenor**

I want gif from tenor
```
python main.py --api-key <TENOR_API_KEY> --source tenor
```
output: replace new gif to `outputs/meme.gif`

### Help description
```
Usage: main.py [OPTIONS]

  Downloads a random GIF matching the given search term from the given source
  and saves it to a file named after the search term in the "outputs"
  directory.

Options:
  -k, --api-key TEXT          API key for Tenor and Giphy  [required]
  -q, --search TEXT           Search term for GIF  [default: meme]
  -s, --source [Tenor|GIPHY]  Source for GIF  [default: GIPHY ]
  --help                      Show this message and exit.
```
