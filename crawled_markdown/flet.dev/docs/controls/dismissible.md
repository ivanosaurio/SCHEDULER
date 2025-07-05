[Skip to main content](https://flet.dev/docs/controls/dismissible/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/dismissible/)
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
  * [Cookbook](https://flet.dev/docs/controls/dismissible/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Layout](https://flet.dev/docs/controls/layout)
  * Dismissible


On this page
# Dismissible
A control that can be dismissed by dragging in the indicated `dismiss_direction`. When dragged or flung in the specified `dismiss_direction`, it's content smoothly slides out of view.
## Examples[​](https://flet.dev/docs/controls/dismissible/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/layout/dismissible)
### Dismissible ListView Tiles[​](https://flet.dev/docs/controls/dismissible/#dismissible-listview-tiles "Direct link to Dismissible ListView Tiles")
python/controls/layout/dismissable/dismissable-listview.py
```
import flet as ftdefmain(page):defhandle_dlg_action_clicked(e):    page.close(dlg)    dlg.data.confirm_dismiss(e.control.data)  dlg = ft.AlertDialog(    modal=True,    title=ft.Text("Please confirm"),    content=ft.Text("Do you really want to delete this item?"),    actions=[      ft.TextButton("Yes", data=True, on_click=handle_dlg_action_clicked),      ft.TextButton("No", data=False, on_click=handle_dlg_action_clicked),],    actions_alignment=ft.MainAxisAlignment.CENTER,)defhandle_confirm_dismiss(e: ft.DismissibleDismissEvent):if e.direction == ft.DismissDirection.END_TO_START:# right-to-left slide# save current dismissible to dialog's data, for confirmation in handle_dlg_action_clicked      dlg.data = e.control      page.open(dlg)else:# left-to-right slide      e.control.confirm_dismiss(True)defhandle_dismiss(e):    e.control.parent.controls.remove(e.control)    page.update()defhandle_update(e: ft.DismissibleUpdateEvent):print(f"Update - direction: {e.direction}, progress: {e.progress}, reached: {e.reached}, previous_reached: {e.previous_reached}")  page.add(    ft.ListView(      expand=True,      controls=[        ft.Dismissible(          content=ft.ListTile(title=ft.Text(f"Item {i}")),          dismiss_direction=ft.DismissDirection.HORIZONTAL,          background=ft.Container(bgcolor=ft.Colors.GREEN),          secondary_background=ft.Container(bgcolor=ft.Colors.RED),          on_dismiss=handle_dismiss,          on_update=handle_update,          on_confirm_dismiss=handle_confirm_dismiss,          dismiss_thresholds={            ft.DismissDirection.END_TO_START:0.2,            ft.DismissDirection.START_TO_END:0.2,},)for i inrange(10)],))ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/dismissable/dismissable-listview.py)
![](https://flet.dev/img/docs/controls/dismissible/dismissible-listview.gif)
## Properties[​](https://flet.dev/docs/controls/dismissible/#properties "Direct link to Properties")
### `background`[​](https://flet.dev/docs/controls/dismissible/#background "Direct link to background")
A Control that is stacked behind the `content`.
If `secondary_background` is also specified, then this control only appears when the content has been dragged down or to the right.
### `content`[​](https://flet.dev/docs/controls/dismissible/#content "Direct link to content")
A child Control contained by the Dismissible.
### `cross_axis_end_offset`[​](https://flet.dev/docs/controls/dismissible/#cross_axis_end_offset "Direct link to cross_axis_end_offset")
Specifies the end offset along the main axis once the card has been dismissed.
If non-zero value is given then widget moves in cross direction depending on whether it is positive or negative.
### `dismiss_direction`[​](https://flet.dev/docs/controls/dismissible/#dismiss_direction "Direct link to dismiss_direction")
The direction in which the control can be dismissed.
Value is of type [`DismissDirection`](https://flet.dev/docs/reference/types/dismissdirection).
### `dismiss_thresholds`[​](https://flet.dev/docs/controls/dismissible/#dismiss_thresholds "Direct link to dismiss_thresholds")
The offset threshold the item has to be dragged in order to be considered dismissed.
Ex: a threshold of `0.4` (the default) means that the item has to be dragged _at least_ 40% in order for it to be dismissed.
It is specified as a dictionary where the key is of type [`DismissDirection`](https://flet.dev/docs/reference/types/dismissdirection) and the value is the threshold(fractional/decimal value between `0.0` and `1.0`):
```
ft.Dismissible(# ...  dismiss_thresholds={    ft.DismissDirection.VERTICAL:0.1,    ft.DismissDirection.START_TO_END:0.7})
```

### `movement_duration`[​](https://flet.dev/docs/controls/dismissible/#movement_duration "Direct link to movement_duration")
The duration for card to dismiss or to come back to original position if not dismissed.
### `resize_duration`[​](https://flet.dev/docs/controls/dismissible/#resize_duration "Direct link to resize_duration")
The amount of time the control will spend contracting before `on_dismiss` is called.
### `secondary_background`[​](https://flet.dev/docs/controls/dismissible/#secondary_background "Direct link to secondary_background")
A control that is stacked behind the `content` and is exposed when the `content` has been dragged up or to the left.
Has no effect if `background` is not specified.
## Events[​](https://flet.dev/docs/controls/dismissible/#events "Direct link to Events")
### `on_confirm_dismiss`[​](https://flet.dev/docs/controls/dismissible/#on_confirm_dismiss "Direct link to on_confirm_dismiss")
Gives the app an opportunity to confirm or veto a pending dismissal. The widget cannot be dragged again until the returned this pending dismissal is resolved.
To resolve the pending dismissal, call the `confirm_dismiss(dismiss)` method passing it a boolean representing the decision. If `True`, then the control will be dismissed, otherwise it will be moved back to its original location.
See the example at the top of this page for a possible implementation.
### `on_dismiss`[​](https://flet.dev/docs/controls/dismissible/#on_dismiss "Direct link to on_dismiss")
Fires when this control has been dismissed, after finishing resizing.
### `on_resize`[​](https://flet.dev/docs/controls/dismissible/#on_resize "Direct link to on_resize")
Fires when this control changes size, for example, when contracting before being dismissed.
### `on_update`[​](https://flet.dev/docs/controls/dismissible/#on_update "Direct link to on_update")
Fires when this control has been dragged.
## Methods[​](https://flet.dev/docs/controls/dismissible/#methods "Direct link to Methods")
### `confirm_dismiss(dismiss: bool)`[​](https://flet.dev/docs/controls/dismissible/#confirm_dismissdismiss-bool "Direct link to confirm_dismissdismiss-bool")
Resolves the pending dismissal. To be called while handling the `on_confirm_dismiss` event.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/dismissible.md)
[PreviousDataTable](https://flet.dev/docs/controls/datatable)[NextDivider](https://flet.dev/docs/controls/divider)
  * [Examples](https://flet.dev/docs/controls/dismissible/#examples)
    * [Dismissible ListView Tiles](https://flet.dev/docs/controls/dismissible/#dismissible-listview-tiles)
  * [Properties](https://flet.dev/docs/controls/dismissible/#properties)
    * [`background`](https://flet.dev/docs/controls/dismissible/#background)
    * [`content`](https://flet.dev/docs/controls/dismissible/#content)
    * [`cross_axis_end_offset`](https://flet.dev/docs/controls/dismissible/#cross_axis_end_offset)
    * [`dismiss_direction`](https://flet.dev/docs/controls/dismissible/#dismiss_direction)
    * [`dismiss_thresholds`](https://flet.dev/docs/controls/dismissible/#dismiss_thresholds)
    * [`movement_duration`](https://flet.dev/docs/controls/dismissible/#movement_duration)
    * [`resize_duration`](https://flet.dev/docs/controls/dismissible/#resize_duration)
    * [`secondary_background`](https://flet.dev/docs/controls/dismissible/#secondary_background)
  * [Events](https://flet.dev/docs/controls/dismissible/#events)
    * [`on_confirm_dismiss`](https://flet.dev/docs/controls/dismissible/#on_confirm_dismiss)
    * [`on_dismiss`](https://flet.dev/docs/controls/dismissible/#on_dismiss)
    * [`on_resize`](https://flet.dev/docs/controls/dismissible/#on_resize)
    * [`on_update`](https://flet.dev/docs/controls/dismissible/#on_update)
  * [Methods](https://flet.dev/docs/controls/dismissible/#methods)
    * [`confirm_dismiss(dismiss: bool)`](https://flet.dev/docs/controls/dismissible/#confirm_dismissdismiss-bool)


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
