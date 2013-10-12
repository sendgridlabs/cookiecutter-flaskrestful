from setuptools import setup

required_packages = [
    'Cython==0.19.1',
    'gevent==1.0dev',
    'setuptools==1.1.6',
    'Flask==0.10.1',
    'Flask-RESTful==0.2.3',
    'WTForms==1.0.5',
    'boto==2.10.0',
    'Fabric==1.6.1',
    'Pygments==1.6',
    'Sphinx==1.2b1',
    'WTForms==1.0.4',
    'Werkzeug==0.9.1',
    'airbrake-flask==0.0.3',
    'anyjson==0.3.3',
    'coverage==3.6',
    'docutils==0.10',
    'gunicorn==17.5',
    'livereload==1.0.0',
    'mock==1.0.1',
    'nose==1.3.0',
    'python-memcached==1.53',
    'requests==1.2.3',
    'six==1.3.0',
    'sphinx-bootstrap-theme==0.3.1',
    'sphinxcontrib-httpdomain==1.1.9'
]

setup(
    name='{{cookiecutter.package_namespace}}.{{cookiecutter.app_name}}',
    description='{{cookiecutter.project_short_description}}',
    version='0.0.1',
    packages=['{{cookiecutter.package_namespace}}',
              '{{cookiecutter.package_namespace}}.{{cookiecutter.app_name}}'],
    namespace_packages=['{{cookiecutter.package_namespace}}'],
    install_requires=required_packages,
    dependency_links=[('https://github.com/surfly/gevent/tarball/master#'
            'egg=gevent-1.0dev')],
    extras_require={
        'test': [
            'nose==1.3.0',
            'ddbmock==1.0.3',
        ]
    }
)
