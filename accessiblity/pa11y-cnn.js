const pa11y = require('pa11y');

(async () => {
  const results = await pa11y('https://www.cnn.com', {
    browserLaunchOptions: {
      executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe'
    }
  });

  console.log(results.issues);
})();
