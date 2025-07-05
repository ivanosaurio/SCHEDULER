### 🔄 Project Awareness & Context
- **Every time you start a new command with the users input, your must read again this file and ensure all the rules are been followed again. This step is mandatory and cannot be overseen.**
- **At the start of your session you must read very file available to you with the only exception been .env. This is something you always must do in order to create the planning.md, otherwise you cant**
- **Always create `PLANNING.md` as a new command is given to you. This planning should have all the users desires broken down into little ministeps**
- **Always read `PLANNING.md`** at the start of a new conversation to understand the project's architecture, goals, style, and constraints.
- **Create in `TASK.md` a new subtask that allows you to work only on 1 task at a time**
- **Check `TASK.md`** before starting a new task. If the task isn’t listed, add it with a brief description and today's date.
- **Use consistent naming conventions, file structure, and architecture patterns** as described in `PLANNING.md`.
- **You must read every file that has an intervinience from you, even if the code only affects other files, you must read all the files it affects that change**
- **All your answers must be in spanish.**

### 🧱 Code Structure & Modularity
- **Never create a file longer than 500 lines of code.** If a file approaches this limit, refactor by splitting it into modules or helper files.
- **Organize code into clearly separated modules**, grouped by feature or responsibility.
For Flet Web Aplications this looks like:
    - 'main.py' - Main central for everything that needs to happen
    - 'config.py' - The place where you export and create all the keys, secrets, and accesses you need for your aplication
    - 'theme.py' - Where you store all the visual structure of your app, so it has a cohesive feeling alongside the entire aplication
    - '.env' - The place where you store all the keys, secrets, and the sensitive information
    - 'assets folder' - The folder used to store the images (png, jpg, jpeg, etc), the videos(mp4, mkv, etc), and every piece of media needed for the app
    - 'views folder' - The folder where you create all the views for the app, the login, register, dashboard etc.
    - 'components folder' - The folder used to store components needed in a one/multiple views, such as: sidepar.py, queue_item.py, placeholder.py, thread_input.py, or any component similar or needed for the view to create.
    - 'services folder' - The folder used in the creation of connections with 3rd party apps, such as supabase, twitter, authentication services etc. The files within this folder lokk like: supabase_service.py, auth_service.py, twitter_service.py etc


- **Use clear, consistent imports** (prefer relative imports within packages).
- **Use clear, consistent imports** (prefer relative imports within packages).
- **Use python_dotenv and load_env()** for environment variables.

### 🧪 Information retrieval
- **You have a folder called crawled_markdown** This contains the only functional methods, functions, practices and information available for you to write code with. Every time you suggest a change or code new lines, you must doble check if you have the explicit way to achieve that result. If not, ask the user to update the folder

### ✅ Task Completion
- **Mark completed tasks in `TASK.md`** immediately after finishing them.
- Add new sub-tasks or TODOs discovered during development to `TASK.md` under a “Discovered During Work” section.

### 📎 Style & Conventions
- **Use Python** as the primary language.
- **Use `pyhton -m pip` for any usecasses that ypu need to use pip**
- **Use `flet` for web structure and creation**
- **Use `supabase` for data base connection and managment**.

### 📚 Documentation & Explainability
- **Create a `README.md` at the start of your session only if theres not one already created** when new features are added, dependencies change, or setup steps are modified ensure the README.md is updated.
- **Comment non-obvious code** and ensure everything is understandable to a mid-level developer.
- When writing complex logic, **add an inline `# Reason:` comment** explaining the why, not just the what.

### 🧠 AI Behavior Rules
- **Never assume missing context. Ask questions if uncertain.**
- **Never hallucinate libraries or functions** – only use known, verified Python packages.
- **Always confirm file paths and module names** exist before referencing them in code or tests.
- **Never delete or overwrite existing code** unless explicitly instructed to or if part of a task from `TASK.md`.