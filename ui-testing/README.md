# UI Testing with Playwright

This folder contains automated UI tests for two major websites — [Wikipedia](https://www.wikipedia.org) and [CNN](https://edition.cnn.com) — using [Playwright](https://playwright.dev/).

## 📦 Folder Contents

| File                     | Description                                      |
|--------------------------|--------------------------------------------------|
| `wikipedia-ui.spec.js`  | UI test for Wikipedia homepage                   |
| `cnn-ui.spec.js`        | UI test for CNN homepage                         |
| `package.json`          | Project setup and dependencies                   |
| `node_modules/`         | Installed Playwright packages                    |

---

## ✅ What Do These Tests Cover?

### 🧪 `wikipedia-ui.spec.js`
- Opens the Wikipedia homepage
- Verifies that the search input is visible
- Checks basic UI interaction readiness

### 🧪 `cnn-ui.spec.js`
- Loads the CNN homepage
- Verifies that the search icon is visible and clickable
- Confirms that the search input field becomes visible after clicking

---

## 🚀 How to Run These Tests

Make sure you're inside the `ui-testing` folder.

### 1. Install Playwright (if not already):
```bash
npm install -D @playwright/test
npx playwright install
**### 2. Run Tests:**

npx playwright test
Or run a specific test:

npx playwright test wikipedia-ui.spec.js
npx playwright test cnn-ui.spec.js
🛠 Notes
These tests use Playwright Test's native assertions (e.g. expect(locator).toBeVisible()).

If a test fails, check if the site has changed structure (e.g. new selectors, dynamic content).

Ensure you have internet access while running tests.

👤 Author
Rain Go — aspiring QA Analyst exploring test automation using open-source tools like Playwright.

python
Copy
Edit
