#USE DEPENDENT OPERATING SYSTEM FUNCTIONALITY
import os

import app

#CREATE TEMPORARY DIRECTORY
import tempfile

#TEST AUTOMATION
import unittest


class AppTests(unittest.TestCase):

    def setUp(self):
        #mkdtemp() is a low level function which requires manual cleanup
        #ValueError is expected when unpacking too many values
        self.db_d, app.app.config['DATABASE'] = tempfile.mkdtemp()
        app.app.testing = True
        self.app = app.app.test_client()
        with app.app.app_context():
            app.phoneBook

    def tearDown(self):
        os.close(self.db_d)
        os.unlink(app.app.config['DATABASE'])

    #TEST HOME
    def test_empty_db(self):
        tp = self.app.get('/')
        assert 'Database is empty'

    #TEST VIEW CONTACT
    def test_viewContact(self):
        tp = self.app.post(
            '/view', data=dict(name='<random>', phone='<random>'))
        assert 'random'

