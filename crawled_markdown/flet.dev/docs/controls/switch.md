[Skip to main content](https://flet.dev/docs/controls/switch/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/switch/)
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
  * [Cookbook](https://flet.dev/docs/controls/switch/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Input and Selections](https://flet.dev/docs/controls/input-and-selections)
  * Switch


On this page
# Switch
A toggle represents a physical switch that allows someone to choose between two mutually exclusive options.
For example, "On/Off", "Show/Hide". Choosing an option should produce an immediate result.
## Examples[​](https://flet.dev/docs/controls/switch/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/input/switch)
### Basic switches[​](https://flet.dev/docs/controls/switch/#basic-switches "Direct link to Basic switches")
python/controls/input-and-selections/switch/switch-basic.py
```
import flet as ftdefmain(page):defbutton_clicked(e):    t.value =f"Switch values are: {c1.value}, {c2.value}, {c3.value}, {c4.value}."    page.update()  t = ft.Text()  c1 = ft.Switch(label="Unchecked switch", value=False)  c2 = ft.Switch(label="Checked switch", value=True)  c3 = ft.Switch(label="Disabled switch", disabled=True)  c4 = ft.Switch(    label="Switch with rendered label_position='left'",    label_position=ft.LabelPosition.LEFT,)  b = ft.ElevatedButton(text="Submit", on_click=button_clicked)  page.add(c1, c2, c3, c4, b, t)ft.app(target=main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/input-and-selections/switch/switch-basic.py)
![](https://flet.dev/img/docs/controls/switch/basic-switch.gif)
### Switch with `on_change` event[​](https://flet.dev/docs/controls/switch/#switch-with-on_change-event "Direct link to switch-with-on_change-event")
python/controls/input-and-selections/switch/switch-with-event.py
```
import flet as ftdefmain(page: ft.Page):deftheme_changed(e):    page.theme_mode =(      ft.ThemeMode.DARKif page.theme_mode == ft.ThemeMode.LIGHTelse ft.ThemeMode.LIGHT)    c.label =("Light theme"if page.theme_mode == ft.ThemeMode.LIGHT else"Dark theme")    page.update()  page.theme_mode = ft.ThemeMode.LIGHT  c = ft.Switch(label="Light theme", on_change=theme_changed)  page.add(c)ft.app(target=main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/input-and-selections/switch/switch-with-event.py)
![](https://flet.dev/img/docs/controls/switch/switch-with-change-event.gif)
## Properties[​](https://flet.dev/docs/controls/switch/#properties "Direct link to Properties")
### `active_color`[​](https://flet.dev/docs/controls/switch/#active_color "Direct link to active_color")
The [color](https://flet.dev/docs/reference/colors) to use when this switch is on.
### `active_track_color`[​](https://flet.dev/docs/controls/switch/#active_track_color "Direct link to active_track_color")
The [color](https://flet.dev/docs/reference/colors) to use on the track when this switch is on.
If `track_color` returns a non-null color in the `SELECTED` state, it will be used instead of this color.
### `adaptive`[​](https://flet.dev/docs/controls/switch/#adaptive "Direct link to adaptive")
If the value is `True`, an adaptive Switch is created based on whether the target platform is iOS/macOS.
On iOS and macOS, a `CupertinoSwitch` is created, which has matching functionality and presentation as `Switch`, and the graphics as expected on iOS. On other platforms, a Material Switch is created.
Defaults to `False`. See the example of usage [here](https://flet.dev/docs/controls/cupertinoswitch#cupertinoswitch-and-adaptive-switch).
### `autofocus`[​](https://flet.dev/docs/controls/switch/#autofocus "Direct link to autofocus")
True if the control will be selected as the initial focus. If there is more than one control on a page with autofocus set, then the first one added to the page will get focus.
### `focus_color`[​](https://flet.dev/docs/controls/switch/#focus_color "Direct link to focus_color")
The [color](https://flet.dev/docs/reference/colors) to use for the focus highlight for keyboard interactions.
### `hover_color`[​](https://flet.dev/docs/controls/switch/#hover_color "Direct link to hover_color")
The [color](https://flet.dev/docs/reference/colors) to be used when it is being hovered over by the mouse pointer.
### `inactive_thumb_color`[​](https://flet.dev/docs/controls/switch/#inactive_thumb_color "Direct link to inactive_thumb_color")
The [color](https://flet.dev/docs/reference/colors) to use on the thumb when this switch is off.
Defaults to colors defined in the [material design specification](https://m3.material.io/components/switch/specs).
If `thumb_color` returns a non-null color in the `DEFAULT` state, it will be used instead of this color.
### `inactive_thumb_image`[​](https://flet.dev/docs/controls/switch/#inactive_thumb_image "Direct link to inactive_thumb_image")
An image to use on the thumb of this switch when the switch is off. Can be a local file path or URL.
### `inactive_track_color`[​](https://flet.dev/docs/controls/switch/#inactive_track_color "Direct link to inactive_track_color")
The [color](https://flet.dev/docs/reference/colors) to use on the track when this switch is off.
Defaults to colors defined in the [material design specification](https://m3.material.io/components/switch/specs).
If `track_color` returns a non-null color in the `DEFAULT` state, it will be used instead of this color.
### `label`[​](https://flet.dev/docs/controls/switch/#label "Direct link to label")
The clickable label to display on the right of the Switch.
### `label_style`[​](https://flet.dev/docs/controls/switch/#label_style "Direct link to label_style")
The label's style.
Value is of type [`TextStyle`](https://flet.dev/docs/reference/types/textstyle).
### `label_position`[​](https://flet.dev/docs/controls/switch/#label_position "Direct link to label_position")
Value is of type [`LabelPosition`](https://flet.dev/docs/reference/types/labelposition) and defaults to `LabelPosition.RIGHT`.
### `mouse_cursor`[​](https://flet.dev/docs/controls/switch/#mouse_cursor "Direct link to mouse_cursor")
The cursor to be displayed when a mouse pointer enters or is hovering over this control. The value is [`MouseCursor`](https://flet.dev/docs/reference/types/mousecursor) enum.
### `overlay_color`[​](https://flet.dev/docs/controls/switch/#overlay_color "Direct link to overlay_color")
The [color](https://flet.dev/docs/reference/colors) for the switch's Material in various [`ControlState`](https://flet.dev/docs/reference/types/controlstate) states. The following [`ControlState`](https://flet.dev/docs/reference/types/controlstate) values are supported: `PRESSED`, `SELECTED`, `HOVERED`, `FOCUSED` and `DEFAULT`.
### `splash_radius`[​](https://flet.dev/docs/controls/switch/#splash_radius "Direct link to splash_radius")
The radius of the splash effect when the switch is pressed.
### `thumb_color`[​](https://flet.dev/docs/controls/switch/#thumb_color "Direct link to thumb_color")
The [color](https://flet.dev/docs/reference/colors) of this switch's thumb in various [`ControlState`](https://flet.dev/docs/reference/types/controlstate) states. The following [`ControlState`](https://flet.dev/docs/reference/types/controlstate) values are supported: `SELECTED`, `HOVERED`, `DISABLED`, `FOCUSED` and `DEFAULT` (fallback).
### `thumb_icon`[​](https://flet.dev/docs/controls/switch/#thumb_icon "Direct link to thumb_icon")
The icon of this Switch's thumb in various [`ControlState`](https://flet.dev/docs/reference/types/controlstate) states. The following [`ControlState`](https://flet.dev/docs/reference/types/controlstate) values are supported: `SELECTED`, `HOVERED`, `DISABLED`, `FOCUSED` and `DEFAULT` (fallback).
### `track_color`[​](https://flet.dev/docs/controls/switch/#track_color "Direct link to track_color")
The [color](https://flet.dev/docs/reference/colors) of this switch's track in various [`ControlState`](https://flet.dev/docs/reference/types/controlstate) states. The following [`ControlState`](https://flet.dev/docs/reference/types/controlstate) values are supported: `SELECTED`, `HOVERED`, `DISABLED`, `FOCUSED` and `DEFAULT` (fallback).
### `track_outline_color`[​](https://flet.dev/docs/controls/switch/#track_outline_color "Direct link to track_outline_color")
The outline [color](https://flet.dev/docs/reference/colors) of this switch's track in various [`ControlState`](https://flet.dev/docs/reference/types/controlstate) states. The following [`ControlState`](https://flet.dev/docs/reference/types/controlstate) values are supported: `SELECTED`, `HOVERED`, `DISABLED`, `FOCUSED` and `DEFAULT` (fallback).
### `track_outline_width`[​](https://flet.dev/docs/controls/switch/#track_outline_width "Direct link to track_outline_width")
The outline width of this switch's track in all or specific [`ControlState`](https://flet.dev/docs/reference/types/controlstate) states. The following states are supported: `SELECTED`, `HOVERED`, `DISABLED`, `FOCUSED` and `DEFAULT` (fallback).
### `value`[​](https://flet.dev/docs/controls/switch/#value "Direct link to value")
Current value of the Switch.
## Events[​](https://flet.dev/docs/controls/switch/#events "Direct link to Events")
### `on_blur`[​](https://flet.dev/docs/controls/switch/#on_blur "Direct link to on_blur")
Fires when the control has lost focus.
### `on_change`[​](https://flet.dev/docs/controls/switch/#on_change "Direct link to on_change")
Fires when the state of the Switch is changed.
### `on_focus`[​](https://flet.dev/docs/controls/switch/#on_focus "Direct link to on_focus")
Fires when the control has received focus.
Event handler argument is of type [`OnFocusEvent`](https://flet.dev/docs/reference/types/onfocusevent).
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/switch.md)
[PreviousSlider](https://flet.dev/docs/controls/slider)[NextTextField](https://flet.dev/docs/controls/textfield)
  * [Examples](https://flet.dev/docs/controls/switch/#examples)
    * [Basic switches](https://flet.dev/docs/controls/switch/#basic-switches)
    * [Switch with `on_change` event](https://flet.dev/docs/controls/switch/#switch-with-on_change-event)
  * [Properties](https://flet.dev/docs/controls/switch/#properties)
    * [`active_color`](https://flet.dev/docs/controls/switch/#active_color)
    * [`active_track_color`](https://flet.dev/docs/controls/switch/#active_track_color)
    * [`adaptive`](https://flet.dev/docs/controls/switch/#adaptive)
    * [`autofocus`](https://flet.dev/docs/controls/switch/#autofocus)
    * [`focus_color`](https://flet.dev/docs/controls/switch/#focus_color)
    * [`hover_color`](https://flet.dev/docs/controls/switch/#hover_color)
    * [`inactive_thumb_color`](https://flet.dev/docs/controls/switch/#inactive_thumb_color)
    * [`inactive_thumb_image`](https://flet.dev/docs/controls/switch/#inactive_thumb_image)
    * [`inactive_track_color`](https://flet.dev/docs/controls/switch/#inactive_track_color)
    * [`label`](https://flet.dev/docs/controls/switch/#label)
    * [`label_style`](https://flet.dev/docs/controls/switch/#label_style)
    * [`label_position`](https://flet.dev/docs/controls/switch/#label_position)
    * [`mouse_cursor`](https://flet.dev/docs/controls/switch/#mouse_cursor)
    * [`overlay_color`](https://flet.dev/docs/controls/switch/#overlay_color)
    * [`splash_radius`](https://flet.dev/docs/controls/switch/#splash_radius)
    * [`thumb_color`](https://flet.dev/docs/controls/switch/#thumb_color)
    * [`thumb_icon`](https://flet.dev/docs/controls/switch/#thumb_icon)
    * [`track_color`](https://flet.dev/docs/controls/switch/#track_color)
    * [`track_outline_color`](https://flet.dev/docs/controls/switch/#track_outline_color)
    * [`track_outline_width`](https://flet.dev/docs/controls/switch/#track_outline_width)
    * [`value`](https://flet.dev/docs/controls/switch/#value)
  * [Events](https://flet.dev/docs/controls/switch/#events)
    * [`on_blur`](https://flet.dev/docs/controls/switch/#on_blur)
    * [`on_change`](https://flet.dev/docs/controls/switch/#on_change)
    * [`on_focus`](https://flet.dev/docs/controls/switch/#on_focus)


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
