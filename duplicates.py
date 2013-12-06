# coding: utf-8

#checks for duplicates in the db, and removes them.

from google.appengine.ext import db

from models import Company

def companies():
    q = Company.all()
    q.order("datetime")
    companies = q.fetch(1000)
    duplicates = []
    for company in companies:
        if company.name in duplicates:
            db.delete(company)
        else:
            duplicates.append(company.name)
