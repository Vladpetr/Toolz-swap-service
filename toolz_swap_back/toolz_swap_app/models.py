from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# TODO: Figure out ManyToMany field in User (see comment near saved_places)
# TODO: make nitty-gritty changes like null=True, blank=True, max_length=number, on_delete=SET_NULL/CASCADE/RESTRICT and others
# TODO: added choices of 1 to 5 for Rating in ListinsReviews

'''
OLD MODELS. SAVED TEMPORARILY FOR IMMEDIATE REFERENCE

class Tool(models.Model):
    toolId = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, help_text='Unique ID for this particular tool')
    toolName = models.CharField(max_length=200)
    toolBrand = models.CharField(max_length=200, null=True, blank=True)
    toolModel = models.CharField(max_length=200, null=True, blank=True)
    toolCondition = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "<ID: {} - Name:{} - Brand:{} - Model:{}>".format(self.toolId, self.toolName, self.toolBrand, self.toolModel)

class Swaps(models.Model):
    #swaps_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, help_text='Unique ID for this particular swap')
    borrowerId =  models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    listingId = models.ForeignKey(
        Listing, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    expires = models.DateTimeField()

    def __str__(self):
        return "<borrowerId: {} - listingId: {}>".format(self.borrowerId, self.listingId)

'''
class Cities(models.Model):
    city_id=models.UUIDField(primary_key=True)
    name=models.CharField()
    country=models.CharField() # suggest to be UUIDField but I think CharField makes more sense
    population=models.IntegerField()
    size_sqkm=models.FloatField()

class Neighborhoods(models.Model):
    neighborhood_id=models.UUIDField(primary_key=True)
    name=models.CharField()
    city=models.ForeignKey(Cities, on_delete=models.CASCADE)
    population=models.IntegerField()
    size_sqkm=models.FloatField()

class ToolTypes(models.Model):
    tool_id=models.UUIDField(primary_key=True)
    name=models.CharField()
    purpose=models.TextField()
    popularity=models.CharField()

class Brands(models.Model):
    brand_id=models.UUIDField(primary_key=True)
    name=models.CharField()
    #price_range=models.CharField()
    logo=models.ImageField()

class Models(models.Model):
    model_id=models.UUIDField(primary_key=True)
    name=models.CharField()
    #price_range=models.CharField()
    year_released=models.IntegerField()
    

class User(AbstractUser):
    username = models.CharField(max_length=40, unique=True)
    USERNAME_FIELD = 'username'

    #user_id = models.UUIDField(primary_key=True)
    #first_name=models.CharField() 
    # first_name, last_name, password, and email are default fields in Django User model.

    phone=models.CharField() # I left it as CharField for now but def. needs to be changed
    address=models.CharField()
    city=models.ForeignKey(Cities, on_delete=models.CASCADE)

    # There is a problem that we need to define Listings be User to be able to define the below
    # However, we also need to define User before Listing. I am sure there is a workaround though
    #saved_places=models.ManyToManyField(Listings)
    #rented_tools=models.ManyToManyField(Listings)
    profile_photo=models.ImageField()
    bio=models.CharField()
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<username:{self.username}, \
                first_name:{self.first_name},\
                last_name:{self.last_name}, \
                email:{self.email};"

class Listings(models.Model):
    # default=uuid.uuid4
    listing_id = models.UUIDField(primary_key=True, unique=True, help_text='Unique ID for this particular listing')
    title = models.CharField(max_length=200)
    owner =  models.ForeignKey(
        User, on_delete=models.RESTRICT, null=True)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    model = models.ForeignKey(Models, on_delete=models.CASCADE)
    tool_category=models.ForeignKey(ToolTypes, on_delete=models.CASCADE)
    address=models.CharField()
    city=models.ForeignKey(Cities, on_delete=models.CASCADE)
    neighborhood=models.ForeignKey(Neighborhoods, on_delete=models.CASCADE)
    description=models.TextField(max_length=2000)
    created_on=models.DateTimeField(auto_now_add=True)

    # I think it'd make more sense to use Rating (1-5) instead of Likes/Dislikes
    rating_average = models.FloatField()
    #likes=models.IntegerField()
    #dislikes=models.IntegerField()

    def __str__(self):
        return f"<listing_id:{self.listing_id}, title:{self.title};"

class ListingRequest(models.Model):
    request_id=models.UUIDField(primary_key=True)
    listing=models.ForeignKey(Listings, on_delete=models.CASCADE)
    created_on=models.DateTimeField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    recipient=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()

    # I guess with a CharField we'd have to parse it?
    # perhaps better to use two DateFields: renting_start and renting_end?
    #dates_requested=models.CharField() 
    renting_start = models.DateTimeField(auto_now_add=True)
    renting_end = models.DateTimeField()

    approved = models.BooleanField()

class ListingReviews(models.Model):
    review_id=models.UUIDField(primary_key=True)
    listing=models.ForeignKey(Listings, on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()

    top_review=models.BooleanField()
    rating = models.IntegerField() # maybe add allowed integers later
    #likes=models.IntegerField()
    #dislikes=models.IntegerField()

class ListingImages(models.Model):
    image_id=models.UUIDField(primary_key=True)
    listing=models.ForeignKey(Listings, on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField()
    top_image=models.BooleanField()

