[Skip to main content](https://flet.dev/docs/cookbook/fonts/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/cookbook/fonts/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/cookbook/fonts/)
    * [Theming](https://flet.dev/docs/cookbook/theming)
    * [Keyboard shortcuts](https://flet.dev/docs/cookbook/keyboard-shortcuts)
    * [Large lists](https://flet.dev/docs/cookbook/large-lists)
    * [Drag and drop](https://flet.dev/docs/cookbook/drag-and-drop)
    * [File picker and uploads](https://flet.dev/docs/cookbook/file-picker-and-uploads)
    * [Animations](https://flet.dev/docs/cookbook/animations)
    * [Authentication](https://flet.dev/docs/cookbook/authentication)
    * [Assets](https://flet.dev/docs/cookbook/assets)
    * [Fonts](https://flet.dev/docs/cookbook/fonts)
    * [Read and write files](https://flet.dev/docs/cookbook/read-and-write-files)
    * [Client storage](https://flet.dev/docs/cookbook/client-storage)
    * [Session storage](https://flet.dev/docs/cookbook/session-storage)
    * [Encrypting sensitive data](https://flet.dev/docs/cookbook/encrypting-sensitive-data)
    * [PubSub](https://flet.dev/docs/cookbook/pub-sub)
    * [Control Refs](https://flet.dev/docs/cookbook/control-refs)
    * [Accessibility](https://flet.dev/docs/cookbook/accessibility)
    * [Logging](https://flet.dev/docs/cookbook/logging)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * Cookbook
  * Fonts


On this page
# Fonts
## System fonts[​](https://flet.dev/docs/cookbook/fonts/#system-fonts "Direct link to System fonts")
You can use the (system) fonts installed on your computer, e.g. "Consolas", "Arial", "Verdana", "Tahoma", etc.
Limitation
System fonts cannot be used in Flet web apps rendered with ["canvas kit"](https://flet.dev/docs/reference/types/webrenderer#canvas_kit).
### Usage Example[​](https://flet.dev/docs/cookbook/fonts/#usage-example "Direct link to Usage Example")
The following example demonstrates how to use the "Consolas" font in a Flet application.
```
import flet as ftdefmain(page: ft.Page):  page.add(    ft.Text(      value="This text is rendered with Consolas font",      font_family="Consolas"))ft.app(main)
```

## Importing Fonts[​](https://flet.dev/docs/cookbook/fonts/#importing-fonts "Direct link to Importing Fonts")
Font can be imported from external resource by providing an absolute URL or from application assets directory (see [Assets Guide](https://flet.dev/docs/cookbook/assets)).
This is done by setting the page's [`fonts`](https://flet.dev/docs/controls/page#fonts) property.
To apply one of the imported fonts, you can:
  * Use [`Theme.font_family`](https://flet.dev/docs/reference/types/theme#font_family) to set a default/fallback app-wide font family.
  * Specify a font for individual controls. For example, [`Text.font_family`](https://flet.dev/docs/controls/text#font_family).


### Usage Example[​](https://flet.dev/docs/cookbook/fonts/#usage-example-1 "Direct link to Usage Example")
The example below loads the "Kanit" font from GitHub and "Open Sans" from local assets. "Kanit" is set as the default app font, while "Open Sans" is applied to a specific `Text` control.
```
import flet as ftdefmain(page: ft.Page):  page.fonts ={"Kanit":"https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf","Open Sans":"/fonts/OpenSans-Regular.ttf"}  page.theme = ft.Theme(font_family="Kanit")# Default app font  page.add(    ft.Text("This text uses the Kanit font"),    ft.Text("This text uses the Open Sans font", font_family="Open Sans"))ft.app(main, assets_dir="assets")
```

### Static and Variable Fonts[​](https://flet.dev/docs/cookbook/fonts/#static-and-variable-fonts "Direct link to Static and Variable Fonts")
Currently, only [static fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Fonts/Variable_Fonts_Guide#standard_or_static_fonts) are supported. These fonts have a specific width, weight, or style combination (e.g., "Open Sans Regular").
Support for [variable fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Fonts/Variable_Fonts_Guide#variable_fonts) is in progress.
However, to use variable fonts, you can create static instances at specific weights using [fonttools](https://pypi.org/project/fonttools/), e.g.:
```
fonttools varLib.mutator ./YourVariableFont-VF.ttf wght=140wdth=85
```

To explore available font features (e.g. possible options for `wght`) use [Wakamai Fondue](https://wakamaifondue.com/beta/) online tool.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/cookbook/fonts.md)
[PreviousAssets](https://flet.dev/docs/cookbook/assets)[NextRead and write files](https://flet.dev/docs/cookbook/read-and-write-files)
  * [System fonts](https://flet.dev/docs/cookbook/fonts/#system-fonts)
    * [Usage Example](https://flet.dev/docs/cookbook/fonts/#usage-example)
  * [Importing Fonts](https://flet.dev/docs/cookbook/fonts/#importing-fonts)
    * [Usage Example](https://flet.dev/docs/cookbook/fonts/#usage-example-1)
    * [Static and Variable Fonts](https://flet.dev/docs/cookbook/fonts/#static-and-variable-fonts)


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
