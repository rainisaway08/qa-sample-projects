<<<<<<< HEAD
import { test, expect } from '@playwright/test';

test('CNN homepage loads and shows search icon', async ({ page }) => {
  await page.goto('https://edition.cnn.com', { waitUntil: 'domcontentloaded' });

  // Confirm page title contains 'CNN'
  await expect(page).toHaveTitle(/CNN/);

  // Locate and click the search icon button
  const searchButton = page.locator('button[aria-label="Search Icon"]');
  await expect(searchButton).toBeVisible({ timeout: 10000 });
  await searchButton.click();

  // ✅ Only use the first matching input (header search bar)
  const searchInput = page.locator('.search-bar input[placeholder="Search CNN..."]').first();
  await expect(searchInput).toBeVisible({ timeout: 10000 });
});
=======
import { test, expect } from '@playwright/test';

test('CNN homepage loads and shows search icon', async ({ page }) => {
  await page.goto('https://edition.cnn.com', { waitUntil: 'domcontentloaded' });

  // Confirm page title contains 'CNN'
  await expect(page).toHaveTitle(/CNN/);

  // Locate and click the search icon button
  const searchButton = page.locator('button[aria-label="Search Icon"]');
  await expect(searchButton).toBeVisible({ timeout: 10000 });
  await searchButton.click();

  // ✅ Only use the first matching input (header search bar)
  const searchInput = page.locator('.search-bar input[placeholder="Search CNN..."]').first();
  await expect(searchInput).toBeVisible({ timeout: 10000 });
});
>>>>>>> 6280e04a4f0946375b5ebe64c2d8a94068982869
