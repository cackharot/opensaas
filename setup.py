import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()

requires = ['pyramid', 'WebError', 'pymongo']

setup(name='opensaas',
      version='0.1',
      description='An open source multi-tenant SAAS service which eases the SAAS application development by providing most of the foundational/common features and drives the app development to build on the core business functionality instead of these.',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author="Cackharot",
      author_email='cackharot@gmail.com',
      url='https://github.com/cackharot/opensaas',
      keywords='saas multi-tenant, tennat management, user management, security management, subscription management, activity management',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="opensaas",
      entry_points = """\
      [paste.app_factory]
      main = opensaas:main
      """,
      paster_plugins=['pyramid'],
      )

