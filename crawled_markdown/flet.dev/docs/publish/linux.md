[Skip to main content](https://flet.dev/docs/publish/linux/#__docusaurus_skipToContent_fallback)
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
  * [Extending Flet](https://flet.dev/docs/publish/linux/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/publish/linux/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * Linux


On this page
# Packaging app for Linux
Flet CLI provides `flet build linux` command that allows packaging Flet app into a Linux application.
note
The command can be run on Linux only.
## Prerequisites[​](https://flet.dev/docs/publish/linux/#prerequisites "Direct link to Prerequisites")
### GStreamer for `Audio`[​](https://flet.dev/docs/publish/linux/#gstreamer-for-audio "Direct link to gstreamer-for-audio")
[GStreamer](https://gstreamer.freedesktop.org/) libraries must be installed if your Flet app uses `Audio` control.
To install minimal set of GStreamer libs on Ubuntu/Debian run the following commands:
```
apt install libgtk-3-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
```

To install full set of GStreamer libs:
```
apt install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
```

See [this guide](https://gstreamer.freedesktop.org/documentation/installing/on-linux.html?gi-language=c) for installing on other Linux distributives.
To build your Flet app that uses `Audio` control add `--include-packages flet_audio` to `flet build` command, for example:
```
flet build apk --include-packages flet_audio
```

### MPV for `Video`[​](https://flet.dev/docs/publish/linux/#mpv-for-video "Direct link to mpv-for-video")
[libmpv](https://mpv.io/) libraries must be installed if your Flet app uses `Video` control. On Ubuntu/Debian you can install it with:
```
sudo apt install libmpv-dev mpv
```

To build your Flet app that uses `Video` control add `--include-packages flet_video` to `flet build` command, for example:
```
flet build apk --include-packages flet_video
```

## `flet build linux`[​](https://flet.dev/docs/publish/linux/#flet-build-linux "Direct link to flet-build-linux")
Creates a Linux application from your Flet app.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/publish/linux.md)
[PreviousmacOS](https://flet.dev/docs/publish/macos)[NextWindows](https://flet.dev/docs/publish/windows)
  * [Prerequisites](https://flet.dev/docs/publish/linux/#prerequisites)
    * [GStreamer for `Audio`](https://flet.dev/docs/publish/linux/#gstreamer-for-audio)
    * [MPV for `Video`](https://flet.dev/docs/publish/linux/#mpv-for-video)
  * [`flet build linux`](https://flet.dev/docs/publish/linux/#flet-build-linux)


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
