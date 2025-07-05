[Skip to main content](https://flet.dev/blog/flet-adaptive-and-custom-controls/#__docusaurus_skipToContent_fallback)
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


# Flet adaptive UI and custom controls release
February 14, 2024 · 3 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
🥰 Happy Valentine's Day lovely people! 🥰
We just released Flet 0.20.0 with the focus on:
  1. Adaptive UI.
  2. Extending Flet apps with 3rd-party Flutter packages.
  3. New controls: [`Video`](https://flet.dev/docs/controls/video) (yay!), [`AudioRecorder`](https://flet.dev/docs/controls/audiorecorder) and a bunch of `Cupertino`-like controls. Flet now includes 97 built-in controls!


warning
Flet 0.20.0 includes a new [`Video`](https://flet.dev/docs/controls/video) control. While macOS and Windows already include all required media libraries to test Flet apps on Linux, the [libmpv](https://mpv.io/) package must be installed. On Ubuntu/Debian in can be installed with:
```
sudo apt install libmpv-dev mpv
```

## Adaptive UI[​](https://flet.dev/blog/flet-adaptive-and-custom-controls/#adaptive-ui "Direct link to Adaptive UI")
Adaptive controls allow writing apps with a single code base which look and behave differently depending on the platform they are running on.
To the date Flet provides 11 adaptive controls. To make control adaptive you should set its `adaptive` property to `True`.
In Flet 0.20.0 we introduce `adaptive` property to all container-alike controls. Setting `adaptive=True` on a container propagates this property to all child adaptive controls.
Page adds `design` property which enables granular control over controls design language and can have the following values: `ft.PageDesign.ADAPTIVE`, `ft.PageDesign.MATERIAL` or `ft.PageDesign.CUPERTINO`.
By setting just `page.design = ft.PageDesign.ADAPTIVE` you can make you app looking awesome on both iOS and Android devices:
### iPhone
![](https://flet.dev/img/blog/adaptive/iphone-adaptive-app.png)
### Android
![](https://flet.dev/img/blog/adaptive/android-adaptive-app.png)
## Integrating existing Flutter packages[​](https://flet.dev/blog/flet-adaptive-and-custom-controls/#integrating-existing-flutter-packages "Direct link to Integrating existing Flutter packages")
Today Flet offers almost 100 controls, but, as you can imagine, not every Flutter library/widget could be added to the core Flet library and Flet team couldn't do that alone in the acceptable timeframe.
At the same time we do not want to put early adopters, who chose Flet to build their next commercial or corporate app, into a situation where their progress depends on Flet team availability and desire to implement a Flutter control they need.
In Flet 0.20.0 we re-factored Flutter core packages and identified the API that can be used by 3rd-party developers to add their own Flet controls written in Dart.
We are currently working on API docs, but you can learn now how custom Flutter packages are implemented by looking at Dart sources for [`Video`](https://github.com/flet-dev/flet/tree/main/packages/flet_video), and [`Audio`](https://github.com/flet-dev/flet/tree/main/packages/flet_audio) controls.
In short, you have to create a new Flutter package which implements and exports two methods:
```
voidensureInitialized();WidgetcreateControl(CreateControlArgs args);
```

See [`ensureInitialized()`](https://github.com/flet-dev/flet/blob/main/packages/flet_video/lib/src/create_control.dart#L16-L18) and [`createControl()`](https://github.com/flet-dev/flet/blob/main/packages/flet_video/lib/src/create_control.dart#L6-L14) implementations for `Video` control.
On Python side you create a new class inherited from `Control` (non-visual or overlay controls) or `ConstrainedControl`.
See [`Video`](https://github.com/flet-dev/flet/blob/main/sdk/python/packages/flet-core/src/flet_core/video.py#L44) class implementation in Python.
To integrate a custom Flutter package while building your Flet app with `flet build` command you can list extra packages with either `--include-packages` option or in `pubspec.yaml` file put into root of your Flet app.
## `Video` control[​](https://flet.dev/blog/flet-adaptive-and-custom-controls/#video-control "Direct link to video-control")
`Video` control is implemented in a separate Flutter package.
To build your Flet app with `Video` control add `--include-packages flet_video` to your `flet build` command, for example:
```
flet build apk --include-packages flet_video
```

Flet 0.20.0 is a relatively ["large" release](https://github.com/flet-dev/flet/blob/main/CHANGELOG.md#0200) and could break some things.
Upgrade to Flet 0.20.0, test your apps and let us know what you think by joining [Flet Discord server](https://discord.gg/dzWXP8SHG8) or creating a new thread on [Flet GitHub discussions](https://github.com/flet-dev/flet/discussions).
Enjoy!
**Tags:**
  * [releases](https://flet.dev/blog/tags/releases)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2024-02-14-flet-adaptive-and-custom-controls.md)
[Newer postFlet FastAPI and async API improvements](https://flet.dev/blog/flet-fastapi-and-async-api-improvements)[Older postPackaging apps for distribution](https://flet.dev/blog/packaging-apps-for-distribution)
  * [Adaptive UI](https://flet.dev/blog/flet-adaptive-and-custom-controls/#adaptive-ui)
  * [Integrating existing Flutter packages](https://flet.dev/blog/flet-adaptive-and-custom-controls/#integrating-existing-flutter-packages)
  * [`Video` control](https://flet.dev/blog/flet-adaptive-and-custom-controls/#video-control)


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
