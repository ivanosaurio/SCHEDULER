[Skip to main content](https://flet.dev/blog/responsive-row-and-mobile-controls/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search
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


# ResponsiveRow and mobile controls
November 13, 2022 · 3 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
We just released [Flet 0.1.65](https://pypi.org/project/flet/0.1.65/) which is adding a bunch of mobile-optimized controls, fixing some bugs and introducing a new layout control - `ResponsiveRow`.
## `ResponsiveRow` control[​](https://flet.dev/blog/responsive-row-and-mobile-controls/#responsiverow-control "Direct link to responsiverow-control")
`ResponsiveRow` borrows the idea of grid layout from [Bootstrap](https://getbootstrap.com/docs/5.2/layout/grid/) web framework.
`ResponsiveRow` allows aligning child controls to virtual columns. By default, a virtual grid has 12 columns, but that can be customized with `ResponsiveRow.columns` property.
Similar to `expand` property every control now has `col` property which allows specifying how many columns a control should span. For example, to make a layout consisting of two columns spanning 6 virtual columns each:
```
import flet as ftft.ResponsiveRow([  ft.Column(col=6, controls=ft.Text("Column 1")),  ft.Column(col=6, controls=ft.Text("Column 2"))])
```

`ResponsiveRow` is "responsive" because it can adapt the size of its children to a changing screen (page, window) size. `col` property in the example above is a constant number which means the child will span 6 columns for any screen size.
If `ResponsiveRow`'s child doesn't have `col` property specified it spans the maximum number of columns.
`col` can be configured to have a different value for specific "breakpoints". Breakpoints are named dimension ranges:
Breakpoint| Dimension  
---|---  
xs| <576px  
sm| ≥576px  
md| ≥768px  
lg| ≥992px  
xl| ≥1200px  
xxl| ≥1400px  
For example, the following example collapses content into a single column on a mobile device and takes two columns on larger screens:
```
import flet as ftft.ResponsiveRow([  ft.Column(col={"sm":6}, controls=ft.Text("Column 1")),  ft.Column(col={"sm":6}, controls=ft.Text("Column 2"))])
```

Here is more elaborate example of responsive layout:
![](https://flet.dev/img/docs/controls/responsive-row/responsive-layout.gif)
```
import flet as ftdefmain(page: ft.Page):defpage_resize(e):    pw.value =f"{page.width} px"    pw.update()  page.on_resize = page_resize  pw = ft.Text(bottom=50, right=50, style="displaySmall")  page.overlay.append(pw)  page.add(    ft.ResponsiveRow([        ft.Container(          ft.Text("Column 1"),          padding=5,          bgcolor=ft.Colors.YELLOW,          col={"sm":6,"md":4,"xl":2},),        ft.Container(          ft.Text("Column 2"),          padding=5,          bgcolor=ft.Colors.GREEN,          col={"sm":6,"md":4,"xl":2},),        ft.Container(          ft.Text("Column 3"),          padding=5,          bgcolor=ft.Colors.BLUE,          col={"sm":6,"md":4,"xl":2},),        ft.Container(          ft.Text("Column 4"),          padding=5,          bgcolor=ft.Colors.PINK_300,          col={"sm":6,"md":4,"xl":2},),],),    ft.ResponsiveRow([        ft.TextField(label="TextField 1", col={"md":4}),        ft.TextField(label="TextField 2", col={"md":4}),        ft.TextField(label="TextField 3", col={"md":4}),],      run_spacing={"xs":10},),)  page_resize(None)ft.app(target=main)
```

`ResponsiveRow` [docs](https://flet.dev/docs/controls/responsiverow), [example](https://github.com/flet-dev/examples/blob/main/python/controls/responsive-row/responsive-layout.py).
## Other new controls[​](https://flet.dev/blog/responsive-row-and-mobile-controls/#other-new-controls "Direct link to Other new controls")
This release adds new visual and non-visual controls requested by Flet community and also required to build UI of the upcoming [Flet Studio](https://flet.dev/docs/cookbook/mobile-support#flet-studio-for-ios-and-android).
### BottomSheet[​](https://flet.dev/blog/responsive-row-and-mobile-controls/#bottomsheet "Direct link to BottomSheet")
Shows a modal Material Design bottom sheet:
![](https://flet.dev/img/docs/controls/bottom-sheet/bottom-sheet-sample.gif)
`BottomSheet` [docs](https://flet.dev/docs/controls/bottomsheet), [example](https://github.com/flet-dev/examples/blob/main/python/controls/bottom-sheet/modal-bottom-sheet.py).
### NavigationBar[​](https://flet.dev/blog/responsive-row-and-mobile-controls/#navigationbar "Direct link to NavigationBar")
Bottom Navigation bar which offers a persistent and convenient way to switch between primary destinations in an app:
![](https://flet.dev/img/docs/controls/navigation-bar/navigation-bar-sample.gif)
`NavigationBar` [docs](https://flet.dev/docs/controls/navigationbar), [example](https://github.com/flet-dev/examples/blob/main/python/controls/navigation-bar/navigation-bar-sample.py).
### Tooltip[​](https://flet.dev/blog/responsive-row-and-mobile-controls/#tooltip "Direct link to Tooltip")
A tooltip control:
![](https://flet.dev/img/docs/controls/tooltip/custom-tooltip.gif)
`Tooltip` [docs](https://flet.dev/docs/reference/types/tooltip), [example](https://github.com/flet-dev/examples/blob/main/python/controls/tooltip/custom-tooltip.py).
### HapticFeedback[​](https://flet.dev/blog/responsive-row-and-mobile-controls/#hapticfeedback "Direct link to HapticFeedback")
Allows access to the haptic feedback (clicks and vibrates) interface on the device.
`HapticFeedback` [docs](https://flet.dev/docs/controls/hapticfeedback).
### ShakeDetector[​](https://flet.dev/blog/responsive-row-and-mobile-controls/#shakedetector "Direct link to ShakeDetector")
A control to detect phone shakes. Based on [shake](https://pub.dev/packages/shake) widget.
`ShakeDetector` [docs](https://flet.dev/docs/controls/shakedetector).
## Other improvements[​](https://flet.dev/blog/responsive-row-and-mobile-controls/#other-improvements "Direct link to Other improvements")
### Markdown code syntax highlight[​](https://flet.dev/blog/responsive-row-and-mobile-controls/#markdown-code-syntax-highlight "Direct link to Markdown code syntax highlight")
[Sample code](https://github.com/flet-dev/examples/blob/main/python/controls/markdown/markdown-code-highlight.py).
![](https://flet.dev/img/docs/controls/markdown/markdown-highlight.png)
### Variable fonts support[​](https://flet.dev/blog/responsive-row-and-mobile-controls/#variable-fonts-support "Direct link to Variable fonts support")
Flutter has finally supported [variable fonts](https://fonts.google.com/knowledge/introducing_type/introducing_variable_fonts) and we bring that into Flet too!
[Sample code](https://github.com/flet-dev/examples/blob/main/python/controls/text/variable-weight-font.py).
![](https://flet.dev/img/docs/controls/text/variable-weight-font.gif)
Upgrade Flet module to the latest version (`pip install flet --upgrade`) and [let us know](https://discord.gg/dzWXP8SHG8) what you think!
Enjoy!
**Tags:**
  * [release](https://flet.dev/blog/tags/release)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2022-11-13-responsive-row-and-mobile-controls.md)
[Newer postFlet versioning and pre-releases](https://flet.dev/blog/flet-versioning-and-pre-releases)[Older postMatplotlib and Plotly charts](https://flet.dev/blog/matplotlib-and-plotly-charts)
  * [`ResponsiveRow` control](https://flet.dev/blog/responsive-row-and-mobile-controls/#responsiverow-control)
  * [Other new controls](https://flet.dev/blog/responsive-row-and-mobile-controls/#other-new-controls)
    * [BottomSheet](https://flet.dev/blog/responsive-row-and-mobile-controls/#bottomsheet)
    * [NavigationBar](https://flet.dev/blog/responsive-row-and-mobile-controls/#navigationbar)
    * [Tooltip](https://flet.dev/blog/responsive-row-and-mobile-controls/#tooltip)
    * [HapticFeedback](https://flet.dev/blog/responsive-row-and-mobile-controls/#hapticfeedback)
    * [ShakeDetector](https://flet.dev/blog/responsive-row-and-mobile-controls/#shakedetector)
  * [Other improvements](https://flet.dev/blog/responsive-row-and-mobile-controls/#other-improvements)
    * [Markdown code syntax highlight](https://flet.dev/blog/responsive-row-and-mobile-controls/#markdown-code-syntax-highlight)
    * [Variable fonts support](https://flet.dev/blog/responsive-row-and-mobile-controls/#variable-fonts-support)


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
