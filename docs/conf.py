# This code is part of Qiskit.
#
# (C) Copyright IBM 2023.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

#
# arraylias documentation build configuration file
#

import sys, os
import subprocess

# General configuration:

project = u'arraylias'
copyright = '2023, Qiskit Development Team'  # pylint: disable=redefined-builtin
author = 'Qiskit Development Team'


# The short X.Y version.
version = '0.0.1'
# The full version, including alpha/beta/rc tags.
release = '0.0.1'

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx.ext.viewcode',
              'sphinx.ext.extlinks',
              'sphinx.ext.todo',
              'sphinx.ext.viewcode',
              'jupyter_sphinx',
              'reno.sphinxext',
              'qiskit_sphinx_theme',
             ]
html_static_path = ['_static']
templates_path = ['_templates']
html_css_files = ['style.css', 'custom.css']

pygments_style = 'colorful'

add_module_names = False

modindex_common_prefix = ['arraylias.']

todo_include_todos = True

source_suffix = ['.rst', '.md']

master_doc = 'index'

# Autosummary options
autosummary_generate = True
autosummary_generate_overwrite = False
autoclass_content = 'both'

# HTML Output Options

html_theme = 'qiskit_sphinx_theme'

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
}

htmlhelp_basename = 'arraylias'
