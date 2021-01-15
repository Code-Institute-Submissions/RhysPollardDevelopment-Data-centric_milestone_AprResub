describe("Base Navbar tests", () => {
    let form;
    beforeEach(() => {
        form = $(`        
            <div class="toggler-icon" id="toggler-icon">
                <div class="bar1"></div>
                <div class="bar2"></div>
                <div class="bar3"></div>
            </div>`)
        $(document.body).append(form);
        setupToggle()
    })

    afterEach(() => {
        form.remove();
        form=null;
    })

    it("add the change class on button click", () => {
        const toggledIcon = document.getElementById("toggler-icon");
        toggledIcon.click();
        expect(toggledIcon.classList).toContain("change");
    })
    
})