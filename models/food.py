from mongoengine import *

class Food(Document):
  title = StringField(max_length=200)
  img = StringField()
  nguyenlieu = StringField()
  cachlam = StringField()
  dish = StringField()
  season = StringField()
  checked = BooleanField()
  author = StringField()

class Users(Document):
  email = StringField(max_length=50)
  password = StringField()
  first_name = StringField()
  last_name = StringField()
  posted = ListField(ReferenceField(Food,reverse_delete_rule=CASCADE, dbref=False))
  favorite = ListField(ReferenceField(Food,reverse_delete_rule=CASCADE, dbref=False))