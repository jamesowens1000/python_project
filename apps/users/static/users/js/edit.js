function validateForm() {
    //First Name checks
    var fname = document.forms["upd"]["upd-fname"].value;
    if (fname.length < 2){
        swal("", "First Name must be at least 2 characters!", "warning");
        return false;
    }
    if (/[^a-zA-Z]+$/.test(fname)) {
        swal("", "First Name must be only letters!", "warning");
        return false;
    }

    //Last Name checks
    var lname = document.forms["upd"]["upd-lname"].value;
    if (lname.length < 2) {
        swal("", "Last Name must be at least 2 characters!", "warning");
        return false;
    }
    if (/[^a-zA-Z]+$/.test(lname)) {
        swal("", "Last Name must be only letters!", "warning");
        return false;
    }

    //Zip Code check
    var zip = document.forms["upd"]["upd-zip"].value;
    if (zip.length > 0){
        if (!/^\d{5}$/.test(phone)) {
            if (zip.length < 5) {
                swal("", "Please enter 5 digits for the zip code!", "warning");
                return false;
            }
        }
    }

    //Phone Number check
    var phone = document.forms["upd"]["upd-phone"].value;
    if (phone.length > 0){
        if (!/^\(?([0-9]{3})\)?[-]?([0-9]{3})[-]?([0-9]{4})$/.test(phone)) {
            swal("", "Please enter a valid phone number! \n Example: 123-456-7890", "warning");
            return false;
        }
    }

    //Email check
    var email = document.forms["upd"]["upd-email"].value;
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        swal("", "Please enter a valid email address! \n Example: joe.smith@email.com", "warning");
        return false;
    }

    //Password checks
    var pword = document.forms["upd"]["upd-password"].value;
    if (pword.length > 0){
        if (pword.length < 8){
            swal("", "Password must be at least 8 characters!", "warning");
            return false;
        }
        if (pword != document.forms["upd"]["conf-password"].value){
            swal("", "Passwords DO NOT match!", "warning");
            return false;
        }
    }
}