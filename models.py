# coding: utf-8


from google.appengine.api import users
from google.appengine.ext import db

class UserPrefs(db.Model):
    user_id = db.StringProperty()
    nickname = db.StringProperty()
    email = db.StringProperty()
    companies = db.ListProperty(db.Key)
    # obj = db.UserProperty()
    # name = db.StringProperty()
    # companies is an implied property - see Company class.


# Company ID
# Name
# Address
# City
# Country
# E-mail (not required)
# Phone Number (not required)
# One or more directors and beneficial owners.

class Company(db.Model):
    name = db.StringProperty() #show this in the web app
    name_lower = db.StringProperty() 
    address = db.StringProperty() #show this in the web app
    address_lower = db.StringProperty() 
    city = db.StringProperty() #show this in the web app
    city_lower = db.StringProperty() 
    country = db.StringProperty() #show this in the web app
    country_lower = db.StringProperty() 
    email = db.StringProperty() #show this in the web app
    email_lower = db.StringProperty() 
    phone_number = db.IntegerProperty()
    ticker = db.StringProperty() #show only this in the android app
    ticker_lower = db.StringProperty() 
    exchange = db.StringProperty()
    datetime = db.DateTimeProperty(auto_now_add=True)
    price = db.FloatProperty()
    movement = db.BooleanProperty()  #whether it went up or down since yesterday. if no value -> no movement.
#    articles = db.ReferenceProperty(Article) #not needed: do this: articles = company.articles.get()
    titles = db.StringListProperty()
    finished_scraping = db.BooleanProperty(False)
#    passport_scan = db.BlobProperty()
#    user = db.ReferenceProperty(UserPrefs, collection_name = "companies")
#    recommendation = db.StringProperty() #'buy', 'hold' or 'sell'
#    confidence = db.FloatProperty() #a number from 0.0 to 1.0
#    user = db.ReferenceProperty(User, collection_name = "companies")

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

    # @property
    # def passport(self):
    #     return Passport.gql("WHERE directors = :1", self.key()) 

class Owner(db.Model):
    name = db.StringProperty()
    passport = db.BlobProperty()
    company = db.ReferenceProperty(Company, collection_name = "owners")

    # @property
    # def passport(self):
    #     return Passport.gql("WHERE owners = :1", self.key()) 

# class Passport(db.Model):
#     content = db.BlobProperty()
#     owner = db.ReferenceProperty(Owner, collection_name = "passports")
#     director = db.ReferenceProperty(Director, collection_name = "passports")

