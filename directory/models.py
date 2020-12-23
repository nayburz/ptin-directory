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
    first_name = models.CharField(
        max_length=255, help_text="Enter your first name or first initial.")
    last_name = models.CharField(
        max_length=255, help_text="Enter your last name.")
    middle_name = models.CharField(
        max_length=255, blank=True, help_text="Enter your middle name or intial.")
    dba = models.CharField(
        max_length=255, blank=True, help_text="Doing Business As")
    website_url = models.URLField(
        max_length=255, blank=True, help_text="Enter your website or link for letting clients get in touch")
    email = models.EmailField(max_length=64, null=True,
                              help_text="Enter your first name or first initial.")
    display_email_on_profile = models.BooleanField(default=False, help_text="Check if you would like your email displayed on your directory page")
    # photo_main = models.ImageField(
    #     blank=True, upload_to='uploads/photos/%Y/%m/%d/', help_text="An image should be at least 300 pixels in size. It is recommended you use a company logo or professional head-shot photo.")
    street = models.CharField(
        max_length=255, blank=True, help_text="Enter your street address.")
    city = models.CharField(
        max_length=255, blank=True, help_text="Enter your city.")

    # TODO Locations:
    # country = 
    # state = models.CharField(choices=sorted(
    #     statenames.items()), max_length=2, blank=True, db_index=True)
    # zipcode = 
    # TODO Need to fix, not working. Use another package?
    # phone_number = PhoneNumberField(blank=True)
    summary = models.CharField(
        max_length=255, blank=True, help_text="One or two lines for that will be displayed in the main directory (maximum of 180 characters). Upgrading to an Enhanced entry will let you also add a much larger description.")
    description = models.TextField(blank=True, null=True, help_text="Please write a fuller description about your, your firm and the services you offer.")
    featured = models.BooleanField(default=False)

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
        return f'{self.last_name}, {self.first_name} // {self.email}'

    # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        """Returns the url to access a particular detail listing page."""
        return reverse('directory:listing_detail', args=[str(self.id)])

    # OTHER METHODS
    def full_name(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'

    def full_address(self):
        """String for representing the Model object."""
        return f'{self.street}, {self.city}'

    def city_state(self):
        """String for representing the Model object."""
        return f'{self.city}, {self.state}'

    def url_text(self):
        parsed_url = urlparse(self.website)
        return parsed_url.hostname.replace("www.", "")
