function validateForm() {
    //First Name checks
    var fname = document.forms["reg"]["reg-fname"].value;
    if (fname.length < 2){
        alert("First Name must be at least 2 characters!");
        return false;
    }
    if (/[^a-zA-Z]+$/.test(fname)) {
        alert("First Name must be only letters!");
        return false;
    }

    //Last Name checks
    var lname = document.forms["reg"]["reg-lname"].value;
    if (lname.length < 2){
        alert("Last Name must be at least 2 characters!");
        return false;
    }
    if (/[^a-zA-Z]+$/.test(lname)) {
        alert("Last Name must be only letters!");
        return false;
    }

    //Email check
    var email = document.forms["reg"]["reg-email"].value;
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        alert("Please enter a valid email address! \n Example: joe.smith@email.com");
        return false;
    }

    //Password checks
    var pword = document.forms["reg"]["reg-password"].value;
    if (pword.length < 8){
        alert("Password must be at least 8 characters!");
        return false;
    }
    if (pword != document.forms["reg"]["conf-password"].value){
        alert("Passwords DO NOT match!");
        return false;
    }
}