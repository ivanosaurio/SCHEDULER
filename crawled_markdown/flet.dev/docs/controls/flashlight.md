[Skip to main content](https://flet.dev/docs/controls/flashlight/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/flashlight/)
  * [Controls](https://flet.dev/docs/controls)
    * [Layout](https://flet.dev/docs/controls/layout)
    * [Navigation](https://flet.dev/docs/controls/app-structure-navigation)
    * [Information Displays](https://flet.dev/docs/controls/information-displays)
    * [Buttons](https://flet.dev/docs/controls/buttons)
    * [Input and Selections](https://flet.dev/docs/controls/input-and-selections)
    * [Dialogs, Alerts and Panels](https://flet.dev/docs/controls/dialogs-alerts-panels)
    * [Charts](https://flet.dev/docs/controls/charts)
    * [Animations](https://flet.dev/docs/controls/animations)
    * [Utility](https://flet.dev/docs/controls/utility)
      * [Audio](https://flet.dev/docs/controls/audio)
      * [AudioRecorder](https://flet.dev/docs/controls/audiorecorder)
      * [Draggable](https://flet.dev/docs/controls/draggable)
      * [DragTarget](https://flet.dev/docs/controls/dragtarget)
      * [FilePicker](https://flet.dev/docs/controls/filepicker)
      * [Flashlight](https://flet.dev/docs/controls/flashlight)
      * [FletApp](https://flet.dev/docs/controls/fletapp)
      * [Geolocator](https://flet.dev/docs/controls/geolocator)
      * [GestureDetector](https://flet.dev/docs/controls/gesturedetector)
      * [HapticFeedback](https://flet.dev/docs/controls/hapticfeedback)
      * [InteractiveViewer](https://flet.dev/docs/controls/interactiveviewer)
      * [MergeSemantics](https://flet.dev/docs/controls/mergesemantics)
      * [PermissionHandler](https://flet.dev/docs/controls/permissionhandler)
      * [SelectionArea](https://flet.dev/docs/controls/selectionarea)
      * [Semantics](https://flet.dev/docs/controls/semantics)
      * [SemanticsService](https://flet.dev/docs/controls/semanticsservice)
      * [ShaderMask](https://flet.dev/docs/controls/shadermask)
      * [ShakeDetector](https://flet.dev/docs/controls/shakedetector)
      * [TransparentPointer](https://flet.dev/docs/controls/transparentpointer)
      * [Video](https://flet.dev/docs/controls/video)
      * [WindowDragArea](https://flet.dev/docs/controls/windowdragarea)
  * [Cookbook](https://flet.dev/docs/controls/flashlight/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Utility](https://flet.dev/docs/controls/utility)
  * Flashlight


On this page
# Flashlight
A control to use FlashLight. Works on iOS and Android. Based on [torch_light](https://pub.dev/packages/torch_light) Flutter widget.
Flashlight control is non-visual and should be added to `page.overlay` list.
Packaging
To build your Flet app that uses `FlashLight` control add `flet-flashlight` to `dependencies` key of the `[project]` section of your `pyproject.toml` file, for example:
```
[project]...dependencies=["flet==0.27.6","flet-flashlight==0.1.0",]
```

## Example[​](https://flet.dev/docs/controls/flashlight/#example "Direct link to Example")
python/controls/utility/flashlight/flashlight-example.py
```
import flet as ftdefmain(page: ft.Page):  flashlight = ft.Flashlight()  page.overlay.append(flashlight)  page.add(ft.TextButton("toggle", on_click=lambda_: flashlight.toggle()))ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/utility/flashlight/flashlight-example.py)
## Methods[​](https://flet.dev/docs/controls/flashlight/#methods "Direct link to Methods")
### `turn_on()`[​](https://flet.dev/docs/controls/flashlight/#turn_on "Direct link to turn_on")
Turns flashlight ON.
### `turn_off()`[​](https://flet.dev/docs/controls/flashlight/#turn_off "Direct link to turn_off")
Turns flashlight OFF.
### `toggle()`[​](https://flet.dev/docs/controls/flashlight/#toggle "Direct link to toggle")
Toggles the state of flashlight.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/flashlight.md)
[PreviousFilePicker](https://flet.dev/docs/controls/filepicker)[NextFletApp](https://flet.dev/docs/controls/fletapp)
  * [Example](https://flet.dev/docs/controls/flashlight/#example)
  * [Methods](https://flet.dev/docs/controls/flashlight/#methods)
    * [`turn_on()`](https://flet.dev/docs/controls/flashlight/#turn_on)
    * [`turn_off()`](https://flet.dev/docs/controls/flashlight/#turn_off)
    * [`toggle()`](https://flet.dev/docs/controls/flashlight/#toggle)


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
