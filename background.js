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

