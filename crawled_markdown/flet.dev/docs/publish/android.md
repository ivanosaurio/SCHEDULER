[Skip to main content](https://flet.dev/docs/publish/android/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search
[![Flet Logo](https://flet.dev/img/logo.svg)![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
    * [Android](https://flet.dev/docs/publish/android)
    * [iOS](https://flet.dev/docs/publish/ios)
    * [macOS](https://flet.dev/docs/publish/macos)
    * [Linux](https://flet.dev/docs/publish/linux)
    * [Windows](https://flet.dev/docs/publish/windows)
    * [Web](https://flet.dev/docs/publish/web)
  * [Extending Flet](https://flet.dev/docs/extend/built-in-extensions)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/cookbook/theming)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * Android


On this page
# Packaging app for Android
## Introduction[​](https://flet.dev/docs/publish/android/#introduction "Direct link to Introduction")
Flet CLI provides `flet build apk` and `flet build aab` commands that allow packaging Flet app into Android APK and Android App Bundle (AAB) respectively.
## Prerequisites[​](https://flet.dev/docs/publish/android/#prerequisites "Direct link to Prerequisites")
### Android SDK[​](https://flet.dev/docs/publish/android/#android-sdk "Direct link to Android SDK")
Java (JDK) and Android SDK will be automatically installed on the first run of `flet build` command.
JDK is installed into `$HOME/java/{version}` directory.
If you have Android Studio installed Flet CLI will locate and use Android SDK coming with the studio; otherwise Android SDK will be installed to `$HOME/Android/sdk` directory.
### Android wheels for binary Python packages[​](https://flet.dev/docs/publish/android/#android-wheels-for-binary-python-packages "Direct link to Android wheels for binary Python packages")
Binary Python packages (vs "pure" Python packages written in Python only) are packages that partially written in C, Rust or other languages producing native code. Example packages are `numpy`, `cryptography`, or `pydantic-core`.
Make sure all non-pure (binary) packages used in your Flet app have [pre-built wheels for Android](https://flet.dev/docs/reference/binary-packages-android-ios).
## `flet build apk`[​](https://flet.dev/docs/publish/android/#flet-build-apk "Direct link to flet-build-apk")
Build an Android APK file from your app.
This command builds release version. 'release' builds don't support debugging and are suitable for deploying to app stores. If you are deploying the app to the Play Store, it's recommended to use Android App Bundles (AAB) or split the APK to reduce the APK size.
  * <https://developer.android.com/guide/app-bundle>
  * <https://developer.android.com/studio/build/configure-apk-splits#configure-abi-split>


### Building platform-specific APKs[​](https://flet.dev/docs/publish/android/#building-platform-specific-apks "Direct link to Building platform-specific APKs")
By default, Flet builds "fat" APK which includes binaries for both `arm64-v8a` and `armeabi-v7a` architectures.
You can configure Flet to split fat APK into smaller APKs for each platform by using `--split-per-abi` option or by setting `split_per_abi` in `pyproject.toml`:
```
[tool.flet.android]split_per_abi = true
```

### Installing APK to a device[​](https://flet.dev/docs/publish/android/#installing-apk-to-a-device "Direct link to Installing APK to a device")
The easiest way to install APK to your device is to use `adb` (Android Debug Bridge) tool.
`adb` is a part of Android SDK. For example, on macOS, if Android SDK was installed with Android Studio the location of `adb` tool will be at `~/Library/Android/sdk/platform-tools/adb`.
[Check this article](https://www.makeuseof.com/install-apps-via-adb-android/) for more information about installing and using `adb` tool on various platforms.
To install APK to a device run the following command:
```
adb install <path-to-your.apk>
```

If more than one device is connected to your computer (say, emulator and a physical phone) you can use `-s` option to specify which device you want to install `.apk` on:
```
adb -s <device> install <path-to-your.apk>
```

where `<device>` can be found with `adb devices` command.
## `flet build aab`[​](https://flet.dev/docs/publish/android/#flet-build-aab "Direct link to flet-build-aab")
Build an Android App Bundle (AAB) file from your app.
This command builds release version. 'release' builds don't support debugging and are suitable for deploying to app stores. App bundle is the recommended way to publish to the Play Store as it improves your app size.
## Signing Android bundle[​](https://flet.dev/docs/publish/android/#signing-android-bundle "Direct link to Signing Android bundle")
TBD
```
[tool.flet.android.signing]# store and key passwords can be passed with `--android-signing-key-store-password`# and `--android-signing-key-password` options or# FLET_ANDROID_SIGNING_KEY_STORE_PASSWORD# and FLET_ANDROID_SIGNING_KEY_PASSWORD environment variables.key_store = "path/to/store.jks" # --android-signing-key-storekey_alias = "upload"
```

## Splash screen[​](https://flet.dev/docs/publish/android/#splash-screen "Direct link to Splash screen")
By default, generated Android app will be showing a splash screen with an image from `assets` directory (see below) or Flet logo. You can disable splash screen for Android app with `--no-android-splash` option.
Configuring splash in `pyproject.toml`:
```
[tool.flet.splash]android = false
```

## Android SDK version settings[​](https://flet.dev/docs/publish/android/#android-sdk-version-settings "Direct link to Android SDK version settings")
### `min_sdk_version`[​](https://flet.dev/docs/publish/android/#min_sdk_version "Direct link to min_sdk_version")
  * Defines the minimum Android version (API level) your app can run on.
  * If a device has a lower version than `min_sdk_version`, your app won’t install or run on that device.
  * Increasing this value means dropping support for older devices.


Configuring in `pyproject.toml`:
```
[tool.flet.android]min_sdk_version = 21
```

If `min_sdk_version` = `21`, your app will not install on Android 4.4 (API 19) or lower.
Default is `21`.
### `target_sdk_version`[​](https://flet.dev/docs/publish/android/#target_sdk_version "Direct link to target_sdk_version")
  * Defines the Android version your app is optimized for.
  * Your app can run on higher Android versions but will behave as if it’s running on `targetSdkVersion` unless explicitly adapted.
  * Google Play requires you to update this regularly to meet new Android requirements.


Configuring in `pyproject.toml`:
```
[tool.flet.android]target_sdk_version = 34
```

If `targetSdkVersion` = `34`, your app will run on Android 14 and above with the latest system behaviors. On newer Android versions, some strict security and API changes may apply automatically.
Default `target_sdk_version` is `35`.
#### Key differences[​](https://flet.dev/docs/publish/android/#key-differences "Direct link to Key differences")
Feature| `min_sdk_version`| `target_sdk_version`  
---|---|---  
Defines...| **Minimum Android version** required to install & run the app| **Optimized Android version** for best compatibility  
Impact| Lowering it allows **more devices** to install the app| Raising it allows access to **newer Android features**  
If set too low| App may not support modern APIs & security| App might not follow latest Android restrictions  
If set too high| App won't install on older devices| No major downside (except adapting to new behaviors)  
Configuring both settings in `pyproject.toml`:
```
[tool.flet.android]min_sdk_version = 21target_sdk_version = 34
```

## Permissions[​](https://flet.dev/docs/publish/android/#permissions "Direct link to Permissions")
Configuring Android permissions and features to be written into `AndroidManifest.xml`:
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


Configuring permissions and features in `pyproject.toml` (notice quotes `"` around key names):
```
[tool.flet.android.permission] # --android-permissions"android.permission.CAMERA" = true"android.permission.CAMERA" = true[tool.flet.android.feature] # --android-features"android.hardware.camera" = false
```

## Meta-data[​](https://flet.dev/docs/publish/android/#meta-data "Direct link to Meta-data")
Configuring Android app meta-data to be written into `AndroidManifest.xml`:
```
flet build --android-meta-data name_1=value_1 name_2=value_2 ...
```

Default Android meta-data:
  * `io.flutter.embedding.android.EnableImpeller=false`


Configuring meta-data in `pyproject.toml` (notice quotes `"` around key names):
```
[tool.flet.android.meta_data]"com.google.android.gms.ads.APPLICATION_ID" = "ca-app-pub-xxxxxxxxxxxxxxxx~yyyyyyyyyy"
```

## Deep linking[​](https://flet.dev/docs/publish/android/#deep-linking "Direct link to Deep linking")
You can configure deep-linking settings for Android app with the following `flet build` options:
  * `--deep-linking-scheme` - deep linking URL scheme to configure for Android builds, i.g. "https" or "myapp".
  * `--deep-linking-host` - deep linking URL host.


The same can be configured in `pyproject.toml`:
```
[tool.flet.android.deep_linking]scheme = "https"host = "mydomain.com"
```

See [Deep linking](https://docs.flutter.dev/ui/navigation/deep-linking) section in Flutter docs for more information and complete setup guide.
## Manifest application element properties[​](https://flet.dev/docs/publish/android/#manifest-application-element-properties "Direct link to Manifest application element properties")
Adding custom properties to `<application>` element in `AndroidManifest.xml`:
```
[tool.flet.android.manifest_application]usesCleartextTraffic = "true"requestLegacyExternalStorage = "true"
```

## Troubleshooting Android[​](https://flet.dev/docs/publish/android/#troubleshooting-android "Direct link to Troubleshooting Android")
To run interactive commands inside simulator or device:
```
adb shell
```

To overcome "permissions denied" error while trying to browse file system in interactive Android shell:
```
su
```

To download a file from a device to your local computer:
```
adb pull <device-path> <local-path>
```

[Edit this page](https://github.com/flet-dev/website/edit/main/docs/publish/android.md)
[PreviousPublishing Flet app to multiple platforms](https://flet.dev/docs/publish)[NextiOS](https://flet.dev/docs/publish/ios)
  * [Introduction](https://flet.dev/docs/publish/android/#introduction)
  * [Prerequisites](https://flet.dev/docs/publish/android/#prerequisites)
    * [Android SDK](https://flet.dev/docs/publish/android/#android-sdk)
    * [Android wheels for binary Python packages](https://flet.dev/docs/publish/android/#android-wheels-for-binary-python-packages)
  * [`flet build apk`](https://flet.dev/docs/publish/android/#flet-build-apk)
    * [Building platform-specific APKs](https://flet.dev/docs/publish/android/#building-platform-specific-apks)
    * [Installing APK to a device](https://flet.dev/docs/publish/android/#installing-apk-to-a-device)
  * [`flet build aab`](https://flet.dev/docs/publish/android/#flet-build-aab)
  * [Signing Android bundle](https://flet.dev/docs/publish/android/#signing-android-bundle)
  * [Splash screen](https://flet.dev/docs/publish/android/#splash-screen)
  * [Android SDK version settings](https://flet.dev/docs/publish/android/#android-sdk-version-settings)
    * [`min_sdk_version`](https://flet.dev/docs/publish/android/#min_sdk_version)
    * [`target_sdk_version`](https://flet.dev/docs/publish/android/#target_sdk_version)
  * [Permissions](https://flet.dev/docs/publish/android/#permissions)
  * [Meta-data](https://flet.dev/docs/publish/android/#meta-data)
  * [Deep linking](https://flet.dev/docs/publish/android/#deep-linking)
  * [Manifest application element properties](https://flet.dev/docs/publish/android/#manifest-application-element-properties)
  * [Troubleshooting Android](https://flet.dev/docs/publish/android/#troubleshooting-android)


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
