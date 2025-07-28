<div align="center">

# <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Activities/Party%20Popper.png" alt="Party Popper" width="30" height="30" /> Gifroz <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Activities/Party%20Popper.png" alt="Party Popper" width="30" height="30" />
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white&style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-3.1.1-green?logo=flask&logoColor=white&style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?logo=open-source-initiative&logoColor=white&style=for-the-badge)
![Vercel](https://img.shields.io/badge/Vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?logo=github&logoColor=white&style=for-the-badge)
![deployment](https://img.shields.io/badge/deployment-automatic-brightgreen?logo=github&logoColor=white&style=for-the-badge)

<img src="https://gifroz.vercel.app/" height="200" />

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Backhand%20Index%20Pointing%20Right.png" alt="Backhand Index Pointing Right" width="25" height="25" /> [https://gifroz.vercel.app/](https://gifroz.vercel.app/) <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Backhand%20Index%20Pointing%20Left.png" alt="Backhand Index Pointing Left" width="25" height="25" />


Experience a new random GIF from GIPHY or Tenor with **every refresh!** Gifroz offers an incredibly simple URL that's a breeze to integrate. 

**Don't believe it? Refresh this page and see the magic!** <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Activities/Crystal%20Ball.png" alt="Crystal Ball" width="25" height="25" />


[![Live Demo](https://img.shields.io/badge/Live%20Demo-3d2c7e?style=for-the-badge&logo=rocket&logoColor=white)](https://gifroz.vercel.app/)


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
![Random GIF](https://gifroz.vercel.app/)
```

### HTML Integration Example
```html
<img src="https://gifroz.vercel.app/" alt="Random GIF">
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

### Examples with Query Parameter

#### Search: fat cat
```markdown
![Random GIF](https://gifroz.vercel.app/?q=fat%20cat)
```
![Random GIF](https://gifroz.vercel.app/?q=fat%20cat)

#### Search: dev & meme
```markdown
![Random GIF](https://gifroz.vercel.app/?q=dev%20%26%20meme)
```
![Random GIF](https://gifroz.vercel.app/?q=dev%20%26%20meme)

#### Search: dev=meme
```markdown
![Random GIF](https://gifroz.vercel.app/?q=dev%3Dmeme)
```
![Random GIF](https://gifroz.vercel.app/?q=dev%3Dmeme)

#### Search: dev-meme
```markdown
![Random GIF](https://gifroz.vercel.app/?q=dev-meme)
```
![Random GIF](https://gifroz.vercel.app/?q=dev-meme)

#### Search: dev gif from Tenor
```markdown
![Random GIF](https://gifroz.vercel.app/?q=dev&source=tenor)
```
![Random GIF](https://gifroz.vercel.app/?q=dev&source=tenor)

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/People%20with%20activities/Man%20Raising%20Hand%20Light%20Skin%20Tone.png" alt="Hand" width="25" height="25" /> Contributing

Contributions are welcome! If you have suggestions or want to improve Gifroz, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

Please open an issue first to discuss any significant changes.

---

## 🔗 Content Attribution

This project utilizes content (GIFs/WebPs) sourced from the following APIs:

* **Tenor:** Powered By Tenor. [Tenor API](https://developers.google.com/tenor/guides/quickstart)
* **GIPHY:** Powered By GIPHY. [GIPHY API](https://developers.giphy.com/docs/api/)

Please note that all content is subject to the respective terms of service and licensing of Tenor and GIPHY.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Red%20Heart.png" alt="Heart" width="20" height="20" /> and Python <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Snake.png" alt="Snake" width="20" height="20" />

</div>