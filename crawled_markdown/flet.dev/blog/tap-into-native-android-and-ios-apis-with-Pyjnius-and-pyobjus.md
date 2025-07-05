[Skip to main content](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#__docusaurus_skipToContent_fallback)
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


# Tap into native Android and iOS APIs with Pyjnius and Pyobjus
February 23, 2025 · 3 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
When building mobile apps with Flet, you may need to interact directly with platform-specific APIs. Whether it’s accessing system information, managing Bluetooth devices, or working with user preferences, **Pyjnius** and **Pyobjus** by Kivy provide a seamless way to bridge Python with Java (for Android) and Objective-C (for iOS).
You can now integrate both Pyjnius and Pyobjus into your Flet apps! 🚀
## Pyjnius for Android[​](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#pyjnius-for-android "Direct link to Pyjnius for Android")
Pyjnius is a Python library for accessing Java classes using the **Java Native Interface** (JNI).
### Adding to a project[​](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#adding-to-a-project "Direct link to Adding to a project")
Add `pyjnius` dependency for Android builds only (other settings in `pyproject.toml` were omitted for brevity):
```
[project]name="pyjnius_demo"version="0.1.0"dependencies=["flet==0.27.1"][tool.flet.android]dependencies=["pyjnius"]
```

### Usage examples[​](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#usage-examples "Direct link to Usage examples")
Here are some example of how Pyjnius can be used in your Flet Android app.
#### Getting Android OS details[​](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#getting-android-os-details "Direct link to Getting Android OS details")
```
from jnius import autoclass# Get Build and Build.VERSION classesBuild = autoclass('android.os.Build')Version = autoclass('android.os.Build$VERSION')# Get OS detailsdevice_model = Build.MODELmanufacturer = Build.MANUFACTURERbrand = Build.BRANDhardware = Build.HARDWAREproduct = Build.PRODUCTdevice = Build.DEVICEos_version = Version.RELEASEsdk_version = Version.SDK_INT
```

#### Listing Bluetooth devices[​](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#listing-bluetooth-devices "Direct link to Listing Bluetooth devices")
```
from jnius import autoclass# Get BluetoothAdapter instanceBluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')bluetooth_adapter = BluetoothAdapter.getDefaultAdapter()if bluetooth_adapter isNone:print("Bluetooth not supported on this device")else:ifnot bluetooth_adapter.isEnabled():print("Bluetooth is disabled. Please enable it.")else:print("Bluetooth is enabled.")# Get paired devices    paired_devices = bluetooth_adapter.getBondedDevices()for device in paired_devices.toArray():print(f"Device Name: {device.getName()}, MAC Address: {device.getAddress()}")
```

### Accessing the Activity[​](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#accessing-the-activity "Direct link to Accessing the Activity")
App main activity instance can be retrieved with the following code:
```
import osfrom jnius import autoclassactivity_host_class = os.getenv("MAIN_ACTIVITY_HOST_CLASS_NAME")assert activity_host_classactivity_host = autoclass(activity_host_class)activity = activity_host.mActivity
```

Heck, you can basically call any Android API using Pyjnius - endless posibilities!
Check complete [Flet Pyjnius example](https://github.com/flet-dev/python-package-tests/tree/main/Pyjnius).
For more Pyjnius examples and API refer to the [Pyjnius Documentation](https://Pyjnius.readthedocs.io/en/latest/quickstart.html).
...or just use ChatGPT (or your favorite LLM) to get more ideas and solutions! 😅
## Pyobjus for iOS[​](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#pyobjus-for-ios "Direct link to Pyobjus for iOS")
Pyobjus is a library for accessing Objective-C classes as Python classes using Objective-C runtime reflection.
### Adding to a project[​](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#adding-to-a-project-1 "Direct link to Adding to a project")
Add `pyobjus` dependency for iOS builds only (other settings in `pyproject.toml` were omitted for brevity):
```
[project]name="Pyjnius"version="0.1.0"dependencies=["flet==0.27.1"][tool.flet.ios]dependencies=["pyobjus"]
```

### Usage examples[​](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#usage-examples-1 "Direct link to Usage examples")
#### The simplest example[​](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#the-simplest-example "Direct link to The simplest example")
```
from pyobjus import autoclassNSString = autoclass('NSString')text = NSString.alloc().initWithUTF8String_('Hello world')print(text.UTF8String())
```

#### Getting OS details[​](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#getting-os-details "Direct link to Getting OS details")
```
from pyobjus import autoclassfrom pyobjus.dylib_manager import load_framework, INCLUDE# Load Foundation frameworkload_framework(INCLUDE.Foundation)# Get NSProcessInfo instanceNSProcessInfo = autoclass('NSProcessInfo')process_info = NSProcessInfo.processInfo()# Retrieve OS version as a stringos_version = process_info.operatingSystemVersionString.UTF8String()print(f"iOS Version: {os_version}")
```

#### Working with app user settings[​](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#working-with-app-user-settings "Direct link to Working with app user settings")
```
from pyobjus import autoclass, objc_strNSUserDefaults = autoclass('NSUserDefaults')key ="pyobjus_hello_world_key"value ="Hello, world!"# set keyNSUserDefaults.standardUserDefaults().setObject_forKey_(objc_str(value), objc_str(key))# get keyret = NSUserDefaults.standardUserDefaults().stringForKey_(objc_str(key))assert ret.UTF8String()== value
```

Check complete [Flet Pyobjus example](https://github.com/flet-dev/python-package-tests/tree/main/pyobjus).
For more Pyobjus examples and API refer to the [Pyobjus Documentation](https://pyobjus.readthedocs.io/en/latest/quickstart.html).
## Plyer challenge[​](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#plyer-challenge "Direct link to Plyer challenge")
There is a [Plyer](https://github.com/kivy/plyer) project by Kivy team which uses both Pyjnius and Pyobjus under the hood.
It's not ported to Flet yet. You can either get more usage examples for [Android](https://github.com/kivy/plyer/tree/master/plyer/platforms/android) and [iOS](https://github.com/kivy/plyer/tree/master/plyer/platforms/ios) from there or help us with porting it to Flet.
**Tags:**
  * [news](https://flet.dev/blog/tags/news)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2025-02-23-tap-into-native-android-and-ios-apis-with-pyjnius-and-pyobjus.md)
[Newer postIntroducing Flet 1.0 Alpha](https://flet.dev/blog/introducing-flet-1-0-alpha)[Older postFlet v0.27.0 Release Announcement](https://flet.dev/blog/flet-v-0-27-release-announcement)
  * [Pyjnius for Android](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#pyjnius-for-android)
    * [Adding to a project](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#adding-to-a-project)
    * [Usage examples](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#usage-examples)
    * [Accessing the Activity](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#accessing-the-activity)
  * [Pyobjus for iOS](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#pyobjus-for-ios)
    * [Adding to a project](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#adding-to-a-project-1)
    * [Usage examples](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#usage-examples-1)
  * [Plyer challenge](https://flet.dev/blog/tap-into-native-android-and-ios-apis-with-Pyjnius-and-pyobjus/#plyer-challenge)


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
