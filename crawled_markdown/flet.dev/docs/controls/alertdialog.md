[Skip to main content](https://flet.dev/docs/controls/alertdialog/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/alertdialog/)
  * [Controls](https://flet.dev/docs/controls)
    * [Layout](https://flet.dev/docs/controls/layout)
    * [Navigation](https://flet.dev/docs/controls/app-structure-navigation)
    * [Information Displays](https://flet.dev/docs/controls/information-displays)
    * [Buttons](https://flet.dev/docs/controls/buttons)
    * [Input and Selections](https://flet.dev/docs/controls/input-and-selections)
    * [Dialogs, Alerts and Panels](https://flet.dev/docs/controls/dialogs-alerts-panels)
      * [AlertDialog](https://flet.dev/docs/controls/alertdialog)
      * [Banner](https://flet.dev/docs/controls/banner)
      * [BottomSheet](https://flet.dev/docs/controls/bottomsheet)
      * [CupertinoActionSheet](https://flet.dev/docs/controls/cupertinoactionsheet)
      * [CupertinoAlertDialog](https://flet.dev/docs/controls/cupertinoalertdialog)
      * [CupertinoBottomSheet](https://flet.dev/docs/controls/cupertinobottomsheet)
      * [CupertinoContextMenu](https://flet.dev/docs/controls/cupertinocontextmenu)
      * [CupertinoDatePicker](https://flet.dev/docs/controls/cupertinodatepicker)
      * [CupertinoPicker](https://flet.dev/docs/controls/cupertinopicker)
      * [CupertinoTimerPicker](https://flet.dev/docs/controls/cupertinotimerpicker)
      * [DatePicker](https://flet.dev/docs/controls/datepicker)
      * [SnackBar](https://flet.dev/docs/controls/snackbar)
      * [TimePicker](https://flet.dev/docs/controls/timepicker)
    * [Charts](https://flet.dev/docs/controls/charts)
    * [Animations](https://flet.dev/docs/controls/animations)
    * [Utility](https://flet.dev/docs/controls/utility)
  * [Cookbook](https://flet.dev/docs/controls/alertdialog/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Dialogs, Alerts and Panels](https://flet.dev/docs/controls/dialogs-alerts-panels)
  * AlertDialog


On this page
# AlertDialog
A material design alert dialog.
An alert dialog informs the user about situations that require acknowledgement. An alert dialog has an optional title and an optional list of actions. The title is displayed above the content and the actions are displayed below the content.
To open this control, simply call the [`page.open()`](https://flet.dev/docs/controls/page#opencontrol) helper-method.
## Examples[​](https://flet.dev/docs/controls/alertdialog/#examples "Direct link to Examples")
[Live example](https://flet-controls-gallery.fly.dev/dialogs/alertdialog)
### Basic and modal dialogs[​](https://flet.dev/docs/controls/alertdialog/#basic-and-modal-dialogs "Direct link to Basic and modal dialogs")
python/controls/dialogs-alerts-panels/alert-dialog/dialogs.py
```
import flet as ftdefmain(page: ft.Page):  page.title ="AlertDialog examples"  dlg = ft.AlertDialog(    title=ft.Text("Hello"),    content=ft.Text("You are notified!"),    alignment=ft.alignment.center,    on_dismiss=lambda e:print("Dialog dismissed!"),    title_padding=ft.padding.all(25),)  dlg_modal = ft.AlertDialog(    modal=True,    title=ft.Text("Please confirm"),    content=ft.Text("Do you really want to delete all those files?"),    actions=[      ft.TextButton("Yes", on_click=lambda e: page.close(dlg_modal)),      ft.TextButton("No", on_click=lambda e: page.close(dlg_modal)),],    actions_alignment=ft.MainAxisAlignment.END,    on_dismiss=lambda e:print("Modal dialog dismissed!"),)  page.add(    ft.ElevatedButton("Open dialog", on_click=lambda e: page.open(dlg)),    ft.ElevatedButton("Open modal dialog", on_click=lambda e: page.open(dlg_modal)),)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/dialogs-alerts-panels/alert-dialog/dialogs.py)
![](https://flet.dev/img/docs/controls/alertdialog/alertdialog-with-custom-content.gif)
## Properties[​](https://flet.dev/docs/controls/alertdialog/#properties "Direct link to Properties")
### `actions`[​](https://flet.dev/docs/controls/alertdialog/#actions "Direct link to actions")
The (optional) set of actions that are displayed at the bottom of the dialog.
Typically this is a list of [`TextButton`](https://flet.dev/docs/controls/textbutton) controls.
### `action_button_padding`[​](https://flet.dev/docs/controls/alertdialog/#action_button_padding "Direct link to action_button_padding")
The padding that surrounds each button in `actions`.
Value is of type [`PaddingValue`](https://flet.dev/docs/reference/types/aliases#paddingvalue).
### `actions_alignment`[​](https://flet.dev/docs/controls/alertdialog/#actions_alignment "Direct link to actions_alignment")
Defines the horizontal layout of the actions.
Value is of type [`MainAxisAlignment`](https://flet.dev/docs/reference/types/mainaxisalignment) and defaults to `MainAxisAlignment.END`.
### `actions_padding`[​](https://flet.dev/docs/controls/alertdialog/#actions_padding "Direct link to actions_padding")
Padding around the set of actions at the bottom of the dialog.
Typically used to provide padding to the button bar between the button bar and the edges of the dialog.
If are no actions, then no padding will be included. The padding around the button bar defaults to zero.
Value is of type [`PaddingValue`](https://flet.dev/docs/reference/types/aliases#paddingvalue).
### `adaptive`[​](https://flet.dev/docs/controls/alertdialog/#adaptive "Direct link to adaptive")
If the value is `True`, an adaptive AlertDialog is created based on whether the target platform is iOS/macOS.
On iOS and macOS, a [`CupertinoAlertDialog`](https://flet.dev/docs/controls/cupertinoalertdialog) is created, which has matching functionality and presentation as `AlertDialog`, and the graphics as expected on iOS. On other platforms, a Material AlertDialog is created.
See the example of usage [here](https://flet.dev/docs/controls/cupertinoalertdialog#cupertinoalertdialog-and-adaptive-alertdialog-example).
Value is of type `bool` and defaults to `False`.
### `barrier_color`[​](https://flet.dev/docs/controls/alertdialog/#barrier_color "Direct link to barrier_color")
The [color](https://flet.dev/docs/reference/colors) of the modal barrier that darkens everything below the dialog.
If `None`, the [`DialogTheme.barrier_color`](https://flet.dev/docs/reference/types/dialogtheme#barrier_color) is used. If it is also `None`, then `Colors.BLACK_54` is used.
### `bgcolor`[​](https://flet.dev/docs/controls/alertdialog/#bgcolor "Direct link to bgcolor")
The background [color](https://flet.dev/docs/reference/colors) of the dialog's surface.
### `clip_behavior`[​](https://flet.dev/docs/controls/alertdialog/#clip_behavior "Direct link to clip_behavior")
Controls how the contents of the dialog are clipped (or not) to the given `shape`.
Value is of type [`ClipBehavior`](https://flet.dev/docs/reference/types/clipbehavior) and defaults to `ClipBehavior.NONE`.
### `content`[​](https://flet.dev/docs/controls/alertdialog/#content "Direct link to content")
The (optional) content of the dialog is displayed in the center of the dialog in a lighter font. Typically this is a [`Column`](https://flet.dev/docs/controls/column) that contains the dialog's [`Text`](https://flet.dev/docs/controls/text) message.
Value is of type `Control`.
### `content_padding`[​](https://flet.dev/docs/controls/alertdialog/#content_padding "Direct link to content_padding")
Padding around the content.
If there is no content, no padding will be provided. Otherwise, padding of 20 pixels is provided above the content to separate the content from the title, and padding of 24 pixels is provided on the left, right, and bottom to separate the content from the other edges of the dialog.
Value is of type [`PaddingValue`](https://flet.dev/docs/reference/types/aliases#paddingvalue).
### `elevation`[​](https://flet.dev/docs/controls/alertdialog/#elevation "Direct link to elevation")
Defines the elevation (z-coordinate) at which the dialog should appear.
Value is of type [`OptionalNumber`](https://flet.dev/docs/reference/types/aliases#optionalnumber).
### `icon`[​](https://flet.dev/docs/controls/alertdialog/#icon "Direct link to icon")
A control that is displayed at the top of the dialog. Typically a [`Icon`](https://flet.dev/docs/controls/icon) control.
### `icon_padding`[​](https://flet.dev/docs/controls/alertdialog/#icon_padding "Direct link to icon_padding")
Padding around the `icon`.
Value is of type [`PaddingValue`](https://flet.dev/docs/reference/types/aliases#paddingvalue).
### `inset_padding`[​](https://flet.dev/docs/controls/alertdialog/#inset_padding "Direct link to inset_padding")
Padding around the Dialog itself.
Value is of type [`PaddingValue`](https://flet.dev/docs/reference/types/aliases#paddingvalue).
Defaults to `padding.symmetric(vertical=40, horizontal=24)` - 40 pixels horizontally and 24 pixels vertically outside of the dialog box.
### `modal`[​](https://flet.dev/docs/controls/alertdialog/#modal "Direct link to modal")
Whether dialog can be dismissed/closed by clicking the area outside of it.
Value is of type `bool` and defaults to `False`.
### `open`[​](https://flet.dev/docs/controls/alertdialog/#open "Direct link to open")
Set to `True` to display a dialog.
Value is of type `bool` and defaults to `False`.
### `semantics_label`[​](https://flet.dev/docs/controls/alertdialog/#semantics_label "Direct link to semantics_label")
The semantic label of the dialog used by accessibility frameworks to announce screen transitions when the dialog is opened and closed.
In iOS, if this label is not provided, a semantic label will be inferred from the `title` if it is not null.
Value is of type `str`.
### `shadow_color`[​](https://flet.dev/docs/controls/alertdialog/#shadow_color "Direct link to shadow_color")
The [color](https://flet.dev/docs/reference/colors) used to paint a drop shadow under the dialog, which reflects the dialog's elevation.
### `shape`[​](https://flet.dev/docs/controls/alertdialog/#shape "Direct link to shape")
The shape of the dialog.
Value is of type [`OutlinedBorder`](https://flet.dev/docs/reference/types/outlinedborder) and defaults to `RoundedRectangleBorder(radius=4.0)`.
### `surface_tint_color`[​](https://flet.dev/docs/controls/alertdialog/#surface_tint_color "Direct link to surface_tint_color")
The [color](https://flet.dev/docs/reference/colors) used as a surface tint overlay on the dialog's background color, which reflects the dialog's elevation.
### `title`[​](https://flet.dev/docs/controls/alertdialog/#title "Direct link to title")
The (optional) title of the dialog is displayed in a large font at the top of the dialog.
Typically a [`Text`](https://flet.dev/docs/controls/text) control.
### `title_padding`[​](https://flet.dev/docs/controls/alertdialog/#title_padding "Direct link to title_padding")
Padding around the title.
If there is no title, no padding will be provided. Otherwise, this padding is used.
Value is of type [`PaddingValue`](https://flet.dev/docs/reference/types/aliases#paddingvalue).
Defaults to providing `24` pixels on the top, left, and right of the title. If the `content` is not `None`, then no bottom padding is provided (but see [`content_padding`](https://flet.dev/docs/controls/alertdialog/#content_padding)). If it is not set, then an extra `20` pixels of bottom padding is added to separate the title from the actions.
## Events[​](https://flet.dev/docs/controls/alertdialog/#events "Direct link to Events")
### `on_dismiss`[​](https://flet.dev/docs/controls/alertdialog/#on_dismiss "Direct link to on_dismiss")
Fires when dialog is dismissed.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/alertdialog.md)
[PreviousDialogs, Alerts and Panels](https://flet.dev/docs/controls/dialogs-alerts-panels)[NextBanner](https://flet.dev/docs/controls/banner)
  * [Examples](https://flet.dev/docs/controls/alertdialog/#examples)
    * [Basic and modal dialogs](https://flet.dev/docs/controls/alertdialog/#basic-and-modal-dialogs)
  * [Properties](https://flet.dev/docs/controls/alertdialog/#properties)
    * [`actions`](https://flet.dev/docs/controls/alertdialog/#actions)
    * [`action_button_padding`](https://flet.dev/docs/controls/alertdialog/#action_button_padding)
    * [`actions_alignment`](https://flet.dev/docs/controls/alertdialog/#actions_alignment)
    * [`actions_padding`](https://flet.dev/docs/controls/alertdialog/#actions_padding)
    * [`adaptive`](https://flet.dev/docs/controls/alertdialog/#adaptive)
    * [`barrier_color`](https://flet.dev/docs/controls/alertdialog/#barrier_color)
    * [`bgcolor`](https://flet.dev/docs/controls/alertdialog/#bgcolor)
    * [`clip_behavior`](https://flet.dev/docs/controls/alertdialog/#clip_behavior)
    * [`content`](https://flet.dev/docs/controls/alertdialog/#content)
    * [`content_padding`](https://flet.dev/docs/controls/alertdialog/#content_padding)
    * [`elevation`](https://flet.dev/docs/controls/alertdialog/#elevation)
    * [`icon`](https://flet.dev/docs/controls/alertdialog/#icon)
    * [`icon_padding`](https://flet.dev/docs/controls/alertdialog/#icon_padding)
    * [`inset_padding`](https://flet.dev/docs/controls/alertdialog/#inset_padding)
    * [`modal`](https://flet.dev/docs/controls/alertdialog/#modal)
    * [`open`](https://flet.dev/docs/controls/alertdialog/#open)
    * [`semantics_label`](https://flet.dev/docs/controls/alertdialog/#semantics_label)
    * [`shadow_color`](https://flet.dev/docs/controls/alertdialog/#shadow_color)
    * [`shape`](https://flet.dev/docs/controls/alertdialog/#shape)
    * [`surface_tint_color`](https://flet.dev/docs/controls/alertdialog/#surface_tint_color)
    * [`title`](https://flet.dev/docs/controls/alertdialog/#title)
    * [`title_padding`](https://flet.dev/docs/controls/alertdialog/#title_padding)
  * [Events](https://flet.dev/docs/controls/alertdialog/#events)
    * [`on_dismiss`](https://flet.dev/docs/controls/alertdialog/#on_dismiss)


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
