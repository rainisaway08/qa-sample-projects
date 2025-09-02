<<<<<<< HEAD
const { test, expect } = require('@playwright/test');

test('Wikipedia homepage search test', async ({ page }) => {
  await page.goto('https://www.wikipedia.org');
  await expect(page.locator('#searchInput')).toBeVisible();
  await page.fill('#searchInput', 'Quality Assurance');
  await page.press('#searchInput', 'Enter');
  await expect(page).toHaveURL(/.*Quality_Assurance.*/);
});
=======
const { test, expect } = require('@playwright/test');

test('Wikipedia homepage search test', async ({ page }) => {
  await page.goto('https://www.wikipedia.org');
  await expect(page.locator('#searchInput')).toBeVisible();
  await page.fill('#searchInput', 'Quality Assurance');
  await page.press('#searchInput', 'Enter');
  await expect(page).toHaveURL(/.*Quality_Assurance.*/);
});
>>>>>>> 6280e04a4f0946375b5ebe64c2d8a94068982869
