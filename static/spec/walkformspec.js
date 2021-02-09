describe("Image Loading tests", () => {
    let form;
    beforeEach(() => {
        form = $(`
            <input id="imageUrl" value="https://valid-url/test"></input>       
            <div class="image-container"><img src="data:," alt="Image preview"
            id="imgContainer"></div>`);
        $(document.body).append(form);
    });

    afterEach(() => {
        form.remove();
        form = null;
    });

    it("should change the src to a new value when changed", () => {
        bindUrlEvent();
        let imgContainer = document.getElementById("imgContainer");
        let input = document.getElementById("imageUrl");
        const event = new Event('change');
        input.dispatchEvent(event);
        expect(imgContainer.src).toBe("https://valid-url/test");
    });

    it("should add show-image class to the img container div", () => {
        bindUrlEvent()
        let containerDiv = document.getElementsByClassName("image-container");
        let input = document.getElementById("imageUrl");
        const event = new Event('change');
        input.dispatchEvent(event);
        expect(containerDiv[0].classList.contains("show-image")).toBe(true);
    });
    
    it("should not addshow-image class to the img container div if no change",
        () => {
        bindUrlEvent()
        let containerDiv = document.getElementsByClassName("image-container");
        let input = document.getElementById("imageUrl");
        expect(containerDiv[0].classList.contains("show-image")).toBe(false);
    });

});