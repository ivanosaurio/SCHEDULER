[Skip to main content](https://flet.dev/docs/getting-started/testing-on-ios/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
    * [Create a new Flet app](https://flet.dev/docs/getting-started/create-flet-app)
    * [Running Flet app](https://flet.dev/docs/getting-started/running-app)
    * [Flet controls](https://flet.dev/docs/getting-started/flet-controls)
    * [Custom controls](https://flet.dev/docs/getting-started/custom-controls)
    * [Adaptive apps](https://flet.dev/docs/getting-started/adaptive-apps)
    * [Navigation and routing](https://flet.dev/docs/getting-started/navigation-and-routing)
    * [Testing on iOS](https://flet.dev/docs/getting-started/testing-on-ios)
    * [Testing on Android](https://flet.dev/docs/getting-started/testing-on-android)
    * [Async apps](https://flet.dev/docs/getting-started/async-apps)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/getting-started/testing-on-ios/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/getting-started/testing-on-ios/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * Testing on iOS


# Testing Flet app on iOS
Start building awesome mobile apps in Python using just your computer and mobile phone!
Install [Flet](https://apps.apple.com/app/flet/id1624979699) app to your iOS device. You will be using this app to see how your Flet project is working on iPhone or iPad.
[![](https://flet.dev/img/docs/getting-started/testing-on-ios/qr-code.jpg)](https://apps.apple.com/app/flet/id1624979699)
To get started on your computer you need Python 3.9 or greater installed.
Important
Your iOS device and computer must be connected to the same Wi-Fi or local network.
It's recommended to start with the creation of a new virtual environment:
  * macOS
  * Linux
  * Windows


```
python3 -m venv .venvsource .venv/bin/activate
```

```
python3 -m venv .venvsource .venv/bin/activate
```

```
python.exe -m venv .venv.venv\Scripts\activate.bat
```

Next, install the latest `flet` package:
```
pip install flet --upgrade
```

Ensure that Flet has successfully installed and Flet CLI is available in `PATH` by running:
```
flet --version
```

Create a new Flet project:
```
flet create my-appcd my-app
```

Run the following command to start Flet development server with your app:
```
flet run --ios
```

A QR code with encoded project URL will be displayed in the terminal:
![](https://flet.dev/img/docs/getting-started/testing-on-ios/app-qr-code.png)
Open **Camera** app on your iOS device, point to a QR code and click **Open in Flet** link.
A dialog asking for permissions to access your local network will popup:
![](https://flet.dev/img/docs/getting-started/testing-on-ios/flet-local-network.png)
Click **Allow** and you should see your Flet app running.
Try updating `main.py` (for example, replace a greeting of `Text` control) - the app will be instantly refreshed on your iOS device.
You can try more complex Flet example from [Introduction](https://flet.dev/docs/#flet-app-example).
To return to "Home" tab either:
  * Long-press anywhere on the screen with 3 fingers or
  * Shake your iOS device.


You can also "manually" add a new project by clicking **"+"** button and typing its URL.
Quick test
There is "Counter" Flet project hosted on the internet that you can add to Flet app to make sure everything works:
```
https://flet-counter-test-ios.fly.dev
```

Check "Gallery" tab for some great examples of what kind of projects could be done with Flet.
Explore [Flet examples](https://github.com/flet-dev/examples/tree/main/python) for even more examples.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/getting-started/testing-on-ios.md)
[PreviousNavigation and routing](https://flet.dev/docs/getting-started/navigation-and-routing)[NextTesting on Android](https://flet.dev/docs/getting-started/testing-on-android)
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
