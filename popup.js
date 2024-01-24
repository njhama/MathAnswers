document.addEventListener('DOMContentLoaded', function () {
    var screenshotButton = document.getElementById('screenshot');
    if (screenshotButton) {
        screenshotButton.addEventListener('click', function () {
            chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
                chrome.tabs.captureVisibleTab(null, { format: 'png' }, function (dataUrl) {
                    const timestamp = new Date().getTime();
                    const folderName = 'MyScreenshots';
                    const filename = `${folderName}/screenshot-${timestamp}.png`;

                    chrome.downloads.download({
                        url: dataUrl,
                        filename: filename,
                        saveAs: false
                    });
                });
            });
        });
    }

    var startActionButton = document.getElementById('startAction');
    if (startActionButton) {
        startActionButton.addEventListener('click', function() {
            chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
                chrome.tabs.sendMessage(tabs[0].id, {action: "startAction"});
            });
        });
    }
});
