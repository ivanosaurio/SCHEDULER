[Skip to main content](https://flet.dev/blog/#__docusaurus_skipToContent_fallback)
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


## [Introducing Flet 1.0 Alpha](https://flet.dev/blog/introducing-flet-1-0-alpha)
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
**Tags:**
  * [news](https://flet.dev/blog/tags/news)


[**Read more**](https://flet.dev/blog/introducing-flet-1-0-alpha)
## [Tap into native Android and iOS APIs with Pyjnius and Pyobjus](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus)
February 23, 2025 · 3 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
When building mobile apps with Flet, you may need to interact directly with platform-specific APIs. Whether it’s accessing system information, managing Bluetooth devices, or working with user preferences, **Pyjnius** and **Pyobjus** by Kivy provide a seamless way to bridge Python with Java (for Android) and Objective-C (for iOS).
You can now integrate both Pyjnius and Pyobjus into your Flet apps! 🚀
**Tags:**
  * [news](https://flet.dev/blog/tags/news)


[**Read more**](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus)
## [Flet v0.27.0 Release Announcement](https://flet.dev/blog/flet-v-0-27-release-announcement)
February 20, 2025 · 5 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
Flet 0.27.0 is now released with exciting new features and improvements!
  * **iOS packaging & signing updates** – ensures compliance with App Store Connect verification requirements.
  * **Reduced startup delay** – faster initial launch for desktop applications.
  * **Faster incremental re-builds** – enhances development efficiency with quicker iteration times.
  * **Enhanced Dropdown control** – improved functionality and user experience.
  * **Bug fixes & stability improvements** – various fixes to enhance overall performance and reliability.


**Tags:**
  * [releases](https://flet.dev/blog/tags/releases)


[**Read more**](https://flet.dev/blog/flet-v-0-27-release-announcement)
## [Flet v0.26.0 Release Announcement](https://flet.dev/blog/flet-v-0-26-release-announcement)
January 24, 2025 · 4 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
The Flet 0.26.0 release is here, featuring a significant update to the extensibility approach!
In summary, a Flet extension is now a single Python package that bundles both Python and Flutter code. This package can be part of your Flet project or hosted in a public Git repository or PyPI.
Built-in Flet extensions, such as `Audio`, `Video`, and `Map`, have been moved to their own repositories. You’re welcome to fork these extensions to create your own or contribute to Flet! These extensions have been published to PyPI, making them easy to include in your Flet app. To use them, simply add the desired extensions to the `dependencies` section of your `pyproject.toml` file.
**Tags:**
  * [releases](https://flet.dev/blog/tags/releases)


[**Read more**](https://flet.dev/blog/flet-v-0-26-release-announcement)
## [Flet v0.25.0 Release Announcement](https://flet.dev/blog/flet-v-0-25-release-announcement)
November 27, 2024 · 10 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
Hey Flet developers, we’ve got something exciting to share — Flet 0.25.0 is officially released!
The biggest news? No more Kivy for iOS and Android packaging. No more dealing with frustrating Python binary dependencies — Flet now uses its own custom Python runtime, so your app builds are easier than ever. Plus, we’ve added loads of new features like better permissions control, faster rebuilds, and even a lightweight Linux client that skips the bloat.
Let’s dive into all the cool stuff Flet 0.25.0 has to offer! 🚀
**Tags:**
  * [releases](https://flet.dev/blog/tags/releases)


[**Read more**](https://flet.dev/blog/flet-v-0-25-release-announcement)
[ Older entries](https://flet.dev/blog/page/2)
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
