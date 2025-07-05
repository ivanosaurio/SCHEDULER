[Skip to main content](https://flet.dev/docs/controls/appbar/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/appbar/)
  * [Controls](https://flet.dev/docs/controls)
    * [Layout](https://flet.dev/docs/controls/layout)
    * [Navigation](https://flet.dev/docs/controls/app-structure-navigation)
      * [AppBar](https://flet.dev/docs/controls/appbar)
      * [BottomAppBar](https://flet.dev/docs/controls/bottomappbar)
      * [CupertinoAppBar](https://flet.dev/docs/controls/cupertinoappbar)
      * [CupertinoNavigationBar](https://flet.dev/docs/controls/cupertinonavigationbar)
      * [MenuBar](https://flet.dev/docs/controls/menubar)
      * [NavigationBar](https://flet.dev/docs/controls/navigationbar)
      * [NavigationDrawer](https://flet.dev/docs/controls/navigationdrawer)
      * [NavigationRail](https://flet.dev/docs/controls/navigationrail)
    * [Information Displays](https://flet.dev/docs/controls/information-displays)
    * [Buttons](https://flet.dev/docs/controls/buttons)
    * [Input and Selections](https://flet.dev/docs/controls/input-and-selections)
    * [Dialogs, Alerts and Panels](https://flet.dev/docs/controls/dialogs-alerts-panels)
    * [Charts](https://flet.dev/docs/controls/charts)
    * [Animations](https://flet.dev/docs/controls/animations)
    * [Utility](https://flet.dev/docs/controls/utility)
  * [Cookbook](https://flet.dev/docs/controls/appbar/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Navigation](https://flet.dev/docs/controls/app-structure-navigation)
  * AppBar


On this page
# AppBar
A material design app bar.
## Examples[​](https://flet.dev/docs/controls/appbar/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/navigation/appbar)
### AppBar[​](https://flet.dev/docs/controls/appbar/#appbar "Direct link to AppBar")
python/controls/navigation/app-bar/appbar-simple.py
```
import flet as ftdefmain(page: ft.Page):  page.title ="AppBar Example"defcheck_item_clicked(e):    e.control.checked =not e.control.checked    page.update()  page.appbar = ft.AppBar(    leading=ft.Icon(ft.Icons.PALETTE),    leading_width=40,    title=ft.Text("AppBar Example"),    center_title=False,    bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,    actions=[      ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),      ft.IconButton(ft.Icons.FILTER_3),      ft.PopupMenuButton(        items=[          ft.PopupMenuItem(text="Item 1"),          ft.PopupMenuItem(),# divider          ft.PopupMenuItem(            text="Checked item", checked=False, on_click=check_item_clicked),]),],)  page.add(ft.Text("Body!"))ft.app(target=main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/navigation/app-bar/appbar-simple.py)
![](https://flet.dev/img/docs/controls/app-bar/app-bar.gif)
## Properties[​](https://flet.dev/docs/controls/appbar/#properties "Direct link to Properties")
### `actions`[​](https://flet.dev/docs/controls/appbar/#actions "Direct link to actions")
A list of `Control`s to display in a row after the title control.
Typically these controls are [`IconButtons`](https://flet.dev/docs/controls/iconbutton) representing common operations. For less common operations, consider using a [`PopupMenuButton`](https://flet.dev/docs/controls/popupmenubutton) as the last action.
**Note** that, if `AppBar.adaptive=True` and the app is opened on an iOS or macOS device, only the first element of this list will be used. This is because the `CupertinoAppBar`(which will be used on those two platforms) only accepts one - trailing - action control.
### `adaptive`[​](https://flet.dev/docs/controls/appbar/#adaptive "Direct link to adaptive")
If the value is `True`, an adaptive AppBar is created based on whether the target platform is iOS/macOS.
On iOS and macOS, a [`CupertinoAppBar`](https://flet.dev/docs/controls/cupertinoappbar) is created, which has matching functionality and presentation as `AppBar`, and the graphics as expected on iOS. On other platforms, a Material AppBar is created.
Value is of type `bool` and defaults to `False`.
### `automatically_imply_leading`[​](https://flet.dev/docs/controls/appbar/#automatically_imply_leading "Direct link to automatically_imply_leading")
Controls whether we should try to imply the leading widget if null.
If `True` and `leading` is null, automatically try to deduce what the leading widget should be. If `False` and `leading` is null, leading space is given to title. If leading widget is not null, this parameter has no effect.
Value is of type `bool`.
### `bgcolor`[​](https://flet.dev/docs/controls/appbar/#bgcolor "Direct link to bgcolor")
The fill [color](https://flet.dev/docs/reference/colors) to use for an AppBar. Default color is defined by current theme.
### `center_title`[​](https://flet.dev/docs/controls/appbar/#center_title "Direct link to center_title")
Whether the title should be centered.
Value is of type `bool` and defaults to `False`.
### `clip_behavior`[​](https://flet.dev/docs/controls/appbar/#clip_behavior "Direct link to clip_behavior")
The content will be clipped (or not) according to this option.
Value is of type [`ClipBehavior`](https://flet.dev/docs/reference/types/clipbehavior).
### `color`[​](https://flet.dev/docs/controls/appbar/#color "Direct link to color")
The default [color](https://flet.dev/docs/reference/colors) for `Text` and `Icon` controls within the app bar. Default color is defined by current theme.
### `elevation`[​](https://flet.dev/docs/controls/appbar/#elevation "Direct link to elevation")
The app bar's elevation.
Note: This effect is only visible when using the Material 2 design (`Theme.use_material3=False`).
Value is of type [`OptionalNumber`](https://flet.dev/docs/reference/types/aliases#optionalnumber) and defaults to `4`.
### `elevation_on_scroll`[​](https://flet.dev/docs/controls/appbar/#elevation_on_scroll "Direct link to elevation_on_scroll")
The elevation to be used if this app bar has something scrolled underneath it.
Value is of type [`OptionalNumber`](https://flet.dev/docs/reference/types/aliases#optionalnumber).
### `exclude_header_semantics`[​](https://flet.dev/docs/controls/appbar/#exclude_header_semantics "Direct link to exclude_header_semantics")
Whether the `title` should be wrapped with header [`Semantics`](https://flet.dev/docs/controls/semantics).
Value is of type `bool` and defaults to `False`.
### `force_material_transparency`[​](https://flet.dev/docs/controls/appbar/#force_material_transparency "Direct link to force_material_transparency")
Forces the app bar to be transparent (instead of Material's default type).
This will also remove the visual display of `bgcolor` and `elevation`, and affect other characteristics of this app bar.
Value is of type `bool`.
### `is_secondary`[​](https://flet.dev/docs/controls/appbar/#is_secondary "Direct link to is_secondary")
Whether this app bar is not being displayed at the top of the screen.
Value is of type `bool` and defaults to `False`.
### `leading`[​](https://flet.dev/docs/controls/appbar/#leading "Direct link to leading")
A `Control` to display before the toolbar's title.
Typically the leading control is an [`Icon`](https://flet.dev/docs/controls/icon) or an [`IconButton`](https://flet.dev/docs/controls/iconbutton).
Value is of type `Control`.
### `leading_width`[​](https://flet.dev/docs/controls/appbar/#leading_width "Direct link to leading_width")
Defines the width of leading control.
Value is of type [`OptionalNumber`](https://flet.dev/docs/reference/types/aliases#optionalnumber) and defaults to `56.0`.
### `shadow_color`[​](https://flet.dev/docs/controls/appbar/#shadow_color "Direct link to shadow_color")
The [color](https://flet.dev/docs/reference/colors) of the shadow below the app bar.
A shadow is only visible and displayed if the `elevation` is greater than zero.
### `shape`[​](https://flet.dev/docs/controls/appbar/#shape "Direct link to shape")
The shape of the app bar's Material as well as its shadow.
Value is of type [`OutlinedBorder`](https://flet.dev/docs/reference/types/outlinedborder).
### `surface_tint_color`[​](https://flet.dev/docs/controls/appbar/#surface_tint_color "Direct link to surface_tint_color")
The color of the surface tint overlay applied to the app bar's `bgcolor` to indicate elevation.
By default, no overlay will be applied.
### `title`[​](https://flet.dev/docs/controls/appbar/#title "Direct link to title")
The primary `Control` displayed in the app bar. Typically a [`Text`](https://flet.dev/docs/controls/text) control that contains a description of the current contents of the app.
**Note** that, if `AppBar.adaptive=True` and the app is opened on an iOS or macOS device, this control will be automatically centered.
Value is of type `Control`.
### `title_spacing`[​](https://flet.dev/docs/controls/appbar/#title_spacing "Direct link to title_spacing")
The spacing around `title` on the horizontal axis. It is applied even if there are no `leading` or `actions` controls.
If you want `title` to take all the space available, set this value to `0.0`.
Value is of type [`OptionalNumber`](https://flet.dev/docs/reference/types/aliases#optionalnumber).
### `title_text_style`[​](https://flet.dev/docs/controls/appbar/#title_text_style "Direct link to title_text_style")
The style to be used for the `Text` controls in the `title`.
Value is of type [`TextStyle`](https://flet.dev/docs/reference/types/textstyle).
### `toolbar_height`[​](https://flet.dev/docs/controls/appbar/#toolbar_height "Direct link to toolbar_height")
Defines the height of the toolbar component of an AppBar.
Value is of tye [`OptionalNumber`](https://flet.dev/docs/reference/types/aliases#optionalnumber) and defaults to `56.0`.
### `toolbar_opacity`[​](https://flet.dev/docs/controls/appbar/#toolbar_opacity "Direct link to toolbar_opacity")
The opacity of the toolbar. Value ranges from `0.0` (transparent) to `1.0` (fully opaque).
Value is of type [`OptionalNumber`](https://flet.dev/docs/reference/types/aliases#optionalnumber) and defaults to `1.0`.
### `toolbar_text_style`[​](https://flet.dev/docs/controls/appbar/#toolbar_text_style "Direct link to toolbar_text_style")
The style to be used for the `Text` controls in the app bar's `leading` and `actions` (but not `title`).
Value is of type [`TextStyle`](https://flet.dev/docs/reference/types/textstyle).
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/appbar.md)
[PreviousNavigation](https://flet.dev/docs/controls/app-structure-navigation)[NextBottomAppBar](https://flet.dev/docs/controls/bottomappbar)
  * [Examples](https://flet.dev/docs/controls/appbar/#examples)
    * [AppBar](https://flet.dev/docs/controls/appbar/#appbar)
  * [Properties](https://flet.dev/docs/controls/appbar/#properties)
    * [`actions`](https://flet.dev/docs/controls/appbar/#actions)
    * [`adaptive`](https://flet.dev/docs/controls/appbar/#adaptive)
    * [`automatically_imply_leading`](https://flet.dev/docs/controls/appbar/#automatically_imply_leading)
    * [`bgcolor`](https://flet.dev/docs/controls/appbar/#bgcolor)
    * [`center_title`](https://flet.dev/docs/controls/appbar/#center_title)
    * [`clip_behavior`](https://flet.dev/docs/controls/appbar/#clip_behavior)
    * [`color`](https://flet.dev/docs/controls/appbar/#color)
    * [`elevation`](https://flet.dev/docs/controls/appbar/#elevation)
    * [`elevation_on_scroll`](https://flet.dev/docs/controls/appbar/#elevation_on_scroll)
    * [`exclude_header_semantics`](https://flet.dev/docs/controls/appbar/#exclude_header_semantics)
    * [`force_material_transparency`](https://flet.dev/docs/controls/appbar/#force_material_transparency)
    * [`is_secondary`](https://flet.dev/docs/controls/appbar/#is_secondary)
    * [`leading`](https://flet.dev/docs/controls/appbar/#leading)
    * [`leading_width`](https://flet.dev/docs/controls/appbar/#leading_width)
    * [`shadow_color`](https://flet.dev/docs/controls/appbar/#shadow_color)
    * [`shape`](https://flet.dev/docs/controls/appbar/#shape)
    * [`surface_tint_color`](https://flet.dev/docs/controls/appbar/#surface_tint_color)
    * [`title`](https://flet.dev/docs/controls/appbar/#title)
    * [`title_spacing`](https://flet.dev/docs/controls/appbar/#title_spacing)
    * [`title_text_style`](https://flet.dev/docs/controls/appbar/#title_text_style)
    * [`toolbar_height`](https://flet.dev/docs/controls/appbar/#toolbar_height)
    * [`toolbar_opacity`](https://flet.dev/docs/controls/appbar/#toolbar_opacity)
    * [`toolbar_text_style`](https://flet.dev/docs/controls/appbar/#toolbar_text_style)


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
