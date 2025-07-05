[Skip to main content](https://flet.dev/blog/drag-and-drop-release/#__docusaurus_skipToContent_fallback)
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


# New release: Drag and Drop, absolute positioning and clickable container
July 14, 2022 · 2 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
We have just released [Flet 0.1.41](https://pypi.org/project/flet/0.1.41/) with drag-and-drop support and other neat features such as absolute positioning of controls inside stack and clickable container!
## Drag and Drop[​](https://flet.dev/blog/drag-and-drop-release/#drag-and-drop "Direct link to Drag and Drop")
Making drag-and-drop in Flet is a real joy - thanks to a smart drag-and-drop implementation in Flutter! You just have "draggable" control which could be dragged to a "drag target" which calls `on_accept` event handler when draggable is dropped.
![](https://flet.dev/img/docs/controls/drag-and-drop/drag-and-drop-colors.gif)
Take a look at [Drag-and-Drop example](https://github.com/flet-dev/examples/blob/main/python/controls/drag-and-drop/drag-drop-colors.py).
Explore [`Draggable`](https://flet.dev/docs/controls/draggable) and [`DragTarget`](https://flet.dev/docs/controls/dragtarget) controls, their properties and events.
## Absolute positioning inside Stack[​](https://flet.dev/blog/drag-and-drop-release/#absolute-positioning-inside-stack "Direct link to Absolute positioning inside Stack")
All visible controls now have `left` `top`, `right` and `bottom` properties to let them be absolutely positioned inside [`Stack`](https://flet.dev/docs/controls/stack), for example:
```
import flet as ftdefmain(page: ft.Page):  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  page.vertical_alignment = ft.MainAxisAlignment.CENTER  page.add(    ft.Container(      ft.Stack([          ft.Text("1", color=ft.Colors.WHITE),          ft.Text("2", color=ft.Colors.WHITE, right=0),          ft.Text("3", color=ft.Colors.WHITE, right=0, bottom=0),          ft.Text("4", color=ft.Colors.WHITE, left=0, bottom=0),          ft.Text("5", color=ft.Colors.WHITE, left=40, top=35),]),      border_radius=8,      padding=5,      width=100,      height=100,      bgcolor=ft.Colors.BROWN_700,))ft.app(target=main)
```

![](https://flet.dev/img/blog/drag-and-drop/absolute-positioned-numbers.png)
## Clickable container[​](https://flet.dev/blog/drag-and-drop-release/#clickable-container "Direct link to Clickable container")
[`Container`](https://flet.dev/docs/controls/container) control has got `on_click` event which allows you to make a button from any control and with a beautiful material ripple effect when `ink` is set to `True`!
![](https://flet.dev/img/docs/controls/container/clickable-container.gif)
See [source code](https://github.com/flet-dev/examples/blob/main/python/controls/container/clickable-container.py) for the example above.
[Give Flet a try](https://flet.dev/docs) and [let us know](https://discord.gg/dzWXP8SHG8) what you think!
**Tags:**
  * [release](https://flet.dev/blog/tags/release)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2022-07-14-drag-and-drop-release.md)
[Newer postNavigation and Routing](https://flet.dev/blog/navigation-and-routing)[Older postUsing custom fonts in a Flet app](https://flet.dev/blog/using-custom-fonts-in-flet-app)
  * [Drag and Drop](https://flet.dev/blog/drag-and-drop-release/#drag-and-drop)
  * [Absolute positioning inside Stack](https://flet.dev/blog/drag-and-drop-release/#absolute-positioning-inside-stack)
  * [Clickable container](https://flet.dev/blog/drag-and-drop-release/#clickable-container)


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
