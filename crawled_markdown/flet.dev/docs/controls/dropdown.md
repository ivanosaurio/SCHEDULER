[Skip to main content](https://flet.dev/docs/controls/dropdown/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/dropdown/)
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
  * [Cookbook](https://flet.dev/docs/controls/dropdown/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Input and Selections](https://flet.dev/docs/controls/input-and-selections)
  * Dropdown


On this page
# Dropdown
Dropdown is used to help people make a choice from a menu and put the selected item into the text input field. It's also possible to filter the list based on the text input or search one item in the menu list.
info
Since version 0.27.0, Flet uses [DropdownMenu](https://api.flutter.dev/flutter/material/DropdownMenu-class.html) flutter widget for [Dropdown](https://flet.dev/docs/controls/dropdown) control, which is a Material 3 version of previously used DropdownButton.
Some properties of previous Dropdown implementation are not available in the new version and were "stubbed" - they will not break your program but don't do anything. See the list of deprecated properties [here](https://flet.dev/docs/controls/dropdown/#deprecated-dropdown-properties-and-events).
Previous version of Dropdown control is available as [`DropdownM2`](https://flet.dev/docs/controls/dropdownm2) control and will be removed in Flet 0.30.0.
## Examples[​](https://flet.dev/docs/controls/dropdown/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/input/dropdown)
### Dropdown with colors[​](https://flet.dev/docs/controls/dropdown/#dropdown-with-colors "Direct link to Dropdown with colors")
python/controls/input-and-selections/dropdown/dropdown-example.py
```
import flet as ftdefmain(page: ft.Page):  colors =[    ft.Colors.RED,    ft.Colors.BLUE,    ft.Colors.YELLOW,    ft.Colors.PURPLE,    ft.Colors.LIME,]defget_options():    options =[]for color in colors:      options.append(        ft.DropdownOption(          key=color.value,          content=ft.Text(            value=color.value,            color=color,),))return optionsdefdropdown_changed(e):    e.control.color = e.control.value    page.update()  dd = ft.Dropdown(    editable=True,    label="Color",    options=get_options(),    on_change=dropdown_changed,)  page.add(dd)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/input-and-selections/dropdown/dropdown-example.py)
![](https://flet.dev/img/docs/controls/dropdown/dropdown-with-colors.png)
### Dropdown with icons[​](https://flet.dev/docs/controls/dropdown/#dropdown-with-icons "Direct link to Dropdown with icons")
python/controls/input-and-selections/dropdown/dropdown-icon-example.py
```
import flet as ftdefmain(page: ft.Page):  icons =[{"name":"Smile","icon_name": ft.Icons.SENTIMENT_SATISFIED_OUTLINED},{"name":"Cloud","icon_name": ft.Icons.CLOUD_OUTLINED},{"name":"Brush","icon_name": ft.Icons.BRUSH_OUTLINED},{"name":"Heart","icon_name": ft.Icons.FAVORITE},]defget_options():    options =[]for icon in icons:      options.append(        ft.DropdownOption(key=icon["name"], leading_icon=icon["icon_name"]))return options  dd = ft.Dropdown(    border=ft.InputBorder.UNDERLINE,    enable_filter=True,    editable=True,    leading_icon=ft.Icons.SEARCH,    label="Icon",    options=get_options(),)  page.add(dd)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/input-and-selections/dropdown/dropdown-icon-example.py)
![](https://flet.dev/img/docs/controls/dropdown/dropdown-with-icons.png)
## `Dropdown` properties[​](https://flet.dev/docs/controls/dropdown/#dropdown-properties "Direct link to dropdown-properties")
### `autofocus`[​](https://flet.dev/docs/controls/dropdown/#autofocus "Direct link to autofocus")
True if the control will be selected as the initial focus. If there is more than one control on a page with autofocus set, then the first one added to the page will get focus.
### `bgcolor`[​](https://flet.dev/docs/controls/dropdown/#bgcolor "Direct link to bgcolor")
The background [color](https://flet.dev/docs/reference/colors) of the dropdown menu in various [`ControlState`](https://flet.dev/docs/reference/types/controlstate) states.
### `border`[​](https://flet.dev/docs/controls/dropdown/#border "Direct link to border")
Border around input.
Value is of type [`InputBorder`](https://flet.dev/docs/reference/types/inputborder) and defaults to `InputBorder.OUTLINE`.
### `border_color`[​](https://flet.dev/docs/controls/dropdown/#border_color "Direct link to border_color")
Border [color](https://flet.dev/docs/reference/colors). Could be `transparent` to hide the border.
### `border_radius`[​](https://flet.dev/docs/controls/dropdown/#border_radius "Direct link to border_radius")
Border radius is an instance of [`BorderRadius`](https://flet.dev/docs/reference/types/borderradius) class.
### `border_width`[​](https://flet.dev/docs/controls/dropdown/#border_width "Direct link to border_width")
The width of the border in virtual pixels. Set to `0` to completely remove border.
Defaults to `1`.
### `color`[​](https://flet.dev/docs/controls/dropdown/#color "Direct link to color")
Text [color](https://flet.dev/docs/reference/colors).
### `content_padding`[​](https://flet.dev/docs/controls/dropdown/#content_padding "Direct link to content_padding")
The [padding](https://flet.dev/docs/reference/types/padding) for the input decoration's container.
### `dense`[​](https://flet.dev/docs/controls/dropdown/#dense "Direct link to dense")
Whether the TextField is part of a dense form (ie, uses less vertical space).
### `elevation`[​](https://flet.dev/docs/controls/dropdown/#elevation "Direct link to elevation")
The dropdown's menu elevation in various [`ControlState`](https://flet.dev/docs/reference/types/controlstate) states.
Defaults to `8`.
### `enable_filter`[​](https://flet.dev/docs/controls/dropdown/#enable_filter "Direct link to enable_filter")
Determine if the menu list can be filtered by the text input. Defaults to false.
If set to true, dropdown menu will show a filtered list. The filtered list will contain items that match the text provided by the input field, with a case-insensitive comparison.
![](https://flet.dev/img/docs/controls/dropdown/dropdown-filter.gif)
### `enable_search`[​](https://flet.dev/docs/controls/dropdown/#enable_search "Direct link to enable_search")
Determine if the first item that matches the text input can be highlighted.
Defaults to true as the search function could be commonly used.
![](https://flet.dev/img/docs/controls/dropdown/dropdown-search.gif)
### `error_style`[​](https://flet.dev/docs/controls/dropdown/#error_style "Direct link to error_style")
The [`TextStyle`](https://flet.dev/docs/reference/types/textstyle) to use for `error_text`.
### `error_text`[​](https://flet.dev/docs/controls/dropdown/#error_text "Direct link to error_text")
Text that appears below the input border.
If non-null, the border's color animates to red and the `helper_text` is not shown.
### `filled`[​](https://flet.dev/docs/controls/dropdown/#filled "Direct link to filled")
If `True` the decoration's container is filled with theme `fill_color`. The default is `False`.
### `fill_color`[​](https://flet.dev/docs/controls/dropdown/#fill_color "Direct link to fill_color")
Background [color](https://flet.dev/docs/reference/colors) of the dropdown input text field. Will not be visible if `filled=False`.
### `focused_border_color`[​](https://flet.dev/docs/controls/dropdown/#focused_border_color "Direct link to focused_border_color")
Border [color](https://flet.dev/docs/reference/colors) in focused state.
### `focused_border_width`[​](https://flet.dev/docs/controls/dropdown/#focused_border_width "Direct link to focused_border_width")
Border width in focused state.
### `helper_style`[​](https://flet.dev/docs/controls/dropdown/#helper_style "Direct link to helper_style")
The [`TextStyle`](https://flet.dev/docs/reference/types/textstyle) to use for `helper_text`.
### `helper_text`[​](https://flet.dev/docs/controls/dropdown/#helper_text "Direct link to helper_text")
Text that provides context about the input's value, such as how the value will be used.
If non-null, the text is displayed below the input decorator, in the same location as `error_text`. If a non-null `error_text` value is specified then the helper text is not shown.
### `hint_style`[​](https://flet.dev/docs/controls/dropdown/#hint_style "Direct link to hint_style")
The [`TextStyle`](https://flet.dev/docs/reference/types/textstyle) to use for `hint_text`.
### `hint_text`[​](https://flet.dev/docs/controls/dropdown/#hint_text "Direct link to hint_text")
Text that suggests what sort of input the field accepts.
Displayed on top of the input when it's empty and either (a) `label` is null or (b) the input has the focus.
### `label`[​](https://flet.dev/docs/controls/dropdown/#label "Direct link to label")
Optional text that describes the input field.
When the input field is empty and unfocused, the label is displayed on top of the input field (i.e., at the same location on the screen where text may be entered in the input field). When the input field receives focus (or if the field is non-empty) the label moves above, either vertically adjacent to, or to the center of the input field.
### `label_style`[​](https://flet.dev/docs/controls/dropdown/#label_style "Direct link to label_style")
The [`TextStyle`](https://flet.dev/docs/reference/types/textstyle) to use for `label`.
### `leading_icon`[​](https://flet.dev/docs/controls/dropdown/#leading_icon "Direct link to leading_icon")
An optional Icon at the front of the text input field inside the decoration box (previously, [`prefix_icon`](https://flet.dev/docs/controls/dropdown/#prefix_icon)).
Defaults to null. If this is not null, the menu items will have extra paddings to be aligned with the text in the text field.
### `menu_height`[​](https://flet.dev/docs/controls/dropdown/#menu_height "Direct link to menu_height")
The height of the dropdown menu. If this is null, the menu will display as many items as possible on the screen.
### `menu_width`[​](https://flet.dev/docs/controls/dropdown/#menu_width "Direct link to menu_width")
The width of the dropdown menu. If this is null, the menu width will be the same as input textfield width.
### `options`[​](https://flet.dev/docs/controls/dropdown/#options "Direct link to options")
A list of `DropdownOption` controls representing items in this dropdown.
### `selected_trailing_icon`[​](https://flet.dev/docs/controls/dropdown/#selected_trailing_icon "Direct link to selected_trailing_icon")
An optional icon at the end of the text field to indicate that the text field is pressed.
Defaults to an Icon with `ft.Icons.ARROW_DROP_UP`.
### `text_align`[​](https://flet.dev/docs/controls/dropdown/#text_align "Direct link to text_align")
The text align for the TextField of the Dropdown.
Value is of type [`TextAlign`](https://flet.dev/docs/reference/types/textalign) and defaults to `TextAlign.START`.
### `text_size`[​](https://flet.dev/docs/controls/dropdown/#text_size "Direct link to text_size")
Text size in virtual pixels.
### `text_style`[​](https://flet.dev/docs/controls/dropdown/#text_style "Direct link to text_style")
The [`TextStyle`](https://flet.dev/docs/reference/types/textstyle) to use for text in input text field.
### `trailing_icon`[​](https://flet.dev/docs/controls/dropdown/#trailing_icon "Direct link to trailing_icon")
An optional icon at the end of the text field (previously, [`select_icon`](https://flet.dev/docs/controls/dropdown/#select_icon)).
Defaults to an Icon with `ft.Icons.ARROW_DROP_DOWN`.
### `width`[​](https://flet.dev/docs/controls/dropdown/#width "Direct link to width")
Determine the width of the Dropdown.
If this is null, the width of the Dropdown will be the same as the width of the widest menu item plus the width of the leading/trailing icon.
### `value`[​](https://flet.dev/docs/controls/dropdown/#value "Direct link to value")
`key` value of the selected option.
## `Dropdown` methods[​](https://flet.dev/docs/controls/dropdown/#dropdown-methods "Direct link to dropdown-methods")
### `focus()`[​](https://flet.dev/docs/controls/dropdown/#focus "Direct link to focus")
Moves focus to this dropdown.
## `Dropdown` events[​](https://flet.dev/docs/controls/dropdown/#dropdown-events "Direct link to dropdown-events")
### `on_blur`[​](https://flet.dev/docs/controls/dropdown/#on_blur "Direct link to on_blur")
Fires when the control has lost focus.
### `on_change`[​](https://flet.dev/docs/controls/dropdown/#on_change "Direct link to on_change")
Fires when the selected item of this dropdown has changed.
### `on_focus`[​](https://flet.dev/docs/controls/dropdown/#on_focus "Direct link to on_focus")
Fires when the control has received focus.
## Deprecated `Dropdown` properties and events[​](https://flet.dev/docs/controls/dropdown/#deprecated-dropdown-properties-and-events "Direct link to deprecated-dropdown-properties-and-events")
warning
The properties and events below are not available in Dropdown control since Flet version 0.27.0 and will be removed in Flet version 0.30.0. They were "stubbed" - using them will not break your program but they don't do anything.
They are still available in previous version of `Dropdown` control [`DropdownM2`](https://flet.dev/docs/controls/dropdownm2) which will be removed in 0.30.0.
### ~~`alignment`~~[​](https://flet.dev/docs/controls/dropdown/#alignment "Direct link to alignment")
Defines how the `hint` or the selected item is positioned within this dropdown.
Alignment is an instance of [`Alignment`](https://flet.dev/docs/reference/types/alignment) class.
### ~~`counter`~~[​](https://flet.dev/docs/controls/dropdown/#counter "Direct link to counter")
A `Control` to place below the line as a character count.
If `None` or an empty string and `counter_text` isn't specified, then nothing will appear in the counter's location.
### ~~`counter_style`~~[​](https://flet.dev/docs/controls/dropdown/#counter_style "Direct link to counter_style")
The [`TextStyle`](https://flet.dev/docs/reference/types/textstyle) to use for `counter_text`.
### ~~`counter_text`~~[​](https://flet.dev/docs/controls/dropdown/#counter_text "Direct link to counter_text")
Optional text to place below the line as a character count.
If `None` or an empty string and `counter` isn't specified, then nothing will appear in the counter's location. If `counter` is specified and visible, then this `counter_text` will be ignored.
### ~~`disabled_hint_content`~~[​](https://flet.dev/docs/controls/dropdown/#disabled_hint_content "Direct link to disabled_hint_content")
A placeholder `Control` for the dropdown's value that is displayed when `value` is `None` and the dropdown is disabled.
### ~~`enable_feedback`~~[​](https://flet.dev/docs/controls/dropdown/#enable_feedback "Direct link to enable_feedback")
Whether detected gestures should provide acoustic and/or haptic feedback. On Android, for example, setting this to `True` produce a click sound and a long-press will produce a short vibration.
Defaults to `True`.
### ~~`focused_bgcolor`~~[​](https://flet.dev/docs/controls/dropdown/#focused_bgcolor "Direct link to focused_bgcolor")
Background [color](https://flet.dev/docs/reference/colors) of dropdown in focused state. Will not be visible if `filled=False`.
### ~~`focused_color`~~[​](https://flet.dev/docs/controls/dropdown/#focused_color "Direct link to focused_color")
Text [color](https://flet.dev/docs/reference/colors) when Dropdown is focused.
### ~~`hint_content`~~[​](https://flet.dev/docs/controls/dropdown/#hint_content "Direct link to hint_content")
A placeholder `Control` for the dropdown's value that is displayed when `value` is `None`.
### ~~`icon`~~[​](https://flet.dev/docs/controls/dropdown/#icon "Direct link to icon")
The [name of the icon](https://flet.dev/docs/reference/icons) or `Control` to show before the input field and outside of the decoration's container.
Example with icon name:
```
icon=ft.Icons.BOOKMARK
```

Example with Control:
```
icon=ft.Icon(ft.Icons.BOOKMARK)
```

### ~~`icon_content`~~[​](https://flet.dev/docs/controls/dropdown/#icon_content "Direct link to icon_content")
The control to use for the drop-down button's icon. Defaults to an `Icon(icons.ARROW_DROP_DOWN)`.
**Deprecated in v0.25.0 and will be removed in v0.28.0. Use[`icon`](https://flet.dev/docs/controls/dropdown/#select_icon) instead.**
### ~~`icon_enabled_color`~~[​](https://flet.dev/docs/controls/dropdown/#icon_enabled_color "Direct link to icon_enabled_color")
The color of any `Icon` descendant of `icon_content` if this button is enabled.
**Deprecated in v0.25.0 and will be removed in v0.28.0. Use[`select_icon_enabled_color`](https://flet.dev/docs/controls/dropdown/#select_icon_enabled_color) instead.**
### ~~`icon_disabled_color`~~[​](https://flet.dev/docs/controls/dropdown/#icon_disabled_color "Direct link to icon_disabled_color")
The color of any `Icon` descendant of `icon_content` if this button is disabled.
**Deprecated in v0.25.0 and will be removed in v0.28.0. Use[`select_icon_enabled_color`](https://flet.dev/docs/controls/dropdown/#select_icon_enabled_color) instead.**
### ~~`icon_size`~~[​](https://flet.dev/docs/controls/dropdown/#icon_size "Direct link to icon_size")
The size of the icon button which wraps `icon_content`.
Defaults to `24.0`.
**Deprecated in v0.25.0 and will be removed in v0.28.0. Use[`icon`](https://flet.dev/docs/controls/dropdown/#icon) instead.**
### ~~`item_height`~~[​](https://flet.dev/docs/controls/dropdown/#item_height "Direct link to item_height")
The height of the items/options in the dropdown menu.
### ~~`max_menu_height`~~[​](https://flet.dev/docs/controls/dropdown/#max_menu_height "Direct link to max_menu_height")
The maximum height of the dropdown menu. If this is null, the menu will display as many items as possible on the screen.
### ~~`options_fill_horizontally`~~[​](https://flet.dev/docs/controls/dropdown/#options_fill_horizontally "Direct link to options_fill_horizontally")
Whether the dropdown's inner contents to horizontally fill its parent. By default this button's inner width is the minimum size of its content.
If `True`, the inner width is expanded to fill its surrounding container.
Value is of type `bool` and defaults to `False`.
### ~~`padding`~~[​](https://flet.dev/docs/controls/dropdown/#padding "Direct link to padding")
The [padding](https://flet.dev/docs/reference/types/padding) around the visible portion of this dropdown.
### ~~`prefix`~~[​](https://flet.dev/docs/controls/dropdown/#prefix "Direct link to prefix")
Optional `Control` to place on the line before the input.
This can be used, for example, to add some padding to text that would otherwise be specified using `prefix_text`, or to add a custom control in front of the input. The control's baseline is lined up with the input baseline.
Only one of `prefix` and `prefix_text` can be specified.
The `prefix` appears after the `prefix_icon`, if both are specified.
### ~~`prefix_icon`~~[​](https://flet.dev/docs/controls/dropdown/#prefix_icon "Direct link to prefix_icon")
note
Use [`leading_icon`](https://flet.dev/docs/controls/dropdown/#leading_icon) instead.
An icon that appears before the `prefix` or `prefix_text` and before the editable part of the text field, within the decoration's container.
### ~~`prefix_style`~~[​](https://flet.dev/docs/controls/dropdown/#prefix_style "Direct link to prefix_style")
The [`TextStyle`](https://flet.dev/docs/reference/types/textstyle) to use for `prefix_text`.
### ~~`prefix_text`~~[​](https://flet.dev/docs/controls/dropdown/#prefix_text "Direct link to prefix_text")
Optional text `prefix` to place on the line before the input.
### ~~`select_icon`~~[​](https://flet.dev/docs/controls/dropdown/#select_icon "Direct link to select_icon")
note
Use [`trailing_icon`](https://flet.dev/docs/controls/dropdown/#trailing_icon) instead.
The [name of the icon](https://flet.dev/docs/reference/icons) or `Control` to use for the drop-down select button's icon. Defaults to an `Icon(ft.Icons.ARROW_DROP_DOWN)`.
Example with icon name:
```
icon=ft.Icons.BOOKMARK
```

Example with Control:
```
icon=ft.Icon(ft.Icons.BOOKMARK)
```

### ~~`select_icon_enabled_color`~~[​](https://flet.dev/docs/controls/dropdown/#select_icon_enabled_color "Direct link to select_icon_enabled_color")
The color of any `Icon` descendant of `select_icon` if this button is enabled.
### ~~`select_icon_disabled_color`~~[​](https://flet.dev/docs/controls/dropdown/#select_icon_disabled_color "Direct link to select_icon_disabled_color")
The color of any `Icon` descendant of `select_icon` if this button is disabled.
### ~~`select_icon_size`~~[​](https://flet.dev/docs/controls/dropdown/#select_icon_size "Direct link to select_icon_size")
The size of the icon button which wraps `select_icon`.
Defaults to `24.0`.
### ~~`suffix`~~[​](https://flet.dev/docs/controls/dropdown/#suffix "Direct link to suffix")
Optional `Control` to place on the line after the input.
This can be used, for example, to add some padding to the text that would otherwise be specified using `suffix_text`, or to add a custom control after the input. The control's baseline is lined up with the input baseline.
Only one of `suffix` and `suffix_text` can be specified.
The `suffix` appears before the `suffix_icon`, if both are specified.
### ~~`suffix_icon`~~[​](https://flet.dev/docs/controls/dropdown/#suffix_icon "Direct link to suffix_icon")
An icon that appears after the editable part of the text field and after the `suffix` or `suffix_text`, within the decoration's container.
### ~~`suffix_style`~~[​](https://flet.dev/docs/controls/dropdown/#suffix_style "Direct link to suffix_style")
The [`TextStyle`](https://flet.dev/docs/reference/types/textstyle) to use for `suffix_text`.
### ~~`suffix_text`~~[​](https://flet.dev/docs/controls/dropdown/#suffix_text "Direct link to suffix_text")
Optional text `suffix` to place on the line after the input.
### ~~`on_click`~~[​](https://flet.dev/docs/controls/dropdown/#on_click "Direct link to on_click")
Fires when this dropdown is clicked.
## `DropdownOption` properties[​](https://flet.dev/docs/controls/dropdown/#dropdownoption-properties "Direct link to dropdownoption-properties")
Represents an item in a dropdown. Either `key` or `text` must be specified, else an `AssertionError` will be raised.
### `content`[​](https://flet.dev/docs/controls/dropdown/#content "Direct link to content")
A `Control` to display in this option. If not specified, `text` will be used as fallback, else `text`will be ignored.
### `key`[​](https://flet.dev/docs/controls/dropdown/#key "Direct link to key")
Option's key. If not specified `text` will be used as fallback.
### `leading_icon`[​](https://flet.dev/docs/controls/dropdown/#leading_icon-1 "Direct link to leading_icon-1")
An optional icon to display before the content or text.
### `style`[​](https://flet.dev/docs/controls/dropdown/#style "Direct link to style")
Customizes this menu item's appearance.
The value is an instance of [`ButtonStyle`](https://flet.dev/docs/reference/types/buttonstyle) class.
### `text`[​](https://flet.dev/docs/controls/dropdown/#text "Direct link to text")
Option's display text. If not specified `key` will be used as fallback.
### `trailing_icon`[​](https://flet.dev/docs/controls/dropdown/#trailing_icon-1 "Direct link to trailing_icon-1")
An optional icon to display after the content or text.
## Deprecated `DropdownOption` properties and events[​](https://flet.dev/docs/controls/dropdown/#deprecated-dropdownoption-properties-and-events "Direct link to deprecated-dropdownoption-properties-and-events")
### ~~`alignment`~~[​](https://flet.dev/docs/controls/dropdown/#alignment-1 "Direct link to alignment-1")
Defines the alignment of this option in it's container.
Value is of type [`Alignment`](https://flet.dev/docs/reference/types/alignment) and defaults to `alignment.center_left`.
### ~~`text_style`~~[​](https://flet.dev/docs/controls/dropdown/#text_style-1 "Direct link to text_style-1")
Defines the style of the `text`.
Value is of type [`TextStyle`](https://flet.dev/docs/reference/types/textstyle).
### ~~`on_click`~~[​](https://flet.dev/docs/controls/dropdown/#on_click-1 "Direct link to on_click-1")
Fires when this option is clicked.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/dropdown.md)
[PreviousCupertinoTextField](https://flet.dev/docs/controls/cupertinotextfield)[NextDropdownM2](https://flet.dev/docs/controls/dropdownm2)
  * [Examples](https://flet.dev/docs/controls/dropdown/#examples)
    * [Dropdown with colors](https://flet.dev/docs/controls/dropdown/#dropdown-with-colors)
    * [Dropdown with icons](https://flet.dev/docs/controls/dropdown/#dropdown-with-icons)
  * [`Dropdown` properties](https://flet.dev/docs/controls/dropdown/#dropdown-properties)
    * [`autofocus`](https://flet.dev/docs/controls/dropdown/#autofocus)
    * [`bgcolor`](https://flet.dev/docs/controls/dropdown/#bgcolor)
    * [`border`](https://flet.dev/docs/controls/dropdown/#border)
    * [`border_color`](https://flet.dev/docs/controls/dropdown/#border_color)
    * [`border_radius`](https://flet.dev/docs/controls/dropdown/#border_radius)
    * [`border_width`](https://flet.dev/docs/controls/dropdown/#border_width)
    * [`color`](https://flet.dev/docs/controls/dropdown/#color)
    * [`content_padding`](https://flet.dev/docs/controls/dropdown/#content_padding)
    * [`dense`](https://flet.dev/docs/controls/dropdown/#dense)
    * [`elevation`](https://flet.dev/docs/controls/dropdown/#elevation)
    * [`enable_filter`](https://flet.dev/docs/controls/dropdown/#enable_filter)
    * [`enable_search`](https://flet.dev/docs/controls/dropdown/#enable_search)
    * [`error_style`](https://flet.dev/docs/controls/dropdown/#error_style)
    * [`error_text`](https://flet.dev/docs/controls/dropdown/#error_text)
    * [`filled`](https://flet.dev/docs/controls/dropdown/#filled)
    * [`fill_color`](https://flet.dev/docs/controls/dropdown/#fill_color)
    * [`focused_border_color`](https://flet.dev/docs/controls/dropdown/#focused_border_color)
    * [`focused_border_width`](https://flet.dev/docs/controls/dropdown/#focused_border_width)
    * [`helper_style`](https://flet.dev/docs/controls/dropdown/#helper_style)
    * [`helper_text`](https://flet.dev/docs/controls/dropdown/#helper_text)
    * [`hint_style`](https://flet.dev/docs/controls/dropdown/#hint_style)
    * [`hint_text`](https://flet.dev/docs/controls/dropdown/#hint_text)
    * [`label`](https://flet.dev/docs/controls/dropdown/#label)
    * [`label_style`](https://flet.dev/docs/controls/dropdown/#label_style)
    * [`leading_icon`](https://flet.dev/docs/controls/dropdown/#leading_icon)
    * [`menu_height`](https://flet.dev/docs/controls/dropdown/#menu_height)
    * [`menu_width`](https://flet.dev/docs/controls/dropdown/#menu_width)
    * [`options`](https://flet.dev/docs/controls/dropdown/#options)
    * [`selected_trailing_icon`](https://flet.dev/docs/controls/dropdown/#selected_trailing_icon)
    * [`text_align`](https://flet.dev/docs/controls/dropdown/#text_align)
    * [`text_size`](https://flet.dev/docs/controls/dropdown/#text_size)
    * [`text_style`](https://flet.dev/docs/controls/dropdown/#text_style)
    * [`trailing_icon`](https://flet.dev/docs/controls/dropdown/#trailing_icon)
    * [`width`](https://flet.dev/docs/controls/dropdown/#width)
    * [`value`](https://flet.dev/docs/controls/dropdown/#value)
  * [`Dropdown` methods](https://flet.dev/docs/controls/dropdown/#dropdown-methods)
    * [`focus()`](https://flet.dev/docs/controls/dropdown/#focus)
  * [`Dropdown` events](https://flet.dev/docs/controls/dropdown/#dropdown-events)
    * [`on_blur`](https://flet.dev/docs/controls/dropdown/#on_blur)
    * [`on_change`](https://flet.dev/docs/controls/dropdown/#on_change)
    * [`on_focus`](https://flet.dev/docs/controls/dropdown/#on_focus)
  * [Deprecated `Dropdown` properties and events](https://flet.dev/docs/controls/dropdown/#deprecated-dropdown-properties-and-events)
    * [~~`alignment`~~](https://flet.dev/docs/controls/dropdown/#alignment)
    * [~~`counter`~~](https://flet.dev/docs/controls/dropdown/#counter)
    * [~~`counter_style`~~](https://flet.dev/docs/controls/dropdown/#counter_style)
    * [~~`counter_text`~~](https://flet.dev/docs/controls/dropdown/#counter_text)
    * [~~`disabled_hint_content`~~](https://flet.dev/docs/controls/dropdown/#disabled_hint_content)
    * [~~`enable_feedback`~~](https://flet.dev/docs/controls/dropdown/#enable_feedback)
    * [~~`focused_bgcolor`~~](https://flet.dev/docs/controls/dropdown/#focused_bgcolor)
    * [~~`focused_color`~~](https://flet.dev/docs/controls/dropdown/#focused_color)
    * [~~`hint_content`~~](https://flet.dev/docs/controls/dropdown/#hint_content)
    * [~~`icon`~~](https://flet.dev/docs/controls/dropdown/#icon)
    * [~~`icon_content`~~](https://flet.dev/docs/controls/dropdown/#icon_content)
    * [~~`icon_enabled_color`~~](https://flet.dev/docs/controls/dropdown/#icon_enabled_color)
    * [~~`icon_disabled_color`~~](https://flet.dev/docs/controls/dropdown/#icon_disabled_color)
    * [~~`icon_size`~~](https://flet.dev/docs/controls/dropdown/#icon_size)
    * [~~`item_height`~~](https://flet.dev/docs/controls/dropdown/#item_height)
    * [~~`max_menu_height`~~](https://flet.dev/docs/controls/dropdown/#max_menu_height)
    * [~~`options_fill_horizontally`~~](https://flet.dev/docs/controls/dropdown/#options_fill_horizontally)
    * [~~`padding`~~](https://flet.dev/docs/controls/dropdown/#padding)
    * [~~`prefix`~~](https://flet.dev/docs/controls/dropdown/#prefix)
    * [~~`prefix_icon`~~](https://flet.dev/docs/controls/dropdown/#prefix_icon)
    * [~~`prefix_style`~~](https://flet.dev/docs/controls/dropdown/#prefix_style)
    * [~~`prefix_text`~~](https://flet.dev/docs/controls/dropdown/#prefix_text)
    * [~~`select_icon`~~](https://flet.dev/docs/controls/dropdown/#select_icon)
    * [~~`select_icon_enabled_color`~~](https://flet.dev/docs/controls/dropdown/#select_icon_enabled_color)
    * [~~`select_icon_disabled_color`~~](https://flet.dev/docs/controls/dropdown/#select_icon_disabled_color)
    * [~~`select_icon_size`~~](https://flet.dev/docs/controls/dropdown/#select_icon_size)
    * [~~`suffix`~~](https://flet.dev/docs/controls/dropdown/#suffix)
    * [~~`suffix_icon`~~](https://flet.dev/docs/controls/dropdown/#suffix_icon)
    * [~~`suffix_style`~~](https://flet.dev/docs/controls/dropdown/#suffix_style)
    * [~~`suffix_text`~~](https://flet.dev/docs/controls/dropdown/#suffix_text)
    * [~~`on_click`~~](https://flet.dev/docs/controls/dropdown/#on_click)
  * [`DropdownOption`properties](https://flet.dev/docs/controls/dropdown/#dropdownoption-properties)
    * [`content`](https://flet.dev/docs/controls/dropdown/#content)
    * [`key`](https://flet.dev/docs/controls/dropdown/#key)
    * [`leading_icon`](https://flet.dev/docs/controls/dropdown/#leading_icon-1)
    * [`style`](https://flet.dev/docs/controls/dropdown/#style)
    * [`text`](https://flet.dev/docs/controls/dropdown/#text)
    * [`trailing_icon`](https://flet.dev/docs/controls/dropdown/#trailing_icon-1)
  * [Deprecated `DropdownOption` properties and events](https://flet.dev/docs/controls/dropdown/#deprecated-dropdownoption-properties-and-events)
    * [~~`alignment`~~](https://flet.dev/docs/controls/dropdown/#alignment-1)
    * [~~`text_style`~~](https://flet.dev/docs/controls/dropdown/#text_style-1)
    * [~~`on_click`~~](https://flet.dev/docs/controls/dropdown/#on_click-1)


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
