[Skip to main content](https://flet.dev/docs/controls/view/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/view/)
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
  * [Cookbook](https://flet.dev/docs/controls/view/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Layout](https://flet.dev/docs/controls/layout)
  * View


On this page
# View
View is the top most container for all other controls.
A root view is automatically created when a new user session started. From layout perspective the View represents a [`Column`](https://flet.dev/docs/controls/column) control, so it has a similar behavior and shares same properties.
## Properties[​](https://flet.dev/docs/controls/view/#properties "Direct link to Properties")
### `appbar`[​](https://flet.dev/docs/controls/view/#appbar "Direct link to appbar")
A [`AppBar`](https://flet.dev/docs/controls/appbar) control to display at the top of the Page.
### `auto_scroll`[​](https://flet.dev/docs/controls/view/#auto_scroll "Direct link to auto_scroll")
`True` if scrollbar should automatically move its position to the end when children updated. Must be `False` for `scroll_to()` to work.
### `bgcolor`[​](https://flet.dev/docs/controls/view/#bgcolor "Direct link to bgcolor")
Background [color](https://flet.dev/docs/reference/colors) of the view.
### `can_pop`[​](https://flet.dev/docs/controls/view/#can_pop "Direct link to can_pop")
This property controls whether the view can be uncoditionally removed from navigation either programmatically, say by modifying `page.views` list, or when a user uses device back button.
By default, `can_pop` is `True` which means the view will be removed with no questions asked. However, if you set `View.can_pop` to `False` then you can add `View.on_confirm_pop` event handler where you can open an alert dialog to confirm or do other checks and then call `View.confirm_pop(True|False)` method to either allow or prevent view from removal.
Another use case is setting `page.views[0].canPop = False` for root view to prevent closing the app with hardware back button on Android.
### `controls`[​](https://flet.dev/docs/controls/view/#controls "Direct link to controls")
A list of `Control`s to display on the Page.
For example, to add a new control to a page:
  * Python


```
page.controls.append(ft.Text("Hello!"))page.update()
```

or to get the same result as above using `page.add()` shortcut method:
  * Python


```
page.add(ft.Text("Hello!"))
```

To remove the top most control on the page:
  * Python


```
page.controls.pop()page.update()
```

Value is of a list of `Control`s.
### `decoration`[​](https://flet.dev/docs/controls/view/#decoration "Direct link to decoration")
The background decoration.
Value is of type [`BoxDecoration`](https://flet.dev/docs/reference/types/boxdecoration).
### `drawer`[​](https://flet.dev/docs/controls/view/#drawer "Direct link to drawer")
A [`NavigationDrawer`](https://flet.dev/docs/controls/navigationdrawer) control to display as a panel sliding from the start edge of the view.
### `end_drawer`[​](https://flet.dev/docs/controls/view/#end_drawer "Direct link to end_drawer")
A [`NavigationDrawer`](https://flet.dev/docs/controls/navigationdrawer) control to display as a panel sliding from the end edge of the view.
### `floating_action_button`[​](https://flet.dev/docs/controls/view/#floating_action_button "Direct link to floating_action_button")
A [`FloatingActionButton`](https://flet.dev/docs/controls/floatingactionbutton) control to display on top of Page content.
### `floating_action_button_location`[​](https://flet.dev/docs/controls/view/#floating_action_button_location "Direct link to floating_action_button_location")
Describes position of [`floating_action_button`](https://flet.dev/docs/controls/view/#floating_action_button)
Value is of type [`FloatingActionButtonLocation`](https://flet.dev/docs/controls/floatingactionbutton)
### `foreground_decoration`[​](https://flet.dev/docs/controls/view/#foreground_decoration "Direct link to foreground_decoration")
The foreground decoration.
Value is of type [`BoxDecoration`](https://flet.dev/docs/reference/types/boxdecoration).
### `fullscreen_dialog`[​](https://flet.dev/docs/controls/view/#fullscreen_dialog "Direct link to fullscreen_dialog")
Whether this view is a full-screen dialog.
In Material and Cupertino, being fullscreen has the effects of making the app bars have a close button instead of a back button. On iOS, dialogs transitions animate differently and are also not closeable with the back swipe gesture.
Value is of type `bool` and defaults to `False`.
### `horizontal_alignment`[​](https://flet.dev/docs/controls/view/#horizontal_alignment "Direct link to horizontal_alignment")
How the child Controls should be placed horizontally.
Value is of type [`CrossAxisAlignment`](https://flet.dev/docs/reference/types/crossaxisalignment) and defaults to `CrossAxisAlignment.START`.
### `on_scroll_interval`[​](https://flet.dev/docs/controls/view/#on_scroll_interval "Direct link to on_scroll_interval")
Throttling in milliseconds for `on_scroll` event.
Value is of type `int` and defaults to `10`.
### `padding`[​](https://flet.dev/docs/controls/view/#padding "Direct link to padding")
A space between page contents and its edges.
Value is of type [`PaddingValue`](https://flet.dev/docs/reference/types/aliases#paddingvalue) and defaults to `padding.all(10)`.
### `route`[​](https://flet.dev/docs/controls/view/#route "Direct link to route")
View's route - not currently used by Flet framework, but can be used in a user program to update [`page.route`](https://flet.dev/docs/controls/page#route) when a view popped.
Value is of type `str`
### `scroll`[​](https://flet.dev/docs/controls/view/#scroll "Direct link to scroll")
Enables a vertical scrolling for the Page to prevent its content overflow.
Value is of type [`ScrollMode`](https://flet.dev/docs/reference/types/scrollmode).
### `spacing`[​](https://flet.dev/docs/controls/view/#spacing "Direct link to spacing")
Vertical spacing between controls on the Page. Default value is 10 virtual pixels. Spacing is applied only when `vertical_alignment` is set to `MainAxisAlignment.START`, `MainAxisAlignment.END` or `MainAxisAlignment.CENTER`.
Value is of type [`OptionalNumber`] and defaults to `10`
### `vertical_alignment`[​](https://flet.dev/docs/controls/view/#vertical_alignment "Direct link to vertical_alignment")
How the child Controls should be placed vertically.
Value is of type [`MainAxisAlignment`](https://flet.dev/docs/reference/types/mainaxisalignment) and defaults to `MainAxisAlignment.START`.
## Methods[​](https://flet.dev/docs/controls/view/#methods "Direct link to Methods")
### `confirm_pop(allow: bool)`[​](https://flet.dev/docs/controls/view/#confirm_popallow-bool "Direct link to confirm_popallow-bool")
Either allow or cancel view removal from the navigation. Used together with `View.can_pop` property and `View.on_confirm_pop` event.
### `scroll_to(offset, delta, key, duration, curve)`[​](https://flet.dev/docs/controls/view/#scroll_tooffset-delta-key-duration-curve "Direct link to scroll_tooffset-delta-key-duration-curve")
Moves scroll position to either absolute `offset`, relative `delta` or jump to the control with specified `key`.
See [`Column.scroll_to()`](https://flet.dev/docs/controls/column#scroll_tooffset-delta-key-duration-curve) for method details and examples.
## Events[​](https://flet.dev/docs/controls/view/#events "Direct link to Events")
### `on_confirm_pop`[​](https://flet.dev/docs/controls/view/#on_confirm_pop "Direct link to on_confirm_pop")
Fires when a view is about to be removed from the navigation. Allows to ask user for confirmation or do other checks and either allow or cancel removal of a view by calling `View.confirm_pop(True | False)` method. This event is fired if `View.can_pop` set to `False`.
### `on_scroll`[​](https://flet.dev/docs/controls/view/#on_scroll "Direct link to on_scroll")
Fires when scroll position is changed by a user.
Event handler argument is of type [`OnScrollEvent`](https://flet.dev/docs/reference/types/onscrollevent).
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/view.md)
[PreviousVerticalDivider](https://flet.dev/docs/controls/verticaldivider)[NextNavigation](https://flet.dev/docs/controls/app-structure-navigation)
  * [Properties](https://flet.dev/docs/controls/view/#properties)
    * [`appbar`](https://flet.dev/docs/controls/view/#appbar)
    * [`auto_scroll`](https://flet.dev/docs/controls/view/#auto_scroll)
    * [`bgcolor`](https://flet.dev/docs/controls/view/#bgcolor)
    * [`can_pop`](https://flet.dev/docs/controls/view/#can_pop)
    * [`controls`](https://flet.dev/docs/controls/view/#controls)
    * [`decoration`](https://flet.dev/docs/controls/view/#decoration)
    * [`drawer`](https://flet.dev/docs/controls/view/#drawer)
    * [`end_drawer`](https://flet.dev/docs/controls/view/#end_drawer)
    * [`floating_action_button`](https://flet.dev/docs/controls/view/#floating_action_button)
    * [`floating_action_button_location`](https://flet.dev/docs/controls/view/#floating_action_button_location)
    * [`foreground_decoration`](https://flet.dev/docs/controls/view/#foreground_decoration)
    * [`fullscreen_dialog`](https://flet.dev/docs/controls/view/#fullscreen_dialog)
    * [`horizontal_alignment`](https://flet.dev/docs/controls/view/#horizontal_alignment)
    * [`on_scroll_interval`](https://flet.dev/docs/controls/view/#on_scroll_interval)
    * [`padding`](https://flet.dev/docs/controls/view/#padding)
    * [`route`](https://flet.dev/docs/controls/view/#route)
    * [`scroll`](https://flet.dev/docs/controls/view/#scroll)
    * [`spacing`](https://flet.dev/docs/controls/view/#spacing)
    * [`vertical_alignment`](https://flet.dev/docs/controls/view/#vertical_alignment)
  * [Methods](https://flet.dev/docs/controls/view/#methods)
    * [`confirm_pop(allow: bool)`](https://flet.dev/docs/controls/view/#confirm_popallow-bool)
    * [`scroll_to(offset, delta, key, duration, curve)`](https://flet.dev/docs/controls/view/#scroll_tooffset-delta-key-duration-curve)
  * [Events](https://flet.dev/docs/controls/view/#events)
    * [`on_confirm_pop`](https://flet.dev/docs/controls/view/#on_confirm_pop)
    * [`on_scroll`](https://flet.dev/docs/controls/view/#on_scroll)


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
