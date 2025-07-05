[Skip to main content](https://flet.dev/docs/cookbook/accessibility/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/cookbook/accessibility/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/cookbook/accessibility/)
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
  * Accessibility


On this page
# Accessibility
Flet is based on Flutter which includes first-class framework support for accessibility in addition to that provided by the underlying operating system.
## Screen readers[​](https://flet.dev/docs/cookbook/accessibility/#screen-readers "Direct link to Screen readers")
For mobile, screen readers ([TalkBack](https://support.google.com/accessibility/android/answer/6283677?hl=en), [VoiceOver](https://www.apple.com/lae/accessibility/iphone/vision/)) enable visually impaired users to get spoken feedback about the contents of the screen and interact with the UI via gestures on mobile and keyboard shortcuts on desktop. Turn on VoiceOver or TalkBack on your mobile device and navigate around your app.
For web, the following screen readers are currently supported:
Mobile Browsers:
  * iOS - VoiceOver
  * Android - TalkBack


Desktop Browsers:
  * MacOS - VoiceOver
  * Windows - JAWs & NVDA


Screen Readers users on web will need to toggle "Enable accessibility" button to build the semantics tree.
### Text[​](https://flet.dev/docs/cookbook/accessibility/#text "Direct link to Text")
Use `Text.semantics_label` property to override default Text control semantics.
### Buttons[​](https://flet.dev/docs/cookbook/accessibility/#buttons "Direct link to Buttons")
All buttons with text on them generate proper semantics.
Use `tooltip` property to add screen reader semantics for `IconButton`, `FloatingActionButton` and `PopupMenuButton` buttons.
### `TextField` and `Dropdown`[​](https://flet.dev/docs/cookbook/accessibility/#textfield-and-dropdown "Direct link to textfield-and-dropdown")
Use `TextField.label` and `Dropdown.label` properties to add screen reader semantics to those controls.
### Custom semantics[​](https://flet.dev/docs/cookbook/accessibility/#custom-semantics "Direct link to Custom semantics")
For any specific requirements use [`Semantics`](https://flet.dev/docs/controls/semantics) control.
### Debugging semantics[​](https://flet.dev/docs/cookbook/accessibility/#debugging-semantics "Direct link to Debugging semantics")
Set `page.show_semantics_debugger` to `True` to show an overlay that shows the accessibility information reported by the framework.
You can implement a specific [keyboard shortcut](https://flet.dev/docs/cookbook/keyboard-shortcuts) to conveniently toggle semantics debugger during app development:
![](https://flet.dev/img/docs/getting-started/debug-accessibility-toggle.gif)
```
import flet as ftdefmain(page: ft.Page):  page.title ="Flet counter example"  page.vertical_alignment = ft.MainAxisAlignment.CENTER  page.horizontal_alignment = ft.CrossAxisAlignment.CENTERdefon_keyboard(e: ft.KeyboardEvent):print(e)if e.key =="S"and e.ctrl:      page.show_semantics_debugger =not page.show_semantics_debugger      page.update()  page.on_keyboard_event = on_keyboard  txt_number = ft.Text("0", size=40)defbutton_click(e):    txt_number.value =str(int(txt_number.value)+1)    page.update()  page.add(    txt_number,    ft.Text("Press CTRL+S to toggle semantics debugger"),    ft.FloatingActionButton(      icon=ft.Icons.ADD, tooltip="Increment number", on_click=button_click),)ft.app(main, view=ft.AppView.WEB_BROWSER)
```

[Edit this page](https://github.com/flet-dev/website/edit/main/docs/cookbook/accessibility.md)
[PreviousControl Refs](https://flet.dev/docs/cookbook/control-refs)[NextLogging](https://flet.dev/docs/cookbook/logging)
  * [Screen readers](https://flet.dev/docs/cookbook/accessibility/#screen-readers)
    * [Text](https://flet.dev/docs/cookbook/accessibility/#text)
    * [Buttons](https://flet.dev/docs/cookbook/accessibility/#buttons)
    * [`TextField` and `Dropdown`](https://flet.dev/docs/cookbook/accessibility/#textfield-and-dropdown)
    * [Custom semantics](https://flet.dev/docs/cookbook/accessibility/#custom-semantics)
    * [Debugging semantics](https://flet.dev/docs/cookbook/accessibility/#debugging-semantics)


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
