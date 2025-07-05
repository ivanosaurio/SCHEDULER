[![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fa88e89e4a86b%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--light.daaeffd3.png&w=256&q=75)![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fa88e89e4a86b%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--dark.b36ebb5f.png&w=256&q=75)](https://supabase.com/)
  * Product 
  * Developers 
  * Solutions 
  * [Pricing](https://supabase.com/pricing)
  * [Docs](https://supabase.com/docs)
  * [Blog](https://supabase.com/blog)


[85.2K](https://github.com/supabase/supabase)[Sign in](https://supabase.com/dashboard)[Start your project](https://supabase.com/dashboard)
Open main menu
# Changelog
New updates and product improvements
### [Update to Edge Functions Regional Invocations ](https://github.com/orgs/supabase/discussions/36850)
Jul 2, 2025
Edge Functions are executed in the region closest to the user making the request. This helps to reduce network latency and provide faster responses to the user.
However, if your Function performs many database or storage operations, invoking the Function in the same region as your database may provide better performance. Some situations where this might be helpful include:
  * Bulk adding and editing records in your database
  * Uploading files


Previously, the region could only be set via the `x-region` header in the request. However, in some instances (e.g., CORS requests, Webhooks), the headers set in the request cannot be controlled. Considering these limitations, we've also made it possible to set the region via the `forceFunctionRegion` query parameter.
`
1
# https://supabase.com/docs/guides/functions/deploy#invoking-remote-functions
2
curl --request POST 'https://<project_ref>.supabase.co/functions/v1/hello-world?forceFunctionRegion=eu-west-3' \
3
 --header 'Authorization: Bearer ANON_KEY' \
4
 --header 'Content-Type: application/json' \
5
 --data '{ "name":"Functions" }'
`
Please check the [Regional Invocations](https://supabase.com/docs/guides/functions/regional-invocation) guide for more details.
### [Deno 2.1 Preview - Hosted Environment ](https://github.com/orgs/supabase/discussions/36814)
Jul 1, 2025
A couple of months ago, we started migrating our Edge Functions platform to use [Deno 2.1](https://deno.com/blog/v2.0). Deno 2 bridges the gap between Node and Deno by supporting Node's built-in APIs, npm modules, and `package.json`. This would make it easy to migrate existing Node apps to run in the Edge Functions platform.
Previously, we [announced](https://github.com/orgs/supabase/discussions/34054) that you can start testing Deno 2.1 locally for your Edge Functions. Thanks to everyone who tried and gave us feedback.
Today, we give you the option to preview Deno 2.1 on our hosted platform. You should try running your existing Edge Functions with Deno 2.1 and report any bugs/issues.
You can first run `deno lint` locally on your Edge Functions code with [no-deprecated-deno-api](https://docs.deno.com/lint/rules/no-deprecated-deno-api/) rule to find any breaking changes in Deno 2.
Once you have updated your functions, you can test them in our hosted platform as follows:
### How to test for Deno 2 compatibility[#](https://supabase.com/changelog#how-to-test-for-deno-2-compatibility)
  * There are two ways to force your functions to run on the Deno 2 preview cluster exist.
  * Add query parameter `forceDenoVersion=2` to your function requests


`
1
https://project-ref.supabase.co/functions/v1/hello-world?forceDenoVersion=2
`
  * Add `x-deno-version: 2` header in requests


`
1
curl --request POST \
2
 --url https://project-ref.supabase.co/functions/v1/hello-world \
3
 --header 'content-type: application/json' \
4
 --header 'x-deno-version: 2' \
5
 --data '{
6
 "name": "test"
7
}
`
**Note** : Deno 2 Preview cluster is only available in the `us-east-2` region.
Also, in the next couple of days, we will notify projects currently using deprecated APIs via email to update their functions to use Deno 2.
### When are we fully rolling out Deno 2.1?[#](https://supabase.com/changelog#when-are-we-fully-rolling-out-deno-21)
Based on the feedback and issues we discover in this preview, we will decide the timeline on making Deno 2.1 the default runtime in our hosted platform. Current ETA is within 3-6 weeks.
### [Forthcoming Postgres 17 Release Notes ](https://github.com/orgs/supabase/discussions/35851)
May 22, 2025
The upcoming release of Supabase Platform will use Postgres 17. The Postgres 17 bundle will no longer include the following Postgres extensions:
  * `timescaledb`
  * `plv8`
  * `plls`
  * `plcoffee`
  * `pgjwt`


Existing projects will NOT be immediately impacted - the extensions will continue to be supported on Supabase Postgres 15, until the Supabase Platform “end of life” of Postgres 15 in approximately 1 year (May 2026). However, the extensions will not receive further updates and fixes. Existing projects will need to drop the extensions before they can upgrade to Postgres 17.
This decision to deprecate these extensions was not made lightly, however these extensions are more complex than “standard” Postgres extensions and require additional support/testing that did not match the usage we see on the platform.
To address the capability gaps left by deprecating plv8 and timescaledb, we plan to include the pg_partman extension in a future Postgres 17 release and will provide documentation to help migrate Timescale hypertables to native Postgres partitioning at that time. For plv8 we recommend porting the logic to Edge Functions, which offer greater scalability and flexibility. These changes are part of our ongoing efforts to streamline our platform, reduce operational complexity, and ensure long-term support for features that align closely with our user base.
If you have additional use-cases for these deprecated extensions, please [reach out to us](https://supabase.help/) and our Success team will work with you to find a solution.
### [Feature Preview: Tabs for Table and SQL Editor ](https://github.com/orgs/supabase/discussions/35636)
May 13, 2025
> [!NOTE] This change has now been fully rolled out - thank you everyone for the feedback! 🙏
## Tabs for Table and SQL Editor[#](https://supabase.com/changelog#tabs-for-table-and-sql-editor)
![Screenshot 2025-04-07 at 19 47 57](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fb17f02d8-aad1-42d5-afcc-30701c9a5a68&w=3840&q=75)
![Screenshot 2025-04-07 at 19 48 30](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F6167c731-b4cf-4a13-a83c-61fec84342b1&w=3840&q=75)
For those who've been with us since the very beginning, you might remember that we used to have tabs in the Table Editor which we eventually removed 😉 We're bringing this nifty UX back with a better UX too, and also introducing this into the SQL Editor as well! Conveniently go between tables across schemas, or flip between snippets without having to navigate through your list of queries (especially if you've got tons of them!)
These are currently behind their own feature previews at the moment, which you can access by clicking on your Profile picture in the top navigation bar, but we're going to be looking into an incremental rollout for everyone! Feel free to let us know what you think! 🙏
## What we'd like to know from you[#](https://supabase.com/changelog#what-wed-like-to-know-from-you)
  * Any bugs or issues that you might have run into while using the new UI
  * Any ideas or suggestions that you reckon will improve the DX based on how you use these 2 editors
  * Feel free to leave any feedback in this thread too!


## Rollout plan[#](https://supabase.com/changelog#rollout-plan)
  * Changes are behind a feature preview in the dashboard
  * Starting from 12th May 2025, we will roll out to the hosted platform first as incremental % rollout where users will be opted into the feature preview by default
  * If you might want _opt out of the changes_ , you may disable the changes via the feature previews which you can access through the user dropdown in the header here: ![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fd260da81-6d28-4ac7-9d07-4a898e4d840b&w=3840&q=75)


### [Developer Update - April 2025 ](https://github.com/orgs/supabase/discussions/35523)
May 7, 2025
Here’s everything that happened with Supabase in the last month:
## Project scoped roles[#](https://supabase.com/changelog#project-scoped-roles)
![project-scoped-roles](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F95d1cf7b-6622-4817-85ed-ff32e826e61a&w=3840&q=75)
[Project scoped roles](https://supabase.link/projectscopedroles-project-scoped-roles-apr2025-tg16) are now available for all Supabase Team plans. Each member in the organization can be assigned a role scoped to the organization or to specific projects.
[[GitHub](https://supabase.link/github-project-scoped-roles-apr2025-k2mz)]
## MCP Server now works with VS Code[#](https://supabase.com/changelog#mcp-server-now-works-with-vs-code)
![mcp-server-now-works-with-vs-code](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fb488e878-bd2c-40e0-8d90-cb762842819b&w=3840&q=75)
Set up the Supabase MCP server to work with Visual Studio Code.
[[Twitter](https://supabase.link/twitter-mcp-server-vscode-setup-apr2025-0580)]
## MCP Server can now create and deploy Edge Functions[#](https://supabase.com/changelog#mcp-server-can-now-create-and-deploy-edge-functions)
![mcp-server-can-now-create-and-deploy-edge-functions](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fbb07ecf5-432b-49b1-9e77-437fa16d8035&w=3840&q=75)
Use the Supabase MCP server to build Edge Functions.
[[Twitter](https://supabase.link/twitter-mcp-edge-functions-deploy-apr2025-az9v)]
## Supabase UI Library now includes Infinite Query block[#](https://supabase.com/changelog#supabase-ui-library-now-includes-infinite-query-block)
![supabase-ui-library-now-includes-infinite-query-block](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F87c12f62-5243-4186-9322-3c21f0118f93&w=3840&q=75)
React hook for infinite lists that fetches data from Supabase. Use it for infinite scroll.
[[Link](https://supabase.link/link-supabase-infinite-query-apr2025-23b2)] [[Twitter](https://supabase.link/twitter-supabase-infinite-query-apr2025-ruve)]
## Supabase UI Library now includes Social Auth[#](https://supabase.com/changelog#supabase-ui-library-now-includes-social-auth)
![supabase-ui-library-now-includes-social-auth](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fc88cd048-39f4-4c8b-8a0b-712439a4cd3e&w=3840&q=75)
A block to quickly create authentication UI for [all supported social logins](https://supabase.link/allsupportedsociallogins-supabase-ui-social-auth-apr2025-6vae).
[[Link](https://supabase.link/link-supabase-ui-social-auth-apr2025-4fcs)] [[Twitter](https://supabase.link/twitter-supabase-ui-social-auth-apr2025-vmmi)]
## Quick Product Announcements[#](https://supabase.com/changelog#quick-product-announcements)
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fbc55dcd6-d819-4f1f-a6fb-37fb16818c6f&w=3840&q=75)
  * The new Supabase SOC 2 report is available. [[Link](https://supabase.com/features/soc-2-compliance)]
  * We published comprehensive documentation about our security processes and controls. [[Docs](https://supabase.link/docs-security-docs-overview-apr2025-5xpu)]


## Made with Supabase[#](https://supabase.com/changelog#made-with-supabase)
  * Web application for creating and editing AI-generated avatars using OpenAI's DALL-E API. Built with React, TypeScript, and Supabase. [[GitHub](https://supabase.link/github-ai-avatar-creator-apr2025-96xb)]
  * Data transformation systems engineered for your needs [[GitHub](https://supabase.link/github-data-transformation-systems-apr2025-tgv8)] [[Website](https://supabase.link/website-data-transformation-systems-apr2025-prei)]
  * Command line for finding lines that have specific keywords in Rust . [[GitHub](https://supabase.link/github-rust-cli-keywords-apr2025-byhp)]


## Community Highlights[#](https://supabase.com/changelog#community-highlights)
![community-highlights](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Ffc42f92d-901b-4796-9a19-448b95e1fd95&w=3840&q=75)
  * Create a Reusable Team component for your application using Next.js, Supabase, and Shadcn [[Article](https://supabase.link/article-reusable-team-component-apr2025-dsxs)]
  * Grocery Tracker App using Vue JS and Supabase [[Article](https://supabase.link/article-grocery-tracker-vue-apr2025-f8uy)]
  * Use Supabase MCP in VSCode and Cursor [[Article](https://supabase.link/article-supabase-mcp-vscode-apr2025-u5vp)]
  * Supabase WordPress Integration - SupaWP Plugin [[Article](https://supabase.link/article-supabase-wordpress-plugin-apr2025-njvx)]
  * Implementing multi-tenancy into a Supabase app with Clerk [[Article](https://supabase.link/article-multi-tenancy-supabase-clerk-apr2025-4aza)]
  * Build This Self-Expanding YouTube-Powered AI Agent Knowledge Base (n8n + Supabase) [[YouTube](https://supabase.link/youtube-self-expanding-ai-apr2025-zvzn)]
  * Custom SMTP for Supabase Email Authentication | Complete Setup + Testing [[YouTube](https://supabase.link/youtube-custom-smtp-supabase-apr2025-od4h)]
  * AI Chatbot That Remembers You! (n8n + Supabase + WhatsApp) [[YouTube](https://supabase.link/youtube-ai-chatbot-remembering-apr2025-t09w)]
  * Building a MCP-Powered Task Manager Agent with Agno and Supabase: A Step-by-Step Guide [[Article](https://supabase.link/article-mcp-task-manager-apr2025-pc21)]
  * How to Build an App From SCRATCH with Lovable + Supabase [[YouTube](https://supabase.link/youtube-build-app-scratch-apr2025-k9xh)]

_This discussion was created from the release[Developer Update - April 2025](https://github.com/supabase/supabase/releases/tag/1.25.04)._
### [Dashboard Updates [210425 - 050525] ](https://github.com/orgs/supabase/discussions/35495)
May 6, 2025
## Sort columns in the Table Editor through the column header[#](https://supabase.com/changelog#sort-columns-in-the-table-editor-through-the-column-header)
![Screenshot 2025-05-05 at 14 35 13](https://github.com/user-attachments/assets/6ffe6abd-5f6d-4e8f-841e-26317f36d4e0)
We've integrated the sorting functionality into the column menu - and these will dynamically update based on the current sort state of the column!
PR: <https://github.com/supabase/supabase/pull/35139>
Link: <https://supabase.com/dashboard/project/_/editor>
## Ability to add billing address when creating or upgrading an organization[#](https://supabase.com/changelog#ability-to-add-billing-address-when-creating-or-upgrading-an-organization)
![Screenshot 2025-04-21 at 21 28 39](https://github.com/user-attachments/assets/e2880c25-acd8-46f6-9593-5894162d0649)
You can now set your billing address when creating or upgrading your organization, and also set a billing name that diverges from your organization name! In hopes of alleviating a common request where invoices needed to be amended as there wasn't a billing address set 🙂🙏
PR: <https://github.com/supabase/supabase/pull/34922>
Link: <https://supabase.com/dashboard/new>
## Other bugs fixes and improvements[#](https://supabase.com/changelog#other-bugs-fixes-and-improvements)
[General](https://supabase.com/dashboard/project/_)
  * Add reset database password callout to Connect modal ([PR](https://github.com/supabase/supabase/pull/35241))


[Table Editor](https://supabase.com/dashboard/project/_/editor)
  * (Feature Preview) Fix searching in table editor unintentional clears all tabs ([PR](https://github.com/supabase/supabase/pull/35198))
  * (Feature Preview) Fix tabs order not persisting when a tab is closed ([PR](https://github.com/supabase/supabase/pull/35216))
  * (Feature Preview) Sync tab labels whenever reopening table editor (SQL Editor too) ([PR](https://github.com/supabase/supabase/pull/35219))
  * Fix table editor rendering multiple columns if the column has multiple identical constraints on it ([PR](https://github.com/supabase/supabase/pull/35326))
  * Fix inability to export data when all rows are selected ([PR](https://github.com/supabase/supabase/pull/35420))


[SQL Editor](https://supabase.com/dashboard/project/_/sql)
  * (Feature Preview) Fix snippets being renamed by AI not updating it's tab label ([PR](https://github.com/supabase/supabase/pull/35218))


[Storage Explorer](https://supabase.com/dashboard/project/_/buckets)
  * Fix footer in list view unintentionally hiding last item ([PR](https://github.com/supabase/supabase/pull/35036))


[Edge Functions](https://supabase.com/dashboard/project/_/functions)
  * Fix logs refresh button not pulling latest data when "Last n" option is selected ([PR](https://github.com/supabase/supabase/pull/35194))


[Logs](https://supabase.com/dashboard/project/_/logs/explorer)
  * Fix datepicker overriding copy events ([PR](https://github.com/supabase/supabase/pull/35361))


[Integrations](https://supabase.com/dashboard/project/_/integrations)
  * Add link to foreign table in table editor from wrappers ([PR](https://github.com/supabase/supabase/pull/35242))


[Custom Reports](https://supabase.com/dashboard/project/_/reports)
  * Fix missing labels on SQL blocks ([PR](https://github.com/supabase/supabase/pull/35328))


### [Project scoped roles now available in Team plans ](https://github.com/orgs/supabase/discussions/35172)
Apr 21, 2025
[Project scoped roles](https://supabase.com/docs/guides/platform/access-control#organization-scoped-roles-vs-project-scoped-roles) are now available for all Supabase Team plans.
With project scoped roles, you can:
  * Restrict team member access to specific projects
  * Set different permission levels for different projects
  * Maintain better security boundaries within your organization
  * Simplify compliance requirements, including HIPAA


Each member in the organization can be assigned a role scoped to the organization or to specific projects. If the member has a role at the organization level, they will have the equivalent permissions for that role across all current and future projects in the organization.
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fa0d0ed5e-2e17-44a9-8eed-6f89d78f6482&w=3840&q=75)
With project scoped permissions, you can assign members to roles scoped to specific projects within your organization.
![image-2](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F11f8c18c-44b8-44aa-adfd-ddc6c5b73baf&w=3840&q=75)
To get started with project scoped roles visit your organization's [team settings page](https://supabase.com/dashboard/org/_/team) to add users and manage their roles. If you're adding project scoped roles for a new user, you can only select one project when sending the invite. You can assign roles to multiple projects after the user accepts the invite.
### [Dashboard Updates [070425 - 210425] ](https://github.com/orgs/supabase/discussions/35169)
Apr 21, 2025
## (Upcoming) Dashboard layout update for organizations[#](https://supabase.com/changelog#upcoming-dashboard-layout-update-for-organizations)
![Screenshot 2025-04-21 at 14 02 09](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F6b98bb8f-3676-4070-9179-a17a7f439b5e&w=3840&q=75) ![Screenshot 2025-04-21 at 14 02 39](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fab0f26a2-7e32-4e33-bcfa-6e1dc71ec00d&w=3840&q=75)
We've updated the layout of the dashboard in hopes to improve the UX for managing team members and billing for organizations, as well as to clearly show the relationship between organizations and their projects. The home page of the dashboard is now scoped to a selected organization instead of showing all projects across all organizations, and accessing organization settings are now in individual links in the side navigation bar.
This isn't publicly available just yet, but we're looking to incrementally roll this out to everyone in batches over the next few weeks, starting as a feature preview initially where you can opt in to experience the updated layout. We'd also love to hear any thoughts or feedback that you might have - do feel free to reach out to us! We're just a message away from the Feedback button at the top right corner of the dashboard 🙏🙂
PR: <https://github.com/supabase/supabase/pull/33150>
Link: <https://supabase.com/dashboard>
## Revamped billing breakdown in organization settings[#](https://supabase.com/changelog#revamped-billing-breakdown-in-organization-settings)
![Screenshot 2025-04-09 at 19 35 37](https://github.com/user-attachments/assets/52a5a94e-2794-4c2e-915b-16cf67441e24)
As with our commitment to making billing as transparent as possible, we've made a number of improvements to the billing breakdown section under your organization settings, such as adding individual documentation links to each usage items charged, adding separate items for read replicas / branching, and more! Read more details about the changes if you might be interested in the attached PR below 🙂
PR: <https://github.com/supabase/supabase/pull/34861>
Link: <https://supabase.com/dashboard/org/_/billing>
## Add Database upgrade logs[#](https://supabase.com/changelog#add-database-upgrade-logs)
![image](https://github.com/user-attachments/assets/93dc6dc4-664b-481e-ae97-1bddb5a3d2ba) ![image](https://github.com/user-attachments/assets/6ef90953-6b28-4efc-b60e-b74465d653bd)
We've added the ability to browse logs relating to database upgrade operations as a way to troubleshoot failed upgrades. Unsuccessful database upgrades are reflected with an alert on the project's home page which now also includes a link to the database upgrade logs along with the exact time interval when the upgrade took place. 🛠️ 🚧
PR: <https://github.com/supabase/supabase/pull/27924>
Link: <https://supabase.com/dashboard/project/_/logs/pg-upgrade-logs>
## Feature previews are now available on local / self-hosted Studio[#](https://supabase.com/changelog#feature-previews-are-now-available-on-local--self-hosted-studio)
Feature previews have always been available only for the hosted version of the dashboard, but we've decided to make it available for local / self-hosted version of the dashboard too!(Studio) Only feature previews that are relevant to the project will be present, so you'll be able to start using the Tabs interfaces for the Table Editor and SQL Editor soon once we've cut a new release 😉
PR: <https://github.com/supabase/supabase/pull/35060>
## Other bug fixes and improvements[#](https://supabase.com/changelog#other-bug-fixes-and-improvements)
[Table Editor](https://supabase.com/dashboard/project/_/editor)
  * Clean up filters and sorts if applied on a column that has been deleted ([PR](https://github.com/supabase/supabase/pull/34934))
  * Optimize row retrieval with CTE to improve load times by almost 30x on larger tables ([PR](https://github.com/supabase/supabase/pull/35071))


[SQL Editor](https://supabase.com/dashboard/project/_/sql/new)
  * (Feature Preview) Persist scroll position when switching between snippet tabs ([PR](https://github.com/supabase/supabase/pull/35094))
  * Fix missing styles when multiple snippets are selected via shift click ([PR](https://github.com/supabase/supabase/pull/35092))


[Reports](https://supabase.com/dashboard/project/_/reports)
  * Support dragging a SQL chart from the Assistant into an empty custom report ([PR](https://github.com/supabase/supabase/pull/34930))


[Logs](https://supabase.com/dashboard/project/_/logs/explorer)
  * Consolidate date picker in logs to a single UI ([PR](https://github.com/supabase/supabase/pull/33164))
  * Add "Last 3 hours" option ([PR](https://github.com/supabase/supabase/pull/34782))
  * Add "Copy as JSON" button when view log details ([PR](https://github.com/supabase/supabase/pull/34784))
  * Add hint and query details to Postgres Logs ([PR](https://github.com/supabase/supabase/pull/34152))
  * Fix `cmd+z` undo behaviour in logs explorer ([PR](https://github.com/supabase/supabase/pull/35086))


[Integrations](https://supabase.com/dashboard/project/_/integrations)
  * Add `meters` table for Stripe FDW ([PR](https://github.com/supabase/supabase/pull/34781))
  * Add Slack FDW ([PR](https://github.com/supabase/supabase/pull/35053))
  * Add Cloudflare D1 FDW ([PR](https://github.com/supabase/supabase/pull/35055))
  * Add Hubspot FDW ([PR](https://github.com/supabase/supabase/pull/35059))
  * Add Orb FDW ([PR](https://github.com/supabase/supabase/pull/35061))


### [Developer Update - March 2025 ](https://github.com/orgs/supabase/discussions/34839)
Apr 8, 2025
Here’s a recap of everything we announced during Launch Week and the month of March:
## Supabase MCP Server[#](https://supabase.com/changelog#supabase-mcp-server)
![lw14-mcp-email](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F8fe72d08-6d56-41fa-9be2-3f21125d64cf&w=3840&q=75)
We are launching an official Supabase MCP server. You can use this server to connect your favorite AI tools (such as Cursor or Claude) directly with Supabase.
[[Link](https://supabase.link/link-supabase-mcp-server-mar2025-67zo)] [[GitHub](https://supabase.link/github-supabase-mcp-launch-mar2025-o0h9)]
## Supabase UI Library[#](https://supabase.com/changelog#supabase-ui-library)
![lw14-ui-email](https://github.com/user-attachments/assets/92bbf147-626d-4501-955a-3122edece47d)
A set of convenient components built on shadcn that can be dropped into any Next.js, React Router, Tanstack Start, or vanilla React application. This initial release includes the following components:
  * [Password-based authentication](https://supabase.link/password-basedauthentication-password-authentication-guide-mar2025-cw5l)
  * [File Upload Dropzone](https://supabase.link/fileuploaddropzone-file-upload-dropzone-mar2025-hfeq)
  * [Realtime Cursor Sharing](https://supabase.link/realtimecursorsharing-realtime-cursor-sharing-mar2025-baf8)
  * [Current User Avatar](https://supabase.link/currentuseravatar-current-user-avatar-mar2025-6tay)
  * [Realtime Avatar Stack](https://supabase.link/realtimeavatarstack-realtime-avatar-stack-mar2025-ut53)
  * [Realtime Chat](https://supabase.link/realtimechat-realtime-chat-feature-mar2025-4xwk)


[[Link](https://supabase.link/link-supabase-ui-library-mar2025-sy2o)]
## Supabase Studio Improvements[#](https://supabase.com/changelog#supabase-studio-improvements)
![lw14-dashboard-updates-email](https://github.com/user-attachments/assets/d303d9e2-50e5-4220-a9c2-99a46f85cffa)
We shipped a number of Supabase Studio improvements and new features. Here’s a quick rundown of what’s new:
  * **Tabs!** : The Table Editor and SQL Editor now have tabs!
  * **Customizable Reports** : create reports to show data exactly how you want to see it
  * **SQL Blocks in Custom reports** : use SQL Snippets in blocks inside your custom reports
  * **Inline SQL Editor** : use a mini SQL Editor anywhere in the Dashboard
  * **Multiple AI Assistant chats** : maintain history of your Assistant chats
  * **Logs improvements** : more detailed inspect panel, and stacked charts


[[Link](https://supabase.link/link-supabase-studio-updates-mar2025-3pej)] [[GitHub](https://supabase.link/github-supabase-studio-updates-mar2025-0w2r)]
## Edge Functions Deploy from the Supabase Dashboard[#](https://supabase.com/changelog#edge-functions-deploy-from-the-supabase-dashboard)
![lw14-dashboard-updates-email](https://github.com/user-attachments/assets/23a51ab6-4d1c-4fae-acf4-cd13f6e8b646)
You can now create, test, edit, and deploy Supabase Edge Functions directly from the Supabase Dashboard.
[[Link](https://supabase.link/link-edge-functions-deploy-dashboard-mar2025-8ttw)]
## Realtime Broadcast from Database[#](https://supabase.com/changelog#realtime-broadcast-from-database)
![lw14-realtime-database-email](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F9ce0bbac-80ea-4006-988c-ef791ce9ab98&w=3840&q=75)
Send messages based on changes in the Database, directly from the Database itself. Scale to support sending Database change messages to tens of thousands of users.
[[Link](https://supabase.link/link-realtime-database-broadcast-mar2025-08p2)]
## Declarative Schemas[#](https://supabase.com/changelog#declarative-schemas)
![lw14-declarative-schemas-email](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F0e95408a-c797-4a0d-ae88-3cf17909c98f&w=3840&q=75)
Use declarative schemas to define your database structure in a clear, centralized, and version-controlled manner.
[[Link](https://supabase.link/link-declarative-schemas-database-mar2025-vlqf)]
## Postgres Language Server[#](https://supabase.com/changelog#postgres-language-server)
![lw14-pls-email-black](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F641beeef-3d37-4bf2-b0df-4ecef2efcded&w=3840&q=75)
Postgres Language Server provides a collection of language tools and a Language Server Protocol (LSP) implementation for Postgres, focusing on developer experience and reliable SQL tooling. Today, we support autocompletion, syntax error highlighting, type-checking, and a linter.
[[Link](https://supabase.link/link-postgres-language-server-tools-mar2025-2ple)]
## Quick Product Announcements[#](https://supabase.com/changelog#quick-product-announcements)
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fb9d1f605-998a-47ce-b9e2-05c6c877e572&w=3840&q=75)
  * We expanded our official Third-party Auth integrations to include [Clerk](https://supabase.link/clerk-third-party-auth-clerk-mar2025-hlnq). We also made Third-party Auth cheaper so that it has pricing parity with Supabase Auth. [[Link](https://supabase.link/link-third-party-auth-clerk-mar2025-qu0z)]
  * We have added Deno 2.1 support for Supabase Edge Runtime. With Deno 2.1, you can use built-in tools to scaffold a new project, manage dependencies, run tests, and lints. [[Link](https://supabase.link/link-deno-2-1-support-mar2025-j2ee)]
  * You can now automate generation and updates of embeddings in your database. [[Link](https://supabase.link/link-automate-embeddings-updates-mar2025-o0r1)] [[Docs](https://supabase.link/docs-automate-embeddings-updates-mar2025-mtlt)]
  * Geo-aware routing for Supabase API Load Balancer optimizes requests performance for your globally distributed users. [[Link](https://supabase.link/link-geo-aware-routing-mar2025-31v5)]
  * Dedicated Poolers are now available in Supabase for everyone on the Pro Plan and above. [[Blog](https://supabase.link/blog-dedicated-poolers-pro-mar2025-lvvf)] [[Link](https://supabase.link/link-dedicated-poolers-available-mar2025-0tgw)]
  * The Supabase docs now support type hints. [[Link](https://supabase.link/link-supabase-type-hints-mar2025-822n)]


## Launch Week Hackathon Winners[#](https://supabase.com/changelog#launch-week-hackathon-winners)
![lw14-hackathon-winners-email](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F05fe2577-87ac-4254-bba9-49c35b37fb08&w=3840&q=75)
  * AI RPG - An Interactive storytelling platform that enables players to create and play through AI-generated narrative adventures. [[Tweet](https://supabase.link/tweet-ai-rpg-narratives-mar2025-q8uf)]
  * AI Travel Concierge - An app that helps you travel by suggesting destinations and attractions and planning them. [[Tweet](https://supabase.link/tweet-ai-travel-assistant-mar2025-p6cy)]
  * CiteAnalytics - A web analytics tool that tracks when LLM visits your website. [[Tweet](https://supabase.link/tweet-citeanalytics-llm-tracking-mar2025-ujpb)]
  * play.theplaylist - Create YouTube playlists with an interactive UI and easily share it with friends. [[Tweet](https://supabase.link/tweet-create-youtube-playlists-mar2025-bkcf)]
  * sendit - A social media content creation tool to refine posts using AI. [[Tweet](https://supabase.link/tweet-sendit-ai-tool-mar2025-113z)]
  * StoryTime - Generate educational stories for kids using AI. [[Tweet](https://supabase.link/tweet-storytime-ai-stories-mar2025-cvwt)]
  * Supabadge - Generate your own beautiful Supabase event badge! [[Tweet](https://supabase.link/tweet-supabadge-generate-event-mar2025-q7so)]
  * SupaQuery - Supabase SQL editor with Vim support. [[Tweet](https://supabase.link/tweet-supaquery-sql-vim-mar2025-gxm8)]
  * QuickAudit - An app that logs every DB change (INSERT/UPDATE/DELETE) for auditing. [[Tweet](https://supabase.link/tweet-quick-audit-db-logs-mar2025-mwid)]
  * Today’s Diary - A diary app with a minimalistic UI that lets you exchange diary entries with another random user every day. [[Tweet](https://supabase.link/tweet-diary-app-exchange-mar2025-p5nq)]


## Made with Supabase[#](https://supabase.com/changelog#made-with-supabase)
  * MagiCan - Finalist of our Lovable x Supabase hackathon. An infinite canvas platform that revolutionizes collaborative storytelling and project planning with advanced AI capabilities. [[Website](https://supabase.link/website-magican-finalist-hackathon-mar2025-ligv)]
  * Next.js + Stripe + Supabase A Production-Ready Template - Start building with authentication and payments in minutes. [[GitHub](https://supabase.link/github-nextjs-stripe-supabase-mar2025-5jfb)] [[Website](https://supabase.link/website-nextjs-stripe-supabase-mar2025-5qu1)]
  * Hono Supabase Auth Example - This example shows how to use Supabase Auth both on the client and server side with Hono. [[GitHub](https://supabase.link/github-hono-supabase-auth-mar2025-zy9i)]
  * Discover exactly when you can achieve financial independence with FireCalculator a precision calculator and visualization tools. [[Website](https://supabase.link/website-financial-independence-timing-mar2025-ncs5)]


## Community Highlights[#](https://supabase.com/changelog#community-highlights)
  * Implementing multi-tenancy into a Supabase app with Clerk [[Link](https://supabase.link/link-multi-tenancy-supabase-clerk-mar2025-3vfc)]
  * Supabase Just Dropped Their Own Fullstack UI Library! [[YouTube](https://supabase.link/youtube-supabase-ui-library-mar2025-uy13)]
  * Generating and Storing Google Gemini Embeddings with Vercel AI SDK and Supabase [[Link](https://supabase.link/link-google-gemini-embeddings-mar2025-kidk)]
  * Secure Your Next.js App: Email & Google Authentication with Supabase, PostgreSQL RLS, and Triggers [[Link](https://supabase.link/link-secure-nextjs-authentication-mar2025-olom)]
  * Supabase just dropped an official MCP Server [[YouTube](https://supabase.link/youtube-supabase-mcp-server-launch-mar2025-yy9s)]

_This discussion was created from the release[Developer Update - March 2025](https://github.com/supabase/supabase/releases/tag/1.25.03)._
### [Dashboard Updates [240225 - 070425] ](https://github.com/orgs/supabase/discussions/34794)
Apr 7, 2025
What better way to wrap up Launch Week 14 than a summary of what was shipped to the dashboard (as well as several other goodies that we also shipped behind the scenes 😉)
## Manage your Edge Functions directly from the dashboard[#](https://supabase.com/changelog#manage-your-edge-functions-directly-from-the-dashboard)
![image](https://github.com/user-attachments/assets/e3381944-e96b-4ca6-97de-6ee77174119d)
You can now create and update your Edge Functions directly from the dashboard! We've introduced a new "Code" tab to the Edge Functions details page, which makes it possible to view and edit your Edge Function source code, then deploy the changes.
PRs:
  * <https://github.com/supabase/supabase/pull/33726>
  * <https://github.com/supabase/supabase/pull/33727>


Link: <https://supabase.com/dashboard/project/_/functions>
## Test your Edge Functions from the dashboard too![#](https://supabase.com/changelog#test-your-edge-functions-from-the-dashboard-too)
![image](https://github.com/user-attachments/assets/bba3b3b6-dd88-4f18-806e-f8f26bc7b532)
To put the cherry on top, we've also introduced an Edge Function tester (which is basically a simplified version of Postman) that can be used to send requests to an Edge Function for testing. Access this UI by hitting the "Test" button while in an Edge Function 🙂
PR: <https://github.com/supabase/supabase/pull/33728>
Link: <https://supabase.com/dashboard/project/_/functions>
## Tabs for the Table Editor and SQL Editor[#](https://supabase.com/changelog#tabs-for-the-table-editor-and-sql-editor)
![Screenshot 2025-04-07 at 19 47 57](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fb17f02d8-aad1-42d5-afcc-30701c9a5a68&w=3840&q=75)
![Screenshot 2025-04-07 at 19 48 30](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F6167c731-b4cf-4a13-a83c-61fec84342b1&w=3840&q=75)
For those who've been with us since the very beginning, you might remember that we used to have tabs in the Table Editor which we eventually removed 😉 We're bringing this nifty UX back with a better UX too, and also introducing this into the SQL Editor as well! Conveniently go between tables across schemas, or flip between snippets without having to navigate through your list of queries (especially if you've got tons of them!)
These are currently behind their own feature previews at the moment, which you can access by clicking on your Profile picture in the top navigation bar. Feel free to let us know what you think!
PR: <https://github.com/supabase/supabase/pull/31071>
Link: <https://supabase.com/dashboard/project/_/editor>
## Support for multiple Assistant chats[#](https://supabase.com/changelog#support-for-multiple-assistant-chats)
![image](https://github.com/user-attachments/assets/69e91dcd-cee8-4ab3-b19d-3f173cee4614)
We've added the ability to create and store multiple chats per project! Switch contexts without losing your conversation with the Assisant, and come back easily from where you left off thereafter too! Chats are also now scoped per project, so switching project also switches the chat.
PR: <https://github.com/supabase/supabase/pull/34011>
Link: <https://supabase.com/dashboard/project/_>
## Support updating your account's email address and unlink identities[#](https://supabase.com/changelog#support-updating-your-accounts-email-address-and-unlink-identities)
![](https://github.com/user-attachments/assets/a527a2b7-4053-42f7-85b2-e7ae00e51ecc)
Account Information has now been replaced with Account Identities and it'll display what identities are linked to your account (either Email and/or GitHub, or SSO). We've also added support for changing your account's email address if you've got an Email identity with us.
PR: <https://github.com/supabase/supabase/pull/33966>
Link: <https://supabase.com/dashboard/account/me>
## Support saving preference for navigation side bar expand behaviour[#](https://supabase.com/changelog#support-saving-preference-for-navigation-side-bar-expand-behaviour)
We've received multiple feedback from users regarding the expansion behaviour of the side navigation bar while in a project, and realised there was an almost even split between individual preferences on how the side bar should behave (keep expanded, keep closed, or expand on hover). As such, we've decided to make this behaviour controllable to your own preference, available now in the account preferences page 😄
PR: <https://github.com/supabase/supabase/pull/33612>
Link: <https://supabase.com/dashboard/project/_>
## Other bug fixes and improvements[#](https://supabase.com/changelog#other-bug-fixes-and-improvements)
[Account](https://supabase.com/dashboard/account/audit)
  * Fix selection of single date for audit logs not returning any results ([PR](https://github.com/supabase/supabase/pull/34689))


[AI Assistant](https://supabase.com/dashboard/project/_)
  * Cache results in browser for the queries that are generated and ran ([PR](https://github.com/supabase/supabase/pull/34509))


[Table Editor](https://supabase.com/dashboard/project/_/editor)
  * Fix exporting tables with large amount of rows ([PR](https://github.com/supabase/supabase/pull/33906))
  * Fix updating a foreign key type while trying to add a foreign key at the same time ([PR](https://github.com/supabase/supabase/pull/34121))


[Logs](https://supabase.com/dashboard/project/_/logs/explorer)
  * Update Field Reference for logs to show parameters for Shared and Dedicated Pooler ([PR](https://github.com/supabase/supabase/pull/34432))


[Reports](https://supabase.com/dashboard/project/_/reports/database)
  * Add Dedicated Pooler connections to Database report ([PR](https://github.com/supabase/supabase/pull/33895))


[Storage Explorer](https://supabase.com/dashboard/project/_/buckets)
  * Fix switching buckets while uploading files to not upload to the bucket that was switched to ([PR](https://github.com/supabase/supabase/pull/34094))


[Database](https://supabase.com/dashboard/project/_/database/backups)
  * Use TimestampInfo to show relative date and times for database backups ([PR](https://github.com/supabase/supabase/pull/33892))


[Project Integrations](https://supabase.com/dashboard/project/_/integrations)
  * Add Notion FDW ([PR](https://github.com/supabase/supabase/pull/33988))
  * Add Clerk FDW ([PR](https://github.com/supabase/supabase/pull/33803))


### [Supabase Management API `GET` Logs Restrictions ](https://github.com/orgs/supabase/discussions/34634)
Apr 1, 2025
We will be enforcing stricter limitations on the v0 and v1 [`GET` Project Logs endpoint](https://api.supabase.com/api/v1#tag/default):
`
1
GET /v1/projects/{ref}/analytics/endpoints/logs.all
2
GET /v0/projects/{ref}/analytics/endpoints/logs.all
`
The restrictions are as so:
  * If neither `?iso_timestamp_start=` nor `?iso_timestamp_end=` is provided, the queried timestamp range will be the last 1 minute.
  * If either `?iso_timestamp_start=` or `?iso_timestamp_end=` is provided, the queried timestamp range will be a 1 minute window either before or after the provided query parameter.
  * If both `?iso_timestamp_start=` and `?iso_timestamp_end=` are provided, the maximum allowed queried timestamp range is 24 hours. The size of the permitted window may be subject to change in the future.


This change will go into effect at 2 April 12pm SGT (4am UTC).
### [Upcoming Change: Improved Experimental Routing for Read Replica Load Balancers ](https://github.com/orgs/supabase/discussions/34494)
Mar 27, 2025
Starting on April 4th, 2025, we will be enhancing the routing behavior for experimental routing on eligible Data API requests. This change affects GET requests to Data APIs only; the routing behavior for all other requests remains unchanged:
Current behavior: Round-robin distribution among all databases (primary and all read replicas) in your project
New behavior: Geo-routing that directs requests to the closest available database
This enhancement delivers a better experience for your users by minimizing latency to your project. You can maximize these benefits by strategically placing Read Replicas close to your major customer locations.
For more information on geo-routing and experimental routing, please visit [our documentation](https://supabase.com/docs/guides/platform/read-replicas#experimental-routing)
### [Dedicated Pooler with PgBouncer ](https://github.com/orgs/supabase/discussions/34404)
Mar 25, 2025
Today we’re announcing the official release of **Dedicated Pooler** - a PgBouncer instance co-located with your Postgres database for lower latency, better performance, and higher reliability.
This is available today for paid plans on the Supabase platform while free and paid plans continue to benefit from our **Shared Pooler** via Supavisor.
### Why Dedicated Poolers[#](https://supabase.com/changelog#why-dedicated-poolers)
We created Dedicated Poolers to give you the ultimate flexibility in choosing the right connection type for your specific use case.
Now you have three options for connecting to your database and you can mix and match depending on your use case:
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fe40e79bd-2524-49d6-a199-f98fc21ba62d&w=3840&q=75)
  1. **Direct connections (All Plans):** Recommended for when you are connecting using servers.
  2. **Shared Pooler (All Plans):** Recommended for when you are connecting using serverless functions (like Next.js or AWS Lambda) and/or IPv6-only networks.
  3. **Dedicated Pooler (Paid Plans):** Recommended for when you are connecting using serverless functions and you start to scale up. Available on Pro Plan and above.


### How It Works[#](https://supabase.com/changelog#how-it-works)
  * **Dedicated Pooler (IPv6 Only) - O** nly `transaction` mode is available. For IPv4-only networks, purchase the IPv4 add on or use the **Shared Pooler.**
  * **Shared Pooler (IPv4 + IPv6)** - Both `transaction` and `session` modes are available. Use this Pooler only for networks that don't support IPv4 or if you need prepared statements.
  * **Dedicated Pooler Prepared Statement Support (Coming Soon) -** We plan to support prepared statements in `transaction` mode by upgrading all PgBouncer instances to version 1.21+.


Get started by navigating to your project’s [Connect settings](https://supabase.link/connect-settings) or learn more about **Dedicated Poolers** by reading the [announcement](https://supabase.link/dedicated-poolers-announcement) or going through the [docs](https://supabase.link/dedicated-poolers-doc).
### [Restricting Access on Auth, Storage, and Realtime Schemas on April 21, 2025 ](https://github.com/orgs/supabase/discussions/34270)
Mar 18, 2025
On April 21, we are restricting certain SQL actions you can perform in your database’s `auth`, `storage`, and `realtime` schemas.
## Why are we making these restrictions?[#](https://supabase.com/changelog#why-are-we-making-these-restrictions)
Supabase Auth, Storage, and Realtime services each rely on their respective schemas in order to function properly.
These restrictions prevent unintended side effects like third-party tooling and user defined changes altering schemas or their objects, such as migration tables and database functions, that could disrupt or break functionality.
## What this means for your project[#](https://supabase.com/changelog#what-this-means-for-your-project)
On April 21, you will no longer be able to perform the following actions on the `auth`, `storage`, and `realtime` schemas:
  * Create tables and database functions
  * Drop existing tables or database functions
  * Create indexes on existing tables
  * Perform destructive actions (i.e. `INSERT`, `UPDATE`, `DELETE`, `TRUNCATE`) on the following migration tables: 
    * `auth.schema_migrations`
    * `storage.migrations`
    * `realtime.schema_migrations`
  * Revoking privileges on tables in these schemas from API roles (e.g. `anon`)


However, you will still have permissions to perform the following actions:
  * Create foreign keys referencing tables in the `auth`, `storage`, and `realtime` schemas
  * Create RLS policies and database triggers on the following tables: 
    * `auth.audit_log_entries`
    * `auth.identities`
    * `auth.refresh_tokens`
    * `auth.sessions`
    * `auth.users`
    * `storage.buckets`
    * `storage.migrations`
    * `storage.objects`
    * `storage.s3_multipart_uploads`
    * `storage.s3_multipart_uploads_parts`
    * `realtime.messages`


## How to determine if you’re affected?[#](https://supabase.com/changelog#how-to-determine-if-youre-affected)
  * Run the following query to check if you created any tables in the `auth`, `storage`, and `realtime` schemas:


`
1
SET search_path = '';
2
SELECT oid::regclass AS table_name
3
FROM pg_class 
4
WHERE 
5
  (relnamespace = 'auth'::regnamespace AND relowner != 'supabase_auth_admin'::regrole) 
6
  OR (relnamespace = 'storage'::regnamespace AND relowner != 'supabase_storage_admin'::regrole) 
7
  OR ( 
8
    relnamespace = 'realtime'::regnamespace
9
    AND relowner NOT IN ( 
10
      SELECT oid 
11
      FROM pg_roles 
12
      WHERE rolname IN ('supabase_admin', 'supabase_realtime_admin') 
13
    ) 
14
  );
`
  * Run the following query to check if you created any database functions in the `auth`, `storage`, and `realtime` schemas:


`
1
SET search_path = '';
2
SELECT pg_catalog.format('%s(%s)', oid::regproc, pg_get_function_identity_arguments(oid::regproc)) AS function_name
3
FROM pg_proc 
4
WHERE 
5
  (pronamespace = 'auth'::regnamespace AND proowner != 'supabase_auth_admin'::regrole) 
6
  OR (pronamespace = 'storage'::regnamespace AND proowner != 'supabase_storage_admin'::regrole) 
7
  OR ( 
8
    pronamespace = 'realtime'::regnamespace 
9
    AND proowner NOT IN ( 
10
      SELECT oid 
11
      FROM pg_roles 
12
      WHERE rolname IN ('supabase_admin', 'supabase_realtime_admin') 
13
    ) 
14
  );
`
## What you need to do[#](https://supabase.com/changelog#what-you-need-to-do)
If any of the above queries return a result, you must move them to either the `public` schema or a schema that you’ve created. Otherwise, they will be deleted.
  * Here’s how you can move a table to another schema:


`
1
CREATE SCHEMA IF NOT EXISTS my_custom_schema;
2
ALTER TABLE storage.my_custom_table SET SCHEMA my_custom_schema;
`
  * Here’s how you can move a database function to another schema:


`
1
CREATE SCHEMA IF NOT EXISTS my_custom_schema;
2
ALTER FUNCTION storage.custom_function() SET SCHEMA my_custom_schema;
`
Additionally, if you're using [Migrations](https://supabase.com/docs/guides/deployment/database-migrations) or [Branching](https://supabase.com/docs/guides/deployment/branching), you'll need to patch your migrations to move these objects to your own schemas. E.g. if you have a migration `20250101000000_add_custom_table.sql` like so:
`
1
-- ...
2
CREATE TABLE auth.my_custom_table (
3
 -- id int8 ...
4
);
5
-- ...
`
Then you need to edit it locally into:
`
1
-- ...
2
CREATE SCHEMA IF NOT EXISTS my_custom_schema;
3
CREATE TABLE my_custom_schema.my_custom_table (
4
 -- id int8 ...
5
);
6
-- ...
`
Then you'll need to repair the migration history on the linked project:
`
1
supabase migration repair --status reverted 20250101000000
2
supabase migration repair --status applied 20250101000000
`
### [Developer Update - February 2025 ](https://github.com/orgs/supabase/discussions/34067)
Mar 7, 2025
Here’s everything that happened with Supabase in the last month:
## Deploy Edge Functions from the Supabase dashboard[#](https://supabase.com/changelog#deploy-edge-functions-from-the-supabase-dashboard)
![deploy-edge-functions-from-the-supabase-dashboard](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F8e327a4c-ca78-4528-bb66-4175abe396dd&w=3840&q=75)
Write your Edge Function in the dashboard using the AI Assistant and deploy it directly.
[[Link](https://supabase.link/link-deploy-edge-functions-feb2025-riur)]
## Deploy Edge Functions from the CLI[#](https://supabase.com/changelog#deploy-edge-functions-from-the-cli)
![deploy-edge-functions-from-the-cli](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F27a2f6a7-8c69-494b-a363-d48dd3fc9b77&w=3840&q=75)
Write your Edge Function locally and deploy it using the CLI and without having to install Docker.
[[Link](https://supabase.link/link-deploy-edge-functions-feb2025-vjje)] [[GitHub](https://supabase.link/github-deploy-edge-functions-feb2025-ke1x)]
## Deploy Edge Functions using the API[#](https://supabase.com/changelog#deploy-edge-functions-using-the-api)
![deploy-edge-functions-using-the-api](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fb38ccee8-5dc0-4a06-87a1-690be64916a8&w=3840&q=75)
AI tools and other products that integrate with Supabase can now deploy Edge Functions using the Supabase API.
[[Link](https://supabase.link/link-deploy-edge-functions-feb2025-k76n)] [[GitHub](https://supabase.link/github-deploy-edge-functions-feb2025-be3l)]
## Connect AI tools and LLMs to Supabase[#](https://supabase.com/changelog#connect-ai-tools-and-llms-to-supabase)
![connect-ai-tools-and-llms-to-supabase](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F213684a4-a7e4-491f-92a9-5b76f26644e3&w=3840&q=75)
We’ve published documentation on how to use the Model Context Protocol (MCP) to connect external AI tools to Supabase. Use natural language commands to perform operations in Supabase.
[[Link](https://supabase.link/link-connect-ai-supabase-feb2025-nwod)] [[Docs](https://supabase.link/docs-connect-ai-tools-supabase-feb2025-nkno)]
## Third-party Auth is now less expensive[#](https://supabase.com/changelog#third-party-auth-is-now-less-expensive)
![third-party-auth-is-now-a-lot-cheaper](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fa03fd89b-c152-4c4c-8b48-bbd5368d0fcf&w=3840&q=75)
We’ve increased the MAU quota for using third-party authentication providers so it’s easier (and more cost-effective) to start using Supabase with an existing project that uses another auth provider.
[[Link](https://supabase.link/link-third-party-auth-costs-feb2025-ztkm)]
## New billing documentation[#](https://supabase.com/changelog#new-billing-documentation)
![new-billing-documentation](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F94cc8c13-1a17-455c-8cff-41375f3441c5&w=3840&q=75)
Better explanations for how bills are computed, upgrading/downgrading subscriptions, and concepts such as Credits or Spend Caps.
[[Docs](https://supabase.link/docs-billing-explanations-updates-feb2025-r7cc)]
## Using Postgres as a Graph Database[#](https://supabase.com/changelog#using-postgres-as-a-graph-database)
![using-postgres-as-a-graph-database](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Ff308c5a1-7c97-44f9-bc6c-dce5760aefdd&w=3840&q=75)
pgRouting is a Postgres extension that can be used to add basic graph functionality to Postgres.
[[Blog Post](https://supabase.link/blogpost-postgres-graph-database-feb2025-tv92)]
## Quick Product Announcements[#](https://supabase.com/changelog#quick-product-announcements)
  * Invoke the SQL Editor from anywhere in the Supabase Dashboard [[Link](https://supabase.link/link-sql-editor-invoke-feb2025-qm5g)]
  * Read HubSpot data from within Postgres using the new FDW [[Link](https://supabase.link/link-hubspot-postgres-fdw-feb2025-5xbp)]
  * Read Notion data from within Postgres using the new FDW [[Link](https://supabase.link/link-notion-data-postgres-feb2025-ndhi)]


## Made with Supabase[#](https://supabase.com/changelog#made-with-supabase)
  * Stripe SaaS OSS with Supabase. Launch Full-Stack Apps 100x Easier.[[GitHub](https://supabase.link/github-stripe-saas-supabase-feb2025-3d9b)] [[YouTube](https://supabase.link/youtube-stripe-saas-supabase-feb2025-z0id)]
  * Atomic CRM. The Open-Source CRM Toolkit for Personalized Solutions [[](https://supabase.link/-atomic-crm-toolkit-feb2025-r8u9)[GitHub](https://supabase.link/github-atomic-crm-toolkit-feb2025-yuhn)] [[Website](https://supabase.link/website-atomic-crm-toolkit-feb2025-ctnu)]
  * GymBrah. Run your fitness business without chaos [[GitHub](https://supabase.link/github-gymbrah-fitness-business-feb2025-t4zq)][[Website](https://supabase.link/website-gymbrah-fitness-business-feb2025-ohtd)]
  * SQL Noir. Learn SQL by solving crimes [[GitHub](https://supabase.link/github-sql-noir-crimes-feb2025-yd7i)] [[Website](https://supabase.link/website-sql-noir-crimes-feb2025-yo87)]


## Community Highlights[#](https://supabase.com/changelog#community-highlights)
  * Global Community Meetups [[Sign up here](https://supabase.link/signuphere-global-community-meetups-feb2025-b2ki)]
  * The easiest way to get started selling SaaS with Polar [[Repo](https://supabase.link/repo-sell-saas-polar-feb2025-osfi)]
  * Supabase 2025 Full Free Course [[YouTube](https://supabase.link/youtube-supabase-free-course-feb2025-dqke)]
  * Build the Reddit Clone with Supabase [[YouTube](https://supabase.link/youtube-reddit-clone-supabase-feb2025-jzl5)]
  * How to Use Cursor Agent and Supabase to Maximize Productivity [[YouTube](https://supabase.link/youtube-cursor-agent-supabase-feb2025-052q)]
  * Multilingual transcription Telegram bot using Supabase and ElevenLabs Scribe API [[Demo](https://supabase.link/demo-multilingual-transcription-bot-feb2025-tg0b)][[YouTube](https://supabase.link/youtube-multilingual-transcription-bot-feb2025-b82z)]
  * Using Remotion Lambda with Supabase [[Docs](https://supabase.link/docs-remotion-lambda-supabase-feb2025-prr4)]

_This discussion was created from the release[Developer Update - February 2025](https://github.com/supabase/supabase/releases/tag/1.25.02)._
### [Deno 2.1 Preview **local only** ](https://github.com/orgs/supabase/discussions/34054)
Mar 6, 2025
You can now try Deno 2.1 locally with Supabase CLI. The goal of local preview is to identify any regressions or missing functionality before we upgrade hosted version to Deno 2.1.
The hosted version still uses Deno 1.4+, and if you deploy functions written with Deno 2.1, some of the features may not work.
### How to try[#](https://supabase.com/changelog#how-to-try)
  * Install Deno 2.1 or newer version on your machine (<https://docs.deno.com/runtime/getting_started/installation/>)
  * Go to your Supabase project. `cd my-supabase-project`
  * Open `supabase/config.toml` and set `deno_version = 2`


`
1
[edge_runtime]
2
deno_version = 2
`
  * All your existing functions should work as before.


*To scaffold a new function as a Deno 2 project:
`
1
deno init --serve hello-world
`
  * Open `supabase/config.toml` and add the following:


`
1
[functions.hello-world]
2
entrypoint = "./functions/hello-world/main.ts"
`
  * Open supabase/functions/hello-world/main.ts and modify line 10 to:


`
1
if (url.pathname === "/hello-world") {
`
  * Use `npx supabase@beta functions serve --no-verify-jwt` to start the dev server.
  * Visit <http://localhost:54321/functions/v1/hello-world>.
  * To run built-in tests, `cd supabase/functions/hello-world; deno test`


Please give it a try and report any bugs and feedback.
### [Greatly increased Third-Party Auth MAU quota for Free and Paid Plans ](https://github.com/orgs/supabase/discussions/33959)
Mar 3, 2025
We are happy to announce that we are simplifying our pricing further by greatly increasing our [Third-Party Auth](https://supabase.com/docs/guides/auth/third-party/overview) quotas and aligning them with our regular auth quotas.
| Free Plan| Pro Plan| Team Plan  
---|---|---|---  
Before| 50 included| 50 included, then $0.00325 per MAU| 50 included, then $0.00325 per MAU  
After| 50,000 included| 100,000 included, then $0.00325 per MAU| 100,000 included, then $0.00325 per MAU  
With Third-Party Auth, Supabase allows you to use a different Auth provider alongside Supabase Auth and have an integrated experience, without being forced to adopt Supabase Auth straight away. This is especially useful if you'd like to start using Supabase with an existing project that uses a different auth provider.
This change is effective immediately.
### [Dashboard Updates [10/02/25 - 24/02/25] ](https://github.com/orgs/supabase/discussions/33835)
Feb 25, 2025
## Inline Editor (Feature Preview)[#](https://supabase.com/changelog#inline-editor-feature-preview)
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fe09b9e15-f0f3-4253-af5a-dc7ac3b64916&w=3840&q=75)
We're introducing a new inline editor that you may toggle through Feature Previews! 🙂 The inline editor can be used to run SQL wherever you are in the dashboard without taking you away from what you're doing. As usual, we'd love to hear what you think about this so please do feel free to share with us the good and (perhaps more importantly) the bad about this functionality right [here](https://github.com/orgs/supabase/discussions/33690) in our GitHub discussions! 🙏 More details and information about this is also available there 😄
PR: <https://github.com/supabase/supabase/pull/33541>
Link: <https://supabase.com/dashboard/project/_>
## Other bug fixes and improvements[#](https://supabase.com/changelog#other-bug-fixes-and-improvements)
[General](https://supabase.com/dashboard/project/_)
  * Fix Assistant's usability for local / self-host environment ([PR](https://github.com/supabase/supabase/pull/33422))


[Auth](https://supabase.com/dashboard/project/_/auth/users)
  * Add context menu support for users to copy email or delete user ([PR](https://github.com/supabase/supabase/pull/33524))
  * Add link to open user logs in the Auth logs ([PR](https://github.com/supabase/supabase/pull/33359))


[Billing](https://supabase.com/dashboard/org/_/billing)
  * Support adding additional billing email address ([PR](https://github.com/supabase/supabase/pull/33408))
  * Add Logdrain Egress to Total Egress per day usage chart ([PR](https://github.com/supabase/supabase/pull/33763))


[Edge Functions](https://supabase.com/dashboard/project/_/functions)
  * Redirect back to main page of edge functions if navigating to a slug that doesn't exist ([PR](https://github.com/supabase/supabase/pull/33479))


[Advisors](https://supabase.com/dashboard/project/_/advisors/query-performance)
  * Remove unnecessary 2dp precision for ms values in Query Performance ([PR](https://github.com/supabase/supabase/pull/33472))
  * Fix retrieving indexes in use for a selected SELECT query ([PR](https://github.com/supabase/supabase/pull/33672))


[Schema Visualizer](https://supabase.com/dashboard/project/_/database/schemas)
  * Support downloading current view as PNG ([PR](https://github.com/supabase/supabase/pull/33527))


[Storage](https://supabase.com/dashboard/project/_/storage/buckets)
  * Fix List view footer showing up top instead of the bottom, covering the first item in the list ([PR](https://github.com/supabase/supabase/pull/33598))


[Logs](https://supabase.com/dashboard/project/_/logs/edge-logs)
  * Allow users to click on a property of a selected log and add it to search ([PR](https://github.com/supabase/supabase/pull/33536))
  * Remember last visited route in the Logs section ([PR](https://github.com/supabase/supabase/pull/33486))


[Reports](https://supabase.com/dashboard/project/_/reports/database)
  * Add Supavisor connections to database reports ([PR](https://github.com/supabase/supabase/pull/33682))


### [Deploy and update Edge Functions using the Management API ](https://github.com/orgs/supabase/discussions/33720)
Feb 19, 2025
We have introduced two new API endpoints that allow you to deploy and update Edge Functions programmatically. This will be handy if you're building a [Supabase integration](https://supabase.com/partners) or want to create an internal workflow without relying on Supabase CLI.
These are the same endpoints we use internally for [Deploying Edge Functions from CLI without needing Docker](https://github.com/orgs/supabase/discussions/33613) and [writing Edge Functions using AI assistant](https://x.com/kiwicopple/status/1889031271801905543).
### Deploy an Edge Function[#](https://supabase.com/changelog#deploy-an-edge-function)
This endpoint allows you to deploy a function by providing source files and metadata in a `multipart/form-data` body. You can also provide a function `slug` as the query parameter. If an existing function for the same slug exists, it will be updated; otherwise, a new function will be created.
You can pass the `bundleOnly=1` query parameter to return the response metadata to the bundled function without persisting it. This is useful if you want to bulk update multiple functions atomically. Check the next section for the new bulk update endpoint.
API reference: <https://supabase.com/docs/reference/api/v1-deploy-a-function>
Example:
`
1
curl --request POST \
2
 --url 'https://api.supabase.com/v1/projects/project-ref/functions/deploy?slug=my-func' \
3
 --header 'Authorization: Bearer sbp_TOKEN' \
4
 --header 'content-type: multipart/form-data' \
5
 --form 'metadata={ "entrypoint_path": "index.ts", "name": "My test" }' \
6
 --form file=@file
`
After the function is created, you can immediately invoke it:
`
1
curl --request POST 'http://{project-ref}.supabase.co/functions/v1/my-func' \
2
 --header 'Authorization: Bearer SUPABASE_ANON_KEY' \
3
 --header 'Content-Type: application/json' \
4
 --data '{ "name":"Functions" }'
`
### Bulk update Edge Functions[#](https://supabase.com/changelog#bulk-update-edge-functions)
This endpoint allows you to update multiple Edge Functions atomically.
When deploying multiple edge functions, we recommend calling the deploy endpoint with the `bundleOnly=1` query parameter, collecting the responses and then calling bulk update endpoint to update them atomically.
API reference: <https://supabase.com/docs/reference/api/v1-bulk-update-functions>
### [Inline Editor Feature Preview ](https://github.com/orgs/supabase/discussions/33690)
Feb 18, 2025
## Write and run queries from anywhere in the dashboard[#](https://supabase.com/changelog#write-and-run-queries-from-anywhere-in-the-dashboard)
<https://github.com/user-attachments/assets/5951fbb2-3db7-48e5-b4fa-7c83fbad3d2d>
Today we are introducing a feature preview that gives you access to a new "inline editor". This is a SQL editor that is accessible from wherever you are in the dashboard. You can write or generate queries, run queries, view results, and save them to snippets if needed. It sits alongside other pages in the dashboard which makes it easy to reference tables, policies, functions, triggers etc while writing your queries.
As part of this preview we are also changing how you create and edit policies, triggers and functions to make use of this new inline editor. We often receive feedback around the existing UI based approach to creating policies, and our hope is that with the continued advancement of LLM's we can augment a plain SQL Editor with AI assistance vs needing a UI. The inline editor has access to an inline Assistant (press cmd + k while in editor) which will help you generate and modify queries.
**To enable the feature preview, click your profile avatar, click feature previews and enable inline editor**
## What we'd like to know from you[#](https://supabase.com/changelog#what-wed-like-to-know-from-you)
  * When you use the inline editor, please tell us what you used it for, how the experience was, and what could be improved
  * For each use case, try the inline assistant (via cmd + k) and provide feedback on the results. We want to continue to iterate on our prompts so that accuracy is as good as it can be
  * How comfortable are you using an open editor with templates and AI guidance vs the existing UI based approach for policies and functions?
  * Any other ideas or suggestions


### [Upcoming breaking change to Dashboard Navigation ](https://github.com/orgs/supabase/discussions/33670)
Feb 17, 2025
> [!NOTE] This change has now been fully rolled out - thank you everyone for the feedback! 🙏
We've made a significant proposal to enhance the Supabase Dashboard UX, ensuring that Organizations serve as the central hub for managing billing and member access. This update introduces clearer navigation between Organizations and Projects, providing a more intuitive experience for all users.
We encourage everyone to share their feedback in this discussion while we actively refine these changes.
## Quick video demo[#](https://supabase.com/changelog#quick-video-demo)
<https://github.com/user-attachments/assets/1492484b-b3f7-44c5-817c-3188689ef528>
## What’s Changed?[#](https://supabase.com/changelog#whats-changed)
### Organization[#](https://supabase.com/changelog#organization)
  * Navigation will focus on 1 Organization at a time.
  * When you are viewing an organization only the Projects for that Navigation will be visible.
  * You can switch Organization by clicking the Organization picker on the top header.


### Sidebar Updates[#](https://supabase.com/changelog#sidebar-updates)
  * Separate sidebars for Projects and Organizations.
  * The User Account Dropdown will be moved to the top right, and be always visible.


### Improved Routing & Auto-Redirects[#](https://supabase.com/changelog#improved-routing--auto-redirects)
  * You will be redirected back to your last active organization when opening the Dashboard.
  * Users without an organization will always be prompted to create one upon signup.
  * If no organization is available, you will be prompted to create an organization.


### New `/organizations` Page[#](https://supabase.com/changelog#new-organizations-page)
  * Lists all organizations owned by the user.
  * We may also support a page which shows all projects for all of your organizations.


### Account Settings[#](https://supabase.com/changelog#account-settings)
  * Account settings moved out of the organization context.


### Usage Banners & In-App Notifications[#](https://supabase.com/changelog#usage-banners--in-app-notifications)
  * Consolidated banners at the top of the dashboard.
  * Clear notifications about unpaid invoices in other organizations.
  * Notifications will be filtered per active organization.


### Self-hosting / Local[#](https://supabase.com/changelog#self-hosting--local)
  * No major changes for self-hosting or local


## Rollout[#](https://supabase.com/changelog#rollout)
  * Changes are behind a feature preview in the dashboard
  * We will roll out to the hosted platform first as incremental % rollout where users will be opted into the feature preview by default
  * If you might want _opt out of the changes_ , you may disable the changes via the feature previews which you can access through the user dropdown in the header here: ![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fd260da81-6d28-4ac7-9d07-4a898e4d840b&w=3840&q=75)


## Feedback[#](https://supabase.com/changelog#feedback)
Please feel free to leave feedback in this thread.
### [Deploy Edge Functions from CLI without needing Docker + import files outside of supabase directory ](https://github.com/orgs/supabase/discussions/33613)
Feb 13, 2025
We've introduced an experimental flag to the Supabase CLI, which allows you to deploy Edge Functions without running Docker.
### How to use[#](https://supabase.com/changelog#how-to-use)
`
1
npx supabase@beta functions deploy --use-api
`
This also simplifies importing files outside the `supabase/` directory within Edge Functions. Useful for monorepo setups where you want to share code between your frontend and Edge Functions.
For example, Given the directory layout below, you can import `my-lib` from either `index.ts` or `deno.json`.
`
1
my-repo/
2
├─ my-app/
3
│ ├─ supabase/
4
│ │ │ functions/
5
│ │ │ │ slug/
6
│ │ │ │ ├─ index.ts
7
│ │ │ │ ├─ deno.json
8
├─ my-lib/
9
│ ├─ src/
10
│ │ ├─ index.ts
11
├─ README.md
`
The new flag is available from the Supabase CLI beta releases [2.13.3](https://github.com/supabase/cli/releases/tag/v2.13.3). Please check [CLI upgrade guide](https://supabase.com/docs/guides/local-development/cli/getting-started?queryGroups=platform&platform=linux#updating-the-supabase-cli) on how to use the beta releases on your machine.
### CI[#](https://supabase.com/changelog#ci)
We also recommend using the `--use-api` flag if you [deploy Edge Functions via CI](https://supabase.com/docs/guides/functions/cicd-workflow). This should speed up the deploys as it no longer requires Docker and also solves a race condition previously occurred when deploying multiple functions in parallel.
Here's an example GitHub Action config:
`
1
name: Deploy Function
23
on:
4
 push:
5
  branches:
6
   - main
7
 workflow_dispatch:
89
jobs:
10
 deploy:
11
  runs-on: ubuntu-latest
1213
  env:
14
   SUPABASE_ACCESS_TOKEN: ${{ secrets.SUPABASE_ACCESS_TOKEN }}
15
   PROJECT_ID: your-project-id
1617
  steps:
18
   - uses: actions/checkout@v3
1920
   - uses: supabase/setup-cli@v1
21
    with:
22
     version: 2.13.3
2324
   - run: supabase functions deploy --use-api --project-ref $PROJECT_ID
`
**Note** : If you run into any issues with the `--use-api`, you can drop the flag to use the default Docker-based deploy mechanism.
**Note 2** : To run/ test Edge Functions locally (`supabase functions serve`), you will still need Docker. This only modifies deploy behavior.
### [Dashboard Updates [27/01/25 - 10/02/25] ](https://github.com/orgs/supabase/discussions/33511)
Feb 11, 2025
## Deploy Edge Functions via the Assistant[#](https://supabase.com/changelog#deploy-edge-functions-via-the-assistant)
<https://github.com/user-attachments/assets/c567ecc2-8eed-4589-b077-f578ceaeb562>
You can now get help with writing edge functions using the Assistant, and also deploy the suggested edge functions right from the dashboard! This is just the first step towards providing a convenient way to manage your edge functions through the dashboard instead of using solely through the CLI, so watch this space! 👀 🙂
PR: <https://github.com/supabase/supabase/pull/33293>
Link: <https://supabase.com/dashboard/project/_>
## Update to Authentication settings location in the dashboard[#](https://supabase.com/changelog#update-to-authentication-settings-location-in-the-dashboard)
![image](https://github.com/user-attachments/assets/f946a195-3ad7-44fd-97d6-cbb7ea943d5a)
All authentication settings are now consolidated into in one place, which is within the Auth section of the dashboard. They were previously split between project settings and the authentication product page which created confusion and potentially hid functionalities that a user might be looking for. We'll eventually also follow up with similar efforts for other product settings to improve the general information architecture of the dashboard, in hopes to help make finding your way around the dashboard better! 😄🙏
PR: <https://github.com/supabase/supabase/pull/33335>
Link: <https://supabase.com/dashboard/project/_/auth/users>
## Table Editor peek referencing row from the table[#](https://supabase.com/changelog#table-editor-peek-referencing-row-from-the-table)
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fa2abdd42-6d15-430f-9d05-2463cf04dfa9&w=3840&q=75)
Clicking "View reference row" from the Table Editor now shows the row in a Popover rather than opening the referencing table with the relevant filters applied. This is in hopes to make the UX less intrusive and abrupt - and we'd love to hear what you think! Feel free to leave any feedback either through the dashboard or right here in the discussions 🙂
PR: <https://github.com/supabase/supabase/pull/33141>
Link: <https://supabase.com/dashboard/project/_/editor>
## Easy way to Fix "Security Definer view" warnings[#](https://supabase.com/changelog#easy-way-to-fix-security-definer-view-warnings)
![screenshot-2025-02-05-at-13 04 15](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F9099c12a-c59b-45e3-914b-f5755dd45a39&w=3840&q=75)
Views that were created in the public schema without specifying security invoker will normally have a warning in the Table Editor regarding its accessibility via the project's API. Understandably, the solution to address this might not be intuitive, especially if you're not familiar with Postgres. As such, we've added a convenient action to automatically address this warning by applying the necessary fixes.
PR: <https://github.com/supabase/supabase/pull/33363>
Link: <https://supabase.com/dashboard/project/_/editor>
## Other bug fixes and improvements[#](https://supabase.com/changelog#other-bug-fixes-and-improvements)
[Table Editor](https://supabase.com/dashboard/project/_/editor)
  * Changing schemas will render the table editor empty state instead of persisting the currently viewed table to prevent confusion ([PR](https://github.com/supabase/supabase/pull/33122))
  * Add support for `bytea` data type ([PR](https://github.com/supabase/supabase/pull/33312))


[SQL Editor](https://supabase.com/dashboard/project/_/sql/new)
  * Each section's (Shared, Favorites, Private) opened/closed state now persists from where you left off ([PR](https://github.com/supabase/supabase/pull/33112))
  * Support duplicating a query ([PR](https://github.com/supabase/supabase/pull/33113))
  * Fix inability to scroll results section when query returns an error with a long message ([PR](https://github.com/supabase/supabase/pull/33277))
  * Opt to not clear search results when clicking on a query while searching ([PR](https://github.com/supabase/supabase/pull/33351))
  * Fix moving query to new folder ([PR](https://github.com/supabase/supabase/pull/33411))


[Database](https://supabase.com/dashboard/project/_/database/tables)
  * Fix database tables not showing foreign key relations when opening Edit Table panel for the first time ([PR](https://github.com/supabase/supabase/pull/33256))


[Reports](https://supabase.com/dashboard/project/_/reports)
  * Add refresh button to Custom reports, API report, Storage report and Database report ([PR](https://github.com/supabase/supabase/pull/33211))


[Webhooks](http://supabase.com/dashboard/project/_/integrations/webhooks/overview)
  * Fix issue with saving values with quotes in http parameters and headers ([PR](https://github.com/supabase/supabase/pull/33155))


[Cron](http://supabase.com/dashboard/project/_/integrations/cron/overview)
  * Support single quotes in cron job names ([PR](https://github.com/supabase/supabase/pull/33219))


[Advisors](https://supabase.com/dashboard/project/_/advisors/query-performance)
  * Support resetting query performance report on read replicas ([PR](https://github.com/supabase/supabase/pull/33346))


[Logs & Analytics](https://supabase.com/dashboard/project/_/logs/edge-logs)
  * Support navigating logs in the table with arrow keys ([PR](https://github.com/supabase/supabase/pull/33391))


### [Developer Update - January 2025 ](https://github.com/orgs/supabase/discussions/33416)
Feb 7, 2025
Here’s everything that happened with Supabase in the last month:
## Third-party Auth with Firebase is now GA[#](https://supabase.com/changelog#third-party-auth-with-firebase-is-now-ga)
![third-party-auth-with-firebase-is-ga](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F75e887ef-9fe1-43c7-b91f-38c70ab6bfcc&w=3840&q=75) Use Firebase Auth with your Supabase projects. [[Docs](https://supabase.link/docs-third-party-auth-ga-jan2025)]
## Easier to see errors in log charts[#](https://supabase.com/changelog#easier-to-see-errors-in-log-charts)
![easier-errors-in-logs](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F9aa50bbc-6888-4155-8635-fa8daddac94d&w=3840&q=75) Log charts in Supabase are now stacked with successes and errors on top of each other, and colored by type. [[Link](https://supabase.link/link-easier-errors-logs-jan2025)] [[GitHub](https://supabase.link/github-easier-errors-logs-jan2025)]
## Enhanced type inference for JSON fields[#](https://supabase.com/changelog#enhanced-type-inference-for-json-fields)
![enhanced-type-inference-for-json-fields](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F23c78985-1239-4872-b6a5-3fe602341a6e&w=3840&q=75) Set up custom types with `supabase-js` for more concise and accurate types that reflect your data. [[GitHub](https://supabase.link/github-enhanced-json-types-jan2025)]
## Type validation for query filter values[#](https://supabase.com/changelog#type-validation-for-query-filter-values)
![type-validation-for-query-filter-values](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fec627922-c456-40ee-a67d-6fca39057c0b&w=3840&q=75) The Supabase TypeScript SDK will correctly validate all query filter values in `eq`, `neq`, and `in` methods. [[GitHub](https://supabase.link/github-type-validation-query-jan2025)] [[Docs](https://supabase.link/docs-type-validation-query-jan2025)]
## AI Prompt for writing Edge Functions[#](https://supabase.com/changelog#ai-prompt-for-writing-edge-functions)
![ai-prompt-for-writing-edge-functions](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fae3cbd6d-a641-4ded-8664-3a418f8c55c1&w=3840&q=75) A prompt to help generate Supabase Edge Functions following best practices that you can supply to Cursor, Copilot, and other AI coding tools. [[Docs](https://supabase.link/docs-ai-prompt-edge-functions-jan2025)]
## Quick Product Announcements[#](https://supabase.com/changelog#quick-product-announcements)
  * Free plans are now limited to 0.5GB _per project_ instead of 0.5GB per account. Keep building! [[GitHub](https://supabase.link/github-free-plans-limited-jan2025)]
  * Now you can top up your credit balance through your [organization's billing settings](https://supabase.com/dashboard/org/_/billing). [[GitHub](https://supabase.link/github-top-up-credit-balance-jan2025)]
  * Added 3 configurable parameters to control disk autoscaling. [[GitHub](https://supabase.link/github-disk-autoscaling-parameters-jan2025)]
  * Easier to find queries in the SQL Editor. [[GitHub](https://supabase.link/github-easier-sql-queries-jan2025)]

_This discussion was created from the release[Developer Update - January 2025](https://github.com/supabase/supabase/releases/tag/1.25.01)._
### [Deprecation of Fly.io Postgres Managed by Supabase on April 11, 2025 ](https://github.com/orgs/supabase/discussions/33413)
Feb 7, 2025
Supabase is deprecating [Fly’s Postgres offering managed by Supabase](https://supabase.link/fly-pg-blog) on April 11, 2025.
### Why are we deprecating this offering?[#](https://supabase.com/changelog#why-are-we-deprecating-this-offering)
This deprecation enables us to focus on a new architecture for scale-to-zero databases, zero-downtime upgrades (more on this later), and more. Afterward, we’ll re-evaluate multi-cloud deployments beyond AWS, our current cloud provider.
### What’s the current status of Fly Postgres on Supabase?[#](https://supabase.com/changelog#whats-the-current-status-of-fly-postgres-on-supabase)
We have disabled Fly Postgres signups and existing Fly Postgres customers will no longer be able to spin up new projects on Supabase. However, you can still access any existing Fly Postgres database.
### What is the deprecation timeline?[#](https://supabase.com/changelog#what-is-the-deprecation-timeline)
Before April 11:
You will still be able to access your existing Fly Postgres projects. We strongly recommend that you [transition to Supabase’s](https://supabase.link/fly-pg-to-supa) or Fly’s native Postgres offering as soon as possible.
On April 11:
Your Fly Postgres projects are removed from our platform.
Reach out to [our support](https://supabase.link/fly-pg-support) if you have any questions or concerns regarding this deprecation.
### [Dashboard Updates [13/01/25 - 27/01/25] ](https://github.com/orgs/supabase/discussions/33144)
Jan 28, 2025
## Log charts now show stacked charts with total warnings and errors[#](https://supabase.com/changelog#log-charts-now-show-stacked-charts-with-total-warnings-and-errors)
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fd2b918ec-2403-414d-a0f6-0bfe2cacbf21&w=3840&q=75)
With stacked charts, you should now be able to get a better, faster glance at your logs' status, and also identify potential issues with incoming requests easily!
Link: <https://supabase.com/dashboard/project/_/logs/edge-logs>
PR: <https://github.com/supabase/supabase/pull/32742>
## Additional parameters added to Disk Settings[#](https://supabase.com/changelog#additional-parameters-added-to-disk-settings)
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fac47c400-a1d4-44c2-95dc-1df9d5c46be0&w=3840&q=75)
3 new configurable parameters have been added that can control the autoscale behaviour of your disk, namely:
  * Autoscale growth percent: Refers to the percentage of current disk size to grow by
  * Minimum increment: Refers to the minimum value to grow the disk size by when autoscaling
  * Maximum disk size: Refers to the maximum size that your disk can grow to


These parameters can be configured anytime with no cooldown, and can be accessed under "Advanced disk settings" in your project settings "Compute and Disk"
Link: <https://supabase.com/dashboard/project/_/settings/compute-and-disk>
PR: <https://github.com/supabase/supabase/pull/32628>
## SQL Editor searching now renders a flat list[#](https://supabase.com/changelog#sql-editor-searching-now-renders-a-flat-list)
<https://github.com/user-attachments/assets/3cd07693-882d-486b-b848-842d67d0316a>
This addresses a UX problem whereby searching for snippets do not immediately surface results that might be within folders - with rendering a flat list instead, this should enable users to find what they need faster. Results are also no longer separated into "Shared", "Favorites", or "Private to make scanning through results easier.
Link: <https://supabase.com/dashboard/project/_/sql/new>
PR: <https://github.com/supabase/supabase/pull/33064>
## Bug fixes and other improvements[#](https://supabase.com/changelog#bug-fixes-and-other-improvements)
[General](https://supabase.com/dashboard)
  * More mobile responsiveness improvements ([PR](https://github.com/supabase/supabase/pull/32630))


[Advisors](https://supabase.com/dashboard/project/_/advisors/query-performance)
  * Show timing in seconds instead of ms if > 1000 ms ([PR](https://github.com/supabase/supabase/pull/32747))
  * Allow exporting advisor results to CSV, or copy as JSON / Markdown


[Cron](https://supabase.com/dashboard/project/_/integrations/cron/overview)
  * Show all cron jobs even those with no names ([PR](https://github.com/supabase/supabase/pull/32765))
  * Any changes made using the UI will reflect in the SQL snippet textbox to support further customization ([PR](https://github.com/supabase/supabase/pull/32767))


[Table Editor](https://supabase.com/dashboard/project/_/editor)
  * Fix a bug with Set to NOW CTA that was specifically happening only in certain timezones ([PR](https://github.com/supabase/supabase/pull/32749))


[SQL Editor](https://supabase.com/dashboard/project/_sql/new)
  * Fix X axis labels with charting in SQL Editor ([PR](https://github.com/supabase/supabase/pull/32769))
  * Fix client crash issue when using a non-numerical column as the Y axis ([PR](https://github.com/supabase/supabase/pull/32795))
  * Opened / closed state of each section is now persisted ([PR](https://github.com/supabase/supabase/pull/33112))
  * Support duplicating a query ([PR](https://github.com/supabase/supabase/pull/33113))


### [Relaxing Database Size limit on Free Plan - 0.5 GB Database Size per project ](https://github.com/orgs/supabase/discussions/33121)
Jan 27, 2025
> [!NOTE] This is only relevant for Free Plan customers.
We've relaxed the Database Size limit on the Free Plan to be 0.5 GB per active project, rather than 0.5 GB for your entire Free Plan organization (previously included paused/deleted projects within your billing cycle). This will be beneficial in a few cases:
  * When pausing or deleting projects, they will no longer count towards the Free Plan limit.
  * When launching more than one project on the Free Plan, each project is allowed 0.5 GB Database Size, rather than a total of 0.5 GB (i.e. two projects using 0.25 GB).


**Before** Every project that has been active at some point in your billing cycle counts towards the 0.5 GB Database Size limit. If you've deleted a project, the average Database Size will still count towards your limit. We sum up the average Database Size of all projects that are/have been active in the billing cycle. Two projects with 0.5 GB Database Size each equal a Database Size usage of 1 GB and therefore exceed the Free Plan quota.
**After** We only limit active projects to a Database Size of 0.5 GB per project. Deleted or paused projects, even within the billing cycle, do not count towards your Database Size limits. As long as none of your active projects exceeds 0.5 GB Database Size, you'll stay within the Free Plan limits. Two projects with 0.5 GB Database Size each would still be within the Free Plan quota, as no project is exceeding 0.5 GB.
### [Developer Update - December 2024 ](https://github.com/orgs/supabase/discussions/33035)
Jan 23, 2025
Welcome to 2025. Here’s everything that happened with Supabase in the last month:
## Supabase Integrations Page[#](https://supabase.com/changelog#supabase-integrations-page)
![supabase-integrations-page](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F67a3aecf-6c07-49df-b129-9f7a158fdb28&w=3840&q=75)
We added an Integrations Section to the Dashboard. Inside you’ll find useful features, like our new Postgres modules: Cron Jobs and Queues.
[[Changelog](https://supabase.link/changelog-supabase-integrations-features-dec2024)]
## Fix Security and Performance Issues with AI[#](https://supabase.com/changelog#fix-security-and-performance-issues-with-ai)
![fix-security-and-performance-Issues-with-ai](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F571661f9-e53f-4049-abfa-a3f1fcf44677&w=3840&q=75)
The AI Assistant has a new ability: it can help you understand and resolve Security and Performance issues. The issue context is passed to the assistant, which explains the issue and suggests fixes.
[[Check out the Security Advisor](https://supabase.link/checkoutthesecurityadvisor-fix-security-performance-dec2024)]
## SQL Editor Inline AI Assistance[#](https://supabase.com/changelog#sql-editor-inline-ai-assistance)
![sql-editor-inline-ai-assistance](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F105afd59-a349-47da-a4c1-f57238add18b&w=3840&q=75)
When using the SQL Editor, you can now hit CMD+K to open an inline AI assistant that will help you make changes to your query. It will only make changes to whatever you have selected, but also has the surrounding context and can access schema, policy, and function information, if needed.
[[Check out the SQL Editor](https://supabase.link/checkoutthesqleditor-sql-editor-ai-assistant-dec2024)]
## Supabase Branching Available in Vercel Integration[#](https://supabase.com/changelog#supabase-branching-available-in-vercel-integration)
![supabase-branching-available-in-vercel-integration](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F8ac12b38-415b-424c-a910-10f65259776d&w=3840&q=75)
Vercel Branching Integration now works with Vercel Marketplace managed projects. You can synchronize environment variables for newly created branches to your Vercel projects, no matter whether the project was created directly in Supabase or through a Vercel dashboard.
[[Changelog](https://supabase.link/changelog-supabase-vercel-branching-dec2024)]
## Database Connection Settings Redesigned[#](https://supabase.com/changelog#database-connection-settings-redesigned)
![database-connection-settings-redesigned](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fdfbea9d4-8c61-4e13-bb5e-9c64ab1dcbfe&w=3840&q=75)
The “Connect” dialog has moved to the top of the [Dashboard](https://supabase.link/dashboard-database-connection-settings-dec2024). You can access your database connection settings from anywhere. The “Connection String” tab includes guidance on when to connect via direct connection, transaction pooler, and session pooler.
[[Dashboard](https://supabase.link/dashboard-database-connection-settings-dec2024)]
## Query Cloudflare D1 from Your Supabase Database[#](https://supabase.com/changelog#query-cloudflare-d1-from-your-supabase-database)
![query-cloudflare-d1-from-your-supabase-database](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fde48d24c-56e3-4233-9981-4bdfdd6d7c99&w=3840&q=75)
Cloudflare D1 is a serverless SQLite service. You can now query it from your Supabase database using our Wrappers service, along with other services like BigQuery, ClickHouse, Firebase, and Snowflake.
[[Docs](https://supabase.link/docs-cloudflare-d1-supabase-dec2024)]
## Quick Product Announcements[#](https://supabase.com/changelog#quick-product-announcements)
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F0dc568a3-cb5c-428f-9aa4-baa0d87f0147&w=3840&q=75)
**Dashboard**
  * The Supabase Dashboard is now responsive. This is just a first step towards a more complete mobile experience. [[Link](https://supabase.link/link-supabase-dashboard-responsive-dec2024)]
  * Granular Disk Size usage break down by Database/WAL/System [[Changelog](https://supabase.link/changelog-disk-size-breakdown-dec2024)]


**Edge Functions**
  * Use a custom NPM registry for Edge Function dependencies [[Changelog](https://supabase.link/changelog-custom-npm-registry-dec2024)]


**Logs**
  * Log Explorer UI Overhaul [[Changelog](https://supabase.link/changelog-log-explorer-ui-dec2024)]


**Connection Pooler**
  * Supavisor Session Mode on port 6543 will be deprecated on February 28, 2025 [[Changelog](https://supabase.link/changelog-supavisor-deprecation-2025-dec2024)]


**Auth**
  * Slack v1 OAuth has been deprecated in favor of Slack (OIDC) [[Changelog](https://supabase.link/changelog-slack-oauth-deprecated-dec2024)]

_This discussion was created from the release[Developer Update - December 2024](https://github.com/supabase/supabase/releases/tag/1.24.12)._
### [Enhanced Type Inference for JSON Fields in supabase-js ](https://github.com/orgs/supabase/discussions/32925)
Jan 19, 2025
TypeScript users, here's a cool new feature! Starting from [v2.48.0](https://github.com/supabase/supabase-js/releases/tag/v2.48.0), defining custom types for JSON fields in `supabase-js` and using them with the JSON selector is now easier, making your code more type-safe and intuitive.
### Quick Example[#](https://supabase.com/changelog#quick-example)
Define your custom JSON type:
`
1
type CustomJsonType = {
2
 foo: string;
3
 bar: { baz: number };
4
 en: 'ONE' | 'TWO' | 'THREE';
5
};
67
export type Database = MergeDeep<
8
 DatabaseGenerated,
9
 {
10
  your_schema: {
11
   Tables: {
12
    your_table: {
13
     Row: {
14
      data: CustomJsonType | null;
15
     };
16
     // Optional: Use if you want type-checking for inserts and update
17
     // Insert: {
18
     // data?: CustomJsonType | null;
19
     // };
20
     // Update: {
21
     // data?: CustomJsonType | null;
22
     // };
23
    }
24
   }
25
   Views: {
26
    your_view: {
27
     Row: {
28
      data: CustomJsonType | null;
29
     };
30
    }
31
   }
32
  }
33
 }
34
>
`
### What You Get[#](https://supabase.com/changelog#what-you-get)
Now, when you query your data:
`
1
const res = await client
2
 .from('your_table')
3
 .select('data->bar->baz, data->en, data->bar');
45
if (res.data) {
6
 console.log(res.data);
7
 // TypeScript infers the shape of your JSON data:
8
 // [
9
 //  {
10
 //   baz: number;
11
 //   en: 'ONE' | 'TWO' | 'THREE';
12
 //   bar: { baz: number };
13
 //  }
14
 // ]
15
}
`
### Get Started[#](https://supabase.com/changelog#get-started)
Start using this feature with our guides:
  * [Generating Types](https://supabase.com/docs/guides/api/rest/generating-types)
  * [Typescript Support](https://supabase.com/docs/reference/javascript/typescript-support)
  * [Helper Types for Tables and Joins](https://supabase.com/docs/reference/javascript/select#helper-types-for-tables-and-joins)


### [Add static files to Edge Functions ](https://github.com/orgs/supabase/discussions/32815)
Jan 15, 2025
Supabase CLI 2.7.0 adds support for bundling Edge Functions with static files.
You can access bundled files via Deno's file-system APIs. Here's an example function that serves a PDF file.
`
1
import fs from 'node:fs'; // This should be the first import to prevent other modules to trying to use their own polyfills.
234
Deno.serve(async () => {
5
 return new Response(
6
  await Deno.readFile("./my-book.pdf"),
7
  {
8
   headers: {
9
    "Content-Type": "application/pdf",
10
    "Content-Disposition": 'attachment; filename="my-book.pdf"',
11
   },
12
  },
13
 );
14
});
`
### Use cases[#](https://supabase.com/changelog#use-cases)
  * Use custom Wasm modules in your Edge Functions ([check this guide](https://supabase.com/docs/guides/functions/wasm) for more details on how to write & use wasm modules in Edge Functions)
  * Create paywalls for serving digital content like ebooks
  * HTML email templates for sending emails using Edge Functions


### How to configure[#](https://supabase.com/changelog#how-to-configure)
You will need to add static files to the function's directory to bundle them. Then, in the `supabase/config.toml` file for the project, add these lines:
`
1
[functions.buy-book]
2
static_files = [ "./functions/buy-book/my-book.pdf" ]
`
You can specify an array of files or use a glob pattern (eg: "./functions/email-templates/*.html")
Check the CLI configuration reference for more details: <https://supabase.com/docs/guides/local-development/cli/config#functions.function_name.static_files>
**Note** : This feature is currently not available with branching and will be added with the next stable release of the CLI.
### [Supabase Connection Pooler Deprecating Session Mode on Port 6543 on February 28, 2025 ](https://github.com/orgs/supabase/discussions/32755)
Jan 13, 2025
 _If you're only using Transaction Mode on Connection Pooler port 6543 or already using Session Mode on port 5432 then no action is required._
On February 28, 2025, Supavisor (Supabase's Connection Pooler) is deprecating Session Mode on port 6543. After this date, port 6543 will only support Transaction Mode while port 5432 continues to support Session Mode.
We’re making this change because Session Mode is already available on port 5432 and this streamlines our connection pooler’s ports and their respective modes.
Required steps:
  1. Update your application/database clients to use port 5432 for Session Mode.
  2. In your project’s [Database Settings](https://supabase.com/dashboard/project/_/settings/database) (”Connection pooling configuration”), set “Pool Mode” to “Transaction” and click “Save” (please keep in mind that this will restart all your connections connected to the Pooler).


Please reach out to [our support](https://supabase.com/dashboard/support/new) if you have any questions or concerns regarding this change.
### [Dashboard Updates [30/12/24 - 13/01/25] ](https://github.com/orgs/supabase/discussions/32741)
Jan 13, 2025
## UI Overhaul for Log Explorer log details[#](https://supabase.com/changelog#ui-overhaul-for-log-explorer-log-details)
<https://github.com/user-attachments/assets/1f752ebc-a814-4f1c-845f-4659a0dc87d3>
The changes here addresses some UX friction whereby depending on the query, the detail panel of the log would be hard to read. We've hence updated the log detail drawing to add better spacing, the option to expand rows, and also use our TimestampInfo tooltip in the UI as well!
PR: <https://github.com/supabase/supabase/pull/31684>
Link: <https://supabase.com/dashboard/project/_/logs/explorer>
## Toggle for enabling connection via S3 protocol in Storage[#](https://supabase.com/changelog#toggle-for-enabling-connection-via-s3-protocol-in-storage)
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fe621ad00-86e1-4d90-95bc-1b00f548657e&w=3840&q=75)
PR: <https://github.com/supabase/supabase/pull/31209>
Link: <https://supabase.com/dashboard/project/_/settings/storage>
## Credit Balance Top Up[#](https://supabase.com/changelog#credit-balance-top-up)
![Screenshot 2025-01-13 at 14 43 06](https://github.com/user-attachments/assets/3c8c5190-0b25-4524-9ee8-1d9cc3a4a2d4)
It is now possible to top up your credit balance through your organization's billing settings. Read more about this in our [discussions page here](https://github.com/orgs/supabase/discussions/32735)
PR: <https://github.com/supabase/supabase/pull/32680>
Link: <https://supabase.green/dashboard/org/_/billing>
## Other bug fixes and improvements[#](https://supabase.com/changelog#other-bug-fixes-and-improvements)
[Auth](https://supabase.com/dashboard/project/_/auth/users)
  * Fix impersonation and searching users with single quotes ([PR](https://github.com/supabase/supabase/pull/32603))


[Advisors](https://supabase.com/dashboard/project/_/advisors/security)
  * Add "Ask Assistant" CTA to advisor issues ([PR](https://github.com/supabase/supabase/pull/32665))


[SQL Editor](https://supabase.com/dashboard/project/_/sql/new)
  * Persist last selected database ([PR](https://github.com/supabase/supabase/pull/32598))


[Logs Explorer](https://supabase.com/dashboard/project/_/logs/explorer)
  * Add copy as CSV + JSON options ([PR](https://github.com/supabase/supabase/pull/31625))


[Edge Functions](https://supabase.com/dashboard/project/_/functions)
  * A number of general improvements (more details in the PR) ([PR](https://github.com/supabase/supabase/pull/31317))


[Cron](https://supabase.com/dashboard/project/_/integrations/cron/jobs)
  * Add last and next run for cron jobs ([PR](https://github.com/supabase/supabase/pull/31305))


### [Credit Balance Top Up ](https://github.com/orgs/supabase/discussions/32735)
Jan 13, 2025
It is now possible to top up your credit balance through your [organization's billing settings](https://supabase.com/dashboard/org/_/billing). On successful payment, an invoice will be issued and you'll be granted credits. Credits will be applied to future invoices only and are not refundable. The topped up credits do not expire.
![Screenshot 2025-01-13 at 14 43 06](https://github.com/user-attachments/assets/3c8c5190-0b25-4524-9ee8-1d9cc3a4a2d4) ![Screenshot 2025-01-13 at 14 47 01](https://github.com/user-attachments/assets/a8cec5dd-0ea4-467a-afa4-d3dfd15f74e8)
This can be useful in many scenarios:
  * Issues with recurring payments (i.e. due to Indian banking regulations)
  * More control about how often your credit card gets charged
  * Easier for some accounting departments
  * Yearly upfront payments


If you run out of credits while you are still on a paid plan, your credit card will be charged as usual.
If you are interested in larger (>$1,000) credit packages, please [reach out](https://supabase.com/dashboard/support/new?subject=I%20would%20like%20to%20inquire%20about%20larger%20credit%20packages&category=Billing).
### [Type validation for query filter values in supabase-js ](https://github.com/orgs/supabase/discussions/32677)
Jan 9, 2025
If you are using our TypeScript SDK with automatically generated types, you are in for a treat. Starting version `2.47.12`, our `@supabase/supabase-js` SDK will correctly validate all query filter values in `eq`, `neq` and `in` methods. Including not only primitives, but enums as well. In both tables, views, and arbitrarily-nested relations.
When using enums, LSP auto-completion also works out-of-the-box now.
![Untitled](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F98543258-394f-45aa-8a36-bc3b547b1d07&w=3840&q=75)
Want to start using them? See our guides for how to get started: <https://supabase.com/docs/guides/api/rest/generating-types> <https://supabase.com/docs/reference/javascript/typescript-support>
### [Use a custom NPM registry for Edge Function dependencies ](https://github.com/orgs/supabase/discussions/32635)
Jan 7, 2025
Some organizations require using all modules from a private NPM registry for security and compliance reasons. Edge Functions now supports configuring a private registry to load all NPM modules using the `NPM_CONFIG_REGISTRY` environment variable.
You can define a private registry in the project's `.env` file or directly specify it when running the deploy command:
`
1
NPM_CONFIG_REGISTRY=https://custom-registry/ supabase functions deploy my-function
`
You will need Supabase CLI version 2.2.8 or higher to use this feature.
Note that Edge Functions also supports [importing private NPM packages](https://supabase.com/docs/guides/functions/import-maps#importing-from-private-registries) (which can be published on any registry).
Check the [Managing dependencies](https://supabase.com/docs/guides/functions/import-maps#using-a-custom-npm-registry) guide to learn more about how to configure and use external dependencies in your Edge Functions.
### [Dashboard Updates [09/12/24 - 23/12/24] ](https://github.com/orgs/supabase/discussions/31318)
Dec 23, 2024
## Improved mobile navigation for the dashboard[#](https://supabase.com/changelog#improved-mobile-navigation-for-the-dashboard)
<https://github.com/user-attachments/assets/a2e1c815-6d65-486f-ae77-1d5993377c40>
We've heard many feedback around mobile support for the dashboard and we're taking the first step towards supporting that 📱🙂 While this PR doesn't completely optimize the mobile UX for the dashboard, navigating around the dashboard on mobile is now supported! We'll definitely be looking into optimizing other parts of the dashboard for mobile use so stay tuned! 😉
PR: <https://github.com/supabase/supabase/pull/31080>
Link: <https://supabase.com/dashboard>
## Inline completions via Assistant in SQL Editor[#](https://supabase.com/changelog#inline-completions-via-assistant-in-sql-editor)
![image](https://github.com/user-attachments/assets/e24c9910-7044-482d-91af-b46111ff34e2)
In hopes to make the Assistant's UX more seamless while in the SQL editor, we've added support for adjusting your SQL snippets inline while in the SQL editor without having to open the Assistant panel. Highlight the section that you'd like to edit, and hit CMD / CTRL + K to pop open the inline prompt 💬 Less clicking, more typing!
PR: <https://github.com/supabase/supabase/pull/30706>
Link: <https://supabase.com/dashboard/project/_/sql/new>
## Improve date time editing in Table Editor Grid[#](https://supabase.com/changelog#improve-date-time-editing-in-table-editor-grid)
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F948e6ae7-e2af-4483-8172-fc12fa675589&w=3840&q=75)
We've also seen a couple of feedback around supporting copying and pasting raw date time values from the Table Editor. We've previously been using the browser native date time input field which we've realised have been less than optimal for the following reasons:
  * Adjusting the value typically takes several clicks which can feel frustrating
  * The precision of time values in JS does not match the precision of time values in Postgres
  * The UX varies a lot across browsers since each browser has their own implementation of the native date time input


As such we've decided to move towards supporting editing your raw values for date, timestamp, and timestamptz type fields, with a helper tooltip to show the time formatted in UTC and your relative timezone. This UX also allows us to support setting values to NULL which we struggled to do so gracefully with native browser date time inputs. Hope this helps make editing your data via the Table Editor easier 🙏🙂 More screenshots available in the attached PR below!
PR: <https://github.com/supabase/supabase/pull/31121>
Link: <https://supabase.com/dashboard/project/_/editor>
## Support for bulk delete users[#](https://supabase.com/changelog#support-for-bulk-delete-users)
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fe3bffd2e-6cae-49dd-a73f-05397ce159b1&w=3840&q=75)
Also another feature that we've heard many requests for - you can now delete your users in bulk! Select the users that you'd like via the checkboxes and a button will appear to allow you to delete them all. There is, however, a temporary limitation that you may only delete up to 20 users at once, but we'll be looking into lifting this limitation eventually 🙂
PR: <https://github.com/supabase/supabase/pull/31271>
Link: <https://supabase.com/dashboard/project/_/auth/users>
## Other bug fixes and improvements[#](https://supabase.com/changelog#other-bug-fixes-and-improvements)
[General](https://supabase.com/dashboard/project/_)
  * Add ability for Assistant to retrieve database functions within a schema ([PR](https://github.com/supabase/supabase/pull/31015))
  * Limit local storage memory to 20 chat messages for Assistant ([PR](https://github.com/supabase/supabase/pull/31015))
  * Support scrolling up in chat while a new response is being streamed ([PR](https://github.com/supabase/supabase/pull/31042))
  * Adjust warnings for destructive prompts via the Assistant ([PR](https://github.com/supabase/supabase/pull/31042))
  * Assistant to adhere to Supabase Linter rules when generating responses ([PR](https://github.com/supabase/supabase/pull/31113))


[Table Editor](https://supabase.com/dashboard/project/_/editor)
  * Add dropdown menu item to copy table name ([PR](https://github.com/supabase/supabase/pull/31089))


### [Dashboard Updates [18/11/24 - 09/12/24] ](https://github.com/orgs/supabase/discussions/31041)
Dec 10, 2024
Launch Week 13 has wrapped up and it's now the holiday season! 🎄🎁 If you might have missed our launches last week - fret not! We've got you covered with a brief summary of the changes that landed in the dashboard right here 🙂
## Dashboard Integrations[#](https://supabase.com/changelog#dashboard-integrations)
![Screenshot 2024-12-10 at 18 02 54](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F65b815f4-b034-4b18-b27a-d1bbc75f0d3a&w=3840&q=75)
You should have noticed by now, but we've added a new Integrations page where you can easily manage all things related to your database that may not necessarily be directly about your database. This allows us to consolidate some features that were in slightly odd places such as the GraphiQL IDE or Database Webhooks, and also provide UIs that are specific to certain database extension(s) such as Vault, or the newly added Queues and Crons (more on that below!). Database Wrappers have also been shifted here as well, and we hope that this shift will help make finding things around the dashboard easier for everyone 🙂🙏
Link: <https://supabase.com/dashboard/project/_/integrations>
PR: <https://github.com/supabase/supabase/pull/30476>
## AI Assistant V2[#](https://supabase.com/changelog#ai-assistant-v2)
![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-1-ai-assistant-v2%2Fthumb.jpg&w=640&q=100)
We've always had the AI assistant sprinkled around the dashboard in the SQL Editor, and RLS Editor. Today we're making it accessible from anywhere in the dashboard, spiced with several new abilities to go along with 🎁 Read more about this in our blog post and learn how you can leverage the assistant to get more done, and quicker! 😄
Blog Post: <https://supabase.com/blog/supabase-ai-assistant-v2>
Link: <https://supabase.com/project/_>
PR: <https://github.com/supabase/supabase/pull/30523>
## Cron[#](https://supabase.com/changelog#cron)
![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-3-supabase-cron%2Fthumb.jpg&w=640&q=100)
Create recurring jobs to run SQL snippets, or call database functions, Supabase Edge Functions, and even remote webhooks with our new Postgres Module, Cron! Supabase Cron is built on the powerful [`pg_cron`](https://github.com/citusdata/pg_cron) extension by the team at [Citus Data](https://github.com/citusdata), and we appreciate the Citus Data for generously licensing their extension with the OSI-compatible [PostgreSQL license](https://github.com/citusdata/pg_cron?tab=PostgreSQL-1-ov-file), allowing us to [support existing tools](https://supabase.com/docs/guides/getting-started/architecture#support-existing-tools) wherever possible. 💪🏻
Blog Post: <https://supabase.com/blog/supabase-cron>
Link: <https://supabase.com/dashboard/project/_/integrations>
PR: <https://github.com/supabase/supabase/pull/29291>
## Queues[#](https://supabase.com/changelog#queues)
![](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flaunch-week-13%2Fday-4-supabase-queues%2Fthumb.png&w=640&q=100)
Process and manage asynchronous tasks with Supabase Queues! This is a Postgres-native, durable Message Queue with guaranteed delivery, improving the scalability and resiliency of your applications, and it's designed to work seamlessly with the entire Supabase platform. Similarly to Cron, Supabase Queues is built on the [`pgmq`](https://github.com/tembo-io/pgmq) extension by the team at [Tembo](https://github.com/tembo-io), and we appreciate the Tembo team for licensing their extension with OSI-compatible [PostgreSQL license](https://github.com/citusdata/pg_cron?tab=PostgreSQL-1-ov-file) as well! 🙏
Blog Post: <https://supabase.com/blog/supabase-queues>
Link: <https://supabase.com/dashboard/project/_/integrations>
PR: <https://github.com/supabase/supabase/pull/30300>
## Restore to a new project[#](https://supabase.com/changelog#restore-to-a-new-project)
You can now copy data easily from an existing Supabase project to an entirely new and independent one! This has been a well requested functionality and we're happy to share that it's finally possible to do so via the dashboard 🙂 Read more about this in our blog post, or in our documentation 🙏
Blog Post: <https://supabase.com/blog/restore-to-a-new-project>
Docs: <https://supabase.com/docs/guides/platform/backups#restore-to-a-new-project>
Link: <https://supabase.com/dashboard/project/_/database/backups/restore-to-new-project>
PR: <https://github.com/supabase/supabase/pull/30325>
## Other bug fixes and improvements[#](https://supabase.com/changelog#other-bug-fixes-and-improvements)
[Table Editor](https://supabase.com/dashboard/project/_/editor)
  * Fix rendering of OID cell types causing a client crash ([PR](https://github.com/supabase/supabase/pull/30784))


### [Slack V1 OAuth Provider Deprecated in favour of Slack (OIDC) ](https://github.com/orgs/supabase/discussions/30772)
Dec 1, 2024
Dear Users,
Slack has [deprecated their existing v1 API](https://api.slack.com/changelog/2024-04-discontinuing-new-creation-of-classic-slack-apps-and-custom-bots) and will fully sunset the API over the [next two years](https://api.slack.com/changelog/2024-09-legacy-custom-bots-classic-apps-deprecation). This means that Slack Applications using the v1 `Slack (Deprecated)` provider will stop functioning if no action is taken. In turn, Supabase Auth users using the `Slack (Deprecated)` provider will also not be able to sign in via the Slack OAuth provider if no action is taken.
![image](https://github.com/user-attachments/assets/eca053a4-72ac-4b4f-aca4-1ef97362a2ed)
We’ve introduced a new replacement OAuth provider named “Slack (OIDC)” which supports the latest Slack API and will send out an email to affected users next week with instructions on how to migrate.
To migrate your authentication system, you'll need to:
  1. [Create a new Slack Application](https://api.slack.com/quickstart) in your Slack dashboard
  2. Update your credentials in the Supabase Dashboard by switching from the deprecated `Slack (Deprecated)` provider to the new `Slack (OIDC)` provider. You can find the provider in your project under [Authentication > Providers > Slack (Deprecated)](https://supabase.com/dashboard/project/_/auth/providers)
  3. Update your code to use the new provider in all OAuth calls, like this:


`
1
const { data, error } = await supabase.auth.signInWithOAuth({
2
  provider: 'slack_oidc',
3
 })
`
  1. If you are using the Supabase CLI , you will also need to update your `config.toml` to use `[auth.external.slack_oidc]` in place of `[auth.external.slack_oidc]`. See the [local development docs](https://supabase.com/docs/guides/local-development/overview#use-auth-locally) for a detailed example.


Refer to our documentation for [further details](https://supabase.com/docs/guides/auth/social-login/auth-slack)
Further configuration of the deprecated Slack provider will not be possible past **15th Jan 2025** as we will remove `Slack` provider from the dashboard then. If you need more time to access the configuration page , reach out to us [via a support ticket](https://supabase.com/dashboard/support/new).
Slack will terminate support for Legacy bots and Classic Apps on March 31, 2025 and March 31, 2026 respectively.
Please reach out via support or on the thread if there are any questions or concerns.
### [Removal of app.settings.jwt_secret from the database ](https://github.com/orgs/supabase/discussions/30606)
Nov 22, 2024
# Introduction[#](https://supabase.com/changelog#introduction)
We are removing `app.settings.jwt_secret` from the `postgres` database on 2024/11/22.
This [setting](https://postgrest.org/en/stable/references/configuration.html#app-settings) has previously been available through our PostgREST integration, and could be accessed using `current_setting('app.settings.jwt_secret')` in SQL.
# Why are we doing this?[#](https://supabase.com/changelog#why-are-we-doing-this)
The `jwt_secret` can be used to mint new, custom JWTs and is security sensitive. Supabase limits access to the `jwt_secret` , through both the dashboard and API, to [specific roles](https://supabase.com/docs/guides/platform/access-control#api-config-permissions) (owner, admin and developer). Allowing access to this setting directly in the database can allow bypassing of these restrictions.
# What do you need to do?[#](https://supabase.com/changelog#what-do-you-need-to-do)
If you need the `jwt_secret`, it can be retrieved through the Supabase [dashboard](https://supabase.com/dashboard/project/_/settings/api).
If you are using the `app.settings.jwt_secret` in SQL, you will need to update your function to retrieve this value from [Vault](https://supabase.com/docs/guides/database/vault).
`
1
select vault.create_secret('JWT_SECRET', 'app.jwt_secret', 'The jwt secret');
23
-- retrieve the value, this replaces select current_setting('app.settings.jwt_secret')
4
select decrypted_secret 
5
  from vault.decrypted_secrets 
6
  where name = 'app.jwt_secret';
`
Also, please consult the [changelog entry for Asymmetric Keys](https://github.com/orgs/supabase/discussions/29289) to understand the coming changes to `jwt_secret` and how keys at Supabase are changing.
### [Dashboard Updates [04/11/24 - 18/11/24] ](https://github.com/orgs/supabase/discussions/30526)
Nov 18, 2024
## Table Editor Performance Improvements[#](https://supabase.com/changelog#table-editor-performance-improvements)
We've set aside some time to look into improving the performance of the Table Editor over the past few weeks, in particular shortening both perceived and actual loading times as you navigate around the Table Editor. This all comes together in several PRs as we explored from 2 angles:
  * Optimizing the queries that are firing behind the scenes by removing redundant sections + minimise waterfall requests
  * Introducing prefetching behaviours as your mouse cursor goes through the list of tables to have the tables' contents ready by the time you open it in the UI


Performance improvements have always been a consistent topic with the team, and we don't intend to stop here! Hopefully these changes will make it smoother and faster for you to build your project with the dashboard and as always let us know any feedback! 🙂🙏 Just a button away in the top right corner of the dashboard to get your thoughts heard 😄
PRs:
  * Query optimizations Part 1: <https://github.com/supabase/supabase/pull/30184>
  * Query optimizations Part 2: <https://github.com/supabase/supabase/pull/30295>
  * Prefetching on the table editor: <https://github.com/supabase/supabase/pull/29987>
  * Prefetching on the home page: <https://github.com/supabase/supabase/pull/30317>


Link: <https://supabase.com/dashboard/project/_/editor>
## Other bug fixes and improvements[#](https://supabase.com/changelog#other-bug-fixes-and-improvements)
[Table Editor](https://supabase.com/dashboard/project/_/editor)
  * Simplified header when rows are selected ([PR](https://github.com/supabase/supabase/pull/29963))
  * Allow exporting of data on tables that are protected ([PR](https://github.com/supabase/supabase/pull/30310))


[Authentication](https://supabase.com/dashboard/project/_/auth/users)
  * Fixed provider "Enabled" state when viewing user details if user's provider is LinkedIn ([PR](https://github.com/supabase/supabase/pull/30373))
  * Sorting users on a column will shift users with NULL values on that column to the bottom ([PR](https://github.com/supabase/supabase/pull/30430))
  * Fix "Last signed in at" column showing up as "Waiting for verification" on subsequent pages as page is scrolled down ([PR](https://github.com/supabase/supabase/pull/30507))


[Storage](https://supabase.com/dashboard/project/_/settings/storage)
  * Add ability to toggle image transformations from settings ([PR](https://github.com/supabase/supabase/pull/30094/files))


### [`supabase-js` release candidate `2.46.2-rc.3` incoming types inferences for PostgREST fixes and feedbacks ](https://github.com/orgs/supabase/discussions/30324)
Nov 6, 2024
🚀 **Announcement:** We’ve just released `supabase-js` version `2.46.2-rc.3`, which resolves several type errors in the PostgREST client.
### Notable issues resolved:[#](https://supabase.com/changelog#notable-issues-resolved)
  * <https://github.com/supabase/postgrest-js/issues/523>
  * <https://github.com/supabase/supabase-js/issues/943>
  * <https://github.com/supabase/postgrest-js/issues/450>
  * <https://github.com/supabase/postgrest-js/issues/546>
  * <https://github.com/supabase/supabase-js/issues/930>


We’d love your feedback to ensure everything runs smoothly!
### **Important Notes:**[ #](https://supabase.com/changelog#important-notes)
This update _might_ require regenerating your database types. You can do this via the Supabase CLI (≥[v1.207.8](https://github.com/supabase/cli/releases/tag/v1.207.8)) or the dashboard. For instructions, check out our guide [here](https://supabase.com/docs/guides/api/rest/generating-types).
### **Potential Issues**[ #](https://supabase.com/changelog#potential-issues)
This version introduces stricter alignment between runtime behavior and type inference. As a result, some types might appear "broken" but are actually being corrected.
The main changes to be aware of:
  1. The result of an embedding now correctly infers a single object or an array based on the relationship.
  2. The result of an object embedding now more accurately identifies whether the result can be `null`.


Before reporting a bug, please double-check that the inferred types are truly incorrect based on your query and database schema.
### **Bug Reporting:**[ #](https://supabase.com/changelog#bug-reporting)
If your project is hosted on Supabase, please open a support ticket [here](https://supabase.com/dashboard/support/new) and check "Allow Supabase Support to access your project temporarily." This will enable us to investigate your database types directly.
Alternatively, you can open an issue on [GitHub](https://github.com/supabase/postgrest-js). Please include:
  1. The generated `Database` type used to instantiate the client (e.g., `createClient<Database>(process.env.SUPABASE_URL, process.env.SUPABASE_ANON_KEY)`). If possible a minimal `SQL` declaration resulting in such `Database` type.
  2. The query where type inference failed (e.g., `.from('which-table').select('which-query')`).
  3. Your TypeScript version (`npx tsc -v`).


### [Write Edge Functions in pure JavaScript instead of using TypeScript ](https://github.com/orgs/supabase/discussions/30307)
Nov 5, 2024
From Supabase CLI version 1.215.0 or higher you can configure a custom entrypoint to your Edge Functions. This can be used to write Edge Functions in pure JavaScript instead of TypeScript.
Save your Function as a JavaScript file (eg: `index.js`) and then update the `supabase/config.toml` as follows:
`
1
[functions.hello-world]
2
# other entries
3
entrypoint = './functions/hello-world/index.js' # path must be relative to config.toml
`
You can use any `.ts`, `.js`, `.tsx`, `.jsx` or `.mjs` file as the entrypoint for a Function.
More details: <https://supabase.com/docs/guides/functions/quickstart#not-using-typescript>
### [Use `deno.json` configuration file in Edge Functions ](https://github.com/orgs/supabase/discussions/30291)
Nov 5, 2024
Each Edge Function can now have its own `deno.json` or `deno.jsonc` file to manage dependencies. You will need to deploy your functions using Supabase CLI version v1.215.0 or above to make use of this feature.
### How to use `deno.json`[#](https://supabase.com/changelog#how-to-use-denojson)
Create a `deno.json` in your function's folder:
`
1
// supabase/functions/function-name/deno.json
2
{
3
 "imports": {
4
  "lodash": "https://cdn.skypack.dev/lodash"
5
 }
6
}
`
You can now use aliased imports in your source code:
`
1
// supabase/functions/function-name/index.ts
2
import lodash from 'lodash'
`
To test your function locally, run `supabase functions serve`. When you're ready, you can deploy it to hosted platform by running `supabase functions deploy function-name`
For more details, check the guide: <https://supabase.com/docs/guides/functions/import-maps#using-denojson-recommended>
### [Dashboard Updates [21/10/24 - 04/11/24] ](https://github.com/orgs/supabase/discussions/30264)
Nov 4, 2024
## Spam validation check now added to Auth templates[#](https://supabase.com/changelog#spam-validation-check-now-added-to-auth-templates)
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fa0dffb5a-6cf5-436e-8364-cbaca61815b1&w=3840&q=75)
We've now added a spam validation checker for your email templates in the Auth section of the dashboard! This is powered by [SpamAssassin](https://spamassassin.apache.org/doc.html) and is in hopes to assist you with writing email content in a way to avoid being marked as spam by email clients.
You will still be able to save your email templates regardless of whether you're using the built-in SMTP provider or a custom SMTP provider. However, we highly recommend fixing these warnings since they can affect email deliverability.
PR: <https://github.com/supabase/supabase/pull/30188>
Links: <https://supabase.com/dashboard/project/_/auth/templates>
## Other improvements and bug fixes[#](https://supabase.com/changelog#other-improvements-and-bug-fixes)
[Authentication](https://supabase.com/dashboard/project/_/auth/users)
  * Hovering over auth logs for a user will show relative time info ([PR](https://github.com/supabase/supabase/pull/30013))
  * Allow sorting on last signed in at for users ([PR](https://github.com/supabase/supabase/pull/30202))
  * Allow selection of functions that return void for auth hooks ([PR](https://github.com/supabase/supabase/pull/30022))
  * Allow updating of SMS rate limit irregardless of SMS autoconfirm being enabled ([PR](https://github.com/supabase/supabase/pull/30039))


[Storage](https://supabase.com/dashboard/project/_storage/buckets)
  * Fix developer roles not being able to update buckets ([PR](https://github.com/supabase/supabase/pull/30024))


[Database](https://supabase.com/dashboard/project/_/database/indexes)
  * Fix create index "Select a table" combobox not using search input ([PR](https://github.com/supabase/supabase/pull/29986))
  * Support opening tables in table editor from the schema visualizer ([PR](https://github.com/supabase/supabase/pull/30052))


[Logs & Analytics](https://supabase.com/dashboard/project/_/logs/edge-logs)
  * Fix filters for log reports ([PR](https://github.com/supabase/supabase/pull/30102))


### [Import NPM packages from private registries in Edge Functions ](https://github.com/orgs/supabase/discussions/30179)
Oct 29, 2024
Edge Functions now support importing NPM packages from private registries. You will need to deploy your functions using Supabase CLI version v1.207.9 or above to make use of this feature.
### How to use packages from private registries[#](https://supabase.com/changelog#how-to-use-packages-from-private-registries)
Create a `.npmrc` file within `supabase/functions`. This will allow you to import the private packages into multiple functions. Alternatively, you can place the `.npmrc` file directly inside `supabase/functions/function-name` directory.
Add your registry details in the `.npmrc` file. Follow [this guide](https://docs.npmjs.com/cli/v10/configuring-npm/npmrc) to learn more about the syntax of npmrc files.
`
1
@myorg:registry=https://npm.registryhost.com
2
//npm.registryhost.com/:_authToken=VALID_AUTH_TOKEN
`
After that, you can import the package directly in your function code or add it to the `import_map.json` (<https://supabase.com/docs/guides/functions/import-maps#using-import-maps>).
`
1
import MyPackage from "npm:@myorg/private-package@v1.0.1"
23
// use MyPackage
`
To test your function locally, run `supabase functions serve`. When you're ready, you can deploy it to hosted platform by running `supabase functions deploy function-name`
### [Dashboard Updates [07/10/24 - 21/10/24] ](https://github.com/orgs/supabase/discussions/30005)
Oct 21, 2024
## Disk size usage section under organization settings[#](https://supabase.com/changelog#disk-size-usage-section-under-organization-settings)
![Screenshot 2024-10-13 at 03 21 37](https://github.com/user-attachments/assets/2a20a674-3b83-4463-b5c4-be008f1a3dcd)
We've added a new disk size section for paid plans to give a quick overview of each project under the organization and their respective disk sizes for better visibility over the corresponding charges. This is only an initial iteration for this UI, we do plan to add historical statistics and more to improve visibility and transparency over what you're using and what you're paying for 🙂
PR: <https://github.com/supabase/supabase/pull/29862>
Link: <https://supabase.com/dashboard/org/_/usage>
## Bug fixes and other improvements[#](https://supabase.com/changelog#bug-fixes-and-other-improvements)
[Table Editor](https://supabase.com/dashboard/project/_/editor)
  * Fix views filtering in table editor for local dashboard ([PR](https://github.com/supabase/supabase/pull/29646))
  * Fix exporting a table that contains columns of enum array types to CSV ([PR](https://github.com/supabase/supabase/pull/29723))


[SQL Editor](https://supabase.com/dashboard/project/_/sql/new)
  * Fix snippets not loading for local dashboard ([PR](https://github.com/supabase/supabase/pull/29750))


[Authentication](https://supabase.com/dashboard/project/_/auth/users)
  * Support searching by properties when viewing a user's raw JSON ([PR](https://github.com/supabase/supabase/pull/29825))


### [Developer Update - September 2024 ](https://github.com/orgs/supabase/discussions/29828)
Oct 10, 2024
We’ve announced a Vercel partnership, we’re hosting an AI hackathon with our friends at Y Combinator, and we raised $80M. Let’s dive right in:
## Supabase + Vercel Partnership[#](https://supabase.com/changelog#supabase--vercel-partnership)
![Supabase + Vercel Partnership](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fseptember2024%2Fsupabase-x-vercel.png%3Ft%3D2024-10-10T02%253A59%253A39.452Z&w=3840&q=75)
We released an official Vercel integration. You can quickly spin up Supabase projects from Vercel’s dashboard, with full support for Vercel templates like Supabase Starter and integrated billing through Vercel.
[Full announcement](https://supabase.link/supabase-vercel-partnership)
## Revamped Users Management UI in Studio[#](https://supabase.com/changelog#revamped-users-management-ui-in-studio)
![Revamped Users Management UI in Studio](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fseptember2024%2Frevamped-users-management-ui-in-studio.png%3Ft%3D2024-10-10T03%253A00%253A01.836Z&w=3840&q=75)
Our Frontend team revamped the Auth section in Studio. You now have access to more user details, ban-user functionality, authenticated logs grouped by user, sort columns based on your preference, and a few other features requested by the community.
[Changelog](https://supabase.link/users-mgmt-revamp)
## Edge Functions are 2x smaller and boot 3x faster[#](https://supabase.com/changelog#edge-functions-are-2x-smaller-and-boot-3x-faster)
![Edge Functions are 2x smaller and boot 3x faster](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fseptember2024%2Fedge-functions-are-2x-smaller-and-boot-3x-faster.png%3Ft%3D2024-10-10T03%253A00%253A13.326Z&w=3840&q=75)
The Edge Functions team has reduced function sizes by half and boot times by 300% in most cases when importing npm modules by lazy evaluating dependencies and reducing package section sizes as well as switching to the xxHash-3 hash algorithm.
[Blog post](https://supabase.link/edge-functions-faster-smaller)
## Supabase AI Hackathon at Y Combinator[#](https://supabase.com/changelog#supabase-ai-hackathon-at-y-combinator)
![Supabase AI Hackathon at Y Combinator](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fseptember2024%2Fsupabase-ai-hackathon-at-y-combinator.png%3Ft%3D2024-10-10T03%253A00%253A23.124Z&w=3840&q=75)
On November 22 + 23 we’re hosting an AI-focused hackathon at Y Combinator in San Francisco. We’re welcoming anyone to apply and build the next wave of AI applications. The panel of judges will include our founders, [Paul Copplestone](https://x.com/kiwicopple) and [Ant Wilson](https://x.com/AntWilson), and YC partners.
[Full announcement](https://supabase.link/supabase-yc-ai-hackathon)
## Launch Week 12 Hackathon Winners[#](https://supabase.com/changelog#launch-week-12-hackathon-winners)
![Launch Week 12 Hackathon Winners](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fseptember2024%2Flaunch-week-12-hackathon-winners.png%3Ft%3D2024-10-10T03%253A00%253A42.904Z&w=3840&q=75)
Many high quality projects were submitted for LW12’s hackathon but our panel of judges selected [Whisker Jam](https://supabase.link/whisker-jam-lw12) as Best Overall Project because of its cuteness (who doesn’t love cats), funky musical instruments, and multiplayer functionality. Congratulations 👏 to [@n0t_buddy](https://twitter.com/n0t_buddy) who will receive the prize of mechanical keyboards.
[Full list of winners](https://supabase.link/lw12-hackathon-winners) | [All the submissions](https://supabase.link/lw12-submissions)
## Quick Product Announcements[#](https://supabase.com/changelog#quick-product-announcements)
  * [Dashboard] Schema Visualizer nodes are now persisted [[Changelog](https://supabase.link/schema-visualizer-nodes)]
  * [Edge Functions] Serverless image transformations with ImageMagick (via Wasm) [[Docs](https://supabase.link/imagemagick-wasm)]
  * [Infra] Projects on compute instances XL and larger can create up to 5 Read Replicas [[Changelog](https://supabase.link/5-read-replicas)]
  * [Storage] XHTML responses only work with a Custom Domain [[Changelog](https://supabase.link/xhtml-custom-domains)]
  * [Billing] Paid projects have an upgrade from Nano to Micro instance at no additional cost [[Docs](https://supabase.link/micro-upgrade)]


## Community Highlights[#](https://supabase.com/changelog#community-highlights)
![community highlights](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fmarketing-emails%2Fseptember2024%2Fcommunity_highlights.png%3Ft%3D2024-10-10T03%253A00%253A54.371Z&w=3840&q=75)
  * Using Cursor to have AI build out a social network app powered by Next.js and Supabase [[Video](https://supabase.link/cursor-ai-app-nextjs-supabase)]
  * Wordle Teams. Compete with friends, keep score to establish bragging rights in the ultimate app for Wordle enthusiasts [[Repo](https://supabase.link/wordle-teams)]
  * Next.js + TanStack Query + Supabase + Supabase Cache Helpers: a detailed tutorial on how to implement this stack in your application [[Article](https://supabase.link/nextjs-tanstack-query-supabase-guide)]
  * Supabase Auth: The Ultimate Authentication Solution for Cross-Platform Apps using React Native [[Article](https://supabase.link/supabase-auth-ultimate-solution-react-native)]
  * How to build local-first Expo Apps [[Video](https://supabase.link/local-first-expo-supabase)]


## Supabase $80 Million Series C[#](https://supabase.com/changelog#supabase-80-million-series-c)
We raised $80 million Series C in an up round that brings our total funding to $196 million. This round was led by Peak XV and Craft Ventures with participation by Avra Capital and previous investors Coatue, Felicis, and Y Combinator.
[Full announcement](https://supabase.link/supabase-80-mil-series-c)
_This discussion was created from the release[Developer Update - September 2024](https://github.com/supabase/supabase/releases/tag/v1.24.09)._
### [Improved docs information architecture ](https://github.com/orgs/supabase/discussions/29798)
Oct 9, 2024
We improved the information architecture (IA) on our docs site.
## Why?[#](https://supabase.com/changelog#why)
We’d outgrown the IA! As we added more features and guides, some sections grew to contain a miscellaneous collection of things that don’t belong together. They just had no better place to go.
With the new IA, it should be easier to find what you’re looking for.
## Summary of changes[#](https://supabase.com/changelog#summary-of-changes)
  * Two top-level menus, **Build** and **Manage** , to replace the old **Build** menu
  * **Build** menu: 
    * **Local development / CLI** is now primarily about local dev, CI/CD information has been moved to **Deployment**
    * Information on both Vercel and Supabase integrations now moved to **Integrations** section
    * New **Deployment** section covers everything needed to get your changes onto hosted Supabase (including branching, Terraform, CI/CD, and production checklists)
  * **Manage** menu: 
    * **Platform management** (formerly “Platform”) trimmed down to contain information about configuring your Supabase platform (including account management, project permissions, and billing)
    * New **Monitoring and troubleshooting** section contains troubleshooting guides and information on logging and telemetry


### [Dashboard Updates [23/09/24 - 07/10/24] ](https://github.com/orgs/supabase/discussions/29710)
Oct 6, 2024
## Improved users management UI[#](https://supabase.com/changelog#improved-users-management-ui)
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F59be9f0e-30ad-4eeb-aa99-cafc6f0b83e5&w=3840&q=75)
One of our oldest pages on the dashboard has finally gotten an upgrade! 😄 We're taking the first steps towards a pattern of visualizing table data with a data grid, with the Auth users page being our first contender. Couple of stuff that we'd love to highlight that were improved and introduced:
### Click on users to grab more details about them in a side panel ([PR](https://github.com/supabase/supabase/pull/29468))[#](https://supabase.com/changelog#click-on-users-to-grab-more-details-about-them-in-a-side-panel-pr)
![Screenshot 2024-10-07 at 11 55 24](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F1393bbe2-ec47-4bef-a7a4-17ce133b060b&w=3840&q=75)
### Added a ban functionality within the danger zone at the bottom of the panel[#](https://supabase.com/changelog#added-a-ban-functionality-within-the-danger-zone-at-the-bottom-of-the-panel)
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fce7db424-5caa-457a-9180-2e999b180a8e&w=3840&q=75)
### Search now also supports filtering for providers ([PR](https://github.com/supabase/supabase/pull/29515))[#](https://supabase.com/changelog#search-now-also-supports-filtering-for-providers-pr)
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fde943a7e-02ae-4de7-a0a6-5f7b4b1d70d7&w=3840&q=75)
### Columns can be sorted based on your preference (and will be persisted in local storage)[#](https://supabase.com/changelog#columns-can-be-sorted-based-on-your-preference-and-will-be-persisted-in-local-storage)
<https://github.com/user-attachments/assets/3f7890ca-04cf-4cb9-8046-63b3db9b6eb9>
### You can also now toggle column visibility, as well as apply sorts on columns[#](https://supabase.com/changelog#you-can-also-now-toggle-column-visibility-as-well-as-apply-sorts-on-columns)
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2Fa3009aac-e8d1-4a4a-9744-8af9d0375822&w=3840&q=75)
### View authentication logs of the user right from the panel ([PR](https://github.com/supabase/supabase/pull/29656))[#](https://supabase.com/changelog#view-authentication-logs-of-the-user-right-from-the-panel-pr)
![image](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fuser-attachments%2Fassets%2F87a6fe4c-f3e4-4fb1-a7be-80ef1e07270d&w=3840&q=75)
These tooling should now allow you to customize the auth users view that best fits your workflow, and we definitely hope to keep making this better so as always, feel free to drop us any feedback good or bad, any bugs via the widget at the top right corner of the dashboard 🙂 We say this all the time and its a promise that we've kept - we look at _every_ feedback that comes in 🤙
PR: <https://github.com/supabase/supabase/pull/29105>
Link: <https://supabase.com/dashboard/project/_/auth/users>
## Timestamp helper for Logs Collections[#](https://supabase.com/changelog#timestamp-helper-for-logs-collections)
<https://github.com/user-attachments/assets/80541e0a-4571-4193-ab9e-8d9af4b63d55>
Hovering over the date/time string in the left most column of a row in any logs collection will now show a helper tooltip that will depict the time in 4 different formats: UTC, Local TZ, Relative time, and raw numerical timestamp. This will hopefully help with interpreting timestamps much easier and faster and alleviate any confusion around timezones! 🙂🕰️ We're also planning to use this pattern across the whole dashboard too wherever time data is involved 💪🏻
PR: <https://github.com/supabase/supabase/pull/29530>
Link: [https://supabase.com/dashboard/project/_/logs/edge-logs](http://localhost:8082/project/_/logs/edge-logs)
## Other bug fixes and improvements[#](https://supabase.com/changelog#other-bug-fixes-and-improvements)
[General](https://supabase.com/dashboard)
  * Added breakdown of security issues dropdown on project home page ([PR](https://github.com/supabase/supabase/pull/29598))


[Organization Settings](https://supabase.com/dashboard/org/_/team)
  * Fixed tooltip not showing up for users with project scoped roles, to show which projects they have roles for ([PR](https://github.com/supabase/supabase/pull/29502))


[Table Editor](https://supabase.com/dashboard/project/_/editor)
  * Autofocus on search input when navigating to table editor ([PR](https://github.com/supabase/supabase/pull/29446))
  * Improved column type dropdown with searching for types ([PR](https://github.com/supabase/supabase/pull/29534))
  * Improved datetime editing in table editor grid + support for setting these column values to NULL ([PR](https://github.com/supabase/supabase/pull/29660))


[Edge Functions](https://supabase.com/dashboard/project/_/settings/functions)
  * Added validations for adding/removing secrets on SUPABASE_ prefixed secrets ([PR](https://github.com/supabase/supabase/pull/29661))


[Reports](https://supabase.com/dashboard/project/_/reports/database)
  * Added database connections charts to database reports ([PR](https://github.com/supabase/supabase/pull/29637))


### [XHTML responses are only allowed with a Custom Domain enabled ](https://github.com/orgs/supabase/discussions/29633)
Oct 1, 2024
## Summary[#](https://supabase.com/changelog#summary)
Returning XHTML responses from the Data APIs and Edge Functions is now only allowed if a [Custom Domain](https://supabase.com/docs/guides/platform/custom-domains) is being used.
Additionally, you can now serve HTML and XHTML responses from the Storage service as well, if a Custom Domain is being used.
If your use-case requires serving these content types, you can continue to do so by using a Custom Domain add-on.
Affected projects have been notified in advance.
## Background[#](https://supabase.com/changelog#background)
HTML responses (i.e. content-types that can be directly rendered by browsers) were historically disallowed for projects not using a custom domain, in order to prevent abuse on the shared domains used for provisioning Supabase projects. This change updates this behavior to process XHTML responses in the same manner, due to the same rationale.
[Next ](https://supabase.com/changelog?next=Y3Vyc29yOnYyOpK0MjAyNC0xMC0wMlQwMTowNDo1OFrOAG7eFA==&restPage=2)
## Build in a weekend, scale to millions
[Start your project](https://supabase.com/dashboard)[Request a demo](https://supabase.com/contact/sales)
## Footer
We protect your data.[More on Security](https://supabase.com/security)
  * SOC2 Type 2 Certified
  * HIPAA Compliant


[![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fa88e89e4a86b%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--light.daaeffd3.png&w=384&q=75)![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fa88e89e4a86b%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--dark.b36ebb5f.png&w=384&q=75)](https://supabase.com/)
[Twitter](https://twitter.com/supabase)[GitHub](https://github.com/supabase)[Discord](https://discord.supabase.com/)[Youtube](https://youtube.com/c/supabase)
###### Product
  * [Database](https://supabase.com/database)
  * [Auth](https://supabase.com/auth)
  * [Functions](https://supabase.com/edge-functions)
  * [Realtime](https://supabase.com/realtime)
  * [Storage](https://supabase.com/storage)
  * [Vector](https://supabase.com/modules/vector)
  * [Cron](https://supabase.com/modules/cron)
  * [Pricing](https://supabase.com/pricing)
  * [Launch Week](https://supabase.com/launch-week)


###### Solutions
  * [AI Builders](https://supabase.com/solutions/ai-builders)
  * [No Code](https://supabase.com/solutions/no-code)
  * [Beginners](https://supabase.com/solutions/beginners)
  * [Developers](https://supabase.com/solutions/developers)
  * [Postgres Devs](https://supabase.com/solutions/postgres-developers)
  * [Switch From Neon](https://supabase.com/solutions/switch-from-neon)
  * [Startups](https://supabase.com/solutions/startups)
  * [Enterprise](https://supabase.com/solutions/enterprise)


###### Resources
  * [Blog](https://supabase.com/blog)
  * [Support](https://supabase.com/support)
  * [System Status](https://status.supabase.com/)
  * [Become a Partner](https://supabase.com/partners)
  * [Integrations](https://supabase.com/partners/integrations)
  * [Brand Assets](https://supabase.com/brand-assets)
  * [Security & Compliance](https://supabase.com/security)
  * [DPA](https://supabase.com/legal/dpa)
  * [SOC2](https://supabase.com/security)
  * [HIPAA](https://forms.supabase.com/hipaa2)


###### Developers
  * [Documentation](https://supabase.com/docs)
  * [Supabase UI](https://supabase.com/ui)
  * [Changelog](https://supabase.com/changelog)
  * [Careers](https://supabase.com/careers)
  * [Contributing](https://github.com/supabase/supabase/blob/master/CONTRIBUTING.md)
  * [Open Source](https://supabase.com/open-source)
  * [SupaSquad](https://supabase.com/supasquad)
  * [DevTo](https://dev.to/supabase)
  * [RSS](https://supabase.com/rss.xml)


###### Company
  * [Company](https://supabase.com/company)
  * [General Availability](https://supabase.com/ga)
  * [Terms of Service](https://supabase.com/terms)
  * [Privacy Policy](https://supabase.com/privacy)
  * Privacy Settings
  * [Acceptable Use Policy](https://supabase.com/aup)
  * [Support Policy](https://supabase.com/support-policy)
  * [Service Level Agreement](https://supabase.com/sla)
  * [Humans.txt](https://supabase.com/humans.txt)
  * [Lawyers.txt](https://supabase.com/lawyers.txt)
  * [Security.txt](https://supabase.com/.well-known/security.txt)


© Supabase Inc
Toggle theme
