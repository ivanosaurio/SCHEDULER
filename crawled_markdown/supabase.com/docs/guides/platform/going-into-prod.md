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
[Deployment](https://supabase.com/docs/guides/deployment)
  * [Overview](https://supabase.com/docs/guides/deployment)
Environments
  * [Managing environments](https://supabase.com/docs/guides/deployment/managing-environments)
  * [Database migrations](https://supabase.com/docs/guides/deployment/database-migrations)
  * [Branching](https://supabase.com/docs/guides/deployment/branching)
Terraform
  * [Terraform provider](https://supabase.com/docs/guides/deployment/terraform)
  * [Terraform tutorial](https://supabase.com/docs/guides/deployment/terraform/tutorial)
  * [Terraform reference](https://supabase.com/docs/guides/deployment/terraform/reference)
Production readiness
  * [Shared responsibility model](https://supabase.com/docs/guides/deployment/shared-responsibility-model)
  * [Maturity model](https://supabase.com/docs/guides/deployment/maturity-model)
  * [Production checklist](https://supabase.com/docs/guides/deployment/going-into-prod)
  * [SOC 2 compliance](https://supabase.com/docs/guides/security/soc-2-compliance)
CI/CD
  * [Generate types from your database](https://supabase.com/docs/guides/deployment/ci/generating-types)
  * [Automated testing](https://supabase.com/docs/guides/deployment/ci/testing)
  * [Back up your database](https://supabase.com/docs/guides/deployment/ci/backups)


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
Home
  1. [Deployment](https://supabase.com/docs/guides/deployment)
  2. Production readiness
  3. [Production checklist](https://supabase.com/docs/guides/deployment/going-into-prod)


Production Checklist
After developing your project and deciding it's Production Ready, you should run through this checklist to ensure that your project:
  * is secure
  * won't falter under the expected load
  * remains available whilst in production


## Security[#](https://supabase.com/docs/guides/deployment/going-into-prod#security)
  * Ensure RLS is enabled 
    * Tables that do not have RLS enabled with reasonable policies allow any client to access and modify their data. This is unlikely to be what you want in the majority of cases.
    * [Learn more about RLS](https://supabase.com/docs/guides/database/postgres/row-level-security).
  * Enable replication on tables containing sensitive data by enabling Row Level Security (RLS) and setting row security policies: 
    * Go to the Authentication > Policies page in the Supabase Dashboard to enable RLS and create security policies.
    * Go to the Database > Publications page in the Supabase Dashboard to manage replication tables.
  * Turn on [SSL Enforcement](https://supabase.com/docs/guides/platform/ssl-enforcement)
  * Enable [Network Restrictions](https://supabase.com/docs/guides/platform/network-restrictions) for your database.
  * Ensure that your Supabase Account is protected with multi-factor authentication (MFA). 
    * If using a GitHub signin, [enable 2FA on GitHub](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication). Since your GitHub account gives you administrative rights to your Supabase org, you should protect it with a strong password and 2FA using a U2F key or a TOTP app.
    * If using email+password signin, set up [MFA for your Supabase account](https://supabase.com/docs/guides/platform/multi-factor-authentication#enable-mfa).
  * Enable [MFA enforcement on your organization](https://supabase.com/docs/guides/platform/network-restrictions). This ensures all users must have a valid MFA backed session to interact with organization and project resources.
  * Consider [adding multiple owners on your Supabase org](https://supabase.com/dashboard/org/_/team). This ensures that if one of the owners is unreachable or loses access to their account, you still have Owner access to your org.
  * Ensure email confirmations are [enabled](https://supabase.com/dashboard/project/_/auth/providers) in the `Settings > Auth` page.
  * Ensure that you've [set the expiry](https://supabase.com/dashboard/project/_/auth/providers) for one-time passwords (OTPs) to a reasonable value that you are comfortable with. We recommend setting this to 3600 seconds (1 hour) or lower.
  * Increase the length of the OTP if you need a higher level of entropy.
  * If your application requires a higher level of security, consider setting up [multi-factor authentication](https://supabase.com/docs/guides/auth/auth-mfa) (MFA) for your users.
  * Use a custom SMTP server for auth emails so that your users can see that the mails are coming from a trusted domain (preferably the same domain that your app is hosted on). Grab SMTP credentials from any major email provider such as SendGrid, AWS SES, etc.
  * Think hard about how _you_ would abuse your service as an attacker, and mitigate.
  * Review these [common cybersecurity threats](https://auth0.com/docs/security/prevent-threats).
  * Check and review issues in your database using [Security Advisor](https://supabase.com/dashboard/project/_/database/security-advisor).


## Performance[#](https://supabase.com/docs/guides/deployment/going-into-prod#performance)
  * Ensure that you have suitable indices to cater to your common query patterns 
    * [Learn more about indexes in Postgres](https://www.enterprisedb.com/postgres-tutorials/overview-postgresql-indexes).
    * `pg_stat_statements` can help you [identify hot or slow queries](https://www.virtual-dba.com/blog/postgresql-performance-identifying-hot-and-slow-queries/).
  * Perform load testing (preferably on a staging env) 
    * Tools like [k6](https://k6.io/) can simulate traffic from many different users.
  * Upgrade your database if you require more resources. If you need anything beyond what is listed, contact enterprise@supabase.io.
  * If you are expecting a surge in traffic (for a big launch) and are on a Team or Enterprise Plan, [contact support](https://supabase.com/dashboard/support/new) with more details about your launch and we'll help keep an eye on your project.
  * If you expect your database size to be > 4 GB, [enable](https://supabase.com/dashboard/project/_/settings/addons?panel=pitr) the Point in Time Recovery (PITR) add-on. Daily backups can take up resources from your database when the backup is in progress. PITR is more resource efficient, since only the changes to the database are backed up.
  * Check and review issues in your database using [Performance Advisor](https://supabase.com/dashboard/project/_/database/performance-advisor).


## Availability[#](https://supabase.com/docs/guides/deployment/going-into-prod#availability)
  * Use your own SMTP credentials so that you have full control over the deliverability of your transactional auth emails (see Settings > Auth) 
    * you can grab SMTP credentials from any major email provider such as SendGrid, AWS SES, etc. You can refer to our [SMTP guide](https://supabase.com/docs/guides/auth/auth-smtp) for more details.
    * The default rate limit for auth emails when using a custom SMTP provider is 30 new users per hour, if doing a major public announcement you will likely require more than this.
  * Applications on the Free Plan that exhibit extremely low activity in a 7 day period may be paused by Supabase to save on server resources. 
    * You can restore paused projects from the Supabase dashboard.
    * Upgrade to Pro to guarantee that your project will not be paused for inactivity.
  * Database backups are not available for download on the Free Plan. 
    * You can set up your own backup systems using tools like [pg_dump](https://www.postgresqltutorial.com/postgresql-backup-database/) or [wal-g](https://github.com/wal-g/wal-g).
    * Nightly backups for Pro Plan projects are available on the Supabase dashboard for up to 7 days.
    * Point in Time Recovery (PITR) allows a project to be backed up at much shorter intervals. This provides users an option to restore to any chosen point of up to seconds in granularity. In terms of Recovery Point Objective (RPO), Daily Backups would be suitable for projects willing to lose up to 24 hours worth of data. If a lower RPO is required, enable PITR.
  * Supabase Projects use disks that offer 99.8-99.9% durability by default. 
    * Use Read Replicas if you require availability resilience to a disk failure event
    * Use PITR if you require durability resilience to a disk failure event
  * Upgrading to the Supabase Pro Plan will give you [access to our support team](https://supabase.com/dashboard/support/new).


## Rate limiting, resource allocation, & abuse prevention[#](https://supabase.com/docs/guides/deployment/going-into-prod#rate-limiting-resource-allocation--abuse-prevention)
  * Supabase employs a number of safeguards against bursts of incoming traffic to prevent abuse and help maximize stability across the platform 
    * If you're on a Team or Enterprise Plan and expect high load events, such as production launches, heavy load testing, or prolonged high resource usage, open a ticket via the [support form](https://supabase.help) for help. Provide at least 2 weeks notice.


### Auth rate limits[#](https://supabase.com/docs/guides/deployment/going-into-prod#auth-rate-limits)
  * The table below shows the rate limit quotas on the following authentication endpoints. You can configure the auth rate limits for your project [here](https://supabase.com/dashboard/project/_/auth/rate-limits).

Endpoint| Path| Limited By| Rate Limit  
---|---|---|---  
All endpoints that send emails| `/auth/v1/signup` `/auth/v1/recover` `/auth/v1/user`[^1]| Sum of combined requests| As of 3 Sep 2024, this has been updated to 2 emails per hour. You can only change this with your own [custom SMTP setup](https://supabase.com/docs/guides/auth/auth-smtp).  
All endpoints that send One-Time-Passwords (OTP)| `/auth/v1/otp`| Sum of combined requests| Defaults to 360 OTPs per hour. Is customizable.  
Send OTPs or magic links| `/auth/v1/otp`| Last request| Defaults to 60 seconds window before a new request is allowed. Is customizable.  
Signup confirmation request| `/auth/v1/signup`| Last request| Defaults to 60 seconds window before a new request is allowed. Is customizable.  
Password Reset Request| `/auth/v1/recover`| Last request| Defaults to 60 seconds window before a new request is allowed. Is customizable.  
Verification requests| `/auth/v1/verify`| IP Address| 360 requests per hour (with bursts up to 30 requests)  
Token refresh requests| `/auth/v1/token`| IP Address| 1800 requests per hour (with bursts up to 30 requests)  
Create or Verify an MFA challenge| `/auth/v1/factors/:id/challenge` `/auth/v1/factors/:id/verify`| IP Address| 15 requests per minute (with bursts up to 30 requests)  
Anonymous sign-ins| `/auth/v1/signup`[^2]| IP Address| 30 requests per hour (with bursts up to 30 requests)  
### Realtime quotas[#](https://supabase.com/docs/guides/deployment/going-into-prod#realtime-quotas)
  * Review the [Realtime quotas](https://supabase.com/docs/guides/realtime/quotas).
  * If you need quotas increased you can always [contact support](https://supabase.com/dashboard/support/new).


### Abuse prevention[#](https://supabase.com/docs/guides/deployment/going-into-prod#abuse-prevention)
  * Supabase provides CAPTCHA protection on the signup, sign-in and password reset endpoints. Refer to [our guide](https://supabase.com/docs/guides/auth/auth-captcha) on how to protect against abuse using this method.


### Email link validity[#](https://supabase.com/docs/guides/deployment/going-into-prod#email-link-validity)
  * When working with enterprise systems, email scanners may scan and make a `GET` request to the reset password link or sign up link in your email. Since links in Supabase Auth are single use, a user who opens an email post-scan to click on a link will receive an error. To get around this problem, consider altering the email template to replace the original magic link with a link to a domain you control. The domain can present the user with a "Sign-in" button which redirect the user to the original magic link URL when clicked.
  * When using a custom SMTP service, some services might have link tracking enabled which may overwrite or disform the email confirmation links sent by Supabase Auth. To prevent this from happening, we recommend that you disable link tracking when using a custom SMTP service.


## Subscribe to Supabase status page[#](https://supabase.com/docs/guides/deployment/going-into-prod#subscribe-to-supabase-status-page)
Stay informed about Supabase service status by subscribing to the [Status Page](https://status.supabase.com/). We recommend setting up Slack notifications through an RSS feed to ensure your team receives timely updates about service status changes.
### Setting up Slack notifications[#](https://supabase.com/docs/guides/deployment/going-into-prod#setting-up-slack-notifications)
  1. Install the RSS app in Slack:
     * Visit the [RSS app page](https://slack.com/marketplace/A0F81R7U7-rss) in the Slack marketplace
     * Click `Add to Slack` if not already installed
     * Otherwise you will get straight to next step, no need to reinstall the app
  2. Configure the Supabase status feed:
     * Create a channel (e.g., `#supabase-status-alerts`) for status updates
     * On the [RSS app page](https://slack.com/marketplace/A0F81R7U7-rss) go to _Add a Feed_ section and set Feed URL to `https://status.supabase.com/history.rss`
     * Select your designated channel and click "Subscribe to this feed"


Once configured, your team will receive automatic notifications in Slack whenever the Supabase Status Page is updated.
For detailed setup instructions, see the [Add RSS feeds to Slack](https://slack.com/intl/en-nz/help/articles/218688467-Add-RSS-feeds-to-Slack).
## Next steps[#](https://supabase.com/docs/guides/deployment/going-into-prod#next-steps)
This checklist is always growing so be sure to check back frequently, and also feel free to suggest additions and amendments by making a PR on [GitHub](https://github.com/supabase/supabase).
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/deployment/going-into-prod.mdx)
### Is this helpful?
No Yes
### On this page
[Security](https://supabase.com/docs/guides/deployment/going-into-prod#security)[Performance](https://supabase.com/docs/guides/deployment/going-into-prod#performance)[Availability](https://supabase.com/docs/guides/deployment/going-into-prod#availability)[Rate limiting, resource allocation, & abuse prevention](https://supabase.com/docs/guides/deployment/going-into-prod#rate-limiting-resource-allocation--abuse-prevention)[Auth rate limits](https://supabase.com/docs/guides/deployment/going-into-prod#auth-rate-limits)[Realtime quotas](https://supabase.com/docs/guides/deployment/going-into-prod#realtime-quotas)[Abuse prevention](https://supabase.com/docs/guides/deployment/going-into-prod#abuse-prevention)[Email link validity](https://supabase.com/docs/guides/deployment/going-into-prod#email-link-validity)[Subscribe to Supabase status page](https://supabase.com/docs/guides/deployment/going-into-prod#subscribe-to-supabase-status-page)[Setting up Slack notifications](https://supabase.com/docs/guides/deployment/going-into-prod#setting-up-slack-notifications)[Next steps](https://supabase.com/docs/guides/deployment/going-into-prod#next-steps)
  * Need some help?
[Contact support](https://supabase.com/support)
  * Latest product updates?
[See Changelog](https://supabase.com/changelog)
  * Something's not right?
[Check system status](https://status.supabase.com/)


[© Supabase Inc](https://supabase.com/)—[Contributing](https://github.com/supabase/supabase/blob/master/apps/docs/DEVELOPERS.md)[Author Styleguide](https://github.com/supabase/supabase/blob/master/apps/docs/CONTRIBUTING.md)[Open Source](https://supabase.com/open-source)[SupaSquad](https://supabase.com/supasquad)Privacy Settings
[GitHub](https://github.com/supabase/supabase)[Twitter](https://twitter.com/supabase)[Discord](https://discord.supabase.com/)
