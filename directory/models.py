from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
# from states import statenames
from django.shortcuts import reverse
from urllib.parse import urlparse









class Person(models.Model):



    # CHOICES
    #
    #
    #
    #

    # DATABASE FIELDS
    last_name = models.CharField(
        max_length=255, help_text="Enter your last name.")
    first_name = models.CharField(
        max_length=255, help_text="Enter your first name or first initial.")
    address = models.CharField(
        max_length=255, blank=True, help_text="Enter your street address.")
    city = models.CharField(
        max_length=255, blank=True, help_text="Enter your city.")
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=50)
    website = models.URLField(
        max_length=255, blank=True, help_text="Enter your website or link for letting clients get in touch")
    profession = models.CharField(max_length=50, blank=True)

    # slug
    slug = models.SlugField(null=True, unique=True, blank=True)
    
    # TODO Locations:
    # country = 
    # state = models.CharField(choices=sorted(
    #     statenames.items()), max_length=2, blank=True, db_index=True)
    
    # TODO Need to fix, not working. Use another package?
    # phone_number = PhoneNumberField(blank=True)
    # summary = models.CharField(
    #     max_length=255, blank=True, help_text="One or two lines for that will be displayed in the main directory (maximum of 180 characters). Upgrading to an Enhanced entry will let you also add a much larger description.")
    # description = models.TextField(blank=True, null=True, help_text="Please write a fuller description about your, your firm and the services you offer.")
    # featured = models.BooleanField(default=False)

    # TODO Social Media:
    # facebook = 
    # twitter =
    # LinkedIn = 



    # META CLASS
    class Meta:
        verbose_name = 'listing'
        verbose_name_plural = 'listings'

    class Meta:
        ordering = ['last_name', 'first_name']

    # TO STRING METHOD
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

    # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        """Returns the url to access a particular detail listing page."""
        return reverse('directory:person-detail', args=[str(self.id)])

    # OTHER METHODS
    def full_name(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'


    def full_address(self):
        """String for representing the Model object."""
        return f'{self.address}, {self.city}'

    def city_state(self):
        """String for representing the Model object."""
        return f'{self.city}, {self.state}'
    
    def city_state_zipcode(self):
        """String for representing the Model object."""
        return f'{self.city}, {self.state} {self.zipcode}'

    def url_text(self):
        parsed_url = urlparse(self.website)
        return parsed_url.hostname.replace("www.", "")



