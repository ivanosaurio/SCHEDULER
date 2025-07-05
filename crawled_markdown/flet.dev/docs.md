[Skip to main content](https://flet.dev/docs/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search
[![Flet Logo](https://flet.dev/img/logo.svg)![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/extend/built-in-extensions)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/cookbook/theming)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * Introduction


On this page
# Introduction
## What is Flet?[​](https://flet.dev/docs/#what-is-flet "Direct link to What is Flet?")
Flet is a framework that allows building web, desktop and mobile applications in Python without prior experience in frontend development.
You can build a UI for your program with Flet [controls](https://flet.dev/docs/controls) which are based on [Flutter](https://flutter.dev) by Google. Flet goes beyond merely wrapping Flutter widgets. It adds its own touch by combining smaller widgets, simplifying complexities, implementing UI best practices, and applying sensible defaults. This ensures that your applications look stylish and polished without requiring additional design efforts on your part.
## Flet app example[​](https://flet.dev/docs/#flet-app-example "Direct link to Flet app example")
Create a sample "Counter" app:
counter.py
```
import flet as ftdefmain(page: ft.Page):  page.title ="Flet counter example"  page.vertical_alignment = ft.MainAxisAlignment.CENTER  txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)defminus_click(e):    txt_number.value =str(int(txt_number.value)-1)    page.update()defplus_click(e):    txt_number.value =str(int(txt_number.value)+1)    page.update()  page.add(    ft.Row([        ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),        txt_number,        ft.IconButton(ft.Icons.ADD, on_click=plus_click),],      alignment=ft.MainAxisAlignment.CENTER,))ft.app(main)
```

To run the app install `flet` module ([create a new Flet environment](https://flet.dev/docs/getting-started)):
```
pip install flet
```

and [run the program](https://flet.dev/docs/getting-started/running-app):
```
flet run counter.py
```

The app will be started in a native OS window - what a nice alternative to Electron!
### macOS
![](https://flet.dev/img/docs/getting-started/flet-counter-macos.png)
### Windows
![](https://flet.dev/img/docs/getting-started/flet-counter-windows.png)
Now, run your app as a web app:
```
flet run --web counter.py
```

A new browser window or tab will be opened:
![](https://flet.dev/img/docs/getting-started/flet-counter-safari.png)
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/introduction.md)
[NextGetting started](https://flet.dev/docs/getting-started/)
  * [What is Flet?](https://flet.dev/docs/#what-is-flet)
  * [Flet app example](https://flet.dev/docs/#flet-app-example)


Docs
  * [Introduction](https://flet.dev/docs)
  * [Controls reference](https://flet.dev/docs/controls)


Community
  * [Discord](https://discord.gg/dzWXP8SHG8)
  * [Stack Overflow](https://stackoverflow.com/questions/tagged/flet)
  * [X](https://x.com/fletdev)
  * [Bluesky](https://bsky.app/profile/fletdev.bsky.social)


More
  * [Blog](https://flet.dev/blog)
  * [GitHub](https://github.com/flet-dev/flet)
  * [Support](https://flet.dev/support)


Legal
  * [Privacy policy](https://flet.dev/privacy-policy)


Copyright © 2025 Appveyor Systems Inc. Built with Docusaurus.
