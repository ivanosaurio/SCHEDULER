[Skip to main content](https://flet.dev/blog/scrolling-controls-and-theming/#__docusaurus_skipToContent_fallback)
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


# Scrolling controls and Theming
May 12, 2023 · 5 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
Flet 0.7.1 enables developers [changing scroll position](https://flet.dev/blog/scrolling-controls-and-theming/#controlling-scroll-position) and [receiving scroll notifications](https://flet.dev/blog/scrolling-controls-and-theming/#receiving-scroll-notifications) from `Page`, `View`, `Column`, `Row`, `ListView` and `GridView` controls.
The release also introduces theming improvements:
  * [Color scheme customization](https://flet.dev/blog/scrolling-controls-and-theming/#color-scheme-customization)
  * [Nested themes](https://flet.dev/blog/scrolling-controls-and-theming/#nested-themes)
  * [Text theming](https://flet.dev/blog/scrolling-controls-and-theming/#text-theming)
  * [Scrollbar theming](https://flet.dev/blog/scrolling-controls-and-theming/#scrollbar-theme)
  * [Tabs theming](https://flet.dev/blog/scrolling-controls-and-theming/#tabs-theming)


## Controlling scroll position[​](https://flet.dev/blog/scrolling-controls-and-theming/#controlling-scroll-position "Direct link to Controlling scroll position")
Scrollable controls (`Page`, `View`, `Column`, `Row`, `ListView` and `GridView`) introduce `scroll_to()` method to change their scroll position to either absolute `offset`, relative `delta` or jump to the control with specified `key`.
Moving to a `key` is particularly exciting as it allows simulating the navigation between page bookmarks, kind of HTML hrefs with `#`:
![](https://flet.dev/img/docs/controls/column/column-scroll-to-key.gif)
Check the [source code](https://github.com/flet-dev/examples/blob/main/python/controls/column/column-scroll-to-key.py) of the example above.
See [`Column.scroll_to`](https://flet.dev/docs/controls/column#scroll_tooffset-delta-key-duration-curve) for more details about controlling scroll position.
## Receiving scroll notifications[​](https://flet.dev/blog/scrolling-controls-and-theming/#receiving-scroll-notifications "Direct link to Receiving scroll notifications")
All scrollable controls now provide `on_scroll` event handler which fires when a scroll position is changed. From event object properties you can determine whether scroll operation has started, finished, changed direction or scroll position went behind scrolling extent (overscroll). You can also get updates of the current scroll position as well as dimensions of the scroll area, for example:
```
import flet as ftdefmain(page: ft.Page):defon_column_scroll(e: ft.OnScrollEvent):print(f"Type: {e.event_type}, pixels: {e.pixels}, min_scroll_extent: {e.min_scroll_extent}, max_scroll_extent: {e.max_scroll_extent}")  cl = ft.Column(    spacing=10,    height=200,    width=200,    scroll=ft.ScrollMode.ALWAYS,    on_scroll=on_column_scroll,)for i inrange(0,50):    cl.controls.append(ft.Text(f"Text line {i}", key=str(i)))  page.add(    ft.Container(cl, border=ft.border.all(1)),)ft.app(main)
```

See [`Column.on_scroll`](https://flet.dev/docs/controls/column#on_scroll) for more details about scroll notification.
Check [infinite scroll example](https://github.com/flet-dev/examples/blob/main/python/controls/column/column-infinite-list.py).
## Color scheme customization[​](https://flet.dev/blog/scrolling-controls-and-theming/#color-scheme-customization "Direct link to Color scheme customization")
Until today the only way to control color scheme for your application was specifying `color_scheme_seed` when creating a new `ft.Theme` object.
This release enables you to fine tune all 30 colors based on the [Material spec](https://m3.material.io/styles/color/the-color-system/color-roles) and used by various Flet controls.
![](https://flet.dev/img/blog/theme-scrolling/material-theme-builder.png)
You can even use [Material Theme Builder](https://m3.material.io/theme-builder#/dynamic) and apply exported color palette to your app, for example:
```
page.theme = ft.Theme(  color_scheme=ft.ColorScheme(    primary=ft.Colors.GREEN,    primary_container=ft.Colors.GREEN_200# ...),)
```

See [`ColorScheme` class](https://flet.dev/docs/reference/types/colorscheme) for more details.
## Nested themes[​](https://flet.dev/blog/scrolling-controls-and-theming/#nested-themes "Direct link to Nested themes")
Another awesome feature of this release is nested themes!
You can have a part of your app to use a different theme or override some theme styles for specific controls.
Remember `page` object having `theme` and `theme_mode` properties? Now `Container` has `theme` and `theme_mode` properties too!
`Container.theme` accepts the same `ft.Theme` object as a page. Specifying `theme_mode` in the container means you don't want to inherit parent theme, but want a completely new, unique scheme for all controls inside the container. However, if the container does not have `theme_mode` property set then the styles from its `theme` property will override the ones from the parent, inherited theme:
```
import flet as ftdefmain(page: ft.Page):# Yellow page theme with SYSTEM (default) mode  page.theme = ft.Theme(    color_scheme_seed=ft.Colors.YELLOW,)  page.add(# Page theme    ft.Container(      content=ft.ElevatedButton("Page theme button"),      bgcolor=ft.Colors.SURFACE_VARIANT,      padding=20,      width=300,),# Inherited theme with primary color overridden    ft.Container(      theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.Colors.PINK)),      content=ft.ElevatedButton("Inherited theme button"),      bgcolor=ft.Colors.SURFACE_VARIANT,      padding=20,      width=300,),# Unique always DARK theme    ft.Container(      theme=ft.Theme(color_scheme_seed=ft.Colors.INDIGO),      theme_mode=ft.ThemeMode.DARK,      content=ft.ElevatedButton("Unique theme button"),      bgcolor=ft.Colors.SURFACE_VARIANT,      padding=20,      width=300,),)ft.app(main)
```

![](https://flet.dev/img/blog/theme-scrolling/nested-themes.png)
## Scrollbar theme[​](https://flet.dev/blog/scrolling-controls-and-theming/#scrollbar-theme "Direct link to Scrollbar theme")
You can now customize the look and fill of scrollbars in your application (or a particular scroillbar with [nested themes](https://flet.dev/blog/scrolling-controls-and-theming/#nested-themes)).
It could be done via [`page.theme.scrollbar_theme`](https://flet.dev/docs/reference/types/scrollbartheme) property, for example:
```
page.theme = ft.Theme(  scrollbar_theme=ft.ScrollbarTheme(    track_color={      ft.MaterialState.HOVERED: ft.Colors.AMBER,      ft.MaterialState.DEFAULT: ft.Colors.TRANSPARENT,},    track_visibility=True,    track_border_color=ft.Colors.BLUE,    thumb_visibility=True,    thumb_color={      ft.MaterialState.HOVERED: ft.Colors.RED,      ft.MaterialState.DEFAULT: ft.Colors.GREY_300,},    thickness=30,    radius=15,    main_axis_margin=5,    cross_axis_margin=10,))
```

![](https://flet.dev/img/docs/controls/column/column-scroll-to.png)
## Text theming[​](https://flet.dev/blog/scrolling-controls-and-theming/#text-theming "Direct link to Text theming")
Material 3 design defines [5 groups of text styles with 3 sizes in each group](https://flet.dev/docs/controls/text#pre-defined-theme-text-styles): "Display", "Headline", "Title", "Label" and "Body" which are used across Flet controls. You can now customize each of those styles with `page.theme.text_theme`, for example:
```
import flet as ftdefmain(page: ft.Page):  page.theme = ft.Theme(    text_theme=ft.TextTheme(body_medium=ft.TextStyle(color=ft.Colors.GREEN)))  page.add(ft.Text("Hello, green world!"))ft.app(main)
```

![](https://flet.dev/img/blog/theme-scrolling/text-theme.png)
Apparently, `Body Medium` is used by `Text` control as a default style.
See [`TextTheme` class](https://flet.dev/docs/reference/types/texttheme) for more details.
## Tabs theming[​](https://flet.dev/blog/scrolling-controls-and-theming/#tabs-theming "Direct link to Tabs theming")
You can now control the look and feel of `Tabs` control. In this release `Tabs` adds a bunch of new properties and there is a new [`page.theme.tabs_theme`](https://flet.dev/docs/reference/types/tabstheme) property to style all tabs in your app:
```
page.theme = ft.Theme(  tabs_theme=ft.TabsTheme(    divider_color=ft.Colors.BLUE,    indicator_color=ft.Colors.RED,    indicator_tab_size=True,    label_color=ft.Colors.GREEN,    unselected_label_color=ft.Colors.AMBER,    overlay_color={      ft.MaterialState.FOCUSED: ft.Colors.with_opacity(0.2, ft.Colors.GREEN),      ft.MaterialState.DEFAULT: ft.Colors.with_opacity(0.2, ft.Colors.PINK),},))
```

![](https://flet.dev/img/blog/theme-scrolling/tabs-theme.png)
See [`TabsTheme` class](https://flet.dev/docs/reference/types/tabstheme) for more details.
## Other changes[​](https://flet.dev/blog/scrolling-controls-and-theming/#other-changes "Direct link to Other changes")
### Flutter 3.10[​](https://flet.dev/blog/scrolling-controls-and-theming/#flutter-310 "Direct link to Flutter 3.10")
This Flet release is based on Flutter 3.10 which [brings new features, performance and size optimizations](https://medium.com/flutter/whats-new-in-flutter-3-10-b21db2c38c73). As a result, most of Flet dependencies bumped their versions too, so if you notice any issues please let us know.
### Color emoji in web apps[​](https://flet.dev/blog/scrolling-controls-and-theming/#color-emoji-in-web-apps "Direct link to Color emoji in web apps")
Color emoji support in web apps are back! In Flutter 3.7 color emoji were disabled in "CanvasKit" renderer (default in Flet) because of their font size (8 MB!) and returned back as an opt-in in Flutter 3.10. You can enable color emoji in server-driven app with `use_color_emoji` argument:
```
ft.app(main, use_color_emoji=True)
```

and [use `--use-color-emoji` switch](https://flet.dev/docs/publish/web/static-website#color-emojis) when publishing app as a static side.
That's all for today!
Upgrade Flet module to the latest version (`pip install flet --upgrade`) and [let us know](https://discord.gg/dzWXP8SHG8) what you think!
**Tags:**
  * [releases](https://flet.dev/blog/tags/releases)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2023-05-12-theming-and-scrollables.md)
[Newer postFlet for iOS](https://flet.dev/blog/flet-for-ios)[Older postCanvas](https://flet.dev/blog/canvas)
  * [Controlling scroll position](https://flet.dev/blog/scrolling-controls-and-theming/#controlling-scroll-position)
  * [Receiving scroll notifications](https://flet.dev/blog/scrolling-controls-and-theming/#receiving-scroll-notifications)
  * [Color scheme customization](https://flet.dev/blog/scrolling-controls-and-theming/#color-scheme-customization)
  * [Nested themes](https://flet.dev/blog/scrolling-controls-and-theming/#nested-themes)
  * [Scrollbar theme](https://flet.dev/blog/scrolling-controls-and-theming/#scrollbar-theme)
  * [Text theming](https://flet.dev/blog/scrolling-controls-and-theming/#text-theming)
  * [Tabs theming](https://flet.dev/blog/scrolling-controls-and-theming/#tabs-theming)
  * [Other changes](https://flet.dev/blog/scrolling-controls-and-theming/#other-changes)
    * [Flutter 3.10](https://flet.dev/blog/scrolling-controls-and-theming/#flutter-310)
    * [Color emoji in web apps](https://flet.dev/blog/scrolling-controls-and-theming/#color-emoji-in-web-apps)


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
