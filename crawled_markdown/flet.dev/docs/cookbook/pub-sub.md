[Skip to main content](https://flet.dev/docs/cookbook/pub-sub/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/cookbook/pub-sub/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/cookbook/pub-sub/)
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
  * PubSub


# PubSub
If you build a chat app using Flet you need somehow to pass user messages between sessions. When a user sends a message it should be broadcasted to all other app sessions and displayed on their pages.
Flet provides a simple built-in PubSub mechanism for asynchronous communication between page sessions.
Flet PubSub allows broadcasting messages to all app sessions or sending only to specific "topic" (or "channel") subscribers.
A typical PubSub usage would be:
  * [subscribe](https://flet.dev/docs/controls/page#subscribehandler) to broadcast messages or [subscribe to a topic](https://flet.dev/docs/controls/page#subscribe_topictopic-handler) on app session start.
  * [send](https://flet.dev/docs/controls/page#send_allmessage) broadcast message or [send to a topic](https://flet.dev/docs/controls/page#send_all_on_topictopic-message) on some event, like "Send" button click.
  * [unsubscribe](https://flet.dev/docs/controls/page#unsubscribe) from broadcast messages or [unsubscribe from a topic](https://flet.dev/docs/controls/page#unsubscribe_topictopic) on some event, like "Leave" button click.
  * [unsubscribe](https://flet.dev/docs/controls/page#unsubscribe_all) from everything on [`page.on_close`](https://flet.dev/docs/controls/page#on_close).


This is an example of a simple chat application:
```
import flet as ftdefmain(page: ft.Page):  page.title ="Flet Chat"# subscribe to broadcast messagesdefon_message(msg):    messages.controls.append(ft.Text(msg))    page.update()  page.pubsub.subscribe(on_message)defsend_click(e):    page.pubsub.send_all(f"{user.value}: {message.value}")# clean up the form    message.value =""    page.update()  messages = ft.Column()  user = ft.TextField(hint_text="Your name", width=150)  message = ft.TextField(hint_text="Your message...", expand=True)# fill all the space  send = ft.ElevatedButton("Send", on_click=send_click)  page.add(messages, ft.Row(controls=[user, message, send]))ft.app(main, view=ft.AppView.WEB_BROWSER)
```

![](https://flet.dev/img/docs/getting-started/chat-app-example.gif)
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/cookbook/pub-sub.md)
[PreviousEncrypting sensitive data](https://flet.dev/docs/cookbook/encrypting-sensitive-data)[NextControl Refs](https://flet.dev/docs/cookbook/control-refs)
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
