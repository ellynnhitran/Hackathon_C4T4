from mongoengine import *

class Food(Document):
  title = StringField(max_length=200)
  img = StringField()
  nguyenlieu = StringField()
  cachlam = StringField()
  dish = StringField()

class User(Document):
  username = StringField(max_length=50)
  password = StringField()
  favorite = ListField(ReferenceField(Food,reverse_delete_rule=CASCADE))