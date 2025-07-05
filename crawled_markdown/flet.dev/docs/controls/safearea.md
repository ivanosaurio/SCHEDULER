[Skip to main content](https://flet.dev/docs/controls/safearea/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/safearea/)
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
  * [Cookbook](https://flet.dev/docs/controls/safearea/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Layout](https://flet.dev/docs/controls/layout)
  * SafeArea


On this page
# SafeArea
A control that insets its `content` by sufficient padding to avoid intrusions by the operating system.
For example, this will indent the `content` by enough to avoid the status bar at the top of the screen.
It will also indent the `content` by the amount necessary to avoid The Notch on the iPhone X, or other similar creative physical features of the display.
When a `minimum_padding` is specified, the greater of the minimum padding or the safe area padding will be applied.
## Example[​](https://flet.dev/docs/controls/safearea/#example "Direct link to Example")
[Live example](https://flet-controls-gallery.fly.dev/layout/safearea)
python/controls/layout/safe-area/safe-area-example.py
```
import flet as ftclassState:  counter =0defmain(page: ft.Page):  state = State()defadd_click(e):    state.counter +=1    counter.value =str(state.counter)    counter.update()  page.floating_action_button = ft.FloatingActionButton(    icon=ft.Icons.ADD, on_click=add_click)  page.add(    ft.SafeArea(      ft.Container(        counter := ft.Text("0", size=50),        alignment=ft.alignment.center,),      expand=True,))ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/safe-area/safe-area-example.py)
## Properties[​](https://flet.dev/docs/controls/safearea/#properties "Direct link to Properties")
### `bottom`[​](https://flet.dev/docs/controls/safearea/#bottom "Direct link to bottom")
Whether to avoid system intrusions on the bottom side of the screen.
Defaults to `True`.
### `content`[​](https://flet.dev/docs/controls/safearea/#content "Direct link to content")
A `Control` to display inside safe area.
### `left`[​](https://flet.dev/docs/controls/safearea/#left "Direct link to left")
Whether to avoid system intrusions on the left.
Defaults to `True`.
### `maintain_bottom_view_padding`[​](https://flet.dev/docs/controls/safearea/#maintain_bottom_view_padding "Direct link to maintain_bottom_view_padding")
Specifies whether the `SafeArea` should maintain the bottom `MediaQueryData.viewPadding` instead of the bottom `MediaQueryData.padding`, defaults to `False`.
For example, if there is an onscreen keyboard displayed above the SafeArea, the padding can be maintained below the obstruction rather than being consumed. This can be helpful in cases where your layout contains flexible controls, which could visibly move when opening a software keyboard due to the change in the padding value. Setting this to true will avoid the UI shift.
### `minimum_padding`[​](https://flet.dev/docs/controls/safearea/#minimum_padding "Direct link to minimum_padding")
This minimum padding to apply.
The greater of the minimum insets and the media padding will be applied.
### `right`[​](https://flet.dev/docs/controls/safearea/#right "Direct link to right")
Whether to avoid system intrusions on the right.
Defaults to `True`.
### `top`[​](https://flet.dev/docs/controls/safearea/#top "Direct link to top")
Whether to avoid system intrusions at the top of the screen, typically the system status bar.
Defaults to `True`.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/safearea.md)
[PreviousRow](https://flet.dev/docs/controls/row)[NextStack](https://flet.dev/docs/controls/stack)
  * [Example](https://flet.dev/docs/controls/safearea/#example)
  * [Properties](https://flet.dev/docs/controls/safearea/#properties)
    * [`bottom`](https://flet.dev/docs/controls/safearea/#bottom)
    * [`content`](https://flet.dev/docs/controls/safearea/#content)
    * [`left`](https://flet.dev/docs/controls/safearea/#left)
    * [`maintain_bottom_view_padding`](https://flet.dev/docs/controls/safearea/#maintain_bottom_view_padding)
    * [`minimum_padding`](https://flet.dev/docs/controls/safearea/#minimum_padding)
    * [`right`](https://flet.dev/docs/controls/safearea/#right)
    * [`top`](https://flet.dev/docs/controls/safearea/#top)


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
