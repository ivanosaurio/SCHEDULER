[Skip to main content](https://flet.dev/docs/publish/web/#__docusaurus_skipToContent_fallback)
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
      * [Static website](https://flet.dev/docs/publish/web/static-website)
      * [Dynamic website](https://flet.dev/docs/publish/web/dynamic-website)
  * [Extending Flet](https://flet.dev/docs/publish/web/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/publish/web/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * Web


# Publishing Flet app to web
Flet allows publishing your app as a **static** or **dynamic** website.
**Static website** - content is not changing and delivered exactly as it's stored. Python code is running in the web browser.
**Dynamic website** - content is dynamically generated for each user. Python code is running on the server.
Here is a table comparing Flet app running as a static vs dynamic website:
| [Static website](https://flet.dev/docs/publish/web/static-website)| [Dynamic website](https://flet.dev/docs/publish/web/dynamic-website)  
---|---|---  
**Loading time**|  ⬇️ Slower - Python runtime (Pyodide) along with app's Python code and all its dependencies must be loaded into the browser. Pyodide initialization takes time too.| ✅ Faster - the app stays and runs on the server.  
**Python compatibility**|  ⬇️ Not every program that works with native Python [can be run with Pyodide](https://pyodide.org/en/stable/usage/wasm-constraints.html)| ✅ Any Python package can be used.  
**Responsiveness**|  ✅ Zero latency between user-generated events (clicks, text field changes, drags) and page updates.| ⬇️ Non-zero latency - user-generated events are communicated to a server via WebSockets. UI updates are communicated back.  
**Performance**|  ⬇️ Slower - Pyodide is currently 3x-5x slower than native Python because of WASM| ✅ Faster - the code is running on the server by native Python.  
**Code protection**|  ⬇️ Low - app's code is loaded into a web browser and can be inspected by a user.| ✅ High - the app is running on the server.  
**Hosting**|  ✅ Cheap/Free - no code is running on the server and thus the app can be hosted anywhere: GitHub Pages, Cloudflare Pages, Replit, Vercel, a shared hosting or your own VPS.| ⬇️ Paid - the app requires Python code to run on the server and communicate with a web browser via WebSockets.  
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/publish/web/index.md)
[PreviousWindows](https://flet.dev/docs/publish/windows)[NextStatic website](https://flet.dev/docs/publish/web/static-website)
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
