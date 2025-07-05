[Skip to main content](https://flet.dev/docs/controls/listview/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/listview/)
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
  * [Cookbook](https://flet.dev/docs/controls/listview/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Layout](https://flet.dev/docs/controls/layout)
  * ListView


On this page
# ListView
A scrollable list of controls arranged linearly.
ListView is the most commonly used scrolling control. It displays its children one after another in the scroll direction. In the cross axis, the children are required to fill the ListView.
info
ListView is very effective for large lists (thousands of items). Prefer it over [`Column`](https://flet.dev/docs/controls/column) or [`Row`](https://flet.dev/docs/controls/row) for smooth scrolling.
## Examples[​](https://flet.dev/docs/controls/listview/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/layout/listview)
### Auto-scrolling ListView with Toggle[​](https://flet.dev/docs/controls/listview/#auto-scrolling-listview-with-toggle "Direct link to Auto-scrolling ListView with Toggle")
python/controls/layout/list-view/listview-toggle-scroll.py
```
from time import sleepimport flet as ftdefmain(page: ft.Page):defchange_auto_scroll(e):print("Change auto scroll triggered")    lv.auto_scroll =not lv.auto_scroll    page.update()  lv = ft.ListView(spacing=10, padding=20, width=150, auto_scroll=True)  lvc = ft.Container(    content=lv,    bgcolor=ft.Colors.GREY_500,)  sw = ft.Switch(    thumb_icon=ft.Icons.LIST_OUTLINED,    value=True,    label="Auto-scroll",    label_position=ft.LabelPosition.RIGHT,    on_change=change_auto_scroll,)  c = ft.Row([lvc, sw],    expand=True,    vertical_alignment=ft.CrossAxisAlignment.START,)  count =1for i inrange(0,60):    lv.controls.append(ft.Text(f"Line {count}", color=ft.Colors.ON_SECONDARY))    count +=1  page.add(c)for i inrange(0,60):    sleep(1)    lv.controls.append(ft.Text(f"Line {count}", color=ft.Colors.ON_SECONDARY))    count +=1    page.update()ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/list-view/listview-toggle-scroll.py)
![](https://flet.dev/img/docs/controls/listview/auto-scroll-listview.gif)
## Properties[​](https://flet.dev/docs/controls/listview/#properties "Direct link to Properties")
### `auto_scroll`[​](https://flet.dev/docs/controls/listview/#auto_scroll "Direct link to auto_scroll")
`True` if scrollbar should automatically move its position to the end when children updated. Must be `False` for `scroll_to()` method to work.
Defaults to `False`.
### `build_controls_on_demand`[​](https://flet.dev/docs/controls/listview/#build_controls_on_demand "Direct link to build_controls_on_demand")
Whether the `controls` should be built lazily/on-demand, i.e. only when they are about to become visible. This is particularly useful when dealing with a large number of controls.
Defaults to `True`.
### `cache_extent`[​](https://flet.dev/docs/controls/listview/#cache_extent "Direct link to cache_extent")
Items that fall in the cache area (area before or after the visible area that are about to become visible when the user scrolls) are laid out even though they are not (yet) visible on screen. The cacheExtent describes how many pixels the cache area extends before the leading edge and after the trailing edge of the viewport.
The total extent, which the viewport will try to cover with `controls`, is `cache_extent` before the leading edge + extent of the main axis + `cache_extent` after the trailing edge.
### `clip_behavior`[​](https://flet.dev/docs/controls/listview/#clip_behavior "Direct link to clip_behavior")
The content will be clipped (or not) according to this option.
Value is of type [`ClipBehavior`](https://flet.dev/docs/reference/types/clipbehavior) and defaults to `ClipBehavior.HARD_EDGE`.
### `controls`[​](https://flet.dev/docs/controls/listview/#controls "Direct link to controls")
A list of `Control`s to display inside ListView.
### `divider_thickness`[​](https://flet.dev/docs/controls/listview/#divider_thickness "Direct link to divider_thickness")
If greater than `0` then Divider is used as a spacing between list view items.
### `first_item_prototype`[​](https://flet.dev/docs/controls/listview/#first_item_prototype "Direct link to first_item_prototype")
`True` if the dimensions of the first item should be used as a "prototype" for all other items, i.e. their height or width will be the same as the first item.
Defaults to `False`.
### `horizontal`[​](https://flet.dev/docs/controls/listview/#horizontal "Direct link to horizontal")
`True` to layout ListView items horizontally.
### `item_extent`[​](https://flet.dev/docs/controls/listview/#item_extent "Direct link to item_extent")
A fixed height or width (for `horizontal` ListView) of an item to optimize rendering.
### `on_scroll_interval`[​](https://flet.dev/docs/controls/listview/#on_scroll_interval "Direct link to on_scroll_interval")
Throttling in milliseconds for `on_scroll` event.
Defaults to `10`.
### `padding`[​](https://flet.dev/docs/controls/listview/#padding "Direct link to padding")
The amount of space by which to inset the children.
Value is of type[`Padding`](https://flet.dev/docs/reference/types/padding).
### `reverse`[​](https://flet.dev/docs/controls/listview/#reverse "Direct link to reverse")
Defines whether the scroll view scrolls in the reading direction.
Defaults to `False`.
### `semantic_child_count`[​](https://flet.dev/docs/controls/listview/#semantic_child_count "Direct link to semantic_child_count")
The number of children that will contribute semantic information.
### `spacing`[​](https://flet.dev/docs/controls/listview/#spacing "Direct link to spacing")
The height of Divider between ListView items. No spacing between items if not specified.
## Methods[​](https://flet.dev/docs/controls/listview/#methods "Direct link to Methods")
### `scroll_to(offset, delta, key, duration, curve)`[​](https://flet.dev/docs/controls/listview/#scroll_tooffset-delta-key-duration-curve "Direct link to scroll_tooffset-delta-key-duration-curve")
Moves scroll position to either absolute `offset`, relative `delta` or jump to the control with specified `key`.
See [`Column.scroll_to()`](https://flet.dev/docs/controls/column#scroll_tooffset-delta-key-duration-curve) for method details and examples.
## Events[​](https://flet.dev/docs/controls/listview/#events "Direct link to Events")
### `on_scroll`[​](https://flet.dev/docs/controls/listview/#on_scroll "Direct link to on_scroll")
Fires when scroll position is changed by a user.
Event handler argument is an instance of [`OnScrollEvent`](https://flet.dev/docs/reference/types/onscrollevent) class.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/listview.md)
[PreviousListTile](https://flet.dev/docs/controls/listtile)[NextPage](https://flet.dev/docs/controls/page)
  * [Examples](https://flet.dev/docs/controls/listview/#examples)
    * [Auto-scrolling ListView with Toggle](https://flet.dev/docs/controls/listview/#auto-scrolling-listview-with-toggle)
  * [Properties](https://flet.dev/docs/controls/listview/#properties)
    * [`auto_scroll`](https://flet.dev/docs/controls/listview/#auto_scroll)
    * [`build_controls_on_demand`](https://flet.dev/docs/controls/listview/#build_controls_on_demand)
    * [`cache_extent`](https://flet.dev/docs/controls/listview/#cache_extent)
    * [`clip_behavior`](https://flet.dev/docs/controls/listview/#clip_behavior)
    * [`controls`](https://flet.dev/docs/controls/listview/#controls)
    * [`divider_thickness`](https://flet.dev/docs/controls/listview/#divider_thickness)
    * [`first_item_prototype`](https://flet.dev/docs/controls/listview/#first_item_prototype)
    * [`horizontal`](https://flet.dev/docs/controls/listview/#horizontal)
    * [`item_extent`](https://flet.dev/docs/controls/listview/#item_extent)
    * [`on_scroll_interval`](https://flet.dev/docs/controls/listview/#on_scroll_interval)
    * [`padding`](https://flet.dev/docs/controls/listview/#padding)
    * [`reverse`](https://flet.dev/docs/controls/listview/#reverse)
    * [`semantic_child_count`](https://flet.dev/docs/controls/listview/#semantic_child_count)
    * [`spacing`](https://flet.dev/docs/controls/listview/#spacing)
  * [Methods](https://flet.dev/docs/controls/listview/#methods)
    * [`scroll_to(offset, delta, key, duration, curve)`](https://flet.dev/docs/controls/listview/#scroll_tooffset-delta-key-duration-curve)
  * [Events](https://flet.dev/docs/controls/listview/#events)
    * [`on_scroll`](https://flet.dev/docs/controls/listview/#on_scroll)


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
