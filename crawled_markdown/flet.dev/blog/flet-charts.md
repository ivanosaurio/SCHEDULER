[Skip to main content](https://flet.dev/blog/flet-charts/#__docusaurus_skipToContent_fallback)
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


# Flet Charts
April 12, 2023 · 2 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
Last year we introduced support for [Matplotlib and Plotly charts](https://flet.dev/blog/matplotlib-and-plotly-charts). Both libraries are able to export charts as SVG images which are then displayed in a Flet app. However, such charts, while serving the purpose of visualization, are lacking interactivity and animation.
Today we are releasing [Flet 0.5.2](https://pypi.org/project/flet/) with built-in charts 📊 based on the awesome [fl_chart](https://pub.dev/packages/fl_chart) library!
Three new chart controls have been introduced:
## LineChart[​](https://flet.dev/blog/flet-charts/#linechart "Direct link to LineChart")
![](https://flet.dev/img/docs/controls/charts/linechart-sample-1.gif)
[Docs](https://flet.dev/docs/controls/linechart) · [Examples](https://github.com/flet-dev/examples/tree/main/python/controls/charts)
## BarChart[​](https://flet.dev/blog/flet-charts/#barchart "Direct link to BarChart")
![](https://flet.dev/img/docs/controls/charts/barchart-sample-2.gif)
[Docs](https://flet.dev/docs/controls/barchart) · [Examples](https://github.com/flet-dev/examples/tree/main/python/controls/charts)
## PieChart[​](https://flet.dev/blog/flet-charts/#piechart "Direct link to PieChart")
![](https://flet.dev/img/docs/controls/charts/piechart-sample-2.gif)
[Docs](https://flet.dev/docs/controls/piechart) · [Examples](https://github.com/flet-dev/examples/tree/main/python/controls/charts)
note
We spent a lot of time studying `fl_chart` library while trying to implement most of its features in a Flet way. However, if you see anything missing in Flet, but available in a library please [submit a new feature request](https://github.com/flet-dev/flet/issues).
## Other changes[​](https://flet.dev/blog/flet-charts/#other-changes "Direct link to Other changes")
### Pyodide 0.23[​](https://flet.dev/blog/flet-charts/#pyodide-023 "Direct link to Pyodide 0.23")
Pyodide, which provides Python runtime in a browser and is used to run Flet app as a static website, was upgraded to version 0.23 which is based on Python 3.11.2 and giving some [size and performance improvements](https://blog.pyodide.org/posts/0.23-release/).
### Memory leak fixes[​](https://flet.dev/blog/flet-charts/#memory-leak-fixes "Direct link to Memory leak fixes")
In this release we paid a lot of attention to memory leak issues in Flet apps. Now, when a user session is closed its memory is reliably released and garbage-collected. That makes Flet ready for production applications with a lot of users.
Upgrade Flet module to the latest version (`pip install flet --upgrade`), give charts a try and [let us know](https://discord.gg/dzWXP8SHG8) what you think!
Hey, [Flet project](https://github.com/flet-dev/flet) has reached ⭐️ 5K stars ⭐️ - thank you all for your continuing support!
**Tags:**
  * [releases](https://flet.dev/blog/tags/releases)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2023-04-12-flet-charts.md)
[Newer postCanvas](https://flet.dev/blog/canvas)[Older postStandalone Flet web apps with Pyodide](https://flet.dev/blog/standalone-flet-web-apps-with-pyodide)
  * [LineChart](https://flet.dev/blog/flet-charts/#linechart)
  * [BarChart](https://flet.dev/blog/flet-charts/#barchart)
  * [PieChart](https://flet.dev/blog/flet-charts/#piechart)
  * [Other changes](https://flet.dev/blog/flet-charts/#other-changes)
    * [Pyodide 0.23](https://flet.dev/blog/flet-charts/#pyodide-023)
    * [Memory leak fixes](https://flet.dev/blog/flet-charts/#memory-leak-fixes)


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
