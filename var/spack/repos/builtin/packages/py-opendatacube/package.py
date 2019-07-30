##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-opendatacube
#
# You can edit this file again by typing:
#
#     spack edit py-opendatacube
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PyOpendatacube(PythonPackage):
    """Open Data Cube analyses continental scale Earth Observation data through time."""

    homepage = "https://www.opendatacube.org"
    url      = "https://github.com/opendatacube/datacube-core/archive/datacube-1.7.tar.gz"

    maintainers = ['petebunting']

    version('1.7', '472a25b9c7c3090f854e8a7725aa67eb')

    # Add dependencies if required.
    depends_on('py-setuptools', type='build')
    depends_on('python', type=('build', 'run'))
    depends_on('postgresql', type=('build', 'run'))
    depends_on('py-click', type=('build', 'run'))
    depends_on('py-cachetools', type=('build', 'run'))
    depends_on('py-affine', type=('build', 'run'))
    depends_on('py-cloudpickle', type=('build', 'run'))
    depends_on('gdal', type=('build', 'run'))
    depends_on('py-dask', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-psycopg2', type=('build', 'run'))
    depends_on('py-jsonschema', type=('build', 'run'))
    depends_on('py-netcdf4', type=('build', 'run'))
    depends_on('py-pypeg2', type=('build', 'run'))
    depends_on('py-python-dateutil', type=('build', 'run'))
    depends_on('py-pyyaml', type=('build', 'run'))
    depends_on('py-rasterio', type=('build', 'run'))
    depends_on('py-sqlalchemy', type=('build', 'run'))
    depends_on('py-toolz', type=('build', 'run'))
    depends_on('py-xarray', type=('build', 'run'))


