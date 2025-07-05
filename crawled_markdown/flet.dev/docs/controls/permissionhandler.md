[Skip to main content](https://flet.dev/docs/controls/permissionhandler/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/permissionhandler/)
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
  * [Cookbook](https://flet.dev/docs/controls/permissionhandler/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Utility](https://flet.dev/docs/controls/utility)
  * PermissionHandler


On this page
# PermissionHandler
PermissionHandler can check and/or request permissions from the running device for access to various components. Works on Windows, iOS, Android and web. Based on the [permission_handler](https://pub.dev/packages/permission_handler) Dart/Flutter package.
PermissionHandler control is non-visual and should be added to [`page.overlay`](https://flet.dev/docs/controls/page#overlay) list.
Packaging
To build your Flet app that uses `PermissionHandler` control add `flet-permission-handler` to `dependencies` key of the `[project]` section of your `pyproject.toml` file, for example:
```
[project]...dependencies=["flet==0.27.6","flet-premission-handler==0.1.0",]
```

## Examples[​](https://flet.dev/docs/controls/permissionhandler/#examples "Direct link to Examples")
### Basic Example[​](https://flet.dev/docs/controls/permissionhandler/#basic-example "Direct link to Basic Example")
python/controls/utility/permission-handler/permission-handler-example.py
```
import flet as ftdefmain(page: ft.Page):  page.scroll = ft.ScrollMode.ADAPTIVE  page.appbar = ft.AppBar(title=ft.Text("PermissionHandler Tests"))  ph = ft.PermissionHandler()  page.overlay.append(ph)defcheck_permission(e):    o = ph.check_permission(e.control.data)    page.add(ft.Text(f"Checked {e.control.data.name}: {o}"))defrequest_permission(e):    o = ph.request_permission(e.control.data)    page.add(ft.Text(f"Requested {e.control.data.name}: {o}"))defopen_app_settings(e):    o = ph.open_app_settings()    page.add(ft.Text(f"App Settings: {o}"))  page.add(    ft.OutlinedButton("Check Microphone Permission",      data=ft.PermissionType.MICROPHONE,      on_click=check_permission,),    ft.OutlinedButton("Request Microphone Permission",      data=ft.PermissionType.MICROPHONE,      on_click=request_permission,),    ft.OutlinedButton("Open App Settings",      on_click=open_app_settings,),)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/utility/permission-handler/permission-handler-example.py)
## Methods[​](https://flet.dev/docs/controls/permissionhandler/#methods "Direct link to Methods")
### `check_permission(of: PermissionType)`[​](https://flet.dev/docs/controls/permissionhandler/#check_permissionof-permissiontype "Direct link to check_permissionof-permissiontype")
Checks the status of the specified [`PermissionType`](https://flet.dev/docs/reference/types/permissiontype).
Returns an instance of type [`PermissionStatus`](https://flet.dev/docs/reference/types/permissionstatus).
### `open_app_settings()`[​](https://flet.dev/docs/controls/permissionhandler/#open_app_settings "Direct link to open_app_settings")
Opens the device's settings. Before calling this method, you usually want to briefly remind the user of which permission is needed and how/where precisely it is to be enabled.
Returns a boolean value: `True` if the device's settings were opened successfully, `False` otherwise.
### `request_permission(of: PermissionType)`[​](https://flet.dev/docs/controls/permissionhandler/#request_permissionof-permissiontype "Direct link to request_permissionof-permissiontype")
Requests the device for access to the specified [`PermissionType`](https://flet.dev/docs/reference/types/permissiontype) from the user.
Returns an instance of type [`PermissionStatus`](https://flet.dev/docs/reference/types/permissionstatus).
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/permissionhandler.md)
[PreviousMergeSemantics](https://flet.dev/docs/controls/mergesemantics)[NextSelectionArea](https://flet.dev/docs/controls/selectionarea)
  * [Examples](https://flet.dev/docs/controls/permissionhandler/#examples)
    * [Basic Example](https://flet.dev/docs/controls/permissionhandler/#basic-example)
  * [Methods](https://flet.dev/docs/controls/permissionhandler/#methods)
    * [`check_permission(of: PermissionType)`](https://flet.dev/docs/controls/permissionhandler/#check_permissionof-permissiontype)
    * [`open_app_settings()`](https://flet.dev/docs/controls/permissionhandler/#open_app_settings)
    * [`request_permission(of: PermissionType)`](https://flet.dev/docs/controls/permissionhandler/#request_permissionof-permissiontype)


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
