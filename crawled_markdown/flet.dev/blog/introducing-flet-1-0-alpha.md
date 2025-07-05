[Skip to main content](https://flet.dev/blog/introducing-flet-1-0-alpha/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search
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


# Introducing Flet 1.0 Alpha
June 26, 2025 · 12 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
Flet has been in the making for over three years, steadily gaining traction and building a vibrant user community. As more developers adopt Flet for real-world projects, one thing has become clear: people are ready to commit — but they also want to see the same commitment from us.
Releasing **Flet 1.0** isn’t just about a version number. It’s about signaling stability, maturity, and long-term vision. A stable API, comprehensive documentation, better testing and clearly communicated roadmap — these are the foundational pieces developers need to confidently build serious apps on Flet.
But **Flet 1.0 isn’t just the next incremental release. It’s a complete re-architecture**.
The first versions of Flet inherited design decisions from Pglet — a web-based framework with a focus on multi-language support. While that served as a useful starting point, Flet has since evolved into a Python-centric framework for building cross-platform apps — web, desktop, and mobile.
With that evolution came technical debt, architectural misfits, and increasing complexity. Rather than patch over the cracks, we made a bold decision: to rewrite Flet from the ground up. It’s always risky to rewrite, but there’s no better time than now — before 1.0 — while the user base is still manageable and we can afford to break things in the name of long-term simplicity and maintainability.
After nearly five months of work, **today we’re releasing the Flet 1.0 Alpha — a technical preview of what’s coming.**
## What’s new[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#whats-new "Direct link to What’s new")
Flet 1.0 introduces major changes that simplify how you build, run, and scale apps. Some are improvements, some are breaking — all are focused on giving you a faster, more flexible developer experience.
  * **Declarative approach to building Flet apps** - alongside the traditional imperative style.
  * **Auto-update** - automatic page updates after event handler completion.
  * **Services** - persistent, non-UI components that live across UI rebuilds and navigation. Existing controls such as `Audio`, `FilePicker`, `Clipboard` were re-written as services.
  * **Complete WASM (WebAssembly) support for web apps** - faster download and performance on modern browsers.
  * **Offline (no-CDN) mode for web apps** - Flutter resources and Pyodide are bundled with the app.
  * **Embedding Flet apps into existing web page** - render Flet app into an HTML element on any web page.
  * **Enhanced Extensions API** - to export services along with controls, with a room for future customizations like splash and loading screens.


### Declarative approach[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#declarative-approach "Direct link to Declarative approach")
Flet 1.0 introduces a **declarative/reactive approach** to building UIs in Flet. Developers can now mix **imperative** and **declarative** patterns in the same app, enabling more flexible and functional UI code.
#### Basic declarative Flet app example[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#basic-declarative-flet-app-example "Direct link to Basic declarative Flet app example")
```
from dataclasses import dataclassimport flet as ft@dataclassclassAppState:  count:intdefincrement(self):    self.count +=1defmain(page: ft.Page):  state = AppState(count=0)  page.floating_action_button = ft.FloatingActionButton(    icon=ft.Icons.ADD, on_click=state.increment)  page.add(    ft.ControlBuilder(      state,lambda state: ft.SafeArea(        ft.Container(          ft.Text(value=f"{state.count}", size=50),          alignment=ft.Alignment.center(),),        expand=True,),      expand=True,))ft.run(main)
```

More declarative examples:
  * [Edit form](https://github.com/flet-dev/examples/blob/v1/python/apps/declarative/edit-form.py)
  * [Progress bar with yield](https://github.com/flet-dev/examples/blob/v1/python/apps/declarative/progress-with-yield.py)
  * 🚀 [Reactive ToDo app](https://github.com/flet-dev/examples/blob/v1/python/apps/todo/todo-reactive.py)


🚧 Documentation is in progress 🚧
### Auto-update[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#auto-update "Direct link to Auto-update")
`Control.update()` is now automatically called once its event handler method is finished. Most of Flet apps will now work without explicit `update()` calls.
Use `yield` inside long-running event handlers to refresh UI, for example:
```
asyncdefbutton_click(): progress.value ="Something started"yieldawait asyncio.sleep(3) progress.value ="Something finished"
```

🚧 Documentation is in progress 🚧
### Services[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#services "Direct link to Services")
"Service" is a persistent, non-visual control that can "survive" page updates and navigation transitions.
Some of the existing controls were re-implemented as services (breaking change):
  * `Audio` ([extension](https://pypi.org/project/flet-audio/))
  * `AudioRecorder` ([extension](https://pypi.org/project/flet-audio-recorder/))
  * `FilePicker`
  * `Flashlight` ([extension](https://pypi.org/project/flet-flashlight/))
  * `Geolocator` ([extension](https://pypi.org/project/flet-geolocator/))
  * `HapticFeedback`
  * `InterstitialAd` ([extension](https://pypi.org/project/flet-ads/))
  * `PermissionHandler` ([extension](https://pypi.org/project/flet-permission-handler/))
  * `SemanticsService`
  * `ShakeDetector`


Service instances must be added to `page.services` list to work.
### WebAssembly support[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#webassembly-support "Direct link to WebAssembly support")
Flet 1.0 web apps use WebAssembly (WASM) by default on [selected browsers](https://docs.flutter.dev/platform-integration/web/wasm#learn-more-about-browser-compatibility).
Built-in Flet web client and Flet apps built with `flet build web` are now include both Dart2JS (with CanvasKit as a renderer) and WebAssembly (with SKWASM renderer) targets.
🚧 Documentation is in progress 🚧
### Offline mode for web apps[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#offline-mode-for-web-apps "Direct link to Offline mode for web apps")
Flet 1.0 has "no-CDN" mode which allows bundling the following resources along with your app instead of loading them from external CDNs:
  * CanvasKit
  * SkWASM
  * Pyodide
  * Fonts


To enable no-CDN during runtime either add `no_cdn=True` to `ft.run()` (it's a new `ft.app()`) call:
```
ft.run(main, no_cdn=True)
```

or set `FLET_WEB_NO_CDN` environment variable to `1`, `true` or `yes`.
To enable no-CDN for `flet build` add `--no-cdn` argument.
🚧 Documentation is in progress 🚧
### Embedding Flet web apps[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#embedding-flet-web-apps "Direct link to Embedding Flet web apps")
You can now embed a Flet web app into any HTML element within an existing web page.
It's also possible to render multiple views of the same app in different HTML elements.
🚧 Documentation is in progress 🚧
### Enhanced Extensions API[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#enhanced-extensions-api "Direct link to Enhanced Extensions API")
The new extensions API allows exporting from your Flutter package of both control and service widgets. Technically, an extension is a class now rather than a method which will allow us to add more hooks into it like custom spash and loading screens.
For example, `flet-ads` extension before has just one `createControl` method:
create_control.dart
```
import 'package:flet/flet.dart';import 'package:google_mobile_ads/google_mobile_ads.dart';import 'banner.dart';import 'interstitial.dart';CreateControlFactory createControl = (CreateControlArgs args) { switch (args.control.type) {  case "banner_ad":   return BannerAdControl(     parent: args.parent, control: args.control, backend: args.backend);  case "interstitial_ad":   return InterstitialAdControl(     parent: args.parent, control: args.control, backend: args.backend);  default:   return null; }};void ensureInitialized() { if (isMobilePlatform()) {  MobileAds.instance.initialize(); }}
```

and for Flet v1 it has two methods `createWidget` and `createService`:
extension.dart
```
import 'package:flet/flet.dart';import 'package:flutter/cupertino.dart';import 'package:google_mobile_ads/google_mobile_ads.dart';import 'banner.dart';import 'interstitial.dart';class Extension extends FletExtension { @override void ensureInitialized() {  if (isMobilePlatform()) {   MobileAds.instance.initialize();  } } @override FletService? createService(Control control) {  switch (control.type) {   case "InterstitialAd":    return InterstitialAdService(control: control);   default:    return null;  } } @override Widget? createWidget(Key? key, Control control) {  switch (control.type) {   case "BannerAd":    return BannerAdControl(control: control);   default:    return null;  } }}
```

This change is breaking.
🚧 Documentation is in progress 🚧
### Other changes and improvements[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#other-changes-and-improvements "Direct link to Other changes and improvements")
### `ft.run` with `before_main`[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#ftrun-with-before_main "Direct link to ftrun-with-before_main")
A new `before_main` arg added to `ft.run()` (replaces `ft.app()`). `before_main` is a hook that allows to reliable configure page-level event handlers before Flutter client starts sending events. `before_main` is a function that accepts one parameter: `page: ft.Page`
Example usage:
```
defconfig(page: ft.Page): page.on_resize =lambda e:print("Page resized!")defmain(page: ft.Page): page.add(ft.Text("Hello!"))ft.run(main, before_main=config)
```

#### Storage paths[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#storage-paths "Direct link to Storage paths")
There is a new `page.storage_paths` multi-platform API based on [path_provider](https://pub.dev/packages/path_provider) for finding commonly used locations on the filesystem:
```
get_application_cache_directory_async(self)->strget_application_documents_directory_async(self)->strget_application_support_directory_async(self)->strget_downloads_directory_async(self)-> Optional[str]get_external_cache_directories_async(self)-> Optional[List[str]]get_external_storage_directories_async(self)-> Optional[List[str]]get_library_directory_async(self)->strget_external_cache_directory_async(self)-> Optional[str]get_temporary_directory_async(self)->strget_console_log_filename_async(self)->str
```

🚧 Documentation is in progress 🚧
#### Event handlers without `e`[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#event-handlers-without-e "Direct link to event-handlers-without-e")
Event handlers can now omit `e` parameter, for example both of these work:
```
button_1.on_click =lambda:print("Clicked!")button_2.on_click =lambda e:print("Clicked!", e)
```

or
```
defincrement():print("Increment clicked")inc_btn.on_click = increment
```

#### `Control.before_event(e)` hook[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#controlbefore_evente-hook "Direct link to controlbefore_evente-hook")
The method is called before calling any event handler.
It receives an instance of `ControlEvent` as parameter and should return either `True` or `False`. Returning `False` cancels event handler. Example implementation in `Page` class:
```
defbefore_event(self, e: ControlEvent):ifisinstance(e, RouteChangeEvent):if self.route == e.route:returnFalse      self.query()returnsuper().before_event(e)
```

#### `ft.context.page` works everywhere[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#ftcontextpage-works-everywhere "Direct link to ftcontextpage-works-everywhere")
It's now possible to get a reference to a current `Page` instance in any part of Flet program.
## The new Architecture[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#the-new-architecture "Direct link to The new Architecture")
Flet 1.0 is not just a feature release — it's a ground-up rewrite designed to address technical debt, improve maintainability, and unlock long-term performance and flexibility. Here are some of the most impactful architectural changes:
### Simplified Python control implementation[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#simplified-python-control-implementation "Direct link to Simplified Python control implementation")
  * Controls are now implemented as Python **dataclasses** , bringing:
    * Automatic constructor generation
    * Native support for default values, type annotations, and field validation
    * No more manual conversions to/from `str` or `JSON`
    * Seamless support for **complex property types** (nested dataclasses, enums, etc.)
  * This significantly reduces boilerplate and makes adding new controls trivial — often zero-maintenance.


### Strong typing and IDE support[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#strong-typing-and-ide-support "Direct link to Strong typing and IDE support")
  * Event handlers are now **strongly typed** , improving both runtime safety and developer ergonomics.
  * All controls include **docstrings** , enabling rich auto-generated API documentation with **Docusaurus**.


### Smarter UI diffing[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#smarter-ui-diffing "Direct link to Smarter UI diffing")
  * A new **diffing algorithm** powers efficient updates to the UI tree.
  * It’s optimized for both **imperative** and **declarative** Flet programming styles.
  * This results in faster rebuilds and fewer unnecessary redraws.


### Dart runtime modernization[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#dart-runtime-modernization "Direct link to Dart runtime modernization")
  * Replaced the old Redux-based state management with **InheritedWidget** + **Provider**.
  * The internal control hierarchy on the Dart side now mirrors the Python control tree, enabling **more efficient traversal and updates**.


### Binary protocol for performance[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#binary-protocol-for-performance "Direct link to Binary protocol for performance")
  * A new **binary serialization protocol** (MessagePack) replaces the JSON-based message format:
    * Significantly reduces traffic size
    * No more base64 encoding for transferring binary data (e.g., images, files)
  * Control property names in Dart now **exactly match their Python counterparts** , making it easier to debug and extend across both runtimes.


## Breaking changes[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#breaking-changes "Direct link to Breaking changes")
Flet 1.0 is a major release and includes breaking changes — for good reason!
The Flet team maintains a list of known breaking changes in [this issue](https://github.com/flet-dev/flet/issues/5238).
If you discover something else that’s broken or incorrect, please submit a new issue or discussion. Once confirmed, we’ll update the list.
Below is a summary of the most significant and impactful breaking changes:
### Single-threaded async UI model[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#single-threaded-async-ui-model "Direct link to Single-threaded async UI model")
Flet 1.0 adopts a single-threaded async UI model, similar to JavaScript or Flutter. This design makes concurrency more predictable and better suited for the browser and mobile platforms.
  * Blocking calls like `time.sleep()` will freeze the UI. Instead of `time.sleep()` use `async def` event handlers and using `await asyncio.sleep()` for delays.
  * Switch to async APIs whenever possible.
  * For CPU-bound tasks, offload them to threads using `asyncio.to_thread(...)`.


🚧 Example with CPU-bound method updating progress bar 🚧
### Async control methods[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#async-control-methods "Direct link to Async control methods")
All controls' get- and set- methods are async now.
Methods that do not return any results have fire-and-forget sync wrappers.
🚧 Documentation is in progress 🚧
### `ft.run()` replaces `ft.app()`[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#ftrun-replaces-ftapp "Direct link to ftrun-replaces-ftapp")
`target` argument renamed to `main` and the rest of method arguments stays the same. A new `before_main` argument added (see above).
### `Page` split[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#page-split "Direct link to page-split")
`Page` split into `Page` and `PageView`.
To support Flet embedding with multi-views.
It's not a breaking-change per-se if you just continue to use `page` instance methods or properties.
🚧 Documentation is in progress 🚧
### Dialogs[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#dialogs "Direct link to Dialogs")
To display a dialog, banner, snack bar, drawer, or any similar popup control, use `page.show_dialog(dialog_control)` instead of `page.open()`.
To close the topmost popup, use `page.pop_dialog()`.
### Drawers[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#drawers "Direct link to Drawers")
`page.drawer` and `page.end_drawer` were removed.
note
We might re-introduce this in the future, to fix displaying of the top menu icon button as in this [example](https://api.flutter.dev/flutter/material/Scaffold/endDrawer.html).
Use `NavigationDrawer.position` property and then `page.show_dialog()` to display drawer instead of `page.drawer` and `page.end_drawer`.
### FilePicker[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#filepicker "Direct link to FilePicker")
FilePicker is now a service and must be added to `page.services` list to work.
API re-worked to provide async methods immediatly returning dialog results without using "result" event handlers.
```
files:list[FilePickerFile]=await file_picker.pick_files_async(allow_multiple=True)file_name:str=await file_picker.save_file_async()dir_name:str=await file_picker.get_directory_path_async()
```

Full examples:
  * [All dialogs](https://github.com/flet-dev/examples/blob/v1/python/controls/utility/file-picker/file-picker-all-modes.py)
  * [Upload](https://github.com/flet-dev/examples/blob/v1/python/controls/utility/file-picker/file-picker-upload-progress.py)


### Clipboard[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#clipboard "Direct link to Clipboard")
Instead of `page.set_clipboard()` use `page.clipboard.set_async()`.
Instead of `page.get_clipboard()` use `page.clipboard.get_async()`.
### Client storage[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#client-storage "Direct link to Client storage")
"Client storage" is now "Shared Preferences".
`page.client_storage` property renamed to `page.shared_preferences`.
### Scrollables[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#scrollables "Direct link to Scrollables")
In scrollable controls `on_scroll_interval` property renamed to `scroll_interval`.
### Buttons[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#buttons "Direct link to Buttons")
All buttons: no `text` property, use `content` instead.
### Charts[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#charts "Direct link to Charts")
Chart controls have been moved to a separate package [flet-charts](https://pypi.org/project/flet-charts/).
### Control ID is integer[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#control-id-is-integer "Direct link to Control ID is integer")
`e.target` is a number now, not a string.
## Trying Flet 1.0 Alpha[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#trying-flet-10-alpha "Direct link to Trying Flet 1.0 Alpha")
We are releasing Flet 1.0 Alpha as [0.70.0.dev5066](https://pypi.org/project/flet/0.70.0.dev5066/).
info
Going forward Flet 1.0 will be called `v1` and Flet 0.x will be called `v0`.
`main` branch of Flet repository will have Flet 1.0 and `v0` branch will have Flet 0.x.
caution
Make sure you are installing Flet pre-release to a new virtual environment.
To install Flet v1 Alpha:
```
pip install 'flet[all]==0.70.0.dev5066'
```

or add `flet==0.70.0.dev5066` to dependencies of your Python project.
### `flet build`[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#flet-build "Direct link to flet-build")
To make `flet build` work with Flet 1.0 Alpha specify exact version of `flet` and all extension packages in `dependencies` section of your `pyproject.toml`:
```
dependencies=[ "flet==0.70.0.dev5066", "flet-audio==0.2.0.dev5066", "flet-video==0.2.0.dev5066", ...]
```

Extensions for Flet v1 will have version `0.2.x` and above and Flet v0 extensions will have version `0.1.x`.
## Roadmap to Flet 1.0[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#roadmap-to-flet-10 "Direct link to Roadmap to Flet 1.0")
  * Flet 0.70 aka "**Flet 1.0 Alpha** " - this release. Generated docs are not yet included. We may release a few Flet 0.71, 0.72, 0.73, etc. to fix things.
  * Flet 0.80 aka "**Flet 1.0 Beta** " - docs generated from sources are ready. All extensions are working and documented. Integration tests are available.
  * Flet 0.90 aka "**Flet 1.0 RC** " - website landing page is updated, API complete and frozen.
  * Flet 1.0 aka "**Flet 1.0 RTM** " - final release! 🎉


## Conclusion[​](https://flet.dev/blog/introducing-flet-1-0-alpha/#conclusion "Direct link to Conclusion")
Flet 1.0 Alpha marks the beginning of a new chapter for the framework — one focused on performance, maintainability, and developer experience. It introduces a streamlined architecture, a powerful declarative programming model, and a reimagined extension system — all while laying the groundwork for a stable and scalable 1.0 release.
This is a technical preview, and while it's not production-ready yet, we invite you to try it out, share your feedback, and help us shape the future of Flet.
We’re incredibly excited about what’s coming next — and we’re just getting started.
**Tags:**
  * [news](https://flet.dev/blog/tags/news)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2025-06-26-introducing-flet-1-0-alpha.md)
[Older postTap into native Android and iOS APIs with Pyjnius and Pyobjus](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus)
  * [What’s new](https://flet.dev/blog/introducing-flet-1-0-alpha/#whats-new)
    * [Declarative approach](https://flet.dev/blog/introducing-flet-1-0-alpha/#declarative-approach)
    * [Auto-update](https://flet.dev/blog/introducing-flet-1-0-alpha/#auto-update)
    * [Services](https://flet.dev/blog/introducing-flet-1-0-alpha/#services)
    * [WebAssembly support](https://flet.dev/blog/introducing-flet-1-0-alpha/#webassembly-support)
    * [Offline mode for web apps](https://flet.dev/blog/introducing-flet-1-0-alpha/#offline-mode-for-web-apps)
    * [Embedding Flet web apps](https://flet.dev/blog/introducing-flet-1-0-alpha/#embedding-flet-web-apps)
    * [Enhanced Extensions API](https://flet.dev/blog/introducing-flet-1-0-alpha/#enhanced-extensions-api)
    * [Other changes and improvements](https://flet.dev/blog/introducing-flet-1-0-alpha/#other-changes-and-improvements)
    * [`ft.run` with `before_main`](https://flet.dev/blog/introducing-flet-1-0-alpha/#ftrun-with-before_main)
  * [The new Architecture](https://flet.dev/blog/introducing-flet-1-0-alpha/#the-new-architecture)
    * [Simplified Python control implementation](https://flet.dev/blog/introducing-flet-1-0-alpha/#simplified-python-control-implementation)
    * [Strong typing and IDE support](https://flet.dev/blog/introducing-flet-1-0-alpha/#strong-typing-and-ide-support)
    * [Smarter UI diffing](https://flet.dev/blog/introducing-flet-1-0-alpha/#smarter-ui-diffing)
    * [Dart runtime modernization](https://flet.dev/blog/introducing-flet-1-0-alpha/#dart-runtime-modernization)
    * [Binary protocol for performance](https://flet.dev/blog/introducing-flet-1-0-alpha/#binary-protocol-for-performance)
  * [Breaking changes](https://flet.dev/blog/introducing-flet-1-0-alpha/#breaking-changes)
    * [Single-threaded async UI model](https://flet.dev/blog/introducing-flet-1-0-alpha/#single-threaded-async-ui-model)
    * [Async control methods](https://flet.dev/blog/introducing-flet-1-0-alpha/#async-control-methods)
    * [`ft.run()` replaces `ft.app()`](https://flet.dev/blog/introducing-flet-1-0-alpha/#ftrun-replaces-ftapp)
    * [`Page` split](https://flet.dev/blog/introducing-flet-1-0-alpha/#page-split)
    * [Dialogs](https://flet.dev/blog/introducing-flet-1-0-alpha/#dialogs)
    * [Drawers](https://flet.dev/blog/introducing-flet-1-0-alpha/#drawers)
    * [FilePicker](https://flet.dev/blog/introducing-flet-1-0-alpha/#filepicker)
    * [Clipboard](https://flet.dev/blog/introducing-flet-1-0-alpha/#clipboard)
    * [Client storage](https://flet.dev/blog/introducing-flet-1-0-alpha/#client-storage)
    * [Scrollables](https://flet.dev/blog/introducing-flet-1-0-alpha/#scrollables)
    * [Buttons](https://flet.dev/blog/introducing-flet-1-0-alpha/#buttons)
    * [Charts](https://flet.dev/blog/introducing-flet-1-0-alpha/#charts)
    * [Control ID is integer](https://flet.dev/blog/introducing-flet-1-0-alpha/#control-id-is-integer)
  * [Trying Flet 1.0 Alpha](https://flet.dev/blog/introducing-flet-1-0-alpha/#trying-flet-10-alpha)
    * [`flet build`](https://flet.dev/blog/introducing-flet-1-0-alpha/#flet-build)
  * [Roadmap to Flet 1.0](https://flet.dev/blog/introducing-flet-1-0-alpha/#roadmap-to-flet-10)
  * [Conclusion](https://flet.dev/blog/introducing-flet-1-0-alpha/#conclusion)


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
