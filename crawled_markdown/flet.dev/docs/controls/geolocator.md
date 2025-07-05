[Skip to main content](https://flet.dev/docs/controls/geolocator/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/geolocator/)
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
  * [Cookbook](https://flet.dev/docs/controls/geolocator/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Utility](https://flet.dev/docs/controls/utility)
  * Geolocator


On this page
# Geolocator
Geolocator fetches Position from device GPS. Works on macOS, Windows, iOS, Android and web. Based on the [geolocator](https://pub.dev/packages/geolocator) Dart/Flutter package.
Geolocator control is non-visual and should be added to `page.overlay` list.
Packaging
To build your Flet app that uses `Geolocator` control add `flet-geolocator` to `dependencies` key of the `[project]` section of your `pyproject.toml` file, for example:
```
[project]...dependencies=["flet==0.27.6","flet-geolocator==0.1.0",]
```

## Examples[​](https://flet.dev/docs/controls/geolocator/#examples "Direct link to Examples")
### Basic Example[​](https://flet.dev/docs/controls/geolocator/#basic-example "Direct link to Basic Example")
python/controls/utility/geolocator/geolocator-example.py
```
import flet as ftasyncdefmain(page: ft.Page):  page.scroll = ft.ScrollMode.ADAPTIVE  page.appbar = ft.AppBar(title=ft.Text("Geolocator Tests"))defhandle_position_change(e):    page.add(ft.Text(f"New position: {e.latitude}{e.longitude}"))  gl = ft.Geolocator(    location_settings=ft.GeolocatorSettings(      accuracy=ft.GeolocatorPositionAccuracy.LOW),    on_position_change=handle_position_change,    on_error=lambda e: page.add(ft.Text(f"Error: {e.data}")),)  page.overlay.append(gl)  settings_dlg =lambda handler: ft.AlertDialog(    adaptive=True,    title=ft.Text("Opening Location Settings..."),    content=ft.Text("You are about to be redirected to the location/app settings. ""Please locate this app and grant it location permissions."),    actions=[ft.TextButton(text="Take me there", on_click=handler)],    actions_alignment=ft.MainAxisAlignment.CENTER,)asyncdefhandle_permission_request(e):    p =await gl.request_permission_async(wait_timeout=60)    page.add(ft.Text(f"request_permission: {p}"))asyncdefhandle_get_permission_status(e):    p =await gl.get_permission_status_async()    page.add(ft.Text(f"get_permission_status: {p}"))asyncdefhandle_get_current_position(e):    p =await gl.get_current_position_async()    page.add(ft.Text(f"get_current_position: ({p.latitude}, {p.longitude})"))asyncdefhandle_get_last_known_position(e):    p =await gl.get_last_known_position_async()    page.add(ft.Text(f"get_last_known_position: ({p.latitude}, {p.longitude})"))asyncdefhandle_location_service_enabled(e):    p =await gl.is_location_service_enabled_async()    page.add(ft.Text(f"is_location_service_enabled: {p}"))asyncdefhandle_open_location_settings(e):    p =await gl.open_location_settings_async()    page.close(location_settings_dlg)    page.add(ft.Text(f"open_location_settings: {p}"))asyncdefhandle_open_app_settings(e):    p =await gl.open_app_settings_async()    page.close(app_settings_dlg)    page.add(ft.Text(f"open_app_settings: {p}"))  location_settings_dlg = settings_dlg(handle_open_location_settings)  app_settings_dlg = settings_dlg(handle_open_app_settings)  page.add(    ft.Row(      wrap=True,      controls=[        ft.OutlinedButton("Request Permission",          on_click=handle_permission_request,),        ft.OutlinedButton("Get Permission Status",          on_click=handle_get_permission_status,),        ft.OutlinedButton("Get Current Position",          on_click=handle_get_current_position,),        ft.OutlinedButton("Get Last Known Position",          visible=Falseif page.web elseTrue,          on_click=handle_get_last_known_position,),        ft.OutlinedButton("Is Location Service Enabled",          on_click=handle_location_service_enabled,),        ft.OutlinedButton("Open Location Settings",          visible=Falseif page.web elseTrue,          on_click=lambda e: page.open(location_settings_dlg),),        ft.OutlinedButton("Open App Settings",          visible=Falseif page.web elseTrue,          on_click=lambda e: page.open(app_settings_dlg),),],))ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/utility/geolocator/geolocator-example.py)
## Properties[​](https://flet.dev/docs/controls/geolocator/#properties "Direct link to Properties")
### `location_settings`[​](https://flet.dev/docs/controls/geolocator/#location_settings "Direct link to location_settings")
Value is of type [`GeolocatorSettings`](https://flet.dev/docs/reference/types/geolocatorsettings).
## Methods[​](https://flet.dev/docs/controls/geolocator/#methods "Direct link to Methods")
### `get_current_position(accuracy, location_settings)`[​](https://flet.dev/docs/controls/geolocator/#get_current_positionaccuracy-location_settings "Direct link to get_current_positionaccuracy-location_settings")
Gets the current position of the device with the desired accuracy and settings.
This method has the following properties:
  * `accuracy`: value is of type [`GeolocatorPositionAccuracy`](https://flet.dev/docs/reference/types/geolocatorpositionaccuracy) and defaults to `GeolocatorPositionAccuracy.BEST`.
  * `location_settings`: value is of type [`GeolocatorSettings`](https://flet.dev/docs/reference/types/geolocatorsettings). If not specified, then the [`location_settings`](https://flet.dev/docs/controls/geolocator/#location_settings) property is used.


Returns an instance of type [`GeolocatorPosition`](https://flet.dev/docs/reference/types/geolocatorposition).
**Note:** Depending on the availability of different location services, this can take several seconds. It is recommended to call the `get_last_known_position()` method first to receive a known/cached position and update it with the result of `get_current_position()`
### `get_last_known_position()`[​](https://flet.dev/docs/controls/geolocator/#get_last_known_position "Direct link to get_last_known_position")
Gets the last known position of the device with the specified accuracy. The accuracy can be defined using the [`location_settings`](https://flet.dev/docs/controls/geolocator/#location_settings) property.
Returns an instance of type [`GeolocatorPosition`](https://flet.dev/docs/reference/types/geolocatorposition).
### `get_permission_status()`[​](https://flet.dev/docs/controls/geolocator/#get_permission_status "Direct link to get_permission_status")
Gets which permission the app has been granted to access the device's location.
Returns an instance of type [`GeolocatorPermissionStatus`](https://flet.dev/docs/reference/types/geolocatorpermissionstatus).
### `request_permission()`[​](https://flet.dev/docs/controls/geolocator/#request_permission "Direct link to request_permission")
Requests the device for access to the device's location.
Returns an instance of type [`GeolocatorPermissionStatus`](https://flet.dev/docs/reference/types/geolocatorpermissionstatus).
### `is_location_service_enabled()`[​](https://flet.dev/docs/controls/geolocator/#is_location_service_enabled "Direct link to is_location_service_enabled")
Checks if location service is enable.
Returns a boolean value: `True` if location service is enabled, `False` otherwise.
### `open_app_settings()`[​](https://flet.dev/docs/controls/geolocator/#open_app_settings "Direct link to open_app_settings")
Attempts to open device's app settings.
Returns a boolean value: `True` if the device's settings were opened successfully, `False` otherwise.
### `open_location_settings()`[​](https://flet.dev/docs/controls/geolocator/#open_location_settings "Direct link to open_location_settings")
Attempts to open device's location settings.
Returns a boolean value: `True` if the device's settings were opened successfully, `False` otherwise.
## Events[​](https://flet.dev/docs/controls/geolocator/#events "Direct link to Events")
### `on_error`[​](https://flet.dev/docs/controls/geolocator/#on_error "Direct link to on_error")
Fires when an error occurs.
### `on_position_change`[​](https://flet.dev/docs/controls/geolocator/#on_position_change "Direct link to on_position_change")
Fires when the position of the device changes.
Event handler argument is of type [`GeolocatorPositionChangeEvent`](https://flet.dev/docs/reference/types/geolocatorpositionchangeevent).
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/geolocator.md)
[PreviousFletApp](https://flet.dev/docs/controls/fletapp)[NextGestureDetector](https://flet.dev/docs/controls/gesturedetector)
  * [Examples](https://flet.dev/docs/controls/geolocator/#examples)
    * [Basic Example](https://flet.dev/docs/controls/geolocator/#basic-example)
  * [Properties](https://flet.dev/docs/controls/geolocator/#properties)
    * [`location_settings`](https://flet.dev/docs/controls/geolocator/#location_settings)
  * [Methods](https://flet.dev/docs/controls/geolocator/#methods)
    * [`get_current_position(accuracy, location_settings)`](https://flet.dev/docs/controls/geolocator/#get_current_positionaccuracy-location_settings)
    * [`get_last_known_position()`](https://flet.dev/docs/controls/geolocator/#get_last_known_position)
    * [`get_permission_status()`](https://flet.dev/docs/controls/geolocator/#get_permission_status)
    * [`request_permission()`](https://flet.dev/docs/controls/geolocator/#request_permission)
    * [`is_location_service_enabled()`](https://flet.dev/docs/controls/geolocator/#is_location_service_enabled)
    * [`open_app_settings()`](https://flet.dev/docs/controls/geolocator/#open_app_settings)
    * [`open_location_settings()`](https://flet.dev/docs/controls/geolocator/#open_location_settings)
  * [Events](https://flet.dev/docs/controls/geolocator/#events)
    * [`on_error`](https://flet.dev/docs/controls/geolocator/#on_error)
    * [`on_position_change`](https://flet.dev/docs/controls/geolocator/#on_position_change)


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
