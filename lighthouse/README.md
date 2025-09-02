# 🌐 Website Performance Testing with Lighthouse CI

This project uses [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci) to automate performance, accessibility, and SEO audits on live websites.

## 📦 What’s Inside
- Automated tests using `npx lhci autorun`
- Reports for:
  - [Wikipedia.org](https://www.wikipedia.org)
  - [CNN.com](https://www.cnn.com)
- Results saved in `/lhci-reports` as `.html` files

## 📊 Example Summary

| Website     | Performance | Accessibility | SEO | Best Practices |
|-------------|-------------|----------------|-----|----------------|
| Wikipedia   | ❌ Low       | ❌ Low          | ✅ High | ⚠️ Medium       |
| CNN         | ❌ Very Low  | ⚠️ Medium       | ❌ Low  | ⚠️ Low          |

> 💡 These scores are based on default Lighthouse thresholds. See the full HTML reports for details.

## 🚀 How to Run It Yourself

1. Clone this repo  
2. Run `npm install`  
3. Run `npx lhci autorun`  
4. Open `/lhci-reports/` to view the audit results

---

🔧 Built using:
- Node.js
- Lighthouse CI
