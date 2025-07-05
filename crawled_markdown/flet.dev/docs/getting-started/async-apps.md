[Skip to main content](https://flet.dev/docs/getting-started/async-apps/#__docusaurus_skipToContent_fallback)
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
  * [Extending Flet](https://flet.dev/docs/getting-started/async-apps/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/getting-started/async-apps/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * Async apps


On this page
# Async apps
Flet app can be written as an async app and use `asyncio` and other Python async libraries. Calling coroutines is naturally supported in Flet, so you don't need to wrap them to run synchronously.
By default, Flet executes control event handlers in separate threads, but sometimes that could be an ineffective usage of CPU or it does nothing while waiting for a HTTP response or executing `sleep()`.
Asyncio, on the other hand, allows implementing concurrency in a single thread by switching execution context between "coroutines". This is especially important for apps that are going to be [published as static websites](https://flet.dev/docs/publish/web/static-website) using [Pyodide](https://pyodide.org/en/stable/). Pyodide is a Python runtime built as a WebAssembly (WASM) and running in the browser. At the time of writing it doesn't support [threading](https://github.com/pyodide/pyodide/issues/237) yet.
## Getting started with async[​](https://flet.dev/docs/getting-started/async-apps/#getting-started-with-async "Direct link to Getting started with async")
You could mark `main()` method of Flet app as `async` and then use any asyncio API inside it:
```
import flet as ftasyncdefmain(page: ft.Page):await asyncio.sleep(1)  page.add(ft.Text("Hello, async world!"))ft.app(main)
```

You can use `await ft.app_async(main)` if Flet app is part of a larger app and called from `async` code.
## Control event handlers[​](https://flet.dev/docs/getting-started/async-apps/#control-event-handlers "Direct link to Control event handlers")
Control event handlers could be both sync and `async`.
If a handler does not call any async methods it could be a regular sync method:
```
defpage_resize(e):print("New page size:", page.window.width, page.window.height)page.on_resize = page_resize
```

However, if a handler calls async logic it must be async too:
```
asyncdefmain(page: ft.Page):asyncdefbutton_click(e):await some_async_method()    page.add(ft.Text("Hello!"))  page.add(ft.ElevatedButton("Say hello!", on_click=button_click))ft.app(main)
```

### Async lambdas[​](https://flet.dev/docs/getting-started/async-apps/#async-lambdas "Direct link to Async lambdas")
There are no async lambdas in Python. It's perfectly fine to have a lambda event handler in async app for simple things:
```
page.on_error =lambda e:print("Page error:", e.data)
```

but you can't have an async lambda, so an async event handler must be used.
## Sleeping[​](https://flet.dev/docs/getting-started/async-apps/#sleeping "Direct link to Sleeping")
To delay code execution in async Flet app you should use [`asyncio.sleep()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.sleep) instead of `time.sleep()`, for example:
```
import asyncioimport flet as ftdefmain(page: ft.Page):asyncdefbutton_click(e):await asyncio.sleep(1)    page.add(ft.Text("Hello!"))  page.add(    ft.ElevatedButton("Say hello with delay!", on_click=button_click))ft.app(main)
```

## Threading[​](https://flet.dev/docs/getting-started/async-apps/#threading "Direct link to Threading")
To run something in the background use [`page.run_task()`](https://flet.dev/docs/controls/page#run_taskhandler-args-kwargs). For example, "Countdown" custom control which is self-updating on background could be implemented as following:
```
import asyncioimport flet as ftclassCountdown(ft.Text):def__init__(self, seconds):super().__init__()    self.seconds = secondsdefdid_mount(self):    self.running =True    self.page.run_task(self.update_timer)defwill_unmount(self):    self.running =Falseasyncdefupdate_timer(self):while self.seconds and self.running:      mins, secs =divmod(self.seconds,60)      self.value ="{:02d}:{:02d}".format(mins, secs)      self.update()await asyncio.sleep(1)      self.seconds -=1defmain(page: ft.Page):  page.add(Countdown(120), Countdown(60))ft.app(main)
```

![](https://flet.dev/img/docs/getting-started/user-control-countdown.gif)
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/getting-started/async-apps.md)
[PreviousTesting on Android](https://flet.dev/docs/getting-started/testing-on-android)[NextPublishing Flet app to multiple platforms](https://flet.dev/docs/publish)
  * [Getting started with async](https://flet.dev/docs/getting-started/async-apps/#getting-started-with-async)
  * [Control event handlers](https://flet.dev/docs/getting-started/async-apps/#control-event-handlers)
    * [Async lambdas](https://flet.dev/docs/getting-started/async-apps/#async-lambdas)
  * [Sleeping](https://flet.dev/docs/getting-started/async-apps/#sleeping)
  * [Threading](https://flet.dev/docs/getting-started/async-apps/#threading)


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
