[Skip to main content](https://flet.dev/docs/cookbook/control-refs/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/cookbook/control-refs/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/cookbook/control-refs/)
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
  * Control Refs


On this page
# Control Refs
Flet controls are objects and to access their properties we need to keep references (variables) to those objects.
Consider the following example:
```
import flet as ftdefmain(page):  first_name = ft.TextField(label="First name", autofocus=True)  last_name = ft.TextField(label="Last name")  greetings = ft.Column()defbtn_click(e):    greetings.controls.append(ft.Text(f"Hello, {first_name.value}{last_name.value}!"))    first_name.value =""    last_name.value =""    page.update()    first_name.focus()  page.add(    first_name,    last_name,    ft.ElevatedButton("Say hello!", on_click=btn_click),    greetings,)ft.app(main)
```

In the very beginning of `main()` method we create three controls which we are going to use in button's `on_click` handler: two `TextField` for first and last names and a `Column` - container for greeting messages. We create controls with all their properties set and in the end of `main()` method, in `page.add()` call, we use their references (variables).
When more and more controls and event handlers are added it becomes challenging to keep all control definitions in one place, so they become scattered across `main()` body. Glancing at `page.add()` parameters it's hard to imagine (without constant jumping to variable definitions in IDE) what would the end form look like:
```
  page.add(    first_name,    last_name,    ft.ElevatedButton("Say hello!", on_click=btn_click),    greetings,)
```

Is `first_name` a TextField, does it have autofocus set? Is greetings a `Row` or a `Column`?
## `Ref` class[​](https://flet.dev/docs/cookbook/control-refs/#ref-class "Direct link to ref-class")
Flet provides `Ref` utility class which allows to define a reference to the control, use that reference in event handlers and set the reference to a real control later, while building a tree. The idea comes from [React](https://reactjs.org/docs/refs-and-the-dom.html).
To define a new typed control reference:
```
first_name = ft.Ref[ft.TextField]()
```

To access referenced control (control de-reference) use `Ref.current` property:
```
# empty first namefirst_name.current.value =""
```

To assign control to a reference set `Control.ref` property to a reference:
```
page.add(  ft.TextField(ref=first_name, label="First name", autofocus=True))
```

note
All Flet controls have `ref` property.
We could re-write our program to use references:
```
import flet as ftdefmain(page):  first_name = ft.Ref[ft.TextField]()  last_name = ft.Ref[ft.TextField]()  greetings = ft.Ref[ft.Column]()defbtn_click(e):    greetings.current.controls.append(      ft.Text(f"Hello, {first_name.current.value}{last_name.current.value}!"))    first_name.current.value =""    last_name.current.value =""    page.update()    first_name.current.focus()  page.add(    ft.TextField(ref=first_name, label="First name", autofocus=True),    ft.TextField(ref=last_name, label="Last name"),    ft.ElevatedButton("Say hello!", on_click=btn_click),    ft.Column(ref=greetings),)ft.app(main)
```

Now we can clearly see in `page.add()` the structure of the page and all the controls it's built of.
Yes, the logic becomes a little bit more verbose as you need to add `.current.` to access ref's control, but it's a matter of personal preference :)
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/cookbook/control-refs.md)
[PreviousPubSub](https://flet.dev/docs/cookbook/pub-sub)[NextAccessibility](https://flet.dev/docs/cookbook/accessibility)
  * [`Ref` class](https://flet.dev/docs/cookbook/control-refs/#ref-class)


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
