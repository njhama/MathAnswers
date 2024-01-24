chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === "startAction") {
        const targetButtonSelector = 'button.myTargetButton';
        const targetButton = document.querySelector(targetButtonSelector);
        if (targetButton) {
            targetButton.click();
            console.log('Button clicked!');
        } else {
            console.log('Target button not found.');
        }
    }
});
