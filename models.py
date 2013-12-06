# coding: utf-8

from google.appengine.ext import db

class Company(db.Model):
    name = db.StringProperty() #show this in the web app
    address = db.StringProperty() #show this in the web app
    city = db.StringProperty() #show this in the web app
    country = db.StringProperty() #show this in the web app
    email = db.StringProperty() #show this in the web app
    phone_number = db.IntegerProperty()
    datetime = db.DateTimeProperty(auto_now_add=True)

    @property
    def director(self):
        return Director.gql("WHERE companies = :1", self.key()) 

    @property
    def owner(self):
        return Owner.gql("WHERE companies = :1", self.key()) 

def companies_key(companies_name=None):
  """Constructs a Datastore key for a Companies entity with companies_name."""
  return db.Key.from_path('Companies', companies_name or 'default_companies')

class Director(db.Model):
    name = db.StringProperty()
    passport = db.BlobProperty()
    company = db.ReferenceProperty(Company, collection_name = "directors")

class Owner(db.Model):
    name = db.StringProperty()
    passport = db.BlobProperty()
    company = db.ReferenceProperty(Company, collection_name = "owners")

