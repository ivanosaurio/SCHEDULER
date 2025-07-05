[Skip to main content](https://flet.dev/docs/controls/gridview/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/gridview/)
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
  * [Cookbook](https://flet.dev/docs/controls/gridview/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Layout](https://flet.dev/docs/controls/layout)
  * GridView


On this page
# GridView
A scrollable, 2D array of controls.
info
GridView is very effective for large lists (thousands of items). Prefer it over wrapping [`Column`](https://flet.dev/docs/controls/column) or [`Row`](https://flet.dev/docs/controls/row) for smooth scrolling. See [Flet Icons Browser](https://github.com/flet-dev/examples/blob/main/python/apps/icons-browser/main.py) for GridView usage example.
## Examples[​](https://flet.dev/docs/controls/gridview/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/layout/gridview)
### Photo gallery[​](https://flet.dev/docs/controls/gridview/#photo-gallery "Direct link to Photo gallery")
![](https://flet.dev/img/docs/controls/gridview/grid-view-example.png)
python/controls/layout/grid-view/photo-gallery.py
```
import flet as ftdefmain(page: ft.Page):  page.title ="GridView Example"  page.theme_mode = ft.ThemeMode.DARK  page.padding =50  page.update()  images = ft.GridView(    expand=1,    runs_count=5,    max_extent=150,    child_aspect_ratio=1.0,    spacing=5,    run_spacing=5,)  page.add(images)for i inrange(0,60):    images.controls.append(      ft.Image(        src=f"https://picsum.photos/150/150?{i}",        fit=ft.ImageFit.NONE,        repeat=ft.ImageRepeat.NO_REPEAT,        border_radius=ft.border_radius.all(10),))  page.update()ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/grid-view/photo-gallery.py)
## Properties[​](https://flet.dev/docs/controls/gridview/#properties "Direct link to Properties")
### `auto_scroll`[​](https://flet.dev/docs/controls/gridview/#auto_scroll "Direct link to auto_scroll")
`True` if scrollbar should automatically move its position to the end when children updated. Must be `False` for `scroll_to()` method to work.
### `cache_extent`[​](https://flet.dev/docs/controls/gridview/#cache_extent "Direct link to cache_extent")
Items that fall in the cache area (area before or after the visible area that are about to become visible when the user scrolls) are laid out even though they are not (yet) visible on screen. The cacheExtent describes how many pixels the cache area extends before the leading edge and after the trailing edge of the viewport.
The total extent, which the viewport will try to cover with `controls`, is `cache_extent` before the leading edge + extent of the main axis + `cache_extent` after the trailing edge.
### `child_aspect_ratio`[​](https://flet.dev/docs/controls/gridview/#child_aspect_ratio "Direct link to child_aspect_ratio")
The ratio of the cross-axis to the main-axis extent of each child.
### `clip_behavior`[​](https://flet.dev/docs/controls/gridview/#clip_behavior "Direct link to clip_behavior")
The content will be clipped (or not) according to this option.
Value is of type [`ClipBehavior`](https://flet.dev/docs/reference/types/clipbehavior) and defaults to `ClipBehavior.HARD_EDGE`.
### `controls`[​](https://flet.dev/docs/controls/gridview/#controls "Direct link to controls")
A list of `Control`s to display inside GridView.
### `horizontal`[​](https://flet.dev/docs/controls/gridview/#horizontal "Direct link to horizontal")
`True` to layout GridView items horizontally.
### `max_extent`[​](https://flet.dev/docs/controls/gridview/#max_extent "Direct link to max_extent")
The maximum width or height of the grid item.
### `on_scroll_interval`[​](https://flet.dev/docs/controls/gridview/#on_scroll_interval "Direct link to on_scroll_interval")
Throttling in milliseconds for `on_scroll` event.
Defaults to `10`.
### `padding`[​](https://flet.dev/docs/controls/gridview/#padding "Direct link to padding")
The amount of space by which to inset the children.
Padding is an instance of [`Padding`](https://flet.dev/docs/reference/types/padding).
### `reverse`[​](https://flet.dev/docs/controls/gridview/#reverse "Direct link to reverse")
Defines whether the scroll view scrolls in the reading direction.
Defaults to `False`.
### `run_spacing`[​](https://flet.dev/docs/controls/gridview/#run_spacing "Direct link to run_spacing")
The number of logical pixels between each child along the cross axis.
### `runs_count`[​](https://flet.dev/docs/controls/gridview/#runs_count "Direct link to runs_count")
The number of children in the cross axis.
### `semantic_child_count`[​](https://flet.dev/docs/controls/gridview/#semantic_child_count "Direct link to semantic_child_count")
The number of children that will contribute semantic information.
### `spacing`[​](https://flet.dev/docs/controls/gridview/#spacing "Direct link to spacing")
The number of logical pixels between each child along the main axis.
## Methods[​](https://flet.dev/docs/controls/gridview/#methods "Direct link to Methods")
### `scroll_to(offset, delta, key, duration, curve)`[​](https://flet.dev/docs/controls/gridview/#scroll_tooffset-delta-key-duration-curve "Direct link to scroll_tooffset-delta-key-duration-curve")
Moves scroll position to either absolute `offset`, relative `delta` or jump to the control with specified `key`.
See [`Column.scroll_to()`](https://flet.dev/docs/controls/column#scroll_tooffset-delta-key-duration-curve) for method details and examples.
## Events[​](https://flet.dev/docs/controls/gridview/#events "Direct link to Events")
### `on_scroll`[​](https://flet.dev/docs/controls/gridview/#on_scroll "Direct link to on_scroll")
Fires when scroll position is changed by a user.
Event handler argument is an instance of [`OnScrollEvent`](https://flet.dev/docs/reference/types/onscrollevent) class.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/gridview.md)
[PreviousExpansionTile](https://flet.dev/docs/controls/expansiontile)[NextListTile](https://flet.dev/docs/controls/listtile)
  * [Examples](https://flet.dev/docs/controls/gridview/#examples)
    * [Photo gallery](https://flet.dev/docs/controls/gridview/#photo-gallery)
  * [Properties](https://flet.dev/docs/controls/gridview/#properties)
    * [`auto_scroll`](https://flet.dev/docs/controls/gridview/#auto_scroll)
    * [`cache_extent`](https://flet.dev/docs/controls/gridview/#cache_extent)
    * [`child_aspect_ratio`](https://flet.dev/docs/controls/gridview/#child_aspect_ratio)
    * [`clip_behavior`](https://flet.dev/docs/controls/gridview/#clip_behavior)
    * [`controls`](https://flet.dev/docs/controls/gridview/#controls)
    * [`horizontal`](https://flet.dev/docs/controls/gridview/#horizontal)
    * [`max_extent`](https://flet.dev/docs/controls/gridview/#max_extent)
    * [`on_scroll_interval`](https://flet.dev/docs/controls/gridview/#on_scroll_interval)
    * [`padding`](https://flet.dev/docs/controls/gridview/#padding)
    * [`reverse`](https://flet.dev/docs/controls/gridview/#reverse)
    * [`run_spacing`](https://flet.dev/docs/controls/gridview/#run_spacing)
    * [`runs_count`](https://flet.dev/docs/controls/gridview/#runs_count)
    * [`semantic_child_count`](https://flet.dev/docs/controls/gridview/#semantic_child_count)
    * [`spacing`](https://flet.dev/docs/controls/gridview/#spacing)
  * [Methods](https://flet.dev/docs/controls/gridview/#methods)
    * [`scroll_to(offset, delta, key, duration, curve)`](https://flet.dev/docs/controls/gridview/#scroll_tooffset-delta-key-duration-curve)
  * [Events](https://flet.dev/docs/controls/gridview/#events)
    * [`on_scroll`](https://flet.dev/docs/controls/gridview/#on_scroll)


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
