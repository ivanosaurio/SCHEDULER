[Skip to main content](https://flet.dev/blog/user-authentication/#__docusaurus_skipToContent_fallback)
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


# User authentication
September 27, 2022 · 3 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
User authentication in Flet is here! 🎉
Now you can implement user authentication ("Login with X" buttons) in your Flet app using 3rd-party identity providers such as GitHub, Google, Azure, Auth0, LinkedIn and others:
![](https://flet.dev/img/docs/getting-started/authentication/github-oauth-authorize.png)
Traditionally, this release is not just about authentication, but it adds a ton of accompanying functionality and small improvements:
  * [Authentication](https://flet.dev/blog/user-authentication/#authentication)
  * [Client storage](https://flet.dev/blog/user-authentication/#client-storage)
  * [Session storage](https://flet.dev/blog/user-authentication/#session-storage)
  * [Encryption API](https://flet.dev/blog/user-authentication/#encryption-api)
  * [Other improvements](https://flet.dev/blog/user-authentication/#other-improvements)


## Authentication[​](https://flet.dev/blog/user-authentication/#authentication "Direct link to Authentication")
Flet authentication features:
  * Works with Flet desktop, web and mobile apps.
  * Using multiple authentication providers in one app.
  * Built-in OAuth providers with automatic user details fetching: 
    * GitHub
    * Azure
    * Google
    * Auth0
  * Optional groups fetching.
  * Automatic token refresh.
  * Login with a saved token ("Remember me").
  * Custom OAuth providers.


A simple example on how to add "Login with GitHub" button to your Flet app:
```
import osimport flet as ftfrom flet.auth.providers.github_oauth_provider import GitHubOAuthProviderdefmain(page: ft.Page):  provider = GitHubOAuthProvider(    client_id=os.getenv("GITHUB_CLIENT_ID"),    client_secret=os.getenv("GITHUB_CLIENT_SECRET"),    redirect_url="http://localhost:8550/api/oauth/redirect",)deflogin_click(e):    page.login(provider)defon_login(e):print("Access token:", page.auth.token.access_token)print("User ID:", page.auth.user.id)  page.on_login = on_login  page.add(ft.ElevatedButton("Login with GitHub", on_click=login_click))ft.app(target=main, port=8550, view=ft.AppView.WEB_BROWSER)
```

note
Before running the app set the secret environment variables in a command line:
```
$ export GITHUB_CLIENT_ID="<client_id>"$ export GITHUB_CLIENT_SECRET="<client_secret>"
```

[Read Authentication guide for more information and examples](https://flet.dev/docs/cookbook/authentication).
## Client storage[​](https://flet.dev/blog/user-authentication/#client-storage "Direct link to Client storage")
Flet's client storage API that allows storing key-value data on a client side in a persistent storage. Flet implementation uses [`shared_preferences`](https://pub.dev/packages/shared_preferences) Flutter package.
Writing data to the storage:
```
page.client_storage.set("key","value")
```

Reading data:
```
value = page.client_storage.get("key")
```

[Read Client storage guide for more information and examples](https://flet.dev/docs/cookbook/client-storage).
## Session storage[​](https://flet.dev/blog/user-authentication/#session-storage "Direct link to Session storage")
Flet introduces an API for storing key-value data in user's session on a server side.
Writing data to the session:
```
page.session.set("key","value")
```

Reading data:
```
value = page.session.get("key")
```

[Read Session storage guide for more information and examples](https://flet.dev/docs/cookbook/session-storage)
## Encryption API[​](https://flet.dev/blog/user-authentication/#encryption-api "Direct link to Encryption API")
In this release Flet introduces utility methods to encrypt and decrypt sensitive text data using symmetric algorithm (where the same key is used for encryption and decryption). It uses [Fernet](https://github.com/fernet/spec/blob/master/Spec.md) implementation from [cryptography](https://pypi.org/project/cryptography/) package, which is AES 128 with some additional hardening, plus PBKDF2 to derive encryption key from a user passphrase.
Encrypting data:
```
from flet.security import encrypt, decryptsecret_key ="S3CreT!"plain_text ="This is a secret message!"encrypted_data = encrypt(plain_text, secret_key)
```

Decrypting data:
```
from flet.security import encrypt, decryptsecret_key ="S3CreT!"plain_text = decrypt(encrypted_data, secret_key)print(plain_text)
```

[Continue reading for more information and examples](https://flet.dev/docs/cookbook/encrypting-sensitive-data).
## Other improvements[​](https://flet.dev/blog/user-authentication/#other-improvements "Direct link to Other improvements")
  * SVG image support ([example](https://github.com/flet-dev/examples/blob/main/python/controls/image/svg-image.py)) and new images properties: 
    * [`Image.color`](https://flet.dev/docs/controls/image#color)
    * [`Image.color_blend_mode`](https://flet.dev/docs/controls/image#color_blend_mode)
    * [`Image.semantics_label`](https://flet.dev/docs/controls/image#semantics_label)
    * [`Image.gapless_playback`](https://flet.dev/docs/controls/image#gapless_playback)
  * [`on_animation_end` callback](https://flet.dev/docs/cookbook/animations#animation-end-callback) to chain animations.
  * [`Container.clip_behavior` property](https://flet.dev/docs/controls/container#clip_behavior).
  * [`page.window.bgcolor`](https://flet.dev/docs/reference/types/window#bgcolor) to make cool transparent app window:


```
import flet as ftdefmain(page: ft.Page):  page.window_bgcolor = ft.Colors.TRANSPARENT  page.bgcolor=ft.Colors.TRANSPARENT  page.window_title_bar_hidden =True  page.window_frameless =True  page.window_left =400  page.window_top =400  page.add(ft.ElevatedButton("I'm a floating button!"))ft.app(target=main)
```

  * [`page.get_clipboard()`](https://flet.dev/docs/controls/page#get_clipboard)
  * [`page.launch_url()`](https://flet.dev/docs/controls/page#launch_urlurl) - better control with additional arguments: 
    * `web_window_name` - window tab/name to open URL in: `_self` - the same tab, `_blank` - a new tab or `<your name>` - a named tab.
    * `web_popup_window` - set to `True` to display a URL in a browser popup window. Default is `False`.
    * `window_width` - optional, popup window width.
    * `window_height` - optional, popup window height.
  * [`page.window.to_front()`](https://flet.dev/docs/reference/types/window#to_front)
  * [`page.close_in_app_web_view()`](https://flet.dev/docs/controls/page#close_in_app_web_view)


Upgrade Flet module to the latest version (`pip install flet --upgrade`), integrate auth in your app and [let us know](https://discord.gg/dzWXP8SHG8) what you think!
Enjoy!
**Tags:**
  * [release](https://flet.dev/blog/tags/release)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2022-09-27-user-authentication.md)
[Newer postGesture detector](https://flet.dev/blog/gesture-detector)[Older postFile picker and uploads](https://flet.dev/blog/file-picker-and-uploads)
  * [Authentication](https://flet.dev/blog/user-authentication/#authentication)
  * [Client storage](https://flet.dev/blog/user-authentication/#client-storage)
  * [Session storage](https://flet.dev/blog/user-authentication/#session-storage)
  * [Encryption API](https://flet.dev/blog/user-authentication/#encryption-api)
  * [Other improvements](https://flet.dev/blog/user-authentication/#other-improvements)


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
