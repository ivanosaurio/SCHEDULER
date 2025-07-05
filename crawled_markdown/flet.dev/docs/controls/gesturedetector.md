[Skip to main content](https://flet.dev/docs/controls/gesturedetector/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/gesturedetector/)
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
  * [Cookbook](https://flet.dev/docs/controls/gesturedetector/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Utility](https://flet.dev/docs/controls/utility)
  * GestureDetector


On this page
# GestureDetector
A control that detects gestures.
Attempts to recognize gestures that correspond to its non-null callbacks.
If this control has a `content`, it defers to that child control for its sizing behavior. If it does not have a `content`, it grows to fit the parent instead.
## Examples[​](https://flet.dev/docs/controls/gesturedetector/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/utility/gesturedetector)
[Solitare game tutorial](https://flet.dev/docs/tutorials/python-solitaire)
### Draggable containers[​](https://flet.dev/docs/controls/gesturedetector/#draggable-containers "Direct link to Draggable containers")
The following example demonstrates how a control can be freely dragged inside a Stack.
The sample also shows that GestureDetector can have a child control (blue container) as well as be nested inside another control (yellow container) giving the same results.
![](https://flet.dev/img/docs/controls/gesture-detector/gesture-detector-two-containers.gif)
python/controls/utility/gesture-detector/draggable-containers.py
```
import flet as ftdefmain(page: ft.Page):defon_pan_update1(e: ft.DragUpdateEvent):    c.top =max(0, c.top + e.delta_y)    c.left =max(0, c.left + e.delta_x)    c.update()defon_pan_update2(e: ft.DragUpdateEvent):    e.control.top =max(0, e.control.top + e.delta_y)    e.control.left =max(0, e.control.left + e.delta_x)    e.control.update()  gd = ft.GestureDetector(    mouse_cursor=ft.MouseCursor.MOVE,    drag_interval=50,    on_pan_update=on_pan_update1,)  c = ft.Container(gd, bgcolor=ft.Colors.AMBER, width=50, height=50, left=0, top=0)  gd1 = ft.GestureDetector(    mouse_cursor=ft.MouseCursor.MOVE,    drag_interval=10,    on_vertical_drag_update=on_pan_update2,    left=100,    top=100,    content=ft.Container(bgcolor=ft.Colors.BLUE, width=50, height=50),)  page.add(ft.Stack([c, gd1], width=1000, height=500))ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/utility/gesture-detector/draggable-containers.py)
## Properties[​](https://flet.dev/docs/controls/gesturedetector/#properties "Direct link to Properties")
### `content`[​](https://flet.dev/docs/controls/gesturedetector/#content "Direct link to content")
A child Control contained by the gesture detector.
### `mouse_cursor`[​](https://flet.dev/docs/controls/gesturedetector/#mouse_cursor "Direct link to mouse_cursor")
The mouse cursor for mouse pointers that are hovering over the control.
Value is of type [`MouseCursor`](https://flet.dev/docs/reference/types/mousecursor).
### `drag_interval`[​](https://flet.dev/docs/controls/gesturedetector/#drag_interval "Direct link to drag_interval")
Throttling in milliseconds for horizontal drag, vertical drag and pan update events. When a user moves a pointer a lot of events are being generated to do precise tracking. `drag_interval` allows sending drag update events to a Flet program every X milliseconds, thus preserving the bandwidth (web and mobile apps). Default is `0` - no throttling, all events are sent to a Flet program, very smooth tracking.
### `hover_interval`[​](https://flet.dev/docs/controls/gesturedetector/#hover_interval "Direct link to hover_interval")
Throttling in milliseconds for `on_hover` event.
## Events[​](https://flet.dev/docs/controls/gesturedetector/#events "Direct link to Events")
### `multi_tap_touches`[​](https://flet.dev/docs/controls/gesturedetector/#multi_tap_touches "Direct link to multi_tap_touches")
The minimum number of pointers to trigger `on_multi_tap` event.
### `on_double_tap`[​](https://flet.dev/docs/controls/gesturedetector/#on_double_tap "Direct link to on_double_tap")
The user has tapped the screen with a primary button at the same location twice in quick succession.
### `on_double_tap_down`[​](https://flet.dev/docs/controls/gesturedetector/#on_double_tap_down "Direct link to on_double_tap_down")
A pointer that might cause a double tap has contacted the screen at a particular location.
Triggered immediately after the down event of the second tap.
Event handler argument is of type [`MapTapEvent`](https://flet.dev/docs/reference/types/tapevent).
### `on_enter`[​](https://flet.dev/docs/controls/gesturedetector/#on_enter "Direct link to on_enter")
Triggered when a mouse pointer has entered this control.
Event handler argument is of type [`HoverEvent`](https://flet.dev/docs/reference/types/hoverevent).
### `on_exit`[​](https://flet.dev/docs/controls/gesturedetector/#on_exit "Direct link to on_exit")
Triggered when a mouse pointer has exited this control.
Event handler argument is of type [`HoverEvent`](https://flet.dev/docs/reference/types/hoverevent).
### `on_horizontal_drag_end`[​](https://flet.dev/docs/controls/gesturedetector/#on_horizontal_drag_end "Direct link to on_horizontal_drag_end")
A pointer that was previously in contact with the screen with a primary button and moving horizontally is no longer in contact with the screen and was moving at a specific velocity when it stopped contacting the screen.
Event handler argument is of type [`DragEndEvent`](https://flet.dev/docs/reference/types/dragendevent).
### `on_horizontal_drag_start`[​](https://flet.dev/docs/controls/gesturedetector/#on_horizontal_drag_start "Direct link to on_horizontal_drag_start")
A pointer has contacted the screen with a primary button and has begun to move horizontally.
Event handler argument is of type [`DragStartEvent`](https://flet.dev/docs/reference/types/dragstartevent).
### `on_horizontal_drag_update`[​](https://flet.dev/docs/controls/gesturedetector/#on_horizontal_drag_update "Direct link to on_horizontal_drag_update")
A pointer that is in contact with the screen with a primary button and moving horizontally has moved in the horizontal direction.
Event handler argument is of type [`DragUpdateEvent`](https://flet.dev/docs/reference/types/dragupdateevent).
### `on_hover`[​](https://flet.dev/docs/controls/gesturedetector/#on_hover "Direct link to on_hover")
Triggered when a mouse pointer has entered this control.
Event handler argument is of type [`HoverEvent`](https://flet.dev/docs/reference/types/hoverevent).
### `on_long_press_end`[​](https://flet.dev/docs/controls/gesturedetector/#on_long_press_end "Direct link to on_long_press_end")
A pointer that has triggered a long-press with a primary button has stopped contacting the screen.
Event handler argument is of type [`LongPressEndEvent`](https://flet.dev/docs/reference/types/longpressendevent).
### `on_long_press_start`[​](https://flet.dev/docs/controls/gesturedetector/#on_long_press_start "Direct link to on_long_press_start")
Called when a long press gesture with a primary button has been recognized.
Triggered when a pointer has remained in contact with the screen at the same location for a long period of time.
Event handler argument is of type [`LongPressStartEvent`](https://flet.dev/docs/reference/types/longpressstartevent).
### `on_pan_end`[​](https://flet.dev/docs/controls/gesturedetector/#on_pan_end "Direct link to on_pan_end")
A pointer that was previously in contact with the screen with a primary button and moving is no longer in contact with the screen and was moving at a specific velocity when it stopped contacting the screen.
Event handler argument is of type [`DragEndEvent`](https://flet.dev/docs/reference/types/dragendevent).
### `on_pan_start`[​](https://flet.dev/docs/controls/gesturedetector/#on_pan_start "Direct link to on_pan_start")
A pointer has contacted the screen with a primary button and has begun to move.
Event handler argument is of type [`DragStartEvent`](https://flet.dev/docs/reference/types/dragstartevent).
### `on_pan_update`[​](https://flet.dev/docs/controls/gesturedetector/#on_pan_update "Direct link to on_pan_update")
A pointer that is in contact with the screen with a primary button and moving has moved again.
Event handler argument is of type [`DragUpdateEvent`](https://flet.dev/docs/reference/types/dragupdateevent).
### `on_scale_end`[​](https://flet.dev/docs/controls/gesturedetector/#on_scale_end "Direct link to on_scale_end")
Event handler argument is of type [`ScaleEndEvent`](https://flet.dev/docs/reference/types/scaleendevent).
### `on_scale_start`[​](https://flet.dev/docs/controls/gesturedetector/#on_scale_start "Direct link to on_scale_start")
The pointers in contact with the screen have established a focal point and initial scale of `1.0`.
Event handler argument is of type [`ScaleStartEvent`](https://flet.dev/docs/reference/types/scalestartevent).
### `on_scale_update`[​](https://flet.dev/docs/controls/gesturedetector/#on_scale_update "Direct link to on_scale_update")
Event handler argument is of type [`ScaleUpdateEvent`](https://flet.dev/docs/reference/types/scaleupdateevent).
### `on_secondary_long_press_end`[​](https://flet.dev/docs/controls/gesturedetector/#on_secondary_long_press_end "Direct link to on_secondary_long_press_end")
A pointer that has triggered a long-press with a secondary button has stopped contacting the screen.
Event handler argument is of type [`LongPressEndEvent`](https://flet.dev/docs/reference/types/longpressendevent).
### `on_secondary_long_press_start`[​](https://flet.dev/docs/controls/gesturedetector/#on_secondary_long_press_start "Direct link to on_secondary_long_press_start")
Called when a long press gesture with a secondary button has been recognized.
Triggered when a pointer has remained in contact with the screen at the same location for a long period of time.
Event handler argument is of type [`LongPressStartEvent`](https://flet.dev/docs/reference/types/longpressstartevent).
### `on_secondary_tap`[​](https://flet.dev/docs/controls/gesturedetector/#on_secondary_tap "Direct link to on_secondary_tap")
A tap with a secondary button has occurred.
### `on_secondary_tap_down`[​](https://flet.dev/docs/controls/gesturedetector/#on_secondary_tap_down "Direct link to on_secondary_tap_down")
A pointer that might cause a tap with a secondary button has contacted the screen at a particular location.
Event handler argument is of type [`MapTapEvent`](https://flet.dev/docs/reference/types/tapevent).
### `on_secondary_tap_up`[​](https://flet.dev/docs/controls/gesturedetector/#on_secondary_tap_up "Direct link to on_secondary_tap_up")
A pointer that will trigger a tap with a secondary button has stopped contacting the screen at a particular location.
Event handler argument is of type [`MapTapEvent`](https://flet.dev/docs/reference/types/tapevent).
### `on_tap`[​](https://flet.dev/docs/controls/gesturedetector/#on_tap "Direct link to on_tap")
A tap with a primary button has occurred.
### `on_tap_down`[​](https://flet.dev/docs/controls/gesturedetector/#on_tap_down "Direct link to on_tap_down")
A pointer that might cause a tap with a primary button has contacted the screen at a particular location.
Event handler argument is of type [`MapTapEvent`](https://flet.dev/docs/reference/types/tapevent).
### `on_tap_up`[​](https://flet.dev/docs/controls/gesturedetector/#on_tap_up "Direct link to on_tap_up")
A pointer that will trigger a tap with a primary button has stopped contacting the screen at a particular location.
Event handler argument is of type [`MapTapEvent`](https://flet.dev/docs/reference/types/tapevent).
### `on_vertical_drag_end`[​](https://flet.dev/docs/controls/gesturedetector/#on_vertical_drag_end "Direct link to on_vertical_drag_end")
A pointer that was previously in contact with the screen with a primary button and moving vertically is no longer in contact with the screen and was moving at a specific velocity when it stopped contacting the screen.
Event handler argument is of type [`DragEndEvent`](https://flet.dev/docs/reference/types/dragendevent).
### `on_vertical_drag_start`[​](https://flet.dev/docs/controls/gesturedetector/#on_vertical_drag_start "Direct link to on_vertical_drag_start")
A pointer has contacted the screen with a primary button and has begun to move vertically.
Event handler argument is of type [`DragStartEvent`](https://flet.dev/docs/reference/types/dragstartevent).
### `on_vertical_drag_update`[​](https://flet.dev/docs/controls/gesturedetector/#on_vertical_drag_update "Direct link to on_vertical_drag_update")
A pointer that is in contact with the screen with a primary button and moving vertically has moved in the vertical direction.
Event handler argument is of type [`DragUpdateEvent`](https://flet.dev/docs/reference/types/dragupdateevent).
### `on_multi_long_press`[​](https://flet.dev/docs/controls/gesturedetector/#on_multi_long_press "Direct link to on_multi_long_press")
Called when a long press gesture with multiple pointers has been recognized.
### `on_multi_tap`[​](https://flet.dev/docs/controls/gesturedetector/#on_multi_tap "Direct link to on_multi_tap")
Triggered when multiple pointers contacted the screen.
Event handler argument is of type [`MultiTapEvent`](https://flet.dev/docs/reference/types/multitapevent).
### `on_scroll`[​](https://flet.dev/docs/controls/gesturedetector/#on_scroll "Direct link to on_scroll")
Event handler argument is of type [`ScrollEvent`](https://flet.dev/docs/reference/types/scrollevent).
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/gesturedetector.md)
[PreviousGeolocator](https://flet.dev/docs/controls/geolocator)[NextHapticFeedback](https://flet.dev/docs/controls/hapticfeedback)
  * [Examples](https://flet.dev/docs/controls/gesturedetector/#examples)
    * [Draggable containers](https://flet.dev/docs/controls/gesturedetector/#draggable-containers)
  * [Properties](https://flet.dev/docs/controls/gesturedetector/#properties)
    * [`content`](https://flet.dev/docs/controls/gesturedetector/#content)
    * [`mouse_cursor`](https://flet.dev/docs/controls/gesturedetector/#mouse_cursor)
    * [`drag_interval`](https://flet.dev/docs/controls/gesturedetector/#drag_interval)
    * [`hover_interval`](https://flet.dev/docs/controls/gesturedetector/#hover_interval)
  * [Events](https://flet.dev/docs/controls/gesturedetector/#events)
    * [`multi_tap_touches`](https://flet.dev/docs/controls/gesturedetector/#multi_tap_touches)
    * [`on_double_tap`](https://flet.dev/docs/controls/gesturedetector/#on_double_tap)
    * [`on_double_tap_down`](https://flet.dev/docs/controls/gesturedetector/#on_double_tap_down)
    * [`on_enter`](https://flet.dev/docs/controls/gesturedetector/#on_enter)
    * [`on_exit`](https://flet.dev/docs/controls/gesturedetector/#on_exit)
    * [`on_horizontal_drag_end`](https://flet.dev/docs/controls/gesturedetector/#on_horizontal_drag_end)
    * [`on_horizontal_drag_start`](https://flet.dev/docs/controls/gesturedetector/#on_horizontal_drag_start)
    * [`on_horizontal_drag_update`](https://flet.dev/docs/controls/gesturedetector/#on_horizontal_drag_update)
    * [`on_hover`](https://flet.dev/docs/controls/gesturedetector/#on_hover)
    * [`on_long_press_end`](https://flet.dev/docs/controls/gesturedetector/#on_long_press_end)
    * [`on_long_press_start`](https://flet.dev/docs/controls/gesturedetector/#on_long_press_start)
    * [`on_pan_end`](https://flet.dev/docs/controls/gesturedetector/#on_pan_end)
    * [`on_pan_start`](https://flet.dev/docs/controls/gesturedetector/#on_pan_start)
    * [`on_pan_update`](https://flet.dev/docs/controls/gesturedetector/#on_pan_update)
    * [`on_scale_end`](https://flet.dev/docs/controls/gesturedetector/#on_scale_end)
    * [`on_scale_start`](https://flet.dev/docs/controls/gesturedetector/#on_scale_start)
    * [`on_scale_update`](https://flet.dev/docs/controls/gesturedetector/#on_scale_update)
    * [`on_secondary_long_press_end`](https://flet.dev/docs/controls/gesturedetector/#on_secondary_long_press_end)
    * [`on_secondary_long_press_start`](https://flet.dev/docs/controls/gesturedetector/#on_secondary_long_press_start)
    * [`on_secondary_tap`](https://flet.dev/docs/controls/gesturedetector/#on_secondary_tap)
    * [`on_secondary_tap_down`](https://flet.dev/docs/controls/gesturedetector/#on_secondary_tap_down)
    * [`on_secondary_tap_up`](https://flet.dev/docs/controls/gesturedetector/#on_secondary_tap_up)
    * [`on_tap`](https://flet.dev/docs/controls/gesturedetector/#on_tap)
    * [`on_tap_down`](https://flet.dev/docs/controls/gesturedetector/#on_tap_down)
    * [`on_tap_up`](https://flet.dev/docs/controls/gesturedetector/#on_tap_up)
    * [`on_vertical_drag_end`](https://flet.dev/docs/controls/gesturedetector/#on_vertical_drag_end)
    * [`on_vertical_drag_start`](https://flet.dev/docs/controls/gesturedetector/#on_vertical_drag_start)
    * [`on_vertical_drag_update`](https://flet.dev/docs/controls/gesturedetector/#on_vertical_drag_update)
    * [`on_multi_long_press`](https://flet.dev/docs/controls/gesturedetector/#on_multi_long_press)
    * [`on_multi_tap`](https://flet.dev/docs/controls/gesturedetector/#on_multi_tap)
    * [`on_scroll`](https://flet.dev/docs/controls/gesturedetector/#on_scroll)


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
