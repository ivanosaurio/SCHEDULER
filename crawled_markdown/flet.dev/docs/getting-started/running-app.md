[Skip to main content](https://flet.dev/docs/getting-started/running-app/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
    * [Create a new Flet app](https://flet.dev/docs/getting-started/create-flet-app)
    * [Running Flet app](https://flet.dev/docs/getting-started/running-app)
    * [Flet controls](https://flet.dev/docs/getting-started/flet-controls)
    * [Custom controls](https://flet.dev/docs/getting-started/custom-controls)
    * [Adaptive apps](https://flet.dev/docs/getting-started/adaptive-apps)
    * [Navigation and routing](https://flet.dev/docs/getting-started/navigation-and-routing)
    * [Testing on iOS](https://flet.dev/docs/getting-started/testing-on-ios)
    * [Testing on Android](https://flet.dev/docs/getting-started/testing-on-android)
    * [Async apps](https://flet.dev/docs/getting-started/async-apps)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/getting-started/running-app/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/getting-started/running-app/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * Running Flet app


On this page
# Running Flet app
Flet app can be run as a desktop or web app using a single `flet run` command.
## Run as a desktop app[​](https://flet.dev/docs/getting-started/running-app/#run-as-a-desktop-app "Direct link to Run as a desktop app")
To run Flet app as a desktop app, use the following command:
```
flet run
```

This command will run `main.py` located in the current directory.
If you need to provide a different path to the file, use the following command:
```
flet run [script]
```

To run `main.py` located in a different directory, provide an absolute or a relative path to the directory where it is located, for example:
```
flet run /Users/JohnSmith/Documents/projects/flet-app
```

To run script with a name other than `main.py`, provide an absolute or a relative path to the file, for example:
```
flet run counter.py
```

The app will be started in a native OS window:
### macOS
![](https://flet.dev/img/docs/getting-started/flet-counter-macos.png)
### Windows
![](https://flet.dev/img/docs/getting-started/flet-counter-windows.png)
## Run as a web app[​](https://flet.dev/docs/getting-started/running-app/#run-as-a-web-app "Direct link to Run as a web app")
To run Flet app as a web app, use the following command:
```
flet run --web[script]
```

A new browser window/tab will be opened and the app will be using a random TCP port:
![](https://flet.dev/img/docs/getting-started/flet-counter-safari.png)
To run on a fixed port use `--port` (`-p`) option, for example:
```
flet run --web--port8000 app.py
```

## Hot reload[​](https://flet.dev/docs/getting-started/running-app/#hot-reload "Direct link to Hot reload")
By default, Flet will watch the script file that was run and reload the app whenever the file is changed and saved, but will not watch for changes in other files.
To watch all the files in the same directory, use the following command:
```
poetry run flet run -d [script]
```

To watch script directory and all sub-directories recursively, use the following command:
```
poetry run flet run -d -r [script]
```

You can find more information about `flet run` command [here](https://flet.dev/docs/reference/cli/run).
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/getting-started/running-app.md)
[PreviousCreate a new Flet app](https://flet.dev/docs/getting-started/create-flet-app)[NextFlet controls](https://flet.dev/docs/getting-started/flet-controls)
  * [Run as a desktop app](https://flet.dev/docs/getting-started/running-app/#run-as-a-desktop-app)
  * [Run as a web app](https://flet.dev/docs/getting-started/running-app/#run-as-a-web-app)
  * [Hot reload](https://flet.dev/docs/getting-started/running-app/#hot-reload)


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
