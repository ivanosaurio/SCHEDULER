[Skip to main content](https://flet.dev/blog/flet-new-packaging-pre-release/#__docusaurus_skipToContent_fallback)
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


# Flet new packaging pre-release
October 10, 2024 · 8 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
Flet packaging for iOS and Android has been relying on Kivy and it was super annoying when your app depends on Python binary packages, such as Numpy or Pillow. You needed to compile those packages yourself using Kivy command line tools. It was really frustrating and even hopeless if Kivy didn't have "recipes" for some packages, like Pydantic.
Kivy no more! We've just published Flet 0.25.0.dev3519 pre-release with the improved `flet build` command which does not use Kivy! Flet is now using its own Python runtime "meticulously crafted in-house".
Flet packaging implementation for iOS and Androind adheres to strict specifications defined in [PEP 730](https://peps.python.org/pep-0730/) (iOS) and [PEP 738](https://peps.python.org/pep-0738/) (Android) which were implemented and released in Python 3.13 (and back-ported to Python 3.12). When pypi.org supports wheel tags for iOS and Android and 3rd-party Python package maintainers start uploading their mobile packages Flet will be compatible with them and you'll be able to use them in your Flet app.
## Installing pre-release[​](https://flet.dev/blog/flet-new-packaging-pre-release/#installing-pre-release "Direct link to Installing pre-release")
```
pip install flet==0.25.0.dev3519
```

note
For testing purposes we suggest installing Flet pre-release in a dedicated Python virtual environment.
## Building the app with pre-release[​](https://flet.dev/blog/flet-new-packaging-pre-release/#building-the-app-with-pre-release "Direct link to Building the app with pre-release")
To build your app with `flet build` command and pre-release version of Flet make sure your `requirements.txt` either contains exact version specifier:
```
flet==0.25.0.dev3519
```

or `--pre` flag before `flet` dependency:
```
--preflet
```

## Python 3.12[​](https://flet.dev/blog/flet-new-packaging-pre-release/#python-312 "Direct link to Python 3.12")
Packaged Flet app runs on Python 3.12.6 runtime for all platforms.
## Pre-built binary packages[​](https://flet.dev/blog/flet-new-packaging-pre-release/#pre-built-binary-packages "Direct link to Pre-built binary packages")
`flet build` command for iOS and Android is now installing pre-built binary packages from <https://pypi.flet.dev>.
New packages can be built with creating a recipe in [Mobile Forge](https://github.com/flet-dev/mobile-forge) project. For now, Flet team is authoring those recipes for you, but when the process is polished and fully-automated you'll be able to send a PR and test the compiled package right away.
If you don't yet see a package at <https://pypi.flet.dev> you can request it in [Flet discussions - Packages](https://github.com/flet-dev/flet/discussions/categories/packages). Please do not request pure Python packages. Go to package's "Download files" section at <https://pypi.org> and make sure it contains binary platform-specific wheels.
Packaging behavior was changed too:
  * The packaging is not trying to replace `flet` dependency with `flet-runtime`, `flet-embed` or `flet-pyodide`, but install all dependencies "as is" from `requirements.txt` or `pyproject.toml` - thanks to the new Flet packages structure (link).
  * If the binary package for target platform is not found the packaging won't be trying to compile it from source distribution, but will fail instead with a meaningful error.


## New packages structure[​](https://flet.dev/blog/flet-new-packaging-pre-release/#new-packages-structure "Direct link to New packages structure")
The structure avoids rewriting pip dependencies while installing `flet` package on various platforms. There was a problem of detecting the correct `flet` package to install (`flet-runtime`, `flet-embed` or`flet-pyodide`?) if `flet` was not a direct dependency in user's app.
New Flet packages:
  * `flet` - required for minimal Flet setup, app entry point for various platforms. Installed on all platforms.
  * `flet-core` - required for minimal Flet setup, core logic and controls. Installed on all platforms.
  * `flet-cli` - contains Flet CLI commands. Installed on desktop only.
  * `flet-desktop` - contains pre-built Flet "client" app binary for macOS, Windows and Linux. By default installed on macOS and Windows desktops only.
  * `flet-desktop-light` - contains a light-weight version (without Audio and Video controls) of Flet "client" for Linux. By default installed on Linux desktops only.
  * `flet-web` - contains Flet web "client" and FastAPI integration. Installed on desktop only.


Other words, packaged Flet app contains only `flet` and `flet-core` packages.
### "Light" client for Linux[​](https://flet.dev/blog/flet-new-packaging-pre-release/#light-client-for-linux "Direct link to "Light" client for Linux")
A light-weight desktop client, without Audio and Video controls, is not installed on Linux by default. It improves initial user experience as user doesn't need to immediately deal with gstreamer (audio) and mpv (video) dependencies right away and Flet "just works".
Once user got some Flet experience and wants to use Video and Audio controls in their application they can install gstreamer and/or mpv and replace Flet desktop with a full version.
Uninstall "light" Flet client:
```
pip uninstall flet-desktop-light --yes
```

Install full Flet desktop client:
```
pip install flet-desktop==0.25.0.dev3519
```

## Permissions[​](https://flet.dev/blog/flet-new-packaging-pre-release/#permissions "Direct link to Permissions")
New `flet build` command allows granular control over permissions, features and entitlements embedded into `AndroidManifest.xml`, `Info.plist` and `.entitlements` files.
No more hard-coded permissions in those files!
### iOS[​](https://flet.dev/blog/flet-new-packaging-pre-release/#ios "Direct link to iOS")
Setting iOS permissions:
```
flet build --info-plist permission_1=True|False|description permission_2=True|False|description ...
```

For example:
```
flet build --info-plist NSLocationWhenInUseUsageDescription=This app uses location service when in use.
```

### macOS[​](https://flet.dev/blog/flet-new-packaging-pre-release/#macos "Direct link to macOS")
Setting macOS entitlements:
```
flet build --macos-entitlements name_1=True|False name_2=True|False ...
```

Default macOS entitlements:
  * `com.apple.security.app-sandbox = False`
  * `com.apple.security.cs.allow-jit = True`
  * `com.apple.security.network.client = True`
  * `com.apple.security.network.server" = True`


### Android[​](https://flet.dev/blog/flet-new-packaging-pre-release/#android "Direct link to Android")
Setting Android permissions and features:
```
flet build --android-permissions permission=True|False ... --android-features feature_name=True|False
```

For example:
```
flet build \  --android-permissions android.permission.READ_EXTERNAL_STORAGE=True \   android.permission.WRITE_EXTERNAL_STORAGE=True \  --android-features android.hardware.location.network=False
```

Default Android permissions:
  * `android.permission.INTERNET`


Default permissions can be disabled with `--android-permissions` option and `False` value, for example:
```
flet build --android-permissions android.permission.INTERNET=False
```

Default Android features:
  * `android.software.leanback=False` (`False` means it's written in manifest as `android:required="false"`)
  * `android.hardware.touchscreen=False`


### Cross-platform permission groups[​](https://flet.dev/blog/flet-new-packaging-pre-release/#cross-platform-permission-groups "Direct link to Cross-platform permission groups")
There are pre-defined permissions that mapped to `Info.plist`, `*.entitlements` and `AndroidManifest.xml` for respective platforms.
Setting cross-platform permissions:
```
flet build --permissions permission_1 permission_2 ...
```

Supported permissions:
  * `location`
  * `camera`
  * `microphone`
  * `photo_library`


#### iOS mapping to `Info.plist` entries[​](https://flet.dev/blog/flet-new-packaging-pre-release/#ios-mapping-to-infoplist-entries "Direct link to ios-mapping-to-infoplist-entries")
  * `location`
    * `NSLocationWhenInUseUsageDescription = This app uses location service when in use.`
    * `NSLocationAlwaysAndWhenInUseUsageDescription = This app uses location service.`
  * `camera`
    * `NSCameraUsageDescription = This app uses the camera to capture photos and videos.`
  * `microphone`
    * `NSMicrophoneUsageDescription = This app uses microphone to record sounds.`
  * `photo_library`
    * `NSPhotoLibraryUsageDescription = This app saves photos and videos to the photo library.`


#### macOS mapping to entitlements[​](https://flet.dev/blog/flet-new-packaging-pre-release/#macos-mapping-to-entitlements "Direct link to macOS mapping to entitlements")
  * `location`
    * `com.apple.security.personal-information.location = True`
  * `camera`
    * `com.apple.security.device.camera = True`
  * `microphone`
    * `com.apple.security.device.audio-input = True`
  * `photo_library`
    * `com.apple.security.personal-information.photos-library = True`


#### Android mappings[​](https://flet.dev/blog/flet-new-packaging-pre-release/#android-mappings "Direct link to Android mappings")
  * `location`
    * permissions: 
      * `android.permission.ACCESS_FINE_LOCATION": True`
      * `android.permission.ACCESS_COARSE_LOCATION": True`
      * `android.permission.ACCESS_BACKGROUND_LOCATION": True`
    * features: 
      * `android.hardware.location.network": False`
      * `android.hardware.location.gps": False`
  * `camera`
    * permissions: 
      * `android.permission.CAMERA": True`
    * features: 
      * `android.hardware.camera": False`
      * `android.hardware.camera.any": False`
      * `android.hardware.camera.front": False`
      * `android.hardware.camera.external": False`
      * `android.hardware.camera.autofocus": False`
  * `microphone`
    * permissions: 
      * `android.permission.RECORD_AUDIO": True`
      * `android.permission.WRITE_EXTERNAL_STORAGE": True`
      * `android.permission.READ_EXTERNAL_STORAGE": True`
  * `photo_library`
    * permissions: 
      * `android.permission.READ_MEDIA_VISUAL_USER_SELECTED": True`


## Control over app compilation and cleanup[​](https://flet.dev/blog/flet-new-packaging-pre-release/#control-over-app-compilation-and-cleanup "Direct link to Control over app compilation and cleanup")
`flet build` command is no longer compiling app `.py` files into `.pyc` by default which allows you to avoid (defer?) discovery of any syntax errors in your app and complete the packaging.
You can control the compilation and cleanup with the following new options:
  * `--compile-app` - compile app's `.py` files.
  * `--compile-packages` - compile installed packages' `.py` files.
  * `--cleanup-on-compile` - remove unnecessary files upon successful compilation.


## Signing Android bundles[​](https://flet.dev/blog/flet-new-packaging-pre-release/#signing-android-bundles "Direct link to Signing Android bundles")
Added new options for signing Android builds:
  * `--android-signing-key-store` - path to an upload keystore `.jks` file for Android apps.
  * `--android-signing-key-store-password` - Android signing store password.
  * `--android-signing-key-alias` - Android signing key alias. Default is "upload".
  * `--android-signing-key-password` - Android signing key password.


Read [Build and release an Android app](https://docs.flutter.dev/deployment/android#signing-the-app) for more information on how to configure upload key for Android builds.
## "Data" and "Temp" directories for the app[​](https://flet.dev/blog/flet-new-packaging-pre-release/#data-and-temp-directories-for-the-app "Direct link to "Data" and "Temp" directories for the app")
Flet developers have been asking where to store application data, such as uploaded files, SQLite databases, etc. that are persistent across application updates.
This release introduce two environment variables that are available in your Flet apps:
  * `FLET_APP_STORAGE_DATA` - directory for storing application data that is preserved between app updates. That directory is already pre-created.
  * `FLET_APP_STORAGE_TEMP` - directory for temporary application files, i.e. cache. That directory is already pre-created.


For example, data folder path can be read in your app as:
```
import os# it's `None` when running the app in web modedata_dir = os.getenv("FLET_APP_STORAGE_DATA")
```

note
`flet run` command creates data and temp directories and sets `FLET_APP_STORAGE_DATA` and `FLET_APP_STORAGE_TEMP` to their paths.
## Deep linking configuration[​](https://flet.dev/blog/flet-new-packaging-pre-release/#deep-linking-configuration "Direct link to Deep linking configuration")
There is a new `--deep-linking-url` option to configure deep linking for iOS and Android builds. The value must be in the format `<sheme>://<host>`.
## Faster re-builds[​](https://flet.dev/blog/flet-new-packaging-pre-release/#faster-re-builds "Direct link to Faster re-builds")
Ephemeral Flutter app created by `flet build` command is not re-created all the time in a temp directory, but cached in `build/flutter` directory which gives faster re-builds, improves packaging troubleshooting and does not pollute temp directory.
## Split APKs per ABI[​](https://flet.dev/blog/flet-new-packaging-pre-release/#split-apks-per-abi "Direct link to Split APKs per ABI")
`flet build` now provides the built-in `--split-per-abi` option to split the APKs per ABIs.
## Known pre-release issues[​](https://flet.dev/blog/flet-new-packaging-pre-release/#known-pre-release-issues "Direct link to Known pre-release issues")
  * `flet publish` is not yet working.


## What else coming in the release[​](https://flet.dev/blog/flet-new-packaging-pre-release/#what-else-coming-in-the-release "Direct link to What else coming in the release")
We would like to include a few more things into Flet 0.25.0 release. Expect more pre-releases in the coming weeks.
### `pyproject.toml` support[​](https://flet.dev/blog/flet-new-packaging-pre-release/#pyprojecttoml-support "Direct link to pyprojecttoml-support")
It's inconvenient and bulky to carry all `flet build` settings as command line options.
You will be able to store project and build settings in `[tool.flet]` section of `pyproject.toml`.
### Running Flet app on simulator[​](https://flet.dev/blog/flet-new-packaging-pre-release/#running-flet-app-on-simulator "Direct link to Running Flet app on simulator")
We will add an option to `flet build` and run packaged app on a real device or simulator.
### Installing Flutter[​](https://flet.dev/blog/flet-new-packaging-pre-release/#installing-flutter "Direct link to Installing Flutter")
`flet build` will download and configure Flutter for you if there is no suitable installation available on your machine.
[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2024-10-10-flet-new-packaging-pre-release.md)
[Newer postpyproject.toml support for flet build command](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command)[Older postFlet v0.24.0 Release Announcement](https://flet.dev/blog/flet-v-0-24-release-announcement)
  * [Installing pre-release](https://flet.dev/blog/flet-new-packaging-pre-release/#installing-pre-release)
  * [Building the app with pre-release](https://flet.dev/blog/flet-new-packaging-pre-release/#building-the-app-with-pre-release)
  * [Python 3.12](https://flet.dev/blog/flet-new-packaging-pre-release/#python-312)
  * [Pre-built binary packages](https://flet.dev/blog/flet-new-packaging-pre-release/#pre-built-binary-packages)
  * [New packages structure](https://flet.dev/blog/flet-new-packaging-pre-release/#new-packages-structure)
    * ["Light" client for Linux](https://flet.dev/blog/flet-new-packaging-pre-release/#light-client-for-linux)
  * [Permissions](https://flet.dev/blog/flet-new-packaging-pre-release/#permissions)
    * [iOS](https://flet.dev/blog/flet-new-packaging-pre-release/#ios)
    * [macOS](https://flet.dev/blog/flet-new-packaging-pre-release/#macos)
    * [Android](https://flet.dev/blog/flet-new-packaging-pre-release/#android)
    * [Cross-platform permission groups](https://flet.dev/blog/flet-new-packaging-pre-release/#cross-platform-permission-groups)
  * [Control over app compilation and cleanup](https://flet.dev/blog/flet-new-packaging-pre-release/#control-over-app-compilation-and-cleanup)
  * [Signing Android bundles](https://flet.dev/blog/flet-new-packaging-pre-release/#signing-android-bundles)
  * ["Data" and "Temp" directories for the app](https://flet.dev/blog/flet-new-packaging-pre-release/#data-and-temp-directories-for-the-app)
  * [Deep linking configuration](https://flet.dev/blog/flet-new-packaging-pre-release/#deep-linking-configuration)
  * [Faster re-builds](https://flet.dev/blog/flet-new-packaging-pre-release/#faster-re-builds)
  * [Split APKs per ABI](https://flet.dev/blog/flet-new-packaging-pre-release/#split-apks-per-abi)
  * [Known pre-release issues](https://flet.dev/blog/flet-new-packaging-pre-release/#known-pre-release-issues)
  * [What else coming in the release](https://flet.dev/blog/flet-new-packaging-pre-release/#what-else-coming-in-the-release)
    * [`pyproject.toml` support](https://flet.dev/blog/flet-new-packaging-pre-release/#pyprojecttoml-support)
    * [Running Flet app on simulator](https://flet.dev/blog/flet-new-packaging-pre-release/#running-flet-app-on-simulator)
    * [Installing Flutter](https://flet.dev/blog/flet-new-packaging-pre-release/#installing-flutter)


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
