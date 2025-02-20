# ----------------------------------------------------------------------------
# Copyright (c) 2022-2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from .dereplication import dereplicate_mags
from .kraken2 import bracken, classification, database
from .metabat2 import metabat2
from . import eggnog


from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

__all__ = [
    'metabat2', 'bracken', 'classification', 'database',
    'dereplicate_mags', 'eggnog'
]
