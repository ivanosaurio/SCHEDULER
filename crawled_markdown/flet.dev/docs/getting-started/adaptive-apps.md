[Skip to main content](https://flet.dev/docs/getting-started/adaptive-apps/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
    * [Create a new Flet app](https://flet.dev/docs/getting-started/create-flet-app)
    * [Running Flet app](https://flet.dev/docs/getting-started/running-app)
    * [Flet controls](https://flet.dev/docs/getting-started/flet-controls)
    * [Custom controls](https://flet.dev/docs/getting-started/custom-controls)
    * [Adaptive apps](https://flet.dev/docs/getting-started/adaptive-apps)
    * [Navigation and routing](https://flet.dev/docs/getting-started/navigation-and-routing)
    * [Testing on iOS](https://flet.dev/docs/getting-started/testing-on-ios)
    * [Testing on Android](https://flet.dev/docs/getting-started/testing-on-android)
    * [Async apps](https://flet.dev/docs/getting-started/async-apps)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/getting-started/adaptive-apps/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/getting-started/adaptive-apps/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * Adaptive apps


On this page
# Adaptive apps
Flet framework allows you to develop adaptive apps which means having a single codebase that will deliver different look depending on the device's platform.
Below is the example of a very simple app that has a different look on iOS and Android platforms:
```
import flet as ftdefmain(page):  page.adaptive =True  page.appbar = ft.AppBar(    leading=ft.TextButton("New", style=ft.ButtonStyle(padding=0)),    title=ft.Text("Adaptive AppBar"),    actions=[      ft.IconButton(ft.cupertino_icons.ADD, style=ft.ButtonStyle(padding=0))],    bgcolor=ft.Colors.with_opacity(0.04, ft.CupertinoColors.SYSTEM_BACKGROUND),)  page.navigation_bar = ft.NavigationBar(    destinations=[      ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explore"),      ft.NavigationBarDestination(icon=ft.Icons.COMMUTE, label="Commute"),      ft.NavigationBarDestination(        icon=ft.Icons.BOOKMARK_BORDER,        selected_icon=ft.Icons.BOOKMARK,        label="Bookmark",),],    border=ft.Border(      top=ft.BorderSide(color=ft.CupertinoColors.SYSTEM_GREY2, width=0)),)  page.add(    ft.SafeArea(      ft.Column([          ft.Checkbox(value=False, label="Dark Mode"),          ft.Text("First field:"),          ft.TextField(keyboard_type=ft.KeyboardType.TEXT),          ft.Text("Second field:"),          ft.TextField(keyboard_type=ft.KeyboardType.TEXT),          ft.Switch(label="A switch"),          ft.FilledButton(content=ft.Text("Adaptive button")),          ft.Text("Text line 1"),          ft.Text("Text line 2"),          ft.Text("Text line 3"),])))ft.app(main)
```

By setting just `page.adaptive = True` you can make you app looking awesome on both iOS and Android devices:
### iPhone
![](https://flet.dev/img/blog/adaptive/iphone-adaptive-app.png)
### Android
![](https://flet.dev/img/blog/adaptive/android-adaptive-app.png)
## Material and Cupertino controls[​](https://flet.dev/docs/getting-started/adaptive-apps/#material-and-cupertino-controls "Direct link to Material and Cupertino controls")
Most of Flet controls are based on [Material design](https://m3.material.io/).
There is also a number of iOS-style controls in Flet that are called Cupertino controls.
Cupertino controls usually have a matching Material control that has [`adaptive`](https://flet.dev/docs/controls#adaptive) property which defaults to`False`. When using a Material control with `adaptive` property set to `True`, a different control will be created depending on the platform, for example:
```
ft.Checkbox(adaptive=True, value=True, label="Adaptive Checkbox")
```

Flet checks the value of [`page.platform`](https://flet.dev/docs/controls/page#platform) property and if it is `ft.PagePlatform.IOS` or `ft.PagePlatform.MACOS`, Cupertino control will be created; in all other cases Material control will be created.
note
[`adaptive`](https://flet.dev/docs/controls#adaptive) property can be set for an individual control or a container control such as `Row`, `Column` or any other control that has `content` or `controls` property. If container control is adaptive, all its child controls will be adaptive, unless `adaptive` property is explicitly set to `False` for a child control.
Below is the list of adaptive Material controls and their matching Cupertino controls:
[AlertDialog](https://flet.dev/docs/controls/alertdialog)![](https://flet.dev/img/docs/adaptive-apps/alertdialog.png)
[CupertinoAlertDialog](https://flet.dev/docs/controls/cupertinoalertdialog)![](https://flet.dev/img/docs/adaptive-apps/cupertinoalertdialog.png)
[Any button in Dialog actions](https://flet.dev/docs/controls/buttons)![](https://flet.dev/img/docs/adaptive-apps/dialogactions.png)
[CupertinoDialogAction](https://flet.dev/docs/controls/cupertinodialogaction)![](https://flet.dev/img/docs/adaptive-apps/cupertinodialogactions.png)
[AppBar](https://flet.dev/docs/controls/appbar)![](https://flet.dev/img/docs/adaptive-apps/appbar.png)
[CupertinoAppBar](https://flet.dev/docs/controls/cupertinoappbar)![](https://flet.dev/img/docs/adaptive-apps/cupertinoappbar.png)
[NavigationBar](https://flet.dev/docs/controls/navigationbar)![](https://flet.dev/img/docs/adaptive-apps/navigationbar.png)
[CupertinoNavigationBar](https://flet.dev/docs/controls/cupertinonavigationbar)![](https://flet.dev/img/docs/adaptive-apps/cupertinonavigationbar.png)
[ListTile](https://flet.dev/docs/controls/listtile)![](https://flet.dev/img/docs/adaptive-apps/listtile.png)
[CupertinoListTile](https://flet.dev/docs/controls/cupertinolisttile)![](https://flet.dev/img/docs/adaptive-apps/cupertinolisttile.png)
[TextField](https://flet.dev/docs/controls/textfield)![](https://flet.dev/img/docs/adaptive-apps/textfield.png)
[CupertinoTextField](https://flet.dev/docs/controls/cupertinotextfield)![](https://flet.dev/img/docs/adaptive-apps/cupertinotextfield.png)
[Checkbox](https://flet.dev/docs/controls/checkbox)![](https://flet.dev/img/docs/adaptive-apps/checkbox.png)
[CupertinoCheckbox](https://flet.dev/docs/controls/cupertinocheckbox)![](https://flet.dev/img/docs/adaptive-apps/cupertinocheckbox.png)
[Slider](https://flet.dev/docs/controls/slider)![](https://flet.dev/img/docs/adaptive-apps/slider.png)
[CupertinoSlider](https://flet.dev/docs/controls/cupertinoslider)![](https://flet.dev/img/docs/adaptive-apps/cupertinoslider.png)
[Switch](https://flet.dev/docs/controls/switch)![](https://flet.dev/img/docs/adaptive-apps/switch.png)
[CupertinoSwitch](https://flet.dev/docs/controls/cupertinoswitch)![](https://flet.dev/img/docs/adaptive-apps/cupertinoswitch.png)
[Radio](https://flet.dev/docs/controls/radio)![](https://flet.dev/img/docs/adaptive-apps/radio.png)
[CupertinoRadio](https://flet.dev/docs/controls/cupertinoradio)![](https://flet.dev/img/docs/adaptive-apps/cupertinoradio.png)
[FilledButton](https://flet.dev/docs/controls/filledbutton)![](https://flet.dev/img/docs/adaptive-apps/filledbutton.png)
[CupertinoFilledButton](https://flet.dev/docs/controls/cupertinobutton)![](https://flet.dev/img/docs/adaptive-apps/cupertinofilledbutton.png)
[FilledTonalButton](https://flet.dev/docs/controls/filledtonalbutton)![](https://flet.dev/img/docs/adaptive-apps/filledtonalbutton.png)
[CupertinoButton](https://flet.dev/docs/controls/cupertinobutton)![](https://flet.dev/img/docs/adaptive-apps/cupertinobutton-filledtonal.png)
[IconButton](https://flet.dev/docs/controls/iconbutton)![](https://flet.dev/img/docs/adaptive-apps/icon-button.png)
[CupertinoButton](https://flet.dev/docs/controls/cupertinobutton)![](https://flet.dev/img/docs/adaptive-apps/icon-button-cupertino.png)
[ElevatedButton](https://flet.dev/docs/controls/elevatedbutton)![](https://flet.dev/img/docs/adaptive-apps/elevatedbutton.png)
[CupertinoButton](https://flet.dev/docs/controls/cupertinobutton)![](https://flet.dev/img/docs/adaptive-apps/cupertinobutton.png)
[OutlinedButton](https://flet.dev/docs/controls/outlinedbutton)![](https://flet.dev/img/docs/adaptive-apps/outlinedbutton.png)
[TextButton](https://flet.dev/docs/controls/textbutton)![](https://flet.dev/img/docs/adaptive-apps/textbutton.png)
## Custom adaptive controls[​](https://flet.dev/docs/getting-started/adaptive-apps/#custom-adaptive-controls "Direct link to Custom adaptive controls")
While Flet offers a number of [controls](https://flet.dev/docs/getting-started/adaptive-apps/#material-and-cupertino-controls) that will be adapted to a platform automatically using their [`adaptive`](https://flet.dev/docs/controls#adaptive) property, there will be cases when you need more specific adaptive UI presentation, for example, using different icon, background color, padding etc. depending on the platform.
With Flet, you can create your own reusable custom controls in Python that will inherit from a Flet control and implement specific properties you need. In the example below, we are creating a new `AdaptiveNavigationBarDestination` control that will be displaying different icon on iOS and Android:
```
classAdaptiveNavigationBarDestination(ft.NavigationBarDestination):def__init__(self, ios_icon, android_icon, label):super().__init__()    self._ios_icon = ios_icon    self._android_icon = android_icon    self.label = labeldefbuild(self):# we can check for platform in build method because self.page is known    self.icon =(      self._ios_iconif self.page.platform == ft.PagePlatform.IOSor self.page.platform == ft.PagePlatform.MACOSelse self._android_icon)
```

We will use `AdaptiveNavigationBarDestination` in `NavigationBar`:
```
import flet as ftfrom adaptive_navigation_destination import AdaptiveNavigationBarDestinationdefmain(page):  page.adaptive =True  page.navigation_bar = ft.NavigationBar(    selected_index=2,    destinations=[      AdaptiveNavigationBarDestination(        ios_icon=ft.cupertino_icons.PERSON_3_FILL,        android_icon=ft.Icons.PERSON,        label="Contacts",),      AdaptiveNavigationBarDestination(        ios_icon=ft.cupertino_icons.CHAT_BUBBLE_2,        android_icon=ft.Icons.CHAT,        label="Chats",),      AdaptiveNavigationBarDestination(        ios_icon=ft.cupertino_icons.SETTINGS,        android_icon=ft.Icons.SETTINGS,        label="Settings",),],)  page.update()ft.app(main)
```

Now the NavigationBar and icons within it will look like different on Android and iOS:
### iOS
![](https://flet.dev/img/docs/adaptive-apps/navigation-bar-custom-ios.png)
### Android
![](https://flet.dev/img/docs/adaptive-apps/navigation-bar-custom-android.png)
note
You may utilise [reusable controls approach](https://flet.dev/docs/getting-started/custom-controls) to adapt your app not only depending on the [`platform`](https://flet.dev/docs/controls/page#platform) but also use [`page.web`](https://flet.dev/docs/controls/page#web) property to have different UI depending on wether the app is running in a browser or not, or even combine `platform` and `web` properties to have specific UI for your MACOS or Windows desktop apps.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/getting-started/adaptive-apps.md)
[PreviousCustom controls](https://flet.dev/docs/getting-started/custom-controls)[NextNavigation and routing](https://flet.dev/docs/getting-started/navigation-and-routing)
  * [Material and Cupertino controls](https://flet.dev/docs/getting-started/adaptive-apps/#material-and-cupertino-controls)
  * [Custom adaptive controls](https://flet.dev/docs/getting-started/adaptive-apps/#custom-adaptive-controls)


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
