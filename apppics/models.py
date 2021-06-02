from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=30)
    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()

    def update_category(self, updated_category):
        self.image_category = updated_category
        self.save()



    
class Meta:
    ordering = ['name']




class Location(models.Model):
    image_location = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def get_location_byid(cls, id):
        location = Location.objects.get(pk=id)
        return location

    def update_location(self, updated_pinpoint):
        self.image_location = updated_pinpoint
        self.save()

    class Meta:
        ordering = ['image_location']




class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=300)
    image = CloudinaryField(blank = True, null = True)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    #location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True)

    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_tag(cls, search_word):
        images = cls.objects.filter(category__name__icontains=search_word)
        return images

    @classmethod  
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    def update_image(self,image_name, image_description):
        self.image_name = image_name
        self.image_description = image_description
        self.save()

    @classmethod
    def get_images(cls):
        all_images = cls.objects.all()
        return all_images 

    @classmethod
    def filter_by_location(cls, loc):
        images_loc = cls.objects.filter(location__id=loc)
        return images_loc


#
