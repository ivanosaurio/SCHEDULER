[Skip to main content](https://flet.dev/docs/controls/radio/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/radio/)
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
  * [Cookbook](https://flet.dev/docs/controls/radio/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Input and Selections](https://flet.dev/docs/controls/input-and-selections)
  * Radio


On this page
# Radio
Radio buttons let people select a single option from two or more choices.
## Examples[​](https://flet.dev/docs/controls/radio/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/input/radio)
### Basic RadioGroup[​](https://flet.dev/docs/controls/radio/#basic-radiogroup "Direct link to Basic RadioGroup")
python/controls/input-and-selections/radio/radiogroup-basic.py
```
import flet as ftdefmain(page):defbutton_clicked(e):    t.value =f"Your favorite color is: {cg.value}"    page.update()  t = ft.Text()  b = ft.ElevatedButton(text="Submit", on_click=button_clicked)  cg = ft.RadioGroup(    content=ft.Column([        ft.Radio(value="red", label="Red"),        ft.Radio(value="green", label="Green"),        ft.Radio(value="blue", label="Blue"),]))  page.add(ft.Text("Select your favorite color:"), cg, b, t)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/input-and-selections/radio/radiogroup-basic.py)
![](https://flet.dev/img/docs/controls/radio/basic-radio.gif)
### RadioGroup with `on_change` event[​](https://flet.dev/docs/controls/radio/#radiogroup-with-on_change-event "Direct link to radiogroup-with-on_change-event")
python/controls/input-and-selections/radio/radiogroup-with-event.py
```
import flet as ftdefmain(page):defradiogroup_changed(e):    t.value =f"Your favorite color is: {e.control.value}"    page.update()  t = ft.Text()  cg = ft.RadioGroup(    content=ft.Column([        ft.Radio(value="red", label="Red"),        ft.Radio(value="green", label="Green"),        ft.Radio(value="blue", label="Blue"),]),    on_change=radiogroup_changed,)  page.add(ft.Text("Select your favorite color:"), cg, t)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/input-and-selections/radio/radiogroup-with-event.py)
![](https://flet.dev/img/docs/controls/radio/radio-with-change-event.gif)
## `RadioGroup` properties[​](https://flet.dev/docs/controls/radio/#radiogroup-properties "Direct link to radiogroup-properties")
### `content`[​](https://flet.dev/docs/controls/radio/#content "Direct link to content")
The content of the RadioGroup. Typically a list of `Radio` controls nested in a container control, e.g. `Column`, `Row`.
### `value`[​](https://flet.dev/docs/controls/radio/#value "Direct link to value")
Current value of the RadioGroup.
## `RadioGroup` events[​](https://flet.dev/docs/controls/radio/#radiogroup-events "Direct link to radiogroup-events")
### `on_change`[​](https://flet.dev/docs/controls/radio/#on_change "Direct link to on_change")
Fires when the state of the RadioGroup is changed.
## `Radio` properties[​](https://flet.dev/docs/controls/radio/#radio-properties "Direct link to radio-properties")
### `active_color`[​](https://flet.dev/docs/controls/radio/#active_color "Direct link to active_color")
The [color](https://flet.dev/docs/reference/colors) used to fill this radio when it is selected.
### `adaptive`[​](https://flet.dev/docs/controls/radio/#adaptive "Direct link to adaptive")
If the value is `True`, an adaptive Radio is created based on whether the target platform is iOS/macOS.
On iOS and macOS, a [`CupertinoRadio`](https://flet.dev/docs/controls/cupertinoradio) is created, which has matching functionality and presentation as `Radio`, and the graphics as expected on iOS. On other platforms, a Material Radio is created.
Defaults to `False`.
### `autofocus`[​](https://flet.dev/docs/controls/radio/#autofocus "Direct link to autofocus")
True if the control will be selected as the initial focus. If there is more than one control on a page with autofocus set, then the first one added to the page will get focus.
### `fill_color`[​](https://flet.dev/docs/controls/radio/#fill_color "Direct link to fill_color")
The [color](https://flet.dev/docs/reference/colors) that fills the radio, in all or specific [`ControlState`](https://flet.dev/docs/reference/types/controlstate) states.
### `focus_color`[​](https://flet.dev/docs/controls/radio/#focus_color "Direct link to focus_color")
The color of this radio when it has the input focus.
### `hover_color`[​](https://flet.dev/docs/controls/radio/#hover_color "Direct link to hover_color")
The color of this radio when it is hovered.
### `label`[​](https://flet.dev/docs/controls/radio/#label "Direct link to label")
The clickable label to display on the right of a Radio.
### `label_style`[​](https://flet.dev/docs/controls/radio/#label_style "Direct link to label_style")
The label's style.
Value is of type [`TextStyle`](https://flet.dev/docs/reference/types/textstyle).
### `label_position`[​](https://flet.dev/docs/controls/radio/#label_position "Direct link to label_position")
Value is of type [`LabelPosition`](https://flet.dev/docs/reference/types/labelposition) and defaults to `LabelPosition.RIGHT`.
### `mouse_cursor`[​](https://flet.dev/docs/controls/radio/#mouse_cursor "Direct link to mouse_cursor")
The cursor for a mouse pointer entering or hovering over this control.
Value is of type [`MouseCursor`](https://flet.dev/docs/reference/types/mousecursor).
### `overlay_color`[​](https://flet.dev/docs/controls/radio/#overlay_color "Direct link to overlay_color")
The overlay [color](https://flet.dev/docs/reference/colors) of this radio in all or specific [`ControlState`](https://flet.dev/docs/reference/types/controlstate) states.
### `splash_radius`[​](https://flet.dev/docs/controls/radio/#splash_radius "Direct link to splash_radius")
The splash radius of the circular Material ink response.
### `toggleable`[​](https://flet.dev/docs/controls/radio/#toggleable "Direct link to toggleable")
Set to `True` if this radio button is allowed to be returned to an indeterminate state by selecting it again when selected.
### `value`[​](https://flet.dev/docs/controls/radio/#value-1 "Direct link to value-1")
The value to set to containing `RadioGroup` when the radio is selected.
### `visual_density`[​](https://flet.dev/docs/controls/radio/#visual_density "Direct link to visual_density")
Defines how compact the radio's layout will be.
Value is of type [`VisualDensity`](https://flet.dev/docs/reference/types/visualdensity).
## `Radio` events[​](https://flet.dev/docs/controls/radio/#radio-events "Direct link to radio-events")
### `on_blur`[​](https://flet.dev/docs/controls/radio/#on_blur "Direct link to on_blur")
Fires when the control has lost focus.
### `on_focus`[​](https://flet.dev/docs/controls/radio/#on_focus "Direct link to on_focus")
Fires when the control has received focus.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/radio.md)
[PreviousDropdownM2](https://flet.dev/docs/controls/dropdownm2)[NextRangeSlider](https://flet.dev/docs/controls/rangeslider)
  * [Examples](https://flet.dev/docs/controls/radio/#examples)
    * [Basic RadioGroup](https://flet.dev/docs/controls/radio/#basic-radiogroup)
    * [RadioGroup with `on_change` event](https://flet.dev/docs/controls/radio/#radiogroup-with-on_change-event)
  * [`RadioGroup` properties](https://flet.dev/docs/controls/radio/#radiogroup-properties)
    * [`content`](https://flet.dev/docs/controls/radio/#content)
    * [`value`](https://flet.dev/docs/controls/radio/#value)
  * [`RadioGroup` events](https://flet.dev/docs/controls/radio/#radiogroup-events)
    * [`on_change`](https://flet.dev/docs/controls/radio/#on_change)
  * [`Radio` properties](https://flet.dev/docs/controls/radio/#radio-properties)
    * [`active_color`](https://flet.dev/docs/controls/radio/#active_color)
    * [`adaptive`](https://flet.dev/docs/controls/radio/#adaptive)
    * [`autofocus`](https://flet.dev/docs/controls/radio/#autofocus)
    * [`fill_color`](https://flet.dev/docs/controls/radio/#fill_color)
    * [`focus_color`](https://flet.dev/docs/controls/radio/#focus_color)
    * [`hover_color`](https://flet.dev/docs/controls/radio/#hover_color)
    * [`label`](https://flet.dev/docs/controls/radio/#label)
    * [`label_style`](https://flet.dev/docs/controls/radio/#label_style)
    * [`label_position`](https://flet.dev/docs/controls/radio/#label_position)
    * [`mouse_cursor`](https://flet.dev/docs/controls/radio/#mouse_cursor)
    * [`overlay_color`](https://flet.dev/docs/controls/radio/#overlay_color)
    * [`splash_radius`](https://flet.dev/docs/controls/radio/#splash_radius)
    * [`toggleable`](https://flet.dev/docs/controls/radio/#toggleable)
    * [`value`](https://flet.dev/docs/controls/radio/#value-1)
    * [`visual_density`](https://flet.dev/docs/controls/radio/#visual_density)
  * [`Radio` events](https://flet.dev/docs/controls/radio/#radio-events)
    * [`on_blur`](https://flet.dev/docs/controls/radio/#on_blur)
    * [`on_focus`](https://flet.dev/docs/controls/radio/#on_focus)


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
