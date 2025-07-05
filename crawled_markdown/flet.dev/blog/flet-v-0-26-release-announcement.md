[Skip to main content](https://flet.dev/blog/flet-v-0-26-release-announcement/#__docusaurus_skipToContent_fallback)
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


# Flet v0.26.0 Release Announcement
January 24, 2025 · 4 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
The Flet 0.26.0 release is here, featuring a significant update to the extensibility approach!
In summary, a Flet extension is now a single Python package that bundles both Python and Flutter code. This package can be part of your Flet project or hosted in a public Git repository or PyPI.
Built-in Flet extensions, such as `Audio`, `Video`, and `Map`, have been moved to their own repositories. You’re welcome to fork these extensions to create your own or contribute to Flet! These extensions have been published to PyPI, making them easy to include in your Flet app. To use them, simply add the desired extensions to the `dependencies` section of your `pyproject.toml` file.
## How to upgrade[​](https://flet.dev/blog/flet-v-0-26-release-announcement/#how-to-upgrade "Direct link to How to upgrade")
Run the following command to upgrade Flet:
```
pip install 'flet[all]' --upgrade
```

note
`[all]` is an "extra" specifier which tells pip to install or upgrade all `flet` packages: `flet`, `flet-cli`, `flet-desktop` and `flet-web`.
Bump `flet` package version to `0.26.0` (or remove it at all to use the latest) in your `pyproject.toml`.
## Extensibility changes[​](https://flet.dev/blog/flet-v-0-26-release-announcement/#extensibility-changes "Direct link to Extensibility changes")
### Built-in extensions[​](https://flet.dev/blog/flet-v-0-26-release-announcement/#built-in-extensions "Direct link to Built-in extensions")
Flet controls based on 3rd-party Flutter packages that used to be a part of Flet repository, now have been moved to separate repos and published on pypi:
  * [flet-ads](https://pypi.org/project/flet-ads/)
  * [flet-audio](https://pypi.org/project/flet-audio/)
  * [flet-audio-recorder](https://pypi.org/project/flet-audio-recorder/)
  * [flet-flashlight](https://pypi.org/project/flet-flashlight/)
  * [flet-geolocator](https://pypi.org/project/flet-geolocator/)
  * [flet-lottie](https://pypi.org/project/flet-lottie/)
  * [flet-map](https://pypi.org/project/flet-map/)
  * [flet-permission-handler](https://pypi.org/project/flet-permission-handler/)
  * [flet-rive](https://pypi.org/project/flet-rive/)
  * [flet-video](https://pypi.org/project/flet-video/)
  * [flet-webview](https://pypi.org/project/flet-webview/)


To use a built-in Flet extension in your project, add it to the `dependencies` section of your `pyproject.toml` file, for example:
```
dependencies = [ "flet-audio", "flet>=0.26.0",]
```

### User extensions[​](https://flet.dev/blog/flet-v-0-26-release-announcement/#user-extensions "Direct link to User extensions")
Flet now makes it easy to create and build projects with your custom controls based on Flutter widgets or Flutter 3rd-party packages:
  1. Create new virtual enviroment and [install Flet](https://flet.dev/docs/getting-started/#virtual-environment) there.
  2. Create new Flet extension project from template:


```
flet create --template extension --project-name my-control
```

A project with new MyControl control will be created. The control is just a Flutter Text widget with a single `text` property.
  1. Build your app.


Flet project created from extension template has `examples/my_control_example` folder with the example app.
When in the folder where your `pyproject.toml` for the app is, run `flet build` command, for example, for macOS:
```
flet build macos -v
```

Run the app and see the new custom Flet Control:
```
open build/macos/my-control-example.app
```

![](https://flet.dev/img/blog/extensions/example.png)
Read more about how to customise your extension [here](https://flet.dev/docs/extend/user-extensions).
## Development environment configuration[​](https://flet.dev/blog/flet-v-0-26-release-announcement/#development-environment-configuration "Direct link to Development environment configuration")
To enhance the developer experience with the `flet build` command, Flet 0.26.0 ensures that the correct versions of Flutter SDK, Java (JDK), and Android SDK are installed. If any of these are missing or outdated, it automatically installs them for you.
You still need to install Visual Studio 2022 yourself if you're building a Flet app for Windows, or Xcode if you're building for iOS or macOS.
In the next releases we are going to introduce automatic configuration and startup of Android and iOS emulators.
## Flutter 3.27[​](https://flet.dev/blog/flet-v-0-26-release-announcement/#flutter-327 "Direct link to Flutter 3.27")
Flet has been migrated to Flutter SDK 3.27. See [this pull request](https://github.com/flet-dev/flet/pull/4703) for new and updated control properties.
## Python 3.9[​](https://flet.dev/blog/flet-v-0-26-release-announcement/#python-39 "Direct link to Python 3.9")
Flet 0.26.0 requires Python 3.9 or later. Python 3.8 has reached [EOL](https://devguide.python.org/versions/).
## Other changes[​](https://flet.dev/blog/flet-v-0-26-release-announcement/#other-changes "Direct link to Other changes")
  * Optional on-demand creation of `ListView.controls` ([#3931](https://github.com/flet-dev/flet/issues/3931))
  * Reset `InteractiveViewer` tranformations ([#4391](https://github.com/flet-dev/flet/issues/4391))
  * Passthrough of mouse events from main window to other applications ([#1438](https://github.com/flet-dev/flet/issues/1438))
  * Implemented `Window.ignore_mouse_events` ([#4465](https://github.com/flet-dev/flet/pull/4465))
  * Adding Google/Android TV platform support ([#4581](https://github.com/flet-dev/flet/pull/4581))
  * Remove `Optional[]` from predefined typing `*Value`s ([#4702](https://github.com/flet-dev/flet/pull/4702))
  * Throttle `InteractiveViewer` update events ([#4704](https://github.com/flet-dev/flet/pull/4704))
  * Remove v0.26.0-related deprecations ([#4456](https://github.com/flet-dev/flet/issues/4456))


## Bug fixes[​](https://flet.dev/blog/flet-v-0-26-release-announcement/#bug-fixes "Direct link to Bug fixes")
  * Fixed: Update project_dependencies.py ([#4459](https://github.com/flet-dev/flet/pull/4459))
  * Fixed: `SafeArea` object has no attribute `_SafeArea__minimum` ([#4500](https://github.com/flet-dev/flet/pull/4500))
  * Fixed: Tooltip corruption in `Segment` and `BarChartRod` on `update()` ([#4525](https://github.com/flet-dev/flet/pull/4525))
  * Fixed: Setting `CheckBox.border_side.stroke_align` to an Enum fails ([#4526](https://github.com/flet-dev/flet/pull/4526))
  * Fixed: `ControlState` should be resolved based on user-defined order ([#4556](https://github.com/flet-dev/flet/pull/4556))
  * Fixed: broken `Dismissible.dismiss_direction` ([#4557](https://github.com/flet-dev/flet/pull/4557))
  * Fixed: Fix Rive not updating ([#4582](https://github.com/flet-dev/flet/pull/4582))
  * Fixed: `DatePicker` regression with first and last dates ([#4661](https://github.com/flet-dev/flet/pull/4661))
  * `flet build` command: Copy `flutter-packages`, support for platform-specific dependencies ([#4667](https://github.com/flet-dev/flet/pull/4667))
  * Fixed: `CupertinoBottomSheet` applies a red color and yellow underline to `Text` content ([#4673](https://github.com/flet-dev/flet/pull/4673))
  * Fixed: setting `ButtonTheme` displays a grey screen ([#4731](https://github.com/flet-dev/flet/pull/4731))
  * Fixed: `Textfield` input border color considers user-specified `border_color` property ([#4735](https://github.com/flet-dev/flet/pull/4735))
  * Fixed: make `Tooltip.message` a required parameter ([#4736](https://github.com/flet-dev/flet/pull/4736))


## Conclusion[​](https://flet.dev/blog/flet-v-0-26-release-announcement/#conclusion "Direct link to Conclusion")
Upgrade to Flet 0.26.0, test your apps and let us know how you find the new features we added.
If you have any questions, please join [Flet Discord server](https://discord.gg/dzWXP8SHG8) or create a new thread on [Flet GitHub discussions](https://github.com/flet-dev/flet/discussions).
Happy Flet-ing! 👾
**Tags:**
  * [releases](https://flet.dev/blog/tags/releases)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2025-01-24-flet-v-0-26-release-announcement.md)
[Newer postFlet v0.27.0 Release Announcement](https://flet.dev/blog/flet-v-0-27-release-announcement)[Older postFlet v0.25.0 Release Announcement](https://flet.dev/blog/flet-v-0-25-release-announcement)
  * [How to upgrade](https://flet.dev/blog/flet-v-0-26-release-announcement/#how-to-upgrade)
  * [Extensibility changes](https://flet.dev/blog/flet-v-0-26-release-announcement/#extensibility-changes)
    * [Built-in extensions](https://flet.dev/blog/flet-v-0-26-release-announcement/#built-in-extensions)
    * [User extensions](https://flet.dev/blog/flet-v-0-26-release-announcement/#user-extensions)
  * [Development environment configuration](https://flet.dev/blog/flet-v-0-26-release-announcement/#development-environment-configuration)
  * [Flutter 3.27](https://flet.dev/blog/flet-v-0-26-release-announcement/#flutter-327)
  * [Python 3.9](https://flet.dev/blog/flet-v-0-26-release-announcement/#python-39)
  * [Other changes](https://flet.dev/blog/flet-v-0-26-release-announcement/#other-changes)
  * [Bug fixes](https://flet.dev/blog/flet-v-0-26-release-announcement/#bug-fixes)
  * [Conclusion](https://flet.dev/blog/flet-v-0-26-release-announcement/#conclusion)


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
