[Skip to main content](https://flet.dev/blog/flet-v-0-24-release-announcement/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
All posts
### 2025
  * [Introducing Flet 1.0 Alpha](https://flet.dev/blog/introducing-flet-1-0-alpha)
  * [Tap into native Android and iOS APIs with Pyjnius and Pyobjus](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus)
  * [Flet v0.27.0 Release Announcement](https://flet.dev/blog/flet-v-0-27-release-announcement)
  * [Flet v0.26.0 Release Announcement](https://flet.dev/blog/flet-v-0-26-release-announcement)


### 2024
  * [Flet v0.25.0 Release Announcement](https://flet.dev/blog/flet-v-0-25-release-announcement)
  * [pyproject.toml support for flet build command](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command)
  * [Flet new packaging pre-release](https://flet.dev/blog/flet-new-packaging-pre-release)
  * [Flet v0.24.0 Release Announcement](https://flet.dev/blog/flet-v-0-24-release-announcement)
  * [Flet v0.23.0 Release Announcement](https://flet.dev/blog/flet-v-0-23-release-announcement)
  * [Flet at PyCon US 2024](https://flet.dev/blog/flet-at-pycon-us-2024)
  * [Flet packaging update](https://flet.dev/blog/flet-packaging-update)
  * [Controls and theming enhancements](https://flet.dev/blog/controls-and-theming-enhancements)
  * [Flet FastAPI and async API improvements](https://flet.dev/blog/flet-fastapi-and-async-api-improvements)
  * [Flet adaptive UI and custom controls release](https://flet.dev/blog/flet-adaptive-and-custom-controls)


### 2023
  * [Packaging apps for distribution](https://flet.dev/blog/packaging-apps-for-distribution)
  * [Flet for FastAPI](https://flet.dev/blog/flet-for-fastapi)
  * [Flet for Android](https://flet.dev/blog/flet-for-android)
  * [Flet for iOS](https://flet.dev/blog/flet-for-ios)
  * [Scrolling controls and Theming](https://flet.dev/blog/scrolling-controls-and-theming)
  * [Canvas](https://flet.dev/blog/canvas)
  * [Flet Charts](https://flet.dev/blog/flet-charts)
  * [Standalone Flet web apps with Pyodide](https://flet.dev/blog/standalone-flet-web-apps-with-pyodide)
  * [Packaging desktop apps with a custom icon](https://flet.dev/blog/packaging-desktop-apps-with-custom-icon)


### 2022
  * [Flet mobile update](https://flet.dev/blog/flet-mobile-update)
  * [Flet versioning and pre-releases](https://flet.dev/blog/flet-versioning-and-pre-releases)
  * [ResponsiveRow and mobile controls](https://flet.dev/blog/responsive-row-and-mobile-controls)
  * [Matplotlib and Plotly charts](https://flet.dev/blog/matplotlib-and-plotly-charts)
  * [Gesture detector](https://flet.dev/blog/gesture-detector)
  * [User authentication](https://flet.dev/blog/user-authentication)
  * [File picker and uploads](https://flet.dev/blog/file-picker-and-uploads)
  * [Fun with animations](https://flet.dev/blog/fun-with-animations)
  * [Beautiful gradients, button styles and TextField rounded corners in a new Flet release](https://flet.dev/blog/gradients-button-textfield-styles)
  * [Control Refs](https://flet.dev/blog/control-refs)
  * [Flet Mobile Strategy](https://flet.dev/blog/flet-mobile-strategy)
  * [Navigation and Routing](https://flet.dev/blog/navigation-and-routing)
  * [New release: Drag and Drop, absolute positioning and clickable container](https://flet.dev/blog/drag-and-drop-release)
  * [Using custom fonts in a Flet app](https://flet.dev/blog/using-custom-fonts-in-flet-app)
  * [Introducing Flet](https://flet.dev/blog/introducing-flet)


# Flet v0.24.0 Release Announcement
August 31, 2024 · 6 min read
[![Henri Ndonko](https://avatars.githubusercontent.com/u/98978078?v=4)](https://github.com/ndonkoHenri)
[Henri Ndonko](https://github.com/ndonkoHenri)
Flet Contributor and Maintainer
[](https://github.com/ndonkoHenri "GitHub")[](https://x.com/ndonkoHenri "X")
I am very happy to announce the release of Flet version 0.24.0! It comes with a very long list of bug fixes, several enhancements and new features.
## New Controls[​](https://flet.dev/blog/flet-v-0-24-release-announcement/#new-controls "Direct link to New Controls")
  * [`InteractiveViewer`](https://flet.dev/docs/controls/interactiveviewer)
  * [`Placeholder`](https://flet.dev/docs/controls/placeholder)


## New Properties[​](https://flet.dev/blog/flet-v-0-24-release-announcement/#new-properties "Direct link to New Properties")
  * [`AudioRecorder`](https://flet.dev/docs/controls/audiorecorder): `cancel_recording()`
  * [`Video`](https://flet.dev/docs/controls/video): `on_completed`, `on_track_changed`
  * [`InputFilter`](https://flet.dev/docs/reference/types/inputfilter): `unicode`, `case_sensitive`, `dot_all`, `multiline`
  * [`Geolocator`](https://flet.dev/docs/controls/geolocator): `on_error`, `on_position_change`
  * [`Barchart`](https://flet.dev/docs/controls/barchart), [`LineChart`](https://flet.dev/docs/controls/linechart): `tooltip_border_side`, `tooltip_direction`, `tooltip_fit_inside_horizontally`, `tooltip_fit_inside_vertically`, `tooltip_horizontal_offset`, `tooltip_margin`, `tooltip_max_content_width`, `tooltip_padding`, `tooltip_rounded_radius`, `tooltip_rotate_angle`
  * [`Container`](https://flet.dev/docs/controls/container): `decoration`, `foreground_decoration`, `ignore_interactions`, `image`
  * [`Page`](https://flet.dev/docs/controls/page), [`View`](https://flet.dev/docs/controls/view): `decoration`, `foreground_decoration`
  * [`CupertinoTextField`](https://flet.dev/docs/controls/cupertinotextfield): `enable_scribble`, `image`, `obscuring_character`, `padding`, `scroll_padding`, `on_click`
  * [`DataTable`](https://flet.dev/docs/controls/datatable): `heading_row_alignment`
  * [`TextField`](https://flet.dev/docs/controls/textfield): `counter`, `disabled_hint_content`, `options_fill_horizontally`
  * [`ExpansionTile`](https://flet.dev/docs/controls/expansiontile): `min_tile_height`, `show_trailing_icon`
  * [`Markdown`](https://flet.dev/docs/controls/markdown): `fit_content`, `img_error_content`, `md_style_sheet`, `shrink_wrap`, `soft_line_break`, `on_selection_change`
  * [`MenuItemButton`](https://flet.dev/docs/controls/menuitembutton): `autofocus`, `overflow_axis`, `semantic_label`
  * [`Tabs`](https://flet.dev/docs/controls/tabs): `label_padding`, `label_text_style`, `padding`, `splash_border_radius`, `unselected_label_text_style`, `on_click`
  * and lot of [new classes](https://flet.dev/docs/reference) (enums, dataclasses, events)…


## Enhancements[​](https://flet.dev/blog/flet-v-0-24-release-announcement/#enhancements "Direct link to Enhancements")
  * Better string output of Events when printed
  * `Image.filter_quality` now has a default of `FilterQuality.MEDIUM` (previously `FilterQuality.LOW`), which is a better default for downscaled images.
  * `Geolocator` control has been improved to support location streaming through the newly added on_position_change event. When defined, you will be able to "listen" to location changes as they happen.
  * When `AppBar.adaptive=True` and the app is running on an Apple platform, the `AppBar.actions` controls are now wrapped in a `Row`, then displayed. Before this, only the first item of `AppBar.actions` list was displayed.
  * The `Markdown` control has been significantly improved. It can now display SVG images and be much more customized.
  * A very requested feature was the ability to set a background image or gradient for the application. In [#3820](https://github.com/flet-dev/flet/pull/3820), we made this possible and easy to use.
  * rtl (right-to-left) property has been added to more controls (`NavigationRailDestination`, `NavigationRail`, `AppBar`, `CupertinoAppBar`, and `NavigationDrawer` ) to improve support for right-to-left text directions.
  * Introduced `--no-rich-output` flag (only in `flet build` command for now) to make it possible to disable rich output (mainly emojis) in the console. More information in [#3708](https://github.com/flet-dev/flet/pull/3708).
  * Typing has been significantly improved, particularly for event-handler properties. In modern IDEs like PyCharm and VSCode, you can now easily determine the type of an event handler's argument by simply hovering over the event in the control. Additionally, the IDE will highlight errors when you attempt to access a non-existent property on the event handler argument, ensuring more robust and error-free code.


## Bug Fixes[​](https://flet.dev/blog/flet-v-0-24-release-announcement/#bug-fixes "Direct link to Bug Fixes")
The below issues were successfully fixed:
  * [#3769](https://github.com/flet-dev/flet/issues/3769): `InputFilter` clears the `TextField` text content when an invalid character is entered
  * [#3770](https://github.com/flet-dev/flet/issues/3770): `Theme.floating_action_button_theme` non existent
  * [#3734](https://github.com/flet-dev/flet/issues/3734): Ensure `Dropdown.alignment` is respected.
  * [#3730](https://github.com/flet-dev/flet/issues/3730): `UnicodeEncodeError` raised when packaging on WindowOS
  * [#2160](https://github.com/flet-dev/flet/issues/2160): `Markdown` control can't render svg images
  * [#2158](https://github.com/flet-dev/flet/issues/2158): `Markdown` broken when an image is not found
  * [#3679](https://github.com/flet-dev/flet/issues/3679): Broken `Dismissible`
  * [#3670](https://github.com/flet-dev/flet/issues/3670): `Switch.height` and `Switch.width` not respected
  * [#3612](https://github.com/flet-dev/flet/issues/3612), [#3566](https://github.com/flet-dev/flet/issues/3566): Broken `OnScrollEvent`
  * [#3564](https://github.com/flet-dev/flet/issues/3564): Broken `TextField.capitalization`
  * [#3649](https://github.com/flet-dev/flet/issues/3649): `CupertinoPicker` jumps-scroll on some platforms
  * [#3557](https://github.com/flet-dev/flet/issues/3557): Impeller causes blank screen on mac Intel
  * [#3574](https://github.com/flet-dev/flet/issues/3574): `Geolocator` not working on Android devices
  * [#3505](https://github.com/flet-dev/flet/issues/3505): `WindowEventType` doesn't contain fullscreen all events


Thanks to all those who reported them!
## Deprecations[​](https://flet.dev/blog/flet-v-0-24-release-announcement/#deprecations "Direct link to Deprecations")
All deprecated items from this release will be removed in version 0.27.0.
  * `ThemeVisualDensity` is deprecated and has been renamed to [`VisualDensity`](https://flet.dev/docs/reference/types/visualdensity)
  * [`CupertinoButton`](https://flet.dev/docs/controls/cupertinobutton): `disabled_color` is deprecated and has been renamed to `disabled_bgcolor`, which better reflects its use
  * [`Markdown`](https://flet.dev/docs/controls/markdown): `code_style` is deprecated and should now be accessed as `code_style_sheet.code_text_style`
  * [`Container`](https://flet.dev/docs/controls/container): `image_fit`, `image_opacity`, `image_repeat`, `image_src` and `image_src_base64` are deprecated and should now be accessed from `image` which is of type [`DecorationImage`](https://flet.dev/docs/reference/types/decorationimage)


## Breaking Changes and Migration[​](https://flet.dev/blog/flet-v-0-24-release-announcement/#breaking-changes-and-migration "Direct link to Breaking Changes and Migration")
### Tooltip[​](https://flet.dev/blog/flet-v-0-24-release-announcement/#tooltip "Direct link to Tooltip")
The Tooltip class is no more a Flet control and is from now on a simple Python dataclass. The tooltip property (available in almost all controls) now supports both strings and Tooltip objects.
Below is how to migrate:
```
# beforepage.add(  ft.Tooltip(    message="This is tooltip",    content=ft.Text("Hover to see tooltip"),    padding=20,    border_radius=10,))# afterpage.add(  ft.Text("Hover to see tooltip",    tooltip=ft.Tooltip(      message="This is tooltip",      padding=20,      border_radius=10,)))
```

### TextField InputFilter[​](https://flet.dev/blog/flet-v-0-24-release-announcement/#textfield-inputfilter "Direct link to TextField InputFilter")
We modified how `InputFilter.regex_string` is internally handled. As a result of this, you (might) now have to anchor your regex pattern. This simply implies using start (^) and end ($) regex anchors. For example: `r"[0-9]"` now becomes `r"^[0-9]$"`. Using this new string will lead work as expected and only numbers/digits will be allowed, but you might notice another issue: the last character of the text field cannot be deleted. To resolve this, you need to add an asterisk (*) in the regex which in this case will simply mean "match zero or more digits (including an empty string)". The new regex now becomes `r"^[0-9]*$"`. To ease this migration, you can use an AI tool with the following simple prompt: `"update the following regex pattern: #### ensuring that the entire string matches the pattern and it allows for an empty string"`.
### Event-Handler subscription[​](https://flet.dev/blog/flet-v-0-24-release-announcement/#event-handler-subscription "Direct link to Event-Handler subscription")
The possibility to "subscribe" more than one callback to an event handler has been removed, as this was somehow biased (was only possible on some, and not all). Below is a simple example:
```
import flet as ftdefmain(page: ft.Page):defprint_one(e):print("1")defprint_two(e):print("2")defprint_three(e):print("3")  c = ft.Container(    bgcolor=ft.Colors.random_color(),    width=300,    height=300,)# subscribe callbacks  c.on_tap_down = print_one  c.on_tap_down = print_two  c.on_tap_down = print_three  page.add(c)ft.app(main)
```

In the above code, we subscribe multiple callbacks to the [`Container.on_tap_down`](https://flet.dev/docs/controls/container#on_tap_down) event. Prior to Flet version 0.24.0, running this code and tapping on the `Container`, you will see all the callbacks getting called ("1", "2" and "3" are printed out). From Flet version 0.24.0 going forward, one event = one callback. Meaning only the lastly subscribed callback will get executed ("3" is printed out) So, if you still want the final output to resemble the first one you can simply create one callback which calls the others:
```
defmain(page: ft.Page):#....defprint_all(e):      print_one(e)      print_two(e)      print_three(e)  c = ft.Container(      bgcolor=ft.Colors.random_color(),      width=300,      height=300,      on_tap_down=print_all,)# OR  c.on_tap_down = print_all
```

## Conclusion[​](https://flet.dev/blog/flet-v-0-24-release-announcement/#conclusion "Direct link to Conclusion")
As you can see, we made a lot of changes in this release and as usual, your feedback is highly welcomed!
Upgrade to Flet 0.24.0, test your apps and let us know how you find the new features we added. If you have any questions, please join [Flet Discord server](https://discord.gg/dzWXP8SHG8) or create a new thread on [Flet GitHub discussions](https://github.com/flet-dev/flet/discussions).
Happy Flet-ing! 👾
**Tags:**
  * [releases](https://flet.dev/blog/tags/releases)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2024-08-31-flet-v-0-24-release-announcement.md)
[Newer postFlet new packaging pre-release](https://flet.dev/blog/flet-new-packaging-pre-release)[Older postFlet v0.23.0 Release Announcement](https://flet.dev/blog/flet-v-0-23-release-announcement)
  * [New Controls](https://flet.dev/blog/flet-v-0-24-release-announcement/#new-controls)
  * [New Properties](https://flet.dev/blog/flet-v-0-24-release-announcement/#new-properties)
  * [Enhancements](https://flet.dev/blog/flet-v-0-24-release-announcement/#enhancements)
  * [Bug Fixes](https://flet.dev/blog/flet-v-0-24-release-announcement/#bug-fixes)
  * [Deprecations](https://flet.dev/blog/flet-v-0-24-release-announcement/#deprecations)
  * [Breaking Changes and Migration](https://flet.dev/blog/flet-v-0-24-release-announcement/#breaking-changes-and-migration)
    * [Tooltip](https://flet.dev/blog/flet-v-0-24-release-announcement/#tooltip)
    * [TextField InputFilter](https://flet.dev/blog/flet-v-0-24-release-announcement/#textfield-inputfilter)
    * [Event-Handler subscription](https://flet.dev/blog/flet-v-0-24-release-announcement/#event-handler-subscription)
  * [Conclusion](https://flet.dev/blog/flet-v-0-24-release-announcement/#conclusion)


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
