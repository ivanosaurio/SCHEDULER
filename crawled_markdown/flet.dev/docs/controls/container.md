[Skip to main content](https://flet.dev/docs/controls/container/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/container/)
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
  * [Cookbook](https://flet.dev/docs/controls/container/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Layout](https://flet.dev/docs/controls/layout)
  * Container


On this page
# Container
Container allows to decorate a control with background color and border and position it with padding, margin and alignment.
## Examples[​](https://flet.dev/docs/controls/container/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/layout/container)
### Clickable container[​](https://flet.dev/docs/controls/container/#clickable-container "Direct link to Clickable container")
![](https://flet.dev/img/docs/controls/container/clickable-container.gif)
python/controls/layout/container/clickable-container.py
```
import flet as ftdefmain(page: ft.Page):  page.theme_mode = ft.ThemeMode.LIGHT  page.title ="Containers - clickable and not"  page.vertical_alignment = ft.MainAxisAlignment.CENTER  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  page.add(    ft.Row([        ft.Container(          content=ft.Text("Non clickable"),          margin=10,          padding=10,          alignment=ft.alignment.center,          bgcolor=ft.Colors.AMBER,          width=150,          height=150,          border_radius=10,),        ft.Container(          content=ft.Text("Clickable without Ink"),          margin=10,          padding=10,          alignment=ft.alignment.center,          bgcolor=ft.Colors.GREEN_200,          width=150,          height=150,          border_radius=10,          on_click=lambda e:print("Clickable without Ink clicked!"),),        ft.Container(          content=ft.Text("Clickable with Ink"),          margin=10,          padding=10,          alignment=ft.alignment.center,          bgcolor=ft.Colors.CYAN_200,          width=150,          height=150,          border_radius=10,          ink=True,          on_click=lambda e:print("Clickable with Ink clicked!"),),        ft.Container(          content=ft.Text("Clickable transparent with Ink"),          margin=10,          padding=10,          alignment=ft.alignment.center,          width=150,          height=150,          border_radius=10,          ink=True,          on_click=lambda e:print("Clickable transparent with Ink clicked!"),),],      alignment=ft.MainAxisAlignment.CENTER,),)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/container/clickable-container.py)
## Properties[​](https://flet.dev/docs/controls/container/#properties "Direct link to Properties")
![](https://flet.dev/img/docs/controls/container/container-diagram.png)
### `alignment`[​](https://flet.dev/docs/controls/container/#alignment "Direct link to alignment")
Align the child control within the container.
Value is of type [`Alignment`](https://flet.dev/docs/reference/types/alignment).
### `animate`[​](https://flet.dev/docs/controls/container/#animate "Direct link to animate")
Enables container "implicit" animation that gradually changes its values over a period of time.
Value is of type [`AnimationValue`](https://flet.dev/docs/reference/types/animationvalue).
### `bgcolor`[​](https://flet.dev/docs/controls/container/#bgcolor "Direct link to bgcolor")
Defines the background [color](https://flet.dev/docs/reference/colors) of the container.
### `blend_mode`[​](https://flet.dev/docs/controls/container/#blend_mode "Direct link to blend_mode")
The blend mode applied to the `color` or `gradient` background of the container.
Value is of type [`BlendMode`](https://flet.dev/docs/reference/types/blendmode) and defaults to `BlendMode.MODULATE`.
### `blur`[​](https://flet.dev/docs/controls/container/#blur "Direct link to blur")
Applies Gaussian blur effect under the container.
The value of this property could be one of the following:
  * **a number** - specifies the same value for horizontal and vertical sigmas, e.g. `10`.
  * **a tuple** - specifies separate values for horizontal and vertical sigmas, e.g. `(10, 1)`.
  * **an instance of[`Blur`](https://flet.dev/docs/reference/types/blur)**


For example:
python/controls/layout/container/container-blur.py
```
import flet as ftdefmain(page: ft.Page):  page.theme_mode = ft.ThemeMode.LIGHT  i =1  img_container = ft.Container(    image=ft.DecorationImage(src="https://picsum.photos/250/250"),    width=250,    height=250,)defchange_img(e):nonlocal iprint(f"button clicked {i}")    img_container.image = ft.DecorationImage(      src=f"https://picsum.photos/250/250?random={i}")    i +=1    page.update()  page.add(    ft.Stack([        img_container,        ft.Container(          width=100,          height=100,          blur=10,          bgcolor="#22CCCC00",),        ft.Container(          width=100,          height=100,          left=20,          top=120,          blur=(0,10),),        ft.Container(          top=50,          right=10,          blur=ft.Blur(10,0, ft.BlurTileMode.MIRROR),          width=100,          height=100,          bgcolor="#44CCCCCC",          border_radius=10,          border=ft.border.all(2, ft.Colors.BLACK),),        ft.ElevatedButton(          text="Change Background",          bottom=5,          right=5,          style=ft.ButtonStyle(text_style=ft.TextStyle(size=8)),          on_click=change_img,),]))ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/container/container-blur.py)
![](https://flet.dev/img/docs/controls/container/container-blur.gif)
### `border`[​](https://flet.dev/docs/controls/container/#border "Direct link to border")
A border to draw above the background color.
Value is of type [`Border`](https://flet.dev/docs/reference/types/border).
### `border_radius`[​](https://flet.dev/docs/controls/container/#border_radius "Direct link to border_radius")
If specified, the corners of the container are rounded by this radius.
Value is of type [`BorderRadius`](https://flet.dev/docs/reference/types/borderradius).
### `clip_behavior`[​](https://flet.dev/docs/controls/container/#clip_behavior "Direct link to clip_behavior")
The content will be clipped (or not) according to this option.
Value is of type [`ClipBehavior`](https://flet.dev/docs/reference/types/clipbehavior) and defaults to `ClipBehavior.ANTI_ALIAS` if `border_radius` is not `None`; otherwise `ClipBehavior.NONE`.
### `color_filter`[​](https://flet.dev/docs/controls/container/#color_filter "Direct link to color_filter")
Applies a color filter to the container.
Value is of type [`ColorFilter`](https://flet.dev/docs/reference/types/colorfilter).
### `content`[​](https://flet.dev/docs/controls/container/#content "Direct link to content")
A child Control contained by the container.
### `dark_theme`[​](https://flet.dev/docs/controls/container/#dark_theme "Direct link to dark_theme")
Allows setting a nested `theme` to be used when in dark theme mode for all controls inside the container and down the tree.
Value is of type [`Theme`](https://flet.dev/docs/cookbook/theming).
### `foreground_decoration`[​](https://flet.dev/docs/controls/container/#foreground_decoration "Direct link to foreground_decoration")
The foreground decoration.
Value is of type [`BoxDecoration`](https://flet.dev/docs/reference/types/boxdecoration).
### `gradient`[​](https://flet.dev/docs/controls/container/#gradient "Direct link to gradient")
Defines the gradient background of the container.
Value is of type [`Gradient`](https://flet.dev/docs/reference/types/gradient).
### `ignore_interactions`[​](https://flet.dev/docs/controls/container/#ignore_interactions "Direct link to ignore_interactions")
Whether to ignore all interactions with this container and its descendants.
Defaults to `False`.
### `image`[​](https://flet.dev/docs/controls/container/#image "Direct link to image")
An image to paint above the `bgcolor` or `gradient`. If `shape=BoxShape.CIRCLE` then this image is clipped to the circle's boundary; if `border_radius` is not `None`then the image is clipped to the given radii.
Value is of type [`DecorationImage`](https://flet.dev/docs/reference/types/decorationimage).
### `ink`[​](https://flet.dev/docs/controls/container/#ink "Direct link to ink")
`True` to produce ink ripples effect when user clicks the container.
Defaults to `False`.
### `ink_color`[​](https://flet.dev/docs/controls/container/#ink_color "Direct link to ink_color")
The splash [color](https://flet.dev/docs/reference/colors) of the ink response.
### `margin`[​](https://flet.dev/docs/controls/container/#margin "Direct link to margin")
Empty space to surround the decoration and child control.
Value is of type [`Margin`](https://flet.dev/docs/reference/types/margin) class or a number.
### `padding`[​](https://flet.dev/docs/controls/container/#padding "Direct link to padding")
Empty space to inscribe inside a container decoration (background, border). The child control is placed inside this padding.
Value is of type [`Padding`](https://flet.dev/docs/reference/types/padding) or a number.
### `rtl`[​](https://flet.dev/docs/controls/container/#rtl "Direct link to rtl")
`True` to set text direction to right-to-left.
Defaults to `False`.
### `shadow`[​](https://flet.dev/docs/controls/container/#shadow "Direct link to shadow")
Shadows cast by the container.
Value is of type [`BoxShadow`](https://flet.dev/docs/reference/types/boxshadow) or a `List[BoxShadow]`.
### `shape`[​](https://flet.dev/docs/controls/container/#shape "Direct link to shape")
Sets the shape of the container.
Value is of type [`BoxShape`](https://flet.dev/docs/reference/types/boxshape) and defaults to `BoxShape.RECTANGLE`.
### `theme_mode`[​](https://flet.dev/docs/controls/container/#theme_mode "Direct link to theme_mode")
Setting `theme_mode` "resets" parent theme and creates a new, unique scheme for all controls inside the container. Otherwise the styles defined in container's `theme` property override corresponding styles from the parent, inherited theme.
Value is of type [`ThemeMode`](https://flet.dev/docs/reference/types/thememode) and defaults to `ThemeMode.SYSTEM`.
### `theme`[​](https://flet.dev/docs/controls/container/#theme "Direct link to theme")
Allows setting a nested `theme` for all controls inside the container and down the tree.
Value is of type [`Theme`](https://flet.dev/docs/cookbook/theming).
**Usage example**
python/controls/layout/container/nested-themes-switch.py
```
import flet as ftdefmain(page: ft.Page):  page.theme_mode = ft.ThemeMode.DARKdefchange_theme_mode(e):if page.theme_mode == ft.ThemeMode.DARK:      page.theme_mode = ft.ThemeMode.LIGHT      sw.thumb_icon = ft.Icons.LIGHT_MODEelse:      sw.thumb_icon = ft.Icons.DARK_MODE      page.theme_mode = ft.ThemeMode.DARK    page.update()# Yellow page theme with SYSTEM (default) mode  page.theme = ft.Theme(    color_scheme_seed=ft.Colors.YELLOW,)  sw = ft.Switch(thumb_icon=ft.Icons.DARK_MODE, on_change=change_theme_mode)  page.add(# Page theme    ft.Row([        ft.Container(          content=ft.ElevatedButton("Page theme button"),          bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,          padding=20,          width=300,),        ft.Container(          content=sw,          padding=ft.padding.only(bottom=50),          alignment=ft.alignment.top_right,),],      alignment=ft.MainAxisAlignment.SPACE_BETWEEN,),# Inherited theme with primary color overridden    ft.Container(      theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.Colors.PINK)),      content=ft.ElevatedButton("Inherited theme button"),      bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,      padding=20,      width=300,),# Unique always DARK theme    ft.Container(      theme=ft.Theme(color_scheme_seed=ft.Colors.INDIGO),      theme_mode=ft.ThemeMode.DARK,      content=ft.ElevatedButton("Unique theme button"),      bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,      padding=20,      width=300,),)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/container/nested-themes-switch.py)
![](https://flet.dev/img/docs/controls/container/container-theme.gif)
### `url`[​](https://flet.dev/docs/controls/container/#url "Direct link to url")
The URL to open when the container is clicked. If provided, `on_click` event is fired after that.
### `url_target`[​](https://flet.dev/docs/controls/container/#url_target "Direct link to url_target")
Where to open URL in the web mode.
Value is of type [`UrlTarget`](https://flet.dev/docs/reference/types/urltarget) and defaults to `UrlTarget.BLANK`.
## Events[​](https://flet.dev/docs/controls/container/#events "Direct link to Events")
### `on_click`[​](https://flet.dev/docs/controls/container/#on_click "Direct link to on_click")
Fires when a user clicks the container. Will not be fired on long press.
### `on_hover`[​](https://flet.dev/docs/controls/container/#on_hover "Direct link to on_hover")
Fires when a mouse pointer enters or exists the container area. `data` property of event object contains `true` (string) when cursor enters and `false` when it exits.
A simple example of a container changing its background color on mouse hover:
python/controls/layout/container/simple-hover.py
```
import flet as ftdefmain(page: ft.Page):defon_hover(e):    e.control.bgcolor ="blue"if e.data =="true"else"red"    e.control.update()  page.add(    ft.Container(width=100, height=100, bgcolor="red", ink=False, on_hover=on_hover))ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/container/simple-hover.py)
![](https://flet.dev/img/docs/controls/container/hover-container.gif)
### `on_long_press`[​](https://flet.dev/docs/controls/container/#on_long_press "Direct link to on_long_press")
Fires when the container is long-pressed.
### `on_tap_down`[​](https://flet.dev/docs/controls/container/#on_tap_down "Direct link to on_tap_down")
Fires when a user clicks the container with or without a long press.
Event handler argument is of type [`ContainerTapEvent`](https://flet.dev/docs/reference/types/containertapevent).
info
If `ink` is `True`, `e` will be plain `ControlEvent` with empty `data` instead of `ContainerTapEvent`.
A simple usage example:
python/controls/layout/container/container-click-events.py
```
import flet as ftdefmain(page: ft.Page):  page.theme_mode = ft.ThemeMode.LIGHT  page.vertical_alignment = ft.MainAxisAlignment.CENTER  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  lp_counter =0  cl_counter =0  td_counter =0defon_click(e):nonlocal cl_counter    cl_counter +=1    t1.spans[-1]= ft.TextSpan(f" {cl_counter} ",      style=ft.TextStyle(size=16, bgcolor=ft.Colors.TEAL_300),)    page.update()defon_long_press(e):nonlocal lp_counter    lp_counter +=1    t3.spans[-1]= ft.TextSpan(f" {lp_counter} ",      style=ft.TextStyle(size=16, bgcolor=ft.Colors.TEAL_300),)    page.update()defon_tap_down(e: ft.ContainerTapEvent):nonlocal td_counter    td_counter +=1    t2.spans[-1]= ft.TextSpan(f" {td_counter} ",      style=ft.TextStyle(size=16, bgcolor=ft.Colors.TEAL_300),)    page.update()  c = ft.Container(    bgcolor=ft.Colors.PINK_900,    content=ft.Text("Press Me!",      text_align=ft.TextAlign.CENTER,      style=ft.TextStyle(        size=30,# weight=ft.FontWeight.BOLD,        foreground=ft.Paint(          color=ft.Colors.BLUE_700,          stroke_cap=ft.StrokeCap.BUTT,          stroke_width=2,          stroke_join=ft.StrokeJoin.BEVEL,          style=ft.PaintingStyle.STROKE,),),      theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,),    alignment=ft.alignment.center,    padding=ft.padding.all(10),    height=150,    width=150,    on_click=on_click,    on_long_press=on_long_press,    on_tap_down=on_tap_down,)  t1 = ft.Text(    spans=[      ft.TextSpan("On Click", style=ft.TextStyle(size=16, weight=ft.FontWeight.BOLD)),      ft.TextSpan(" counter: ", style=ft.TextStyle(size=16, italic=True)),      ft.TextSpan(f" {cl_counter} ",        style=ft.TextStyle(size=16, bgcolor=ft.Colors.TEAL_300),),])  t2 = ft.Text(    spans=[      ft.TextSpan("Tap Down", style=ft.TextStyle(size=16, weight=ft.FontWeight.BOLD)),      ft.TextSpan(" counter: ", style=ft.TextStyle(size=16, italic=True)),      ft.TextSpan(f" {td_counter} ",        style=ft.TextStyle(size=16, bgcolor=ft.Colors.TEAL_300),),])  t3 = ft.Text(    spans=[      ft.TextSpan("Long Press", style=ft.TextStyle(size=16, weight=ft.FontWeight.BOLD)),      ft.TextSpan(" counter: ", style=ft.TextStyle(size=16, italic=True)),      ft.TextSpan(f" {lp_counter} ",        style=ft.TextStyle(size=16, bgcolor=ft.Colors.TEAL_300),),])  page.add(c, t1, t3, t2)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/container/container-click-events.py)
![](https://flet.dev/img/docs/controls/container/container-click-events.gif)
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/container.md)
[PreviousColumn](https://flet.dev/docs/controls/column)[NextCupertinoListTile](https://flet.dev/docs/controls/cupertinolisttile)
  * [Examples](https://flet.dev/docs/controls/container/#examples)
    * [Clickable container](https://flet.dev/docs/controls/container/#clickable-container)
  * [Properties](https://flet.dev/docs/controls/container/#properties)
    * [`alignment`](https://flet.dev/docs/controls/container/#alignment)
    * [`animate`](https://flet.dev/docs/controls/container/#animate)
    * [`bgcolor`](https://flet.dev/docs/controls/container/#bgcolor)
    * [`blend_mode`](https://flet.dev/docs/controls/container/#blend_mode)
    * [`blur`](https://flet.dev/docs/controls/container/#blur)
    * [`border`](https://flet.dev/docs/controls/container/#border)
    * [`border_radius`](https://flet.dev/docs/controls/container/#border_radius)
    * [`clip_behavior`](https://flet.dev/docs/controls/container/#clip_behavior)
    * [`color_filter`](https://flet.dev/docs/controls/container/#color_filter)
    * [`content`](https://flet.dev/docs/controls/container/#content)
    * [`dark_theme`](https://flet.dev/docs/controls/container/#dark_theme)
    * [`foreground_decoration`](https://flet.dev/docs/controls/container/#foreground_decoration)
    * [`gradient`](https://flet.dev/docs/controls/container/#gradient)
    * [`ignore_interactions`](https://flet.dev/docs/controls/container/#ignore_interactions)
    * [`image`](https://flet.dev/docs/controls/container/#image)
    * [`ink`](https://flet.dev/docs/controls/container/#ink)
    * [`ink_color`](https://flet.dev/docs/controls/container/#ink_color)
    * [`margin`](https://flet.dev/docs/controls/container/#margin)
    * [`padding`](https://flet.dev/docs/controls/container/#padding)
    * [`rtl`](https://flet.dev/docs/controls/container/#rtl)
    * [`shadow`](https://flet.dev/docs/controls/container/#shadow)
    * [`shape`](https://flet.dev/docs/controls/container/#shape)
    * [`theme_mode`](https://flet.dev/docs/controls/container/#theme_mode)
    * [`theme`](https://flet.dev/docs/controls/container/#theme)
    * [`url`](https://flet.dev/docs/controls/container/#url)
    * [`url_target`](https://flet.dev/docs/controls/container/#url_target)
  * [Events](https://flet.dev/docs/controls/container/#events)
    * [`on_click`](https://flet.dev/docs/controls/container/#on_click)
    * [`on_hover`](https://flet.dev/docs/controls/container/#on_hover)
    * [`on_long_press`](https://flet.dev/docs/controls/container/#on_long_press)
    * [`on_tap_down`](https://flet.dev/docs/controls/container/#on_tap_down)


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
