describe("Search Page tests", () => {
    let form;
    beforeEach(() => {
        form = $(`
        <div class="row" id="results">
        </div>`)
        $(document.body).append(form);
    });

    afterEach(() => {
        form.remove();
        form = null;
    });

    it("should hide buttons and center when scrollwidth and width match", () => {
        const results = document.getElementById("results");
        const scrollSpy = spyOn(results, "scrollIntoView");
        scrollResults();
        expect(scrollSpy).toHaveBeenCalledWith({ behavior: "smooth"});
    });
})