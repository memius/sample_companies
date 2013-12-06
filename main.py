# coding: utf-8

import jinja2, webapp2, time, os

from google.appengine.api import urlfetch
from google.appengine.ext import db

import duplicates

from models import Company, Owner, Director

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):

    def get(self): 

        self.response.write("Welcome to Thomas Hagen's sample company website")

        # template_values = {
        #     'message' : "Welcome to Thomas Hagen's sample company website"
        #     }

        # template = jinja_environment.get_template('index.html')
        # self.response.out.write(template.render(template_values))

class AddHandler(webapp2.RequestHandler):
    def get(self):

        template_values = {
#            'company' : "yolo"
            }

        template = jinja_environment.get_template('add.html')
        self.response.out.write(template.render(template_values))

class AddedHandler(webapp2.RequestHandler):
    def post(self):
        company = Company()

        try:
            name = self.request.get('name') 
            company.name = name
        except:
            pass

        try:
            address = self.request.get('address') 
            company.address = address
        except:
            pass

        try:
            city = self.request.get('city') 
            company.city = city
        except:
            pass

        try:
            country = self.request.get('country') 
            company.country = country
        except:
            pass

        try:
            email = self.request.get('email') 
            company.email = email
        except:
            pass

        try:
            phone_number = int(self.request.get('phone_number'))
            company.phone_number = phone_number
        except:
            pass

        company.put()

        company_id = company.key().id()

        self.redirect("company/" + str(company_id))

# class PassportHandler (webapp2.RequestHandler):
#   def get(self, passport_id):
#       company = Company.get_by_id(int(passport_id))
#       passport_scan = company.passport_scan

#       self.response.headers['Content-Type'] = "application/pdf" 
#       self.response.out.write(passport_scan)

class OwnersHandler(webapp2.RequestHandler): # lets you add an owner
    def get(self,company_id):
        company = Company.get_by_id(int(company_id))

        template_values = {
            'company' : company
            }

        template = jinja_environment.get_template('owners.html')
        self.response.out.write(template.render(template_values))

class DirectorsHandler(webapp2.RequestHandler): # lets you add a director
    def get(self,directors_id):
        company = Company.get_by_id(int(directors_id))

        template_values = {
            'company' : company
            }

        template = jinja_environment.get_template('directors.html')
        self.response.out.write(template.render(template_values))

class OwnerHandler(webapp2.RequestHandler): # show or add passport of one owner 
    def get(self,owner_id):
        owner = Owner.get_by_id(int(owner_id))

        if owner.passport:
            self.response.headers['Content-Type']="application/pdf"
            self.response.write(owner.passport)
        else:
            template_values = {
                'owner' : owner 
                }

            template = jinja_environment.get_template('ownerattach.html')
            self.response.out.write(template.render(template_values))

class DirectorHandler(webapp2.RequestHandler): # show or add passport of director
    def get(self,director_id):
        director = Director.get_by_id(int(director_id))
        if director.passport:
            self.response.headers['Content-Type']="application/pdf"
            self.response.write(director.passport)
        else:
            template_values = {
                'director' : director 
                }

            template = jinja_environment.get_template('directorattach.html')
            self.response.out.write(template.render(template_values))

class EditHandler(webapp2.RequestHandler):
    def get(self,edit_id):
        company = Company.get_by_id(int(edit_id))

        template_values = {
            'company' : company
            }

        template = jinja_environment.get_template('edit.html')
        self.response.out.write(template.render(template_values))

class OwnerEditedHandler(webapp2.RequestHandler):
    def post(self,owner_id):
        owner = Owner.get_by_id(int(owner_id))
        p = self.request.get('passport') 
        owner.passport = p
        owner.put()
        self.redirect("/owner/" + str(owner_id))

class DirectorEditedHandler(webapp2.RequestHandler):
    def post(self,director_id):
        director = Director.get_by_id(int(director_id))
        p = self.request.get('passport') 
        director.passport = p
        director.put()
        self.redirect("/director/" + str(director_id))

class EditedHandler(webapp2.RequestHandler):
    def post(self):
        company_id = self.request.get('company_id') 
        company = Company.get_by_id(int(company_id))

        try:
            name = self.request.get('name') 
            company.name = name
        except:
            pass

        try:
            address = self.request.get('address') 
            company.address = address
        except:
            pass

        try:
            city = self.request.get('city') 
            company.city = city
        except:
            pass

        try:
            country = self.request.get('country') 
            company.country = country
        except:
            pass

        try:
            email = self.request.get('email') 
            company.email = email
        except:
            pass

        try:
            phone_number = int(self.request.get('phone_number'))
            company.phone_number = phone_number
        except:
            pass

        try:
            owner_name = self.request.get('owner_name')
            owner = Owner()
            owner.name = owner_name
            owner.company = company.key()
            owner.put()
        except:
            pass

        try:
            director_name = self.request.get('director_name')
            director = Director()
            director.name = director_name
            director.company = company.key()
            director.put()
        except:
            pass
        
        company.put()   
        self.redirect("company/" + str(company_id))

class OwnerAttachHandler(webapp2.RequestHandler):
    def post(self,owner_id):
        
        owner = Owners.filter("name= ",owner_id)

        template_values = {
            'owner' : owner
            }

        template = jinja_environment.get_template('attach.html')
        self.response.out.write(template.render(template_values))

class DirectorAttachHandler(webapp2.RequestHandler):
    def post(self,director_id):
        
        director = Directors.filter("name= ",director_id)

        template_values = {
            'director' : director
            }

        template = jinja_environment.get_template('attach.html')
        self.response.out.write(template.render(template_values))

class CompanyClickHandler(webapp2.RequestHandler):
    def get(self,company_id): # apparently, it must be company_id, not something else.
        company = Company.get_by_id(int(company_id))
         
        template_values = {
            'company' : company
            }

        template = jinja_environment.get_template('company.html')
        self.response.out.write(template.render(template_values))

class CompaniesHandler(webapp2.RequestHandler):
    def get(self):
        companies = Company.all()

        keys_names = []
        for company in companies:
            keys_names.append([company.key().id(),company.name])

        template_values = {
            'keys_names' : keys_names,
            'companies' : companies
            }

        template = jinja_environment.get_template('companies.html')
        self.response.out.write(template.render(template_values))

class DuplicateHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('you have removed duplicates')
        duplicates.companies()

app = webapp2.WSGIApplication([
#        ('/auth_return', AuthHandler),
        ('/companies', CompaniesHandler),
        ('/dupes',DuplicateHandler),
        ('/company/(.*)', CompanyClickHandler),
        ('/edit/(.*)',EditHandler),
        ('/edited',EditedHandler),
        ('/add',AddHandler),
        ('/added',AddedHandler),
        ('/owners/(.*)',OwnersHandler),
        ('/owner/(.*)',OwnerHandler),
        ('/owneredited/(.*)',OwnerEditedHandler),
        ('/directors/(.*)',DirectorsHandler),
        ('/director/(.*)',DirectorHandler),
        ('/directoredited/(.*)',DirectorEditedHandler),
        ('/ownerattach/(.*)', OwnerAttachHandler),
        ('/directorattach/(.*)', DirectorAttachHandler),
        ('/.*', MainPage),
        ], ) 

