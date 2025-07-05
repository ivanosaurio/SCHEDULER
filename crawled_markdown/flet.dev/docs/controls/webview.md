[Skip to main content](https://flet.dev/docs/controls/webview/#__docusaurus_skipToContent_fallback)
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
      * [Ads](https://flet.dev/docs/controls/ads)
      * [Canvas](https://flet.dev/docs/controls/canvas)
      * [CircleAvatar](https://flet.dev/docs/controls/circleavatar)
      * [CupertinoActivityIndicator](https://flet.dev/docs/controls/cupertinoactivityindicator)
      * [Icon](https://flet.dev/docs/controls/icon)
      * [Image](https://flet.dev/docs/controls/image)
      * [Map](https://flet.dev/docs/controls/map)
      * [Markdown](https://flet.dev/docs/controls/markdown)
      * [Text](https://flet.dev/docs/controls/text)
      * [ProgressBar](https://flet.dev/docs/controls/progressbar)
      * [ProgressRing](https://flet.dev/docs/controls/progressring)
      * [WebView](https://flet.dev/docs/controls/webview)
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
  * [Controls](https://flet.dev/docs/controls)
  * [Information Displays](https://flet.dev/docs/controls/information-displays)
  * WebView


On this page
# WebView
Easily load web pages while allowing user interaction.
Packaging
To build your Flet app that uses ads control add `flet-webview` to `dependencies` key of the `[project]` section of your `pyproject.toml` file, for example:
```
[project]...dependencies = [ "flet==0.27.6", "flet-webview==0.1.0",]
```

## Examples[​](https://flet.dev/docs/controls/webview/#examples "Direct link to Examples")
A simple implementation that loads the [flet.dev](https://flet.dev) website:
python/controls/information-displays/web-view/web-view-example.py
```
loading...
```

[View on GitHub](https://github.com/flet-dev/examples/blob/main/python/controls/information-displays/web-view/web-view-example.py)
## Properties[​](https://flet.dev/docs/controls/webview/#properties "Direct link to Properties")
### `bgcolor`[​](https://flet.dev/docs/controls/webview/#bgcolor "Direct link to bgcolor")
Set the background [color](https://flet.dev/docs/reference/colors) of the WebView.
### `enable_javascript`[​](https://flet.dev/docs/controls/webview/#enable_javascript "Direct link to enable_javascript")
Enable or disable the JavaScript execution on the page. Note that disabling the JavaScript execution on the page may result to unexpected web page behaviour.
Value is of type `bool`.
### ~~`javascript_enabled`~~[​](https://flet.dev/docs/controls/webview/#javascript_enabled "Direct link to javascript_enabled")
Enable or disable the JavaScript execution on the page. Note that disabling the JavaScript execution on the page may result to unexpected web page behaviour.
Value is of type `bool`.
**Deprecated in v0.25.0 and will be removed in v0.28.0. Use[`enable_javascript`](https://flet.dev/docs/controls/webview/#enable_javascript) instead.**
### `prevent_link`[​](https://flet.dev/docs/controls/webview/#prevent_link "Direct link to prevent_link")
Specify a prefix for links to prevent navigating or downloading.
Value is of type `str`.
### `url`[​](https://flet.dev/docs/controls/webview/#url "Direct link to url")
Start the WebView by loading the `url` value.
Value is of type `str`.
## Methods[​](https://flet.dev/docs/controls/webview/#methods "Direct link to Methods")
### `can_go_back()`[​](https://flet.dev/docs/controls/webview/#can_go_back "Direct link to can_go_back")
Whether there's a back history item. Only for Android, iOS and macOS platforms.
Returns a `bool`.
### `can_go_forward()`[​](https://flet.dev/docs/controls/webview/#can_go_forward "Direct link to can_go_forward")
Whether there's a forward history item. Only for Android, iOS and macOS platforms.
### `clear_cache()`[​](https://flet.dev/docs/controls/webview/#clear_cache "Direct link to clear_cache")
Clears all caches used by the WebView. Only for Android, iOS and macOS platforms.
The following caches are cleared:
  * Browser HTTP Cache
  * [Cache API](https://web.dev/articles/cache-api-quick-guide) caches. Service workers tend to use this cache.
  * Application cache


### `clear_local_storage()`[​](https://flet.dev/docs/controls/webview/#clear_local_storage "Direct link to clear_local_storage")
Clears the local storage used by the WebView. Only for Android, iOS and macOS platforms.
### `disable_zoom()`[​](https://flet.dev/docs/controls/webview/#disable_zoom "Direct link to disable_zoom")
Disable zooming using the on-screen zoom controls and gestures. Only for Android, iOS and macOS platforms.
### `enable_zoom()`[​](https://flet.dev/docs/controls/webview/#enable_zoom "Direct link to enable_zoom")
Enable zooming using the on-screen zoom controls and gestures. Only for Android, iOS and macOS platforms.
### `get_current_url()`[​](https://flet.dev/docs/controls/webview/#get_current_url "Direct link to get_current_url")
Returns the current URL that the WebView is displaying or `None` if no URL was ever loaded. Only for Android, iOS and macOS platforms.
### `get_title()`[​](https://flet.dev/docs/controls/webview/#get_title "Direct link to get_title")
The title of the currently loaded page. Only for Android, iOS and macOS platforms.
### `get_user_agent()`[​](https://flet.dev/docs/controls/webview/#get_user_agent "Direct link to get_user_agent")
Gets the value used for the HTTP `User-Agent:` request header. Only for Android, iOS and macOS platforms.
### `go_back()`[​](https://flet.dev/docs/controls/webview/#go_back "Direct link to go_back")
Go back in the history of the webview, if `can_go_back()` is `True`. Only for Android, iOS and macOS platforms.
### `go_forward()`[​](https://flet.dev/docs/controls/webview/#go_forward "Direct link to go_forward")
Go forward in the history of the webview, if `can_go_forward()` is `True`. Only for Android, iOS and macOS platforms.
### `load_file()`[​](https://flet.dev/docs/controls/webview/#load_file "Direct link to load_file")
Loads the provided local file. Only for Android, iOS and macOS platforms.
It has the following parameters:
  * `absolute_path`: The path to the local file to load.


### `load_html()`[​](https://flet.dev/docs/controls/webview/#load_html "Direct link to load_html")
Loads the provided HTML string. Only for Android, iOS and macOS platforms.
It has the following parameters:
  * `html`: The HTML string to load.
  * `base_url` (optional): Used when resolving relative URLs within the HTML string.


### `load_request()`[​](https://flet.dev/docs/controls/webview/#load_request "Direct link to load_request")
Makes an HTTP request and loads the response in the webview. Only for Android, iOS and macOS platforms.
It has the following parameters:
  * `url`: The URL of the webview to load.
  * `method`: The method of the request. Value is of type `WebviewRequestMethod` and defaults to `WebviewRequestMethod.GET`.


### `reload()`[​](https://flet.dev/docs/controls/webview/#reload "Direct link to reload")
Reload the current URL. Only for Android, iOS and macOS platforms.
### `run_javascript()`[​](https://flet.dev/docs/controls/webview/#run_javascript "Direct link to run_javascript")
Runs the given JavaScript in the context of the current page. Only for Android, iOS and macOS platforms.
It has the following parameters:
  * `value`: The JavaScript code to run.


### `scroll_by()`[​](https://flet.dev/docs/controls/webview/#scroll_by "Direct link to scroll_by")
Scroll by the provided amount of webview pixels. Only for Android, iOS and macOS platforms.
It has the following parameters:
  * `x`: The amount of pixels to scroll by on the x-axis.
  * `y`: The amount of pixels to scroll by on the y-axis.


### `scroll_to()`[​](https://flet.dev/docs/controls/webview/#scroll_to "Direct link to scroll_to")
Scroll to the provided position of webview pixels. Only for Android, iOS and macOS platforms.
It has the following parameters:
  * `x`: The x-coordinate of the scroll position.
  * `y`: The y-coordinate of the scroll position.


## Events[​](https://flet.dev/docs/controls/webview/#events "Direct link to Events")
### `on_console_message`[​](https://flet.dev/docs/controls/webview/#on_console_message "Direct link to on_console_message")
Fires when a console message is logged. Only for Android, iOS and macOS platforms.
Event handler argument is of type [`WebviewConsoleMessageEvent`](https://flet.dev/docs/reference/types/webviewconsolemessageevent).
### `on_javascript_alert_dialog`[​](https://flet.dev/docs/controls/webview/#on_javascript_alert_dialog "Direct link to on_javascript_alert_dialog")
Fires when a JavaScript alert dialog is about to be shown. Only for Android, iOS and macOS platforms.
Event handler argument is of type [`WebviewJavascriptEvent`](https://flet.dev/docs/reference/types/webviewjavascriptevent).
### `on_page_ended`[​](https://flet.dev/docs/controls/webview/#on_page_ended "Direct link to on_page_ended")
Fires when all the webview page loading processes are ended. Only for Android, iOS and macOS platforms.
### `on_page_started`[​](https://flet.dev/docs/controls/webview/#on_page_started "Direct link to on_page_started")
Fires soon as the first loading process of the webview page is started. Only for Android, iOS and macOS platforms.
### `on_progress`[​](https://flet.dev/docs/controls/webview/#on_progress "Direct link to on_progress")
Fires when the progress of the webview page loading is changed. Only for Android, iOS and macOS platforms.
### `on_scroll`[​](https://flet.dev/docs/controls/webview/#on_scroll "Direct link to on_scroll")
Fires when the scroll position changes. Only for Android, iOS and macOS platforms.
Event handler argument is of type [`WebviewScrollEvent`](https://flet.dev/docs/reference/types/webviewscrollevent).
### `on_url_change`[​](https://flet.dev/docs/controls/webview/#on_url_change "Direct link to on_url_change")
Fires when the URL of the webview page is changed. Only for Android, iOS and macOS platforms.
### `on_web_resource_error`[​](https://flet.dev/docs/controls/webview/#on_web_resource_error "Direct link to on_web_resource_error")
Fires when there is error with loading a webview page resource. Only for Android, iOS and macOS platforms.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/controls/webview.md)
[PreviousProgressRing](https://flet.dev/docs/controls/progressring)[NextButtons](https://flet.dev/docs/controls/buttons)
  * [Examples](https://flet.dev/docs/controls/webview/#examples)
  * [Properties](https://flet.dev/docs/controls/webview/#properties)
    * [`bgcolor`](https://flet.dev/docs/controls/webview/#bgcolor)
    * [`enable_javascript`](https://flet.dev/docs/controls/webview/#enable_javascript)
    * [~~`javascript_enabled`~~](https://flet.dev/docs/controls/webview/#javascript_enabled)
    * [`prevent_link`](https://flet.dev/docs/controls/webview/#prevent_link)
    * [`url`](https://flet.dev/docs/controls/webview/#url)
  * [Methods](https://flet.dev/docs/controls/webview/#methods)
    * [`can_go_back()`](https://flet.dev/docs/controls/webview/#can_go_back)
    * [`can_go_forward()`](https://flet.dev/docs/controls/webview/#can_go_forward)
    * [`clear_cache()`](https://flet.dev/docs/controls/webview/#clear_cache)
    * [`clear_local_storage()`](https://flet.dev/docs/controls/webview/#clear_local_storage)
    * [`disable_zoom()`](https://flet.dev/docs/controls/webview/#disable_zoom)
    * [`enable_zoom()`](https://flet.dev/docs/controls/webview/#enable_zoom)
    * [`get_current_url()`](https://flet.dev/docs/controls/webview/#get_current_url)
    * [`get_title()`](https://flet.dev/docs/controls/webview/#get_title)
    * [`get_user_agent()`](https://flet.dev/docs/controls/webview/#get_user_agent)
    * [`go_back()`](https://flet.dev/docs/controls/webview/#go_back)
    * [`go_forward()`](https://flet.dev/docs/controls/webview/#go_forward)
    * [`load_file()`](https://flet.dev/docs/controls/webview/#load_file)
    * [`load_html()`](https://flet.dev/docs/controls/webview/#load_html)
    * [`load_request()`](https://flet.dev/docs/controls/webview/#load_request)
    * [`reload()`](https://flet.dev/docs/controls/webview/#reload)
    * [`run_javascript()`](https://flet.dev/docs/controls/webview/#run_javascript)
    * [`scroll_by()`](https://flet.dev/docs/controls/webview/#scroll_by)
    * [`scroll_to()`](https://flet.dev/docs/controls/webview/#scroll_to)
  * [Events](https://flet.dev/docs/controls/webview/#events)
    * [`on_console_message`](https://flet.dev/docs/controls/webview/#on_console_message)
    * [`on_javascript_alert_dialog`](https://flet.dev/docs/controls/webview/#on_javascript_alert_dialog)
    * [`on_page_ended`](https://flet.dev/docs/controls/webview/#on_page_ended)
    * [`on_page_started`](https://flet.dev/docs/controls/webview/#on_page_started)
    * [`on_progress`](https://flet.dev/docs/controls/webview/#on_progress)
    * [`on_scroll`](https://flet.dev/docs/controls/webview/#on_scroll)
    * [`on_url_change`](https://flet.dev/docs/controls/webview/#on_url_change)
    * [`on_web_resource_error`](https://flet.dev/docs/controls/webview/#on_web_resource_error)


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
