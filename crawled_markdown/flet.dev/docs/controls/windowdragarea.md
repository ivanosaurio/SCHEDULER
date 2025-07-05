[Skip to main content](https://flet.dev/docs/controls/windowdragarea/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/windowdragarea/)
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
  * [Cookbook](https://flet.dev/docs/controls/windowdragarea/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Utility](https://flet.dev/docs/controls/utility)
  * WindowDragArea


On this page
# WindowDragArea
A control for drag to move, maximize and restore application window.
When you have hidden the title bar with [`page.window.title_bar_hidden`](https://flet.dev/docs/reference/types/window#title_bar_hidden), you can add this control to move the window position.
## Examples[​](https://flet.dev/docs/controls/windowdragarea/#examples "Direct link to Examples")
### App window without a title that can be moved[​](https://flet.dev/docs/controls/windowdragarea/#app-window-without-a-title-that-can-be-moved "Direct link to App window without a title that can be moved")
![](https://flet.dev/img/docs/controls/window-drag-area/no-title-draggable-window.png)
python/controls/utility/window-drag-area/no-frame-window.py
```
import flet as ftdefmain(page: ft.Page):  page.window.title_bar_hidden =True  page.window.title_bar_buttons_hidden =True  page.add(    ft.Row([        ft.WindowDragArea(          ft.Container(            ft.Text("Drag this area to move, maximize and restore application window."),            bgcolor=ft.Colors.AMBER_300,            padding=10,),          expand=True,),        ft.IconButton(ft.Icons.CLOSE, on_click=lambda_: page.window.close()),]))ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/utility/window-drag-area/no-frame-window.py)
## Properties[​](https://flet.dev/docs/controls/windowdragarea/#properties "Direct link to Properties")
### `content`[​](https://flet.dev/docs/controls/windowdragarea/#content "Direct link to content")
A control to use for dragging/maximizing/restoring app window.
Value is of type `Control`.
### `maximizable`[​](https://flet.dev/docs/controls/windowdragarea/#maximizable "Direct link to maximizable")
Whether double-clicking on a window drag area causes window to maximize/restore.
Value is of type `bool` and defaults to `True`.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/windowdragarea.md)
[PreviousVideo](https://flet.dev/docs/controls/video)[NextTheming](https://flet.dev/docs/cookbook/theming)
  * [Examples](https://flet.dev/docs/controls/windowdragarea/#examples)
    * [App window without a title that can be moved](https://flet.dev/docs/controls/windowdragarea/#app-window-without-a-title-that-can-be-moved)
  * [Properties](https://flet.dev/docs/controls/windowdragarea/#properties)
    * [`content`](https://flet.dev/docs/controls/windowdragarea/#content)
    * [`maximizable`](https://flet.dev/docs/controls/windowdragarea/#maximizable)


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
