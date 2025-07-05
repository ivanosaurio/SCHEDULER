[Skip to main content](https://flet.dev/docs/controls/page/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/controls/page/)
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
  * [Cookbook](https://flet.dev/docs/controls/page/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Controls](https://flet.dev/docs/controls)
  * [Layout](https://flet.dev/docs/controls/layout)
  * Page


On this page
# Page
Page is a container for [`View`](https://flet.dev/docs/controls/view) controls.
A page instance and the root view are automatically created when a new user session started.
## Properties[​](https://flet.dev/docs/controls/page/#properties "Direct link to Properties")
### `auto_scroll`[​](https://flet.dev/docs/controls/page/#auto_scroll "Direct link to auto_scroll")
`True` if scrollbar should automatically move its position to the end when children updated. Must be `False` for `scroll_to()` method to work.
### `appbar`[​](https://flet.dev/docs/controls/page/#appbar "Direct link to appbar")
An [`AppBar`](https://flet.dev/docs/controls/appbar) control to display at the top of the Page.
### `bgcolor`[​](https://flet.dev/docs/controls/page/#bgcolor "Direct link to bgcolor")
Background color of the Page.
A color value could be a hex value in `#ARGB` format (e.g. `#FFCC0000`), `#RGB` format (e.g. `#CC0000`) or a named color from `flet.colors` module.
### `bottom_appbar`[​](https://flet.dev/docs/controls/page/#bottom_appbar "Direct link to bottom_appbar")
[`BottomAppBar`](https://flet.dev/docs/controls/bottomappbar) control to display at the bottom of the Page. If both [`bottom_appbar`](https://flet.dev/docs/controls/page/#bottom_appbar) and [`navigation_bar`](https://flet.dev/docs/controls/page/#navigation_bar) properties are provided, `NavigationBar` will be displayed.
### `browser_context_menu`[​](https://flet.dev/docs/controls/page/#browser_context_menu "Direct link to browser_context_menu")
Used to enable or disable the context menu that appears when the user right-clicks on the web page.
Value is of type [`BrowserContextMenu`](https://flet.dev/docs/reference/types/browsercontextmenu).
🌎 Web only.
### `client_ip`[​](https://flet.dev/docs/controls/page/#client_ip "Direct link to client_ip")
IP address of the connected user.
🌎 Web only.
### `client_user_agent`[​](https://flet.dev/docs/controls/page/#client_user_agent "Direct link to client_user_agent")
Browser details of the connected user.
🌎 Web only.
### `controls`[​](https://flet.dev/docs/controls/page/#controls "Direct link to controls")
A list of Controls to display on the Page.
For example, to add a new control to a page:
```
page.controls.append(ft.Text("Hello!"))page.update()
```

or to get the same result as above using [`page.add()`](https://flet.dev/docs/controls/page/#addcontrols) method
To remove the top most control on the page:
```
page.controls.pop()page.update()
```

### `dark_theme`[​](https://flet.dev/docs/controls/page/#dark_theme "Direct link to dark_theme")
Customizes the theme of the application when in dark theme mode.
Value is an instance of the `Theme()` class - more information in the [theming](https://flet.dev/docs/cookbook/theming) guide.
### `debug`[​](https://flet.dev/docs/controls/page/#debug "Direct link to debug")
`True` if Flutter client of Flet app is running in debug mode.
### `decoration`[​](https://flet.dev/docs/controls/page/#decoration "Direct link to decoration")
The background decoration.
Value is of type [`BoxDecoration`](https://flet.dev/docs/reference/types/boxdecoration).
### `design`[​](https://flet.dev/docs/controls/page/#design "Direct link to design")
Reserved for future use.
### `drawer`[​](https://flet.dev/docs/controls/page/#drawer "Direct link to drawer")
A [`NavigationDrawer`](https://flet.dev/docs/controls/navigationdrawer) control to display as a panel sliding from the start edge of the page.
### `end_drawer`[​](https://flet.dev/docs/controls/page/#end_drawer "Direct link to end_drawer")
A [`NavigationDrawer`](https://flet.dev/docs/controls/navigationdrawer) control to display as a panel sliding from the end edge of the page.
### `floating_action_button`[​](https://flet.dev/docs/controls/page/#floating_action_button "Direct link to floating_action_button")
A [`FloatingActionButton`](https://flet.dev/docs/controls/floatingactionbutton) control to display on top of Page content.
### `floating_action_button_location`[​](https://flet.dev/docs/controls/page/#floating_action_button_location "Direct link to floating_action_button_location")
Defines a position for the `FloatingActionButton`.
Value is of type [`FloatingActionButtonLocation`](https://flet.dev/docs/reference/types/floatingactionbuttonlocation) enum. Default is `FloatingActionButtonLocation.END_FLOAT`.
### `fonts`[​](https://flet.dev/docs/controls/page/#fonts "Direct link to fonts")
Defines the custom fonts to be used in the application.
Value is a dictionary, in which the keys represent the font family name used for reference and the values
  * **Key** : The font family name used for reference.
  * **Value** : The font source, either an absolute URL or a relative path to a local asset. The following font file formats are supported `.ttc`, `.ttf` and `.otf`.


Usage example [here](https://flet.dev/docs/cookbook/fonts#importing-fonts).
### `height`[​](https://flet.dev/docs/controls/page/#height "Direct link to height")
A height of a web page or content area of a native OS window containing Flet app. This property is read-only. It's usually being used inside [`page.on_resized`](https://flet.dev/docs/controls/page/#on_resized) handler.
### `horizontal_alignment`[​](https://flet.dev/docs/controls/page/#horizontal_alignment "Direct link to horizontal_alignment")
How the child Controls should be placed horizontally.
Property value is [`CrossAxisAlignment`](https://flet.dev/docs/reference/types/crossaxisalignment) enum. Default is `START`.
### `locale_configuration`[​](https://flet.dev/docs/controls/page/#locale_configuration "Direct link to locale_configuration")
A locale configuration for the app.
Value is of type [`LocaleConfiguration`](https://flet.dev/docs/reference/types/localeconfiguration).
### `media`[​](https://flet.dev/docs/controls/page/#media "Direct link to media")
Provides details about app media (screen, window). See [MediaQueryData](https://api.flutter.dev/flutter/widgets/MediaQueryData-class.html) in Flutter docs for more info.
Value is of type [`PageMediaData`](https://flet.dev/docs/reference/types/pagemediadata).
note
In most cases you should be fine by wrapping your content into [`SafeArea`](https://flet.dev/docs/controls/safearea) control.
### `name`[​](https://flet.dev/docs/controls/page/#name "Direct link to name")
Page name as specified in `ft.app()` call. Page name is set when Flet app is running as web app. This is a portion of the URL after host name.
### `navigation_bar`[​](https://flet.dev/docs/controls/page/#navigation_bar "Direct link to navigation_bar")
[`NavigationBar`](https://flet.dev/docs/controls/navigationbar) control to display at the bottom of the page. If both [`bottom_appbar`](https://flet.dev/docs/controls/page/#bottom_appbar) and [`navigation_bar`](https://flet.dev/docs/controls/page/#navigation_bar) properties are provided, `NavigationBar` will be displayed.
### `on_scroll_interval`[​](https://flet.dev/docs/controls/page/#on_scroll_interval "Direct link to on_scroll_interval")
Throttling in milliseconds for `on_scroll` event.
Defaults to `10`.
### `overlay`[​](https://flet.dev/docs/controls/page/#overlay "Direct link to overlay")
A list of `Control`s displayed as a stack on top of main page contents.
### `padding`[​](https://flet.dev/docs/controls/page/#padding "Direct link to padding")
A space between page contents and its edges. Default value is 10 pixels from each side. To set zero padding:
```
page.padding =0page.update()
```

Value is of type [`Padding`](https://flet.dev/docs/reference/types/padding).
### `platform`[​](https://flet.dev/docs/controls/page/#platform "Direct link to platform")
Operating system the application is running on.
Value is of type [`PagePlatform`](https://flet.dev/docs/reference/types/pageplatform).
This property can be used to create adaptive UI with different controls depending on the operating system:
```
defmain(page: ft.Page):if page.platform == ft.PagePlatform.MACOS:    page.add(ft.CupertinoDialogAction("Cupertino Button"))else:    page.add(ft.TextButton("Material Button"))
```

You can also set this property for testing purposes:
python/controls/layout/page/set-platform.py
```
import flet as ftdefmain(page):defset_android(e):    page.platform = ft.PagePlatform.ANDROID    page.update()print("New platform:", page.platform)defset_ios(e):    page.platform ="ios"    page.update()print("New platform:", page.platform)  page.add(    ft.Switch(label="Switch A", adaptive=True),    ft.ElevatedButton("Set Android", on_click=set_android),    ft.ElevatedButton("Set iOS", on_click=set_ios),)print("Default platform:", page.platform)ft.app(main)
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/layout/page/set-platform.py)
### `platform_brightness`[​](https://flet.dev/docs/controls/page/#platform_brightness "Direct link to platform_brightness")
The current brightness mode of the host platform.
Value is read-only and of type [`Brightness`](https://flet.dev/docs/reference/types/brightness).
### `pubsub`[​](https://flet.dev/docs/controls/page/#pubsub "Direct link to pubsub")
A simple PubSub implementation for passing messages between app sessions.
#### `subscribe(handler)`[​](https://flet.dev/docs/controls/page/#subscribehandler "Direct link to subscribehandler")
Subscribe current app session for broadcast (no topic) messages. `handler` is a function or method with a single `message` argument, for example:
```
defmain(page: ft.Page):defon_broadcast_message(message):print(message)  page.pubsub.subscribe(on_broadcast_message)
```

#### `subscribe_topic(topic, handler)`[​](https://flet.dev/docs/controls/page/#subscribe_topictopic-handler "Direct link to subscribe_topictopic-handler")
Subscribe current app session to a specific topic. `handler` is a function or method with two arguments: `topic` and `message`, for example:
```
defmain(page: ft.Page):defon_message(topic, message):print(topic, message)  page.pubsub.subscribe_topic("general", on_message)
```

#### `send_all(message)`[​](https://flet.dev/docs/controls/page/#send_allmessage "Direct link to send_allmessage")
Broadcast message to all subscribers. `message` could be anything: a simple literal or a class instance, for example:
```
@dataclassclassMessage:  user:str  text:strdefmain(page: ft.Page):defon_broadcast_message(message):    page.add(ft.Text(f"{message.user}: {message.text}"))  page.pubsub.subscribe(on_broadcast_message)defon_send_click(e):    page.pubsub.send_all(Message("John","Hello, all!"))  page.add(ft.ElevatedButton(text="Send message", on_click=on_send_click))
```

#### `send_all_on_topic(topic, message)`[​](https://flet.dev/docs/controls/page/#send_all_on_topictopic-message "Direct link to send_all_on_topictopic-message")
Send message to all subscribers on specific topic.
#### `send_others(message)`[​](https://flet.dev/docs/controls/page/#send_othersmessage "Direct link to send_othersmessage")
Broadcast message to all subscribers except sender.
#### `send_others_on_topic(topic, message)`[​](https://flet.dev/docs/controls/page/#send_others_on_topictopic-message "Direct link to send_others_on_topictopic-message")
Send message to all subscribers on specific topic except sender.
#### `unsubscribe()`[​](https://flet.dev/docs/controls/page/#unsubscribe "Direct link to unsubscribe")
Unsubscribe current app session from broadcast messages, for example:
```
@dataclassclassMessage:  user:str  text:strdefmain(page: ft.Page):defon_leave_click(e):    page.pubsub.unsubscribe()  page.add(ft.ElevatedButton(text="Leave chat", on_click=on_leave_click))
```

#### `unsubscribe_topic(topic)`[​](https://flet.dev/docs/controls/page/#unsubscribe_topictopic "Direct link to unsubscribe_topictopic")
Unsubscribe current app session from specific topic.
#### `unsubscribe_all()`[​](https://flet.dev/docs/controls/page/#unsubscribe_all "Direct link to unsubscribe_all")
Unsubscribe current app session from broadcast messages and all topics, for example:
```
defmain(page: ft.Page):defclient_exited(e):    page.pubsub.unsubscribe_all()  page.on_close = client_exited
```

### `pwa`[​](https://flet.dev/docs/controls/page/#pwa "Direct link to pwa")
`True` if the application is running as Progressive Web App (PWA).
Value is read-only.
### `query`[​](https://flet.dev/docs/controls/page/#query "Direct link to query")
A part of app URL after `?`. The value is an instance of `QueryString` with helper methods for fetching query parameters.
### `route`[​](https://flet.dev/docs/controls/page/#route "Direct link to route")
Get or sets page's navigation route. See [Navigation and routing](https://flet.dev/docs/getting-started/navigation-and-routing) section for more information and examples.
### `rtl`[​](https://flet.dev/docs/controls/page/#rtl "Direct link to rtl")
`True` to set text direction to right-to-left.
Defaults to `False`.
### `scroll`[​](https://flet.dev/docs/controls/page/#scroll "Direct link to scroll")
Enables a vertical scrolling for the Page to prevent its content overflow.
Value is of type [`ScrollMode`](https://flet.dev/docs/reference/types/scrollmode).
### `session`[​](https://flet.dev/docs/controls/page/#session "Direct link to session")
A simple key-value storage for session data.
### `session_id`[​](https://flet.dev/docs/controls/page/#session_id "Direct link to session_id")
A unique ID of user's session. This property is read-only.
### `spacing`[​](https://flet.dev/docs/controls/page/#spacing "Direct link to spacing")
Vertical spacing between controls on the Page. Default value is 10 virtual pixels. Spacing is applied only when `alignment` is set to `start`, `end` or `center`.
### `show_semantics_debugger`[​](https://flet.dev/docs/controls/page/#show_semantics_debugger "Direct link to show_semantics_debugger")
`True` turns on an overlay that shows the accessibility information reported by the framework.
### `theme`[​](https://flet.dev/docs/controls/page/#theme "Direct link to theme")
Customizes the theme of the application when in light theme mode. Currently, a theme can only be automatically generated from a "seed" color. For example, to generate light theme from a green color.
Value is an instance of the `Theme()` class - more information in the [theming](https://flet.dev/docs/cookbook/theming) guide.
### `theme_mode`[​](https://flet.dev/docs/controls/page/#theme_mode "Direct link to theme_mode")
The page's theme mode.
Value is of type [`ThemeMode`](https://flet.dev/docs/reference/types/thememode) and defaults to `ThemeMode.SYSTEM`.
### `title`[​](https://flet.dev/docs/controls/page/#title "Direct link to title")
A title of browser or native OS window, for example:
```
page.title ="My awesome app"page.update()
```

### `url`[​](https://flet.dev/docs/controls/page/#url "Direct link to url")
The complete web app's URL.
### `vertical_alignment`[​](https://flet.dev/docs/controls/page/#vertical_alignment "Direct link to vertical_alignment")
How the child Controls should be placed vertically.
Value is of type [`MainAxisAlignment`](https://flet.dev/docs/reference/types/mainaxisalignment) and defaults to `MainAxisAlignment.START`.
### `views`[​](https://flet.dev/docs/controls/page/#views "Direct link to views")
A list of [`View`](https://flet.dev/docs/controls/view) controls to build navigation history.
The last view in the list is the one displayed on a page.
The first view is a "root" view which cannot be popped.
### `web`[​](https://flet.dev/docs/controls/page/#web "Direct link to web")
`True` if the application is running in the web browser.
### `width`[​](https://flet.dev/docs/controls/page/#width "Direct link to width")
A width of a web page or content area of a native OS window containing Flet app. This property is read-only. It's usually being used inside [`page.on_resized`](https://flet.dev/docs/controls/page/#on_resized) handler.
### `window`[​](https://flet.dev/docs/controls/page/#window "Direct link to window")
A class with properties/methods/events to control app's native OS window.
Value is of type [`Window`](https://flet.dev/docs/reference/types/window).
## Methods[​](https://flet.dev/docs/controls/page/#methods "Direct link to Methods")
### `add(*controls)`[​](https://flet.dev/docs/controls/page/#addcontrols "Direct link to addcontrols")
Adds controls to page
```
page.add(ft.Text("Hello!"), ft.FilledButton("Button"))
```

### `can_launch_url(url)`[​](https://flet.dev/docs/controls/page/#can_launch_urlurl "Direct link to can_launch_urlurl")
Checks whether the specified URL can be handled by some app installed on the device.
Returns `True` if it is possible to verify that there is a handler available. A `False` return value can indicate either that there is no handler available, or that the application does not have permission to check. For example:
  * On recent versions of Android and iOS, this will always return `False` unless the application has been configuration to allow querying the system for launch support.
  * On web, this will always return `False` except for a few specific schemes that are always assumed to be supported (such as http(s)), as web pages are never allowed to query installed applications.


### `close(control)`[​](https://flet.dev/docs/controls/page/#closecontrol "Direct link to closecontrol")
Closes the provided control.
It sets the `control.open=False` and calls `update()`.
### `close_in_app_web_view()`[​](https://flet.dev/docs/controls/page/#close_in_app_web_view "Direct link to close_in_app_web_view")
Closes in-app web view opened with `launch_url()`.
📱 Mobile only.
### `error(message)`[​](https://flet.dev/docs/controls/page/#errormessage "Direct link to errormessage")
### `fetch_page_details()`[​](https://flet.dev/docs/controls/page/#fetch_page_details "Direct link to fetch_page_details")
### `get_clipboard()`[​](https://flet.dev/docs/controls/page/#get_clipboard "Direct link to get_clipboard")
Get the last text value saved to a clipboard on a client side.
### `get_control(id)`[​](https://flet.dev/docs/controls/page/#get_controlid "Direct link to get_controlid")
Get a control by its `id`.
Example:
```
import flet as ftdefmain(page: ft.Page):  x = ft.IconButton(ft.Icons.ADD)  page.add(x)print(type(page.get_control(x.uid)))ft.app(main)
```

### `get_upload_url(file_name, expires)`[​](https://flet.dev/docs/controls/page/#get_upload_urlfile_name-expires "Direct link to get_upload_urlfile_name-expires")
Generates presigned upload URL for built-in upload storage:
  * `file_name` - a relative to upload storage path.
  * `expires` - a URL time-to-live in seconds.


For example:
```
upload_url = page.get_upload_url("dir/filename.ext",60)
```

To enable built-in upload storage provide `upload_dir` argument to `flet.app()` call:
```
ft.app(main, upload_dir="uploads")
```

### `go(route)`[​](https://flet.dev/docs/controls/page/#goroute "Direct link to goroute")
A helper method that updates [`page.route`](https://flet.dev/docs/controls/page/#route), calls [`page.on_route_change`](https://flet.dev/docs/controls/page/#on_route_change) event handler to update views and finally calls `page.update()`.
### `insert(at, *controls)`[​](https://flet.dev/docs/controls/page/#insertat-controls "Direct link to insertat-controls")
Inserts controls at specific index of `page.controls` list.
### `launch_url(url)`[​](https://flet.dev/docs/controls/page/#launch_urlurl "Direct link to launch_urlurl")
Opens `url` in a new browser window.
Optional method arguments:
  * `web_window_name` - window tab/name to open URL in: [`UrlTarget.SELF`](https://flet.dev/docs/reference/types/urltarget#self) - the same browser tab, [`UrlTarget.BLANK`](https://flet.dev/docs/reference/types/urltarget#blank) - a new browser tab (or in external application on mobile device) or `<your name>` - a named tab.
  * `web_popup_window` - set to `True` to display a URL in a browser popup window. Defaults to `False`.
  * `window_width` - optional, popup window width.
  * `window_height` - optional, popup window height.


### `login(provider, fetch_user, fetch_groups, scope, saved_token, on_open_authorization_url, complete_page_html, redirect_to_page, authorization)`[​](https://flet.dev/docs/controls/page/#loginprovider-fetch_user-fetch_groups-scope-saved_token-on_open_authorization_url-complete_page_html-redirect_to_page-authorization "Direct link to loginprovider-fetch_user-fetch_groups-scope-saved_token-on_open_authorization_url-complete_page_html-redirect_to_page-authorization")
Starts OAuth flow. See [Authentication](https://flet.dev/docs/cookbook/authentication) guide for more information and examples.
### `logout()`[​](https://flet.dev/docs/controls/page/#logout "Direct link to logout")
Clears current authentication context. See [Authentication](https://flet.dev/docs/cookbook/authentication#signing-out) guide for more information and examples.
### `open(control)`[​](https://flet.dev/docs/controls/page/#opencontrol "Direct link to opencontrol")
Opens the provided control.
Adds this control to the [`page.overlay`](https://flet.dev/docs/controls/page/#overlay), sets the `control.open=True`, then calls `update()`.
### `remove(*controls)`[​](https://flet.dev/docs/controls/page/#removecontrols "Direct link to removecontrols")
Removes specific controls from `page.controls` list.
### `remove_at(index)`[​](https://flet.dev/docs/controls/page/#remove_atindex "Direct link to remove_atindex")
Remove controls from `page.controls` list at specific index.
### `run_task(handler, *args, **kwargs)`[​](https://flet.dev/docs/controls/page/#run_taskhandler-args-kwargs "Direct link to run_taskhandler-args-kwargs")
Run `handler` coroutine as a new Task in the event loop associated with the current page.
### `run_thread(handler, *args)`[​](https://flet.dev/docs/controls/page/#run_threadhandler-args "Direct link to run_threadhandler-args")
Run `handler` function as a new Thread in the executor associated with the current page.
### `scroll_to(offset, delta, key, duration, curve)`[​](https://flet.dev/docs/controls/page/#scroll_tooffset-delta-key-duration-curve "Direct link to scroll_tooffset-delta-key-duration-curve")
Moves scroll position to either absolute `offset`, relative `delta` or jump to the control with specified `key`.
See [`Column.scroll_to()`](https://flet.dev/docs/controls/column#scroll_tooffset-delta-key-duration-curve) for method details and examples.
### `set_clipboard(data)`[​](https://flet.dev/docs/controls/page/#set_clipboarddata "Direct link to set_clipboarddata")
Set clipboard data on a client side (user's web browser or a desktop), for example:
```
page.set_clipboard("This value comes from Flet app")
```

## Events[​](https://flet.dev/docs/controls/page/#events "Direct link to Events")
### `on_app_lifecycle_state_change`[​](https://flet.dev/docs/controls/page/#on_app_lifecycle_state_change "Direct link to on_app_lifecycle_state_change")
Triggers when app lifecycle state changes.
You can use this event to know when the app becomes active (brought to the front) to update UI with the latest information. This event works on iOS, Android, all desktop platforms and web.
Event handler argument is of type [`AppLifecycleStateChangeEvent`](https://flet.dev/docs/reference/types/applifecyclestatechangeevent).
### `on_close`[​](https://flet.dev/docs/controls/page/#on_close "Direct link to on_close")
Fires when a session has expired after configured amount of time (60 minutes by default).
### `on_connect`[​](https://flet.dev/docs/controls/page/#on_connect "Direct link to on_connect")
Fires when a web user (re-)connects to a page session. It is not triggered when an app page is first opened, but is triggered when the page is refreshed, or Flet web client has re-connected after computer was unlocked. This event could be used to detect when a web user becomes "online".
### `on_disconnect`[​](https://flet.dev/docs/controls/page/#on_disconnect "Direct link to on_disconnect")
Fires when a web user disconnects from a page session, i.e. closes browser tab/window.
### `on_error`[​](https://flet.dev/docs/controls/page/#on_error "Direct link to on_error")
Fires when unhandled exception occurs.
### `on_keyboard_event`[​](https://flet.dev/docs/controls/page/#on_keyboard_event "Direct link to on_keyboard_event")
Fires when a keyboard key is pressed.
Event handler argument is of type [`KeyboardEvent`](https://flet.dev/docs/reference/types/keyboardevent).
### `on_login`[​](https://flet.dev/docs/controls/page/#on_login "Direct link to on_login")
Fires upon successful or failed OAuth authorization flow.
See [Authentication](https://flet.dev/docs/cookbook/authentication#checking-authentication-results) guide for more information and examples.
### `on_logout`[​](https://flet.dev/docs/controls/page/#on_logout "Direct link to on_logout")
Fires after `page.logout()` call.
### `on_media_change`[​](https://flet.dev/docs/controls/page/#on_media_change "Direct link to on_media_change")
Fires when `page.media` has changed.
Event handler argument is of type [`PageMediaData`](https://flet.dev/docs/reference/types/pagemediadata).
### `on_platform_brigthness_change`[​](https://flet.dev/docs/controls/page/#on_platform_brigthness_change "Direct link to on_platform_brigthness_change")
Fires when brightness of app host platform has changed.
### `on_resized`[​](https://flet.dev/docs/controls/page/#on_resized "Direct link to on_resized")
Fires when a user resizes a browser or native OS window containing Flet app, for example:
```
defpage_resized(e):print("New page size:", page.window.width, page.window_height)page.on_resized = page_resized
```

Event handler argument is of type [`WindowResizeEvent`](https://flet.dev/docs/reference/types/windowresizeevent).
### `on_route_change`[​](https://flet.dev/docs/controls/page/#on_route_change "Direct link to on_route_change")
Fires when page route changes either programmatically, by editing application URL or using browser Back/Forward buttons.
Event handler argument is of type [`RouteChangeEvent`](https://flet.dev/docs/reference/types/routechangeevent).
### `on_scroll`[​](https://flet.dev/docs/controls/page/#on_scroll "Direct link to on_scroll")
Fires when page's scroll position is changed by a user.
Event handler argument is of type [`OnScrollEvent`](https://flet.dev/docs/reference/types/onscrollevent).
### `on_view_pop`[​](https://flet.dev/docs/controls/page/#on_view_pop "Direct link to on_view_pop")
Fires when the user clicks automatic "Back" button in [`AppBar`](https://flet.dev/docs/controls/appbar) control.
Event handler argument is of type [`ViewPopEvent`](https://flet.dev/docs/reference/types/viewpopevent).
## Magic methods[​](https://flet.dev/docs/controls/page/#magic-methods "Direct link to Magic methods")
### `__contains__(control)`[​](https://flet.dev/docs/controls/page/#__contains__control "Direct link to __contains__control")
Checks if a control is present on the page, for example:
```
import flet as ftdefmain(page: ft.Page):  hello = ft.Text("Hello, World!")  page.add(hello)print(hello in page)# Trueft.app(main)
```

ß
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/page.md)
[PreviousListView](https://flet.dev/docs/controls/listview)[NextPagelet](https://flet.dev/docs/controls/pagelet)
  * [Properties](https://flet.dev/docs/controls/page/#properties)
    * [`auto_scroll`](https://flet.dev/docs/controls/page/#auto_scroll)
    * [`appbar`](https://flet.dev/docs/controls/page/#appbar)
    * [`bgcolor`](https://flet.dev/docs/controls/page/#bgcolor)
    * [`bottom_appbar`](https://flet.dev/docs/controls/page/#bottom_appbar)
    * [`browser_context_menu`](https://flet.dev/docs/controls/page/#browser_context_menu)
    * [`client_ip`](https://flet.dev/docs/controls/page/#client_ip)
    * [`client_user_agent`](https://flet.dev/docs/controls/page/#client_user_agent)
    * [`controls`](https://flet.dev/docs/controls/page/#controls)
    * [`dark_theme`](https://flet.dev/docs/controls/page/#dark_theme)
    * [`debug`](https://flet.dev/docs/controls/page/#debug)
    * [`decoration`](https://flet.dev/docs/controls/page/#decoration)
    * [`design`](https://flet.dev/docs/controls/page/#design)
    * [`drawer`](https://flet.dev/docs/controls/page/#drawer)
    * [`end_drawer`](https://flet.dev/docs/controls/page/#end_drawer)
    * [`floating_action_button`](https://flet.dev/docs/controls/page/#floating_action_button)
    * [`floating_action_button_location`](https://flet.dev/docs/controls/page/#floating_action_button_location)
    * [`fonts`](https://flet.dev/docs/controls/page/#fonts)
    * [`height`](https://flet.dev/docs/controls/page/#height)
    * [`horizontal_alignment`](https://flet.dev/docs/controls/page/#horizontal_alignment)
    * [`locale_configuration`](https://flet.dev/docs/controls/page/#locale_configuration)
    * [`media`](https://flet.dev/docs/controls/page/#media)
    * [`name`](https://flet.dev/docs/controls/page/#name)
    * [`navigation_bar`](https://flet.dev/docs/controls/page/#navigation_bar)
    * [`on_scroll_interval`](https://flet.dev/docs/controls/page/#on_scroll_interval)
    * [`overlay`](https://flet.dev/docs/controls/page/#overlay)
    * [`padding`](https://flet.dev/docs/controls/page/#padding)
    * [`platform`](https://flet.dev/docs/controls/page/#platform)
    * [`platform_brightness`](https://flet.dev/docs/controls/page/#platform_brightness)
    * [`pubsub`](https://flet.dev/docs/controls/page/#pubsub)
    * [`pwa`](https://flet.dev/docs/controls/page/#pwa)
    * [`query`](https://flet.dev/docs/controls/page/#query)
    * [`route`](https://flet.dev/docs/controls/page/#route)
    * [`rtl`](https://flet.dev/docs/controls/page/#rtl)
    * [`scroll`](https://flet.dev/docs/controls/page/#scroll)
    * [`session`](https://flet.dev/docs/controls/page/#session)
    * [`session_id`](https://flet.dev/docs/controls/page/#session_id)
    * [`spacing`](https://flet.dev/docs/controls/page/#spacing)
    * [`show_semantics_debugger`](https://flet.dev/docs/controls/page/#show_semantics_debugger)
    * [`theme`](https://flet.dev/docs/controls/page/#theme)
    * [`theme_mode`](https://flet.dev/docs/controls/page/#theme_mode)
    * [`title`](https://flet.dev/docs/controls/page/#title)
    * [`url`](https://flet.dev/docs/controls/page/#url)
    * [`vertical_alignment`](https://flet.dev/docs/controls/page/#vertical_alignment)
    * [`views`](https://flet.dev/docs/controls/page/#views)
    * [`web`](https://flet.dev/docs/controls/page/#web)
    * [`width`](https://flet.dev/docs/controls/page/#width)
    * [`window`](https://flet.dev/docs/controls/page/#window)
  * [Methods](https://flet.dev/docs/controls/page/#methods)
    * [`add(*controls)`](https://flet.dev/docs/controls/page/#addcontrols)
    * [`can_launch_url(url)`](https://flet.dev/docs/controls/page/#can_launch_urlurl)
    * [`close(control)`](https://flet.dev/docs/controls/page/#closecontrol)
    * [`close_in_app_web_view()`](https://flet.dev/docs/controls/page/#close_in_app_web_view)
    * [`error(message)`](https://flet.dev/docs/controls/page/#errormessage)
    * [`fetch_page_details()`](https://flet.dev/docs/controls/page/#fetch_page_details)
    * [`get_clipboard()`](https://flet.dev/docs/controls/page/#get_clipboard)
    * [`get_control(id)`](https://flet.dev/docs/controls/page/#get_controlid)
    * [`get_upload_url(file_name, expires)`](https://flet.dev/docs/controls/page/#get_upload_urlfile_name-expires)
    * [`go(route)`](https://flet.dev/docs/controls/page/#goroute)
    * [`insert(at, *controls)`](https://flet.dev/docs/controls/page/#insertat-controls)
    * [`launch_url(url)`](https://flet.dev/docs/controls/page/#launch_urlurl)
    * [`login(provider, fetch_user, fetch_groups, scope, saved_token, on_open_authorization_url, complete_page_html, redirect_to_page, authorization)`](https://flet.dev/docs/controls/page/#loginprovider-fetch_user-fetch_groups-scope-saved_token-on_open_authorization_url-complete_page_html-redirect_to_page-authorization)
    * [`logout()`](https://flet.dev/docs/controls/page/#logout)
    * [`open(control)`](https://flet.dev/docs/controls/page/#opencontrol)
    * [`remove(*controls)`](https://flet.dev/docs/controls/page/#removecontrols)
    * [`remove_at(index)`](https://flet.dev/docs/controls/page/#remove_atindex)
    * [`run_task(handler, *args, **kwargs)`](https://flet.dev/docs/controls/page/#run_taskhandler-args-kwargs)
    * [`run_thread(handler, *args)`](https://flet.dev/docs/controls/page/#run_threadhandler-args)
    * [`scroll_to(offset, delta, key, duration, curve)`](https://flet.dev/docs/controls/page/#scroll_tooffset-delta-key-duration-curve)
    * [`set_clipboard(data)`](https://flet.dev/docs/controls/page/#set_clipboarddata)
  * [Events](https://flet.dev/docs/controls/page/#events)
    * [`on_app_lifecycle_state_change`](https://flet.dev/docs/controls/page/#on_app_lifecycle_state_change)
    * [`on_close`](https://flet.dev/docs/controls/page/#on_close)
    * [`on_connect`](https://flet.dev/docs/controls/page/#on_connect)
    * [`on_disconnect`](https://flet.dev/docs/controls/page/#on_disconnect)
    * [`on_error`](https://flet.dev/docs/controls/page/#on_error)
    * [`on_keyboard_event`](https://flet.dev/docs/controls/page/#on_keyboard_event)
    * [`on_login`](https://flet.dev/docs/controls/page/#on_login)
    * [`on_logout`](https://flet.dev/docs/controls/page/#on_logout)
    * [`on_media_change`](https://flet.dev/docs/controls/page/#on_media_change)
    * [`on_platform_brigthness_change`](https://flet.dev/docs/controls/page/#on_platform_brigthness_change)
    * [`on_resized`](https://flet.dev/docs/controls/page/#on_resized)
    * [`on_route_change`](https://flet.dev/docs/controls/page/#on_route_change)
    * [`on_scroll`](https://flet.dev/docs/controls/page/#on_scroll)
    * [`on_view_pop`](https://flet.dev/docs/controls/page/#on_view_pop)
  * [Magic methods](https://flet.dev/docs/controls/page/#magic-methods)
    * [`__contains__(control)`](https://flet.dev/docs/controls/page/#__contains__control)


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
