[Skip to main content](https://flet.dev/docs/cookbook/keyboard-shortcuts/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/cookbook/keyboard-shortcuts/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/cookbook/keyboard-shortcuts/)
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
  * Keyboard shortcuts


# Keyboard shortcuts
A solid keyboard support is a key for user productivity while using your web and, especially, desktop app. Indeed, it could be really annoying to constantly switch between mouse and keyboard.
In addition to form controls' `.autofocus` property and [`TextField.focus()`](https://flet.dev/docs/controls/textfield#focus) method Flet allows handling "global" keyboard events.
To capture all keystrokes implement `page.on_keyboard_event` handler. Event handler parameter `e` is an instance of `KeyboardEvent` class with the following properties:
  * `key` - a textual representation of a pressed key, e.g. `A`, `Enter` or `F5`.
  * `shift` - `True` if "Shift" key is pressed.
  * `ctrl` - `True` if "Control" key is pressed.
  * `alt` - `True` if "Alt" ("Option") key is pressed.
  * `meta` - `True` if "Command" key is pressed.


This is a simple usage example:
```
import flet as ftdefmain(page: ft.Page):defon_keyboard(e: ft.KeyboardEvent):    page.add(      ft.Text(f"Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"))  page.on_keyboard_event = on_keyboard  page.add(    ft.Text("Press any key with a combination of CTRL, ALT, SHIFT and META keys..."))ft.app(main)
```

![](https://flet.dev/img/docs/getting-started/keyboard-shortcuts.png)
Here is [more advanced example](https://github.com/flet-dev/examples/blob/main/python/controls/page/keyboard-events.py).
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/cookbook/keyboard-shortcuts.md)
[PreviousTheming](https://flet.dev/docs/cookbook/theming)[NextLarge lists](https://flet.dev/docs/cookbook/large-lists)
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
