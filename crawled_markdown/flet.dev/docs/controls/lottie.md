[Skip to main content](https://flet.dev/docs/controls/lottie/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/lottie/)
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
  * [Cookbook](https://flet.dev/docs/controls/lottie/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Animations](https://flet.dev/docs/controls/animations)
  * Lottie


On this page
# Lottie
Displays an animation from a Lottie file (URL or local file).
Packaging
To build your Flet app that uses `Lottie` control add `flet-lottie` to `dependencies` key of the `[project]` section of your `pyproject.toml` file, for example:
```
[project]...dependencies=["flet==0.27.6","flet-lottie==0.1.0",]
```

## Examples[​](https://flet.dev/docs/controls/lottie/#examples "Direct link to Examples")
python/controls/animations/lottie/lottie-basic.py
```
import flet as ftimport flet_lottie as fldefmain(page: ft.Page):  l = fl.Lottie(    src="https://raw.githubusercontent.com/xvrh/lottie-flutter/refs/heads/master/example/assets/Logo/LogoSmall.json",    reverse=False,    animate=True,)  c1 = ft.Container(content=l, bgcolor=ft.Colors.AMBER_ACCENT, padding=50)  page.add(c1)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/animations/lottie/lottie-basic.py)
![](https://flet.dev/img/docs/controls/lottie/lottie-animation-2.gif)
## Properties[​](https://flet.dev/docs/controls/lottie/#properties "Direct link to Properties")
### `animate`[​](https://flet.dev/docs/controls/lottie/#animate "Direct link to animate")
Whether the animation should be played automatically.
Defaults to `True`.
### `background_loading`[​](https://flet.dev/docs/controls/lottie/#background_loading "Direct link to background_loading")
Whether the animation should be loaded in the background.
### `filter_quality`[​](https://flet.dev/docs/controls/lottie/#filter_quality "Direct link to filter_quality")
The quality of the image layer.
Value is of type [`FilterQuality`](https://flet.dev/docs/reference/types/filterquality) and defaults to `FilterQuality.LOW`.
### `fit`[​](https://flet.dev/docs/controls/lottie/#fit "Direct link to fit")
How to inscribe the Lottie composition into the space allocated during layout.
Value is of type [`ImageFit`](https://flet.dev/docs/reference/types/imagefit).
### `repeat`[​](https://flet.dev/docs/controls/lottie/#repeat "Direct link to repeat")
Whether the animation should repeat in a loop. Has no effect if `animate` is `False`.
Defaults to `True`.
### `reverse`[​](https://flet.dev/docs/controls/lottie/#reverse "Direct link to reverse")
Whether the animation should be played in reverse (from start to end and then continuously from end to start). Has no effect if `animate` and `repeat` are `False`.
Defaults to `False`.
### `src`[​](https://flet.dev/docs/controls/lottie/#src "Direct link to src")
The source of the Lottie file. Can be a URL or a local [asset file](https://flet.dev/docs/cookbook/assets).
### `src_base64`[​](https://flet.dev/docs/controls/lottie/#src_base64 "Direct link to src_base64")
The base64 encoded string of the Lottie file. Either this or `src` must be provided. If both are provided, `src_base64` will be prioritized/used.
## Events[​](https://flet.dev/docs/controls/lottie/#events "Direct link to Events")
### `on_error`[​](https://flet.dev/docs/controls/lottie/#on_error "Direct link to on_error")
Fires when an error occurs while loading the Lottie file.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/lottie.md)
[PreviousAnimatedSwitcher](https://flet.dev/docs/controls/animatedswitcher)[NextRive](https://flet.dev/docs/controls/rive)
  * [Examples](https://flet.dev/docs/controls/lottie/#examples)
  * [Properties](https://flet.dev/docs/controls/lottie/#properties)
    * [`animate`](https://flet.dev/docs/controls/lottie/#animate)
    * [`background_loading`](https://flet.dev/docs/controls/lottie/#background_loading)
    * [`filter_quality`](https://flet.dev/docs/controls/lottie/#filter_quality)
    * [`fit`](https://flet.dev/docs/controls/lottie/#fit)
    * [`repeat`](https://flet.dev/docs/controls/lottie/#repeat)
    * [`reverse`](https://flet.dev/docs/controls/lottie/#reverse)
    * [`src`](https://flet.dev/docs/controls/lottie/#src)
    * [`src_base64`](https://flet.dev/docs/controls/lottie/#src_base64)
  * [Events](https://flet.dev/docs/controls/lottie/#events)
    * [`on_error`](https://flet.dev/docs/controls/lottie/#on_error)


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
