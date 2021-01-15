describe("User Profile tests", () => {
    let form;
    beforeEach(() => {
        form = $(`        
        <div class="row">
            <div class="scrolling-wrapper col-12" id="favScroll">
                <div id="sized-div">Hi</div>
            </div>
            <button class="left-scroll col-1" id="leftScroll">
                <i class="fas fa-angle-left"></i>
            </button>
            <button class="right-scroll col-1" id="rightScroll">
                <i class="fas fa-angle-right"></i>
            </button>
        </div>`)
        $(document.body).append(form);
    })

    afterEach(() => {
        form.remove();
        form=null;
    })

    it("should hide buttons and center when scrollwidth and width match", () => {
        const leftScroll = document.getElementById("leftScroll");
        const rightScroll = document.getElementById("rightScroll");
        const scrollArea = document.getElementById("favScroll");
        setScrollState()
        expect(leftScroll.style.visibility).toEqual('hidden');
        expect(rightScroll.style.visibility).toEqual('hidden');
        expect(scrollArea.classList).toContain('justify-content-center');
    })
    
    it("should not hide buttons or center when scrollwidth > clientwidth", () => {
        const leftScroll = document.getElementById("leftScroll");
        const rightScroll = document.getElementById("rightScroll");
        const scrollArea = document.getElementById("favScroll");
        const sizedDiv = document.getElementById("sized-div");
        sizedDiv.style.minWidth = "5000px";
        setScrollState()
        expect(leftScroll.style.visibility).not.toEqual('hidden');
        expect(rightScroll.style.visibility).not.toEqual('hidden');
        expect(scrollArea.classList).not.toContain('justify-content-center');
    })

    it("should change the value of scrollLeft when leftButton clicked", () => {
        const leftScroll = document.getElementById("leftScroll");
        const scrollArea = document.getElementById("favScroll");
        const sizedDiv = document.getElementById("sized-div");
        sizedDiv.style.minWidth = "5000px";
        scrollArea.style.overflow = "scroll";
        scrollArea.style.maxWidth = "800px";
        scrollArea.style.scrollBehavior="auto"
        scrollArea.scrollLeft = 500;
        setScrollState();
        leftScroll.click();
        expect(scrollArea.scrollLeft).toEqual(180);
    })

    it("should change the value of scrollLeft when rightButton clicked", () => {
        const leftScroll = document.getElementById("leftScroll");
        const scrollArea = document.getElementById("favScroll");
        const sizedDiv = document.getElementById("sized-div");
        sizedDiv.style.minWidth = "5000px";
        scrollArea.style.overflow = "scroll";
        scrollArea.style.maxWidth = "800px";
        scrollArea.style.scrollBehavior="auto"
        setScrollState();
        rightScroll.click();
        expect(scrollArea.scrollLeft).toEqual(320);
    })
})