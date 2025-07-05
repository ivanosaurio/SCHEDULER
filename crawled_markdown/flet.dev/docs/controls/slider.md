[Skip to main content](https://flet.dev/docs/controls/slider/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/slider/)
  * [Controls](https://flet.dev/docs/controls)
    * [Layout](https://flet.dev/docs/controls/layout)
    * [Navigation](https://flet.dev/docs/controls/app-structure-navigation)
    * [Information Displays](https://flet.dev/docs/controls/information-displays)
    * [Buttons](https://flet.dev/docs/controls/buttons)
    * [Input and Selections](https://flet.dev/docs/controls/input-and-selections)
      * [AutoComplete](https://flet.dev/docs/controls/autocomplete)
      * [AutofillGroup](https://flet.dev/docs/controls/autofillgroup)
      * [Checkbox](https://flet.dev/docs/controls/checkbox)
      * [Chip](https://flet.dev/docs/controls/chip)
      * [CupertinoCheckbox](https://flet.dev/docs/controls/cupertinocheckbox)
      * [CupertinoRadio](https://flet.dev/docs/controls/cupertinoradio)
      * [CupertinoSlider](https://flet.dev/docs/controls/cupertinoslider)
      * [CupertinoSwitch](https://flet.dev/docs/controls/cupertinoswitch)
      * [CupertinoTextField](https://flet.dev/docs/controls/cupertinotextfield)
      * [Dropdown](https://flet.dev/docs/controls/dropdown)
      * [DropdownM2](https://flet.dev/docs/controls/dropdownm2)
      * [Radio](https://flet.dev/docs/controls/radio)
      * [RangeSlider](https://flet.dev/docs/controls/rangeslider)
      * [SearchBar](https://flet.dev/docs/controls/searchbar)
      * [Slider](https://flet.dev/docs/controls/slider)
      * [Switch](https://flet.dev/docs/controls/switch)
      * [TextField](https://flet.dev/docs/controls/textfield)
    * [Dialogs, Alerts and Panels](https://flet.dev/docs/controls/dialogs-alerts-panels)
    * [Charts](https://flet.dev/docs/controls/charts)
    * [Animations](https://flet.dev/docs/controls/animations)
    * [Utility](https://flet.dev/docs/controls/utility)
  * [Cookbook](https://flet.dev/docs/controls/slider/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Input and Selections](https://flet.dev/docs/controls/input-and-selections)
  * Slider


On this page
# Slider
A slider provides a visual indication of adjustable content, as well as the current setting in the total range of content.
Use a slider when you want people to set defined values (such as volume or brightness), or when people would benefit from instant feedback on the effect of setting changes.
## Examples[​](https://flet.dev/docs/controls/slider/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/input/slider)
### Basic sliders[​](https://flet.dev/docs/controls/slider/#basic-sliders "Direct link to Basic sliders")
python/controls/input-and-selections/slider/slider-basic.py
```
import flet as ftdefmain(page):  page.add(    ft.Text("Default slider:"),    ft.Slider(),    ft.Text("Default disabled slider:"),    ft.Slider(disabled=True),)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/input-and-selections/slider/slider-basic.py)
### Sliders with values[​](https://flet.dev/docs/controls/slider/#sliders-with-values "Direct link to Sliders with values")
python/controls/input-and-selections/slider/slider-values.py
```
import flet as ftdefmain(page):  page.add(    ft.Text("Slider with value:"),    ft.Slider(value=0.3),    ft.Text("Slider with a custom range and label:"),    ft.Slider(min=0,max=100, divisions=10, label="{value}%"),)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/input-and-selections/slider/slider-values.py)
![](https://flet.dev/img/docs/controls/slider/slider-with-custom-content.gif)
### Slider with `on_change` event[​](https://flet.dev/docs/controls/slider/#slider-with-on_change-event "Direct link to slider-with-on_change-event")
python/controls/input-and-selections/slider/slider-with-change.py
```
import flet as ftdefmain(page):defslider_changed(e):    t.value =f"Slider changed to {e.control.value}"    page.update()  t = ft.Text()  page.add(    ft.Text("Slider with 'on_change' event:"),    ft.Slider(min=0,max=100, divisions=10, label="{value}%", on_change=slider_changed),    t,)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/input-and-selections/slider/slider-with-change.py)
![](https://flet.dev/img/docs/controls/slider/slider-with-change-event.gif)
## Properties[​](https://flet.dev/docs/controls/slider/#properties "Direct link to Properties")
### `active_color`[​](https://flet.dev/docs/controls/slider/#active_color "Direct link to active_color")
The [color](https://flet.dev/docs/reference/colors) to use for the portion of the slider track that is active.
The "active" side of the slider is the side between the thumb and the minimum value.
### `adaptive`[​](https://flet.dev/docs/controls/slider/#adaptive "Direct link to adaptive")
If the value is `True`, an adaptive Slider is created based on whether the target platform is iOS or macOS.
On iOS and macOS, a [`CupertinoSlider`](https://flet.dev/docs/controls/cupertinoslider), which has matching functionality and presentation as `Slider`, and are the graphics expected on iOS. On other platforms, this creates a Material Slider.
Defaults to `False`.
### `autofocus`[​](https://flet.dev/docs/controls/slider/#autofocus "Direct link to autofocus")
True if the control will be selected as the initial focus. If there is more than one control on a page with autofocus set, then the first one added to the page will get focus.
### `divisions`[​](https://flet.dev/docs/controls/slider/#divisions "Direct link to divisions")
The number of discrete divisions.
Typically used with `label` to show the current discrete value.
If not set, the slider is continuous.
### `inactive_color`[​](https://flet.dev/docs/controls/slider/#inactive_color "Direct link to inactive_color")
The [color](https://flet.dev/docs/reference/colors) for the inactive portion of the slider track.
The "inactive" side of the slider is the side between the thumb and the maximum value.
### `interaction`[​](https://flet.dev/docs/controls/slider/#interaction "Direct link to interaction")
The allowed way for the user to interact with this slider. Value is a [`SliderInteraction`](https://flet.dev/docs/reference/types/sliderinteraction) and defaults to `SliderInteraction.TAP_AND_SLIDE`.
### `label`[​](https://flet.dev/docs/controls/slider/#label "Direct link to label")
Format with `{value}`.
A label to show above the slider when the slider is active. The value of `label` may contain `{value}` which will be replaced with a current slider value.
It is used to display the value of a discrete slider, and it is displayed as part of the value indicator shape.
If not set, then the value indicator will not be displayed.
### `max`[​](https://flet.dev/docs/controls/slider/#max "Direct link to max")
The maximum value the user can select. Must be greater than or equal to `min`.
If the `max` is equal to the `min`, then the slider is disabled.
Defaults to `1.0`.
### `min`[​](https://flet.dev/docs/controls/slider/#min "Direct link to min")
The minimum value the user can select. Must be less than or equal to `max`.
If the `max` is equal to the `min`, then the slider is disabled.
Defaults to `0.0`.
### `mouse_cursor`[​](https://flet.dev/docs/controls/slider/#mouse_cursor "Direct link to mouse_cursor")
The cursor to be displayed when a mouse pointer enters or is hovering over this control.
Value is of type [`MouseCursor`](https://flet.dev/docs/reference/types/mousecursor).
### `overlay_color`[​](https://flet.dev/docs/controls/slider/#overlay_color "Direct link to overlay_color")
The highlight [color](https://flet.dev/docs/reference/colors) that's typically used to indicate that the range slider thumb is in `ControlState.HOVERED` or `DRAGGED` [`ControlState`](https://flet.dev/docs/reference/types/controlstate)s.
### `round`[​](https://flet.dev/docs/controls/slider/#round "Direct link to round")
The number of decimals displayed on the `label` containing `value`.
Defaults to `0`, which displays value rounded to the nearest integer.
### `secondary_active_color`[​](https://flet.dev/docs/controls/slider/#secondary_active_color "Direct link to secondary_active_color")
The [color](https://flet.dev/docs/reference/colors) to use for the portion of the slider track between the thumb and the `secondary_track_value`.
### `secondary_track_value`[​](https://flet.dev/docs/controls/slider/#secondary_track_value "Direct link to secondary_track_value")
The secondary track value for this slider.
If not null, a secondary track using `secondary_active_color` is drawn between the thumb and this value, over the inactive track. If less than `value`, then the secondary track is not shown.
It can be ideal for media scenarios such as showing the buffering progress while the `value` shows the play progress.
### `thumb_color`[​](https://flet.dev/docs/controls/slider/#thumb_color "Direct link to thumb_color")
The [color](https://flet.dev/docs/reference/colors) of the thumb.
### `value`[​](https://flet.dev/docs/controls/slider/#value "Direct link to value")
The currently selected value for this slider.
The slider's thumb is drawn at a position that corresponds to this value.
Defaults to value of `min` property.
## Events[​](https://flet.dev/docs/controls/slider/#events "Direct link to Events")
### `on_blur`[​](https://flet.dev/docs/controls/slider/#on_blur "Direct link to on_blur")
Fires when the control has lost focus.
### `on_change`[​](https://flet.dev/docs/controls/slider/#on_change "Direct link to on_change")
Fires when the state of the Slider is changed.
### `on_change_end`[​](https://flet.dev/docs/controls/slider/#on_change_end "Direct link to on_change_end")
Fires when the user is done selecting a new value for the slider.
### `on_change_start`[​](https://flet.dev/docs/controls/slider/#on_change_start "Direct link to on_change_start")
Fires when the user starts selecting a new value for the slider.
### `on_focus`[​](https://flet.dev/docs/controls/slider/#on_focus "Direct link to on_focus")
Fires when the control has received focus.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/slider.md)
[PreviousSearchBar](https://flet.dev/docs/controls/searchbar)[NextSwitch](https://flet.dev/docs/controls/switch)
  * [Examples](https://flet.dev/docs/controls/slider/#examples)
    * [Basic sliders](https://flet.dev/docs/controls/slider/#basic-sliders)
    * [Sliders with values](https://flet.dev/docs/controls/slider/#sliders-with-values)
    * [Slider with `on_change` event](https://flet.dev/docs/controls/slider/#slider-with-on_change-event)
  * [Properties](https://flet.dev/docs/controls/slider/#properties)
    * [`active_color`](https://flet.dev/docs/controls/slider/#active_color)
    * [`adaptive`](https://flet.dev/docs/controls/slider/#adaptive)
    * [`autofocus`](https://flet.dev/docs/controls/slider/#autofocus)
    * [`divisions`](https://flet.dev/docs/controls/slider/#divisions)
    * [`inactive_color`](https://flet.dev/docs/controls/slider/#inactive_color)
    * [`interaction`](https://flet.dev/docs/controls/slider/#interaction)
    * [`label`](https://flet.dev/docs/controls/slider/#label)
    * [`max`](https://flet.dev/docs/controls/slider/#max)
    * [`min`](https://flet.dev/docs/controls/slider/#min)
    * [`mouse_cursor`](https://flet.dev/docs/controls/slider/#mouse_cursor)
    * [`overlay_color`](https://flet.dev/docs/controls/slider/#overlay_color)
    * [`round`](https://flet.dev/docs/controls/slider/#round)
    * [`secondary_active_color`](https://flet.dev/docs/controls/slider/#secondary_active_color)
    * [`secondary_track_value`](https://flet.dev/docs/controls/slider/#secondary_track_value)
    * [`thumb_color`](https://flet.dev/docs/controls/slider/#thumb_color)
    * [`value`](https://flet.dev/docs/controls/slider/#value)
  * [Events](https://flet.dev/docs/controls/slider/#events)
    * [`on_blur`](https://flet.dev/docs/controls/slider/#on_blur)
    * [`on_change`](https://flet.dev/docs/controls/slider/#on_change)
    * [`on_change_end`](https://flet.dev/docs/controls/slider/#on_change_end)
    * [`on_change_start`](https://flet.dev/docs/controls/slider/#on_change_start)
    * [`on_focus`](https://flet.dev/docs/controls/slider/#on_focus)


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
