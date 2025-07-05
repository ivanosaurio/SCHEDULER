[Skip to main content](https://flet.dev/blog/flet-fastapi-and-async-api-improvements/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
All posts
### 2025
  * [Introducing Flet 1.0 Alpha](https://flet.dev/blog/introducing-flet-1-0-alpha)
  * [Tap into native Android and iOS APIs with Pyjnius and Pyobjus](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus)
  * [Flet v0.27.0 Release Announcement](https://flet.dev/blog/flet-v-0-27-release-announcement)
  * [Flet v0.26.0 Release Announcement](https://flet.dev/blog/flet-v-0-26-release-announcement)


### 2024
  * [Flet v0.25.0 Release Announcement](https://flet.dev/blog/flet-v-0-25-release-announcement)
  * [pyproject.toml support for flet build command](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command)
  * [Flet new packaging pre-release](https://flet.dev/blog/flet-new-packaging-pre-release)
  * [Flet v0.24.0 Release Announcement](https://flet.dev/blog/flet-v-0-24-release-announcement)
  * [Flet v0.23.0 Release Announcement](https://flet.dev/blog/flet-v-0-23-release-announcement)
  * [Flet at PyCon US 2024](https://flet.dev/blog/flet-at-pycon-us-2024)
  * [Flet packaging update](https://flet.dev/blog/flet-packaging-update)
  * [Controls and theming enhancements](https://flet.dev/blog/controls-and-theming-enhancements)
  * [Flet FastAPI and async API improvements](https://flet.dev/blog/flet-fastapi-and-async-api-improvements)
  * [Flet adaptive UI and custom controls release](https://flet.dev/blog/flet-adaptive-and-custom-controls)


### 2023
  * [Packaging apps for distribution](https://flet.dev/blog/packaging-apps-for-distribution)
  * [Flet for FastAPI](https://flet.dev/blog/flet-for-fastapi)
  * [Flet for Android](https://flet.dev/blog/flet-for-android)
  * [Flet for iOS](https://flet.dev/blog/flet-for-ios)
  * [Scrolling controls and Theming](https://flet.dev/blog/scrolling-controls-and-theming)
  * [Canvas](https://flet.dev/blog/canvas)
  * [Flet Charts](https://flet.dev/blog/flet-charts)
  * [Standalone Flet web apps with Pyodide](https://flet.dev/blog/standalone-flet-web-apps-with-pyodide)
  * [Packaging desktop apps with a custom icon](https://flet.dev/blog/packaging-desktop-apps-with-custom-icon)


### 2022
  * [Flet mobile update](https://flet.dev/blog/flet-mobile-update)
  * [Flet versioning and pre-releases](https://flet.dev/blog/flet-versioning-and-pre-releases)
  * [ResponsiveRow and mobile controls](https://flet.dev/blog/responsive-row-and-mobile-controls)
  * [Matplotlib and Plotly charts](https://flet.dev/blog/matplotlib-and-plotly-charts)
  * [Gesture detector](https://flet.dev/blog/gesture-detector)
  * [User authentication](https://flet.dev/blog/user-authentication)
  * [File picker and uploads](https://flet.dev/blog/file-picker-and-uploads)
  * [Fun with animations](https://flet.dev/blog/fun-with-animations)
  * [Beautiful gradients, button styles and TextField rounded corners in a new Flet release](https://flet.dev/blog/gradients-button-textfield-styles)
  * [Control Refs](https://flet.dev/blog/control-refs)
  * [Flet Mobile Strategy](https://flet.dev/blog/flet-mobile-strategy)
  * [Navigation and Routing](https://flet.dev/blog/navigation-and-routing)
  * [New release: Drag and Drop, absolute positioning and clickable container](https://flet.dev/blog/drag-and-drop-release)
  * [Using custom fonts in a Flet app](https://flet.dev/blog/using-custom-fonts-in-flet-app)
  * [Introducing Flet](https://flet.dev/blog/introducing-flet)


# Flet FastAPI and async API improvements
March 6, 2024 · 6 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
Flet makes writing dynamic, real-time web apps a real fun!
Flet 0.21.0 further improves web apps development experience as well as using asyncio APIs in your Flet apps.
Here's what's new in Flet 0.21.0:
## FastAPI with Uvicorn replaces built-in web server[​](https://flet.dev/blog/flet-fastapi-and-async-api-improvements/#fastapi-with-uvicorn-replaces-built-in-web-server "Direct link to FastAPI with Uvicorn replaces built-in web server")
From very beginning of Flet life to serve web apps there was a built-in web server written in Go and called "Fletd". It's being started on the background when you run your app with `flet run --web`. Fletd was part of Flet Python wheel contributing a few megabytes to its size. Additionally, Python app was using WebSockets to talk to Fletd web server which was adding sometimes noticeable overhead.
Then, in [Flet 0.10.0](https://flet.dev/blog/flet-for-fastapi) we have added FastAPI support to build "serious" web apps using AsyncIO API.
Now, in Flet 0.21.0 built-in web server has been completely removed and replaced with FastAPI and Uvicorn. Fletd is not a part of Flet distribution anymore.
Using FastAPI means there is no more communication overhead as web server is a part of Flet app. Also, you don't need to do any additional steps to host your app in production with FastAPI - you just use the same `ft.app(main)` command to run your app.
Breaking change
`flet_fastapi` package has been deprecated and its contents moved to `flet` package as `flet.fastapi` module. If you were using FastAPI in your Flet app replace:
```
import flet_fastapi
```

with
```
import flet.fastapi as flet_fastapi
```

**Use any ASGI web server for hosting**
You can host your Flet web app with any ASGI-compatible server such as [Uvicorn](https://www.uvicorn.org/) (used by default), [Hypercorn](https://pgjones.gitlab.io/hypercorn/) or [Daphne](https://github.com/django/daphne).
Just tell Flet to export ASGI app:
main.py
```
import flet as ftdefmain(page: ft.Page):  page.add(ft.Text("Hello ASGI!"))app = ft.app(main, export_asgi_app=True)
```

and then run with Hypercorn as:
```
hypercorn main:app --bind 0.0.0.0:8000
```

**Web app environment variables**
Every aspect of web app hosting can be controlled with environment variables:
  * `FLET_FORCE_WEB_SERVER` - `true` to force running app as a web app. Automatically set on headless Linux hosts.
  * `FLET_SERVER_PORT` - TCP port to run app on. `8000` if the program is running on a Linux server or `FLET_FORCE_WEB_SERVER` is set; otherwise random port.
  * `FLET_SERVER_IP` - IP address to listen web app on, e.g. `127.0.0.1`. Default is `0.0.0.0` - bound to all server IPs.
  * `FLET_ASSETS_DIR` - absolute path to app "assets" directory.
  * `FLET_UPLOAD_DIR` - absolute path to app "upload" directory.
  * `FLET_MAX_UPLOAD_SIZE` - max allowed size of uploaded file, in bytes. Unlimited if not specified.
  * `FLET_SECRET_KEY` - a secret key to sign temporary upload URLs.
  * `FLET_WEB_APP_PATH` - a URL path after domain name to host web app under, e.g. `/apps/myapp`. Default is `/` - host app in the root.
  * `FLET_SESSION_TIMEOUT` - session lifetime, in seconds. Default is `3600`.
  * `FLET_OAUTH_STATE_TIMEOUT` - max allowed time to complete OAuth web flow, in seconds. Default is `600`.
  * `FLET_WEB_RENDERER` - Flutter rendering mode: `canvaskit` (default), `html` or `auto`.
  * `FLET_WEB_USE_COLOR_EMOJI` - `true`, or `True` or `1` to load web font with colorful emojis.
  * `FLET_WEB_ROUTE_URL_STRATEGY` - `path` (default) or `hash`.
  * `FLET_WEBSOCKET_HANDLER_ENDPOINT` - custom path for WebSocket handler. Default is `/ws`.
  * `FLET_UPLOAD_HANDLER_ENDPOINT` - custom path for upload handler. Default is `/upload`.
  * `FLET_OAUTH_CALLBACK_HANDLER_ENDPOINT` - custom path for OAuth handler. Default is `/oauth_callback`.


## Async-first framework[​](https://flet.dev/blog/flet-fastapi-and-async-api-improvements/#async-first-framework "Direct link to Async-first framework")
Flet is now async-first framework which means you don't have to decide whether your app is entirely sync or async, but you can mix both sync and async methods in the same app.
For example, in Flet 0.21.0 you can write an app like this:
```
import flet as ftimport timeimport asynciodefmain(page: ft.Page):defhandler(e):   time.sleep(3)   page.add(ft.Text("Handler clicked"))asyncdefhandler_async(e):await asyncio.sleep(3)   page.add(ft.Text("Async handler clicked"))  page.add(    ft.ElevatedButton("Call handler", on_click=handler),    ft.ElevatedButton("Call async handler", on_click=handler_async))ft.app(main)
```

In the example above a click on one button is handled by a "blocking" handler while a click on second button calls asynchronous handler. The first handler is run in a `threading.Thread` while second handler is run in `asyncio.Task`.
Also, notice in `async def` handler you are not required to use `await page.add_async()` anymore, but a regular `page.add()` works just fine.
API changes
Most of `Page.<method>_async()` and `Control.<method>_async()` methods have been deprecated and their `Page.<method>()` and `Control.<method>()` counterparts should be used instead.
The only exception here is methods returning results, like those ones in `Audio` control: you still have to use async methods in async event handlers.
## Custom controls API normalized[​](https://flet.dev/blog/flet-fastapi-and-async-api-improvements/#custom-controls-api-normalized "Direct link to Custom controls API normalized")
In this Flet release we also re-visited API for writing custom controls in Python.
As a result `UserControl` class has been deprecated. You just inherit from a specific control with layout that works for your needs.
For example, `Countdown` custom control is just a `Text` and could be implemented as following:
```
import asyncioimport flet as ftclassCountdown(ft.Text):def__init__(self, seconds):super().__init__()    self.seconds = secondsdefdid_mount(self):    self.running =True    self.page.run_task(self.update_timer)defwill_unmount(self):    self.running =Falseasyncdefupdate_timer(self):while self.seconds and self.running:      mins, secs =divmod(self.seconds,60)      self.value ="{:02d}:{:02d}".format(mins, secs)      self.update()await asyncio.sleep(1)      self.seconds -=1defmain(page: ft.Page):  page.add(Countdown(120), Countdown(60))ft.app(main)
```

Notice the usage of `self.page.run_task(self.update_timer)` to start a new task. There is also `self.page.run_thread()` method that must be used by control developer to start a new background job in a thread.
If you want to spawn your own tasks or threads Flet provides the current event loop and thread executor via `Page.loop` and `Page.executor` properties respectively.
API changes
`Control._before_build_command()` replaced with `Control.before_update()`
`Control.build()` should not return any control now, but must update inherited control properties, for example:
```
defbuild():  self.controls.append(ft.Text("Something"))
```

`Control.did_mount_async()` and `Control.will_unmount_async()` are deprecated. Use `Control.did_mount()` and `Control.will_unmount()` instead.
## New Cupertino controls[​](https://flet.dev/blog/flet-fastapi-and-async-api-improvements/#new-cupertino-controls "Direct link to New Cupertino controls")
This Flet release adds more Cupertino controls to make your apps shine on iOS:
  * `CupertinoActivityIndicator`
  * `CupertinoActionSheet`
  * `CupertinoSlidingSegmentedButton`
  * `CupertinoSegmentedButton`
  * `CupertinoTimerPicker`
  * `CupertinoPicker`
  * `CupertinoDatePicker`
  * `CupertinoContextMenu`


## Accessibility improvements[​](https://flet.dev/blog/flet-fastapi-and-async-api-improvements/#accessibility-improvements "Direct link to Accessibility improvements")
Now Flet has complete implementation of `Semantics` control and new `SemanticsService` control.
## App lifecycle change event[​](https://flet.dev/blog/flet-fastapi-and-async-api-improvements/#app-lifecycle-change-event "Direct link to App lifecycle change event")
There is a new `Page.on_app_lifecycle_state_change` event that allows listening for changes in the application lifecycle.
For example, you can now update UI with the latest information when the app becomes active (brought to the front). This event works on iOS, Android, all desktop platforms and web!
The following app lifecycle transitions are recognized:
  * `SHOW`
  * `RESUME`
  * `HIDE`
  * `INACTIVE`
  * `PAUSE`
  * `DETACH`
  * `RESTART`


note
Read more about each [lifecycle state](https://flet.dev/docs/controls/page#on_app_lifecycle_state_change).
Here's a small example of how this event can be used:
```
import flet as ftdefmain(page: ft.Page):defapp_lifecycle_change(e: ft.AppLifecycleStateChangeEvent):if e.state == ft.AppLifecycleState.RESUME:print("Update UI with fresh data!")  page.on_app_lifecycle_state_change = app_lifecycle_change  page.add(ft.Text("Hello World"))ft.app(target=main)
```

Flet 0.21.0 release has some breaking changes. Upgrade to it, test your apps and let us know how it worked for you. Join [Flet Discord server](https://discord.gg/dzWXP8SHG8) or create a new thread on [Flet GitHub discussions](https://github.com/flet-dev/flet/discussions).
Enjoy!
**Tags:**
  * [releases](https://flet.dev/blog/tags/releases)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2024-03-06-flet-fastapi-and-async-api-improvements.md)
[Newer postControls and theming enhancements](https://flet.dev/blog/controls-and-theming-enhancements)[Older postFlet adaptive UI and custom controls release](https://flet.dev/blog/flet-adaptive-and-custom-controls)
  * [FastAPI with Uvicorn replaces built-in web server](https://flet.dev/blog/flet-fastapi-and-async-api-improvements/#fastapi-with-uvicorn-replaces-built-in-web-server)
  * [Async-first framework](https://flet.dev/blog/flet-fastapi-and-async-api-improvements/#async-first-framework)
  * [Custom controls API normalized](https://flet.dev/blog/flet-fastapi-and-async-api-improvements/#custom-controls-api-normalized)
  * [New Cupertino controls](https://flet.dev/blog/flet-fastapi-and-async-api-improvements/#new-cupertino-controls)
  * [Accessibility improvements](https://flet.dev/blog/flet-fastapi-and-async-api-improvements/#accessibility-improvements)
  * [App lifecycle change event](https://flet.dev/blog/flet-fastapi-and-async-api-improvements/#app-lifecycle-change-event)


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
