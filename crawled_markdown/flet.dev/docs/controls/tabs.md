[Skip to main content](https://flet.dev/docs/controls/tabs/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/tabs/)
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
  * [Cookbook](https://flet.dev/docs/controls/tabs/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Layout](https://flet.dev/docs/controls/layout)
  * Tabs


On this page
# Tabs
The Tabs control is used for navigating frequently accessed, distinct content categories. Tabs allow for navigation between two or more content views and relies on text headers to articulate the different sections of content.
## Examples[​](https://flet.dev/docs/controls/tabs/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/layout/tabs)
### Tabs[​](https://flet.dev/docs/controls/tabs/#tabs "Direct link to Tabs")
![](https://flet.dev/img/docs/controls/tabs/tabs-simple.gif)
python/controls/layout/tabs/tabs-simple.py
```
import flet as ftdefmain(page: ft.Page):  t = ft.Tabs(    selected_index=1,    animation_duration=300,    tabs=[      ft.Tab(        text="Tab 1",        content=ft.Container(          content=ft.Text("This is Tab 1"), alignment=ft.alignment.center),),      ft.Tab(        text="Tab 2",        icon=ft.Icons.SETTINGS,        content=ft.Container(          content=ft.Text("This is Tab 2"), alignment=ft.alignment.center),),      ft.Tab(        tab_content=ft.CircleAvatar(          foreground_image_src="https://avatars.githubusercontent.com/u/7119543?s=88&v=4"),        content=ft.Container(          content=ft.Text("This is Tab 3"), alignment=ft.alignment.center),),],    expand=1,)  page.add(t)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/tabs/tabs-simple.py)
## `Tabs` properties[​](https://flet.dev/docs/controls/tabs/#tabs-properties "Direct link to tabs-properties")
### `animation_duration`[​](https://flet.dev/docs/controls/tabs/#animation_duration "Direct link to animation_duration")
Duration of animation in milliseconds of switching between tabs.
Defaults to `50`.
### `clip_behavior`[​](https://flet.dev/docs/controls/tabs/#clip_behavior "Direct link to clip_behavior")
The content will be clipped (or not) according to this option.
Value is of type [`ClipBehavior`](https://flet.dev/docs/reference/types/clipbehavior).
### `divider_color`[​](https://flet.dev/docs/controls/tabs/#divider_color "Direct link to divider_color")
The [color](https://flet.dev/docs/reference/colors) of the divider.
### `divider_height`[​](https://flet.dev/docs/controls/tabs/#divider_height "Direct link to divider_height")
The height of the divider.
Defaults to `1.0`.
### `enable_feedback`[​](https://flet.dev/docs/controls/tabs/#enable_feedback "Direct link to enable_feedback")
Whether detected gestures should provide acoustic and/or haptic feedback. On Android, for example, setting this to `True` produce a click sound and a long-press will produce a short vibration.
Defaults to `True`.
### `indicator_border_radius`[​](https://flet.dev/docs/controls/tabs/#indicator_border_radius "Direct link to indicator_border_radius")
The radius of the indicator's corners.
### `indicator_border_side`[​](https://flet.dev/docs/controls/tabs/#indicator_border_side "Direct link to indicator_border_side")
The [color](https://flet.dev/docs/reference/colors) and weight of the horizontal line drawn below the selected tab.
### `indicator_color`[​](https://flet.dev/docs/controls/tabs/#indicator_color "Direct link to indicator_color")
The [color](https://flet.dev/docs/reference/colors) of the indicator(line that appears below the selected tab).
### `indicator_padding`[​](https://flet.dev/docs/controls/tabs/#indicator_padding "Direct link to indicator_padding")
Locates the selected tab's underline relative to the tab's boundary. The `indicator_tab_size` property can be used to define the tab indicator's bounds in terms of its (centered) tab widget with `False`, or the entire tab with `True`.
### `indicator_tab_size`[​](https://flet.dev/docs/controls/tabs/#indicator_tab_size "Direct link to indicator_tab_size")
`True` for indicator to take entire tab.
### `indicator_thickness`[​](https://flet.dev/docs/controls/tabs/#indicator_thickness "Direct link to indicator_thickness")
The thickness of the indicator. Value must be greater than zero.
Defaults to `3.0` when `secondary=False`, else `3.0`.
### Nesting tabs[​](https://flet.dev/docs/controls/tabs/#nesting-tabs "Direct link to Nesting tabs")
![](https://flet.dev/img/docs/controls/tabs/nested-tabs.gif)
python/controls/layout/tabs/nested-tabs.py
```
import flet as ftdefmain(page: ft.Page):  dt = ft.Tabs(    is_secondary=True,    tabs=[      ft.Tab(text="Fast Food", content=ft.Text("Grab something on the go!")),      ft.Tab(text="Fine Dining", content=ft.Text("Take your time!")),],)  et = ft.Tabs(    is_secondary=True,    tabs=[      ft.Tab(text="Cinema", content=ft.Text("Find a Film!")),      ft.Tab(text="Music", content=ft.Text("Listen to some Tunes!")),],)  lt = ft.Tabs(    is_secondary=True,    tabs=[      ft.Tab(text="Hotel", content=ft.Text("Enjoy your Room!")),      ft.Tab(text="Hostel", content=ft.Text("Grab a Bunk!")),],)  t = ft.Tabs(    selected_index=1,    animation_duration=300,    tabs=[      ft.Tab(        text="Dining",        icon=ft.Icons.RESTAURANT,        content=dt,),      ft.Tab(        text="Entertainment",        icon=ft.Icons.LOCAL_ACTIVITY,        content=et,),      ft.Tab(        text="Lodging",        icon=ft.Icons.HOTEL,        content=lt,),],    expand=1,)  page.add(t)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/tabs/nested-tabs.py)
### `is_secondary`[​](https://flet.dev/docs/controls/tabs/#is_secondary "Direct link to is_secondary")
Whether to create a secondary/nested tab bar. Secondary tabs are used within a content area to further separate related content and establish hierarchy.
Defaults to `False`.
### `label_color`[​](https://flet.dev/docs/controls/tabs/#label_color "Direct link to label_color")
The [color](https://flet.dev/docs/reference/colors) of selected tab labels.
### `label_padding`[​](https://flet.dev/docs/controls/tabs/#label_padding "Direct link to label_padding")
The padding around the tab label.
Value is of type [`Padding`](https://flet.dev/docs/reference/types/padding).
### `label_text_style`[​](https://flet.dev/docs/controls/tabs/#label_text_style "Direct link to label_text_style")
The text style of the tab labels.
Value is of type [`TextStyle`](https://flet.dev/docs/reference/types/textstyle).
### `mouse_cursor`[​](https://flet.dev/docs/controls/tabs/#mouse_cursor "Direct link to mouse_cursor")
The cursor to be displayed when a mouse pointer enters or is hovering over this control. The value is [`MouseCursor`](https://flet.dev/docs/reference/types/mousecursor) enum.
### `overlay_color`[​](https://flet.dev/docs/controls/tabs/#overlay_color "Direct link to overlay_color")
Defines the ink response focus, hover, and splash [colors](https://flet.dev/docs/reference/colors) in various [`ControlState`](https://flet.dev/docs/reference/types/controlstate) states. The following `ControlState` values are supported: `PRESSED`, `HOVERED` and `FOCUSED`.
### `padding`[​](https://flet.dev/docs/controls/tabs/#padding "Direct link to padding")
The padding around the Tabs control.
Value is of type [`Padding`](https://flet.dev/docs/reference/types/padding).
### `selected_index`[​](https://flet.dev/docs/controls/tabs/#selected_index "Direct link to selected_index")
The index of currently selected tab.
### `scrollable`[​](https://flet.dev/docs/controls/tabs/#scrollable "Direct link to scrollable")
Whether this tab bar can be scrolled horizontally.
If `scrollable` is `True`, then each tab is as wide as needed for its label and the entire Tabs controls is scrollable. Otherwise each tab gets an equal share of the available space.
### `splash_border_radius`[​](https://flet.dev/docs/controls/tabs/#splash_border_radius "Direct link to splash_border_radius")
Defines the clipping radius of splashes that extend outside the bounds of the tab.
Value is of type [`BorderRadius`](https://flet.dev/docs/reference/types/borderradius).
### `tab_alignment`[​](https://flet.dev/docs/controls/tabs/#tab_alignment "Direct link to tab_alignment")
Specifies the horizontal alignment of the tabs within the Tabs control.
Value is of type [`TabAlignment`](https://flet.dev/docs/reference/types/tabalignment) and defaults to `TabAlignment.START`, if `scrollable=True`, and to `TabAlignment.FILL`, if `scrollable=False`.
### `tabs`[​](https://flet.dev/docs/controls/tabs/#tabs-1 "Direct link to tabs-1")
A list of `Tab` controls.
### `unselected_label_color`[​](https://flet.dev/docs/controls/tabs/#unselected_label_color "Direct link to unselected_label_color")
The [color](https://flet.dev/docs/reference/colors) of unselected tab labels.
### `unselected_label_text_style`[​](https://flet.dev/docs/controls/tabs/#unselected_label_text_style "Direct link to unselected_label_text_style")
The text style of the unselected tab labels.
Value is of type [`TextStyle`](https://flet.dev/docs/reference/types/textstyle).
## `Tabs` events[​](https://flet.dev/docs/controls/tabs/#tabs-events "Direct link to tabs-events")
### `on_change`[​](https://flet.dev/docs/controls/tabs/#on_change "Direct link to on_change")
Fires when `selected_index` changes.
### `on_click`[​](https://flet.dev/docs/controls/tabs/#on_click "Direct link to on_click")
Fires when a tab is clicked.
## `Tab` properties[​](https://flet.dev/docs/controls/tabs/#tab-properties "Direct link to tab-properties")
### `content`[​](https://flet.dev/docs/controls/tabs/#content "Direct link to content")
A `Control` to display below the Tab when it is selected.
### `icon`[​](https://flet.dev/docs/controls/tabs/#icon "Direct link to icon")
An icon to display on the left of Tab text.
### `tab_content`[​](https://flet.dev/docs/controls/tabs/#tab_content "Direct link to tab_content")
A `Control` representing custom tab content replacing `text` and `icon`.
### `text`[​](https://flet.dev/docs/controls/tabs/#text "Direct link to text")
Tab's display name.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/tabs.md)
[PreviousStack](https://flet.dev/docs/controls/stack)[NextVerticalDivider](https://flet.dev/docs/controls/verticaldivider)
  * [Examples](https://flet.dev/docs/controls/tabs/#examples)
    * [Tabs](https://flet.dev/docs/controls/tabs/#tabs)
  * [`Tabs` properties](https://flet.dev/docs/controls/tabs/#tabs-properties)
    * [`animation_duration`](https://flet.dev/docs/controls/tabs/#animation_duration)
    * [`clip_behavior`](https://flet.dev/docs/controls/tabs/#clip_behavior)
    * [`divider_color`](https://flet.dev/docs/controls/tabs/#divider_color)
    * [`divider_height`](https://flet.dev/docs/controls/tabs/#divider_height)
    * [`enable_feedback`](https://flet.dev/docs/controls/tabs/#enable_feedback)
    * [`indicator_border_radius`](https://flet.dev/docs/controls/tabs/#indicator_border_radius)
    * [`indicator_border_side`](https://flet.dev/docs/controls/tabs/#indicator_border_side)
    * [`indicator_color`](https://flet.dev/docs/controls/tabs/#indicator_color)
    * [`indicator_padding`](https://flet.dev/docs/controls/tabs/#indicator_padding)
    * [`indicator_tab_size`](https://flet.dev/docs/controls/tabs/#indicator_tab_size)
    * [`indicator_thickness`](https://flet.dev/docs/controls/tabs/#indicator_thickness)
    * [Nesting tabs](https://flet.dev/docs/controls/tabs/#nesting-tabs)
    * [`is_secondary`](https://flet.dev/docs/controls/tabs/#is_secondary)
    * [`label_color`](https://flet.dev/docs/controls/tabs/#label_color)
    * [`label_padding`](https://flet.dev/docs/controls/tabs/#label_padding)
    * [`label_text_style`](https://flet.dev/docs/controls/tabs/#label_text_style)
    * [`mouse_cursor`](https://flet.dev/docs/controls/tabs/#mouse_cursor)
    * [`overlay_color`](https://flet.dev/docs/controls/tabs/#overlay_color)
    * [`padding`](https://flet.dev/docs/controls/tabs/#padding)
    * [`selected_index`](https://flet.dev/docs/controls/tabs/#selected_index)
    * [`scrollable`](https://flet.dev/docs/controls/tabs/#scrollable)
    * [`splash_border_radius`](https://flet.dev/docs/controls/tabs/#splash_border_radius)
    * [`tab_alignment`](https://flet.dev/docs/controls/tabs/#tab_alignment)
    * [`tabs`](https://flet.dev/docs/controls/tabs/#tabs-1)
    * [`unselected_label_color`](https://flet.dev/docs/controls/tabs/#unselected_label_color)
    * [`unselected_label_text_style`](https://flet.dev/docs/controls/tabs/#unselected_label_text_style)
  * [`Tabs` events](https://flet.dev/docs/controls/tabs/#tabs-events)
    * [`on_change`](https://flet.dev/docs/controls/tabs/#on_change)
    * [`on_click`](https://flet.dev/docs/controls/tabs/#on_click)
  * [`Tab` properties](https://flet.dev/docs/controls/tabs/#tab-properties)
    * [`content`](https://flet.dev/docs/controls/tabs/#content)
    * [`icon`](https://flet.dev/docs/controls/tabs/#icon)
    * [`tab_content`](https://flet.dev/docs/controls/tabs/#tab_content)
    * [`text`](https://flet.dev/docs/controls/tabs/#text)


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
