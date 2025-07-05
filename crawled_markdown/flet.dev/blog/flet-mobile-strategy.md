[Skip to main content](https://flet.dev/blog/flet-mobile-strategy/#__docusaurus_skipToContent_fallback)
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


# Flet Mobile Strategy
July 24, 2022 · 4 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
Flet project has received a lot of attention recently and we would like to thank all the developers who tried Flet and have been spreading the word about it in the communities! Your support motivates us to move Flet project forward with faster pace!
New Flet developers are constantly asking if there is a way to package Flet program to an `.apk` file to deploy to Android devices or `.ipa` to deploy to iOS.
In this post I would like to share our vision for Flet going mobile and provide a roadmap.
## Server-Driven UI[​](https://flet.dev/blog/flet-mobile-strategy/#server-driven-ui "Direct link to Server-Driven UI")
Flet is a Server-driven UI (SDUI) framework. SDUI is an emerging technology which is the best described in [Technology Radar post](https://www.thoughtworks.com/en-ca/radar/techniques/server-driven-ui):
> Server-driven UI separates the rendering into a generic container in the mobile app while the structure and data for each view is provided by the server. This means that changes that once required a round trip to an app store can now be accomplished via simple changes to the responses the server sends.
Companies like [DoorDash](https://doordash.engineering/2021/08/24/improving-development-velocity-with-generic-server-driven-ui-components/), [Airbnb](https://medium.com/airbnb-engineering/a-deep-dive-into-airbnbs-server-driven-ui-system-842244c5f5), [Lyft](https://podcasts.apple.com/us/podcast/server-driven-ui-with-kevin-fang-jeff-hurray/id1453587931?i=1000509742062) and others have been successfully implementing Server-driven UI in their mobile apps to reduce time-to-market.
### Flet approach[​](https://flet.dev/blog/flet-mobile-strategy/#flet-approach "Direct link to Flet approach")
Flet is going to implement Server-Driven UI approach where program written in Python or other language is running on the server and only a thin client - either standalone Flutter app (`.apk` or `.ipa` package) in app store or a Flutter widget as a part of another app - is delivered to a mobile:
![](https://flet.dev/img/docs/getting-started/flet-highlevel-diagram.svg)
Once SDUI experience is ready we'll start working on a [standalone mobile package](https://flet.dev/blog/flet-mobile-strategy/#standalone-mobile-package-for-flet-app).
## Roadmap[​](https://flet.dev/blog/flet-mobile-strategy/#roadmap "Direct link to Roadmap")
To provide the best experience for Flet apps on mobile platforms, we plan to release the following items by the end of this year:
### Flet widget for Flutter[​](https://flet.dev/blog/flet-mobile-strategy/#flet-widget-for-flutter "Direct link to Flet widget for Flutter")
The first step we are going to do is to separate Flet client into a Flutter widget and publish the package at <https://pub.dev>. Flet widget could be then integrated by mobile developers into existing or new Flutter apps for adding dynamic server-driven UI experiences to the core app functionality. A new Flutter app could be also created with a single Flet widget just for the purpose of hosting a complete Flet app.
Developers will follow Flutter guide for packaging, signing and distributing their apps to [Android](https://docs.flutter.dev/deployment/android), [iOS](https://docs.flutter.dev/deployment/ios), [Linux](https://docs.flutter.dev/deployment/linux), [macOS](https://docs.flutter.dev/deployment/macos) or [Windows](https://docs.flutter.dev/deployment/windows) platforms.
Flet team will provide sample CI pipelines to automate packaging, signing and publishing of Flutter apps.
### Flet Studio for iOS and Android[​](https://flet.dev/blog/flet-mobile-strategy/#flet-studio-for-ios-and-android "Direct link to Flet Studio for iOS and Android")
The next step is a standalone "Flet Studio" app (the name is not final) in App Store and Google Play for "testing mobile experiences developed with Flet framework". Developers or beta testers will be able to "register" URL of their hosted Flet app within Flet Studio and instantly see how it performs on a mobile device.
### White-labeled Flet mobile app[​](https://flet.dev/blog/flet-mobile-strategy/#white-labeled-flet-mobile-app "Direct link to White-labeled Flet mobile app")
We are going to provide a guide and CI pipeline for automatic publishing of white-labeled Flet app to a user App Store or Google Play account. This app will be "pinned" to a specific app URL and could additionally bundle app assets (media, fonts) to minimize network usage.
### Standalone mobile package for Flet app[​](https://flet.dev/blog/flet-mobile-strategy/#standalone-mobile-package-for-flet-app "Direct link to Standalone mobile package for Flet app")
We are going to investigate the way and develop a prototype for bundling together Flet framework, user program, language runtime and all dependencies into a standalone mobile package (`.apk` or `.ipa` package), so Flet program does not require a web server.
### Embedding Flet into native apps[​](https://flet.dev/blog/flet-mobile-strategy/#embedding-flet-into-native-apps "Direct link to Embedding Flet into native apps")
We are going to provide a guide, sample apps and CI pipeline to integrate Flet widget into existing native Android and iOS apps (not developed with Flutter) using [Flutter Add-to-App](https://docs.flutter.dev/development/add-to-app) feature. [Put Flutter to work](https://medium.com/flutter/put-flutter-to-work-95f5fdcc592e) article gives a real-world example on how to integrate Flutter into existing mobile app.
This is the current plan.
In the meantime, [give Flet a try](https://flet.dev/docs) and [let us know](https://discord.gg/dzWXP8SHG8) what you think!
**Tags:**
  * [product](https://flet.dev/blog/tags/product)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2022-07-24-flet-mobile-strategy.md)
[Newer postControl Refs](https://flet.dev/blog/control-refs)[Older postNavigation and Routing](https://flet.dev/blog/navigation-and-routing)
  * [Server-Driven UI](https://flet.dev/blog/flet-mobile-strategy/#server-driven-ui)
    * [Flet approach](https://flet.dev/blog/flet-mobile-strategy/#flet-approach)
  * [Roadmap](https://flet.dev/blog/flet-mobile-strategy/#roadmap)
    * [Flet widget for Flutter](https://flet.dev/blog/flet-mobile-strategy/#flet-widget-for-flutter)
    * [Flet Studio for iOS and Android](https://flet.dev/blog/flet-mobile-strategy/#flet-studio-for-ios-and-android)
    * [White-labeled Flet mobile app](https://flet.dev/blog/flet-mobile-strategy/#white-labeled-flet-mobile-app)
    * [Standalone mobile package for Flet app](https://flet.dev/blog/flet-mobile-strategy/#standalone-mobile-package-for-flet-app)
    * [Embedding Flet into native apps](https://flet.dev/blog/flet-mobile-strategy/#embedding-flet-into-native-apps)


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
