describe("User Profile tests", () => {
    let form;
    var originalTimeout;
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
                data-info="/delete_walk/5fd8ca1b500712aacd3b2fa3">
                Delete Walk
            </button>
        </div>        
        <div class="modal custom fade" tabindex="-1" role="dialog" id="deleteConfirm"
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

        originalTimeout = jasmine.DEFAULT_TIMEOUT_INTERVAL;
        jasmine.DEFAULT_TIMEOUT_INTERVAL = 10000;
    });

    afterEach(() => {
        form.remove();
        form = null;
        jasmine.DEFAULT_TIMEOUT_INTERVAL = originalTimeout;
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
        const cancel = document.getElementById("cancel");
        confirm_delete();
        var POLL_TIME = 20;
        var endTime = new Date().getTime() + 5000;

        var checkCondition = function() {
            if (new Date().getTime() <= endTime && confirmModal.classList.contains("show")) {
                setTimeout(checkCondition, POLL_TIME);
            } else {
                expect(confirmModal).toContain("show");
                cancel.click();
            }
        };
        checkCondition();

    })
})