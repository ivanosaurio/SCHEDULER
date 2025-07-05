[Skip to main content](https://flet.dev/blog/using-custom-fonts-in-flet-app/#__docusaurus_skipToContent_fallback)
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


# Using custom fonts in a Flet app
June 12, 2022 · 2 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
You can now use your own fonts in a Flet app!
The following font formats are supported:
  * `.ttc`
  * `.ttf`
  * `.otf`


Use [`page.fonts`](https://flet.dev/docs/controls/page#fonts) property to import fonts.
Set `page.fonts` property to a dictionary where key is the font family name to refer that font and the value is the URL of the font file to import:
```
defmain(page: ft.Page):  page.fonts ={"Kanit":"https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf","Aleo Bold Italic":"https://raw.githubusercontent.com/google/fonts/master/ofl/aleo/Aleo-BoldItalic.ttf"}  page.update()# ...
```

Font can be imported from external resource by providing an absolute URL or from application assets by providing relative URL and `assets_dir`.
Specify `assets_dir` in `flet.app()` call to set the location of assets that should be available to the application. `assets_dir` could be a relative to your `main.py` directory or an absolute path. For example, consider the following program structure:
```
/assets  /fonts    /OpenSans-Regular.ttfmain.py
```

## Code sample[​](https://flet.dev/blog/using-custom-fonts-in-flet-app/#code-sample "Direct link to Code sample")
The following program loads "Kanit" font from GitHub and "Open Sans" from the assets. "Kanit" is set as a default app font and "Open Sans" is used for a specific Text control:
```
import flet as ftdefmain(page: ft.Page):  page.title ="Custom fonts"  page.fonts ={"Kanit":"https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf","Open Sans":"fonts/OpenSans-Regular.ttf",}  page.theme = ft.Theme(font_family="Kanit")  page.add(    ft.Text("This is rendered with Kanit font"),    ft.Text("This is Open Sans font example", font_family="Open Sans"),)ft.app(target=main, assets_dir="assets")
```

![](https://flet.dev/img/blog/using-custom-fonts-in-flet-app/custom-fonts-example.png)
## Static vs Variable fonts[​](https://flet.dev/blog/using-custom-fonts-in-flet-app/#static-vs-variable-fonts "Direct link to Static vs Variable fonts")
At the moment only [static](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Fonts/Variable_Fonts_Guide#standard_or_static_fonts) fonts are supported, i.e. fonts containing only one specific width/weight/style combination, for example "Open Sans Regular" or "Roboto Bold Italic".
[Variable](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Fonts/Variable_Fonts_Guide#variable_fonts) fonts support is still [work in progress](https://github.com/flutter/flutter/issues/33709).
However, if you need to use a variable font in your app you can create static "instantiations" at specific weights using [fonttools](https://pypi.org/project/fonttools/), then use those:
fonttools varLib.mutator ./YourVariableFont-VF.ttf wght=140 wdth=85
To explore available font features (e.g. possible options for `wght`) use [Wakamai Fondue](https://wakamaifondue.com/beta/) online tool.
[Give Flet a try](https://flet.dev/docs) and [let us know](https://discord.gg/dzWXP8SHG8) what you think!
**Tags:**
  * [how-to](https://flet.dev/blog/tags/how-to)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2022-06-12-using-custom-fonts-in-flet-app.md)
[Newer postNew release: Drag and Drop, absolute positioning and clickable container](https://flet.dev/blog/drag-and-drop-release)[Older postIntroducing Flet](https://flet.dev/blog/introducing-flet)
  * [Code sample](https://flet.dev/blog/using-custom-fonts-in-flet-app/#code-sample)
  * [Static vs Variable fonts](https://flet.dev/blog/using-custom-fonts-in-flet-app/#static-vs-variable-fonts)


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
