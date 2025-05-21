<div align="center">

# <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Activities/Party%20Popper.png" alt="Party Popper" width="30" height="30" /> Gifroz <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Activities/Party%20Popper.png" alt="Party Popper" width="30" height="30" />

<img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Disguised%20Face.png" alt="Disguised Face" width="50" height="50" />

A fun and fast random GIF generator powered by GIPHY and Tenor APIs! <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Star.png" alt="Star" width="30" height="30" />

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white&style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-3.1.1-green?logo=flask&logoColor=white&style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?logo=open-source-initiative&logoColor=white&style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?logo=github&logoColor=white&style=for-the-badge)
![Made with Python](http://ForTheBadge.com/images/badges/made-with-python.svg)

</div>

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Glowing%20Star.png" alt="Glowing Star" width="25" height="25" /> Features

- 🎨 Generate random GIFs based on search terms.
- 🔍 Supports both GIPHY and Tenor as sources.
- 🖼️ Easy integration with markdown, HTML, or direct URL usage.
- ⚡ Fast and lightweight API.
- 🔧 Fully customizable with query parameters.

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Rocket.png" alt="Rocket" width="25" height="25" /> How to Use

### Markdown Integration Example
```markdown
![Random GIF](http://localhost:5000)
```

### HTML Integration Example
```html
<img src="http://localhost:5000" alt="Random GIF">
```
### Query Parameters

| Parameter | Description                                                                 | Default Value | Example Usage                     |
|-----------|-----------------------------------------------------------------------------|---------------|-----------------------------------|
| `q`       | Search term for the GIF. Avoid special characters like `&`, `=`. Use URL encoding for spaces (e.g., `q=qa%20meme`). | `meme`        | `q=cat`                        |
| `source`  | Source for the GIF. Options: `giphy` or `tenor`.                           | `giphy`       | `source=tenor`                   |

> [!WARNING]  
> Avoid using special characters like `&`, `=` directly in the `q` parameter. These characters can cause issues with the API. Instead, use URL encoding. For example:
> - Use `%20` for spaces (e.g., `q=qa%20meme`).
> - Replace `&` with `%26` (e.g., `q=pm%26qa`).

#### Examples with Query Parameter

**Search: cats shocked**
```markdown
![Random GIF](http://localhost:5000/?q=cats%20shocked)
```

**Search: dev & meme**
```markdown
![Random GIF](http://localhost:5000/?q=dev%20%26%20meme)
```

**Search: dev=meme**
```markdown
![Random GIF](http://localhost:5000/?q=dev%3Dmeme)
```

**Search: dev-meme**
```markdown
![Random GIF](http://localhost:5000/?q=dev-meme)
```

**Search: dev gif from Tenor**
```markdown
![Random GIF](http://localhost:5000/?q=dev&source=tenor)
```

---

## 🛠️ Setup for Development

Follow these steps to set up the project for development:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/gifroz.git
cd gifroz
```

### 2. Install Dependencies
Make sure you have `uv` installed:
```bash
pip install uv
```
Then initialize the project:
```bash
uv init gifroz
uv add flask python-dotenv requests
```

### 3. Create a `.env` File
Create a `.env` file in the root directory with the following  content [.env.example](.env.example)

### 4. Run the Project
Start the server:
```bash
uv run python flask run
```
The API will be available at `http://localhost:5000/`.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Red%20Heart.png" alt="Heart" width="20" height="20" /> and Python <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Snake.png" alt="Snake" width="20" height="20" />

</div>