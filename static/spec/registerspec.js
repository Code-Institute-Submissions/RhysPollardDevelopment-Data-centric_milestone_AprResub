describe("Register Page tests", () => {
    let form;
    beforeEach(() => {
        form = $(`        
            <div class="form-group">
                <label for="password" id="passwordLabel">Password</label>
                <input aria-describedby="passwordLabel" class="form-control" 
                id="password" minlength="10" name="password" 
                placeholder="Password" required="" type="password" value="">
                <small id="passwordHelp" class="form-text text-muted">
                Password must be at least 10 characters long.</small>
            </div>
            <div class="form-group">
                <label for="confirm_password" id="confirmLabel">
                Repeat Password</label>
                <input aria-describedby="confirmLabel" class="form-control" 
                id="confirm_password" name="confirm_password" 
                placeholder="Confirm Password" required="" 
                type="password" value="">
                <div class="invalid-feedback">
                    <p>Passwords do not match!</p>
                </div>
            </div>`)
        $(document.body).append(form);
        setupToggle()
    })

    afterEach(() => {
        form.remove();
        form=null;
    })

    it("should validate password match on keyup", () => {
        addPasswordEvents();
        const password = $("#password");
        const confirmPassword = $("#confirm_password");
        confirmPassword[0].setCustomValidity("Test");
        console.log(confirmPassword[0].validationMessage);
        password[0].value = "a";
        confirmPassword[0].value = "a";
        password[0].dispatchEvent(new KeyboardEvent('keyup',{'key':'a'}));
        expect(confirmPassword[0].validationMessage).toEqual("");
    })

    it("should validate password does not match on keyup", () => {
        addPasswordEvents();
        const password = $("#password");
        const confirmPassword = $("#confirm_password");
        confirmPassword[0].setCustomValidity("Test");
        console.log(confirmPassword[0].validationMessage);
        password[0].value = "a";
        password[0].dispatchEvent(new KeyboardEvent('keyup',{'key':'a'}));
        expect(confirmPassword[0].validationMessage).toEqual("Passwords do not match!");
    })
    
    it("should validate confirm_password match on keyup", () => {
        addPasswordEvents();
        const password = $("#password");
        const confirmPassword = $("#confirm_password");
        confirmPassword[0].setCustomValidity("Test");
        console.log(confirmPassword[0].validationMessage);
        password[0].value = "a";
        confirmPassword[0].value = "a";
        confirmPassword[0].dispatchEvent(new KeyboardEvent('keyup',{'key':'a'}));
        expect(confirmPassword[0].validationMessage).toEqual("");
    })
    
    it("should validate confirm_password does not match on keyup", () => { 
        addPasswordEvents();
        const password = $("#password");
        const confirmPassword = $("#confirm_password");
        confirmPassword[0].setCustomValidity("Test");
        console.log(confirmPassword[0].validationMessage);
        confirmPassword[0].value = "a";
        confirmPassword[0].dispatchEvent(new KeyboardEvent('keyup',{'key':'a'}));
        expect(confirmPassword[0].validationMessage).toEqual("Passwords do not match!");
    })
    
})