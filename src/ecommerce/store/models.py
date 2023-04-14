from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#customer 

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


#product

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()    
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
        
    
    

#Order

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping
         
         
         
#order item 

class OrderItem(models.Model):
    product = models.ForeignKey(Product ,on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order , on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
    
#shiping address

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer ,on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order , on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    Country = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    telephone = models.IntegerField(null=True)
    date_added = models.DateField(auto_now_add=False)
    
    def __str__(self):
        return self.address
    
    
    
    