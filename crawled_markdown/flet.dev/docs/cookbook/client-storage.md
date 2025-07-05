[Skip to main content](https://flet.dev/docs/cookbook/client-storage/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/cookbook/client-storage/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/cookbook/client-storage/)
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
  * Client storage


# Client storage
Flet's client storage API allows storing key-value data on a client side in a persistent storage. Flet implementation uses [`shared_preferences`](https://pub.dev/packages/shared_preferences) Flutter package.
The actual storage mechanism depends on a platform where Flet app is running:
  * Web - [Local storage](https://developer.mozilla.org/en-US/docs/Web/API/Storage).
  * Desktop - JSON file.
  * iOS - [NSUserDefaults](https://developer.apple.com/documentation/foundation/nsuserdefaults).
  * Android - [SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences).


Writing data to the storage:
```
# stringspage.client_storage.set("key","value")# numbers, booleanspage.client_storage.set("number.setting",12345)page.client_storage.set("bool_setting",True)# listspage.client_storage.set("favorite_colors",["red","green","blue"])
```

note
Each Flutter application using `shared_preferences` plugin has its own set of preferences. As the same Flet client (which is a Flutter app) is used to run UI for multiple Flet apps any values stored in one Flet application are visible/available to another Flet app running by the same user.
To distinguish one application settings from another it is recommended to use some unique prefix for all storage keys, for example `{company}.{product}.`. For example to store auth token in one app you could use `acme.one_app.auth_token` key and in another app use `acme.second_app.auth_token`.
caution
It is responsibility of Flet app developer to encrypt sensitive data before sending it to a client storage, so it's not read/tampered by another app or an app user.
Reading data:
```
# The value is automatically converted back to the original typevalue = page.client_storage.get("key")colors = page.client_storage.get("favorite_colors")# colors = ["red", "green", "blue"]
```

Check if a key exists:
```
page.client_storage.contains_key("key")# True if the key exists
```

Get all keys:
```
page.client_storage.get_keys("key-prefix.")
```

Remove a value:
```
page.client_storage.remove("key")
```

Clear the storage:
```
page.client_storage.clear()
```

caution
`clear()` is a dangerous function that removes all preferences of all Flet apps ever run by the same user and serves as a heads-up that permanent application data shouldn't be stored in the client storage.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/cookbook/client-storage.md)
[PreviousRead and write files](https://flet.dev/docs/cookbook/read-and-write-files)[NextSession storage](https://flet.dev/docs/cookbook/session-storage)
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
