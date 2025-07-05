[Skip to main content](https://flet.dev/docs/getting-started/create-flet-app/#__docusaurus_skipToContent_fallback)
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
  * [Extending Flet](https://flet.dev/docs/getting-started/create-flet-app/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/getting-started/create-flet-app/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * Create a new Flet app


# Create a new Flet app
Create a new directory (or directory with `pyproject.toml` already exists if initialized with `poetry` or `uv`) and switch into it.
To create a new "minimal" Flet app run the following command:
  * venv
  * uv
  * poetry


```
flet create
```

```
uv run flet create
```

```
poetry run flet create
```

The command will create the following directory structure:
```
├── README.md├── pyproject.toml├── src│   ├── assets│   │   └── icon.png│   └── main.py└── storage  ├── data  └── temp
```

note
  1. Original `pyproject.toml` created by `uv init` or `poetry init` will be replaced with the one from Flet app template.
  2. In case you encounter the error `Error creating the project from a template: 'git' is not installed.`, it means that you don't have _Git_ installed. Please visit [git-scm.com/downloads](https://git-scm.com/downloads) and install the latest version of _Git_. To verify your installation, type `git` in the terminal. Please note that _Git_ is not the same as _GitHub CLI_ which is not an alternative for use with Flet.


`src/main.py` contains Flet program. It has `main()` function where you would add UI elements ([controls](https://flet.dev/docs/getting-started/flet-controls)) to a page or a window. The application ends with a blocking `ft.app()` function which initializes Flet app and [runs](https://flet.dev/docs/getting-started/running-app) `main()`.
You can find more information about `flet create` command [here](https://flet.dev/docs/reference/cli/create).
Now let's see Flet in action by [running the app](https://flet.dev/docs/getting-started/running-app)!
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/getting-started/create-flet-app.md)
[PreviousGetting started](https://flet.dev/docs/getting-started/)[NextRunning Flet app](https://flet.dev/docs/getting-started/running-app)
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
