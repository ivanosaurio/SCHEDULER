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
[REST API](https://supabase.com/docs/guides/api)
  * [Overview](https://supabase.com/docs/guides/api)
  * [Quickstart](https://supabase.com/docs/guides/api/quickstart)
  * [Client Libraries](https://supabase.com/docs/guides/api/rest/client-libs)
  * [Auto-generated Docs](https://supabase.com/docs/guides/api/rest/auto-generated-docs)
  * [Generating TypeScript Types](https://supabase.com/docs/guides/api/rest/generating-types)
Tools
  * [SQL to REST API Translator](https://supabase.com/docs/guides/api/sql-to-rest)
Guides
  * [Creating API routes](https://supabase.com/docs/guides/api/creating-routes)
  * [How API Keys work](https://supabase.com/docs/guides/api/api-keys)
  * [Securing your API](https://supabase.com/docs/guides/api/securing-your-api)
Using the Data APIs
  * [Managing tables, views, and data](https://supabase.com/docs/guides/database/tables)
  * [Querying joins and nested tables](https://supabase.com/docs/guides/database/joins-and-nesting)
  * [JSON and unstructured data](https://supabase.com/docs/guides/database/json)
  * [Managing database functions](https://supabase.com/docs/guides/database/functions)
  * [Using full-text search](https://supabase.com/docs/guides/database/full-text-search)
  * [Debugging performance issues](https://supabase.com/docs/guides/database/debugging-performance)
  * [Using custom schemas](https://supabase.com/docs/guides/api/using-custom-schemas)
  * [Converting from SQL to JavaScript API](https://supabase.com/docs/guides/api/sql-to-api)


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
REST API
  1. [REST API](https://supabase.com/docs/guides/api)
  2. [Overview](https://supabase.com/docs/guides/api)


REST API
Supabase auto-generates an API directly from your database schema allowing you to connect to your database through a restful interface, directly from the browser.
The API is auto-generated from your database and is designed to get you building as fast as possible, without writing a single line of code.
You can use them directly from the browser (two-tier architecture), or as a complement to your own API server (three-tier architecture).
## Features [#](https://supabase.com/docs/guides/api#rest-api-overview)
Supabase provides a RESTful API using [PostgREST](https://postgrest.org/). This is a very thin API layer on top of Postgres. It exposes everything you need from a CRUD API at the URL `https://<project_ref>.supabase.co/rest/v1/`.
The REST interface is automatically reflected from your database's schema and is:
  * **Instant and auto-generated.** As you update your database the changes are immediately accessible through your API.
  * **Self documenting.** Supabase generates documentation in the Dashboard which updates as you make database changes.
  * **Secure.** The API is configured to work with PostgreSQL's Row Level Security, provisioned behind an API gateway with key-auth enabled.
  * **Fast.** Our benchmarks for basic reads are more than 300% faster than Firebase. The API is a very thin layer on top of Postgres, which does most of the heavy lifting.
  * **Scalable.** The API can serve thousands of simultaneous requests, and works well for Serverless workloads.


The reflected API is designed to retain as much of Postgres' capability as possible including:
  * Basic CRUD operations (Create/Read/Update/Delete)
  * Arbitrarily deep relationships among tables/views, functions that return table types can also nest related tables/views.
  * Works with Postgres Views, Materialized Views and Foreign Tables
  * Works with Postgres Functions
  * User defined computed columns and computed relationships
  * The Postgres security model - including Row Level Security, Roles, and Grants.


The REST API resolves all requests to a single SQL statement leading to fast response times and high throughput.
Reference:
  * [Docs](https://postgrest.org/)
  * [Source Code](https://github.com/PostgREST/postgrest)


## API URL and keys[#](https://supabase.com/docs/guides/api#api-url-and-keys)
You can find the API URL and Keys in the [Dashboard](https://supabase.com/dashboard/project/_/settings/api-keys).
[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/api.mdx)
### Is this helpful?
No Yes
### On this page
[Features ](https://supabase.com/docs/guides/api#rest-api-overview)[API URL and keys](https://supabase.com/docs/guides/api#api-url-and-keys)
  * Need some help?
[Contact support](https://supabase.com/support)
  * Latest product updates?
[See Changelog](https://supabase.com/changelog)
  * Something's not right?
[Check system status](https://status.supabase.com/)


[© Supabase Inc](https://supabase.com/)—[Contributing](https://github.com/supabase/supabase/blob/master/apps/docs/DEVELOPERS.md)[Author Styleguide](https://github.com/supabase/supabase/blob/master/apps/docs/CONTRIBUTING.md)[Open Source](https://supabase.com/open-source)[SupaSquad](https://supabase.com/supasquad)Privacy Settings
[GitHub](https://github.com/supabase/supabase)[Twitter](https://twitter.com/supabase)[Discord](https://discord.supabase.com/)
