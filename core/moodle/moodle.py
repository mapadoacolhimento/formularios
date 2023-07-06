from core.moodle import moodle_api
from django.conf import settings


def create_and_enrol(form_data):
    
    moodle_api.URL = settings.MOODLE_API_URL
    moodle_api.KEY = settings.MOODLE_API_KEY
    
    user  ={
        'firstname':form_data.values['first_name'],
        'lastname':form_data.values['last_name'],
        'email':form_data.values['email'],
        'username':form_data.values['email'],
        'password':'Pa' + form_data.values['document_number'],
        'auth':'manual',
        'createpassword': 1,
    }
    try:
      response = moodle_api.call('core_user_create_users', users = [user])       
    except: 
      return False
    
    try:
      moodle_api.call('enrol_manual_enrol_users', enrolments = [{'roleid':5,'userid':response[0]["id"],'courseid':2}])
    except: 
      return False
    
    return True