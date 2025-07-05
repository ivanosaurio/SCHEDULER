[Skip to main content](https://flet.dev/docs/controls/navigationbar/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/navigationbar/)
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
  * [Cookbook](https://flet.dev/docs/controls/navigationbar/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Navigation](https://flet.dev/docs/controls/app-structure-navigation)
  * NavigationBar


On this page
# NavigationBar
Material 3 Navigation Bar component.
Navigation bars offer a persistent and convenient way to switch between primary destinations in an app.
## Examples[​](https://flet.dev/docs/controls/navigationbar/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/navigation/navigationbar)
### A simple NavigationBar[​](https://flet.dev/docs/controls/navigationbar/#a-simple-navigationbar "Direct link to A simple NavigationBar")
![](https://flet.dev/img/docs/controls/navigation-bar/navigation-bar-sample.gif)
python/controls/navigation/navigation-bar/navigation-bar-sample.py
```
import flet as ftdefmain(page: ft.Page):  page.title ="NavigationBar Example"  page.navigation_bar = ft.NavigationBar(    destinations=[      ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explore"),      ft.NavigationBarDestination(icon=ft.Icons.COMMUTE, label="Commute"),      ft.NavigationBarDestination(        icon=ft.Icons.BOOKMARK_BORDER,        selected_icon=ft.Icons.BOOKMARK,        label="Favorites",),])  page.add(ft.Text("Body!"))ft.app(target=main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/navigation/navigation-bar/navigation-bar-sample.py)
## `NavigationBar` properties[​](https://flet.dev/docs/controls/navigationbar/#navigationbar-properties "Direct link to navigationbar-properties")
### `adaptive`[​](https://flet.dev/docs/controls/navigationbar/#adaptive "Direct link to adaptive")
If the value is `True`, an adaptive `NavigationBar` is created based on whether the target platform is iOS/macOS.
On iOS and macOS, a `CupertinoNavigationBar` is created, which has matching functionality and presentation as `NavigationBar`, and the graphics as expected on iOS. On other platforms, a Material `NavigationBar` is created.
Defaults to `False`.
### `animation_duration`[​](https://flet.dev/docs/controls/navigationbar/#animation_duration "Direct link to animation_duration")
The transition time for each destination as it goes between selected and unselected.
### `bgcolor`[​](https://flet.dev/docs/controls/navigationbar/#bgcolor "Direct link to bgcolor")
The [color](https://flet.dev/docs/reference/colors) of the navigation bar itself.
### `destinations`[​](https://flet.dev/docs/controls/navigationbar/#destinations "Direct link to destinations")
Defines the appearance of the button items that are arrayed within the navigation bar.
The value must be a list of two or more `NavigationBarDestination` instances.
### `elevation`[​](https://flet.dev/docs/controls/navigationbar/#elevation "Direct link to elevation")
The elevation of the navigation bar itself.
### `indicator_color`[​](https://flet.dev/docs/controls/navigationbar/#indicator_color "Direct link to indicator_color")
The [color](https://flet.dev/docs/reference/colors) of the selected destination indicator.
### `indicator_shape`[​](https://flet.dev/docs/controls/navigationbar/#indicator_shape "Direct link to indicator_shape")
The shape of the selected destination indicator.
Value is of type [`OutlinedBorder`](https://flet.dev/docs/reference/types/outlinedborder).
### `label_behavior`[​](https://flet.dev/docs/controls/navigationbar/#label_behavior "Direct link to label_behavior")
Defines how the destinations' labels will be laid out and when they'll be displayed.
Can be used to show all labels, show only the selected label, or hide all labels.
Value is of type [`NavigationBarLabelBehavior`](https://flet.dev/docs/reference/types/navigationbarlabelbehavior) and defaults to `NavigationBarLabelBehavior.ALWAYS_SHOW`.
### `overlay_color`[​](https://flet.dev/docs/controls/navigationbar/#overlay_color "Direct link to overlay_color")
The highlight [color](https://flet.dev/docs/reference/colors) of the `NavigationDestination` in various [`ControlState`](https://flet.dev/docs/reference/types/controlstate) states. The following [`ControlState`](https://flet.dev/docs/reference/types/controlstate) values are supported: `PRESSED`, `HOVERED` and `FOCUSED`.
### `selected_index`[​](https://flet.dev/docs/controls/navigationbar/#selected_index "Direct link to selected_index")
The index into `destinations` for the current selected `NavigationBarDestination` or `None` if no destination is selected.
### `shadow_color`[​](https://flet.dev/docs/controls/navigationbar/#shadow_color "Direct link to shadow_color")
The [color](https://flet.dev/docs/reference/colors) used for the drop shadow to indicate `elevation`.
### `surface_tint_color`[​](https://flet.dev/docs/controls/navigationbar/#surface_tint_color "Direct link to surface_tint_color")
The surface tint of the Material that holds the NavigationDrawer's contents.
## `NavigationBar` events[​](https://flet.dev/docs/controls/navigationbar/#navigationbar-events "Direct link to navigationbar-events")
### `on_change`[​](https://flet.dev/docs/controls/navigationbar/#on_change "Direct link to on_change")
Fires when selected destination changed.
## `NavigationBarDestination` properties[​](https://flet.dev/docs/controls/navigationbar/#navigationbardestination-properties "Direct link to navigationbardestination-properties")
### `bgcolor`[​](https://flet.dev/docs/controls/navigationbar/#bgcolor-1 "Direct link to bgcolor-1")
The [color](https://flet.dev/docs/reference/colors) of this destination.
### `icon`[​](https://flet.dev/docs/controls/navigationbar/#icon "Direct link to icon")
The [name of the icon](https://flet.dev/docs/reference/icons) or `Control` of the destination.
Example with icon name:
```
icon=ft.Icons.BOOKMARK
```

Example with Control:
```
icon=ft.Icon(ft.Icons.BOOKMARK)
```

If `selected_icon` is provided, this will only be displayed when the destination is not selected.
To make the NavigationBar more accessible, consider choosing an icon with a stroked and filled version, such as `ft.Icons.CLOUD` and `ft.Icons.CLOUD_QUEUE`. The icon should be set to the stroked version and `selected_icon` to the filled version.
### ~~`icon_content`~~[​](https://flet.dev/docs/controls/navigationbar/#icon_content "Direct link to icon_content")
The icon `Control` of the destination. Typically the icon is an [`Icon`](https://flet.dev/docs/controls/icon) control. Used instead of `icon` property.
**Deprecated in v0.25.0 and will be removed in v0.28.0. Use[`icon`](https://flet.dev/docs/controls/navigationbar/#icon) instead.**
### `label`[​](https://flet.dev/docs/controls/navigationbar/#label "Direct link to label")
The text label that appears below the icon of this `NavigationBarDestination`.
### `selected_icon`[​](https://flet.dev/docs/controls/navigationbar/#selected_icon "Direct link to selected_icon")
The [name](https://flet.dev/docs/reference/icons) of alternative icon or `Control` displayed when this destination is selected.
Example with icon name:
```
selected_icon=ft.Icons.BOOKMARK
```

Example with Control:
```
selected_icon=ft.Icon(ft.Icons.BOOKMARK)
```

If this icon is not provided, the NavigationBar will display `icon` in either state.
### ~~`selected_icon_content`~~[​](https://flet.dev/docs/controls/navigationbar/#selected_icon_content "Direct link to selected_icon_content")
An alternative icon `Control` displayed when this destination is selected.
**Deprecated in v0.25.0 and will be removed in v0.28.0. Use[`selected_icon`](https://flet.dev/docs/controls/navigationbar/#selected_icon) instead.**
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/navigationbar.md)
[PreviousMenuBar](https://flet.dev/docs/controls/menubar)[NextNavigationDrawer](https://flet.dev/docs/controls/navigationdrawer)
  * [Examples](https://flet.dev/docs/controls/navigationbar/#examples)
    * [A simple NavigationBar](https://flet.dev/docs/controls/navigationbar/#a-simple-navigationbar)
  * [`NavigationBar` properties](https://flet.dev/docs/controls/navigationbar/#navigationbar-properties)
    * [`adaptive`](https://flet.dev/docs/controls/navigationbar/#adaptive)
    * [`animation_duration`](https://flet.dev/docs/controls/navigationbar/#animation_duration)
    * [`bgcolor`](https://flet.dev/docs/controls/navigationbar/#bgcolor)
    * [`destinations`](https://flet.dev/docs/controls/navigationbar/#destinations)
    * [`elevation`](https://flet.dev/docs/controls/navigationbar/#elevation)
    * [`indicator_color`](https://flet.dev/docs/controls/navigationbar/#indicator_color)
    * [`indicator_shape`](https://flet.dev/docs/controls/navigationbar/#indicator_shape)
    * [`label_behavior`](https://flet.dev/docs/controls/navigationbar/#label_behavior)
    * [`overlay_color`](https://flet.dev/docs/controls/navigationbar/#overlay_color)
    * [`selected_index`](https://flet.dev/docs/controls/navigationbar/#selected_index)
    * [`shadow_color`](https://flet.dev/docs/controls/navigationbar/#shadow_color)
    * [`surface_tint_color`](https://flet.dev/docs/controls/navigationbar/#surface_tint_color)
  * [`NavigationBar` events](https://flet.dev/docs/controls/navigationbar/#navigationbar-events)
    * [`on_change`](https://flet.dev/docs/controls/navigationbar/#on_change)
  * [`NavigationBarDestination` properties](https://flet.dev/docs/controls/navigationbar/#navigationbardestination-properties)
    * [`bgcolor`](https://flet.dev/docs/controls/navigationbar/#bgcolor-1)
    * [`icon`](https://flet.dev/docs/controls/navigationbar/#icon)
    * [~~`icon_content`~~](https://flet.dev/docs/controls/navigationbar/#icon_content)
    * [`label`](https://flet.dev/docs/controls/navigationbar/#label)
    * [`selected_icon`](https://flet.dev/docs/controls/navigationbar/#selected_icon)
    * [~~`selected_icon_content`~~](https://flet.dev/docs/controls/navigationbar/#selected_icon_content)


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
