[Skip to main content](https://flet.dev/docs/cookbook/assets/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/cookbook/assets/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/cookbook/assets/)
    * [Theming](https://flet.dev/docs/cookbook/theming)
    * [Keyboard shortcuts](https://flet.dev/docs/cookbook/keyboard-shortcuts)
    * [Large lists](https://flet.dev/docs/cookbook/large-lists)
    * [Drag and drop](https://flet.dev/docs/cookbook/drag-and-drop)
    * [File picker and uploads](https://flet.dev/docs/cookbook/file-picker-and-uploads)
    * [Animations](https://flet.dev/docs/cookbook/animations)
    * [Authentication](https://flet.dev/docs/cookbook/authentication)
    * [Assets](https://flet.dev/docs/cookbook/assets)
    * [Fonts](https://flet.dev/docs/cookbook/fonts)
    * [Read and write files](https://flet.dev/docs/cookbook/read-and-write-files)
    * [Client storage](https://flet.dev/docs/cookbook/client-storage)
    * [Session storage](https://flet.dev/docs/cookbook/session-storage)
    * [Encrypting sensitive data](https://flet.dev/docs/cookbook/encrypting-sensitive-data)
    * [PubSub](https://flet.dev/docs/cookbook/pub-sub)
    * [Control Refs](https://flet.dev/docs/cookbook/control-refs)
    * [Accessibility](https://flet.dev/docs/cookbook/accessibility)
    * [Logging](https://flet.dev/docs/cookbook/logging)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * Cookbook
  * Assets


On this page
# Assets
Flet apps can include both code and assets/resources. An asset is a file that is bundled and deployed with your app and is accessible at runtime. Common types of assets include static data (e.g., JSON files), configuration files, icons, images, videos, etc.
To use relative paths for your asset files, you need to provide a path to your assets directory when launching your app with the `ft.app()` function. The parameter for this is called `assets_dir`, which defaults to `"assets"`. This parameter specifies the folder where local assets are stored and can be either an absolute path or a path relative to the app's entry point file, such as `main.py`.
## Example: Displaying a Local Image[​](https://flet.dev/docs/cookbook/assets/#example-displaying-a-local-image "Direct link to Example: Displaying a Local Image")
Suppose you have a folder named `assets` in the same directory as your `main.py` file, and this folder contains an image file named `sample.png` in a subfolder called `images`:
```
/assets  /images     /sample.pngmain.py
```

To display this image in your app, you can do the following:
```
import flet as ftdefmain(page: ft.Page):  page.add(    ft.Image(src="images/sample.png"))ft.app(main, assets_dir="assets")
```

The same approach applies to other asset types like fonts, Lottie animations, Rive files, etc.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/cookbook/assets.md)
[PreviousAuthentication](https://flet.dev/docs/cookbook/authentication)[NextFonts](https://flet.dev/docs/cookbook/fonts)
  * [Example: Displaying a Local Image](https://flet.dev/docs/cookbook/assets/#example-displaying-a-local-image)


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
