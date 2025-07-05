[Skip to main content](https://flet.dev/docs/getting-started/#__docusaurus_skipToContent_fallback)
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
  * [Extending Flet](https://flet.dev/docs/getting-started/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/getting-started/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * Getting started


On this page
# Getting started
Before you can create your first Flet app you need to setup your development environment which requires Python 3.9 or above and `flet` package.
We recommend installing Flet in a virtual environment which can be done in a number of different ways.
## Prerequisites[​](https://flet.dev/docs/getting-started/#prerequisites "Direct link to Prerequisites")
### macOS[​](https://flet.dev/docs/getting-started/#macos "Direct link to macOS")
Flet supports macOS 11 (Big Sur) or later.
### Windows[​](https://flet.dev/docs/getting-started/#windows "Direct link to Windows")
Flet supports 64-bit version of Microsoft Windows 10 or later.
### Linux[​](https://flet.dev/docs/getting-started/#linux "Direct link to Linux")
Flet supports Debian Linux 11 or later and Ubuntu Linux 20.04 LTS or later.
There are additional [prerequisites](https://flet.dev/docs/publish/linux#prerequisites) when developing and running Flet apps on Linux.
Windows Subsystem for Linux (WSL)
Flet apps can be run on WSL 2 (Windows Subsystem for Linux 2). If you are getting `cannot open display` error [following this guide](https://github.com/microsoft/wslg/wiki/Diagnosing-%22cannot-open-display%22-type-issues-with-WSLg) for troubleshooting.
#### Audio support[​](https://flet.dev/docs/getting-started/#audio-support "Direct link to Audio support")
If you recieve `error while loading shared libraries: libgstapp-1.0.so.0` GStreamer is not installed in your WSL environment.
To install GStreamer run the following command:
```
apt install -y libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools
```

#### Video support[​](https://flet.dev/docs/getting-started/#video-support "Direct link to Video support")
Video support in Flet on WSL requires `libmpv` library.
If you recieve `error while loading shared libraries: libmpv.so.1: cannot open shared object file: No such file or directory` it means the library is not installed.
To install `libmpv` run the following commands:
```
sudo apt updatesudo apt install libmpv-dev libmpv2sudo ln -s /usr/lib/x86_64-linux-gnu/libmpv.so /usr/lib/libmpv.so.1
```

## Virtual environment[​](https://flet.dev/docs/getting-started/#virtual-environment "Direct link to Virtual environment")
You can create virtual environment by running the following commands in your terminal:
  * macOS
  * Linux
  * Windows


```
mkdir first-flet-appcd first-flet-apppython3 -m venv .venvsource .venv/bin/activate
```

```
mkdir first-flet-appcd first-flet-apppython3 -m venv .venvsource .venv/bin/activate
```

```
md first-flet-appcd first-flet-apppython -m venv .venv.venv\Scripts\activate
```

Once you activated virtual environment, you'll see that your prompt now shows `(.venv)` prefix.
Now you can install the latest version of Flet in `.venv` virtual environment:
  * macOS
  * Linux
  * Windows


```
pip install 'flet[all]'
```

```
pip install flet[all]
```

```
pip install flet[all]
```

To check what version of Flet was installed:
```
flet --version
```

You can read more about Python `venv` module [here](https://docs.python.org/3/library/venv.html).
Now you are ready to [create your first Flet app](https://flet.dev/docs/getting-started/create-flet-app).
## Poetry[​](https://flet.dev/docs/getting-started/#poetry "Direct link to Poetry")
Another way to setup a virtual environment for your Flet project is using [Poetry](https://python-poetry.org/docs/).
Poetry 2.0
All Poetry examples in Flet docs is for Poetry 2.0 as it supports standard `[project]` section in `pyproject.toml`.
Once you have Poetry [installed](https://python-poetry.org/docs/#installation), run the following commands in your terminal:
```
mkdir my-appcd my-apppoetry init --dev-dependency='flet[all]' --python='>=3.9' --no-interaction
```

This command will create `pyproject.toml` in `my-app` directory.
Run the following command to install Flet and other dependencies:
```
poetry install --no-root
```

Make sure Flet CLI has been installed and can be run:
```
poetry run flet --version
```

Now you are ready to [create your first Flet app](https://flet.dev/docs/getting-started/create-flet-app).
note
When [creating](https://flet.dev/docs/getting-started/create-flet-app) and [running](https://flet.dev/docs/getting-started/running-app) Flet app using Poetry, you'll need to use `poetry run` before each command!
## uv[​](https://flet.dev/docs/getting-started/#uv "Direct link to uv")
**uv** is "An extremely fast Python package and project manager, written in Rust."
[Install `uv`](https://github.com/astral-sh/uv?tab=readme-ov-file#installation) and run the following commands in your terminal:
```
mkdir my-appcd my-appuv init
```

This command will create `pyproject.toml` in `my-app` directory.
Run the following command to add Flet as dependency:
```
uv add 'flet[all]' --dev
```

Make sure Flet CLI has been installed and can be run:
```
uv run flet --version
```

Now you are ready to [create your first Flet app](https://flet.dev/docs/getting-started/create-flet-app).
note
When [creating](https://flet.dev/docs/getting-started/create-flet-app) and [running](https://flet.dev/docs/getting-started/running-app) Flet app using uv, you'll need to use `uv run` before each command!
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/getting-started/index.md)
[PreviousIntroduction](https://flet.dev/docs/)[NextCreate a new Flet app](https://flet.dev/docs/getting-started/create-flet-app)
  * [Prerequisites](https://flet.dev/docs/getting-started/#prerequisites)
    * [macOS](https://flet.dev/docs/getting-started/#macos)
    * [Windows](https://flet.dev/docs/getting-started/#windows)
    * [Linux](https://flet.dev/docs/getting-started/#linux)
  * [Virtual environment](https://flet.dev/docs/getting-started/#virtual-environment)
  * [Poetry](https://flet.dev/docs/getting-started/#poetry)
  * [uv](https://flet.dev/docs/getting-started/#uv)


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
