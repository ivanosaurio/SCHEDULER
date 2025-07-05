[Skip to main content](https://flet.dev/docs/controls/checkbox/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/checkbox/)
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
  * [Cookbook](https://flet.dev/docs/controls/checkbox/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Input and Selections](https://flet.dev/docs/controls/input-and-selections)
  * Checkbox


On this page
# Checkbox
Checkbox allows to select one or more items from a group, or switch between two mutually exclusive options (checked or unchecked, on or off).
## Examples[​](https://flet.dev/docs/controls/checkbox/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/input/checkbox)
### Basic checkboxes[​](https://flet.dev/docs/controls/checkbox/#basic-checkboxes "Direct link to Basic checkboxes")
python/controls/input-and-selections/checkbox/checkbox-basic.py
```
import flet as ftdefmain(page: ft.Page):defbutton_clicked(e):    t.value =f"Checkboxes values are: {c1.value}, {c2.value}, {c3.value}, {c4.value}, {c5.value}."    page.update()  t = ft.Text()  c1 = ft.Checkbox(label="Unchecked by default checkbox", value=False)  c2 = ft.Checkbox(label="Undefined by default tristate checkbox", tristate=True)  c3 = ft.Checkbox(label="Checked by default checkbox", value=True)  c4 = ft.Checkbox(label="Disabled checkbox", disabled=True)  c5 = ft.Checkbox(    label="Checkbox with rendered label_position='left'",    label_position=ft.LabelPosition.LEFT,)  b = ft.ElevatedButton(text="Submit", on_click=button_clicked)  page.add(c1, c2, c3, c4, c5, b, t)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/input-and-selections/checkbox/checkbox-basic.py)
![](https://flet.dev/img/docs/controls/checkbox/basic-checkbox.gif)
### Checkbox with `on_change` event[​](https://flet.dev/docs/controls/checkbox/#checkbox-with-on_change-event "Direct link to checkbox-with-on_change-event")
python/controls/input-and-selections/checkbox/checkbox-with-event.py
```
import flet as ftdefmain(page: ft.Page):defcheckbox_changed(e):    page.add(ft.Text(f"Checkbox value changed to {c.value}"))    page.update()  c = ft.Checkbox(label="Checkbox with 'change' event", on_change=checkbox_changed)  page.add(c)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/input-and-selections/checkbox/checkbox-with-event.py)
![](https://flet.dev/img/docs/controls/checkbox/checkbox-with-change-event.gif)
## Properties[​](https://flet.dev/docs/controls/checkbox/#properties "Direct link to Properties")
### `active_color`[​](https://flet.dev/docs/controls/checkbox/#active_color "Direct link to active_color")
The [color](https://flet.dev/docs/reference/colors) to use when this checkbox is checked.
### `adaptive`[​](https://flet.dev/docs/controls/checkbox/#adaptive "Direct link to adaptive")
If the value is `True`, an adaptive Checkbox is created based on whether the target platform is iOS/macOS.
On iOS and macOS, a [`CupertinoCheckbox`](https://flet.dev/docs/controls/cupertinocheckbox) is created, which has matching functionality and presentation as `Checkbox`, and the graphics as expected on iOS. On other platforms, a Material Checkbox is created.
See the example of usage [here](https://flet.dev/docs/controls/cupertinocheckbox#cupertinocheckbox-and-adaptive-checkbox-example).
Defaults to `False`.
### `autofocus`[​](https://flet.dev/docs/controls/checkbox/#autofocus "Direct link to autofocus")
True if the control will be selected as the initial focus. If there is more than one control on a page with autofocus set, then the first one added to the page will get focus.
### `border`[​](https://flet.dev/docs/controls/checkbox/#border "Direct link to border")
The color and width of the checkbox's border to be rendered when the checkbox's `value` is `False`.
### `check_color`[​](https://flet.dev/docs/controls/checkbox/#check_color "Direct link to check_color")
The [color](https://flet.dev/docs/reference/colors) to use for the check icon when this checkbox is checked.
### `fill_color`[​](https://flet.dev/docs/controls/checkbox/#fill_color "Direct link to fill_color")
The [color](https://flet.dev/docs/reference/colors) that fills the checkbox in various [`ControlState`](https://flet.dev/docs/reference/types/controlstate) states.
### `hover_color`[​](https://flet.dev/docs/controls/checkbox/#hover_color "Direct link to hover_color")
The [color](https://flet.dev/docs/reference/colors) to use when this checkbox is hovered.
### `is_error`[​](https://flet.dev/docs/controls/checkbox/#is_error "Direct link to is_error")
Whether this checkbox wants to show an error state. When `True` this checkbox will have a different default container color and check color. Defaults to `False`.
### `label`[​](https://flet.dev/docs/controls/checkbox/#label "Direct link to label")
The clickable label to display on the right of a checkbox.
### `label_style`[​](https://flet.dev/docs/controls/checkbox/#label_style "Direct link to label_style")
The label's style. An instance of type [`TextStyle`](https://flet.dev/docs/reference/types/textstyle).
### `label_position`[​](https://flet.dev/docs/controls/checkbox/#label_position "Direct link to label_position")
Defines on which side of the checkbox the `label` should be shown.
Value is of type [`LabelPosition`](https://flet.dev/docs/reference/types/labelposition) and defaults to `LabelPosition.RIGHT`.
### `mouse_cursor`[​](https://flet.dev/docs/controls/checkbox/#mouse_cursor "Direct link to mouse_cursor")
The cursor to be displayed when a mouse pointer enters or is hovering over this control.
Value is of type [`MouseCursor`](https://flet.dev/docs/reference/types/mousecursor).
### `overlay_color`[​](https://flet.dev/docs/controls/checkbox/#overlay_color "Direct link to overlay_color")
The [color](https://flet.dev/docs/reference/colors) of the checkbox's overlay in various [`ControlState`](https://flet.dev/docs/reference/types/controlstate) states.
This property supports the following `ControlState` values: `PRESSED`, `SELECTED`, `HOVERED` and `FOCUSED`.
### `semantics_label`[​](https://flet.dev/docs/controls/checkbox/#semantics_label "Direct link to semantics_label")
The semantic label for the checkbox that is not shown in the UI, but will be announced by screen readers in accessibility modes (e.g TalkBack/VoiceOver).
### `shape`[​](https://flet.dev/docs/controls/checkbox/#shape "Direct link to shape")
The shape of the checkbox. The value is an instance of [`OutlinedBorder`](https://flet.dev/docs/reference/types/outlinedborder) class.
Defaults to `RoundedRectangleBorder(radius=2)`.
### `splash_radius`[​](https://flet.dev/docs/controls/checkbox/#splash_radius "Direct link to splash_radius")
The radius of the circular Material ink response (ripple) in logical pixels.
Defaults to `20.0`.
### `tristate`[​](https://flet.dev/docs/controls/checkbox/#tristate "Direct link to tristate")
If `True` the checkboxes value can be `True`, `False`, or `None`.
Checkbox displays a dash when its value is `None`.
### `value`[​](https://flet.dev/docs/controls/checkbox/#value "Direct link to value")
Current value of the checkbox.
## Events[​](https://flet.dev/docs/controls/checkbox/#events "Direct link to Events")
### `on_blur`[​](https://flet.dev/docs/controls/checkbox/#on_blur "Direct link to on_blur")
Fires when the control has lost focus.
### `on_change`[​](https://flet.dev/docs/controls/checkbox/#on_change "Direct link to on_change")
Fires when the state of the Checkbox is changed.
### `on_focus`[​](https://flet.dev/docs/controls/checkbox/#on_focus "Direct link to on_focus")
Fires when the control has received focus.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/checkbox.md)
[PreviousAutofillGroup](https://flet.dev/docs/controls/autofillgroup)[NextChip](https://flet.dev/docs/controls/chip)
  * [Examples](https://flet.dev/docs/controls/checkbox/#examples)
    * [Basic checkboxes](https://flet.dev/docs/controls/checkbox/#basic-checkboxes)
    * [Checkbox with `on_change` event](https://flet.dev/docs/controls/checkbox/#checkbox-with-on_change-event)
  * [Properties](https://flet.dev/docs/controls/checkbox/#properties)
    * [`active_color`](https://flet.dev/docs/controls/checkbox/#active_color)
    * [`adaptive`](https://flet.dev/docs/controls/checkbox/#adaptive)
    * [`autofocus`](https://flet.dev/docs/controls/checkbox/#autofocus)
    * [`border`](https://flet.dev/docs/controls/checkbox/#border)
    * [`check_color`](https://flet.dev/docs/controls/checkbox/#check_color)
    * [`fill_color`](https://flet.dev/docs/controls/checkbox/#fill_color)
    * [`hover_color`](https://flet.dev/docs/controls/checkbox/#hover_color)
    * [`is_error`](https://flet.dev/docs/controls/checkbox/#is_error)
    * [`label`](https://flet.dev/docs/controls/checkbox/#label)
    * [`label_style`](https://flet.dev/docs/controls/checkbox/#label_style)
    * [`label_position`](https://flet.dev/docs/controls/checkbox/#label_position)
    * [`mouse_cursor`](https://flet.dev/docs/controls/checkbox/#mouse_cursor)
    * [`overlay_color`](https://flet.dev/docs/controls/checkbox/#overlay_color)
    * [`semantics_label`](https://flet.dev/docs/controls/checkbox/#semantics_label)
    * [`shape`](https://flet.dev/docs/controls/checkbox/#shape)
    * [`splash_radius`](https://flet.dev/docs/controls/checkbox/#splash_radius)
    * [`tristate`](https://flet.dev/docs/controls/checkbox/#tristate)
    * [`value`](https://flet.dev/docs/controls/checkbox/#value)
  * [Events](https://flet.dev/docs/controls/checkbox/#events)
    * [`on_blur`](https://flet.dev/docs/controls/checkbox/#on_blur)
    * [`on_change`](https://flet.dev/docs/controls/checkbox/#on_change)
    * [`on_focus`](https://flet.dev/docs/controls/checkbox/#on_focus)


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
