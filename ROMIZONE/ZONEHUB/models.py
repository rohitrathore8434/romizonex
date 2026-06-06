from django.db import models

# Create your models here.
class REGISTERX(models.Model):
    full_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=8)


class EmailForm(models.Model):
    email=models.EmailField()
    otp=models.CharField(max_length=6)

    def __str__(self):
        return self.email+" "+self.otp     
# ---------------------------------Home--------------------------------------------

class h_todaydeals(models.Model):
  image=models.ImageField(upload_to="photos/")
  name=models.CharField(max_length=50)
  price=models.CharField(max_length=200)
  link = models.URLField()

  def __str__(self):
      return self.name
  
class h_toppicks(models.Model):
  image=models.ImageField(upload_to="photos/")
  name=models.CharField(max_length=50)
  price=models.CharField(max_length=200)
  link = models.URLField()

  def __str__(self):
      return self.name
  
class h_blogs(models.Model):
  image=models.ImageField(upload_to="photos/")
  title=models.CharField(max_length=50)
  cetegory=models.CharField(max_length=30 ,default=1)
  
  def __str__(self):
      return self.title
# -------------------------------------Deal------------------------------------------
class deal_all(models.Model):
  badge=models.CharField(max_length=10,default=1)
  image=models.ImageField(upload_to="photos/")
  name=models.CharField(max_length=55)
  price=models.IntegerField()
  discount=models.CharField(max_length=200)
  link = models.URLField()

  def __str__(self):
      return self.name
  
class d_electronic(models.Model):
  badge=models.CharField(max_length=10,default=1)
  image=models.ImageField(upload_to="photos/")
  name=models.CharField(max_length=55)
  price=models.IntegerField()
  discount=models.CharField(max_length=200)
  link = models.URLField()

  def __str__(self):
      return self.name  

class d_fitness(models.Model):
  badge=models.CharField(max_length=10,default=1)  
  image=models.ImageField(upload_to="photos/")
  name=models.CharField(max_length=55)
  price=models.IntegerField()
  discount=models.CharField(max_length=200)
  link = models.URLField()

  def __str__(self):
      return self.name


class d_fashion(models.Model):
  badge=models.CharField(max_length=10,default=1)  
  image=models.ImageField(upload_to="photos/")
  name=models.CharField(max_length=55)
  price=models.IntegerField()
  discount=models.CharField(max_length=200)
  link = models.URLField()

  def __str__(self):
      return self.name

class d_mobile(models.Model):
  badge=models.CharField(max_length=10,default=1)  
  image=models.ImageField(upload_to="photos/")
  name=models.CharField(max_length=55)
  price=models.IntegerField()
  discount=models.CharField(max_length=200)
  link = models.URLField()

  def __str__(self):
      return self.name
  
  
class d_beauty(models.Model):
  badge=models.CharField(max_length=10,default=1)  
  image=models.ImageField(upload_to="photos/")
  name=models.CharField(max_length=55)
  price=models.IntegerField()
  discount=models.CharField(max_length=200)
  link = models.URLField()

  def __str__(self):
      return self.name



class d_food(models.Model):
  badge=models.CharField(max_length=10,default=1)  
  image=models.ImageField(upload_to="photos/")
  name=models.CharField(max_length=55)
  price=models.IntegerField()
  discount=models.CharField(max_length=200)
  link = models.URLField()

  def __str__(self):
      return self.name



class d_kitchen(models.Model):
  badge=models.CharField(max_length=10,default=1)  
  image=models.ImageField(upload_to="photos/")
  name=models.CharField(max_length=55)
  price=models.IntegerField()
  discount=models.CharField(max_length=200)
  link = models.URLField()

  def __str__(self):
      return self.name



class d_toys(models.Model):
  badge=models.CharField(max_length=10,default=1)  
  image=models.ImageField(upload_to="photos/")
  name=models.CharField(max_length=55)
  price=models.IntegerField()
  discount=models.CharField(max_length=200)
  link = models.URLField()

  def __str__(self):
      return self.name



class d_furniture(models.Model):
  badge=models.CharField(max_length=10,default=1)  
  image=models.ImageField(upload_to="photos/")
  name=models.CharField(max_length=55)
  price=models.IntegerField()
  discount=models.CharField(max_length=200)
  link = models.URLField()

  def __str__(self):
      return self.name



class d_appliances(models.Model):
  badge=models.CharField(max_length=10,default=1)  
  image=models.ImageField(upload_to="photos/")
  name=models.CharField(max_length=55)
  price=models.IntegerField()
  discount=models.CharField(max_length=200)
  link = models.URLField()

  def __str__(self):
      return self.name




# -------------------------------BLOG-----------------------------------------
class all_fitness(models.Model):
  image=models.ImageField(upload_to="photos/")
  title=models.CharField(max_length=65)
  decription=models.CharField(max_length=55)
  text=models.TextField(default="No description")
  
  def __str__(self):
      return self.title
  
class all_funny(models.Model):
  image=models.ImageField(upload_to="photos/")
  title=models.CharField(max_length=65)
  decription=models.CharField(max_length=55)
  text=models.TextField(default="No description")
  
  def __str__(self):
      return self.title  
  
class all_news(models.Model):
  image=models.ImageField(upload_to="photos/")
  title=models.CharField(max_length=65)
  decription=models.CharField(max_length=55)
  text=models.TextField(default="No description")
  
  def __str__(self):
      return self.title  
  
class b_fitness(models.Model):
  image=models.ImageField(upload_to="photos/")
  title=models.CharField(max_length=65)
  decription=models.CharField(max_length=55)
  text=models.TextField(default="No description")
  
  def __str__(self):
      return self.title

class b_funny(models.Model):
  image=models.ImageField(upload_to="photos/")
  title=models.CharField(max_length=52)
  decription=models.CharField(max_length=55)
  text=models.TextField(default="No description")
  
  def __str__(self):
      return self.title

class b_news(models.Model):
  image=models.ImageField(upload_to="photos/")
  title=models.CharField(max_length=65)
  decription=models.CharField(max_length=55)
  text=models.TextField(default="No description")
  
  def __str__(self):
      return self.title
# -----------------------------------------deal----------------------------------
class d_pickup_x1(models.Model):
  off=models.CharField(max_length=30)
  image=models.ImageField(upload_to="photos/")
  name=models.CharField(max_length=57)
  decription=models.CharField(max_length=35)
  price=models.CharField(max_length=200)
  oldprice=models.CharField(max_length=200)
  link = models.URLField()

  def __str__(self):
      return self.name