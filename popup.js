// popup.js
document.addEventListener('DOMContentLoaded', function () {
    var screenshotButton = document.getElementById('screenshot');
    if (screenshotButton) {
        screenshotButton.addEventListener('click', function () {
            // Send a message to the content script to get inner HTML
            chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
                console.log('Sending message to content script'); // Add this line
                chrome.tabs.sendMessage(tabs[0].id, { action: "getInnerHTML" }, function (response) {
                    console.log('Received response from content script'); // Add this line
                    const innerHTML = response ? response.innerHTML : "Element with class 'h1pyello' not found.";
                    const timestamp = new Date().getTime();
                    const folderName = 'MyScreenshots';
                    const filename = `${folderName}/screenshot-${timestamp}.html`;

                    // Create a Blob with the inner HTML content
                    const blob = new Blob([innerHTML], { type: 'text/html' });
                    const blobUrl = URL.createObjectURL(blob);

                    // Download the HTML file
                    chrome.downloads.download({
                        url: blobUrl,
                        filename: filename,
                        saveAs: false
                    });
                });
            });
        });
    }

    // Rest of your code
});
