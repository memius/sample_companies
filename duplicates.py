# coding: utf-8

#checks for duplicates in the db, and removes them.

from google.appengine.ext import db
from google.appengine.api import memcache

from models import Company

def companies():
    q = Company.all()
    q.order("datetime")
    companies = q.fetch(1000)
    duplicates = []
    checked = []
    for company in companies:

        # if company.name == "General Electric Company":
        #     company.exchange = "NYSE"
        #     company.put()
        #     # db.delete(company)

        if company.name in duplicates:
            db.delete(company)
        else:
            duplicates.append(company.name)
            checked.append(company)

    duplicates = []
    for company in checked:
        if company.ticker in duplicates:
            db.delete(company)
        else:
            duplicates.append(company.ticker)

