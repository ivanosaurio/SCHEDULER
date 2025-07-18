[Skip to main content](https://flet.dev/docs/publish/ios/#__docusaurus_skipToContent_fallback)
⭐️ If you like Flet, give it a star on [GitHub](https://github.com/flet-dev/flet) and join the discussion on [Discord](https://discord.gg/dzWXP8SHG8).
[![Flet Logo](https://flet.dev/img/logo.svg)![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)[Docs](https://flet.dev/docs/)[Gallery](https://flet.dev/gallery)[Roadmap](https://flet.dev/roadmap)[Blog](https://flet.dev/blog)
[](https://github.com/flet-dev/flet)
Search
[![Flet Logo](https://flet.dev/img/logo.svg)![Flet Logo](https://flet.dev/img/logo.svg)**Flet**](https://flet.dev/)
  * [Introduction](https://flet.dev/docs/)
  * [Getting started](https://flet.dev/docs/getting-started/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
    * [Android](https://flet.dev/docs/publish/android)
    * [iOS](https://flet.dev/docs/publish/ios)
    * [macOS](https://flet.dev/docs/publish/macos)
    * [Linux](https://flet.dev/docs/publish/linux)
    * [Windows](https://flet.dev/docs/publish/windows)
    * [Web](https://flet.dev/docs/publish/web)
  * [Extending Flet](https://flet.dev/docs/extend/built-in-extensions)
  * [Controls](https://flet.dev/docs/controls)
  * [Cookbook](https://flet.dev/docs/cookbook/theming)
  * [Tutorials](https://flet.dev/docs/tutorials)
  * [Reference](https://flet.dev/docs/reference)


  * [](https://flet.dev/)
  * [Publishing Flet app](https://flet.dev/docs/publish)
  * iOS


On this page
# Packaging app for iOS
## Introduction[​](https://flet.dev/docs/publish/ios/#introduction "Direct link to Introduction")
Flet CLI provides `flet build ipa` command that allows packaging Flet app into an iOS archive bundle and IPA for distribution.
note
The command can be run on macOS only.
## Prerequisites[​](https://flet.dev/docs/publish/ios/#prerequisites "Direct link to Prerequisites")
### Rosetta 2[​](https://flet.dev/docs/publish/ios/#rosetta-2 "Direct link to Rosetta 2")
Flutter requires [Rosetta 2](https://support.apple.com/en-us/HT211861) on Apple silicon:
```
sudo softwareupdate --install-rosetta --agree-to-license
```

### Xcode[​](https://flet.dev/docs/publish/ios/#xcode "Direct link to Xcode")
[Xcode](https://developer.apple.com/xcode/) 15 or later to compile native Swift or ObjectiveC code.
### CocoaPods[​](https://flet.dev/docs/publish/ios/#cocoapods "Direct link to CocoaPods")
[CocoaPods](https://cocoapods.org/) 1.16 to compile and enable Flutter plugins.
### iOS wheels for binary Python packages[​](https://flet.dev/docs/publish/ios/#ios-wheels-for-binary-python-packages "Direct link to iOS wheels for binary Python packages")
Binary Python packages (vs "pure" Python packages written in Python only) are packages that partially written in C, Rust or other languages producing native code. Example packages are `numpy`, `cryptography`, or `pydantic-core`.
Make sure all non-pure (binary) packages used in your Flet app have [pre-built wheels for iOS](https://flet.dev/docs/reference/binary-packages-android-ios).
## `flet build ipa`[​](https://flet.dev/docs/publish/ios/#flet-build-ipa "Direct link to flet-build-ipa")
Build an iOS app archive (`.ipa`) for testing and distribution (macOS host only).
To generate an `.ipa `file for testing on your device or uploading to App Store Connect for distribution, you will need:
  * **Apple Developer Program** subscription with access to App Store Connect.
  * **Application Indentifier**.
  * **Signing Certificate**.
  * **Provisioning Profile**.


## Application Identifier[​](https://flet.dev/docs/publish/ios/#application-identifier "Direct link to Application Identifier")
An **Application Identifier (App ID)** is a unique string that identifies your app within the Apple ecosystem. It is required to sign and distribute an iOS app and is used for various services like **Push Notifications, App Groups, iCloud, and In-App Purchases**.
An App ID consists of two parts:
  1. **Team ID** – A unique 10-character string assigned by Apple to your developer account.
  2. **Bundle ID** – A reverse domain-style identifier for your app (e.g., `com.example.myapp`).


Example of a full App ID:
```
TeamID.com.example.myapp
```

### Creating a new App ID[​](https://flet.dev/docs/publish/ios/#creating-a-new-app-id "Direct link to Creating a new App ID")
  1. Visit [Apple Developer Portal](https://developer.apple.com/account/resources/identifiers/list).
  2. Sign in with your **Apple Developer Account**.
  3. Click the **"+"** button to add a new identifier.
  4. Select **"App IDs"** and click **Continue**.
  5. **Enter a Description** – This is just for reference (e.g., "MyApp Identifier").
  6. **Choose the App ID Type:**
     * Select **"App"** for a standard iOS/macOS app.
     * If you need an identifier for services like Apple Pay or Passbook, select the appropriate option.
  7. **Bundle ID** – Choose: 
     * **Explicit Bundle ID** (`com.example.myapp`) – Recommended for most apps.
     * **Wildcard Bundle ID** (`com.example.*`) – Allows multiple apps to use the same identifier (rarely used).
  8. **Enable App Services** – Check the boxes for any services your app needs (e.g., Push Notifications, Sign in with Apple, etc.).
  9. Click **Continue** and **Register**.


Now you have **Bundle ID** and **Team ID** that must be used to sign iOS bundle.
The next step is creating a **Certificate** and a **Provisioning Profile** to install and distribute your app.
## Signing Certificate[​](https://flet.dev/docs/publish/ios/#signing-certificate "Direct link to Signing Certificate")
### Generating a Certificate Signing Request (CSR)[​](https://flet.dev/docs/publish/ios/#generating-a-certificate-signing-request-csr "Direct link to Generating a Certificate Signing Request \(CSR\)")
Before creating a development or distribution certificate, you need a **CSR (Certificate Signing Request)**.
  1. **Open Keychain Access** on your Mac (`Command ⌘ + Space`, then search for "Keychain Access").
  2. In the top menu, go to **Keychain Access → Certificate Assistant → Request a Certificate From a Certificate Authority…**
  3. Fill in: 
     * **User Email Address:** Your Apple Developer email.
     * **Common Name:** A descriptive name (e.g., "My App Distribution").
     * **CA Email Address:** Leave this blank.
     * **Request is for:** Select "**Saved to disk** ".
  4. Click **Continue** , choose a location to save the `.certSigningRequest` file, and click **Save**.


### Creating a Certificate in Apple Developer Portal[​](https://flet.dev/docs/publish/ios/#creating-a-certificate-in-apple-developer-portal "Direct link to Creating a Certificate in Apple Developer Portal")
  1. Go to [Apple Developer Certificates Page](https://developer.apple.com/account/resources/certificates/list).
  2. Click the **"+"** button to create a new certificate.
  3. Select **"Apple Distribution"** (for App Store & Ad Hoc) or **"Apple Development"** (for development) and click **Continue**.
  4. Upload the **CSR file** you created earlier and click **Continue**.
  5. Apple will generate the certificate. Click **Download** to get the `.cer` file.
  6. Double-click the downloaded `.cer` file to install it in **Keychain Access**.
  7. Open **Keychain Access** app and ensure the certificate is installed under **"login"** keychain. The name of development certificate usually starts with **"Apple development:"** and the name of distribution certificate starts with **"Apple distribution:"**.


## Provisioning Profile[​](https://flet.dev/docs/publish/ios/#provisioning-profile "Direct link to Provisioning Profile")
A **Provisioning Profile** is a file that allows an iOS app to run on physical devices and be distributed through the App Store or internally. It links your **App ID** , **Developer/Distribution Certificate** , and **Registered Devices**.
There are different types of provisioning profiles:
  * **Development Profile** – Used for testing on physical devices.
  * **Ad Hoc Profile** – Used for distributing an app outside the App Store to specific devices.
  * **App Store Profile** – Used for submitting an app to the App Store.
  * **Enterprise Profile** – Used for internal distribution within an organization.


### Creating a new Provisioning Profile[​](https://flet.dev/docs/publish/ios/#creating-a-new-provisioning-profile "Direct link to Creating a new Provisioning Profile")
**Step 1: Go to Apple Developer Portal**
  1. Visit [Apple Developer Portal](https://developer.apple.com/account/resources/profiles/list).
  2. Sign in with your **Apple Developer Account**.


**Step 2: Create a New Provisioning Profile**
  1. Click the **"+"** button to add a new provisioning profile.
  2. Choose the **type of profile** : 
     * Select **"iOS App Development"** for testing on devices.
     * Select **"Ad Hoc"** for distributing to specific devices.
     * Select **"App Store"** for submitting an app to the App Store.
     * Select **"In-House"** (Enterprise accounts only) for internal distribution.
  3. Click **Continue**.


**Step 3: Select an App ID**
  1. Choose the **App ID** that matches your app.
  2. Click **Continue**.


**Step 4: Select a Distribution Certificate**
  1. Choose the **iOS Distribution Certificate** or **Development Certificate** (depending on the profile type).
  2. Click **Continue**.


**Step 5: Select Registered Devices (For Development & Ad Hoc)**
  1. If you selected **Development** or **Ad Hoc** , choose the devices that can run the app.
  2. Click **Continue**.


**Step 6: Name and Generate the Profile**
  1. Enter a **Profile Name** (e.g., "MyApp Development Profile").
  2. Click **Generate**.
  3. Click **Download** to get the `.mobileprovision` file.


### Installing Provisioning Profile[​](https://flet.dev/docs/publish/ios/#installing-provisioning-profile "Direct link to Installing Provisioning Profile")
Provisioning profiles are stored in `~/Library/MobileDevice/Provisioning Profiles` directory.
To install downloaded provisioning profile just copy it to `~/Library/MobileDevice/Provisioning\ Profiles` directory with a new `{UUID}.mobileprovision` name.
Run the following command to get profile UUID:
```
profile_uuid=$(security cms -D -i ~/Downloads/{profile-name}.mobileprovision | xmllint --xpath "string(//key[.='UUID']/following-sibling::string[1])" -)echo $profile_uuid
```

Run this command to copy profile to `~/Library/MobileDevice/Provisioning Profiles` with a new name `{UUID}.mobileprovision`:
```
cp ~/Downloads/{profile-name}.mobileprovision ~/Library/MobileDevice/Provisioning\ Profiles/${profile_uuid}.mobileprovision
```

warning
If the copied profile disappears from the `~/Library/MobileDevice/Provisioning Profiles` directory, ensure that the Xcode process is not running in the background.
Finally, you can use this command to list all installed provisioning profiles, with their names and UUIDs:
```
for profile in ~/Library/MobileDevice/Provisioning\ Profiles/*.mobileprovision; do security cms -D -i "$profile" | grep -E -A1 '<key>(Name|UUID)</key>' | sed -n 's/.*<string>\(.*\)<\/string>/\1/p' | paste -d ' | ' - -; done
```

## Configuring build[​](https://flet.dev/docs/publish/ios/#configuring-build "Direct link to Configuring build")
To can either pass .ipa build options via `flet build` command line or configure in `pyproject.toml`.
### Command line[​](https://flet.dev/docs/publish/ios/#command-line "Direct link to Command line")
To successfully generate "runnable" IPA you should provide correct values for the following arguments:
  * `--ios-export-method` - specifies how the app should be packaged when exporting an `.ipa` file. Default is `debugging`. Can be one of the following: 
    * `debugging` (or deprecated `development`) - used for debugging and testing on development devices.
    * `release-testing` (or deprecated `ad-hoc`) - used for distributing the app outside the App Store to specific registered devices.
    * `app-store-connect` (or deprecated `app-store`) - used for submitting the app to the App Store.
    * `enterprise` - used for internal distribution within an organization (requires an enterprise account).
  * `--ios-provisioning-profile` - provisioning profile name or UUID that used to sign and export an iOS app.
  * `--ios-signing-certificate` - certificate name, SHA-1 hash, or automatic selector to use for signing iOS app bundle. Automatic selectors allow Xcode to pick the newest installed certificate of a particular type. The available automatic selectors are "Apple Development", "Apple Distribution", "Developer ID Application", "iOS Developer", "iOS Distribution", "Mac App Distribution", and "Mac Developer".
  * `--ios-team-id` - developer team ID to export iOS app.
  * `--bundle-id` - bundle ID for the application, e.g. "com.mycompany.app-name" - used as an iOS, Android, macOS and Linux bundle ID.
  * `--org` - organization name in reverse domain name notation, e.g. `com.mycompany` (defaults to `com.flet`). The value is combined with `--project` and used as an iOS and Android bundle ID.
  * `--project` - project name in C-style identifier format (lowercase alphanumerics with underscores) used to build bundle ID and as a name for bundle executable. By default, it's the name of Flet app directory.


Development package
To build `.ipa` for testing on your developer device you need to provide `--ios-provisioning-profile` option only. `flet build` will assume `debugging` as an export method and automatically choose the most recent "Apple Development" certificate in your keychain. Team ID is not required.
Bundle ID or Org?
You can specify either `--bundle-id`, `--org`, or both.
  * If only the `--bundle-id` is provided and "--org" is not, the organization name is derived from the bundle ID by extracting the part before the last dot.
  * If only `--org` is specified and the "--bundle-id" is not, the bundle ID is generated as `{org}.{project_name}`.


### `pyproject.toml`[​](https://flet.dev/docs/publish/ios/#pyprojecttoml "Direct link to pyprojecttoml")
You can also configure package export and signing settings in `pyproject.toml`.
Project name and org:
```
[project]name = "my-app"[tool.flet]org = "com.mycompany"
```

or bundle ID:
```
[tool.flet]bundle_id = "com.mycompany.example-app"
```

Both `org` and `bundle_id` could be platform-specific, for example:
```
[tool.flet.ios]bundle_id = "com.mycompany.example-app-ios"[tool.flet.android]bundle_id = "com.mycompany.example-app-android"
```

To configure iOS signing settings that will be globally applied to all export methods:
```
[tool.flet.ios]provisioning_profile = "release-testing com.mycompany.example-app"signing_certificate = "Apple Distribution"team_id = "ABCDEFE234"export_options = { uploadSymbols = false }
```

To configure signing settings per export methods:
```
[tool.flet.ios.export_methods."debugging"]provisioning_profile = "debugging com.mycompany.example-app"signing_certificate = "Apple Development"[tool.flet.ios.export_methods."release-testing"]provisioning_profile = "release-testing com.mycompany.example-app"team_id = "ABCDEFE234"signing_certificate = "Apple Distribution"export_options = { uploadSymbols = false }[tool.flet.ios.export_methods."app-store-connect"]provisioning_profile = "app-store-connect com.mycompany.example-app"team_id = "ABCDEFE234"signing_certificate = "Apple Distribution"export_options = { uploadSymbols = true }
```

With the settings above you can run `flet build` command with just `--ios-export-method` provided, for example:
```
flet build ipa --ios-export-method release-testing
```

## Deploying app to an Apple device for testing[​](https://flet.dev/docs/publish/ios/#deploying-app-to-an-apple-device-for-testing "Direct link to Deploying app to an Apple device for testing")
Apple Configurator for macOS allows you to install `.ipa` files on iOS devices without using the App Store.
Follow these steps to deploy an `.ipa` file to your device:
**Step 1: Install Apple Configurator**
  1. Install [Apple Configurator](https://apps.apple.com/ca/app/apple-configurator/id1037126344?mt=12) from App Store.


**Step 2: Connect the iOS Device**
  1. Connect the **iPhone** or **iPad** to your Mac using a USB cable.
  2. Unlock the device and **Trust** the computer if prompted.


**Step 3: Open Apple Configurator**
  1. Launch **Apple Configurator** on your Mac.
  2. The connected device should appear in the main window.


**Step 4: Add the`.ipa` File**
  1. Drag and drop the `.ipa` file onto the connected device in Apple Configurator.
  2. Alternatively, click **Add → Apps** , then choose the `.ipa` file from your Mac.


**Step 5: Install the App**
  1. Click **Prepare** or **Install** to begin the deployment.
  2. Apple Configurator will install the app on the device.


**Step 6: Trust the Developer Profile (For Ad Hoc or Enterprise Apps)**
If the `.ipa` is installed from an **Ad Hoc or Enterprise profile** , you may need to manually trust the developer:
  1. On the iOS device, go to **Settings → General → VPN & Device Management**.
  2. Under **Developer App** , select your **Developer Profile**.
  3. Tap **Trust** and confirm.


## Uploading app to App Store Connect for distribution[​](https://flet.dev/docs/publish/ios/#uploading-app-to-app-store-connect-for-distribution "Direct link to Uploading app to App Store Connect for distribution")
**Transporter** is a macOS app that allows you to upload `.ipa` files to **App Store Connect** for distribution.
**Step 1: Install Transporter**
  1. Install [Transporter](https://apps.apple.com/us/app/transporter/id1450874784) from App Store.


**Step 2: Prepare the`.ipa` File**
  1. Ensure your `.ipa` file is built with either **app-store-connect** or **release-testing** export methods.


**Step 3: Open Transporter and Sign In**
  1. Launch **Transporter** on your Mac.
  2. Sign in with your **Apple Developer Account** (the same one used for App Store Connect).


**Step 4: Upload the`.ipa` File**
  1. Drag and drop the `.ipa` file into the Transporter window.
  2. Alternatively, click **Add App** , then choose the `.ipa` file from your Mac.
  3. Click `...` button next to "Deliver" and choose "Verify".
  4. Wait for Transporter to **verify** the file.
  5. Click **"Deliver"** to start the upload.


**Step 5: Check Upload Status**
  1. Once the upload is complete, Transporter will display a **success message**.
  2. If there are errors, review them and correct any issues before retrying the upload.


**Step 6: Confirm in App Store Connect**
  1. Go to [App Store Connect](https://appstoreconnect.apple.com/).
  2. Navigate to **Apps → Your App → TestFlight or App Store Version**.
  3. The uploaded build should appear under **Processing** (this may take a few minutes to an hour).
  4. Once processing is complete, you can **submit the app for review**.


## Permissions[​](https://flet.dev/docs/publish/ios/#permissions "Direct link to Permissions")
Setting iOS permissions which are written into `Info.plist` file:
```
flet build --info-plist permission_1=True|False|description permission_2=True|False|description ...
```

For example:
```
flet build --info-plist NSLocationWhenInUseUsageDescription="This app uses location service when in use."
```

Configuring iOS permissions in `pyproject.toml`:
```
[tool.flet.ios.info] # --info-plistNSCameraUsageDescription = "This app uses the camera to ..."
```

## Deep linking[​](https://flet.dev/docs/publish/ios/#deep-linking "Direct link to Deep linking")
You can configure deep-linking settings for iOS bundle with the following `flet build` options:
  * `--deep-linking-scheme` - deep linking URL scheme to configure for iOS and Android builds, i.g. "https" or "myapp".
  * `--deep-linking-host` - deep linking URL host.


The same can be configured in `pyproject.toml`:
```
[tool.flet.ios.deep_linking]scheme = "https"host = "mydomain.com"
```

See [Deep linking](https://docs.flutter.dev/ui/navigation/deep-linking) section in Flutter docs for more information and complete setup guide.
[Edit this page](https://github.com/flet-dev/website/edit/main/docs/publish/ios.md)
[PreviousAndroid](https://flet.dev/docs/publish/android)[NextmacOS](https://flet.dev/docs/publish/macos)
  * [Introduction](https://flet.dev/docs/publish/ios/#introduction)
  * [Prerequisites](https://flet.dev/docs/publish/ios/#prerequisites)
    * [Rosetta 2](https://flet.dev/docs/publish/ios/#rosetta-2)
    * [Xcode](https://flet.dev/docs/publish/ios/#xcode)
    * [CocoaPods](https://flet.dev/docs/publish/ios/#cocoapods)
    * [iOS wheels for binary Python packages](https://flet.dev/docs/publish/ios/#ios-wheels-for-binary-python-packages)
  * [`flet build ipa`](https://flet.dev/docs/publish/ios/#flet-build-ipa)
  * [Application Identifier](https://flet.dev/docs/publish/ios/#application-identifier)
    * [Creating a new App ID](https://flet.dev/docs/publish/ios/#creating-a-new-app-id)
  * [Signing Certificate](https://flet.dev/docs/publish/ios/#signing-certificate)
    * [Generating a Certificate Signing Request (CSR)](https://flet.dev/docs/publish/ios/#generating-a-certificate-signing-request-csr)
    * [Creating a Certificate in Apple Developer Portal](https://flet.dev/docs/publish/ios/#creating-a-certificate-in-apple-developer-portal)
  * [Provisioning Profile](https://flet.dev/docs/publish/ios/#provisioning-profile)
    * [Creating a new Provisioning Profile](https://flet.dev/docs/publish/ios/#creating-a-new-provisioning-profile)
    * [Installing Provisioning Profile](https://flet.dev/docs/publish/ios/#installing-provisioning-profile)
  * [Configuring build](https://flet.dev/docs/publish/ios/#configuring-build)
    * [Command line](https://flet.dev/docs/publish/ios/#command-line)
    * [`pyproject.toml`](https://flet.dev/docs/publish/ios/#pyprojecttoml)
  * [Deploying app to an Apple device for testing](https://flet.dev/docs/publish/ios/#deploying-app-to-an-apple-device-for-testing)
  * [Uploading app to App Store Connect for distribution](https://flet.dev/docs/publish/ios/#uploading-app-to-app-store-connect-for-distribution)
  * [Permissions](https://flet.dev/docs/publish/ios/#permissions)
  * [Deep linking](https://flet.dev/docs/publish/ios/#deep-linking)


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
