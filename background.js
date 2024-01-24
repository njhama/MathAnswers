chrome.action.onClicked.addListener((tab) => {
    chrome.scripting.executeScript({
        target: { tabId: tab.id },
        function: captureFullPage
    });
});

function captureFullPage() {
    const scrollBy = window.innerHeight;
    const maxHeight = document.body.scrollHeight;
    let scrollTop = 0;

    const captureAndScroll = () => {
        chrome.tabs.captureVisibleTab(null, {format: 'png'}, (dataUrl) => {
            // You would need to send this dataUrl to your background script or a server
            // where you can stitch the images together.
            console.log('Captured dataUrl:', dataUrl);

            scrollTop += scrollBy;
            if (scrollTop < maxHeight) {
                window.scrollTo(0, scrollTop);
                setTimeout(captureAndScroll, 300);
            } else {
                console.log('Reached end of page');
                
            }
        });
    };

    captureAndScroll();
}

