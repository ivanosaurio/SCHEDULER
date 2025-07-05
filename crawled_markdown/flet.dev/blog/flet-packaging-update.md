[Skip to main content](https://flet.dev/blog/flet-packaging-update/#__docusaurus_skipToContent_fallback)
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


# Flet packaging update
May 1, 2024 · 7 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
## The problem[​](https://flet.dev/blog/flet-packaging-update/#the-problem "Direct link to The problem")
When you package your Flet program in Python to run on a mobile device (or desktop) the resulting bundle (.apk, .ipa, .exe, .app) contains your Python program, Python interpreter and [Python Standard Library](https://docs.python.org/3/library/index.html).
If your program uses only Python standard library then packaging process is relatively easy - Flet zips your code and combines Flutter app together with Python interpreter and standard library both compiled for the target platform: Android or iOS.
However, problems may arise when your Flet program uses third-party packages, with thousands of them published on PyPI or Conda.
There are two kinds of third-party packages:
### Pure-Python packages[​](https://flet.dev/blog/flet-packaging-update/#pure-python-packages "Direct link to Pure-Python packages")
A "pure-Python" package is a package that only contains Python code, and doesn't include extensions written in C, C++, Rust or other languages. You only need a Python interpreter and the Python Standard Library to run a pure-Python package, and it doesn't matter what your OS or platform is.
Examples of such packages: `httpx`, `click`, `rich`, `requests`.
To verify if the package is pure, find that package on [PyPI](https://pypi.org) and navigate to its "Download files" page. If under "Built distribution" section there is only one wheel ending with `-py3-none-any.whl` then _most probably_ it's a pure Python package that will work "as is" on any device with Python.
![](https://flet.dev/img/blog/packaging/pypi-pure-package.png)
We say _"probably"_ because that pure package could depend on a non-pure package which brings you to the next section. For example, [`pydantic`](https://pypi.org/project/pydantic/#files) is a pure package, but to work properly it requires [`pydantic-core`](https://pypi.org/project/pydantic-core/#files) non-pure package written in Rust.
### Non-pure Python packages[​](https://flet.dev/blog/flet-packaging-update/#non-pure-python-packages "Direct link to Non-pure Python packages")
A "non-pure Python" package is one that is fully or partially written in C, C++, Rust, or another language and must be compiled to machine code for the platform on which it will run.
Examples of such packages: `cryptography`, `opencv-python`, `numpy`, `msgpack`.
On "Download files" page of non-pure package you will find a bunch of wheels pre-built for various platforms: macOS, Windows, Linux.
![](https://flet.dev/img/blog/packaging/pypi-non-pure-package.png)
When you run `pip install <package>` pip tries to find a wheel for your specific platform and Python version looking at wheel suffixes that include that information.
It's a courtesy of package developer to provide pre-compiled wheels for multiple platforms. There could be missing wheels for some platforms, or no wheels at all - just `.tar.gz` under "Source distribution" with package sources.
#### Building package from sources is hard[​](https://flet.dev/blog/flet-packaging-update/#building-package-from-sources-is-hard "Direct link to Building package from sources is hard")
To install a package with source distribution only, pip will attempt to build non-Python code on your machine using installed compilers, linkers, libraries, and SDKs. However, this process can be lengthy and error-prone. The compiled code base might be large, and your machine could lack the required libraries or toolchains.
#### No wheels for iOS and Android yet[​](https://flet.dev/blog/flet-packaging-update/#no-wheels-for-ios-and-android-yet "Direct link to No wheels for iOS and Android yet")
There are no pre-built wheels for iOS and Android on PyPI and PyPI's validation process won't allow package developers to upload them anyway as both iOS and Android are not officially supported platforms in Python.
There is a process ([PEP 730](https://peps.python.org/pep-0730/) and [PEP 738](https://peps.python.org/pep-0738/)) to add official support for iOS and Android to Python 3.13, so, hopefully, the developer experience will improve.
#### Package dependencies[​](https://flet.dev/blog/flet-packaging-update/#package-dependencies "Direct link to Package dependencies")
Pure-Python packages can import or depend on non-pure packages and you should keep that in mind while packaging your Flet app to run on a mobile device.
For example, `supabase` package, to access Supabase API, is a pure package which depends on `pydantic` package which is also pure Python package. In its turn `pydantic` package depends on `pydantic-core` which is a non-pure package written in Rust. Thus, to run your Flet app using Supabase API the packaging process should be able to find a pre-build wheel for your target platform. If PyPI doesn't have that wheel then it could be either Flet developers, building that wheel on their servers and hosting it somewhere, or you, building that wheel on your own machine.
To see a dependency graph for a package you can use [`pipgrip`](https://pypi.org/project/pipgrip/).
Run it with `--tree` option to get a tree view of dependencies:
```
$ pipgrip --tree fastapifastapi (0.110.3)├── pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4 (2.7.1)│  ├── annotated-types>=0.4.0 (0.6.0)│  ├── pydantic-core==2.18.2 (2.18.2)│  │  └── typing-extensions!=4.7.0,>=4.6.0 (4.11.0)│  └── typing-extensions>=4.6.1 (4.11.0)├── starlette<0.38.0,>=0.37.2 (0.37.2)│  └── anyio<5,>=3.4.0 (4.3.0)│    ├── idna>=2.8 (3.7)│    └── sniffio>=1.1 (1.3.1)└── typing-extensions>=4.8.0 (4.11.0)
```

## Current approach[​](https://flet.dev/blog/flet-packaging-update/#current-approach "Direct link to Current approach")
We released the first version of packaging [4 months ago](https://flet.dev/blog/packaging-apps-for-distribution) and since then, we have realized that the initial approach has multiple flaws and should be improved.
When you run `flet build apk` with the current Flet version it downloads Python runtime with standard library both pre-built for Android (or iOS if ran with `flet build ipa`).
For non-pure packages, like `numpy`, Flet is asking you to build those packages by yourself using "Python for Android" (p4a) tool from Kivy and then provide a path to "p4a" distributive where those pre-build packages could be found.
This is problem #1 - you are forced to struggle with a complicated process of installing "p4a" tool and compiling Python modules on your machine.
Problem #2 - all packages from p4a's `dist` directory will be included into a final application bundle - it could contain non-relevant packages and other junk.
Problem #3 - non-pure packages must be built _before_ running `flet build` command. You have to analyze all dependencies of your app and separate what must be built with p4a.
Problem #4 - p4a "recipes" to build packages could be either very old or missing. You hope that older version of the package works with your app, try authoring a "recipe" and hope it works or submit a request for new recipe in Kivy repository.
When you're done with building non-pure packages using p4a, Flet requires you to specify only pure packages in `requirements.txt` which doesn't work if pure package directly or indirectly depends on non-pure (see [example above](https://flet.dev/blog/flet-packaging-update/#package-dependencies)) - this is problem #5. There is a [recent example](https://github.com/flet-dev/flet/issues/3114) of this problem: `flet build` replaces `flet` with `flet-embed` in `requirements.txt`, but it's unable to know if there is a 3rd-party package depending on `flet`, thus both `flet-embed` and non-suitable-for-mobile `flet` are installed. This is not a solution, but a hack!
## Packaging 2.0[​](https://flet.dev/blog/flet-packaging-update/#packaging-20 "Direct link to Packaging 2.0")
In the next iteration of Flet's packaging implementation, we are going to move away from Kivy and replace it with [Mobile Forge](https://github.com/flet-dev/mobile-forge). Mobile Forge has been created by Beeware team based and their experience with Briefcase and Chaquopy. Mobile Forge is a clean-room implementation of a packaging tool for binary Python packages which is relies on [crossenv](https://github.com/benfogle/crossenv).
The main promise of Mobile Forge with `crossenv` is that most existing non-pure Python packages will be able to compile for iOS and/or Android by simply adding a recipe with `meta.yaml` file only, without requiring any hacks or patches.
We are going to use Mobile Forge to pre-build the most popular non-pure Python packages for iOS and Android and host them in our own public repository. You will be able to use that tool to build and contribute other packages, non present in our repository.
We've created a new ["Packages" category in Flet discussions](https://github.com/flet-dev/flet/discussions/categories/packages) where you can post, vote and discuss requests for non-pure (native) Python packages that work with Flet (check [rules](https://github.com/flet-dev/flet/discussions/3139) before posting there). Flet's goal is to provide the most comprehensive catalog of pre-built Python packages and make the process of adding new packages as friendly and transparent as possible.
The new version of `flet build` will use a custom-made virtual pip index. This index will analyze dependencies, detect non-pure packages, and offer to pip mobile packages. For all other packages, it will fall back to PyPI.
The new packaging will be hopefully available in a few weeks. While we are working we encourage you to visit [Packages](https://github.com/flet-dev/flet/discussions/categories/packages) and see if the package you need is there. Submitting a request or voting for existing package will help us to prioritize package "recipes".
Thank you!
**Tags:**
  * [releases](https://flet.dev/blog/tags/releases)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2024-05-01-flet-packaging-update.md)
[Newer postFlet at PyCon US 2024](https://flet.dev/blog/flet-at-pycon-us-2024)[Older postControls and theming enhancements](https://flet.dev/blog/controls-and-theming-enhancements)
  * [The problem](https://flet.dev/blog/flet-packaging-update/#the-problem)
    * [Pure-Python packages](https://flet.dev/blog/flet-packaging-update/#pure-python-packages)
    * [Non-pure Python packages](https://flet.dev/blog/flet-packaging-update/#non-pure-python-packages)
  * [Current approach](https://flet.dev/blog/flet-packaging-update/#current-approach)
  * [Packaging 2.0](https://flet.dev/blog/flet-packaging-update/#packaging-20)


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
