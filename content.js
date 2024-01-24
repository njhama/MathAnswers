// content.js
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "getInnerHTML") {
        const element = document.querySelector('h4.h1pyel1o');
        const innerHTML = element ? element.innerHTML : "test";
        sendResponse({ innerHTML });
    }
});
