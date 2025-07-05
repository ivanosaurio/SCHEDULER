[Skip to main content](https://flet.dev/docs/controls/map/#__docusaurus_skipToContent_fallback)
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
    * [Layout](https://flet.dev/docs/controls/layout)
    * [Navigation](https://flet.dev/docs/controls/app-structure-navigation)
    * [Information Displays](https://flet.dev/docs/controls/information-displays)
      * [Ads](https://flet.dev/docs/controls/ads)
      * [Canvas](https://flet.dev/docs/controls/canvas)
      * [CircleAvatar](https://flet.dev/docs/controls/circleavatar)
      * [CupertinoActivityIndicator](https://flet.dev/docs/controls/cupertinoactivityindicator)
      * [Icon](https://flet.dev/docs/controls/icon)
      * [Image](https://flet.dev/docs/controls/image)
      * [Map](https://flet.dev/docs/controls/map)
        * [CircleLayer](https://flet.dev/docs/controls/mapcirclelayer)
        * [MarkerLayer](https://flet.dev/docs/controls/mapmarkerlayer)
        * [PolygonLayer](https://flet.dev/docs/controls/mappolygonlayer)
        * [PolylineLayer](https://flet.dev/docs/controls/mappolylinelayer)
        * [RichAttribution](https://flet.dev/docs/controls/maprichattribution)
        * [SimpleAttribution](https://flet.dev/docs/controls/mapsimpleattribution)
        * [TileLayer](https://flet.dev/docs/controls/maptilelayer)
        * [TextSourceAttribution](https://flet.dev/docs/controls/maptextsourceattribution)
      * [Markdown](https://flet.dev/docs/controls/markdown)
      * [Text](https://flet.dev/docs/controls/text)
      * [ProgressBar](https://flet.dev/docs/controls/progressbar)
      * [ProgressRing](https://flet.dev/docs/controls/progressring)
      * [WebView](https://flet.dev/docs/controls/webview)
    * [Buttons](https://flet.dev/docs/controls/buttons)
    * [Input and Selections](https://flet.dev/docs/controls/input-and-selections)
    * [Dialogs, Alerts and Panels](https://flet.dev/docs/controls/dialogs-alerts-panels)
    * [Charts](https://flet.dev/docs/controls/charts)
    * [Animations](https://flet.dev/docs/controls/animations)
    * [Utility](https://flet.dev/docs/controls/utility)
  * [Cookbook](https://flet.dev/docs/cookbook/theming)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Information Displays](https://flet.dev/docs/controls/information-displays)
  * Map


On this page
# Map
Used to display a map with various layers.
Packaging
To build your Flet app that uses `Map` control add `flet-map` to `dependencies` key of the `[project]` section of your `pyproject.toml` file, for example:
```
[project]...dependencies = [ "flet==0.27.6", "flet-map==0.1.0",]
```

## Examples[​](https://flet.dev/docs/controls/map/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/displays/map)
### Example[​](https://flet.dev/docs/controls/map/#example "Direct link to Example")
python/controls/information-displays/map/map-layers-example.py
```
loading...
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/information-displays/map/map-layers-example.py)
![](https://flet.dev/img/docs/controls/map/map-example.png)
## Properties[​](https://flet.dev/docs/controls/map/#properties "Direct link to Properties")
### `bgcolor`[​](https://flet.dev/docs/controls/map/#bgcolor "Direct link to bgcolor")
The background color.
### `initial_center`[​](https://flet.dev/docs/controls/map/#initial_center "Direct link to initial_center")
The initial center of the map.
Value is of type [`MapLatitudeLongitude`](https://flet.dev/docs/reference/types/maplatitudelongitude).
### `initial_rotation`[​](https://flet.dev/docs/controls/map/#initial_rotation "Direct link to initial_rotation")
The initial rotation value.
### `initial_zoom`[​](https://flet.dev/docs/controls/map/#initial_zoom "Direct link to initial_zoom")
The initial zoom level.
### `interaction_configuration`[​](https://flet.dev/docs/controls/map/#interaction_configuration "Direct link to interaction_configuration")
The interaction configuration.
Value is of type [`MapInteractionConfiguration`](https://flet.dev/docs/reference/types/mapinteractionconfiguration).
### `keep_alive`[​](https://flet.dev/docs/controls/map/#keep_alive "Direct link to keep_alive")
A boolean value to keep the map alive.
### `max_zoom`[​](https://flet.dev/docs/controls/map/#max_zoom "Direct link to max_zoom")
The maximum zoom level.
### `min_zoom`[​](https://flet.dev/docs/controls/map/#min_zoom "Direct link to min_zoom")
The minimum zoom level.
### `layers`[​](https://flet.dev/docs/controls/map/#layers "Direct link to layers")
A list of layers to be displayed on the map.
Value is of type [`MapLayer`](https://flet.dev/docs/reference/types/maplayer).
## Events[​](https://flet.dev/docs/controls/map/#events "Direct link to Events")
### `on_event`[​](https://flet.dev/docs/controls/map/#on_event "Direct link to on_event")
Fires when any map events occurs.
Event handler argument is of type [`MapEvent`](https://flet.dev/docs/reference/types/mapevent).
### `on_hover`[​](https://flet.dev/docs/controls/map/#on_hover "Direct link to on_hover")
Fires when a hover event occurs.
Event handler argument is of type [`MapHoverEvent`](https://flet.dev/docs/reference/types/maphoverevent).
### `on_init`[​](https://flet.dev/docs/controls/map/#on_init "Direct link to on_init")
Fires when the map is initialized.
### `on_long_press`[​](https://flet.dev/docs/controls/map/#on_long_press "Direct link to on_long_press")
Fires when a long press event occurs.
Event handler argument is of type [`MapTapEvent`](https://flet.dev/docs/reference/types/maptapevent).
### `on_position_change`[​](https://flet.dev/docs/controls/map/#on_position_change "Direct link to on_position_change")
Fires when the map position changes.
Event handler argument is of type [`MapPositionChangeEvent`](https://flet.dev/docs/reference/types/mappositionchangeevent).
### `on_pointer_down`[​](https://flet.dev/docs/controls/map/#on_pointer_down "Direct link to on_pointer_down")
Fires when a pointer down event occurs.
Event handler argument is of type [`MapPointerEvent`](https://flet.dev/docs/reference/types/mappointerevent).
### `on_pointer_cancel`[​](https://flet.dev/docs/controls/map/#on_pointer_cancel "Direct link to on_pointer_cancel")
Fires when a pointer cancel event occurs.
Event handler argument is of type [`MapPointerEvent`](https://flet.dev/docs/reference/types/mappointerevent).
### `on_pointer_up`[​](https://flet.dev/docs/controls/map/#on_pointer_up "Direct link to on_pointer_up")
Fires when a pointer up event occurs.
Event handler argument is of type [`MapPointerEvent`](https://flet.dev/docs/reference/types/mappointerevent).
### `on_secondary_tap`[​](https://flet.dev/docs/controls/map/#on_secondary_tap "Direct link to on_secondary_tap")
Fires when a secondary tap event occurs.
Event handler argument is of type [`MapTapEvent`](https://flet.dev/docs/reference/types/maptapevent).
### `on_tap`[​](https://flet.dev/docs/controls/map/#on_tap "Direct link to on_tap")
Fires when a tap event occurs.
Event handler argument is of type [`MapTapEvent`](https://flet.dev/docs/reference/types/maptapevent).
## Methods[​](https://flet.dev/docs/controls/map/#methods "Direct link to Methods")
### `rotate_from`[​](https://flet.dev/docs/controls/map/#rotate_from "Direct link to rotate_from")
Apply a rotation of `degree` to the current rotation.
It has the following arguments:
  * `animation_curve`: The curve of the zoom animation. Value is of type [`AnimationCurve`](https://flet.dev/docs/reference/types/animationcurve) and defaults to `Map.animation_curve`.
  * `degree`: The degree to rotate.


### `reset_rotation`[​](https://flet.dev/docs/controls/map/#reset_rotation "Direct link to reset_rotation")
Reset the rotation to 0 degrees.
It has the following arguments:
  * `animation_curve`: The curve of the zoom animation. Value is of type [`AnimationCurve`](https://flet.dev/docs/reference/types/animationcurve) and defaults to `Map.animation_curve`.
  * `animation_duration`: The duration of the zoom animation. Value is of type [`DurationValue`](https://flet.dev/docs/reference/types/aliases#durationvalue) and defaults to `Map.animation_duration`.


### `zoom_in`[​](https://flet.dev/docs/controls/map/#zoom_in "Direct link to zoom_in")
Add one level to the current zoom level.
It has the following arguments:
  * `animation_curve`: The curve of the zoom animation. Value is of type [`AnimationCurve`](https://flet.dev/docs/reference/types/animationcurve) and defaults to `Map.animation_curve`.
  * `animation_duration`: The duration of the zoom animation. Value is of type [`DurationValue`](https://flet.dev/docs/reference/types/aliases#durationvalue) and defaults to `Map.animation_duration`.


### `zoom_out`[​](https://flet.dev/docs/controls/map/#zoom_out "Direct link to zoom_out")
Subtract one level from the current zoom level.
It has the following arguments:
  * `animation_curve`: The curve of the zoom animation. Value is of type [`AnimationCurve`](https://flet.dev/docs/reference/types/animationcurve) and defaults to `Map.animation_curve`.
  * `animation_duration`: The duration of the zoom animation. Value is of type [`DurationValue`](https://flet.dev/docs/reference/types/aliases#durationvalue) and defaults to `Map.animation_duration`.


### `zoom_to`[​](https://flet.dev/docs/controls/map/#zoom_to "Direct link to zoom_to")
Zoom to a specific level.
It has the following arguments:
  * `animation_curve`: The curve of the zoom animation. Value is of type [`AnimationCurve`](https://flet.dev/docs/reference/types/animationcurve) and defaults to `Map.animation_curve`.
  * `animation_duration`: The duration of the zoom animation. Value is of type [`DurationValue`](https://flet.dev/docs/reference/types/aliases#durationvalue) and defaults to `Map.animation_duration`.
  * `zoom`: The zoom level to zoom to.


### `move_to`[​](https://flet.dev/docs/controls/map/#move_to "Direct link to move_to")
Move to a specific location.
It has the following arguments:
  * `animation_curve`: The curve of the move animation. Value is of type [`AnimationCurve`](https://flet.dev/docs/reference/types/animationcurve) and defaults to `Map.animation_curve`.
  * `animation_duration`: The duration of the move animation. Value is of type [`DurationValue`](https://flet.dev/docs/reference/types/aliases#durationvalue) and defaults to `Map.animation_duration`.
  * `destination`: The destination point to move to. Value is of type [`MapLatitudeLongitude`](https://flet.dev/docs/reference/types/maplatitudelongitude).
  * `zoom`: The zoom level to move to.
  * `offset`: The offset to move to. Value is of type [`OffsetValue`](https://flet.dev/docs/reference/types/aliases#offsetvalue).
  * `rotation`: The rotation to move to.


### `center_on`[​](https://flet.dev/docs/controls/map/#center_on "Direct link to center_on")
Center the map on a specific location.
It has the following arguments:
  * `animation_curve`: The curve of the move animation. Value is of type [`AnimationCurve`](https://flet.dev/docs/reference/types/animationcurve) and defaults to `Map.animation_curve`.
  * `animation_duration`: The duration of the move animation. Value is of type [`DurationValue`](https://flet.dev/docs/reference/types/aliases#durationvalue) and defaults to `Map.animation_duration`.
  * `point`: The point to center on. Value is of type [`MapLatitudeLongitude`](https://flet.dev/docs/reference/types/maplatitudelongitude).
  * `zoom`: The zoom level to move to.


[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/map.md)
[PreviousImage](https://flet.dev/docs/controls/image)[NextCircleLayer](https://flet.dev/docs/controls/mapcirclelayer)
  * [Examples](https://flet.dev/docs/controls/map/#examples)
    * [Example](https://flet.dev/docs/controls/map/#example)
  * [Properties](https://flet.dev/docs/controls/map/#properties)
    * [`bgcolor`](https://flet.dev/docs/controls/map/#bgcolor)
    * [`initial_center`](https://flet.dev/docs/controls/map/#initial_center)
    * [`initial_rotation`](https://flet.dev/docs/controls/map/#initial_rotation)
    * [`initial_zoom`](https://flet.dev/docs/controls/map/#initial_zoom)
    * [`interaction_configuration`](https://flet.dev/docs/controls/map/#interaction_configuration)
    * [`keep_alive`](https://flet.dev/docs/controls/map/#keep_alive)
    * [`max_zoom`](https://flet.dev/docs/controls/map/#max_zoom)
    * [`min_zoom`](https://flet.dev/docs/controls/map/#min_zoom)
    * [`layers`](https://flet.dev/docs/controls/map/#layers)
  * [Events](https://flet.dev/docs/controls/map/#events)
    * [`on_event`](https://flet.dev/docs/controls/map/#on_event)
    * [`on_hover`](https://flet.dev/docs/controls/map/#on_hover)
    * [`on_init`](https://flet.dev/docs/controls/map/#on_init)
    * [`on_long_press`](https://flet.dev/docs/controls/map/#on_long_press)
    * [`on_position_change`](https://flet.dev/docs/controls/map/#on_position_change)
    * [`on_pointer_down`](https://flet.dev/docs/controls/map/#on_pointer_down)
    * [`on_pointer_cancel`](https://flet.dev/docs/controls/map/#on_pointer_cancel)
    * [`on_pointer_up`](https://flet.dev/docs/controls/map/#on_pointer_up)
    * [`on_secondary_tap`](https://flet.dev/docs/controls/map/#on_secondary_tap)
    * [`on_tap`](https://flet.dev/docs/controls/map/#on_tap)
  * [Methods](https://flet.dev/docs/controls/map/#methods)
    * [`rotate_from`](https://flet.dev/docs/controls/map/#rotate_from)
    * [`reset_rotation`](https://flet.dev/docs/controls/map/#reset_rotation)
    * [`zoom_in`](https://flet.dev/docs/controls/map/#zoom_in)
    * [`zoom_out`](https://flet.dev/docs/controls/map/#zoom_out)
    * [`zoom_to`](https://flet.dev/docs/controls/map/#zoom_to)
    * [`move_to`](https://flet.dev/docs/controls/map/#move_to)
    * [`center_on`](https://flet.dev/docs/controls/map/#center_on)


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
