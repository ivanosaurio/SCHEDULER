[Skip to main content](https://flet.dev/blog/flet-for-android/#__docusaurus_skipToContent_fallback)
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


# Flet for Android
July 8, 2023 · 2 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
🤖 Android support is here!
[![](https://flet.dev/img/docs/getting-started/testing-on-android/google-play-badge.png)](https://play.google.com/store/apps/details?id=com.appveyor.flet)
With Flet Android app you can see how your Flet Python app looks and behaves on Android devices while the app itself is running on your computer.
Similar to iOS, Flet for Android is a Flutter app written entirely in Python with the help of two open-source packages: [`serious_python`](https://pub.dev/packages/serious_python) and [`flet`](https://pub.dev/packages/flet). Resulting app package is technically compliant with Google Play requirements, so you can publish awesome Android apps in pure Python.
**[Follow this guide](https://flet.dev/docs/getting-started/testing-on-android)** to get started with testing your Flet apps on Android. Explore the app, browse gallery, play with sample projects and app settings.
## FAQ[​](https://flet.dev/blog/flet-for-android/#faq "Direct link to FAQ")
### How to package my Flet app for Google Play?[​](https://flet.dev/blog/flet-for-android/#how-to-package-my-flet-app-for-google-play "Direct link to How to package my Flet app for Google Play?")
We are going to provide a project template for bootstrap Flutter app and a guide how to combine Flutter, `serious_python` package and your Python app together to create a standalone Android app and publish it to Google Play.
Check [`serious_python`'s readme](https://github.com/flet-dev/serious-python#usage) for instructions on how create a Flutter bootstrap and package your Python app to run within it. Use [flet_example](https://github.com/flet-dev/serious-python/tree/main/example/flet_example) project as a starting point.
### Will you provide packaging for Windows, macOS and Linux?[​](https://flet.dev/blog/flet-for-android/#will-you-provide-packaging-for-windows-macos-and-linux "Direct link to Will you provide packaging for Windows, macOS and Linux?")
Yes! At the moment Flet desktop apps are packaged with `flet pack` command and PyInstaller. Produced app bundle adds performance and size overhead and is hard to customize, so we are going to replace it with native Flutter packaging.
## Flet v0.9.0 release notes[​](https://flet.dev/blog/flet-for-android/#flet-v090-release-notes "Direct link to Flet v0.9.0 release notes")
For testing on Android you need to upgrade your Flet installation to v0.9.0.
There were [a few changes](https://github.com/flet-dev/flet/blob/main/CHANGELOG.md#090) mainly to support Android in Flet CLI. Let us know if you notice something unusual.
Enjoy!
**Tags:**
  * [releases](https://flet.dev/blog/tags/releases)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2023-07-08-flet-for-android.md)
[Newer postFlet for FastAPI](https://flet.dev/blog/flet-for-fastapi)[Older postFlet for iOS](https://flet.dev/blog/flet-for-ios)
  * [FAQ](https://flet.dev/blog/flet-for-android/#faq)
    * [How to package my Flet app for Google Play?](https://flet.dev/blog/flet-for-android/#how-to-package-my-flet-app-for-google-play)
    * [Will you provide packaging for Windows, macOS and Linux?](https://flet.dev/blog/flet-for-android/#will-you-provide-packaging-for-windows-macos-and-linux)
  * [Flet v0.9.0 release notes](https://flet.dev/blog/flet-for-android/#flet-v090-release-notes)


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
