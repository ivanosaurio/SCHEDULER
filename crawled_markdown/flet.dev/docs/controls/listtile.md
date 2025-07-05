[Skip to main content](https://flet.dev/docs/controls/listtile/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/listtile/)
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
  * [Cookbook](https://flet.dev/docs/controls/listtile/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Layout](https://flet.dev/docs/controls/layout)
  * ListTile


On this page
# ListTile
A single fixed-height row that typically contains some text as well as a leading or trailing icon.
## Examples[​](https://flet.dev/docs/controls/listtile/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/layout/listtile)
![](https://flet.dev/img/docs/controls/listtile/listtiles.png)
python/controls/layout/list-tile/list-tile-examples.py
```
import flet as ftdefmain(page):  page.title ="ListTile Examples"  page.add(    ft.Card(      content=ft.Container(        width=500,        content=ft.Column([            ft.ListTile(              title=ft.Text("One-line list tile"),),            ft.ListTile(              title=ft.Text("One-line dense list tile"), dense=True),            ft.ListTile(              leading=ft.Icon(ft.Icons.SETTINGS),              title=ft.Text("One-line selected list tile"),              selected=True,),            ft.ListTile(              leading=ft.Image(src="/icons/icon-192.png", fit="contain"),              title=ft.Text("One-line with leading control"),),            ft.ListTile(              title=ft.Text("One-line with trailing control"),              trailing=ft.PopupMenuButton(                icon=ft.Icons.MORE_VERT,                items=[                  ft.PopupMenuItem(text="Item 1"),                  ft.PopupMenuItem(text="Item 2"),],),),            ft.ListTile(              leading=ft.Icon(ft.Icons.ALBUM),              title=ft.Text("One-line with leading and trailing controls"),              trailing=ft.PopupMenuButton(                icon=ft.Icons.MORE_VERT,                items=[                  ft.PopupMenuItem(text="Item 1"),                  ft.PopupMenuItem(text="Item 2"),],),),            ft.ListTile(              leading=ft.Icon(ft.Icons.SNOOZE),              title=ft.Text("Two-line with leading and trailing controls"),              subtitle=ft.Text("Here is a second title."),              trailing=ft.PopupMenuButton(                icon=ft.Icons.MORE_VERT,                items=[                  ft.PopupMenuItem(text="Item 1"),                  ft.PopupMenuItem(text="Item 2"),],),),],          spacing=0,),        padding=ft.padding.symmetric(vertical=10),)))ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/list-tile/list-tile-examples.py)
## Properties[​](https://flet.dev/docs/controls/listtile/#properties "Direct link to Properties")
### `adaptive`[​](https://flet.dev/docs/controls/listtile/#adaptive "Direct link to adaptive")
If the value is `True`, an adaptive ListTile is created based on whether the target platform is iOS/macOS.
On iOS and macOS, a [`CupertinoListTile`](https://flet.dev/docs/controls/cupertinolisttile) is created, which has matching functionality and presentation as `ListTile`, and the graphics as expected on iOS. On other platforms, a Material ListTile is created.
If a `CupertinoListTile` is created, the following parameters are ignored: `autofocus`, `dense`, `is_three_line`, `selected` and `on_long_press` event.
Defaults to `False`.
### `autofocus`[​](https://flet.dev/docs/controls/listtile/#autofocus "Direct link to autofocus")
`True` if the control will be selected as the initial focus. If there is more than one control on a page with autofocus set, then the first one added to the page will get focus.
### `bgcolor`[​](https://flet.dev/docs/controls/listtile/#bgcolor "Direct link to bgcolor")
The list tile's background [color](https://flet.dev/docs/reference/colors).
### `bgcolor_activated`[​](https://flet.dev/docs/controls/listtile/#bgcolor_activated "Direct link to bgcolor_activated")
The list tile's splash [color](https://flet.dev/docs/reference/colors) after the tile was tapped.
### `content_padding`[​](https://flet.dev/docs/controls/listtile/#content_padding "Direct link to content_padding")
The tile's internal padding. Insets a ListTile's contents: its `leading`, `title`, `subtitle`, and `trailing` controls.
Value is of type [`Padding`](https://flet.dev/docs/reference/types/padding) and defaults to `padding.symmetric(horizontal=16)`.
### `dense`[​](https://flet.dev/docs/controls/listtile/#dense "Direct link to dense")
Whether this list tile is part of a vertically dense list. Dense list tiles default to a smaller height.
### `enable_feedback`[​](https://flet.dev/docs/controls/listtile/#enable_feedback "Direct link to enable_feedback")
Whether detected gestures should provide acoustic and/or haptic feedback. On Android, for example, setting this to `True` produce a click sound and a long-press will produce a short vibration.
Defaults to `True`.
### `horizontal_spacing`[​](https://flet.dev/docs/controls/listtile/#horizontal_spacing "Direct link to horizontal_spacing")
The horizontal gap between the `title` and the `leading`/`trailing` controls.
Defaults to `16`.
### `hover_color`[​](https://flet.dev/docs/controls/listtile/#hover_color "Direct link to hover_color")
The tile's [color](https://flet.dev/docs/reference/colors) when hovered.
### `icon_color`[​](https://flet.dev/docs/controls/listtile/#icon_color "Direct link to icon_color")
Defines the default [color](https://flet.dev/docs/reference/colors) for the `Icon`s present in `leading` and `trailing`.
### `is_three_line`[​](https://flet.dev/docs/controls/listtile/#is_three_line "Direct link to is_three_line")
Whether this list tile is intended to display three lines of text.
If `True`, then subtitle must be non-null (since it is expected to give the second and third lines of text).
If `False`, the list tile is treated as having one line if the subtitle is null and treated as having two lines if the subtitle is non-null.
When using a Text control for title and subtitle, you can enforce line limits using [`Text.max_lines`](https://flet.dev/docs/controls/text#max_lines).
### `leading`[​](https://flet.dev/docs/controls/listtile/#leading "Direct link to leading")
A `Control` to display before the title.
### `leading_and_trailing_text_style`[​](https://flet.dev/docs/controls/listtile/#leading_and_trailing_text_style "Direct link to leading_and_trailing_text_style")
The [`TextStyle`](https://flet.dev/docs/reference/types/textstyle) for the `leading` and `trailing` controls.
### `min_height`[​](https://flet.dev/docs/controls/listtile/#min_height "Direct link to min_height")
The minimum height allocated for this control.
If `None` or not set, default tile heights are `56.0`, `72.0`, and `88.0` for one, two, and three lines of text respectively. If [`dense`](https://flet.dev/docs/controls/listtile/#dense) is `True`, these defaults are changed to `48.0`, `64.0`, and `76.0`.
Note that, a visual density value or a large title will also adjust the default tile heights.
### `min_leading_width`[​](https://flet.dev/docs/controls/listtile/#min_leading_width "Direct link to min_leading_width")
The minimum width allocated for the `leading` control.
Defaults to `40`.
### `min_vertical_padding`[​](https://flet.dev/docs/controls/listtile/#min_vertical_padding "Direct link to min_vertical_padding")
The minimum padding on the top and bottom of the `title` and `subtitle` controls.
Defaults to `4`.
### `mouse_cursor`[​](https://flet.dev/docs/controls/listtile/#mouse_cursor "Direct link to mouse_cursor")
The cursor to be displayed when a mouse pointer enters or is hovering over this control. The value is [`MouseCursor`](https://flet.dev/docs/reference/types/mousecursor) enum.
### `selected`[​](https://flet.dev/docs/controls/listtile/#selected "Direct link to selected")
If this tile is also enabled then icons and text are rendered with the same color. By default the selected color is the theme's primary color.
### `selected_color`[​](https://flet.dev/docs/controls/listtile/#selected_color "Direct link to selected_color")
Defines the [color](https://flet.dev/docs/reference/colors) used for icons and text when `selected=True`.
### `selected_tile_color`[​](https://flet.dev/docs/controls/listtile/#selected_tile_color "Direct link to selected_tile_color")
Defines the background [color](https://flet.dev/docs/reference/colors) of ListTile when `selected=True`.
### `shape`[​](https://flet.dev/docs/controls/listtile/#shape "Direct link to shape")
The tile's shape. The value is an instance of [`OutlinedBorder`](https://flet.dev/docs/reference/types/outlinedborder) class.
### `subtitle`[​](https://flet.dev/docs/controls/listtile/#subtitle "Direct link to subtitle")
Additional content displayed below the title. Typically a [`Text`](https://flet.dev/docs/controls/text) widget.
If `is_three_line` is `False`, this should not wrap. If `is_three_line` is `True`, this should be configured to take a maximum of two lines. For example, you can use [`Text.max_lines`](https://flet.dev/docs/controls/text#max_lines) to enforce the number of lines.
### `subtitle_text_style`[​](https://flet.dev/docs/controls/listtile/#subtitle_text_style "Direct link to subtitle_text_style")
The [`TextStyle`](https://flet.dev/docs/reference/types/textstyle) for the `subtitle` control.
### `style`[​](https://flet.dev/docs/controls/listtile/#style "Direct link to style")
Defines the font used for the title.
Value is of type [`ListTileStyle`](https://flet.dev/docs/reference/types/listtilestyle) and defaults to `ListTileStyle.LIST`.
### `text_color`[​](https://flet.dev/docs/controls/listtile/#text_color "Direct link to text_color")
The [color](https://flet.dev/docs/reference/colors) used for text. Defines the color of `Text` controls found in `title`, `subtitle`, `leading`, and `trailing`.
### `title`[​](https://flet.dev/docs/controls/listtile/#title "Direct link to title")
A `Control` to display as primary content of the list tile.
Typically a [`Text`](https://flet.dev/docs/controls/text) control. This should not wrap. To enforce the single line limit, use [`Text.max_lines`](https://flet.dev/docs/controls/text#max_lines).
### `title_alignment`[​](https://flet.dev/docs/controls/listtile/#title_alignment "Direct link to title_alignment")
Defines how `leading` and `trailing` are vertically aligned relative to the titles (`title` and `subtitle`).
Value is of type [`ListTileAlignment`](https://flet.dev/docs/reference/types/listtilealignment) and defaults to `ListTileAlignment.THREE_LINE` in Material 3 or `ListTileAlignment.TITLE_HEIGHT` in Material 2.
### `title_text_style`[​](https://flet.dev/docs/controls/listtile/#title_text_style "Direct link to title_text_style")
The [`TextStyle`](https://flet.dev/docs/reference/types/textstyle) for the `title` control.
### `toggle_inputs`[​](https://flet.dev/docs/controls/listtile/#toggle_inputs "Direct link to toggle_inputs")
Whether clicking on a list tile should toggle the state of `Radio`, `Checkbox` or `Switch` inside the tile.
Defaults to `False`.
### `trailing`[​](https://flet.dev/docs/controls/listtile/#trailing "Direct link to trailing")
A `Control` to display after the title. Typically an [`Icon`](https://flet.dev/docs/controls/icon) control.
### `url`[​](https://flet.dev/docs/controls/listtile/#url "Direct link to url")
The URL to open when the list tile is clicked. If registered, `on_click` event is fired after that.
### `url_target`[​](https://flet.dev/docs/controls/listtile/#url_target "Direct link to url_target")
Where to open URL in the web mode.
Value is of type [`UrlTarget`](https://flet.dev/docs/reference/types/urltarget) and defaults to `UrlTarget.BLANK`.
### `visual_density`[​](https://flet.dev/docs/controls/listtile/#visual_density "Direct link to visual_density")
Defines how compact the control's layout will be.
Value is of type [`VisualDensity`](https://flet.dev/docs/reference/types/visualdensity).
## Events[​](https://flet.dev/docs/controls/listtile/#events "Direct link to Events")
### `on_click`[​](https://flet.dev/docs/controls/listtile/#on_click "Direct link to on_click")
Fires when a user clicks or taps the list tile.
### `on_long_press`[​](https://flet.dev/docs/controls/listtile/#on_long_press "Direct link to on_long_press")
Fires when the user long-presses on this list tile.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/listtile.md)
[PreviousGridView](https://flet.dev/docs/controls/gridview)[NextListView](https://flet.dev/docs/controls/listview)
  * [Examples](https://flet.dev/docs/controls/listtile/#examples)
  * [Properties](https://flet.dev/docs/controls/listtile/#properties)
    * [`adaptive`](https://flet.dev/docs/controls/listtile/#adaptive)
    * [`autofocus`](https://flet.dev/docs/controls/listtile/#autofocus)
    * [`bgcolor`](https://flet.dev/docs/controls/listtile/#bgcolor)
    * [`bgcolor_activated`](https://flet.dev/docs/controls/listtile/#bgcolor_activated)
    * [`content_padding`](https://flet.dev/docs/controls/listtile/#content_padding)
    * [`dense`](https://flet.dev/docs/controls/listtile/#dense)
    * [`enable_feedback`](https://flet.dev/docs/controls/listtile/#enable_feedback)
    * [`horizontal_spacing`](https://flet.dev/docs/controls/listtile/#horizontal_spacing)
    * [`hover_color`](https://flet.dev/docs/controls/listtile/#hover_color)
    * [`icon_color`](https://flet.dev/docs/controls/listtile/#icon_color)
    * [`is_three_line`](https://flet.dev/docs/controls/listtile/#is_three_line)
    * [`leading`](https://flet.dev/docs/controls/listtile/#leading)
    * [`leading_and_trailing_text_style`](https://flet.dev/docs/controls/listtile/#leading_and_trailing_text_style)
    * [`min_height`](https://flet.dev/docs/controls/listtile/#min_height)
    * [`min_leading_width`](https://flet.dev/docs/controls/listtile/#min_leading_width)
    * [`min_vertical_padding`](https://flet.dev/docs/controls/listtile/#min_vertical_padding)
    * [`mouse_cursor`](https://flet.dev/docs/controls/listtile/#mouse_cursor)
    * [`selected`](https://flet.dev/docs/controls/listtile/#selected)
    * [`selected_color`](https://flet.dev/docs/controls/listtile/#selected_color)
    * [`selected_tile_color`](https://flet.dev/docs/controls/listtile/#selected_tile_color)
    * [`shape`](https://flet.dev/docs/controls/listtile/#shape)
    * [`subtitle`](https://flet.dev/docs/controls/listtile/#subtitle)
    * [`subtitle_text_style`](https://flet.dev/docs/controls/listtile/#subtitle_text_style)
    * [`style`](https://flet.dev/docs/controls/listtile/#style)
    * [`text_color`](https://flet.dev/docs/controls/listtile/#text_color)
    * [`title`](https://flet.dev/docs/controls/listtile/#title)
    * [`title_alignment`](https://flet.dev/docs/controls/listtile/#title_alignment)
    * [`title_text_style`](https://flet.dev/docs/controls/listtile/#title_text_style)
    * [`toggle_inputs`](https://flet.dev/docs/controls/listtile/#toggle_inputs)
    * [`trailing`](https://flet.dev/docs/controls/listtile/#trailing)
    * [`url`](https://flet.dev/docs/controls/listtile/#url)
    * [`url_target`](https://flet.dev/docs/controls/listtile/#url_target)
    * [`visual_density`](https://flet.dev/docs/controls/listtile/#visual_density)
  * [Events](https://flet.dev/docs/controls/listtile/#events)
    * [`on_click`](https://flet.dev/docs/controls/listtile/#on_click)
    * [`on_long_press`](https://flet.dev/docs/controls/listtile/#on_long_press)


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
