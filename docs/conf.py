#
# pyhf documentation build configuration file, created by
# sphinx-quickstart on Fri Feb  9 11:58:49 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use Path('../relative_path_to_dir').resolve() to make it absolute, like shown here.

from pathlib import Path
import sys
from pkg_resources import get_distribution

sys.path.insert(0, str(Path('./exts').resolve()))


def setup(app):
    app.add_css_file(
        'https://cdnjs.cloudflare.com/ajax/libs/github-fork-ribbon-css/0.2.2/gh-fork-ribbon.min.css'
    )


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.bibtex',
    'sphinx.ext.napoleon',
    'sphinx_click.ext',
    'nbsphinx',
    'sphinx_issues',
    'sphinx_copybutton',
    'sphinx_togglebutton',
    'xref',
]
bibtex_bibfiles = [
    "bib/docs.bib",
    "bib/HEPData_likelihoods.bib",
    "bib/media.bib",
    "bib/posters.bib",
    "bib/preferred.bib",
    "bib/talks.bib",
    "bib/tutorials.bib",
    "bib/use_citations.bib",
    "bib/general_citations.bib",
]
bibtex_default_style = "unsrt"

# external links
xref_links = {"arXiv:1007.1727": ("[1007.1727]", "https://arxiv.org/abs/1007.1727")}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
    'iminuit': ('https://iminuit.readthedocs.io/en/stable/', None),
    'uproot': ('https://uproot.readthedocs.io/en/latest/', None),
    'jsonpatch': ('https://python-json-patch.readthedocs.io/en/latest/', None),
}

# GitHub repo
issues_github_path = 'scikit-hep/pyhf'

# Generate the API documentation when building
autosummary_generate = True
numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

# The encoding of source files.
#
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'pyhf'
copyright = '2018, Lukas Heinrich, Matthew Feickert, Giordon Stark'
author = 'Lukas Heinrich, Matthew Feickert, Giordon Stark'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
# The full version, including alpha/beta/rc tags.
release = get_distribution('pyhf').version
# for example take major/minor/patch
version = '.'.join(release.split('.')[:3])

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#
# today = ''
#
# Else, today_fmt is used as the format for a strftime call.
#
# today_fmt = '%B %d, %Y'

autodoc_mock_imports = [
    'tensorflow',
    'torch',
    'jax',
    'iminuit',
    'tensorflow_probability',
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    '_build',
    'JOSS',
    '**.ipynb_checkpoints',
    'examples/experiments/edwardpyhf.ipynb',
    'examples/notebooks/ImpactPlot.ipynb',
    'examples/notebooks/Recast.ipynb',
    'examples/notebooks/StatError.ipynb',
    'examples/notebooks/example-tensorflow.ipynb',
    'examples/notebooks/histogrammar.ipynb',
    'examples/notebooks/histosys.ipynb',
    'examples/notebooks/histosys-pytorch.ipynb',
    'examples/notebooks/importxml.ipynb',
    'examples/notebooks/multichannel-coupled-normsys.ipynb',
    'examples/notebooks/multichannel-normsys.ipynb',
    'examples/notebooks/normsys.ipynb',
    'examples/notebooks/pullplot.ipynb',
    'examples/notebooks/pytorch_tests_onoff.ipynb',
    'examples/notebooks/tensorflow-limit.ipynb',
]

# The reST default role (used for this markup: `text`) to use for all
# documents.
#
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = []

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#
# html_title = u'pyhf v0.3.0'

# A shorter title for the navigation bar.  Default is the same as html_title.
#
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
# html_logo = None

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]

html_js_files = [
    'js/custom.js',
]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#
html_extra_path = ['_extras']

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
# html_last_updated_fmt = None

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#
# html_additional_pages = {}

# If false, no module index is generated.
#
# html_domain_indices = True

# If false, no index is generated.
#
# html_use_index = True

# If true, the index is split into individual pages for each letter.
#
# html_split_index = False

# If true, links to the reST sources are added to the pages.
#
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr', 'zh'
#
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
#
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'pyhfdoc'

# sphinx-copybutton configuration
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True
copybutton_here_doc_delimiter = "EOF"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        'pyhf.tex',
        'pyhf Documentation',
        'Lukas Heinrich, Matthew Feickert, Giordon Stark',
        'manual',
    )
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#
# latex_use_parts = False

# If true, show page references after internal links.
#
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
#
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
#
# latex_appendices = []

# It false, will not define \strong, \code, 	itleref, \crossref ... but only
# \sphinxstrong, ..., \sphinxtitleref, ... To help avoid clash with user added
# packages.
#
# latex_keep_old_macro_names = True

# If false, no module index is generated.
#
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'pyhf', 'pyhf Documentation', [author], 1)]

# If true, show URL addresses after external links.
#
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        'pyhf',
        'pyhf Documentation',
        author,
        'pyhf',
        'One line description of project.',
        'Miscellaneous',
    )
]

# Documents to append as an appendix to all manuals.
#
# texinfo_appendices = []

# If false, no module index is generated.
#
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#
# texinfo_no_detailmenu = False

mathjax3_config = {
    'tex2jax': {'inlineMath': [['$', '$'], ['\\(', '\\)']]},
    'tex': {
        'macros': {
            'bm': ["\\boldsymbol{#1}", 1],  # \usepackage{bm}, see mathjax/MathJax#1219
            'HiFa': r'\texttt{HistFactory}',
            'Root': r'\texttt{ROOT}',
            'RooStats': r'\texttt{RooStats}',
            'RooFit': r'\texttt{RooFit}',
            'pyhf': r'\texttt{pyhf}',
            'CLs': r'\mathrm{CL}_{s}',
            'freeset': r'\bm{\eta}',
            'constrset': r'\bm{\chi}',
            'singleconstr': r'\chi',
            'channelcounts': r'\bm{n}',
            'auxdata': r'\bm{a}',
            'poiset': r'\bm{\psi}',
            'nuisset': r'\bm{\theta}',
            'fullset': r'\bm{\phi}',
            'singlefull': r'\phi',
            'TeV': r'\textrm{TeV}',
        }
    },
}

# c.f. https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder
linkcheck_ignore = ['cli.html#pyhf-xml2json']
linkcheck_retries = 50
