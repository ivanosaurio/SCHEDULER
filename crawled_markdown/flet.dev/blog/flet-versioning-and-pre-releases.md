[Skip to main content](https://flet.dev/blog/flet-versioning-and-pre-releases/#__docusaurus_skipToContent_fallback)
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


# Flet versioning and pre-releases
November 16, 2022 · 2 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
Flet is a fast-evolving framework with a new functionality and bug fixes being committed every other day.
The development model with one pull request per release didn't work well for the project as users waited for weeks to get hands on a new release and, honestly, from development perspective producing large "heroic" releases takes a lot of energy 🫠.
From now on we'll be breaking releases into multiple pull requests with one feature/bugfix per PR.
Every PR merged into `main` branch will be publishing pre-release (developmental release) package to [pypi.org](https://pypi.org/project/flet/) having version format of `X.Y.Z.devN`.
## Installing pre-releases[​](https://flet.dev/blog/flet-versioning-and-pre-releases/#installing-pre-releases "Direct link to Installing pre-releases")
To install Flet pre-release package use the following command:
```
pip install flet --pre
```

info
We recommend installing pre-release builds into a virtual environment.
## Flet versioning[​](https://flet.dev/blog/flet-versioning-and-pre-releases/#flet-versioning "Direct link to Flet versioning")
Flet is switching to [Semanting Versioning](https://semver.org/) with a version number `MAJOR.MINOR.PATCH`:
  1. `MAJOR` will be incremented when there are "incompatible API changes". Right now it's `0` and we expect to make it `1` when we feel that Flet API is stable enough.
  2. `MINOR` will be incremented when a new functionality added in a backwards compatible manner.
  3. `PATCH` will be incremented when we make backward compatible bug fixes.


According to that rule, upcoming Flet release will have version `0.2.0`. Bug fixes for that release will be labeled as `0.2.1`, `0.2.2`, etc. The release after that release will be `0.3.0` and so on.
Flet pre-releases will have a format of `MAJOR.{LAST_MINOR + 1}.0.dev{BUILD}` where `LAST_MINOR` is `MINOR` version of the last release and `{BUILD}` is a build number set by [CI](https://ci.appveyor.com/project/flet-dev/flet). For example, if the last published release is `0.1.65` pre-releases will have versions `0.2.0.dev{BUILD}`. Pre-releases after `0.2.0` release will be labeled as `0.3.0.dev{BUILD}`.
**Tags:**
  * [news](https://flet.dev/blog/tags/news)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2022-11-16-flet-versioning-and-pre-releases.md)
[Newer postFlet mobile update](https://flet.dev/blog/flet-mobile-update)[Older postResponsiveRow and mobile controls](https://flet.dev/blog/responsive-row-and-mobile-controls)
  * [Installing pre-releases](https://flet.dev/blog/flet-versioning-and-pre-releases/#installing-pre-releases)
  * [Flet versioning](https://flet.dev/blog/flet-versioning-and-pre-releases/#flet-versioning)


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
