describe("User Profile tests", () => {
    let form;
    const hrefInfo = "/delete_walk/5fd8ca1b500712aacd3b2fa3";
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
        </div>        
        <div class="user-input row">
            <a href="{{ url_for('edit_walk',route_id=route._id) }}"
                class="button clear col-sm-6">Edit Walk</a>
            <button class="button delete col-sm-6" data-toggle="modal"
                data-info="${hrefInfo}" id="openModal">
                Delete Walk
            </button>
        </div>        
        <div class="modal custom" tabindex="-1" role="dialog" id="deleteConfirm"
            aria-labelledby="mySmallModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-sm">
                <div class="modal-content">
                    <div class="modal-body custom">
                        <h4 class="modal-title custom">
                            Delete this walk?
                        </h4>
                        <button class="button cancel" id="cancel"> Cancel
                        </button>
                        <button class="button confirm" id="confirm">
                            Confirm
                        </button>
                    </div>
                </div>
            </div>
        </div>`)
        $(document.body).append(form);
    });

    afterEach(() => {
        form.remove();
        form = null;
    });

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
        const rightScroll = document.getElementById("rightScroll");
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

    it("should open a modal on clicking the delete walk", () => {
        const confirmModal = document.getElementById("deleteConfirm");
        confirm_delete();
        expect(confirmModal.classList).toContain("show");
        // hide the modal
        $(confirmModal).modal("hide");
    })

    it("should call confirm delete with url when clicked", () => {
        const confirmSpy = spyOn(window, "confirm_delete")
        const confirmModal = document.getElementById("deleteConfirm");
        const openModal = document.getElementById("openModal");
        bindEvents();
        openModal.click();
        expect(confirmSpy).toHaveBeenCalledWith(hrefInfo)
        $(confirmModal).modal("hide");
        confirmSpy.and.callThrough();
    })

    it("should close the modal when cancel is clicked", () => {
        const cancel = document.getElementById("cancel");
        const confirmModal = document.getElementById("deleteConfirm");
        const openModal = document.getElementById("openModal");
        bindEvents();
        confirm_delete();
        cancel.click();
        expect(openModal.classList).not.toContain("show");
    })



})