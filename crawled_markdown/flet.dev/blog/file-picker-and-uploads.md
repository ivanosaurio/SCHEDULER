[Skip to main content](https://flet.dev/blog/file-picker-and-uploads/#__docusaurus_skipToContent_fallback)
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


# File picker and uploads
September 2, 2022 · 4 min read
[![Feodor Fitsner](https://avatars0.githubusercontent.com/u/5041459?s=400&v=4)](ttps://github.com/FeodorFitsner)
[Feodor Fitsner](ttps://github.com/FeodorFitsner)
Flet founder and developer
[](https://github.com/FeodorFitsner "GitHub")[](https://x.com/fletdev "X")
Finally, File picker with uploads has arrived! 🎉
File picker control opens a native OS dialog for selecting files and directories. It's based on a fantastic [file_picker](https://pub.dev/packages/file_picker) Flutter package.
It works on all platforms: Web, macOS, Window, Linux, iOS and Android.
![](https://flet.dev/img/docs/controls/file-picker/file-picker-all-modes-demo.png)
Check out [source code of the demo above](https://github.com/flet-dev/examples/blob/main/python/controls/file-picker/file-picker-all-modes.py).
File picker allows opening three dialogs:
  * **Pick files** - one or multiple, any files or only specific types.
  * **Save file** - choose directory and file name.
  * **Get directory** - select directory.


When running Flet app in a browser only "Pick files" option is available and it's used for uploads only as it, obviously, doesn't return a full path to a selected file.
Where file picker really shines is a desktop! All three dialogs return full paths to selected files and directories - great assistance to your users!
## Using file picker in your app[​](https://flet.dev/blog/file-picker-and-uploads/#using-file-picker-in-your-app "Direct link to Using file picker in your app")
It is recommended to add file picker to [`page.overlay.controls`](https://flet.dev/docs/controls/page#overlay) collection, so it doesn't affect the layout of your app. Despite file picker has 0x0 size it is still considered as a control when put into `Row` or `Column`.
```
import flet as ftfile_picker = ft.FilePicker()page.overlay.append(file_picker)page.update()
```

To open file picker dialog call one of the three methods:
  * `pick_files()`
  * `save_file()`
  * `get_directory_path()`


Lambda works pretty nice for that:
```
ft.ElevatedButton("Choose files...",  on_click=lambda_: file_picker.pick_files(allow_multiple=True))
```

When dialog is closed `FilePicker.on_result` event handler is called which event object has one of the following properties set:
  * `files` - "Pick files" dialog only, a list of selected files or `None` if dialog was cancelled.
  * `path` - "Save file" and "Get directory" dialogs, a full path to a file or directory or `None` if dialog was cancelled.


```
import flet as ftdefon_dialog_result(e: ft.FilePickerResultEvent):print("Selected files:", e.files)print("Selected file or directory:", e.path)file_picker = ft.FilePicker(on_result=on_dialog_result)
```

The last result is always available in `FilePicker.result` property.
Check [File picker](https://flet.dev/docs/controls/filepicker) control docs for all available dialog methods and their parameters.
## Uploading files[​](https://flet.dev/blog/file-picker-and-uploads/#uploading-files "Direct link to Uploading files")
File picker has built-in upload capabilities that work on all platforms and the web.
To upload one or more files you should call `FilePicker.pick_files()` first. When the files are selected by the user they are not automatically uploaded anywhere, but instead their references are kept in the file picker state.
To perform an actual upload you should call `FilePicker.upload()` method and pass the list of files that need to be uploaded along with their upload URLs and upload method (`PUT` or `POST`):
```
import flet as ftdefupload_files(e):  upload_list =[]if file_picker.result !=Noneand file_picker.result.files !=None:for f in file_picker.result.files:      upload_list.append(        FilePickerUploadFile(          f.name,          upload_url=page.get_upload_url(f.name,600),))    file_picker.upload(upload_list)ft.ElevatedButton("Upload", on_click=upload_files)
```

note
If you need to separate uploads for each user you can specify a filename prepended with any number of directories in `page.get_upload_url()` call, for example:
```
upload_url = page.get_upload_url(f"/{username}/pictures/{f.name}",600)
```

`/{username}/pictures` directories will be automatically created inside `upload_dir` if not exist.
### Upload storage[​](https://flet.dev/blog/file-picker-and-uploads/#upload-storage "Direct link to Upload storage")
Notice the usage of `page.get_upload_url()` method - it generates a presigned upload URL for Flet's internal upload storage.
Use any storage for file uploads
You can [generate presigned upload URL](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html#generating-a-presigned-url-to-upload-a-file) for AWS S3 storage using boto3 library.
The same technique should work for [Wasabi](https://wasabi.com/), [Backblaze](https://www.backblaze.com/), [MinIO](https://min.io/) and any other storage providers with S3-compatible API.
To enable Flet saving uploaded files to a directory provide full or relative path to that directory in `flet.app()` call:
```
ft.app(target=main, upload_dir="uploads")
```

You can even put uploads inside "assets" directory, so uploaded files, e.g. pictures, docs or other media, can be accessed from a Flet client right away:
```
ft.app(target=main, assets_dir="assets", upload_dir="assets/uploads")
```

and somewhere in your app you can display uploaded picture with:
```
page.add(ft.Image(src="/uploads/<some-uploaded-picture.png>"))
```

### Upload progress[​](https://flet.dev/blog/file-picker-and-uploads/#upload-progress "Direct link to Upload progress")
Once `FilePicker.upload()` method is called Flet client asynchronously starts uploading selected files one-by-one and reports the progress via `FilePicker.on_upload` callback.
Event object of `on_upload` event is an instance of `FilePickerUploadEvent` class with the following fields:
  * `file_name`
  * `progress` - a value from `0.0` to `1.0`.
  * `error`


The callback is called at least twice for every uploaded file: with `0` progress before upload begins and with `1.0` progress when upload is finished. For files larger than 1 MB a progress is additionally reported for every 10% uploaded.
Check that [example](https://github.com/flet-dev/examples/blob/main/python/controls/file-picker/file-picker-upload-progress.py) demonstrating multiple file uploads:
![](https://flet.dev/img/docs/controls/file-picker/file-picker-multiple-uploads.png)
See [File picker](https://flet.dev/docs/controls/filepicker) control docs for all its properties and examples.
Upgrade Flet module to the latest version (`pip install flet --upgrade`), give File Picker a try and [let us know](https://discord.gg/dzWXP8SHG8) what you think!
Enjoy!
**Tags:**
  * [release](https://flet.dev/blog/tags/release)


[Edit this page](https://github.com/flet-dev/website/edit/main/blog/2022-09-02-file-picker-and-uploads.md)
[Newer postUser authentication](https://flet.dev/blog/user-authentication)[Older postFun with animations](https://flet.dev/blog/fun-with-animations)
  * [Using file picker in your app](https://flet.dev/blog/file-picker-and-uploads/#using-file-picker-in-your-app)
  * [Uploading files](https://flet.dev/blog/file-picker-and-uploads/#uploading-files)
    * [Upload storage](https://flet.dev/blog/file-picker-and-uploads/#upload-storage)
    * [Upload progress](https://flet.dev/blog/file-picker-and-uploads/#upload-progress)


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
