[Skip to main content](https://flet.dev/blog/flet-for-fastapi/#__docusaurus_skipToContent_fallback)
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


# Flet for FastAPI
August 30, 2023 · 2 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
We've just released Flet 0.10.0 with FastAPI support!
![](https://flet.dev/img/blog/fastapi/fastapi-logo-teal.png)
[FastAPI](https://fastapi.tiangolo.com/) coupled with Uvicorn, Hypercorn, Gunicorn or other web server replaces built-in Flet web server (Fletd) to reliably run production Flet workloads.
On the other hand, seasoned FastAPI developers can use Flet to easily add interactive, real-time dashboards and admin UI to their existing or new FastAPI services.
## A minimal app example[​](https://flet.dev/blog/flet-for-fastapi/#a-minimal-app-example "Direct link to A minimal app example")
```
import flet as ftimport flet_fastapiasyncdefmain(page: ft.Page):await page.add_async(    ft.Text("Hello, Flet!"))app = flet_fastapi.app(main)
```

It's a simple app that just outputs "Hello, Flet!" on a web page.
To run the app install Flet for FastAPI and Uvicorn:
```
pip install flet-fastapipip install uvicorn
```

Save the code above to `hello.py` and then start uvicorn as:
```
uvicorn hello:app
```

Open the browser and navigate to <http://127.0.0.1:8000> to see the app running.
note
Flet app must be [async](https://flet.dev/docs/getting-started/async-apps) in order to work with FastAPI WebSocket handler.
## Features and benefits[​](https://flet.dev/blog/flet-for-fastapi/#features-and-benefits "Direct link to Features and benefits")
  * [Multiple Flet apps on a single domain](https://flet.dev/docs/publish/web/dynamic-website#hosting-multiple-flet-apps-under-the-same-domain) - mapped to the root and/or sub-paths.
  * Simple [one-line mappings](https://flet.dev/docs/publish/web/dynamic-website#flet-fastapi-app) or [individual endpoint configurations](https://flet.dev/docs/publish/web/dynamic-website#configuring-individual-flet-endpoints).
  * Light-weight async wrapper around FastAPI WebSocket connection for greater concurrency.
  * Serves Flet static files with user assets and app meta-information customization.
  * Uploads handler for `FilePicker` control.
  * OAuth callback handler for authentication flows.


Check [the guide](https://flet.dev/docs/publish/web/dynamic-website) for complete information about Flet with FastAPI.
Let us know what you think by joining [Flet Discord server](https://discord.gg/dzWXP8SHG8) or creating a new thread on [Flet GitHub discussions](https://github.com/flet-dev/flet/discussions).
**Tags:**
  * [releases](https://flet.dev/blog/tags/releases)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2023-08-30-flet-for-fastapi.md)
[Newer postPackaging apps for distribution](https://flet.dev/blog/packaging-apps-for-distribution)[Older postFlet for Android](https://flet.dev/blog/flet-for-android)
  * [A minimal app example](https://flet.dev/blog/flet-for-fastapi/#a-minimal-app-example)
  * [Features and benefits](https://flet.dev/blog/flet-for-fastapi/#features-and-benefits)


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
