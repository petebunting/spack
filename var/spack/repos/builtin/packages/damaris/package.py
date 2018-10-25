# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Damaris(CMakePackage):
    """Damaris is a middleware for I/O and in situ analytics
    targeting large-scale, MPI-based HPC simulations."""

    homepage = "https://project.inria.fr/damaris/"
    url = "https://gitlab.inria.fr/Damaris/damaris"

    version('master', git='https://gitlab.inria.fr/Damaris/damaris.git')
    version('1.3.1',  git='https://gitlab.inria.fr/Damaris/damaris.git', 
            commit='98c27e99458c10b834c4e59753f4ce5a42337c6f', preferred=True)

    variant('fortran', default=True,  description='Enable Fortran support')
    variant('hdf5',    default=False, description='Enable the HDF5 storage plugin')
    variant('static',  default=False, description='Builds a static version of the library')

    depends_on('mpi')
    depends_on('cmake@3.12.0:', type=('build'))
    depends_on('boost +thread+log+filesystem+date_time @1.67:')
    depends_on('xsd')
    depends_on('xerces-c')
    depends_on('hdf5@1.8.20:', when='+hdf5')

    def cmake_args(self):

        args = []
        if(not self.spec.variants['static'].value):
            args.extend(['-DBUILD_SHARED_LIBS=ON'])

        args.extend(['-DCMAKE_CXX_COMPILER=%s' % self.spec['mpi'].mpicxx])
        args.extend(['-DCMAKE_C_COMPILER=%s' % self.spec['mpi'].mpicc])
        args.extend(['-DBOOST_ROOT=%s' % self.spec['boost'].prefix])
        args.extend(['-DXercesC_ROOT=%s' % self.spec['xerces-c'].prefix])
        args.extend(['-DXSD_ROOT=%s' % self.spec['xsd'].prefix])

        if (self.spec.variants['fortran'].value):
            args.extend(['-DCMAKE_Fortran_COMPILER=%s'
                         % self.spec['mpi'].mpifc])
            args.extend(['-DENABLE_FORTRAN:BOOL=ON'])

        if (self.spec.variants['hdf5'].value):
            args.extend(['-DENABLE_HDF5:BOOL=ON'])
            args.extend(['-DHDF5_ROOT:PATH=%s' % self.spec['hdf5'].prefix])
        return args