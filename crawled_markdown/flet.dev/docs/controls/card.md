[Skip to main content](https://flet.dev/docs/controls/card/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/card/)
  * [Controls](https://flet.dev/docs/controls)
    * [Layout](https://flet.dev/docs/controls/layout)
      * [Card](https://flet.dev/docs/controls/card)
      * [Column](https://flet.dev/docs/controls/column)
      * [Container](https://flet.dev/docs/controls/container)
      * [CupertinoListTile](https://flet.dev/docs/controls/cupertinolisttile)
      * [DataTable](https://flet.dev/docs/controls/datatable)
      * [Dismissible](https://flet.dev/docs/controls/dismissible)
      * [Divider](https://flet.dev/docs/controls/divider)
      * [ExpansionPanelList](https://flet.dev/docs/controls/expansionpanel)
      * [ExpansionTile](https://flet.dev/docs/controls/expansiontile)
      * [GridView](https://flet.dev/docs/controls/gridview)
      * [ListTile](https://flet.dev/docs/controls/listtile)
      * [ListView](https://flet.dev/docs/controls/listview)
      * [Page](https://flet.dev/docs/controls/page)
      * [Pagelet](https://flet.dev/docs/controls/pagelet)
      * [Placeholder](https://flet.dev/docs/controls/placeholder)
      * [ReorderableListView](https://flet.dev/docs/controls/reorderablelistview)
      * [ResponsiveRow](https://flet.dev/docs/controls/responsiverow)
      * [Row](https://flet.dev/docs/controls/row)
      * [SafeArea](https://flet.dev/docs/controls/safearea)
      * [Stack](https://flet.dev/docs/controls/stack)
      * [Tabs](https://flet.dev/docs/controls/tabs)
      * [VerticalDivider](https://flet.dev/docs/controls/verticaldivider)
      * [View](https://flet.dev/docs/controls/view)
    * [Navigation](https://flet.dev/docs/controls/app-structure-navigation)
    * [Information Displays](https://flet.dev/docs/controls/information-displays)
    * [Buttons](https://flet.dev/docs/controls/buttons)
    * [Input and Selections](https://flet.dev/docs/controls/input-and-selections)
    * [Dialogs, Alerts and Panels](https://flet.dev/docs/controls/dialogs-alerts-panels)
    * [Charts](https://flet.dev/docs/controls/charts)
    * [Animations](https://flet.dev/docs/controls/animations)
    * [Utility](https://flet.dev/docs/controls/utility)
  * [Cookbook](https://flet.dev/docs/controls/card/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Layout](https://flet.dev/docs/controls/layout)
  * Card


On this page
# Card
A material design card: a panel with slightly rounded corners and an elevation shadow.
## Examples[​](https://flet.dev/docs/controls/card/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/layout/card)
python/controls/layout/card/card-with-buttons.py
```
import flet as ftdefmain(page: ft.Page):  page.title ="Card Example"  page.theme_mode = ft.ThemeMode.LIGHT  page.add(    ft.Card(      content=ft.Container(        content=ft.Column([            ft.ListTile(              leading=ft.Icon(ft.Icons.ALBUM),              title=ft.Text("The Enchanted Nightingale"),              subtitle=ft.Text("Music by Julie Gable. Lyrics by Sidney Stein."),              bgcolor=ft.Colors.GREY_400,),            ft.Row([ft.TextButton("Buy tickets"), ft.TextButton("Listen")],              alignment=ft.MainAxisAlignment.END,),]),        width=400,        padding=10,),      shadow_color=ft.Colors.ON_SURFACE_VARIANT,))ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/card/card-with-buttons.py)
![](https://flet.dev/img/docs/controls/card/card.gif)
## Properties[​](https://flet.dev/docs/controls/card/#properties "Direct link to Properties")
### `clip_behavior`[​](https://flet.dev/docs/controls/card/#clip_behavior "Direct link to clip_behavior")
The `content` will be clipped (or not) according to this option.
Value is of type [`ClipBehavior`](https://flet.dev/docs/reference/types/clipbehavior) and defaults to `ClipBehavior.NONE`.
### `color`[​](https://flet.dev/docs/controls/card/#color "Direct link to color")
The card's background [color](https://flet.dev/docs/reference/colors).
### `content`[​](https://flet.dev/docs/controls/card/#content "Direct link to content")
The `Control` that should be displayed inside the card.
This control can only have one child. To lay out multiple children, let this control's child be a control such as [`Row`](https://flet.dev/docs/controls/row), [`Column`](https://flet.dev/docs/controls/column), or [`Stack`](https://flet.dev/docs/controls/stack), which have a children property, and then provide the children to that control.
### `elevation`[​](https://flet.dev/docs/controls/card/#elevation "Direct link to elevation")
Controls the size of the shadow below the card. Default value is `1.0`.
### `is_semantic_container`[​](https://flet.dev/docs/controls/card/#is_semantic_container "Direct link to is_semantic_container")
Set to `True` (default) if this card represents a single semantic container, or to `False` if it instead represents a collection of individual semantic nodes (different types of content).
### `margin`[​](https://flet.dev/docs/controls/card/#margin "Direct link to margin")
The empty space that surrounds the card.
Value can be one of the following types: `int`, `float`, or [`Margin`](https://flet.dev/docs/reference/types/margin).
### `shadow_color`[​](https://flet.dev/docs/controls/card/#shadow_color "Direct link to shadow_color")
The [color](https://flet.dev/docs/reference/colors) to paint the shadow below the card.
### `shape`[​](https://flet.dev/docs/controls/card/#shape "Direct link to shape")
The shape of the card.
Value is of type [`OutlinedBorder`](https://flet.dev/docs/reference/types/outlinedborder) and defaults to `RoundedRectangleBorder(radius=4.0)`.
### `show_border_on_foreground`[​](https://flet.dev/docs/controls/card/#show_border_on_foreground "Direct link to show_border_on_foreground")
Whether the shape of the border should be painted in front of the `content` or behind.
Defaults to `True`.
### `surface_tint_color`[​](https://flet.dev/docs/controls/card/#surface_tint_color "Direct link to surface_tint_color")
The [color](https://flet.dev/docs/reference/colors) used as an overlay on `color` to indicate elevation.
If this is `None`, no overlay will be applied. Otherwise this color will be composited on top of `color` with an opacity related to `elevation` and used to paint the background of the card.
Defaults to `None`.
### `variant`[​](https://flet.dev/docs/controls/card/#variant "Direct link to variant")
Defines the card variant to be used.
Value is of type [`CardVariant`](https://flet.dev/docs/reference/types/cardvariant) and defaults to `CardVariant.ELEVATED`.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/card.md)
[PreviousLayout](https://flet.dev/docs/controls/layout)[NextColumn](https://flet.dev/docs/controls/column)
  * [Examples](https://flet.dev/docs/controls/card/#examples)
  * [Properties](https://flet.dev/docs/controls/card/#properties)
    * [`clip_behavior`](https://flet.dev/docs/controls/card/#clip_behavior)
    * [`color`](https://flet.dev/docs/controls/card/#color)
    * [`content`](https://flet.dev/docs/controls/card/#content)
    * [`elevation`](https://flet.dev/docs/controls/card/#elevation)
    * [`is_semantic_container`](https://flet.dev/docs/controls/card/#is_semantic_container)
    * [`margin`](https://flet.dev/docs/controls/card/#margin)
    * [`shadow_color`](https://flet.dev/docs/controls/card/#shadow_color)
    * [`shape`](https://flet.dev/docs/controls/card/#shape)
    * [`show_border_on_foreground`](https://flet.dev/docs/controls/card/#show_border_on_foreground)
    * [`surface_tint_color`](https://flet.dev/docs/controls/card/#surface_tint_color)
    * [`variant`](https://flet.dev/docs/controls/card/#variant)


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
