[Skip to main content](https://flet.dev/blog/matplotlib-and-plotly-charts/#__docusaurus_skipToContent_fallback)
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


# Matplotlib and Plotly charts
October 24, 2022 · 2 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
We are thrilled to introduce Matplotlib and Plotly charting controls in [Flet 0.1.63](https://pypi.org/project/flet/0.1.63/)!
[Matplotlib](https://matplotlib.org/) and [Plotly](https://plotly.com/python/) are the most recognized Python charting libraries with a ton of features. They are greatly compatible with other scientific Python libraries such as Numpy or Pandas.
No doubt, it would be nearly impossible to replicate their functionality as pure Flutter widgets. Fortunately, both Matplotlib and Plotly can export charts into various formats, such as SVG. On the other hand Flet can [display SVG images](https://github.com/flet-dev/examples/blob/main/python/controls/image/svg-image.py) and that gives a perfect combination - Flet charting controls for Matplotlib and Plotly!
The resulting solution works so great that it's possible to display almost any example from [Matplotlib](https://matplotlib.org/stable/gallery/index.html) and [Plotly](https://plotly.com/python/) galleries - your imagination is the only limit!
Plot a [simple bar chart](https://github.com/flet-dev/examples/blob/main/python/controls/charts/mpl-barchart.py):
![](https://flet.dev/img/docs/controls/charts/matplotlib-barchart.png)
a nice [scatter with legend](https://github.com/flet-dev/examples/blob/main/python/controls/charts/mpl-scatter.py):
![](https://flet.dev/img/docs/controls/charts/matplotlib-scatter.png)
or some multi-chart [contour plot](https://github.com/flet-dev/examples/blob/main/python/controls/charts/mpl-contour.py):
![](https://flet.dev/img/docs/controls/charts/matplotlib-contour.png)
Check the docs for Matplotlib and Plotly charting controls:
  * [MatplotlibChart](https://flet.dev/docs/controls/matplotlibchart)
  * [PlotlyChart](https://flet.dev/docs/controls/plotlychart)


Explore [Flet chart examples](https://github.com/flet-dev/examples/tree/main/python/controls/charts).
Learn Python libraries by examples:
  * [Matplotlib gallery](https://matplotlib.org/stable/gallery/index.html)
  * [Plotly gallery](https://plotly.com/python/)


In the future releases, we may add an interactive "toolbar" for Matplotlib charts by implementing a custom [backend](https://matplotlib.org/stable/users/explain/backends.html). Or maybe it's a great exercise for Flet users? 😉
Also, when it's time for Flet to support other languages we would need to re-visit charting to make it language-agnostic as the current charting implementation relies on Python libraries.
Upgrade Flet module to the latest version (`pip install flet --upgrade`), integrate auth in your app and [let us know](https://discord.gg/dzWXP8SHG8) what you think!
Enjoy!
**Tags:**
  * [release](https://flet.dev/blog/tags/release)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2022-10-24-matplotlib-and-plotly-charts.md)
[Newer postResponsiveRow and mobile controls](https://flet.dev/blog/responsive-row-and-mobile-controls)[Older postGesture detector](https://flet.dev/blog/gesture-detector)
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
