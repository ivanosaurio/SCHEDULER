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
[Auth](https://supabase.com/docs/guides/auth/redirect-urls)
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
  3. [Redirect URLs](https://supabase.com/docs/guides/auth/redirect-urls)


Redirect URLs
Set up redirect urls with Supabase Auth.
## Overview[#](https://supabase.com/docs/guides/auth/redirect-urls#overview)
Supabase Auth allows your application to receive a [user session](https://supabase.com/docs/guides/auth/sessions) on web pages or in mobile apps that only you allow.
When using [passwordless sign-ins](https://supabase.com/docs/reference/javascript/auth-signinwithotp) or [third-party providers](https://supabase.com/docs/reference/javascript/auth-signinwithoauth#sign-in-using-a-third-party-provider-with-redirect), the Supabase client library methods provide a `redirectTo` parameter to specify where to redirect the user to after authentication. By default, the user will be redirected to the [`SITE_URL`](https://supabase.com/docs/guides/auth/redirect-urls) but you can modify the `SITE_URL` or add additional redirect URLs to the allow list. Once you've added necessary URLs to the allow list, you can specify the URL you want the user to be redirected to in the `redirectTo` parameter.
When using [Sign in with Web3](https://supabase.com/docs/guides/auth/auth-web3) the message signed by the user in the Web3 wallet application will indicate the URL on which the signature took place. Supabase Auth will reject messages that are signed for URLs that have not been allowed.
To edit the allow list, go to the [URL Configuration](https://supabase.com/dashboard/project/_/auth/url-configuration) page. In local development or self-hosted projects, use the [configuration file](https://supabase.com/docs/guides/cli/config#auth.additional_redirect_urls).
## Use wildcards in redirect URLs[#](https://supabase.com/docs/guides/auth/redirect-urls#use-wildcards-in-redirect-urls)
Supabase allows you to specify wildcards when adding redirect URLs to the [allow list](https://supabase.com/dashboard/project/_/auth/url-configuration). You can use wildcard match patterns to support preview URLs from providers like Netlify and Vercel.
Wildcard| Description  
---|---  
`*`| matches any sequence of non-separator characters  
`**`| matches any sequence of characters  
`?`| matches any single non-separator character  
`c`| matches character c (c != `*`, `**`, `?`, `\`, `[`, `{`, `}`)  
`\c`| matches character c  
`[!{ character-range }]`| matches any sequence of characters not in the `{ character-range }`. For example, `[!a-z]` will not match any characters ranging from a-z.  
The separator characters in a URL are defined as `.` and `/`. Use [this tool](https://www.digitalocean.com/community/tools/glob?comments=true&glob=http%3A%2F%2Flocalhost%3A3000%2F%2A%2A&matches=false&tests=http%3A%2F%2Flocalhost%3A3000&tests=http%3A%2F%2Flocalhost%3A3000%2F&tests=http%3A%2F%2Flocalhost%3A3000%2F%3Ftest%3Dtest&tests=http%3A%2F%2Flocalhost%3A3000%2Ftest-test%3Ftest%3Dtest&tests=http%3A%2F%2Flocalhost%3A3000%2Ftest%2Ftest%3Ftest%3Dtest) to test your patterns.
##### Recommendation
While the "globstar" (`**`) is useful for local development and preview URLs, we recommend setting the exact redirect URL path for your site URL in production.
### Redirect URL examples with wildcards[#](https://supabase.com/docs/guides/auth/redirect-urls#redirect-url-examples-with-wildcards)
Redirect URL| Description  
---|---  
`http://localhost:3000/*`| matches `http://localhost:3000/foo`, `http://localhost:3000/bar` but not `http://localhost:3000/foo/bar` or `http://localhost:3000/foo/` (note the trailing slash)  
`http://localhost:3000/**`| matches `http://localhost:3000/foo`, `http://localhost:3000/bar` and `http://localhost:3000/foo/bar`  
`http://localhost:3000/?`| matches `http://localhost:3000/a` but not `http://localhost:3000/foo`  
`http://localhost:3000/[!a-z]`| matches `http://localhost:3000/1` but not `http://localhost:3000/a`  
## Netlify preview URLs[#](https://supabase.com/docs/guides/auth/redirect-urls#netlify-preview-urls)
For deployments with Netlify, set the `SITE_URL` to your official site URL. Add the following additional redirect URLs for local development and deployment previews:
  * `http://localhost:3000/**`
  * `https://**--my_org.netlify.app/**`


## Vercel preview URLs[#](https://supabase.com/docs/guides/auth/redirect-urls#vercel-preview-urls)
For deployments with Vercel, set the `SITE_URL` to your official site URL. Add the following additional redirect URLs for local development and deployment previews:
  * `http://localhost:3000/**`
  * `https://*-<team-or-account-slug>.vercel.app/**`


Vercel provides an environment variable for the URL of the deployment called `NEXT_PUBLIC_VERCEL_URL`. See the [Vercel docs](https://vercel.com/docs/concepts/projects/environment-variables#system-environment-variables) for more details. You can use this variable to dynamically redirect depending on the environment. You should also set the value of the environment variable called NEXT_PUBLIC_SITE_URL, this should be set to your site URL in production environment to ensure that redirects function correctly.
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
constgetURL=()=>{leturl=process?.env?.NEXT_PUBLIC_SITE_URL??// Set this to your site URL in production env.process?.env?.NEXT_PUBLIC_VERCEL_URL??// Automatically set by Vercel.'http://localhost:3000/'// Make sure to include `https://` when not localhost.url=url.startsWith('http') ?url:`https://${url}`// Make sure to include a trailing `/`.url=url.endsWith('/') ?url:`${url}/`returnurl}const{data,error}=awaitsupabase.auth.signInWithOAuth({provider:'github',options:{redirectTo:getURL(),},})

```

## Email templates when using `redirectTo`[#](https://supabase.com/docs/guides/auth/redirect-urls#email-templates-when-using-redirectto)
When using a `redirectTo` option, you may need to replace the `{{ .SiteURL }}` with `{{ .RedirectTo }}` in your email templates. See the [Email Templates guide](https://supabase.com/docs/guides/auth/auth-email-templates) for more information.
For example, change the following:
```

1
2
3
4
5
6
7
<!-- Old --><a href="{{ .SiteURL }}/auth/confirm?token_hash={{ .TokenHash }}&type=email">Confirm your mail</a><!-- New --><a href="{{ .RedirectTo }}/auth/confirm?token_hash={{ .TokenHash }}&type=email">Confirm your mail</a>

```

## Mobile deep linking URIs[#](https://supabase.com/docs/guides/auth/redirect-urls#mobile-deep-linking-uris)
For mobile applications you can use deep linking URIs. For example, for your `SITE_URL` you can specify something like `com.supabase://login-callback/` and for additional redirect URLs something like `com.supabase.staging://login-callback/` if needed.
Read more about deep linking and find code examples for different frameworks [here](https://supabase.com/docs/guides/auth/native-mobile-deep-linking).
## Error handling[#](https://supabase.com/docs/guides/auth/redirect-urls#error-handling)
When authentication fails, the user will still be redirected to the redirect URL provided. However, the error details will be returned as query fragments in the URL. You can parse these query fragments and show a custom error message to the user. For example:
```

1
2
3
4
5
6
constparams=newURLSearchParams(window.location.hash.slice())if (params.get('error_code').startsWith('4')) {// show error message if error is a 4xx errorwindow.alert(params.get('error_description'))}

```

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/auth/redirect-urls.mdx)
### Is this helpful?
No Yes
### On this page
[Overview](https://supabase.com/docs/guides/auth/redirect-urls#overview)[Use wildcards in redirect URLs](https://supabase.com/docs/guides/auth/redirect-urls#use-wildcards-in-redirect-urls)[Redirect URL examples with wildcards](https://supabase.com/docs/guides/auth/redirect-urls#redirect-url-examples-with-wildcards)[Netlify preview URLs](https://supabase.com/docs/guides/auth/redirect-urls#netlify-preview-urls)[Vercel preview URLs](https://supabase.com/docs/guides/auth/redirect-urls#vercel-preview-urls)[Email templates when using redirectTo](https://supabase.com/docs/guides/auth/redirect-urls#email-templates-when-using-redirectto)[Mobile deep linking URIs](https://supabase.com/docs/guides/auth/redirect-urls#mobile-deep-linking-uris)[Error handling](https://supabase.com/docs/guides/auth/redirect-urls#error-handling)
  * Need some help?
[Contact support](https://supabase.com/support)
  * Latest product updates?
[See Changelog](https://supabase.com/changelog)
  * Something's not right?
[Check system status](https://status.supabase.com/)


[© Supabase Inc](https://supabase.com/)—[Contributing](https://github.com/supabase/supabase/blob/master/apps/docs/DEVELOPERS.md)[Author Styleguide](https://github.com/supabase/supabase/blob/master/apps/docs/CONTRIBUTING.md)[Open Source](https://supabase.com/open-source)[SupaSquad](https://supabase.com/supasquad)Privacy Settings
[GitHub](https://github.com/supabase/supabase)[Twitter](https://twitter.com/supabase)[Discord](https://discord.supabase.com/)
