[Skip to main content](https://flet.dev/docs/publish/macos/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
    * [Android](https://flet.dev/docs/publish/android)
    * [iOS](https://flet.dev/docs/publish/ios)
    * [macOS](https://flet.dev/docs/publish/macos)
    * [Linux](https://flet.dev/docs/publish/linux)
    * [Windows](https://flet.dev/docs/publish/windows)
    * [Web](https://flet.dev/docs/publish/web)
  * [Extending Flet](https://flet.dev/docs/publish/macos/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/publish/macos/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * macOS


On this page
# Packaging app for macOS
Flet CLI provides `flet build macos` command that allows packaging Flet app into a macOS application bundle.
note
The command can be run on macOS only.
## Prerequisites[​](https://flet.dev/docs/publish/macos/#prerequisites "Direct link to Prerequisites")
### Rosetta 2[​](https://flet.dev/docs/publish/macos/#rosetta-2 "Direct link to Rosetta 2")
Flutter requires [Rosetta 2](https://support.apple.com/en-us/HT211861) on Apple silicon:
```
sudo softwareupdate --install-rosetta --agree-to-license
```

### Xcode[​](https://flet.dev/docs/publish/macos/#xcode "Direct link to Xcode")
[Xcode](https://developer.apple.com/xcode/) 15 or later to compile native Swift or ObjectiveC code.
### CocoaPods[​](https://flet.dev/docs/publish/macos/#cocoapods "Direct link to CocoaPods")
[CocoaPods](https://cocoapods.org/) 1.16 to compile and enable Flutter plugins.
## `flet build macos`[​](https://flet.dev/docs/publish/macos/#flet-build-macos "Direct link to flet-build-macos")
Creates a macOS application bundle from your Flet app.
## Bundle architecture[​](https://flet.dev/docs/publish/macos/#bundle-architecture "Direct link to Bundle architecture")
By default, `flet build macos` command builds universal app bundle that works on both Apple Silicon and older Intel processors. Therefore, packaging utility will try to download Python binary wheels for both `arm64` and `x86_64` platforms. Recent releases of some popular packages do not include `x86_64` wheels anymore, so the entire packaging operation will fail.
You can limit the build command to a specific architecture only, by using `--arch` option. For example, to build macOS app bundle that works on Apple Silicon only use the following command:
```
flet build macos --arch arm64
```

The same can be configured in `pyproject.toml`:
```
[tool.flet.macos]build_arch="arm64"
```

## Permissions[​](https://flet.dev/docs/publish/macos/#permissions "Direct link to Permissions")
Setting macOS entitlements which are written and `.entitlements` files:
```
flet build --macos-entitlements name_1=True|False name_2=True|False ...
```

Default macOS entitlements:
  * `com.apple.security.app-sandbox = False`
  * `com.apple.security.cs.allow-jit = True`
  * `com.apple.security.network.client = True`
  * `com.apple.security.network.server" = True`


Configuring macOS app entitlements in `pyproject.toml` (notice `"` around entitlement name):
```
[tool.flet.macos]entitlement."com.apple.security.personal-information.photos-library"=true
```

[Edit this page](https://github.com/flet-dev/website/edit/main/docs/publish/macos.md)
[PreviousiOS](https://flet.dev/docs/publish/ios)[NextLinux](https://flet.dev/docs/publish/linux)
  * [Prerequisites](https://flet.dev/docs/publish/macos/#prerequisites)
    * [Rosetta 2](https://flet.dev/docs/publish/macos/#rosetta-2)
    * [Xcode](https://flet.dev/docs/publish/macos/#xcode)
    * [CocoaPods](https://flet.dev/docs/publish/macos/#cocoapods)
  * [`flet build macos`](https://flet.dev/docs/publish/macos/#flet-build-macos)
  * [Bundle architecture](https://flet.dev/docs/publish/macos/#bundle-architecture)
  * [Permissions](https://flet.dev/docs/publish/macos/#permissions)


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
