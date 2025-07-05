[Skip to main content](https://flet.dev/blog/flet-for-ios/#__docusaurus_skipToContent_fallback)
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


# Flet for iOS
July 5, 2023 · 2 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
🎉 Whoo-hoo, Flet app is now on App Store! 🎉
[![](https://flet.dev/img/blog/ios/flet-1080x1080.png)](https://apps.apple.com/app/flet/id1624979699)
With Flet iOS app you can see how your Flet Python app looks and behaves on iPhone or iPad while the app itself is running on your computer.
But it's more than just testing Flet apps on the phone! Flet mobile app itself is written in Python and its publishing to App Store is an important milestone for the entire Flet project. It is a successful proof that you can create awesome mobile apps in Python only and package them so that they are accepted in App Store!
**[Follow this guide](https://flet.dev/docs/getting-started/testing-on-ios)** to get started with testing your Flet apps on iPhone or iPad. Explore the app, browse gallery, play with sample projects and app settings.
I would like to thank [Kivy project](https://kivy.org/) for making a [toolchain for iOS](https://github.com/kivy/kivy-ios) which we used to compile Python interpreter and dependencies for iOS devices. We published [serious_python](https://pub.dev/packages/serious_python) package for adding Python runtime to any Flutter app.
## FAQ[​](https://flet.dev/blog/flet-for-ios/#faq "Direct link to FAQ")
### When Android is supported?[​](https://flet.dev/blog/flet-for-ios/#when-android-is-supported "Direct link to When Android is supported?")
Soon. It has #1 priority now and we've already started working on it.
### How to package my Flet app for App Store?[​](https://flet.dev/blog/flet-for-ios/#how-to-package-my-flet-app-for-app-store "Direct link to How to package my Flet app for App Store?")
We are going to provide a project template for bootstrap Flutter app and a guide how to combine Flutter, `serious_python` package and your Python app together to create a standalone iOS app and publish it to App Store.
Later this year we'll create a CI pipeline to fully automate the process.
Check [`serious_python`'s readme](https://github.com/flet-dev/serious-python#usage) for instructions on how create a Flutter bootstrap and package your Python app to run within it. Use [flet_example](https://github.com/flet-dev/serious-python/tree/main/src/serious_python/example/flet_example) project as a starting point.
## Flet v0.8.0 release notes[​](https://flet.dev/blog/flet-for-ios/#flet-v080-release-notes "Direct link to Flet v0.8.0 release notes")
For testing on iOS you need to upgrade your Flet installation to v0.8.0.
It's been [changed a lot](https://github.com/flet-dev/flet/blob/main/CHANGELOG.md#080) in v0.8.0 and there were some breaking changes. Bear with us while you are upgrading to 0.8.0 and let us know if you have any troubles with it.
Enjoy!
**Tags:**
  * [releases](https://flet.dev/blog/tags/releases)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2023-07-05-flet-for-ios.md)
[Newer postFlet for Android](https://flet.dev/blog/flet-for-android)[Older postScrolling controls and Theming](https://flet.dev/blog/scrolling-controls-and-theming)
  * [FAQ](https://flet.dev/blog/flet-for-ios/#faq)
    * [When Android is supported?](https://flet.dev/blog/flet-for-ios/#when-android-is-supported)
    * [How to package my Flet app for App Store?](https://flet.dev/blog/flet-for-ios/#how-to-package-my-flet-app-for-app-store)
  * [Flet v0.8.0 release notes](https://flet.dev/blog/flet-for-ios/#flet-v080-release-notes)


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
