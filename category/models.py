from django.db import models 

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Category') 
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subcategories', null=True, blank=True)  
    slug = models.SlugField(unique=True, blank=True)

    def get_full_path(self):
        if self.parent_category:
            return f'{self.parent_category.get_full_path()} > {self.name}'
        return self.name 
    
    def __str__(self):
        return self.name