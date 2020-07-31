import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xab\xf1K&9aP\xd8\x8e\x8do\x05g\x1f\x10\xf7'
    MONGODB_SETTINGS = {'db':'UTA_Enrollment'}


    #  py -c "import os; print(os.urandom(16))"