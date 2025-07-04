## Accessibility Testing

This project includes basic accessibility audits using [Pa11y](https://pa11y.org/).

### ✅ Tested URLs:
- [Wikipedia.org](https://www.wikipedia.org) → [`wikipedia-a11y-report.txt`](accessibility/wikipedia-a11y-report.txt)
- [CNN.com](https://www.cnn.com) → [`cnn-a11y-report.txt`](accessibility/cnn-a11y-report.txt)

These reports highlight potential WCAG 2.1 AA compliance issues such as:
- Missing form labels or legends
- Malformed language attributes
- Use of deprecated HTML
- Missing alt text or responsive image handling

Tools used:
- Node.js
- Pa11y CLI
- Google Chrome (manual executable path)
