[Skip to main content](https://flet.dev/docs/controls/column/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/column/)
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
  * [Cookbook](https://flet.dev/docs/controls/column/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Layout](https://flet.dev/docs/controls/layout)
  * Column


On this page
# Column
A control that displays its children in a vertical array.
To cause a child control to expand and fill the available vertical space set its `expand` property.
## Examples[​](https://flet.dev/docs/controls/column/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/layout/column)
### Column spacing[​](https://flet.dev/docs/controls/column/#column-spacing "Direct link to Column spacing")
![](https://flet.dev/img/docs/controls/column/column-spacing.gif)
python/controls/layout/column/column-spacing.py
```
import flet as ftdefmain(page: ft.Page):defitems(count):    items =[]for i inrange(1, count +1):      items.append(        ft.Container(          content=ft.Text(value=str(i)),          alignment=ft.alignment.center,          width=50,          height=50,          bgcolor=ft.Colors.AMBER,          border_radius=ft.border_radius.all(5),))return itemsdefspacing_slider_change(e):    col.spacing =int(e.control.value)    col.update()  gap_slider = ft.Slider(min=0,max=100,    divisions=10,    value=0,    label="{value}",    width=500,    on_change=spacing_slider_change,)  col = ft.Column(spacing=0, controls=items(5))  page.add(ft.Column([ft.Text("Spacing between items"), gap_slider]), col)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/column/column-spacing.py)
### Column wrapping[​](https://flet.dev/docs/controls/column/#column-wrapping "Direct link to Column wrapping")
![](https://flet.dev/img/docs/controls/column/column-wrapping.gif)
python/controls/layout/column/column-wrap.py
```
import flet as ftHEIGHT =400defmain(page: ft.Page):defitems(count):    items =[]for i inrange(1, count +1):      items.append(        ft.Container(          content=ft.Text(value=str(i)),          alignment=ft.alignment.center,          width=30,          height=30,          bgcolor=ft.Colors.AMBER,          border_radius=ft.border_radius.all(5),))return itemsdefslider_change(e):    col.height =float(e.control.value)    col.update()  width_slider = ft.Slider(min=0,max=HEIGHT,    divisions=20,    value=HEIGHT,    label="{value}",    width=500,    on_change=slider_change,)  col = ft.Column(    wrap=True,    spacing=10,    run_spacing=10,    controls=items(10),    height=HEIGHT,)  page.add(    ft.Column([        ft.Text("Change the column height to see how child items wrap onto multiple columns:"),        width_slider,]),    ft.Container(content=col, bgcolor=ft.Colors.TRANSPARENT),)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/column/column-wrap.py)
### Column vertical alignments[​](https://flet.dev/docs/controls/column/#column-vertical-alignments "Direct link to Column vertical alignments")
![](https://flet.dev/img/docs/controls/column/column-alignment.png)
python/controls/layout/column/column-alignment.py
```
import flet as ftdefmain(page: ft.Page):defitems(count):    items =[]for i inrange(1, count +1):      items.append(        ft.Container(          content=ft.Text(value=str(i)),          alignment=ft.alignment.center,          width=50,          height=50,          bgcolor=ft.Colors.AMBER_500,))return itemsdefcolumn_with_alignment(align: ft.MainAxisAlignment):return ft.Column([        ft.Text(str(align), size=10),        ft.Container(          content=ft.Column(items(3), alignment=align),          bgcolor=ft.Colors.AMBER_100,          height=400,),])  page.add(    ft.Row([        column_with_alignment(ft.MainAxisAlignment.START),        column_with_alignment(ft.MainAxisAlignment.CENTER),        column_with_alignment(ft.MainAxisAlignment.END),        column_with_alignment(ft.MainAxisAlignment.SPACE_BETWEEN),        column_with_alignment(ft.MainAxisAlignment.SPACE_AROUND),        column_with_alignment(ft.MainAxisAlignment.SPACE_EVENLY),],      spacing=30,      alignment=ft.MainAxisAlignment.START,))ft.app(target=main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/column/column-alignment.py)
### Column horizontal alignments[​](https://flet.dev/docs/controls/column/#column-horizontal-alignments "Direct link to Column horizontal alignments")
![](https://flet.dev/img/docs/controls/column/column-horiz-alignment.png)
python/controls/layout/column/column-horiz-alignment.py
```
import flet as ftdefmain(page: ft.Page):defitems(count):    items =[]for i inrange(1, count +1):      items.append(        ft.Container(          content=ft.Text(value=str(i)),          alignment=ft.alignment.center,          width=50,          height=50,          bgcolor=ft.Colors.AMBER_500,))return itemsdefcolumn_with_horiz_alignment(align: ft.CrossAxisAlignment):return ft.Column([        ft.Text(str(align), size=16),        ft.Container(          content=ft.Column(            items(3),            alignment=ft.MainAxisAlignment.START,            horizontal_alignment=align,),          bgcolor=ft.Colors.AMBER_100,          width=100,),])  page.add(    ft.Row([        column_with_horiz_alignment(ft.CrossAxisAlignment.START),        column_with_horiz_alignment(ft.CrossAxisAlignment.CENTER),        column_with_horiz_alignment(ft.CrossAxisAlignment.END),],      spacing=30,      alignment=ft.MainAxisAlignment.START,))ft.app(target=main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/column/column-horiz-alignment.py)
### Infinite scroll list[​](https://flet.dev/docs/controls/column/#infinite-scroll-list "Direct link to Infinite scroll list")
The following example demonstrates adding of list items on-the-fly, as user scroll to the bottom, creating the illusion of infinite list:
python/controls/layout/column/column-infinite-list.py
```
import threadingimport flet as ftclassState:  i =0s = State()sem = threading.Semaphore()defmain(page: ft.Page):defon_scroll(e: ft.OnScrollEvent):if e.pixels >= e.max_scroll_extent -100:if sem.acquire(blocking=False):try:for i inrange(0,10):            cl.controls.append(ft.Text(f"Text line {s.i}", key=str(s.i)))            s.i +=1          cl.update()finally:          sem.release()  cl = ft.Column(    spacing=10,    height=200,    width=200,    scroll=ft.ScrollMode.ALWAYS,    on_scroll_interval=0,    on_scroll=on_scroll,)for i inrange(0,50):    cl.controls.append(ft.Text(f"Text line {s.i}", key=str(s.i)))    s.i +=1  page.add(ft.Container(cl, border=ft.border.all(1)))ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/column/column-infinite-list.py)
### Scrolling column programmatically[​](https://flet.dev/docs/controls/column/#scrolling-column-programmatically "Direct link to Scrolling column programmatically")
![](https://flet.dev/img/docs/controls/column/column-scroll-to.png)
The following example demonstrates various `scroll_to()` options as well as defines a custom scrollbar theme:
python/controls/layout/column/column-scroll-misc.py
```
import flet as ftdefmain(page: ft.Page):  page.theme = ft.Theme(    scrollbar_theme=ft.ScrollbarTheme(      track_color={        ft.ControlState.HOVERED: ft.Colors.AMBER,        ft.ControlState.DEFAULT: ft.Colors.TRANSPARENT,},      track_visibility=True,      track_border_color=ft.Colors.BLUE,      thumb_visibility=True,      thumb_color={        ft.ControlState.HOVERED: ft.Colors.RED,        ft.ControlState.DEFAULT: ft.Colors.GREY_300,},      thickness=30,      radius=15,      main_axis_margin=5,      cross_axis_margin=10,# interactive=False,))  cl = ft.Column(    spacing=10,    height=200,    width=float("inf"),    scroll=ft.ScrollMode.ALWAYS,)for i inrange(0,100):    cl.controls.append(ft.Text(f"Text line {i}", key=str(i)))defscroll_to_offset(e):    cl.scroll_to(offset=500, duration=1000)defscroll_to_start(e):    cl.scroll_to(offset=0, duration=1000)defscroll_to_end(e):    cl.scroll_to(offset=-1, duration=2000, curve=ft.AnimationCurve.EASE_IN_OUT)defscroll_to_key(e):    cl.scroll_to(key="20", duration=1000)defscroll_to_delta(e):    cl.scroll_to(delta=100, duration=200)defscroll_to_minus_delta(e):    cl.scroll_to(delta=-100, duration=200)  page.add(    ft.Container(cl, border=ft.border.all(1)),    ft.ElevatedButton("Scroll to offset 500", on_click=scroll_to_offset),    ft.Row([        ft.ElevatedButton("Scroll -100", on_click=scroll_to_minus_delta),        ft.ElevatedButton("Scroll +100", on_click=scroll_to_delta),]),    ft.ElevatedButton("Scroll to key '20'", on_click=scroll_to_key),    ft.Row([        ft.ElevatedButton("Scroll to start", on_click=scroll_to_start),        ft.ElevatedButton("Scroll to end", on_click=scroll_to_end),]),)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/column/column-scroll-misc.py)
## Properties[​](https://flet.dev/docs/controls/column/#properties "Direct link to Properties")
### `alignment`[​](https://flet.dev/docs/controls/column/#alignment "Direct link to alignment")
How the child Controls should be placed vertically.
Value is of type [`MainAxisAlignment`](https://flet.dev/docs/reference/types/mainaxisalignment).
### `auto_scroll`[​](https://flet.dev/docs/controls/column/#auto_scroll "Direct link to auto_scroll")
`True` if scrollbar should automatically move its position to the end when children updated. Must be `False` for `scroll_to()` method to work.
### `controls`[​](https://flet.dev/docs/controls/column/#controls "Direct link to controls")
A list of Controls to display inside the Column.
### `horizontal_alignment`[​](https://flet.dev/docs/controls/column/#horizontal_alignment "Direct link to horizontal_alignment")
How the child Controls should be placed horizontally.
Value is of type [`CrossAxisAlignment`](https://flet.dev/docs/reference/types/crossaxisalignment) and defaults to `CrossAxisAlignment.START`.
### `on_scroll_interval`[​](https://flet.dev/docs/controls/column/#on_scroll_interval "Direct link to on_scroll_interval")
Throttling in milliseconds for `on_scroll` event.
Defaults to `10`.
### `rtl`[​](https://flet.dev/docs/controls/column/#rtl "Direct link to rtl")
`True` to set text direction to right-to-left.
Defaults to `False`.
### `run_alignment`[​](https://flet.dev/docs/controls/column/#run_alignment "Direct link to run_alignment")
How the runs should be placed in the cross-axis when `wrap=True`.
Value is of type [`MainAxisAlignment`](https://flet.dev/docs/reference/types/mainaxisalignment) and defaults to `MainAxisAlignment.START`.
### `run_spacing`[​](https://flet.dev/docs/controls/column/#run_spacing "Direct link to run_spacing")
Spacing between runs when `wrap=True`. Default value is 10.
### `scroll`[​](https://flet.dev/docs/controls/column/#scroll "Direct link to scroll")
Enables a vertical scrolling for the Column to prevent its content overflow.
Value is of type [`ScrollMode`](https://flet.dev/docs/reference/types/scrollmode) and defaults to `ScrollMode.None`.
### `spacing`[​](https://flet.dev/docs/controls/column/#spacing "Direct link to spacing")
Spacing between the `controls`. It is applied only when `alignment` is set to `MainAxisAlignment.START`, `MainAxisAlignment.END` or `MainAxisAlignment.CENTER`.
Default value is `10` virtual pixels.
### `tight`[​](https://flet.dev/docs/controls/column/#tight "Direct link to tight")
Specifies how much space should be occupied vertically.
Defaults to `False` - allocate all space to children.
### `wrap`[​](https://flet.dev/docs/controls/column/#wrap "Direct link to wrap")
When set to `True` the Column will put child controls into additional columns (runs) if they don't fit a single column.
## Methods[​](https://flet.dev/docs/controls/column/#methods "Direct link to Methods")
### `scroll_to(offset, delta, key, duration, curve)`[​](https://flet.dev/docs/controls/column/#scroll_tooffset-delta-key-duration-curve "Direct link to scroll_tooffset-delta-key-duration-curve")
Moves scroll position to either absolute `offset`, relative `delta` or jump to the control with specified `key`.
`offset` is an absolute value between minimum and maximum extents of a scrollable control, for example:
```
products.scroll_to(offset=100, duration=1000)
```

`offset` could be a negative to scroll from the end of a scrollable. For example, to scroll to the very end:
```
products.scroll_to(offset=-1, duration=1000)
```

`delta` allows moving scroll relatively to the current position. Use positive `delta` to scroll forward and negative `delta` to scroll backward. For example, to move scroll on 50 pixels forward:
```
products.scroll_to(delta=50)
```

`key` allows moving scroll position to a control with specified `key`. Most of Flet controls have `key` property which is translated to Flutter as "global key". `key` must be unique for the entire page/view. For example:
```
import flet as ftdefmain(page: ft.Page):  cl = ft.Column(    spacing=10,    height=200,    width=200,    scroll=ft.ScrollMode.ALWAYS,)for i inrange(0,50):    cl.controls.append(ft.Text(f"Text line {i}", key=str(i)))defscroll_to_key(e):    cl.scroll_to(key="20", duration=1000)  page.add(    ft.Container(cl, border=ft.border.all(1)),    ft.ElevatedButton("Scroll to key '20'", on_click=scroll_to_key),)ft.app(main)
```

note
`scroll_to()` method won't work with `ListView` and `GridView` controls building their items dynamically.
`duration` is scrolling animation duration in milliseconds. Defaults to `0` - no animation.
`curve` configures animation curve. Property value is [`AnimationCurve`](https://flet.dev/docs/reference/types/animationcurve) enum. Defaults to `AnimationCurve.EASE`.
## Events[​](https://flet.dev/docs/controls/column/#events "Direct link to Events")
### `on_scroll`[​](https://flet.dev/docs/controls/column/#on_scroll "Direct link to on_scroll")
Fires when scroll position is changed by a user.
Event handler argument is an instance of [`OnScrollEvent`](https://flet.dev/docs/reference/types/onscrollevent) class.
## Expanding children[​](https://flet.dev/docs/controls/column/#expanding-children "Direct link to Expanding children")
When a child Control is placed into a Column you can "expand" it to fill the available space. Every Control has `expand` property that can have either a boolean value (`True` - expand control to fill all available space) or an integer - an "expand factor" specifying how to divide a free space with other expanded child controls. For example, this code creates a column with a Container taking all available space and a Text control at the bottom serving as a status bar:
```
r = ft.Column([ ft.Container(expand=True, content=ft.Text("Here is search results")), ft.Text("Records found: 10")])
```

The following example with numeric expand factors creates a Column with 3 containers in it and having heights of `20% (1/5)`, `60% (3/5)` and `20% (1/5)` respectively:
```
r = ft.Column([ ft.Container(expand=1, content=ft.Text("Header")), ft.Container(expand=3, content=ft.Text("Body")), ft.Container(expand=1, content=ft.Text("Footer"))])
```

In general, the resulting height of a child in percents is calculated as `expand / sum(all expands) * 100%`.
If you need to give the child Control of the Column the flexibility to expand to fill the available space vertically but not require it to fill the available space, set its `expand_loose` property to `True`.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/column.md)
[PreviousCard](https://flet.dev/docs/controls/card)[NextContainer](https://flet.dev/docs/controls/container)
  * [Examples](https://flet.dev/docs/controls/column/#examples)
    * [Column spacing](https://flet.dev/docs/controls/column/#column-spacing)
    * [Column wrapping](https://flet.dev/docs/controls/column/#column-wrapping)
    * [Column vertical alignments](https://flet.dev/docs/controls/column/#column-vertical-alignments)
    * [Column horizontal alignments](https://flet.dev/docs/controls/column/#column-horizontal-alignments)
    * [Infinite scroll list](https://flet.dev/docs/controls/column/#infinite-scroll-list)
    * [Scrolling column programmatically](https://flet.dev/docs/controls/column/#scrolling-column-programmatically)
  * [Properties](https://flet.dev/docs/controls/column/#properties)
    * [`alignment`](https://flet.dev/docs/controls/column/#alignment)
    * [`auto_scroll`](https://flet.dev/docs/controls/column/#auto_scroll)
    * [`controls`](https://flet.dev/docs/controls/column/#controls)
    * [`horizontal_alignment`](https://flet.dev/docs/controls/column/#horizontal_alignment)
    * [`on_scroll_interval`](https://flet.dev/docs/controls/column/#on_scroll_interval)
    * [`rtl`](https://flet.dev/docs/controls/column/#rtl)
    * [`run_alignment`](https://flet.dev/docs/controls/column/#run_alignment)
    * [`run_spacing`](https://flet.dev/docs/controls/column/#run_spacing)
    * [`scroll`](https://flet.dev/docs/controls/column/#scroll)
    * [`spacing`](https://flet.dev/docs/controls/column/#spacing)
    * [`tight`](https://flet.dev/docs/controls/column/#tight)
    * [`wrap`](https://flet.dev/docs/controls/column/#wrap)
  * [Methods](https://flet.dev/docs/controls/column/#methods)
    * [`scroll_to(offset, delta, key, duration, curve)`](https://flet.dev/docs/controls/column/#scroll_tooffset-delta-key-duration-curve)
  * [Events](https://flet.dev/docs/controls/column/#events)
    * [`on_scroll`](https://flet.dev/docs/controls/column/#on_scroll)
  * [Expanding children](https://flet.dev/docs/controls/column/#expanding-children)


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
