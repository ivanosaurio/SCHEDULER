[Skip to main content](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#__docusaurus_skipToContent_fallback)
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


# pyproject.toml support for flet build command
October 15, 2024 · 5 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
The number of options for `flet build` command grew substantially over the time and it's been inconvenient to carry all these settings in a command line.
Today, we are excited to announce another Flet pre-release which now allows configuring app build settings in `pyproject.toml`!
## Installing pre-release[​](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#installing-pre-release "Direct link to Installing pre-release")
```
pip install flet==0.25.0.dev3526
```

note
For testing purposes we suggest installing Flet pre-release in a dedicated Python virtual environment.
## Building the app with pre-release[​](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#building-the-app-with-pre-release "Direct link to Building the app with pre-release")
To build your app with `flet build` command and pre-release version of Flet make sure your `requirements.txt` either contains exact version specifier:
```
flet==0.25.0.dev3526
```

or `--pre` flag before `flet` dependency:
```
--preflet
```

## Quick start[​](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#quick-start "Direct link to Quick start")
Create the following minimal `pyproject.toml` file in the root of your Flet app or run `flet create` to create a new app from template:
```
[project]name="my_app"version="1.0.0"description="My first Flet project"authors=[{name="John Smith",email="john@email.com"}]dependencies=["flet==0.25.0.dev3526"]
```

note
With `pyproject.toml`, you no longer need `requirements.txt`. However, if a `requirements.txt` file exists in the app's directory, the flet build command will prioritize reading dependencies from it instead of those listed in `pyproject.toml`.
`[project]` is the standard required section of `project.toml`.
note
Flet also supports `[tool.poetry]` section created by Poetry which contains project settings.
A minimal `pyproject.toml` for Poetry, which is also supported by `flet build` command, is the following:
```
[tool.poetry]name="my_app"version="1.0.0"description="My first Flet project"authors=["John Smith <john@email.com>"][tool.poetry.dependencies]python="^3.10"flet="0.25.0.dev3526"
```

`project.name` (or `tool.poetry.name`) corresponds to `--project` option of `flet build` command and it will be the name of app bundle or executable. The value of `project.name` will be "slugified" where all non-alphanumeric values are replaced with dashes `-`.
`project.version` (or `tool.poetry.version`) corresponds to `--build-version` option and it is a value in "x.y.z" string used as the version number shown to users.
`project.description` (or `tool.poetry.description`) corresponds to `--description` option which is the description to use for executable or bundle.
note
`project.authors` and `tool.poetry.authors` are not used by `flet build`, but required by a standard and other tools.
### Overriding config with CLI options[​](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#overriding-config-with-cli-options "Direct link to Overriding config with CLI options")
All settings in `pyproject.toml` have corresponding `flet build` CLI options. If you run the flet build command and specify options that are already configured in `pyproject.toml`, the CLI option values will override those from the configuration file.
## Project dependencies[​](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#project-dependencies "Direct link to Project dependencies")
List project dependencies in `project.dependencies` section. The value is an array with pip-like requirement specifiers:
```
[project]dependencies = [ "flet==0.25.0.dev3526", "numpy"]
```

## Product information[​](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#product-information "Direct link to Product information")
All Flet specific settings should be put into `[tool.flet]` section and sub-sections below it.
Product information settings complement the ones in `[project]` section and allows configuring app bundle identifier and product display name.
```
[tool.flet]org="com.mycompany"# --orgproduct="Product name"# --productcompany="My Company"# --companycopyright="Copyright (C) 2024 by MyCompany"# --copyrightbuild_number=1# --build-number
```

## App package contents[​](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#app-package-contents "Direct link to App package contents")
The following settings control the contents of Python app archive and compilation of app/packages sources.
```
[tool.flet]app.module="main"# --module-nameapp.path="src"# path to Python app relative to `pyproject.toml`app.exclude=["assets"]# --excludecompile.app=false# --compile-appcompile.packages=false# --compile-packagescompile.cleanup=false# --cleanup-on-compile
```

They could be alternatively written under their own sub-sections as:
```
[tool.flet.app]module="main"path="src"exclude=["assets"][tool.flet.compile]app=falsepackages=falsecleanup=false
```

## Splash[​](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#splash "Direct link to Splash")
```
[tool.flet.splash]color=""# --splash-colordark_color=""# --splash-dark-colorweb=false# --no-web-splashios=false# --no-ios-splashandroid=false# --no-android-splash
```

## Permissions[​](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#permissions "Direct link to Permissions")
```
[tool.flet]permissions=["camera","microphone"]# --permissions
```

## Deep linking[​](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#deep-linking "Direct link to Deep linking")
```
[tool.flet.deep_linking]scheme="https"# --deep-linking-schemehost="mydomain.com"# --deep-linking-host
```

### Android settings[​](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#android-settings "Direct link to Android settings")
```
[tool.flet.android]adaptive_icon_background=""# --android-adaptive-icon-backgroundsplit_per_abi=false# --split-per-abi
```

Permissions (notice quotes `"` around key names):
```
[tool.flet.android.permission]# --android-permissions"android.permission.CAMERA"=true"android.permission.CAMERA"=true
```

Features (notice quotes `"` around key names):
```
[tool.flet.android.feature]# --android-features"android.hardware.camera"=false
```

Android-specific deep-linking:
```
[tool.flet.android.deep_linking]scheme="https"# --deep-linking-schemehost="mydomain.com"# --deep-linking-host
```

Android bundle signing options:
```
[tool.flet.android.signing]# store and key passwords can be passed with `--android-signing-key-store-password`# and `--android-signing-key-password` options or# FLET_ANDROID_SIGNING_KEY_STORE_PASSWORD# and FLET_ANDROID_SIGNING_KEY_PASSWORD environment variables.key_store="path/to/store.jks"# --android-signing-key-storekey_alias="upload"
```

### iOS settings[​](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#ios-settings "Direct link to iOS settings")
```
[tool.flet.ios]team="team_id"# --team[tool.flet.ios.info]# --info-plistNSCameraUsageDescription="This app uses the camera to ..."[tool.flet.ios.info.deep_linking]scheme="https"host="mydomain.com"
```

### macOS settings[​](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#macos-settings "Direct link to macOS settings")
```
[tool.flet.macos]entitlement."com.apple.security.personal-information.photos-library"=true
```

```
[tool.flet]build_arch="arm64"# --arch - if arch is not specified Flet will build universal package for both arm64 and x86_64 archs
```

### Web settings[​](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#web-settings "Direct link to Web settings")
```
[tool.flet.web]base_url="/"# --base-urlrenderer="canvaskit"# --web-rendereruse_color_emoji=false# --use-color-emojiroute_url_strategy="path"# --route-url-strategy
```

## Flutter settings[​](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#flutter-settings "Direct link to Flutter settings")
### Dependencies[​](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#dependencies "Direct link to Dependencies")
```
flutter.dependencies=["flet_video","flet_audio"]# --include-packages
```

or with alternative syntax with versions:
```
[tool.flet.flutter.dependencies]flet_video="1.0.0"flet_audio="2.0.0"
```

or with path to the package on your disk:
```
[tool.flet.flutter.dependencies.my_package]path="/path/to/my_package"
```

### Extra build args[​](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#extra-build-args "Direct link to Extra build args")
flutter.build_args = ["--some-flutter-arg"] # --flutter-build-args
### Extra `pubspec.yaml` settings[​](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#extra-pubspecyaml-settings "Direct link to extra-pubspecyaml-settings")
Allows injecting arbitrary content into resulting `pubspec.yaml`, for example:
```
[tool.flet.flutter.pubspec.dependency_overrides]web="1.0.0"
```

## Custom template[​](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#custom-template "Direct link to Custom template")
```
[tool.flet.template]path="gh:some-github/repo"# --templatedir=""# --template-dirref=""# --template-ref
```

That's it! Upgrade to Flet 0.25.0.dev3526, give this new feature and try and let us know what you think!
Cheers!
[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2024-10-15-pyproject-toml-support-for-flet-build-command.md)
[Newer postFlet v0.25.0 Release Announcement](https://flet.dev/blog/flet-v-0-25-release-announcement)[Older postFlet new packaging pre-release](https://flet.dev/blog/flet-new-packaging-pre-release)
  * [Installing pre-release](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#installing-pre-release)
  * [Building the app with pre-release](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#building-the-app-with-pre-release)
  * [Quick start](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#quick-start)
    * [Overriding config with CLI options](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#overriding-config-with-cli-options)
  * [Project dependencies](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#project-dependencies)
  * [Product information](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#product-information)
  * [App package contents](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#app-package-contents)
  * [Splash](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#splash)
  * [Permissions](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#permissions)
  * [Deep linking](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#deep-linking)
    * [Android settings](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#android-settings)
    * [iOS settings](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#ios-settings)
    * [macOS settings](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#macos-settings)
    * [Web settings](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#web-settings)
  * [Flutter settings](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#flutter-settings)
    * [Dependencies](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#dependencies)
    * [Extra build args](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#extra-build-args)
    * [Extra `pubspec.yaml` settings](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#extra-pubspecyaml-settings)
  * [Custom template](https://flet.dev/blog/pyproject-toml-support-for-flet-build-command/#custom-template)


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
