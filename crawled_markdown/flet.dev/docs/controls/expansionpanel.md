[Skip to main content](https://flet.dev/docs/controls/expansionpanel/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/expansionpanel/)
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
  * [Cookbook](https://flet.dev/docs/controls/expansionpanel/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Layout](https://flet.dev/docs/controls/layout)
  * ExpansionPanelList


On this page
# ExpansionPanelList
A material expansion panel list that lays out its children and animates expansions.
## Examples[​](https://flet.dev/docs/controls/expansionpanel/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/layout/expansionpanellist)
### Simple Example[​](https://flet.dev/docs/controls/expansionpanel/#simple-example "Direct link to Simple Example")
python/controls/layout/expansion-panel-list/expansion-panel-list.py
```
import flet as ftdefmain(page: ft.Page):  page.theme_mode = ft.ThemeMode.LIGHTdefhandle_change(e: ft.ControlEvent):print(f"change on panel with index {e.data}")defhandle_delete(e: ft.ControlEvent):    panel.controls.remove(e.control.data)    page.update()  panel = ft.ExpansionPanelList(    expand_icon_color=ft.Colors.AMBER,    elevation=8,    divider_color=ft.Colors.AMBER,    on_change=handle_change,    controls=[      ft.ExpansionPanel(# has no header and content - placeholders will be used        bgcolor=ft.Colors.BLUE_400,        expanded=True,)],)  colors =[    ft.Colors.GREEN_500,    ft.Colors.BLUE_800,    ft.Colors.RED_800,]for i inrange(3):    bgcolor = colors[i %len(colors)]    exp = ft.ExpansionPanel(      bgcolor=bgcolor,      header=ft.ListTile(title=ft.Text(f"Panel {i}"), bgcolor=bgcolor),)    exp.content = ft.ListTile(      title=ft.Text(f"This is in Panel {i}"),      subtitle=ft.Text(f"Press the icon to delete panel {i}"),      trailing=ft.IconButton(ft.Icons.DELETE, on_click=handle_delete, data=exp),      bgcolor=bgcolor,)    panel.controls.append(exp)  page.add(panel)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/expansion-panel-list/expansion-panel-list.py)
![](https://flet.dev/img/docs/controls/expansion-panel/expansion-panel.gif)
## `ExpansionPanelList` Properties[​](https://flet.dev/docs/controls/expansionpanel/#expansionpanellist-properties "Direct link to expansionpanellist-properties")
### `controls`[​](https://flet.dev/docs/controls/expansionpanel/#controls "Direct link to controls")
A list of `ExpansionPanel`s to display inside `ExpansionPanelList`.
### `divider_color`[​](https://flet.dev/docs/controls/expansionpanel/#divider_color "Direct link to divider_color")
The [color](https://flet.dev/docs/reference/colors) of the divider when `ExpansionPanel.expanded` is `False`.
### `elevation`[​](https://flet.dev/docs/controls/expansionpanel/#elevation "Direct link to elevation")
Defines the elevation of the children controls (`ExpansionPanel`s), while it is expanded. Default value is `2`.
### `expanded_header_padding`[​](https://flet.dev/docs/controls/expansionpanel/#expanded_header_padding "Direct link to expanded_header_padding")
Defines the padding around the header when expanded.
Padding value is an instance of [`Padding`](https://flet.dev/docs/reference/types/padding) class. Default value is `padding.symmetric(vertical=16.0)`.
### `expanded_icon_color`[​](https://flet.dev/docs/controls/expansionpanel/#expanded_icon_color "Direct link to expanded_icon_color")
The [color](https://flet.dev/docs/reference/colors) of the icon. Defaults to `colors.BLACK_54` in light theme mode and `colors.WHITE_60` in dark theme mode.
### `spacing`[​](https://flet.dev/docs/controls/expansionpanel/#spacing "Direct link to spacing")
The size of the gap between the `ExpansionPanel`s when expanded.
## Events[​](https://flet.dev/docs/controls/expansionpanel/#events "Direct link to Events")
### `on_change`[​](https://flet.dev/docs/controls/expansionpanel/#on_change "Direct link to on_change")
Fires when an `ExpansionPanel` is expanded or collapsed. The event's data (`e.data`), contains the index of the `ExpansionPanel` which triggered this event.
## `ExpansionPanel` properties[​](https://flet.dev/docs/controls/expansionpanel/#expansionpanel-properties "Direct link to expansionpanel-properties")
### `bgcolor`[​](https://flet.dev/docs/controls/expansionpanel/#bgcolor "Direct link to bgcolor")
The background [color](https://flet.dev/docs/reference/colors) of the panel.
### `content`[​](https://flet.dev/docs/controls/expansionpanel/#content "Direct link to content")
The control to be found in the body of the `ExpansionPanel`. It is displayed below the `header` when the panel is expanded.
If this property is `None`, the `ExpansionPanel` will have a placeholder `Text` as content.
### `can_tap_header`[​](https://flet.dev/docs/controls/expansionpanel/#can_tap_header "Direct link to can_tap_header")
If `True`, tapping on the panel's `header` will expand or collapse it. Defaults to `False`.
### `expanded`[​](https://flet.dev/docs/controls/expansionpanel/#expanded "Direct link to expanded")
Whether expanded(`True`) or collapsed(`False`). Defaults to `False`.
### `header`[​](https://flet.dev/docs/controls/expansionpanel/#header "Direct link to header")
The control to be found in the header of the `ExpansionPanel`. If `can_tap_header` is `True`, tapping on the header will expand or collapse the panel.
If this property is `None`, the `ExpansionPanel` will have a placeholder `Text` as header.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/expansionpanel.md)
[PreviousDivider](https://flet.dev/docs/controls/divider)[NextExpansionTile](https://flet.dev/docs/controls/expansiontile)
  * [Examples](https://flet.dev/docs/controls/expansionpanel/#examples)
    * [Simple Example](https://flet.dev/docs/controls/expansionpanel/#simple-example)
  * [`ExpansionPanelList` Properties](https://flet.dev/docs/controls/expansionpanel/#expansionpanellist-properties)
    * [`controls`](https://flet.dev/docs/controls/expansionpanel/#controls)
    * [`divider_color`](https://flet.dev/docs/controls/expansionpanel/#divider_color)
    * [`elevation`](https://flet.dev/docs/controls/expansionpanel/#elevation)
    * [`expanded_header_padding`](https://flet.dev/docs/controls/expansionpanel/#expanded_header_padding)
    * [`expanded_icon_color`](https://flet.dev/docs/controls/expansionpanel/#expanded_icon_color)
    * [`spacing`](https://flet.dev/docs/controls/expansionpanel/#spacing)
  * [Events](https://flet.dev/docs/controls/expansionpanel/#events)
    * [`on_change`](https://flet.dev/docs/controls/expansionpanel/#on_change)
  * [`ExpansionPanel` properties](https://flet.dev/docs/controls/expansionpanel/#expansionpanel-properties)
    * [`bgcolor`](https://flet.dev/docs/controls/expansionpanel/#bgcolor)
    * [`content`](https://flet.dev/docs/controls/expansionpanel/#content)
    * [`can_tap_header`](https://flet.dev/docs/controls/expansionpanel/#can_tap_header)
    * [`expanded`](https://flet.dev/docs/controls/expansionpanel/#expanded)
    * [`header`](https://flet.dev/docs/controls/expansionpanel/#header)


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
