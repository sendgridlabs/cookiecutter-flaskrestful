# -*- coding: utf-8 -*-
import os
import sys

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(ROOT_PATH)
import sphinx_bootstrap_theme

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx.ext.todo',
              'sphinxcontrib.httpdomain', 'sphinx.ext.extlinks',
              'sphinx.ext.viewcode', 'sphinxcontrib.autohttp.flask']

# nitpicky = True
autoclass_content = "both"
source_suffix = '.rst'
master_doc = 'index'
project = u'{{cookiecutter.project_short_description}}'
copyright = u'{{cookiecutter.year}}, {{cookiecutter.company_name}}'
version = 'v1'
pygments_style = 'sphinx'
exclude_patterns = []
add_function_parentheses = True
add_module_names = True

html_domain_indices = False
html_use_index = False
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
templates_path = ['_templates']
html_static_path = ['_static']
html_last_updated_fmt = '%b %d, %Y'
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = False
html_title = "%s %s" % (project, version)
html_logo = ""
html_favicon = ""

html_sidebars = {
    'index': None,
    '**': ['localtoc.html', 'searchbox.html']
}

html_theme_options = {
    # Navigation bar title. (Default: ``project`` value)
    # 'navbar_title': "Demo",

    # Tab name for entire site. (Default: "Site")
    'navbar_site_name': "Endpoints",

    # A list of tuples containing pages or urls to link to.
    # Valid tuples should be in the following forms:
    #    (name, page)                 # a link to a page
    #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
    #    (name, "http://example.com", True) # arbitrary absolute url
    # Note the "1" or "True" value above as the third argument to indicate
    # an arbitrary url.
    'navbar_links': [
        ("Home", "index"),
        ("Getting Started", "getting_started")
    ],

    # Render the next and previous page links in navbar. (Default: true)
    'navbar_sidebarrel': False,

    # Render the current pages TOC in the navbar. (Default: true)
    'navbar_pagenav': False,

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': -1,

    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    #
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "false",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar navbar-inverse",

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "true",

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': None,

    # Bootswatch (http://bootswatch.com/) theme.
    #
    # Options are nothing with "" (default) or the name of a valid theme
    # such as "amelia" or "cosmo".
    #
    # Note that this is served off CDN, so won't be available offline.
    'bootswatch_theme': "flatly",

    # Choose Bootstrap version.
    # Values: "3" (default) or "2" (in quotes)
    'bootstrap_version': "3",
}
