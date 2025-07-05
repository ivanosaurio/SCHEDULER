[Skip to main content](https://flet.dev/docs/publish/windows/#__docusaurus_skipToContent_fallback)
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
  * [Extending Flet](https://flet.dev/docs/publish/windows/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/publish/windows/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * Windows


On this page
# Packaging app for Windows
Flet CLI provides `flet build windows` command that allows packaging Flet app into a Windows application.
note
The command can be run on Windows only.
## Prerequisites[​](https://flet.dev/docs/publish/windows/#prerequisites "Direct link to Prerequisites")
### Visual Studio 2022[​](https://flet.dev/docs/publish/windows/#visual-studio-2022 "Direct link to Visual Studio 2022")
Building Flet app for Windows desktop requires [Visual Studio 2022](https://learn.microsoft.com/visualstudio/install/install-visual-studio?view=vs-2022) with **Desktop development with C++** workload installed.
[Follow this medium article](https://medium.com/@teamcode20233/a-guide-to-install-desktop-development-with-c-workload-542bb92cfe90) for the instructions on downloading & installing correct Visual Studio components for Flutter desktop development.
### Enable Developer Mode[​](https://flet.dev/docs/publish/windows/#enable-developer-mode "Direct link to Enable Developer Mode")
While running `flet build` on Windows you may get the following error:
```
Building with plugins requires symlink support.Please enable Developer Mode in your system settings. Run start ms-settings:developersto open settings.
```

[Follow this SO answer](https://stackoverflow.com/a/70994092/1435891) for the instructions on how to enable developer mode in Windows 11.
## `flet build windows`[​](https://flet.dev/docs/publish/windows/#flet-build-windows "Direct link to flet-build-windows")
Creates a Windows application from your Flet app.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/publish/windows.md)
[PreviousLinux](https://flet.dev/docs/publish/linux)[NextWeb](https://flet.dev/docs/publish/web)
  * [Prerequisites](https://flet.dev/docs/publish/windows/#prerequisites)
    * [Visual Studio 2022](https://flet.dev/docs/publish/windows/#visual-studio-2022)
    * [Enable Developer Mode](https://flet.dev/docs/publish/windows/#enable-developer-mode)
  * [`flet build windows`](https://flet.dev/docs/publish/windows/#flet-build-windows)


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
