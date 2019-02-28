function validateForm() {
    //First Name checks
    var fname = document.forms["reg"]["reg-fname"].value;
    if (fname.length < 2){
        swal("", "First Name must be at least 2 characters!", "warning");
        return false;
    }
    if (/[^a-zA-Z]+$/.test(fname)) {
        swal("", "First Name must be only letters!", "warning");
        return false;
    }

    //Last Name checks
    var lname = document.forms["reg"]["reg-lname"].value;
    if (lname.length < 2){
        swal("", "Last Name must be at least 2 characters!", "warning");
        return false;
    }
    if (/[^a-zA-Z]+$/.test(lname)) {
        swal("", "Last Name must be only letters!", "warning");
        return false;
    }

    //Email check
    var email = document.forms["reg"]["reg-email"].value;
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        swal("", "Please enter a valid email address! \n Example: joe.smith@email.com", "warning");
        return false;
    }

    //Password checks
    var pword = document.forms["reg"]["reg-password"].value;
    if (pword.length < 8){
        swal("", "Password must be at least 8 characters!", "warning");
        return false;
    }
    if (pword != document.forms["reg"]["conf-password"].value){
        swal("", "Passwords DO NOT match!", "warning");
        return false;
    }
}