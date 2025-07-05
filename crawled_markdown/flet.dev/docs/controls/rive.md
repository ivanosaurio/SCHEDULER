[Skip to main content](https://flet.dev/docs/controls/rive/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/rive/)
  * [Controls](https://flet.dev/docs/controls)
    * [Layout](https://flet.dev/docs/controls/layout)
    * [Navigation](https://flet.dev/docs/controls/app-structure-navigation)
    * [Information Displays](https://flet.dev/docs/controls/information-displays)
    * [Buttons](https://flet.dev/docs/controls/buttons)
    * [Input and Selections](https://flet.dev/docs/controls/input-and-selections)
    * [Dialogs, Alerts and Panels](https://flet.dev/docs/controls/dialogs-alerts-panels)
    * [Charts](https://flet.dev/docs/controls/charts)
    * [Animations](https://flet.dev/docs/controls/animations)
      * [AnimatedSwitcher](https://flet.dev/docs/controls/animatedswitcher)
      * [Lottie](https://flet.dev/docs/controls/lottie)
      * [Rive](https://flet.dev/docs/controls/rive)
    * [Utility](https://flet.dev/docs/controls/utility)
  * [Cookbook](https://flet.dev/docs/controls/rive/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Animations](https://flet.dev/docs/controls/animations)
  * Rive


On this page
# Rive
Displays an animation from a [Rive](https://rive.app/) file (URL or local file).
## Examples[​](https://flet.dev/docs/controls/rive/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/utility/rive)
### Basic Example[​](https://flet.dev/docs/controls/rive/#basic-example "Direct link to Basic Example")
python/controls/animations/rive/rive-basic.py
```
import flet as ftdefmain(page):  page.add(    ft.Rive("https://cdn.rive.app/animations/vehicles.riv",      placeholder=ft.ProgressBar(),      width=300,      height=200,))ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/animations/rive/rive-basic.py)
![](https://flet.dev/img/docs/controls/rive/basic-rive.gif)
## Properties[​](https://flet.dev/docs/controls/rive/#properties "Direct link to Properties")
### `alignment`[​](https://flet.dev/docs/controls/rive/#alignment "Direct link to alignment")
The alignment for the animation.
### `artboard`[​](https://flet.dev/docs/controls/rive/#artboard "Direct link to artboard")
The name of the artboard to use. If not specified, the default artboard of the provided `src` is used.
### `enable_antialiasing`[​](https://flet.dev/docs/controls/rive/#enable_antialiasing "Direct link to enable_antialiasing")
Whether to enable antialiasing when rendering.
Defaults to `True`.
### `fit`[​](https://flet.dev/docs/controls/rive/#fit "Direct link to fit")
The animation's fit.
### `placeholder_content`[​](https://flet.dev/docs/controls/rive/#placeholder_content "Direct link to placeholder_content")
The control to be displayed while the rive is loading.
### `src`[​](https://flet.dev/docs/controls/rive/#src "Direct link to src")
The source of your rive animation. Can either be a URL or a local asset file.
### `use_artboard_size`[​](https://flet.dev/docs/controls/rive/#use_artboard_size "Direct link to use_artboard_size")
Whether to use the inherent size of the artboard, i.e. the absolute size defined by the artboard, or size the widget based on the available constraints only (sized by parent). Defaults to `False`.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/rive.md)
[PreviousLottie](https://flet.dev/docs/controls/lottie)[NextUtility](https://flet.dev/docs/controls/utility)
  * [Examples](https://flet.dev/docs/controls/rive/#examples)
    * [Basic Example](https://flet.dev/docs/controls/rive/#basic-example)
  * [Properties](https://flet.dev/docs/controls/rive/#properties)
    * [`alignment`](https://flet.dev/docs/controls/rive/#alignment)
    * [`artboard`](https://flet.dev/docs/controls/rive/#artboard)
    * [`enable_antialiasing`](https://flet.dev/docs/controls/rive/#enable_antialiasing)
    * [`fit`](https://flet.dev/docs/controls/rive/#fit)
    * [`placeholder_content`](https://flet.dev/docs/controls/rive/#placeholder_content)
    * [`src`](https://flet.dev/docs/controls/rive/#src)
    * [`use_artboard_size`](https://flet.dev/docs/controls/rive/#use_artboard_size)


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
