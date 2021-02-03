describe("Favourite Icon tests", () => {
    let form;
    beforeEach(() => {
        form = $(`
        <input type="checkbox" class="heart-box"
        id="favourite"></input>`);
        $(document.body).append(form);
    });

    afterEach(() => {
        form.remove();
        form = null;
    });

    it("should bind favourite icon to event listener", () => {
        const favIcon = document.getElementById("favourite");
        const eventSpy = spyOn(favIcon, "addEventListener");
        bindFavourite();
        expect(eventSpy).toHaveBeenCalledWith("change", jasmine.any(Function));
    });

    /*Could not test the window.location.pathname string manipulation, cannot
    spy on window.location or edit values. */
    it("should invoke togglefavourites via ajax when clicked", () => {
        const favIcon = document.getElementById("favourite");
        const eventSpy = spyOn(favIcon, "addEventListener");
        bindFavourite();
        const ajaxSpy = spyOn($, "ajax");
        eventSpy.calls.mostRecent().args[1]();
        expect(ajaxSpy).toHaveBeenCalledWith({
            type: "POST",
            url: '/toggle_favourite',
            data: {
                id: `/testing`,
                checkbox: false
            }
        });
    });
});