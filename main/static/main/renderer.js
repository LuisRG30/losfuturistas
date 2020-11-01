var url = "/media/";
url += "edit1.pdf";
console.log(url);

var loadingTask = pdfjsLib.getDocument(url)
loadingTask.promise.then(function(pdf) {
    pdf.getPage(1).then(page => {
        var myCanvas = document.getElementById('my-canvas');
        var context = myCanvas.getContext('2d');

        var viewport = page.getViewport({scale: 1}); 
        myCanvas.width = viewport.width;
        myCanvas.height = viewport.height;

        var renderContext = {
            canvasContext: context,
            viewport: viewport
        };
        page.render(renderContext);
    });
});

