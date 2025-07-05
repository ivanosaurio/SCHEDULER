[Skip to main content](https://flet.dev/docs/controls/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search
[![Flet Logo](https://flet.dev/img/logo.svg)![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/extend/built-in-extensions)
  * [Controls](https://flet.dev/docs/controls)
    * [Layout](https://flet.dev/docs/controls/layout)
    * [Navigation](https://flet.dev/docs/controls/app-structure-navigation)
    * [Information Displays](https://flet.dev/docs/controls/information-displays)
    * [Buttons](https://flet.dev/docs/controls/buttons)
    * [Input and Selections](https://flet.dev/docs/controls/input-and-selections)
    * [Dialogs, Alerts and Panels](https://flet.dev/docs/controls/dialogs-alerts-panels)
    * [Charts](https://flet.dev/docs/controls/charts)
    * [Animations](https://flet.dev/docs/controls/animations)
    * [Utility](https://flet.dev/docs/controls/utility)
  * [Cookbook](https://flet.dev/docs/cookbook/theming)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * Controls


On this page
# Controls reference
Flet UI is built of controls. Controls are organized into hierarchy, or a tree, where each control has a parent (except [Page](https://flet.dev/docs/controls/page)) and container controls like [Column](https://flet.dev/docs/controls/column), [Dropdown](https://flet.dev/docs/controls/dropdown) can contain child controls, for example:
```
Page ├─ TextField ├─ Dropdown │  ├─ Option │  └─ Option └─ Row   ├─ ElevatedButton   └─ ElevatedButton
```

[Control gallery live demo](https://flet-controls-gallery.fly.dev/layout)
## Controls by categories[​](https://flet.dev/docs/controls/#controls-by-categories "Direct link to Controls by categories")
## [🗃️ Layout23 items](https://flet.dev/docs/controls/layout)## [🗃️ Navigation8 items](https://flet.dev/docs/controls/app-structure-navigation)## [🗃️ Information Displays12 items](https://flet.dev/docs/controls/information-displays)## [🗃️ Buttons18 items](https://flet.dev/docs/controls/buttons)## [🗃️ Input and Selections17 items](https://flet.dev/docs/controls/input-and-selections)## [🗃️ Dialogs, Alerts and Panels13 items](https://flet.dev/docs/controls/dialogs-alerts-panels)## [🗃️ Charts5 items](https://flet.dev/docs/controls/charts)## [🗃️ Animations3 items](https://flet.dev/docs/controls/animations)## [🗃️ Utility21 items](https://flet.dev/docs/controls/utility)
## Common control properties[​](https://flet.dev/docs/controls/#common-control-properties "Direct link to Common control properties")
Flet controls have the following properties:
### `adaptive`[​](https://flet.dev/docs/controls/#adaptive "Direct link to adaptive")
`adaptive` property can be specified for a control in the following cases:
  * A control has matching Cupertino control with similar functionality/presentation and graphics as expected on iOS/macOS. In this case, if `adaptive` is `True`, either Material or Cupertino control will be created depending on the target platform.
These controls have their Cupertino analogs and `adaptive` property:
    * [`AlertDialog`](https://flet.dev/docs/controls/alertdialog)
    * [`AppBar`](https://flet.dev/docs/controls/appbar)
    * [`Checkbox`](https://flet.dev/docs/controls/checkbox)
    * [`ListTile`](https://flet.dev/docs/controls/listtile)
    * [`NavigationBar`](https://flet.dev/docs/controls/navigationbar)
    * [`Radio`](https://flet.dev/docs/controls/radio)
    * [`Slider`](https://flet.dev/docs/controls/slider)
    * [`Switch`](https://flet.dev/docs/controls/switch)
  * A control has child controls. In this case `adaptive` property value is passed on to its children that don't have their `adaptive` property set.
The following container controls have `adaptive` property:
    * [`Card`](https://flet.dev/docs/controls/card)
    * [`Column`](https://flet.dev/docs/controls/column)
    * [`Container`](https://flet.dev/docs/controls/container)
    * [`Dismissible`](https://flet.dev/docs/controls/dismissible)
    * [`ExpansionPanel`](https://flet.dev/docs/controls/expansionpanel)
    * [`FletApp`](https://flet.dev/docs/controls/fletapp)
    * [`GestureDetector`](https://flet.dev/docs/controls/gesturedetector)
    * [`GridView`](https://flet.dev/docs/controls/gridview)
    * [`ListView`](https://flet.dev/docs/controls/listview)
    * [`Page`](https://flet.dev/docs/controls/page)
    * [`Row`](https://flet.dev/docs/controls/row)
    * [`SafeArea`](https://flet.dev/docs/controls/safearea)
    * [`Stack`](https://flet.dev/docs/controls/stack)
    * [`Tabs`](https://flet.dev/docs/controls/tabs)
    * [`View`](https://flet.dev/docs/controls/view)


### `badge`[​](https://flet.dev/docs/controls/#badge "Direct link to badge")
The `badge` property (available in almost all controls) supports both strings and [`Badge`](https://flet.dev/docs/reference/types/badge) objects.
### `bottom`[​](https://flet.dev/docs/controls/#bottom "Direct link to bottom")
Effective inside [`Stack`](https://flet.dev/docs/controls/stack) only. The distance that the child's bottom edge is inset from the bottom of the stack.
### `data`[​](https://flet.dev/docs/controls/#data "Direct link to data")
Arbitrary data that can be attached to a control.
### `disabled`[​](https://flet.dev/docs/controls/#disabled "Direct link to disabled")
Every control has `disabled` property which is `False` by default - control and all its children are enabled. `disabled` property is mostly used with data entry controls like `TextField`, `Dropdown`, `Checkbox`, buttons. However, `disabled` could be set to a parent control and its value will be propagated down to all children recursively.
For example, if you have a form with multiple entry controls you can disable them all together by disabling container:
```
c = ft.Column(controls=[  ft.TextField(),  ft.TextField()])c.disabled =Truepage.add(c)
```

### `expand`[​](https://flet.dev/docs/controls/#expand "Direct link to expand")
When a child Control is placed into a [`Column`](https://flet.dev/docs/controls/column) or a [`Row`](https://flet.dev/docs/controls/row) you can "expand" it to fill the available space. `expand` property could be a boolean value (`True` - expand control to fill all available space) or an integer - an "expand factor" specifying how to divide a free space with other expanded child controls.
For more information and examples about `expand` property see "Expanding children" sections in [`Column`](https://flet.dev/docs/controls/column#expanding-children) or [`Row`](https://flet.dev/docs/controls/row#expanding-children).
Here is an example of expand being used in action for both [`Column`](https://flet.dev/docs/controls/column) and [`Row`](https://flet.dev/docs/controls/row):
```
import flet as ftdef main(page: ft.Page):  page.spacing = 0  page.padding = 0  page.add(    ft.Column(      controls=[        ft.Row(          [            ft.Card(              content=ft.Text("Card_1"),              color=ft.Colors.ORANGE_300,              expand=True,              height=page.height,              margin=0,            ),            ft.Card(              content=ft.Text("Card_2"),              color=ft.Colors.GREEN_100,              expand=True,              height=page.height,              margin=0,            ),          ],          expand=True,          spacing=0,        ),      ],      expand=True,      spacing=0,    ),  )ft.app(main)
```

### `expand_loose`[​](https://flet.dev/docs/controls/#expand_loose "Direct link to expand_loose")
Effective only if `expand` is `True`.
If `expand_loose` is `True`, the child control of a [`Column`](https://flet.dev/docs/controls/column) or a [`Row`](https://flet.dev/docs/controls/row) will be given the flexibility to expand to fill the available space in the main axis (e.g., horizontally for a Row or vertically for a Column), but will not be required to fill the available space.
The default value is `False`.
Here is the example of Containers placed in Rows with `expand_loose = True`:
```
import flet as ftclassMessage(ft.Container):def__init__(self, author, body):super().__init__()    self.content = ft.Column(      controls=[        ft.Text(author, weight=ft.FontWeight.BOLD),        ft.Text(body),],)    self.border = ft.border.all(1, ft.Colors.BLACK)    self.border_radius = ft.border_radius.all(10)    self.bgcolor = ft.Colors.GREEN_200    self.padding =10    self.expand =True    self.expand_loose =Truedefmain(page: ft.Page):  chat = ft.ListView(    padding=10,    spacing=10,    controls=[      ft.Row(        alignment=ft.MainAxisAlignment.START,        controls=[          Message(            author="John",            body="Hi, how are you?",),],),      ft.Row(        alignment=ft.MainAxisAlignment.END,        controls=[          Message(            author="Jake",            body="Hi I am good thanks, how about you?",),],),      ft.Row(        alignment=ft.MainAxisAlignment.START,        controls=[          Message(            author="John",            body="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.",),],),      ft.Row(        alignment=ft.MainAxisAlignment.END,        controls=[          Message(            author="Jake",            body="Thank you!",),],),],)  page.window.width =393  page.window.height =600  page.window.always_on_top =False  page.add(chat)ft.app(main)
```

![](https://flet.dev/img/docs/controls/overview/expand = True, expand_loose = True.png)
### `height`[​](https://flet.dev/docs/controls/#height "Direct link to height")
Imposed Control height in virtual pixels.
### `left`[​](https://flet.dev/docs/controls/#left "Direct link to left")
Effective inside [`Stack`](https://flet.dev/docs/controls/stack) only. The distance that the child's left edge is inset from the left of the stack.
### `parent`[​](https://flet.dev/docs/controls/#parent "Direct link to parent")
Points to the direct ancestor(parent) of this control.
It defaults to `None` and will only have a value when this control is mounted (added to the page tree).
The `Page` control (which is the root of the tree) is an exception - it always has `parent=None`.
### `right`[​](https://flet.dev/docs/controls/#right "Direct link to right")
Effective inside [`Stack`](https://flet.dev/docs/controls/stack) only. The distance that the child's right edge is inset from the right of the stack.
### `tooltip`[​](https://flet.dev/docs/controls/#tooltip "Direct link to tooltip")
The `tooltip` property (available in almost all controls) now supports both strings and [`Tooltip`](https://flet.dev/docs/reference/types/tooltip) objects.
### `top`[​](https://flet.dev/docs/controls/#top "Direct link to top")
Effective inside [`Stack`](https://flet.dev/docs/controls/stack) only. The distance that the child's top edge is inset from the top of the stack.
### `visible`[​](https://flet.dev/docs/controls/#visible "Direct link to visible")
Every control has `visible` property which is `True` by default - control is rendered on the page. Setting `visible` to `False` completely prevents control (and all its children if any) from rendering on a page canvas. Hidden controls cannot be focused or selected with a keyboard or mouse and they do not emit any events.
### `width`[​](https://flet.dev/docs/controls/#width "Direct link to width")
Imposed Control width in virtual pixels.
## Transformations[​](https://flet.dev/docs/controls/#transformations "Direct link to Transformations")
### `offset`[​](https://flet.dev/docs/controls/#offset "Direct link to offset")
Applies a translation transformation before painting the control.
The translation is expressed as a `transform.Offset` scaled to the control's size. For example, an `Offset` with a `x` of `0.25` will result in a horizontal translation of one quarter the width of the control.
The following example displays container at `0, 0` top left corner of a stack as transform applies `-1 * 100, -1 * 100` (`offset * control_size`) horizontal and vertical translations to the control:
```
import flet as ftdefmain(page: ft.Page):  page.add(    ft.Stack([        ft.Container(          bgcolor="red",          width=100,          height=100,          left=100,          top=100,          offset=ft.transform.Offset(-1,-1),)],      width=1000,      height=1000,))ft.app(main)
```

### `opacity`[​](https://flet.dev/docs/controls/#opacity "Direct link to opacity")
Defines the transparency of the control.
Value ranges from `0.0` (completely transparent) to `1.0` (completely opaque without any transparency) and defaults to `1.0`.
### `rotate`[​](https://flet.dev/docs/controls/#rotate "Direct link to rotate")
Transforms control using a rotation around the center.
The value of `rotate` property could be one of the following types:
  * `number` - a rotation in clockwise radians. Full circle `360°` is `math.pi * 2` radians, `90°` is `pi / 2`, `45°` is `pi / 4`, etc.
  * `transform.Rotate` - allows to specify rotation `angle` as well as `alignment` - the location of rotation center.


For example:
```
ft.Image(  src="https://picsum.photos/100/100",  width=100,  height=100,  border_radius=5,  rotate=Rotate(angle=0.25* pi, alignment=ft.alignment.center_left))
```

### `scale`[​](https://flet.dev/docs/controls/#scale "Direct link to scale")
Scale control along the 2D plane. Default scale factor is `1.0` - control is not scaled. `0.5` - the control is twice smaller, `2.0` - the control is twice larger.
Different scale multipliers can be specified for `x` and `y` axis, but setting `Control.scale` property to an instance of `transform.Scale` class:
```
from dataclasses import fieldclassScale:  scale:float= field(default=None)  scale_x:float= field(default=None)  scale_y:float= field(default=None)  alignment: Alignment = field(default=None)
```

Either `scale` or `scale_x` and `scale_y` could be specified, but not all of them, for example:
```
ft.Image(  src="https://picsum.photos/100/100",  width=100,  height=100,  border_radius=5,  scale=Scale(scale_x=2, scale_y=0.5))
```

[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/overview.md)
[PreviousUser extensions](https://flet.dev/docs/extend/user-extensions)[NextLayout](https://flet.dev/docs/controls/layout)
  * [Controls by categories](https://flet.dev/docs/controls/#controls-by-categories)
  * [Common control properties](https://flet.dev/docs/controls/#common-control-properties)
    * [`adaptive`](https://flet.dev/docs/controls/#adaptive)
    * [`badge`](https://flet.dev/docs/controls/#badge)
    * [`bottom`](https://flet.dev/docs/controls/#bottom)
    * [`data`](https://flet.dev/docs/controls/#data)
    * [`disabled`](https://flet.dev/docs/controls/#disabled)
    * [`expand`](https://flet.dev/docs/controls/#expand)
    * [`expand_loose`](https://flet.dev/docs/controls/#expand_loose)
    * [`height`](https://flet.dev/docs/controls/#height)
    * [`left`](https://flet.dev/docs/controls/#left)
    * [`parent`](https://flet.dev/docs/controls/#parent)
    * [`right`](https://flet.dev/docs/controls/#right)
    * [`tooltip`](https://flet.dev/docs/controls/#tooltip)
    * [`top`](https://flet.dev/docs/controls/#top)
    * [`visible`](https://flet.dev/docs/controls/#visible)
    * [`width`](https://flet.dev/docs/controls/#width)
  * [Transformations](https://flet.dev/docs/controls/#transformations)
    * [`offset`](https://flet.dev/docs/controls/#offset)
    * [`opacity`](https://flet.dev/docs/controls/#opacity)
    * [`rotate`](https://flet.dev/docs/controls/#rotate)
    * [`scale`](https://flet.dev/docs/controls/#scale)


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
