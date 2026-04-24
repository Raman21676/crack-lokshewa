# Crack Lokshewa Mock Test Website

This is a static, frontend-only mock test website designed for students preparing for government jobs in Nepal (Kharidar, Subbha, Adhikrit, etc.).

## Features
*   **Static Architecture:** Runs completely without a backend database. Ideal for free hosting on GitHub Pages.
*   **Data Driven:** All questions and categories are stored in easily editable JSON files.
*   **Modern UI:** Responsive, clean design with micro-animations.
*   **Full Test Flow:** Browse categories -> Select Test -> Answer Questions -> View Results & Correct Answers.

## How to Test Locally
Because this project uses the `fetch()` API to load the JSON files, simply double-clicking `index.html` might not work in some browsers due to security restrictions (CORS). 

You need to serve the folder over a local HTTP server.

**Option 1: Using VS Code**
1. Open this folder in Visual Studio Code.
2. Install the **"Live Server"** extension.
3. Right-click on `index.html` and select "Open with Live Server".

**Option 2: Using Python**
If you have Python installed, open your terminal/command prompt in this folder and run:
`python -m http.server 8000`
Then open your browser and go to `http://localhost:8000`

## How to Add More Questions
All data is stored in the `data/` folder.

1. **Add a new category:** Edit `data/categories.json`.
2. **Add tests to a category:** Create a folder for the category (e.g., `data/police/`) and create a `tests.json` inside it.
3. **Add questions to a test:** Inside the category folder, create a JSON file named exactly as the test's ID (e.g., `test1.json`) and follow the structure of existing tests.

## Deployment to GitHub Pages
1. Create a new repository on GitHub.
2. Upload all the files in this folder to the repository.
3. Go to the repository **Settings** > **Pages**.
4. Select the `main` branch as the source and save.
5. Your website will be live in a few minutes!
