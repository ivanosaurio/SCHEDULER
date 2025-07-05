[Skip to main content](https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting/#__docusaurus_skipToContent_fallback)
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
        * [Hosting](https://flet.dev/docs/publish/web/dynamic-website/hosting)
          * [Fly.io](https://flet.dev/docs/publish/web/dynamic-website/hosting/fly-io)
          * [Replit](https://flet.dev/docs/publish/web/dynamic-website/hosting/replit)
          * [Self Hosting](https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting)
  * [Extending Flet](https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting/)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting/)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * [Web](https://flet.dev/docs/publish/web)
  * [Dynamic website](https://flet.dev/docs/publish/web/dynamic-website)
  * [Hosting](https://flet.dev/docs/publish/web/dynamic-website/hosting)
  * Self Hosting


On this page
# Self Hosting
Host a Flet app on your own server with NGINX.
There are free and inexpensive cloud server tiers available at [AWS](https://aws.amazon.com/free/), [Oracle](https://www.oracle.com/cloud/free/), [Linode](https://www.linode.com/pricing/), and more.
## Setup Flet Environment[​](https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting/#setup-flet-environment "Direct link to Setup Flet Environment")
### `requirements.txt` and virtualenv[​](https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting/#requirementstxt-and-virtualenv "Direct link to requirementstxt-and-virtualenv")
Create `requirements.txt` with a list of application dependencies. At minimum it should contain `flet` module:
```
flet
```

Create a virtualenv and install requirements:
```
python -m venv .venvsource .venv/bin/activatepip install -r requirements.txt
```

### Sample Flet app[​](https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting/#sample-flet-app "Direct link to Sample Flet app")
```
import flet as ftdefmain(page: ft.Page):  page.title ="My Flet app"  page.add(ft.Text("Hello, world!"))if __name__ =="__main__":  ft.app(main)
```

Flet app will be served from the root URL, but you can configure `FLET_WEB_APP_PATH` environment variable to serve beneath the root e.g. `/apps/myapp`.
By default, Flet web app will be running on port `8000`, but you can change that by setting up `FLET_SERVER_PORT` environment variable.
[Complete list of environment variables](https://flet.dev/docs/publish/web/dynamic-website#environment-variables) supported by a web app.
## Automatically start Flet app[​](https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting/#automatically-start-flet-app "Direct link to Automatically start Flet app")
### Create `systemd` unit file[​](https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting/#create-systemd-unit-file "Direct link to create-systemd-unit-file")
Automatically start the Flet app using a `systemd` service unit file `flet.service`.
Setup below assumes your Flet app script is defined in `$HOME/flet-app/main.py`. Replace `User`, `Group`, `WorkingDirectory`, etc. as per your setup.
```
[Unit]Description=Flet AppAfter=network.target[Service]User=ubuntuGroup=ubuntuWorkingDirectory=/home/ubuntu/flet-appEnvironment="PATH=/home/ubuntu/flet-app/.venv/bin"ExecStart=/home/ubuntu/flet-app/.venv/bin/python /home/ubuntu/flet-app/main.py[Install]WantedBy=multi-user.target
```

### Enable Flet app service[​](https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting/#enable-flet-app-service "Direct link to Enable Flet app service")
```
cd /etc/systemd/systemsudo ln -s /home/ubuntu/flet-app/flet.servicesudo systemctl start fletsudo systemctl enable fletsudo systemctl status flet
```

## NGINX Proxy Setup[​](https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting/#nginx-proxy-setup "Direct link to NGINX Proxy Setup")
NGINX will proxy the Flet app and the websocket.
In your `/etc/nginx/sites-available/*` config file, updating path and port as needed:
```
  location / {    proxy_pass     http://127.0.0.1:8000/;    proxy_http_version 1.1;    proxy_set_header  Upgrade $http_upgrade;    proxy_set_header  Connection keep-alive;    proxy_set_header  Host $host;    proxy_cache_bypass $http_upgrade;    proxy_set_header  X-Forwarded-For $proxy_add_x_forwarded_for;    proxy_set_header  X-Forwarded-Proto $scheme;  }  location /ws {    proxy_pass     http://127.0.0.1:8000/ws;    proxy_http_version 1.1;    proxy_set_header  Upgrade $http_upgrade;    proxy_set_header  Connection "upgrade";    proxy_set_header  Host $host;    proxy_cache_bypass $http_upgrade;    proxy_set_header  X-Forwarded-For $proxy_add_x_forwarded_for;    proxy_set_header  X-Forwarded-Proto $scheme;  }
```

That's it! Restart NGINX, and open your app in a browser.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/publish/web/dynamic-website/hosting/self-hosting.md)
[PreviousReplit](https://flet.dev/docs/publish/web/dynamic-website/hosting/replit)[NextBuilt-in extensions](https://flet.dev/docs/extend/built-in-extensions)
  * [Setup Flet Environment](https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting/#setup-flet-environment)
    * [`requirements.txt` and virtualenv](https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting/#requirementstxt-and-virtualenv)
    * [Sample Flet app](https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting/#sample-flet-app)
  * [Automatically start Flet app](https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting/#automatically-start-flet-app)
    * [Create `systemd` unit file](https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting/#create-systemd-unit-file)
    * [Enable Flet app service](https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting/#enable-flet-app-service)
  * [NGINX Proxy Setup](https://flet.dev/docs/publish/web/dynamic-website/hosting/self-hosting/#nginx-proxy-setup)


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
