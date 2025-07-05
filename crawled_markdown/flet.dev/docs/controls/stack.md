[Skip to main content](https://flet.dev/docs/controls/stack/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/stack/)
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
  * [Cookbook](https://flet.dev/docs/controls/stack/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Layout](https://flet.dev/docs/controls/layout)
  * Stack


On this page
# Stack
A control that positions its children on top of each other.
This control is useful if you want to overlap several children in a simple way, for example having some text and an image, overlaid with a gradient and a button attached to the bottom.
Stack is also useful if you want to implement [implicit animations](https://flet.dev/docs/cookbook/animations) that require knowing absolute position of a target value.
## Examples[​](https://flet.dev/docs/controls/stack/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/layout/stack)
### Transparent title over an image[​](https://flet.dev/docs/controls/stack/#transparent-title-over-an-image "Direct link to Transparent title over an image")
![](https://flet.dev/img/docs/controls/stack/image-title.png)
python/controls/layout/stack/image-title.py
```
import flet as ftdefmain(page: ft.Page):  st = ft.Stack([      ft.Image(        src=f"https://picsum.photos/300/300",        width=300,        height=300,        fit=ft.ImageFit.CONTAIN,),      ft.Row([          ft.Text("Image title",            color=ft.Colors.ON_SURFACE,            size=40,            weight=ft.FontWeight.BOLD,            opacity=0.5,)],        alignment=ft.MainAxisAlignment.CENTER,),],    width=300,    height=300,)  page.add(st)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/stack/image-title.py)
### Avatar with online status[​](https://flet.dev/docs/controls/stack/#avatar-with-online-status "Direct link to Avatar with online status")
![](https://flet.dev/img/docs/controls/stack/avatar-with-status.png)
python/controls/layout/stack/avatar-with-status.py
```
import flet as ftdefmain(page):  page.add(    ft.Stack([        ft.CircleAvatar(          foreground_image_src="https://avatars.githubusercontent.com/u/5041459?s=88&v=4"),        ft.Container(          content=ft.CircleAvatar(bgcolor=ft.Colors.GREEN, radius=5),          alignment=ft.alignment.bottom_left,),],      width=40,      height=40,))ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/stack/avatar-with-status.py)
### Absolute positioning inside Stack[​](https://flet.dev/docs/controls/stack/#absolute-positioning-inside-stack "Direct link to Absolute positioning inside Stack")
![](https://flet.dev/img/docs/controls/stack/stack-absolute-position.png)
python/controls/layout/stack/absolute-positioned.py
```
import flet as ftdefmain(page: ft.Page):  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  page.vertical_alignment = ft.MainAxisAlignment.CENTER  page.add(    ft.Container(      ft.Stack([          ft.Container(            width=20, height=20, bgcolor=ft.Colors.RED, border_radius=5),          ft.Container(            width=20,            height=20,            bgcolor=ft.Colors.YELLOW,            border_radius=5,            right=0,),          ft.Container(            width=20,            height=20,            bgcolor=ft.Colors.BLUE,            border_radius=5,            right=0,            bottom=0,),          ft.Container(            width=20,            height=20,            bgcolor=ft.Colors.GREEN,            border_radius=5,            left=0,            bottom=0,),          ft.Column([              ft.Container(                width=20,                height=20,                bgcolor=ft.Colors.PURPLE,                border_radius=5,)],            left=85,            top=85,),]),      border_radius=8,      padding=5,      width=200,      height=200,      bgcolor=ft.Colors.BLACK,))ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/stack/absolute-positioned.py)
## Properties[​](https://flet.dev/docs/controls/stack/#properties "Direct link to Properties")
### `alignment`[​](https://flet.dev/docs/controls/stack/#alignment "Direct link to alignment")
The alignment of the non-positioned (those that do not specify an alignment - ex neither top nor bottom - in a particular axis and partially-positioned `controls`.
### `clip_behavior`[​](https://flet.dev/docs/controls/stack/#clip_behavior "Direct link to clip_behavior")
The content will be clipped (or not) according to this option.
Value is of type [`ClipBehavior`](https://flet.dev/docs/reference/types/clipbehavior) and defaults to `ClipBehavior.HARD_EDGE`.
### `controls`[​](https://flet.dev/docs/controls/stack/#controls "Direct link to controls")
A list of Controls to display inside the Stack. The last control in the list is displayed on top.
### `fit`[​](https://flet.dev/docs/controls/stack/#fit "Direct link to fit")
How to size the non-positioned `controls`.
Value is of type [`StackFit`](https://flet.dev/docs/reference/types/stackfit) and defaults to `StackFit.LOOSE`.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/stack.md)
[PreviousSafeArea](https://flet.dev/docs/controls/safearea)[NextTabs](https://flet.dev/docs/controls/tabs)
  * [Examples](https://flet.dev/docs/controls/stack/#examples)
    * [Transparent title over an image](https://flet.dev/docs/controls/stack/#transparent-title-over-an-image)
    * [Avatar with online status](https://flet.dev/docs/controls/stack/#avatar-with-online-status)
    * [Absolute positioning inside Stack](https://flet.dev/docs/controls/stack/#absolute-positioning-inside-stack)
  * [Properties](https://flet.dev/docs/controls/stack/#properties)
    * [`alignment`](https://flet.dev/docs/controls/stack/#alignment)
    * [`clip_behavior`](https://flet.dev/docs/controls/stack/#clip_behavior)
    * [`controls`](https://flet.dev/docs/controls/stack/#controls)
    * [`fit`](https://flet.dev/docs/controls/stack/#fit)


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
