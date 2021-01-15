describe("Base Navbar tests", () => {
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
    
})