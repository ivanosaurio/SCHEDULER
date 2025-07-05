[Skip to main content](https://flet.dev/blog/flet-mobile-update/#__docusaurus_skipToContent_fallback)
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


# Flet mobile update
December 8, 2022 · 5 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
This post is a continuation of [Flet mobile strategy](https://flet.dev/blog/flet-mobile-strategy) published a few months ago.
Our original approach to Flet running on a mobile device was Server-Driven UI. Though SDUI has its own benefits (like bypassing App Store for app updates) it doesn't work in all cases, requires web server to host Python part of the app and, as a result, adds latency which is not great for user actions requiring nearly instance UI response, like drawing apps.
I've been thinking on how to make Python runtime embedded into Flutter iOS or Android app to run user Python program. No doubt, it's technically possible as Kivy and BeeWare projects do that already.
## Current Flet architecture[​](https://flet.dev/blog/flet-mobile-update/#current-flet-architecture "Direct link to Current Flet architecture")
The current architecture of Flet desktop app is shown on the diagram below:
![](https://flet.dev/img/blog/mobile-update/flet-desktop-architecture.svg)
Running Flet program on a desktop involves three applications (processes) working together:
  * **Python runtime** (`python3`) - Python interpreter running your Python script. This is what you are starting from a command line. Python starts Fletd server and connects to it via WebSockets.
  * **Fletd server** (`fletd`)- Flet web server written in Go, listening on a TCP port. Fletd holds the state of all user sessions (for desktop app there is only one session) and dispatches page updates and user generated events between Python program and Flet client.
  * **Flet client** (`flet`) - desktop app written in Flutter and displaying UI in a native OS window. Flet client connects to Fletd server via WebSockets.


The architecture above works well for Flet web apps where web server is essential part, but for desktop it seems redundant:
  * If all three processes run on the same computer WebSockets could be replaced with sockets or named pipes with less overhead.
  * Fletd server has no much sense as there is only one user session and UI state is persistently stored in Flet desktop client which is never "reloaded".


## Flet new desktop architecture[​](https://flet.dev/blog/flet-mobile-update/#flet-new-desktop-architecture "Direct link to Flet new desktop architecture")
Flet desktop app architecture can be simplified by replacing Fletd with a "stub" written in Python and communicating with Flet desktop client via sockets (Windows) and named pipes (macOS and Linux):
![](https://flet.dev/img/blog/mobile-update/flet-desktop-architecture-v2.svg)
## Flet mobile architecture[​](https://flet.dev/blog/flet-mobile-update/#flet-mobile-architecture "Direct link to Flet mobile architecture")
Mobile applications are running in a very strict context with a number of limitations. For example, on iOS the app cannot spawn a new processes. Other words, Flet Flutter app cannot just start "python.exe" and pass your script as an argument.
Luckily for us, [Python can be embedded](https://docs.python.org/3/extending/embedding.html) into another app as a C library and Dart (the language in which Flutter apps are written) allows calling C libraries via [FFI](https://dart.dev/guides/libraries/c-interop) (Foreign Function Interface).
Additionally, while Android allows loading of dynamically linked libraries iOS requires all libraries statically linked into app executable. [This article](https://blog.logrocket.com/dart-ffi-native-libraries-flutter/) covers Dart FFI in more details, if you are curious.
Flet mobile architecture could look like this:
![](https://flet.dev/img/blog/mobile-update/flet-mobile-architecture-v2.svg)
Python runtime will be statically or dynamically linked with Flutter client app and called via FFI and/or named pipes.
Running Python on mobile will have some limitations though. Most notable one is the requirement to use "pure" Python modules or modules with native code compiled specifically for mobile ARM64 architecture.
## Asyncio support[​](https://flet.dev/blog/flet-mobile-update/#asyncio-support "Direct link to Asyncio support")
[Asyncio](https://docs.python.org/3/library/asyncio.html) is part of Python 3 and we start seeing more and more libraries catching up with async/await programming model which is more effective for I/O-bound and UI logic.
Currently, Flet is spawning all UI event handlers in new threads and it's also a pain to see `threading.sleep()` calls hogging threads here and there just to do some UI animation. All that looks expensive.
Using of async libraries from a sync code is [possible](https://github.com/flet-dev/flet/issues/128), but looks hacky and inefficient as it keeps CPU busy just to wait async method to finish. So, we want a first-class support of async code in Flet app.
Async/await model is a state machine switching between tasks in a single thread. By going async Flet will able to utilize [streams](https://docs.python.org/3/library/asyncio-stream.html) for socket server and use async [WebSockets library](https://pypi.org/project/websockets/) library. It will be possible to use both sync and async event handlers in a single Flet app without any compromises or hacks.
Even more exciting, async Flet will be able to run entirely in the browser within [Pyodide](https://pyodide.org/) - Python distribution based on WebAssembly (WASM). WebAssembly doesn't have multi-threading support yet, so running in a single thread is a must. Just imagine, Flet web app with a truly offline Flet PWA that does not require a web server to run a Python code!
## Development plan[​](https://flet.dev/blog/flet-mobile-update/#development-plan "Direct link to Development plan")
We are going to crunch the scope above in a few iterations:
  1. Async API support with async WebSockets library. Works with the same Fletd in Go.
  2. Fletd server ("stub") in Python to use with a desktop.
  3. Embedding Python with Fletd "stub" and user program into iOS.
  4. Embedding Python into Android.
  5. Packaging mobile apps for iOS and Android.


HELP WANTED
🙏 I'm looking for a help from the community with developing C/C++/native code integration part between Flutter and Python on iOS and Android. It could be either free help or a paid job - let me know if you are interested!
Hop to [Discord](https://discord.gg/dzWXP8SHG8) to discuss the plan, offer help, ask questions!
**Tags:**
  * [news](https://flet.dev/blog/tags/news)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2022-12-08-flet-mobile-update.md)
[Newer postPackaging desktop apps with a custom icon](https://flet.dev/blog/packaging-desktop-apps-with-custom-icon)[Older postFlet versioning and pre-releases](https://flet.dev/blog/flet-versioning-and-pre-releases)
  * [Current Flet architecture](https://flet.dev/blog/flet-mobile-update/#current-flet-architecture)
  * [Flet new desktop architecture](https://flet.dev/blog/flet-mobile-update/#flet-new-desktop-architecture)
  * [Flet mobile architecture](https://flet.dev/blog/flet-mobile-update/#flet-mobile-architecture)
  * [Asyncio support](https://flet.dev/blog/flet-mobile-update/#asyncio-support)
  * [Development plan](https://flet.dev/blog/flet-mobile-update/#development-plan)


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
