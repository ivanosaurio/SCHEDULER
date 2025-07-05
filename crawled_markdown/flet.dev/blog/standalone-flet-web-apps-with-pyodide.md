[Skip to main content](https://flet.dev/blog/standalone-flet-web-apps-with-pyodide/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
All posts
### 2025
  * [Introducing Flet 1.0 Alpha](https://flet.dev/blog/introducing-flet-1-0-alpha)
  * [Tap into native Android and iOS APIs with Pyjnius and Pyobjus](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus)
  * [Flet v0.27.0 Release Announcement](https://flet.dev/blog/flet-v-0-27-release-announcement)
  * [Flet v0.26.0 Release Announcement](https://flet.dev/blog/flet-v-0-26-release-announcement)


### 2024
  * [Flet v0.25.0 Release Announcement](https://flet.dev/blog/flet-v-0-25-release-announcement)
  * [pyproject.toml support for flet build command](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command)
  * [Flet new packaging pre-release](https://flet.dev/blog/flet-new-packaging-pre-release)
  * [Flet v0.24.0 Release Announcement](https://flet.dev/blog/flet-v-0-24-release-announcement)
  * [Flet v0.23.0 Release Announcement](https://flet.dev/blog/flet-v-0-23-release-announcement)
  * [Flet at PyCon US 2024](https://flet.dev/blog/flet-at-pycon-us-2024)
  * [Flet packaging update](https://flet.dev/blog/flet-packaging-update)
  * [Controls and theming enhancements](https://flet.dev/blog/controls-and-theming-enhancements)
  * [Flet FastAPI and async API improvements](https://flet.dev/blog/flet-fastapi-and-async-api-improvements)
  * [Flet adaptive UI and custom controls release](https://flet.dev/blog/flet-adaptive-and-custom-controls)


### 2023
  * [Packaging apps for distribution](https://flet.dev/blog/packaging-apps-for-distribution)
  * [Flet for FastAPI](https://flet.dev/blog/flet-for-fastapi)
  * [Flet for Android](https://flet.dev/blog/flet-for-android)
  * [Flet for iOS](https://flet.dev/blog/flet-for-ios)
  * [Scrolling controls and Theming](https://flet.dev/blog/scrolling-controls-and-theming)
  * [Canvas](https://flet.dev/blog/canvas)
  * [Flet Charts](https://flet.dev/blog/flet-charts)
  * [Standalone Flet web apps with Pyodide](https://flet.dev/blog/standalone-flet-web-apps-with-pyodide)
  * [Packaging desktop apps with a custom icon](https://flet.dev/blog/packaging-desktop-apps-with-custom-icon)


### 2022
  * [Flet mobile update](https://flet.dev/blog/flet-mobile-update)
  * [Flet versioning and pre-releases](https://flet.dev/blog/flet-versioning-and-pre-releases)
  * [ResponsiveRow and mobile controls](https://flet.dev/blog/responsive-row-and-mobile-controls)
  * [Matplotlib and Plotly charts](https://flet.dev/blog/matplotlib-and-plotly-charts)
  * [Gesture detector](https://flet.dev/blog/gesture-detector)
  * [User authentication](https://flet.dev/blog/user-authentication)
  * [File picker and uploads](https://flet.dev/blog/file-picker-and-uploads)
  * [Fun with animations](https://flet.dev/blog/fun-with-animations)
  * [Beautiful gradients, button styles and TextField rounded corners in a new Flet release](https://flet.dev/blog/gradients-button-textfield-styles)
  * [Control Refs](https://flet.dev/blog/control-refs)
  * [Flet Mobile Strategy](https://flet.dev/blog/flet-mobile-strategy)
  * [Navigation and Routing](https://flet.dev/blog/navigation-and-routing)
  * [New release: Drag and Drop, absolute positioning and clickable container](https://flet.dev/blog/drag-and-drop-release)
  * [Using custom fonts in a Flet app](https://flet.dev/blog/using-custom-fonts-in-flet-app)
  * [Introducing Flet](https://flet.dev/blog/introducing-flet)


# Standalone Flet web apps with Pyodide
February 6, 2023 · 4 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
We've just released [Flet 0.4.0](https://pypi.org/project/flet/) with a super exciting new feature - [packaging Flet apps into a standalone static website](https://flet.dev/docs/publish/web/static-website) that can be run entirely in the browser! The app can be published to any free hosting for static websites such as GitHub Pages or Cloudflare Pages. Thanks to [Pyodide](https://pyodide.org/en/stable/) - a Python port to WebAssembly!
![](https://flet.dev/img/blog/pyodide/pyodide-logo.png)
You can quickly build awesome single-page applications (SPA) entirely in Python and host them everywhere! No HTML, CSS or JavaScript required!
## Quick Flet with Pyodide demo[​](https://flet.dev/blog/standalone-flet-web-apps-with-pyodide/#quick-flet-with-pyodide-demo "Direct link to Quick Flet with Pyodide demo")
Install the latest Flet package:
```
pip install flet --upgrade
```

Create a simple `counter.py` app:
counter.py
```
import flet as ftdefmain(page: ft.Page):  page.title ="Flet counter example"  page.vertical_alignment = ft.MainAxisAlignment.CENTER  txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)defminus_click(e):    txt_number.value =str(int(txt_number.value)-1)    page.update()defplus_click(e):    txt_number.value =str(int(txt_number.value)+1)    page.update()  page.add(    ft.Row([        ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),        txt_number,        ft.IconButton(ft.Icons.ADD, on_click=plus_click),],      alignment=ft.MainAxisAlignment.CENTER,))ft.app(main)
```

Run a brand-new `flet publish` command to publish Flet app as a static website:
```
flet publish counter.py
```

The website will be published to `dist` directory next to `counter.py`. Give website a try using built-in Python web server:
```
python -m http.server --directory dist
```

Open `http://localhost:8000` in your browser to check the published app.
![](https://flet.dev/img/docs/getting-started/flet-counter-safari.png)
Here are a few live Flet apps hosted at Cloudflare Pages:
[![](https://flet.dev/img/gallery/todo.png)To-Do](https://gallery.flet.dev/todo/)
[![](https://flet.dev/img/gallery/icons-browser.png)Icons browser](https://gallery.flet.dev/icons-browser/)
[![](https://flet.dev/img/gallery/calc.png)Calc](https://gallery.flet.dev/calculator/)
[![](https://flet.dev/img/gallery/solitaire.png)Solitaire](https://gallery.flet.dev/solitaire/)
[![](https://flet.dev/img/gallery/trolli.png)Trolli](https://gallery.flet.dev/trolli/)
[Check the guide](https://flet.dev/docs/publish/web/static-website) for more information about publishing Flet apps as standalone websites.
## Built-in Fletd server in Python[​](https://flet.dev/blog/standalone-flet-web-apps-with-pyodide/#built-in-fletd-server-in-python "Direct link to Built-in Fletd server in Python")
Flet 0.4.0 also implements a [new Flet desktop architecture](https://flet.dev/blog/flet-mobile-update#flet-new-desktop-architecture).
It replaces Fletd server written in Go with a light-weight shim written in Python with a number of pros:
  1. Only 2 system processes are needed to run Flet app: Python interpreter and Flutter client.
  2. Less communication overhead (minus two network hops between Python and Fletd) and lower latency (shim uses TCP on Windows and Unix domain sockets on macOS/Linux).
  3. Shim binds to `127.0.0.1` on Windows by default which is more secure.
  4. The size of a standalone app bundle produced by `flet pack` reduced by ~8 MB.


The implementation was also required to support Pyodide (we can't run Go web server in the browser, right?) and paves the way to iOS and Android support.
### Other changes[​](https://flet.dev/blog/standalone-flet-web-apps-with-pyodide/#other-changes "Direct link to Other changes")
  * All controls loading resources from web URLs (`Image.src`, `Audio.src`, `Page.fonts`, `Container.image_src`) are now able to load them from local files too, by providing a full path in the file system, and from `assets` directory by providing relative path. For desktop apps a path in `src` property could be one of the following: 
    * A path relative to `assets` directory, with or without starting slash, for example: `/image.png` or `image.png`. The name of artifact dir should not be included.
    * An absolute path within a computer file system, e.g. `C:\projects\app\assets\image.png` or `/Users/john/images/picture.png`.
    * A full URL, e.g. `https://mysite.com/images/pic.png`.
    * Add `page.on_error = lambda e: print("Page error:", e.data)` to see failing images.
  * `flet` Python package has separated into two packages: `flet-core` and `flet`.
  * PDM replaced with Poetry.
  * `beartype` removed everywhere.


### 💥 Breaking changes[​](https://flet.dev/blog/standalone-flet-web-apps-with-pyodide/#-breaking-changes "Direct link to 💥 Breaking changes")
  * Default routing scheme changed from "hash" to "path" (no `/#/` at the end of app URL). Use `ft.app(main, route_url_strategy="hash")` to get original behavior.
  * OAuth authentication is not supported anymore in standalone desktop Flet apps.


## Async support[​](https://flet.dev/blog/standalone-flet-web-apps-with-pyodide/#async-support "Direct link to Async support")
Flet apps can now be written as async apps and use `asyncio` with other Python async libraries. Calling coroutines is naturally supported in Flet, so you don't need to wrap them to run synchronously.
To start with an async Flet app you should make `main()` method `async`:
```
import flet as ftasyncdefmain(page: ft.Page):await page.add_async(ft.Text("Hello, async world!"))ft.app(main)
```

[Read the guide](https://flet.dev/docs/getting-started/async-apps) for more information about writing async Flet apps.
## Conclusion[​](https://flet.dev/blog/standalone-flet-web-apps-with-pyodide/#conclusion "Direct link to Conclusion")
Flet 0.4.0 brings the following exciting features:
  * Standalone web apps with Pyodide running in the browser and hosted on a cheap hosting.
  * Faster and more secure architecture with a built-in Fletd server.
  * Async apps support.


Upgrade Flet module to the latest version (`pip install flet --upgrade`), give `flet publish` command a try and [let us know](https://discord.gg/dzWXP8SHG8) what you think!
Hey, by the way, [Flet project](https://github.com/flet-dev/flet) has reached ⭐️ 4.2K stars ⭐️ (+1K in just one month) - keep going!
**Tags:**
  * [releases](https://flet.dev/blog/tags/releases)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2023-02-06-standalone-flet-web-apps-with-pyodide.md)
[Newer postFlet Charts](https://flet.dev/blog/flet-charts)[Older postPackaging desktop apps with a custom icon](https://flet.dev/blog/packaging-desktop-apps-with-custom-icon)
  * [Quick Flet with Pyodide demo](https://flet.dev/blog/standalone-flet-web-apps-with-pyodide/#quick-flet-with-pyodide-demo)
  * [Built-in Fletd server in Python](https://flet.dev/blog/standalone-flet-web-apps-with-pyodide/#built-in-fletd-server-in-python)
    * [Other changes](https://flet.dev/blog/standalone-flet-web-apps-with-pyodide/#other-changes)
    * [💥 Breaking changes](https://flet.dev/blog/standalone-flet-web-apps-with-pyodide/#-breaking-changes)
  * [Async support](https://flet.dev/blog/standalone-flet-web-apps-with-pyodide/#async-support)
  * [Conclusion](https://flet.dev/blog/standalone-flet-web-apps-with-pyodide/#conclusion)


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
