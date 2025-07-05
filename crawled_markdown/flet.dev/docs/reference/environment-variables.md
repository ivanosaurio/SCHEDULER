[Skip to main content](https://flet.dev/docs/reference/environment-variables/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search`K`
[![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Extending Flet](https://flet.dev/docs/reference/environment-variables/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/reference/environment-variables/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)
    * [Colors](https://flet.dev/docs/reference/colors)
    * [CLI](https://flet.dev/docs/reference/cli/)
    * [Environment variables](https://flet.dev/docs/reference/environment-variables)
    * [Packages for Android and iOS](https://flet.dev/docs/reference/binary-packages-android-ios)
    * [Icons](https://flet.dev/docs/reference/icons)
    * [Types](https://flet.dev/docs/types)


  * [](https://flet.dev/)
  * [Reference](https://flet.dev/docs/reference)
  * Environment variables


On this page
# Environment variables
Below is the list of useful environment variables and their default values:
#### `FLET_APP_CONSOLE`[​](https://flet.dev/docs/reference/environment-variables/#flet_app_console "Direct link to flet_app_console")
The path to the application's console log file (`console.log`) in the temporary storage directory.
Its value is set in production mode.
#### `FLET_APP_STORAGE_DATA`[​](https://flet.dev/docs/reference/environment-variables/#flet_app_storage_data "Direct link to flet_app_storage_data")
A directory for the storage of persistent application data that is preserved between app updates. It is already pre-created and its location depends on the platform the app is running on.
#### `FLET_APP_STORAGE_TEMP`[​](https://flet.dev/docs/reference/environment-variables/#flet_app_storage_temp "Direct link to flet_app_storage_temp")
A directory for the storage of temporary application files, i.e. cache. It is already pre-created and its location depends on the platform the app is running on.
#### `FLET_ASSETS_DIR`[​](https://flet.dev/docs/reference/environment-variables/#flet_assets_dir "Direct link to flet_assets_dir")
Absolute path to app "assets" directory.
Defaults to `assets`.
#### `FLET_CLI_NO_RICH_OUTPUT`[​](https://flet.dev/docs/reference/environment-variables/#flet_cli_no_rich_output "Direct link to flet_cli_no_rich_output")
Whether to disable rich output in the console.
Default is `"false"`.
#### `FLET_PLATFORM`[​](https://flet.dev/docs/reference/environment-variables/#flet_platform "Direct link to flet_platform")
The platform on which the application is running. Its value is one of the following: `"android"`, `"ios"`, `"linux"`, `"macos"`, `"windows"` or `"fuchsia"`.
#### `FLET_CLI_SKIP_FLUTTER_DOCTOR`[​](https://flet.dev/docs/reference/environment-variables/#flet_cli_skip_flutter_doctor "Direct link to flet_cli_skip_flutter_doctor")
Whether to skip running `flutter doctor` when a build fails.
Default is `False`.
#### `FLET_FORCE_WEB_SERVER`[​](https://flet.dev/docs/reference/environment-variables/#flet_force_web_server "Direct link to flet_force_web_server")
Set to `true` to force running app as a web app. Automatically set on headless Linux hosts.
#### `FLET_OAUTH_CALLBACK_HANDLER_ENDPOINT`[​](https://flet.dev/docs/reference/environment-variables/#flet_oauth_callback_handler_endpoint "Direct link to flet_oauth_callback_handler_endpoint")
Custom path for OAuth handler.
Defaults to `/oauth_callback`.
#### `FLET_OAUTH_STATE_TIMEOUT`[​](https://flet.dev/docs/reference/environment-variables/#flet_oauth_state_timeout "Direct link to flet_oauth_state_timeout")
Maximum allowed time (in seconds) to complete OAuth web flow.
Defaults to `600`.
#### `FLET_MAX_UPLOAD_SIZE`[​](https://flet.dev/docs/reference/environment-variables/#flet_max_upload_size "Direct link to flet_max_upload_size")
Maximum allowed size (in bytes) of uploaded files.
Default is unlimited.
#### `FLET_SECRET_KEY`[​](https://flet.dev/docs/reference/environment-variables/#flet_secret_key "Direct link to flet_secret_key")
A secret key to sign temporary upload URLs.
#### `FLET_SERVER_IP`[​](https://flet.dev/docs/reference/environment-variables/#flet_server_ip "Direct link to flet_server_ip")
IP address to listen web app on, e.g. `127.0.0.1`.
Defaults to `0.0.0.0` - bound to all server IPs.
#### `FLET_SERVER_PORT`[​](https://flet.dev/docs/reference/environment-variables/#flet_server_port "Direct link to flet_server_port")
TCP port to run app on. `8000` if the program is running on a Linux server or `FLET_FORCE_WEB_SERVER` is set; otherwise random port.
#### `FLET_SERVER_UDS_PATH`[​](https://flet.dev/docs/reference/environment-variables/#flet_server_uds_path "Direct link to flet_server_uds_path")
The Unix Domain Socket (UDS) path for the Flet server. It enables inter-process communication on Unix-based systems, with its value being a socket file path in the format `flet_<pid>.sock`.
#### `FLET_SESSION_TIMEOUT`[​](https://flet.dev/docs/reference/environment-variables/#flet_session_timeout "Direct link to flet_session_timeout")
Session lifetime in seconds. Default is `3600`.
#### `FLET_UPLOAD_DIR`[​](https://flet.dev/docs/reference/environment-variables/#flet_upload_dir "Direct link to flet_upload_dir")
Absolute path to app "upload" directory.
#### `FLET_UPLOAD_HANDLER_ENDPOINT`[​](https://flet.dev/docs/reference/environment-variables/#flet_upload_handler_endpoint "Direct link to flet_upload_handler_endpoint")
Custom path for upload handler. Default is `/upload`.
#### `FLET_WEB_APP_PATH`[​](https://flet.dev/docs/reference/environment-variables/#flet_web_app_path "Direct link to flet_web_app_path")
A URL path after domain name to host web app under, e.g. `/apps/myapp`. Default is `/` - host app in the root.
#### `FLET_WEBSOCKET_HANDLER_ENDPOINT`[​](https://flet.dev/docs/reference/environment-variables/#flet_websocket_handler_endpoint "Direct link to flet_websocket_handler_endpoint")
Custom path for WebSocket handler. Default is `/ws`.
#### `FLET_WEB_RENDERER`[​](https://flet.dev/docs/reference/environment-variables/#flet_web_renderer "Direct link to flet_web_renderer")
Web rendering mode: `canvaskit` (default), `html` or `auto`.
#### `FLET_WEB_USE_COLOR_EMOJI`[​](https://flet.dev/docs/reference/environment-variables/#flet_web_use_color_emoji "Direct link to flet_web_use_color_emoji")
Set to `True`, `true` or `1` to load web font with colorful emojis.
#### `FLET_WEB_ROUTE_URL_STRATEGY`[​](https://flet.dev/docs/reference/environment-variables/#flet_web_route_url_strategy "Direct link to flet_web_route_url_strategy")
The URL strategy of the web application: `path` (default) or `hash`.
## Setting Boolean values[​](https://flet.dev/docs/reference/environment-variables/#setting-boolean-values "Direct link to Setting Boolean values")
The boolean `True` is represented by one of the following string values: `"true"`, `"1"` or `"yes"`. Any other value will be interpreted as `False`.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/reference/environment-variables.md)
[Previouspublish](https://flet.dev/docs/reference/cli/publish)[NextPackages for Android and iOS](https://flet.dev/docs/reference/binary-packages-android-ios)
  * [Setting Boolean values](https://flet.dev/docs/reference/environment-variables/#setting-boolean-values)


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
