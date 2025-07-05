[Skip to main content](https://flet.dev/blog/flet-v-0-23-release-announcement/#__docusaurus_skipToContent_fallback)
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


# Flet v0.23.0 Release Announcement
June 18, 2024 · 3 min read
[![Henri Ndonko](https://avatars.githubusercontent.com/u/98978078?v=4)](https://github.com/ndonkoHenri)
[Henri Ndonko](https://github.com/ndonkoHenri)
Flet Contributor and Maintainer
[](https://github.com/ndonkoHenri "GitHub")[](https://x.com/ndonkoHenri "X")
We are excited to announce the release of Flet 0.23.0. It is a big release with many new features and bug fixes.
## New Controls[​](https://flet.dev/blog/flet-v-0-23-release-announcement/#new-controls "Direct link to New Controls")
  * [`AutoComplete`](https://flet.dev/docs/controls/autocomplete)
  * [`AutoFillGroup`](https://flet.dev/docs/controls/autofillgroup)
  * [`Flashlight`](https://flet.dev/docs/controls/flashlight)
  * [`Geolocator`](https://flet.dev/docs/controls/geolocator)
  * [`Map`](https://flet.dev/docs/controls/map)
  * [`PermissionHandler`](https://flet.dev/docs/controls/permissionhandler)


## New Properties[​](https://flet.dev/blog/flet-v-0-23-release-announcement/#new-properties "Direct link to New Properties")
  * [`Option`](https://flet.dev/docs/controls/dropdown#dropdownoption-properties): `content`, `text_style`
  * [`TextStyle`](https://flet.dev/docs/reference/types/textstyle): `baseline`, `overflow`, `word_spacing`


## Error Handling[​](https://flet.dev/blog/flet-v-0-23-release-announcement/#error-handling "Direct link to Error Handling")
> PEP 20 (Zen of Python): Errors should never pass silently.
Several devs reported that, on some occasions, a control might visually break without clear information on what caused the break.
For example, in issue [#3149](https://github.com/flet-dev/flet/issues/3149), @base-13 mentioned that _"in a DataTable if the number of columns is less than the number of datacells in any row it will grey out whole table without throwing error"_.
Knowing this, we added more assertion-checks in most of the controls, such that, when you provide them with a wrong value, an AssertionError is raised with a very clear message of what was wrongly done.
If you find out that some checks are still missing, please point them out so they can be addressed.
## Command Line (CLI) Output[​](https://flet.dev/blog/flet-v-0-23-release-announcement/#command-line-cli-output "Direct link to Command Line \(CLI\) Output")
The output of the `flet build` command has been prettified.
Also, a new option has been added --show-platform-matrix which displays a table containing the build platform matrix, which has header columns "Command" (possible build commands) and "Platform" (the device you should use with the respective command).
Furthermore, when the targeted platform can't be built on your device, a table displaying the build platform matrix is shown with an informative message.
## Breaking Changes[​](https://flet.dev/blog/flet-v-0-23-release-announcement/#breaking-changes "Direct link to Breaking Changes")
While doing "Error Handling" mentioned above, we had to mark some important properties as required.
The following properties are now "required" (must be provided and visible) when creating an instance of their classes:
  * [`AnimatedSwitcher.content`](https://flet.dev/docs/controls/animatedswitcher#content)
  * [`Banner.content`](https://flet.dev/docs/controls/banner#content), [`Banner.actions`](https://flet.dev/docs/controls/banner#actions)
  * [`BottomSheet.content`](https://flet.dev/docs/controls/bottomsheet#content)
  * [`CupertinoActionSheetAction.content`](https://flet.dev/docs/controls/cupertinoactionsheetaction#content)
  * [`DataRow.cells`](https://flet.dev/docs/controls/datatable)
  * [`DataTable.columns`](https://flet.dev/docs/controls/datatable)
  * [`DragTarget.content`](https://flet.dev/docs/controls/dragtarget#content)
  * [`Draggable.content`](https://flet.dev/docs/controls/draggable#content)
  * [`ExpansionTile.title`](https://flet.dev/docs/controls/expansiontile#title)
  * [`MenuBar.controls`](https://flet.dev/docs/controls/menubar#controls)
  * [`Pagelet.content`](https://flet.dev/docs/controls/pagelet#content)
  * [`RadioGroup.content`](https://flet.dev/docs/controls/radio#content)
  * [`SafeArea.content`](https://flet.dev/docs/controls/safearea#content)
  * [`ShaderMask.shader`](https://flet.dev/docs/controls/shadermask#shader)
  * [`WindowDragArea.content`](https://flet.dev/docs/controls/windowdragarea#content)


## Bug Fixes[​](https://flet.dev/blog/flet-v-0-23-release-announcement/#bug-fixes "Direct link to Bug Fixes")
The below issues were successfully fixed:
  * [#3144](https://github.com/flet-dev/flet/issues/3144): `ScrollbarTheme.thickness` value not respected when not interacting with
  * [#3072](https://github.com/flet-dev/flet/issues/3072): High-resolution videos play laggy on Android TV devices.
  * [#3023](https://github.com/flet-dev/flet/issues/3023): (Regression) Some `LineChart` colors not visually respected
  * [#2989](https://github.com/flet-dev/flet/issues/2989): Color of [`Dropdown`](https://flet.dev/docs/controls/dropdown) when disabled doesn't reflect its disabled state
  * [#1753](https://github.com/flet-dev/flet/issues/1753): [`Markdown`](https://flet.dev/docs/controls/markdown) code block not selectable
  * [#3097](https://github.com/flet-dev/flet/issues/3097): Hot-reload occurs when a file is opened
  * [#1647](https://github.com/flet-dev/flet/issues/1647): [`Container.theme_mode`](https://flet.dev/docs/controls/container#theme_mode) not honoured when `Container.theme=None`
  * [#3064](https://github.com/flet-dev/flet/issues/3064): [`Container.on_tap_down`](https://flet.dev/docs/controls/container#on_tap_down) not called when `Container.on_click=None`


Special Thanks to the dynamic Flet community for reporting all the issues they encountered. We keep working hard on solving the remaining ones.
## Deprecations[​](https://flet.dev/blog/flet-v-0-23-release-announcement/#deprecations "Direct link to Deprecations")
  * All the `Page.window_***` properties are now deprecated and moved to [`Page.window`](https://flet.dev/docs/controls/page#window) property, which is of type [`Window`](https://flet.dev/docs/reference/types/window). To migrate, simply use change `window_` to `window.` as seen below:
```
# before page.window_height =200page.on_window_event =lambda e:print(e.type)# nowpage.window.height =200page.window.on_event =lambda e:print(e.type)
```

  * `SafeArea.minimum` is deprecated and has been renamed to [`minimum_padding`](https://flet.dev/docs/controls/safearea#minimum_padding)
  * `MaterialState` enum is deprecated and has been renamed to [`ControlState`](https://flet.dev/docs/reference/types/controlstate)
  * `NavigationDestination` is deprecated and has been renamed to [`NavigationBarDestination`](https://flet.dev/docs/controls/navigationbar#navigationbardestination-properties)


Also, the deprecation policy has been modified. While Flet is pre-1.0, all deprecations will be removed from the API after the next 3 releases. So the above deprecations made in v0.23.0 (and all the other deprecations made in the previous versions), will be removed in v0.26.0.
That's it! :)
Upgrade to Flet 0.23.0, test your apps and let us know how you find the new features we added. If you have any questions, please join [Flet Discord server](https://discord.gg/dzWXP8SHG8) or create a new thread on [Flet GitHub discussions](https://github.com/flet-dev/flet/discussions).
Happy Flet-ing!
**Tags:**
  * [releases](https://flet.dev/blog/tags/releases)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2024-06-18-flet-v-0-23-release-announcement.md)
[Newer postFlet v0.24.0 Release Announcement](https://flet.dev/blog/flet-v-0-24-release-announcement)[Older postFlet at PyCon US 2024](https://flet.dev/blog/flet-at-pycon-us-2024)
  * [New Controls](https://flet.dev/blog/flet-v-0-23-release-announcement/#new-controls)
  * [New Properties](https://flet.dev/blog/flet-v-0-23-release-announcement/#new-properties)
  * [Error Handling](https://flet.dev/blog/flet-v-0-23-release-announcement/#error-handling)
  * [Command Line (CLI) Output](https://flet.dev/blog/flet-v-0-23-release-announcement/#command-line-cli-output)
  * [Breaking Changes](https://flet.dev/blog/flet-v-0-23-release-announcement/#breaking-changes)
  * [Bug Fixes](https://flet.dev/blog/flet-v-0-23-release-announcement/#bug-fixes)
  * [Deprecations](https://flet.dev/blog/flet-v-0-23-release-announcement/#deprecations)


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
