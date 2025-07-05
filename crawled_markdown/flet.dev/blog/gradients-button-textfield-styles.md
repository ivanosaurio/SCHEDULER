[Skip to main content](https://flet.dev/blog/gradients-button-textfield-styles/#__docusaurus_skipToContent_fallback)
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


# Beautiful gradients, button styles and TextField rounded corners in a new Flet release
August 4, 2022 · 4 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
We've just released [Flet 0.1.46](https://pypi.org/project/flet/0.1.46/) adding new exciting features:
  * Gradient backgrounds in Container
  * Extensive styling for buttons, TextField and Dropdown controls
  * ...and more


## Gradient backgrounds[​](https://flet.dev/blog/gradients-button-textfield-styles/#gradient-backgrounds "Direct link to Gradient backgrounds")
### Linear gradient[​](https://flet.dev/blog/gradients-button-textfield-styles/#linear-gradient "Direct link to Linear gradient")
![](https://flet.dev/img/blog/gradients/linear-gradient.png)
```
import mathimport flet as ftdefmain(page: ft.Page):  page.add(    ft.Container(      alignment=ft.alignment.center,      gradient=ft.LinearGradient(        begin=ft.alignment.top_left,        end=Alignment(0.8,1),        colors=["0xff1f005c","0xff5b0060","0xff870160","0xffac255e","0xffca485c","0xffe16b5c","0xfff39060","0xffffb56b",],        tile_mode=ft.GradientTileMode.MIRROR,        rotation=math.pi /3,),      width=150,      height=150,      border_radius=5,))ft.app(target=main)
```

Check [`LinearGradient`](https://flet.dev/docs/reference/types/lineargradient) docs for more information about `LinearGradient` properties.
### Radial gradient[​](https://flet.dev/blog/gradients-button-textfield-styles/#radial-gradient "Direct link to Radial gradient")
![](https://flet.dev/img/blog/gradients/radial-gradient.png)
```
import flet as ftdefmain(page: ft.Page):  page.add(    ft.Container(      alignment=ft.alignment.center,      gradient=ft.RadialGradient(        center=Alignment(0.7,-0.6),        radius=0.2,        colors=["0xFFFFFF00",# yellow sun"0xFF0099FF",# blue sky],        stops=[0.4,1.0],),      width=150,      height=150,      border_radius=5,))ft.app(target=main)
```

Check [`RadialGradient`](https://flet.dev/docs/reference/types/radialgradient) docs for more information about `RadialGradient` properties.
### Sweep gradient[​](https://flet.dev/blog/gradients-button-textfield-styles/#sweep-gradient "Direct link to Sweep gradient")
![](https://flet.dev/img/blog/gradients/sweep-gradient.png)
```
import mathimport flet as ftdefmain(page: ft.Page):  page.add(    ft.Container(      alignment=ft.alignment.center,      gradient=SweepGradient(        center=ft.alignment.center,        start_angle=0.0,        end_angle=math.pi *2,        colors=["0xFF4285F4","0xFF34A853","0xFFFBBC05","0xFFEA4335","0xFF4285F4",],        stops=[0.0,0.25,0.5,0.75,1.0],),      width=150,      height=150,      border_radius=5,))ft.app(target=main)
```

Check [`SweepGradient`](https://flet.dev/docs/reference/types/sweepgradient) docs for more information about `SweepGradient` properties.
## Buttons styling[​](https://flet.dev/blog/gradients-button-textfield-styles/#buttons-styling "Direct link to Buttons styling")
This Flet release introduces `style` property to all button controls which is an instance of `ButtonStyle` class. `ButtonStyle` allows controlling all visual aspects of a button, such as shape, foreground, background and shadow colors, content padding, border width and radius!
Moreover, each individual style attribute could be configured for a different "Material states" of a button, such as "hovered", "focused", "disabled" and others. For example, you can configure a different shape, background color for a hovered state and configure fallback values for all other states.
Check this "extreme" styling example:
![](https://flet.dev/img/blog/gradients/styled-button.gif)
```
import flet as ftfrom flet.border import BorderSidefrom flet.buttons import RoundedRectangleBorderdefmain(page: ft.Page):  page.add(    ft.ElevatedButton("Styled button 1",      style=ft.ButtonStyle(        color={          ft.MaterialState.HOVERED: ft.Colors.WHITE,          ft.MaterialState.FOCUSED: ft.Colors.BLUE,          ft.MaterialState.DEFAULT: ft.Colors.BLACK,},        bgcolor={ft.MaterialState.FOCUSED: ft.Colors.PINK_200,"": ft.Colors.YELLOW},        padding={ft.MaterialState.HOVERED:20},        overlay_color=ft.Colors.TRANSPARENT,        elevation={"pressed":0,"":1},        animation_duration=500,        side={          ft.MaterialState.DEFAULT: BorderSide(1, ft.Colors.BLUE),          ft.MaterialState.HOVERED: BorderSide(2, ft.Colors.BLUE),},        shape={          ft.MaterialState.HOVERED: RoundedRectangleBorder(radius=20),          ft.MaterialState.DEFAULT: RoundedRectangleBorder(radius=2),},),))ft.app(target=main)
```

`ft.MaterialState.DEFAULT` state is a fallback style.
Button shape could also be changed with `ButtonStyle.shape` property:
![](https://flet.dev/img/blog/gradients/button-shapes.png)
```
import flet as ftfrom flet.buttons import(  BeveledRectangleBorder,  CircleBorder,  ContinuousRectangleBorder,  RoundedRectangleBorder,  StadiumBorder,)defmain(page: ft.Page):  page.padding =30  page.spacing =30  page.add(    ft.FilledButton("Stadium",      style=ft.ButtonStyle(        shape=ft.StadiumBorder(),),),    ft.FilledButton("Rounded rectangle",      style=ft.ButtonStyle(        shape=ft.RoundedRectangleBorder(radius=10),),),    ft.FilledButton("Continuous rectangle",      style=ft.ButtonStyle(        shape=ft.ContinuousRectangleBorder(radius=30),),),    ft.FilledButton("Beveled rectangle",      style=ft.ButtonStyle(        shape=ft.BeveledRectangleBorder(radius=10),),),    ft.FilledButton("Circle",      style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30),),)ft.app(target=main)
```

Check [`ElevatedButton.style`](https://flet.dev/docs/controls/elevatedbutton#style) property docs for a complete description of `ButtonStyle` class and its properties.
## TextField and Dropdown styling[​](https://flet.dev/blog/gradients-button-textfield-styles/#textfield-and-dropdown-styling "Direct link to TextField and Dropdown styling")
It is now possible to configure text size, border style and corners radius for normal and focused states of `TextField` and `Dropdown` controls. `TextField` also allows configuring colors for a cursor and selection.
Additionally, the maximum length of entered into `TextField` can now be limited with `max_length` property.
We also introduced `capitalization` property for automatic capitalization of characters as you type them into `TextField`. You can choose from 4 capitalization strategies: `none` (default), `characters`, `words` and `sentences`.
An example of styled `TextField` with `max_length` and `capitalization`:
![](https://flet.dev/img/blog/gradients/styled-textfield.gif)
```
import flet as ftdefmain(page: ft.Page):  page.padding =50  page.add(    ft.TextField(      text_size=30,      cursor_color=ft.Colors.RED,      selection_color=ft.Colors.YELLOW,      color=ft.Colors.PINK,      bgcolor=ft.Colors.BLACK26,      filled=True,      focused_color=ft.Colors.GREEN,      focused_bgcolor=ft.Colors.CYAN_200,      border_radius=30,      border_color=ft.Colors.GREEN_800,      focused_border_color=ft.Colors.GREEN_ACCENT_400,      max_length=20,      capitalization="characters",))ft.app(target=main)
```

An example of styled `Dropdown` control:
![](https://flet.dev/img/blog/gradients/styled-dropdown.gif)
```
import flet as ftdefmain(page: ft.Page):  page.padding =50  page.add(    ft.Dropdown(      options=[        ft.dropdown.Option("a","Item A"),        ft.dropdown.Option("b","Item B"),        ft.dropdown.Option("c","Item C"),],      border_radius=30,      filled=True,      border_color=ft.Colors.TRANSPARENT,      bgcolor=ft.Colors.BLACK12,      focused_bgcolor=ft.Colors.BLUE_100,))ft.app(target=main)
```

## Other changes[​](https://flet.dev/blog/gradients-button-textfield-styles/#other-changes "Direct link to Other changes")
`IconButton` got `selected` state which plays nice with a new `style`.
This is an example of a toggle icon button:
![](https://flet.dev/img/blog/gradients/toggle-icon-button.gif)
```
import flet as ftdefmain(page: ft.Page):deftoggle_icon_button(e):    e.control.selected =not e.control.selected    e.control.update()  page.add(    ft.IconButton(      icon=ft.Icons.BATTERY_1_BAR,      selected_icon=ft.Icons.BATTERY_FULL,      on_click=toggle_icon_button,      selected=False,      style=ft.ButtonStyle(color={"selected": ft.Colors.GREEN,"": ft.Colors.RED}),))ft.app(target=main)
```

[Give Flet a try](https://flet.dev/docs) and [let us know](https://discord.gg/dzWXP8SHG8) what you think!
**Tags:**
  * [release](https://flet.dev/blog/tags/release)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2022-08-04-gradients-button-textfield-styles.md)
[Newer postFun with animations](https://flet.dev/blog/fun-with-animations)[Older postControl Refs](https://flet.dev/blog/control-refs)
  * [Gradient backgrounds](https://flet.dev/blog/gradients-button-textfield-styles/#gradient-backgrounds)
    * [Linear gradient](https://flet.dev/blog/gradients-button-textfield-styles/#linear-gradient)
    * [Radial gradient](https://flet.dev/blog/gradients-button-textfield-styles/#radial-gradient)
    * [Sweep gradient](https://flet.dev/blog/gradients-button-textfield-styles/#sweep-gradient)
  * [Buttons styling](https://flet.dev/blog/gradients-button-textfield-styles/#buttons-styling)
  * [TextField and Dropdown styling](https://flet.dev/blog/gradients-button-textfield-styles/#textfield-and-dropdown-styling)
  * [Other changes](https://flet.dev/blog/gradients-button-textfield-styles/#other-changes)


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
