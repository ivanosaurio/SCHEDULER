[Skip to main content](https://flet.dev/docs/cookbook/theming/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/cookbook/theming/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/cookbook/theming/)
    * [Theming](https://flet.dev/docs/cookbook/theming)
    * [Keyboard shortcuts](https://flet.dev/docs/cookbook/keyboard-shortcuts)
    * [Large lists](https://flet.dev/docs/cookbook/large-lists)
    * [Drag and drop](https://flet.dev/docs/cookbook/drag-and-drop)
    * [File picker and uploads](https://flet.dev/docs/cookbook/file-picker-and-uploads)
    * [Animations](https://flet.dev/docs/cookbook/animations)
    * [Authentication](https://flet.dev/docs/cookbook/authentication)
    * [Assets](https://flet.dev/docs/cookbook/assets)
    * [Fonts](https://flet.dev/docs/cookbook/fonts)
    * [Read and write files](https://flet.dev/docs/cookbook/read-and-write-files)
    * [Client storage](https://flet.dev/docs/cookbook/client-storage)
    * [Session storage](https://flet.dev/docs/cookbook/session-storage)
    * [Encrypting sensitive data](https://flet.dev/docs/cookbook/encrypting-sensitive-data)
    * [PubSub](https://flet.dev/docs/cookbook/pub-sub)
    * [Control Refs](https://flet.dev/docs/cookbook/control-refs)
    * [Accessibility](https://flet.dev/docs/cookbook/accessibility)
    * [Logging](https://flet.dev/docs/cookbook/logging)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * Cookbook
  * Theming


On this page
# Theming
It is possible to configure your application and/or the containing controls to follow a particular themes.
### App-wide themes[​](https://flet.dev/docs/cookbook/theming/#app-wide-themes "Direct link to App-wide themes")
The `Page` control (uppermost control in the tree) has two useful properties for this: `theme` and `dark_theme` properties to configure the appearance/theme of the entire app in light and dark theme modes respectively.
Both of type [`Theme`](https://flet.dev/docs/reference/types/theme), they represent the default/fallback themes to be used app-wide, except explicitly modified/overriden in the tree.
```
page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN)page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE)
```

### Nested themes[​](https://flet.dev/docs/cookbook/theming/#nested-themes "Direct link to Nested themes")
You can have a part of your app to use a different theme or override some theme styles for specific controls.
Some container-like controls have `theme` and `theme_mode` properties of type [`Theme`](https://flet.dev/docs/reference/types/theme) and [`ThemeMode`](https://flet.dev/docs/reference/types/thememode) respectively.
Specifying `theme_mode` in the `Container` means you don't want to inherit parent theme mode, but want a completely new, unique scheme for all controls inside the container. However, if the container does not have `theme_mode` property set then the styles from its theme property will override the ones from the parent inherited theme:
```
import flet as ftdefmain(page: ft.Page):# Yellow page theme with SYSTEM (default) mode  page.theme = ft.Theme(    color_scheme_seed=ft.Colors.YELLOW,)  page.add(# Page theme    ft.Container(      content=ft.ElevatedButton("Page theme button"),      bgcolor=ft.Colors.SURFACE_VARIANT,      padding=20,      width=300,),# Inherited theme with primary color overridden    ft.Container(      theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.Colors.PINK)),      content=ft.ElevatedButton("Inherited theme button"),      bgcolor=ft.Colors.SURFACE_VARIANT,      padding=20,      width=300,),# Unique always DARK theme    ft.Container(      theme=ft.Theme(color_scheme_seed=ft.Colors.INDIGO),      theme_mode=ft.ThemeMode.DARK,      content=ft.ElevatedButton("Unique theme button"),      bgcolor=ft.Colors.SURFACE_VARIANT,      padding=20,      width=300,),)ft.app(main)
```

![](https://flet.dev/img/blog/theme-scrolling/nested-themes.png)
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/cookbook/theming.md)
[PreviousWindowDragArea](https://flet.dev/docs/controls/windowdragarea)[NextKeyboard shortcuts](https://flet.dev/docs/cookbook/keyboard-shortcuts)
  * [App-wide themes](https://flet.dev/docs/cookbook/theming/#app-wide-themes)
  * [Nested themes](https://flet.dev/docs/cookbook/theming/#nested-themes)


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
