const { test, expect } = require('@playwright/test');

test('Wikipedia homepage search test', async ({ page }) => {
  await page.goto('https://www.wikipedia.org');
  await expect(page.locator('#searchInput')).toBeVisible();
  await page.fill('#searchInput', 'Quality Assurance');
  await page.press('#searchInput', 'Enter');
  await expect(page).toHaveURL(/.*Quality_Assurance.*/);
});
