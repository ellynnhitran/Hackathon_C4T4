from mongoengine import Document, StringField

class Food(Document):
  title = StringField(max_length=200)
  img = StringField()
  nguyenlieu = StringField()
  cachlam = StringField()