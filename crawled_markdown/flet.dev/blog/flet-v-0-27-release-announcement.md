[Skip to main content](https://flet.dev/blog/flet-v-0-27-release-announcement/#__docusaurus_skipToContent_fallback)
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


# Flet v0.27.0 Release Announcement
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


## How to upgrade[​](https://flet.dev/blog/flet-v-0-27-release-announcement/#how-to-upgrade "Direct link to How to upgrade")
Run the following command to upgrade Flet:
```
pip install 'flet[all]' --upgrade
```

note
`[all]` is an "extra" specifier which tells pip to install or upgrade all `flet` packages: `flet`, `flet-cli`, `flet-desktop` and `flet-web`.
Bump `flet` package version to `0.27.0` (or remove it at all to use the latest) in your `pyproject.toml`.
## Revamped iOS Packaging[​](https://flet.dev/blog/flet-v-0-27-release-announcement/#revamped-ios-packaging "Direct link to Revamped iOS Packaging")
  * Third-party Flet app dependencies (also known as “site packages” like `numpy`, `pandas`, `flet`, etc.) are now bundled inside a framework, ensuring Xcode signs all files correctly and passes App Store Connect verification.
  * New `flet build` options for proper iOS package signing.
  * Comprehensive step-by-step documentation for packaging and deploying iOS apps. [Learn more!](https://flet.dev/docs/publish/ios)


## Enhanced startup performance for desktop apps[​](https://flet.dev/blog/flet-v-0-27-release-announcement/#enhanced-startup-performance-for-desktop-apps "Direct link to Enhanced startup performance for desktop apps")
Currently, when packaging for macOS, Windows, and Linux, third-party Flet app dependencies (e.g., numpy, pandas, flet, etc.), also known as **site packages** , are bundled inside the app.zip artifact. This can cause a startup delay, sometimes significant, as the app needs to extract the artifact to the user’s file system before launching.
With Flet 0.27.0, site packages are now copied in an **unpacked state** directly into the application bundle instead of being compressed into app.zip. This change significantly reduces the first launch time.
## Faster incremental re-builds[​](https://flet.dev/blog/flet-v-0-27-release-announcement/#faster-incremental-re-builds "Direct link to Faster incremental re-builds")
If certain parts of the build configuration remain unchanged, the `flet build` command attempts to skip or optimize specific build pipeline steps (such as re-installing Flet app dependencies), reducing the overall completion time for consecutive builds.
Faster builds mean happier developers! 😄
## Pyodide 0.27.2[​](https://flet.dev/blog/flet-v-0-27-release-announcement/#pyodide-0272 "Direct link to Pyodide 0.27.2")
Pyodide 0.27.2 is based on Python 3.12 and has some serious performance improvments to foreign function interface (FFI).
Flet now supports Python 3.12 across all packaging platforms.
The next stop is Python 3.13!
## Enhanced `Dropdown` control.[​](https://flet.dev/blog/flet-v-0-27-release-announcement/#enhanced-dropdown-control "Direct link to enhanced-dropdown-control")
Since version 0.27.0, Flet uses [DropdownMenu](https://api.flutter.dev/flutter/material/DropdownMenu-class.html) flutter widget for [Dropdown](https://flet.dev/docs/controls/dropdown) control, which is a Material 3 version of previously used DropdownButton. Additionally to enhanced look and feel, it allows filter the list based on the text input or search one item in the menu list.
![](https://flet.dev/img/docs/controls/dropdown/dropdown-search.gif)
Some properties of previous Dropdown implementation are not available in the new version and were "stubbed" - they will not break your program but don't do anything. See the list of deprecated properties [here](https://flet.dev/docs/controls/dropdown/#deprecated-dropdown-properties-and-events).
Previous version of Dropdown control is available as [`DropdownM2`](https://flet.dev/docs/controls/dropdownm2) control and will be removed in Flet 0.30.0.
## 💥 Breaking changes[​](https://flet.dev/blog/flet-v-0-27-release-announcement/#-breaking-changes "Direct link to 💥 Breaking changes")
### `flet build` command[​](https://flet.dev/blog/flet-v-0-27-release-announcement/#flet-build-command "Direct link to flet-build-command")
  * `--team` option renamed to `--ios-team-id`.
  * `--include-packages` has been removed. Just add extension package into `dependencies` section of your `pyproject.toml` file: <https://flet.dev/docs/extend/built-in-extensions>
  * `--cleanup-on-compile` removed and two new options added to separate cleanup of app and 3rd-party site packages: `--cleanup-app` and `--cleanup-packages`. Two additional options: `--cleanup-app-files` and `--cleanup-package-files` work together with `--cleanup-*` and allow specifying lists of globs to exclude from app and site packages.
  * `tool.flet.build_arch` renamed to `tool.flet.target_arch`.


### Removed `v0.24.0` Deprecations[​](https://flet.dev/blog/flet-v-0-27-release-announcement/#removed-v0240-deprecations "Direct link to removed-v0240-deprecations")
The following items, deprecated in Flet 0.24.0, have been removed: <https://flet.dev/blog/flet-v-0-24-release-announcement#deprecations>
### `CupertinoCheckbox.inactive_color` property[​](https://flet.dev/blog/flet-v-0-27-release-announcement/#cupertinocheckboxinactive_color-property "Direct link to cupertinocheckboxinactive_color-property")
The `inactive_color` property of the [`CupertinoCheckbox`](https://flet.dev/docs/controls/cupertinocheckbox) has been removed in favor of [`fill_color`](https://flet.dev/docs/controls/cupertinocheckbox#fill_color).
## Other changes[​](https://flet.dev/blog/flet-v-0-27-release-announcement/#other-changes "Direct link to Other changes")
The full list of changes can be found in the [CHANGELOG](https://github.com/flet-dev/flet/blob/main/CHANGELOG.md).
### New features[​](https://flet.dev/blog/flet-v-0-27-release-announcement/#new-features "Direct link to New features")
  * feat: `ReorderableListView` Control ([#4865](https://github.com/flet-dev/flet/pull/4865))
  * feat: Implement `Container.dark_theme` property ([#4857](https://github.com/flet-dev/flet/issues/4857))
  * Upgrade to Pyodide 0.27 for `httpx` Support ([#4840](https://github.com/flet-dev/flet/issues/4840))
  * Remove `CupertinoCheckbox.inactive_color` in favor of `fill_color` ([#4837](https://github.com/flet-dev/flet/issues/4837))
  * feat: `flet build`: use Provisioning Profile to sign iOS app archive (`.ipa`), deprecate `--team` option ([#4869](https://github.com/flet-dev/flet/issues/4869))
  * feat: `flet doctor` CLI command ([#4803](https://github.com/flet-dev/flet/pull/4803))
  * feat: implement button themes (for `ElevatedButton`, `OutlinedButton`, `TextButton`, `FilledButton`, `IconButton `) ([#4872](https://github.com/flet-dev/flet/pull/4872))
  * feat: `ControlEvent.data` should be of type `Optional[str]` and default to `None` ([#4786](https://github.com/flet-dev/flet/issues/4786))
  * feat: `flet build`: add `--source-packages` to allow installing certain Python packages from source distros ([#4762](https://github.com/flet-dev/flet/issues/4762))


### Bug fixes[​](https://flet.dev/blog/flet-v-0-27-release-announcement/#bug-fixes "Direct link to Bug fixes")
  * Fixed: Disable rich's Markup for stdout logs ([#4795](https://github.com/flet-dev/flet/issues/4795))
  * Fixed: Setting `SearchBar.bar_border_side` isn't visually honoured ([#4767](https://github.com/flet-dev/flet/issues/4767))
  * Fixed: Dropdown: Long options cause the down-arrow to oveflow ([#4838](https://github.com/flet-dev/flet/issues/4838))
  * Fixed: CupertinoSlider initialisation does not allow values less then zero/greater then 1 ([#4853](https://github.com/flet-dev/flet/issues/4853))
  * Fixed: Same code shows different appearance in Flet APP/Web/PC local. ([#4855](https://github.com/flet-dev/flet/issues/4855))
  * Fixed: Transforming scale renders a grey screen ([#4759](https://github.com/flet-dev/flet/issues/4759))
  * Fixed: UnicodeDecodeError when using accented characters in manifest.json ([#4713](https://github.com/flet-dev/flet/issues/4713))
  * Fixed: Implement `SearchBar.blur()` to programmatically unfocus the bar ([#4827](https://github.com/flet-dev/flet/issues/4827))
  * Fixed: Disable markup for flet-cli stdout logs ([#4796](https://github.com/flet-dev/flet/pull/4796))


## Conclusion[​](https://flet.dev/blog/flet-v-0-27-release-announcement/#conclusion "Direct link to Conclusion")
Upgrade to Flet 0.27.0, test your apps and let us know how you find the new features we added.
If you have any questions, please join [Flet Discord server](https://discord.gg/dzWXP8SHG8) or create a new thread on [Flet GitHub discussions](https://github.com/flet-dev/flet/discussions).
Happy Flet-ing! 👾
**Tags:**
  * [releases](https://flet.dev/blog/tags/releases)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2025-02-20-flet-v-0-27-release-announcement.md)
[Newer postTap into native Android and iOS APIs with Pyjnius and Pyobjus](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus)[Older postFlet v0.26.0 Release Announcement](https://flet.dev/blog/flet-v-0-26-release-announcement)
  * [How to upgrade](https://flet.dev/blog/flet-v-0-27-release-announcement/#how-to-upgrade)
  * [Revamped iOS Packaging](https://flet.dev/blog/flet-v-0-27-release-announcement/#revamped-ios-packaging)
  * [Enhanced startup performance for desktop apps](https://flet.dev/blog/flet-v-0-27-release-announcement/#enhanced-startup-performance-for-desktop-apps)
  * [Faster incremental re-builds](https://flet.dev/blog/flet-v-0-27-release-announcement/#faster-incremental-re-builds)
  * [Pyodide 0.27.2](https://flet.dev/blog/flet-v-0-27-release-announcement/#pyodide-0272)
  * [Enhanced `Dropdown` control.](https://flet.dev/blog/flet-v-0-27-release-announcement/#enhanced-dropdown-control)
  * [💥 Breaking changes](https://flet.dev/blog/flet-v-0-27-release-announcement/#-breaking-changes)
    * [`flet build` command](https://flet.dev/blog/flet-v-0-27-release-announcement/#flet-build-command)
    * [Removed `v0.24.0` Deprecations](https://flet.dev/blog/flet-v-0-27-release-announcement/#removed-v0240-deprecations)
    * [`CupertinoCheckbox.inactive_color` property](https://flet.dev/blog/flet-v-0-27-release-announcement/#cupertinocheckboxinactive_color-property)
  * [Other changes](https://flet.dev/blog/flet-v-0-27-release-announcement/#other-changes)
    * [New features](https://flet.dev/blog/flet-v-0-27-release-announcement/#new-features)
    * [Bug fixes](https://flet.dev/blog/flet-v-0-27-release-announcement/#bug-fixes)
  * [Conclusion](https://flet.dev/blog/flet-v-0-27-release-announcement/#conclusion)


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
