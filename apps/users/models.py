from django.db import models

class UserManager(models.Manager):
    def validator(self, postData, pageType, userEmail):
        errors = {}

        if pageType == 'registration':  #Registration Checks
            
            checkEmail = User.objects.filter(email=postData['reg-email'])
            if checkEmail:
                errors['reg-email'] = "A user with this email is already registered. Please enter a different email."

        elif pageType == 'login': #Login Checks

            checkUser = User.objects.filter(email=postData['log-email'], password=postData['log-pword'])
            if (len(checkUser) < 1):
                #If there is no match, we return to the reg/login page with an error message, as stated below
                errors['log-invalid'] = "The email and password combination entered do not match a record in our database"
        
        elif pageType == 'update': #Update Page Checks
            
            if (postData['email'] != userEmail):
                checkEmail = User.objects.filter(email=postData['email'])
                if checkEmail:
                    errors['email'] = "A user with this email is already registered. Please enter a different email."

        return errors


class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()