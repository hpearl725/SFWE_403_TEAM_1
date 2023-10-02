# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
import os
import sys
sys.path.insert(0, os.path.abspath('C:/Users/rsfutch77/Desktop/Working/swfe_workspace/SFWE_403_TEAM_1/GUI'))
sys.path.insert(0, os.path.abspath('C:/Users/rsfutch77/Desktop/Working/swfe_workspace/SFWE_403_TEAM_1/logs'))
   
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Pharmacy Manager'
copyright = '2023, Team1'
author = 'Team1'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for intersphinx extension ---------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}
