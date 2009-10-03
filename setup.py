try:
    from setuptools import setup, find_packages
except:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from admin_upload import __version__

setup(
    name = 'django-admin-uploads',
    version = __version__,
    description = 'File/media browser for Django admin interface. Designed to'
                  'insert images and files into textareas in the admin'
                  'interface with a simple GUI interface.',
    long_description = open('README.rst').read(),
    keywords = 'django apps',
    license = 'New BSD License',
    author = 'Peter Baumgartner',
    author_email = 'pete@lincolnloop.com',
    url = 'http://github.com/rizumu/django-admin-uploads/',
    dependency_links = [],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
)

