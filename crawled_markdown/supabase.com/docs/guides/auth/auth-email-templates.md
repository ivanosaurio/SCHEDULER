[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
  * [Start](https://supabase.com/docs/guides/getting-started)
  * Products 
  * Build 
  * Manage 
  * Reference 
  * Resources 


[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
Search docs...
K
[Sign up](https://supabase.com/dashboard)
Main menu
[Auth](https://supabase.com/docs/guides/auth/auth-email-templates)
  * [Overview](https://supabase.com/docs/guides/auth)
  * [Architecture](https://supabase.com/docs/guides/auth/architecture)
Getting Started
  * [Next.js](https://supabase.com/docs/guides/auth/quickstarts/nextjs)
  * [React](https://supabase.com/docs/guides/auth/quickstarts/react)
  * [React Native](https://supabase.com/docs/guides/auth/quickstarts/react-native)
Concepts
  * [Users](https://supabase.com/docs/guides/auth/users)
  * [Identities](https://supabase.com/docs/guides/auth/identities)
  * [Sessions](https://supabase.com/docs/guides/auth/sessions)
Flows (How-tos)
  * [Server-Side Rendering](https://supabase.com/docs/guides/auth/server-side)
  * [Password-based](https://supabase.com/docs/guides/auth/passwords)
  * [Email (Magic Link or OTP)](https://supabase.com/docs/guides/auth/auth-email-passwordless)
  * [Phone Login](https://supabase.com/docs/guides/auth/phone-login)
  * [Social Login (OAuth)](https://supabase.com/docs/guides/auth/social-login)
  * [Enterprise SSO](https://supabase.com/docs/guides/auth/enterprise-sso)
  * [Anonymous Sign-Ins](https://supabase.com/docs/guides/auth/auth-anonymous)
  * [Web3 (Sign in with Solana)](https://supabase.com/docs/guides/auth/auth-web3)
  * [Mobile Deep Linking](https://supabase.com/docs/guides/auth/native-mobile-deep-linking)
  * [Identity Linking](https://supabase.com/docs/guides/auth/auth-identity-linking)
  * [Multi-Factor Authentication](https://supabase.com/docs/guides/auth/auth-mfa)
  * [Signout](https://supabase.com/docs/guides/auth/signout)
Debugging
  * [Error Codes](https://supabase.com/docs/guides/auth/debugging/error-codes)
Third-party auth
  * [Overview](https://supabase.com/docs/guides/auth/third-party/overview)
  * [Clerk](https://supabase.com/docs/guides/auth/third-party/clerk)
  * [Firebase Auth](https://supabase.com/docs/guides/auth/third-party/firebase-auth)
  * [Auth0](https://supabase.com/docs/guides/auth/third-party/auth0)
  * [AWS Cognito (Amplify)](https://supabase.com/docs/guides/auth/third-party/aws-cognito)
  * [WorkOS](https://supabase.com/docs/guides/auth/third-party/workos)
Configuration
  * [General Configuration](https://supabase.com/docs/guides/auth/general-configuration)
  * [Email Templates](https://supabase.com/docs/guides/auth/auth-email-templates)
  * [Redirect URLs](https://supabase.com/docs/guides/auth/redirect-urls)
  * [Auth Hooks](https://supabase.com/docs/guides/auth/auth-hooks)
  * [Custom SMTP](https://supabase.com/docs/guides/auth/auth-smtp)
  * [User Management](https://supabase.com/docs/guides/auth/managing-user-data)
Security
  * [Password Security](https://supabase.com/docs/guides/auth/password-security)
  * [Rate Limits](https://supabase.com/docs/guides/auth/rate-limits)
  * [Bot Detection (CAPTCHA)](https://supabase.com/docs/guides/auth/auth-captcha)
  * [JWTs](https://supabase.com/docs/guides/auth/jwts)
  * [JWT Fields Reference](https://supabase.com/docs/guides/auth/jwt-fields)
  * [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security)
  * [Column Level Security](https://supabase.com/docs/guides/database/postgres/column-level-security)
  * [Custom Claims & RBAC](https://supabase.com/docs/guides/database/postgres/custom-claims-and-role-based-access-control-rbac)
Auth UI
  * [Auth UI (Deprecated)](https://supabase.com/docs/guides/auth/auth-helpers/auth-ui)
  * [Flutter Auth UI](https://supabase.com/docs/guides/auth/auth-helpers/flutter-auth-ui)


[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
  * [Start](https://supabase.com/docs/guides/getting-started)
  * Products 
  * Build 
  * Manage 
  * Reference 
  * Resources 


[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
Search docs...
K
[Sign up](https://supabase.com/dashboard)
Auth
  1. Auth
  2. Configuration
  3. [Email Templates](https://supabase.com/docs/guides/auth/auth-email-templates)


Email Templates
Learn how to manage the email templates in Supabase.
You can customize the email messages used for the authentication flows. You can edit the following email templates:
  * Confirm signup
  * Invite user
  * Magic Link
  * Change Email Address
  * Reset Password


## Terminology[#](https://supabase.com/docs/guides/auth/auth-email-templates#terminology)
The templating system provides the following variables for use:
Name| Description  
---|---  
`{{ .ConfirmationURL }}`| Contains the confirmation URL. For example, a signup confirmation URL would look like: `https://project-ref.supabase.co/auth/v1/verify?token={{ .TokenHash }}&type=email&redirect_to=https://example.com/path` .  
`{{ .Token }}`| Contains a 6-digit One-Time-Password (OTP) that can be used instead of the `{{. ConfirmationURL }}` .  
`{{ .TokenHash }}`| Contains a hashed version of the `{{ .Token }}`. This is useful for constructing your own email link in the email template.  
`{{ .SiteURL }}`| Contains your application's Site URL. This can be configured in your project's [authentication settings](https://supabase.com/dashboard/project/_/auth/url-configuration).  
`{{ .RedirectTo }}`| Contains the redirect URL passed when `signUp`, `signInWithOtp`, `signInWithOAuth`, `resetPasswordForEmail` or `inviteUserByEmail` is called. The redirect URL allow list can be configured in your project's [authentication settings](https://supabase.com/dashboard/project/_/auth/url-configuration).  
`{{ .Data }}`| Contains metadata from `auth.users.user_metadata`. Use this to personalize the email message.  
`{{ .Email }}`| Contains the original email address of the user. Empty when when trying to [link an email address to an anonymous user](https://supabase.com/docs/guides/auth/auth-anonymous#link-an-email--phone-identity).  
`{{ .NewEmail }}`| Contains the new email address of the user. This variable is only supported in the "Change Email Address" template.  
## Editing email templates[#](https://supabase.com/docs/guides/auth/auth-email-templates#editing-email-templates)
On hosted Supabase projects, edit your email templates on the [Email Templates](https://supabase.com/dashboard/project/_/auth/templates) page. On self-hosted projects or in local development, edit your [configuration files](https://supabase.com/docs/guides/local-development/customizing-email-templates).
You can also manage email templates using the Management API:
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
# Get your access token from https://supabase.com/dashboard/account/tokensexportSUPABASE_ACCESS_TOKEN="your-access-token"exportPROJECT_REF="your-project-ref"# Get current email templatescurl-XGET"https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth"\-H"Authorization: Bearer $SUPABASE_ACCESS_TOKEN"\|jq'to_entries | map(select(.key | startswith("mailer_templates"))) | from_entries'# Update email templatescurl-XPATCH"https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth"\-H"Authorization: Bearer $SUPABASE_ACCESS_TOKEN"\-H"Content-Type: application/json"\-d'{   "mailer_subjects_confirmation": "Confirm your signup",   "mailer_templates_confirmation_content": "<h2>Confirm your signup</h2><p>Follow this link to confirm your user:</p><p><a href=\"{{ .ConfirmationURL }}\">Confirm your email</a></p>",   "mailer_subjects_magic_link": "Your Magic Link",   "mailer_templates_magic_link_content": "<h2>Magic Link</h2><p>Follow this link to login:</p><p><a href=\"{{ .ConfirmationURL }}\">Log In</a></p>",   "mailer_subjects_recovery": "Rest Your Password",   "mailer_templates_recovery_content": "<h2>Reset Password</h2><p>Follow this link to reset the password for your user:</p><p><a href=\"{{ .ConfirmationURL }}\">Reset Password</a></p>",   "mailer_subjects_invite": "You have been invited",   "mailer_templates_invite_content": "<h2>You have been invited</h2><p>You have been invited to create a user on {{ .SiteURL }}. Follow this link to accept the invite:</p><p><a href=\"{{ .ConfirmationURL }}\">Accept the invite</a></p>",   "mailer_subjects_email_change": "Confirm email change",   "mailer_templates_email_change_content": "<h2>Confirm email change</h2><p>Follow this link to confirm the update of your email:</p><p><a href=\"{{ .ConfirmationURL }}\">Change email</a></p>", }'

```

## Mobile deep linking[#](https://supabase.com/docs/guides/auth/auth-email-templates#mobile-deep-linking)
For mobile applications, you might need to link or redirect to a specific page within your app. See the [Mobile Deep Linking guide](https://supabase.com/docs/guides/auth/native-mobile-deep-linking) to set this up.
## Limitations[#](https://supabase.com/docs/guides/auth/auth-email-templates#limitations)
### Email prefetching[#](https://supabase.com/docs/guides/auth/auth-email-templates#email-prefetching)
Certain email providers may have spam detection or other security features that prefetch URL links from incoming emails (e.g. [Safe Links in Microsoft Defender for Office 365](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/safe-links-about?view=o365-worldwide)). In this scenario, the `{{ .ConfirmationURL }}` sent will be consumed instantly which leads to a "Token has expired or is invalid" error. To guard against this:
  * Use an email OTP instead by including `{{ .Token }}` in the email template.
  * Create your own custom email link to redirect the user to a page where they can click on a button to confirm the action. For example, you can include the following in your email template:
```

1
2
3
<a href="{{ .SiteURL }}/confirm-signup?confirmation_url={{ .ConfirmationURL }}">Confirm your signup</a>

```

The user should be brought to a page on your site where they can confirm the action by clicking a button. The button should contain the actual confirmation link which can be obtained from parsing the `confirmation_url={{ .ConfirmationURL }}` query parameter in the URL.


### Email tracking[#](https://supabase.com/docs/guides/auth/auth-email-templates#email-tracking)
If you are using an external email provider that enables "email tracking", the links inside the Supabase email templates will be overwritten and won't perform as expected. We recommend disabling email tracking to ensure email links are not overwritten.
### Redirecting the user to a server-side endpoint[#](https://supabase.com/docs/guides/auth/auth-email-templates#redirecting-the-user-to-a-server-side-endpoint)
If you intend to use [Server-side rendering](https://supabase.com/docs/guides/auth/server-side-rendering), you might want the email link to redirect the user to a server-side endpoint to check if they are authenticated before returning the page. However, the default email link will redirect the user after verification to the redirect URL with the session in the query fragments. Since the session is returned in the query fragments by default, you won't be able to access it on the server-side.
You can customize the email link in the email template to redirect the user to a server-side endpoint successfully. For example:
```

1
2
3
4
<ahref="https://api.example.com/v1/authenticate?token_hash={{ .TokenHash }}&type=invite&redirect_to={{ .RedirectTo }}">Accept the invite</a>

```

When the user clicks on the link, the request will hit `https://api.example.com/v1/authenticate` and you can grab the `token_hash`, `type` and `redirect_to` query parameters from the URL. Then, you can call the [`verifyOtp`](https://supabase.com/docs/reference/javascript/auth-verifyotp) method to get back an authenticated session before redirecting the user back to the client. Since the `verifyOtp` method makes a `POST` request to Supabase Auth to verify the user, the session will be returned in the response body, which can be read by the server. For example:
```

1
2
3
4
5
6
7
8
const{token_hash,type}=Object.fromEntries(newURLSearchParams(window.location.search))const{data:{session},error,}=awaitsupabase.auth.verifyOtp({token_hash,type:typeasEmailOtpType})// subsequently redirect the user back to the client using the redirect_to param// ...

```

## Customization[#](https://supabase.com/docs/guides/auth/auth-email-templates#customization)
Supabase Auth makes use of [Go Templates](https://pkg.go.dev/text/template). This means it is possible to conditionally render information based on template properties.
### Send different email to early access users[#](https://supabase.com/docs/guides/auth/auth-email-templates#send-different-email-to-early-access-users)
Send a different email to users who signed up via an early access domain (`https://www.earlyaccess.trial.com`).
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
{{ if eq .Data.Domain "https://www.example.com" }}<h1>Welcome to Our Database Service!</h1> <p>Dear Developer,</p> <p>Welcome to Billy, the scalable developer platform!</p> <p>Best Regards,<br>Billy Team</p>{{ else if eq .Data.Domain "https://www.earlyaccess.trial.com" }}<h1>Welcome to Our Database Service!</h1> <p>Dear Developer,</p> <p>Welcome Billy, the scalable developer platform!</p> <p> As an early access member, you have access to select features like Point To Space Restoration.</p> <p>Best Regards,<br>Billy Team</p>{{ end }}

```

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/auth/auth-email-templates.mdx)
### Is this helpful?
No Yes
### On this page
[Terminology](https://supabase.com/docs/guides/auth/auth-email-templates#terminology)[Editing email templates](https://supabase.com/docs/guides/auth/auth-email-templates#editing-email-templates)[Mobile deep linking](https://supabase.com/docs/guides/auth/auth-email-templates#mobile-deep-linking)[Limitations](https://supabase.com/docs/guides/auth/auth-email-templates#limitations)[Email prefetching](https://supabase.com/docs/guides/auth/auth-email-templates#email-prefetching)[Email tracking](https://supabase.com/docs/guides/auth/auth-email-templates#email-tracking)[Redirecting the user to a server-side endpoint](https://supabase.com/docs/guides/auth/auth-email-templates#redirecting-the-user-to-a-server-side-endpoint)[Customization](https://supabase.com/docs/guides/auth/auth-email-templates#customization)[Send different email to early access users](https://supabase.com/docs/guides/auth/auth-email-templates#send-different-email-to-early-access-users)
  * Need some help?
[Contact support](https://supabase.com/support)
  * Latest product updates?
[See Changelog](https://supabase.com/changelog)
  * Something's not right?
[Check system status](https://status.supabase.com/)


[© Supabase Inc](https://supabase.com/)—[Contributing](https://github.com/supabase/supabase/blob/master/apps/docs/DEVELOPERS.md)[Author Styleguide](https://github.com/supabase/supabase/blob/master/apps/docs/CONTRIBUTING.md)[Open Source](https://supabase.com/open-source)[SupaSquad](https://supabase.com/supasquad)Privacy Settings
[GitHub](https://github.com/supabase/supabase)[Twitter](https://twitter.com/supabase)[Discord](https://discord.supabase.com/)
