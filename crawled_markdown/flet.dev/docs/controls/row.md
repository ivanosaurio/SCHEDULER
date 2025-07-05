[Skip to main content](https://flet.dev/docs/controls/row/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/row/)
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
  * [Cookbook](https://flet.dev/docs/controls/row/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Layout](https://flet.dev/docs/controls/layout)
  * Row


On this page
# Row
A control that displays its children in a horizontal array.
To cause a child control to expand and fill the available horizontal space set its `expand` property.
## Examples[​](https://flet.dev/docs/controls/row/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/layout/row)
### Row spacing[​](https://flet.dev/docs/controls/row/#row-spacing "Direct link to Row spacing")
![](https://flet.dev/img/docs/controls/row/row-spacing.gif)
python/controls/layout/row/row-spacing.py
```
import flet as ftdefmain(page: ft.Page):defitems(count):    items =[]for i inrange(1, count +1):      items.append(        ft.Container(          content=ft.Text(value=str(i)),          alignment=ft.alignment.center,          width=50,          height=50,          bgcolor=ft.Colors.AMBER,          border_radius=ft.border_radius.all(5),))return itemsdefgap_slider_change(e):    row.spacing =int(e.control.value)    row.update()  gap_slider = ft.Slider(min=0,max=50,    divisions=50,    value=0,    label="{value}",    on_change=gap_slider_change,)  row = ft.Row(spacing=0, controls=items(10), scroll=ft.ScrollMode.AUTO)  page.add(ft.Column([ft.Text("Spacing between items"), gap_slider]), row)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/row/row-spacing.py)
### Row wrapping[​](https://flet.dev/docs/controls/row/#row-wrapping "Direct link to Row wrapping")
![](https://flet.dev/img/docs/controls/row/row-wrap.gif)
python/controls/layout/row/row-wrap.py
```
import flet as ftdefmain(page: ft.Page):defitems(count):    items =[]for i inrange(1, count +1):      items.append(        ft.Container(          content=ft.Text(value=str(i)),          alignment=ft.alignment.center,          width=50,          height=50,          bgcolor=ft.Colors.AMBER,          border_radius=ft.border_radius.all(5),))return itemsdefslider_change(e):    row.width =float(e.control.value)    row.update()  width_slider = ft.Slider(min=0,max=page.window.width,    divisions=20,    value=page.window.width,    label="{value}",    on_change=slider_change,)  row = ft.Row(    wrap=True,    spacing=10,    run_spacing=10,    controls=items(30),    width=page.window.width,)  page.add(    ft.Column([        ft.Text("Change the row width to see how child items wrap onto multiple rows:"),        width_slider,]),    row,)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/row/row-wrap.py)
### Row horizontal alignments[​](https://flet.dev/docs/controls/row/#row-horizontal-alignments "Direct link to Row horizontal alignments")
![](https://flet.dev/img/docs/controls/row/row-alignment.png)
python/controls/layout/row/row-alignment.py
```
import flet as ftdefmain(page: ft.Page):  page.scroll = ft.ScrollMode.AUTOdefitems(count):    items =[]for i inrange(1, count +1):      items.append(        ft.Container(          content=ft.Text(value=str(i)),          alignment=ft.alignment.center,          width=50,          height=50,          bgcolor=ft.Colors.AMBER_500,))return itemsdefrow_with_alignment(align: ft.MainAxisAlignment):return ft.Column([        ft.Text(str(align), size=16),        ft.Container(          content=ft.Row(items(3), alignment=align),          bgcolor=ft.Colors.AMBER_100,),],)  page.add(    ft.Column([        row_with_alignment(ft.MainAxisAlignment.START),        row_with_alignment(ft.MainAxisAlignment.CENTER),        row_with_alignment(ft.MainAxisAlignment.END),        row_with_alignment(ft.MainAxisAlignment.SPACE_BETWEEN),        row_with_alignment(ft.MainAxisAlignment.SPACE_AROUND),        row_with_alignment(ft.MainAxisAlignment.SPACE_EVENLY),],      scroll=ft.ScrollMode.AUTO,))ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/row/row-alignment.py)
### Row vertical[​](https://flet.dev/docs/controls/row/#row-vertical "Direct link to Row vertical")
![](https://flet.dev/img/docs/controls/row/row-vertical-alignment.png)
python/controls/layout/row/row-vert-alignment.py
```
import flet as ftdefmain(page: ft.Page):defitems(count):    items =[]for i inrange(1, count +1):      items.append(        ft.Container(          content=ft.Text(value=str(i)),          alignment=ft.alignment.center,          width=50,          height=50,          bgcolor=ft.Colors.AMBER_500,))return itemsdefrow_with_vertical_alignment(align: ft.CrossAxisAlignment):return ft.Column([        ft.Text(str(align), size=16),        ft.Container(          content=ft.Row(items(3), vertical_alignment=align),          bgcolor=ft.Colors.AMBER_100,          height=150,),])  page.add(    row_with_vertical_alignment(ft.CrossAxisAlignment.START),    row_with_vertical_alignment(ft.CrossAxisAlignment.CENTER),    row_with_vertical_alignment(ft.CrossAxisAlignment.END),)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/row/row-vert-alignment.py)
## Properties[​](https://flet.dev/docs/controls/row/#properties "Direct link to Properties")
### `alignment`[​](https://flet.dev/docs/controls/row/#alignment "Direct link to alignment")
How the child Controls should be placed horizontally.
Value is of type [`MainAxisAlignment`](https://flet.dev/docs/reference/types/mainaxisalignment) and defaults to `MainAxisAlignment.START`.
### `auto_scroll`[​](https://flet.dev/docs/controls/row/#auto_scroll "Direct link to auto_scroll")
`True` if scrollbar should automatically move its position to the end when children updated. Must be `False` for `scroll_to()` method to work.
### `controls`[​](https://flet.dev/docs/controls/row/#controls "Direct link to controls")
A list of Controls to display inside the Row.
### `rtl`[​](https://flet.dev/docs/controls/row/#rtl "Direct link to rtl")
`True` to set text direction to right-to-left.
Defaults to `False`.
### `run_alignment`[​](https://flet.dev/docs/controls/row/#run_alignment "Direct link to run_alignment")
How the runs should be placed in the cross-axis when `wrap=True`.
Value is of type [`MainAxisAlignment`](https://flet.dev/docs/reference/types/mainaxisalignment) and defaults to `MainAxisAlignment.START`.
### `run_spacing`[​](https://flet.dev/docs/controls/row/#run_spacing "Direct link to run_spacing")
Spacing between runs when `wrap=True`.
Defaults to `10`.
### `scroll`[​](https://flet.dev/docs/controls/row/#scroll "Direct link to scroll")
Enables horizontal scrolling for the Row to prevent its content overflow.
Value is of type [`ScrollMode`](https://flet.dev/docs/reference/types/scrollmode).
### `spacing`[​](https://flet.dev/docs/controls/row/#spacing "Direct link to spacing")
Spacing between controls in a row. Default value is 10 virtual pixels. Spacing is applied only when `alignment` is set to `MainAxisAlignment.START`, `MainAxisAlignment.END` or `MainAxisAlignment.CENTER`.
### `on_scroll_interval`[​](https://flet.dev/docs/controls/row/#on_scroll_interval "Direct link to on_scroll_interval")
Throttling in milliseconds for `on_scroll` event.
Defaults to `10`.
### `tight`[​](https://flet.dev/docs/controls/row/#tight "Direct link to tight")
Specifies how much space should be occupied horizontally.
Defaults to `False`, meaning all space is allocated to children.
### `vertical_alignment`[​](https://flet.dev/docs/controls/row/#vertical_alignment "Direct link to vertical_alignment")
How the child Controls should be placed vertically.
Value is of type [`CrossAxisAlignment`](https://flet.dev/docs/reference/types/crossaxisalignment) and defaults to `CrossAxisAlignment.START`.
### `wrap`[​](https://flet.dev/docs/controls/row/#wrap "Direct link to wrap")
When set to `True` the Row will put child controls into additional rows (runs) if they don't fit a single row.
## Methods[​](https://flet.dev/docs/controls/row/#methods "Direct link to Methods")
### `scroll_to(offset, delta, key, duration, curve)`[​](https://flet.dev/docs/controls/row/#scroll_tooffset-delta-key-duration-curve "Direct link to scroll_tooffset-delta-key-duration-curve")
Moves scroll position to either absolute `offset`, relative `delta` or jump to the control with specified `key`.
See [`Column.scroll_to()`](https://flet.dev/docs/controls/column#scroll_tooffset-delta-key-duration-curve) for method details and examples.
## Events[​](https://flet.dev/docs/controls/row/#events "Direct link to Events")
### `on_scroll`[​](https://flet.dev/docs/controls/row/#on_scroll "Direct link to on_scroll")
Fires when scroll position is changed by a user.
Event handler argument is an instance of [`OnScrollEvent`](https://flet.dev/docs/reference/types/onscrollevent) class.
## Expanding children[​](https://flet.dev/docs/controls/row/#expanding-children "Direct link to Expanding children")
When a child Control is placed into a Row you can "expand" it to fill the available space. Every Control has `expand` property that can have either a boolean value (`True` - expand control to fill all available space) or an integer - an "expand factor" specifying how to divide a free space with other expanded child controls. For example, this code creates a row with a TextField taking all available space and an ElevatedButton next to it:
```
r = ft.Row([ ft.TextField(hint_text="Enter your name", expand=True), ft.ElevatedButton(text="Join chat")])
```

The following example with numeric expand factors creates a Row with 3 containers in it and having widths of `20% (1/5)`, `60% (3/5)` and `20% (1/5)` respectively:
```
r = ft.Row([ ft.Container(expand=1, content=ft.Text("A")), ft.Container(expand=3, content=ft.Text("B")), ft.Container(expand=1, content=ft.Text("C"))])
```

In general, the resulting width of a child in percents is calculated as `expand / sum(all expands) * 100%`.
If you need to give the child Control of the Row the flexibility to expand to fill the available space horizontally but not require it to fill the available space, set its `expand_loose` property to `True`.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/row.md)
[PreviousResponsiveRow](https://flet.dev/docs/controls/responsiverow)[NextSafeArea](https://flet.dev/docs/controls/safearea)
  * [Examples](https://flet.dev/docs/controls/row/#examples)
    * [Row spacing](https://flet.dev/docs/controls/row/#row-spacing)
    * [Row wrapping](https://flet.dev/docs/controls/row/#row-wrapping)
    * [Row horizontal alignments](https://flet.dev/docs/controls/row/#row-horizontal-alignments)
    * [Row vertical](https://flet.dev/docs/controls/row/#row-vertical)
  * [Properties](https://flet.dev/docs/controls/row/#properties)
    * [`alignment`](https://flet.dev/docs/controls/row/#alignment)
    * [`auto_scroll`](https://flet.dev/docs/controls/row/#auto_scroll)
    * [`controls`](https://flet.dev/docs/controls/row/#controls)
    * [`rtl`](https://flet.dev/docs/controls/row/#rtl)
    * [`run_alignment`](https://flet.dev/docs/controls/row/#run_alignment)
    * [`run_spacing`](https://flet.dev/docs/controls/row/#run_spacing)
    * [`scroll`](https://flet.dev/docs/controls/row/#scroll)
    * [`spacing`](https://flet.dev/docs/controls/row/#spacing)
    * [`on_scroll_interval`](https://flet.dev/docs/controls/row/#on_scroll_interval)
    * [`tight`](https://flet.dev/docs/controls/row/#tight)
    * [`vertical_alignment`](https://flet.dev/docs/controls/row/#vertical_alignment)
    * [`wrap`](https://flet.dev/docs/controls/row/#wrap)
  * [Methods](https://flet.dev/docs/controls/row/#methods)
    * [`scroll_to(offset, delta, key, duration, curve)`](https://flet.dev/docs/controls/row/#scroll_tooffset-delta-key-duration-curve)
  * [Events](https://flet.dev/docs/controls/row/#events)
    * [`on_scroll`](https://flet.dev/docs/controls/row/#on_scroll)
  * [Expanding children](https://flet.dev/docs/controls/row/#expanding-children)


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
