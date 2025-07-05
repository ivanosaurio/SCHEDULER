[Skip to main content](https://flet.dev/docs/cookbook/file-picker-and-uploads/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/cookbook/file-picker-and-uploads/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/cookbook/file-picker-and-uploads/)
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
  * File picker and uploads


On this page
# File picker and uploads
[File picker](https://flet.dev/docs/controls/filepicker) control opens a native OS dialog for selecting files and directories.
It works on all platforms: Web, macOS, Window, Linux, iOS and Android.
![](https://flet.dev/img/docs/controls/file-picker/file-picker-all-modes-demo.png)
Check out [source code of the demo above](https://github.com/flet-dev/examples/blob/main/python/controls/file-picker/file-picker-all-modes.py).
File picker allows opening three dialogs:
  * **Pick files** - one or multiple, any files or only specific types.
  * **Save file** - choose directory and file name.
  * **Get directory** - select directory.


When running Flet app in a browser only "Pick files" option is available and it's used for uploads only as it, obviously, doesn't return a full path to a selected file.
Where file picker really shines is a desktop! All three dialogs return full paths to selected files and directories - great assistance to your users!
info
In Linux, the FilePicker control depends on [Zenity](https://help.gnome.org/users/zenity/stable/) when running Flet as an app. This is not a requirement when running Flet in a browser.
To install Zenity on Ubuntu/Debian run the following commands:
```
sudoapt-getinstallzenity
```

## Using file picker in your app[​](https://flet.dev/docs/cookbook/file-picker-and-uploads/#using-file-picker-in-your-app "Direct link to Using file picker in your app")
It is recommended to add file picker to [`page.overlay`](https://flet.dev/docs/controls/page#overlay) collection, so it doesn't affect the layout of your app. Despite file picker has 0x0 size it is still considered as a control when put into `Row` or `Column`.
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
## Uploading files[​](https://flet.dev/docs/cookbook/file-picker-and-uploads/#uploading-files "Direct link to Uploading files")
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
### Upload storage[​](https://flet.dev/docs/cookbook/file-picker-and-uploads/#upload-storage "Direct link to Upload storage")
Notice the usage of `page.get_upload_url()` method - it generates a presigned upload URL for Flet's internal upload storage.
Use any storage for file uploads
You can [generate presigned upload URL](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html#generating-a-presigned-url-to-upload-a-file) for AWS S3 storage using boto3 library.
The same technique should work for [Wasabi](https://wasabi.com/), [Backblaze](https://www.backblaze.com/), [MinIO](https://min.io/) and any other storage providers with S3-compatible API.
To enable Flet saving uploaded files to a directory provide full or relative path to that directory in `flet.app()` call:
```
ft.app(main, upload_dir="uploads")
```

You can even put uploads inside "assets" directory, so uploaded files, e.g. pictures, docs or other media, can be accessed from a Flet client right away:
```
ft.app(main, assets_dir="assets", upload_dir="assets/uploads")
```

and somewhere in your app you can display uploaded picture with:
```
page.add(ft.Image(src="/uploads/<some-uploaded-picture.png>"))
```

### Upload progress[​](https://flet.dev/docs/cookbook/file-picker-and-uploads/#upload-progress "Direct link to Upload progress")
Once `FilePicker.upload()` method is called Flet client asynchronously starts uploading selected files one-by-one and reports the progress via `FilePicker.on_upload` callback.
Event object of `on_upload` event is an instance of `FilePickerUploadEvent` class with the following fields:
  * `file_name`
  * `progress` - a value from `0.0` to `1.0`.
  * `error`


The callback is called at least twice for every uploaded file: with `0` progress before upload begins and with `1.0` progress when upload is finished. For files larger than 1 MB a progress is additionally reported for every 10% uploaded.
Check that [example](https://github.com/flet-dev/examples/blob/main/python/controls/file-picker/file-picker-upload-progress.py) demonstrating multiple file uploads:
![](https://flet.dev/img/docs/controls/file-picker/file-picker-multiple-uploads.png)
See [File picker](https://flet.dev/docs/controls/filepicker) control docs for all its properties and examples.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/cookbook/file-picker-and-uploads.md)
[PreviousDrag and drop](https://flet.dev/docs/cookbook/drag-and-drop)[NextAnimations](https://flet.dev/docs/cookbook/animations)
  * [Using file picker in your app](https://flet.dev/docs/cookbook/file-picker-and-uploads/#using-file-picker-in-your-app)
  * [Uploading files](https://flet.dev/docs/cookbook/file-picker-and-uploads/#uploading-files)
    * [Upload storage](https://flet.dev/docs/cookbook/file-picker-and-uploads/#upload-storage)
    * [Upload progress](https://flet.dev/docs/cookbook/file-picker-and-uploads/#upload-progress)


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
