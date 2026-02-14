"""
Minimal setup.py for building Cython extensions.
Most configuration is now in pyproject.toml.
"""
import os
import sys
from setuptools import setup, Extension


def generate_cython():
    """Generate C files from Cython sources."""
    from Cython.Build import cythonize
    
    module_list = [
        "py_stringmatching/similarity_measure/cython/cython_affine.pyx",
        "py_stringmatching/similarity_measure/cython/cython_jaro.pyx",
        "py_stringmatching/similarity_measure/cython/cython_jaro_winkler.pyx",
        "py_stringmatching/similarity_measure/cython/cython_levenshtein.pyx",
        "py_stringmatching/similarity_measure/cython/cython_needleman_wunsch.pyx",
        "py_stringmatching/similarity_measure/cython/cython_smith_waterman.pyx",
        "py_stringmatching/similarity_measure/cython/cython_utils.pyx"
    ]

    p = cythonize(module_list)

    if not p:
        raise RuntimeError("Running cythonize failed!")


def get_numpy_include():
    """Get numpy include directory using modern approach."""
    import numpy
    return numpy.get_include()


def main():
    # Check if we need to generate Cython sources
    no_frills = (len(sys.argv) >= 2 and ('--help' in sys.argv[1:] or
                                         sys.argv[1] in ('--help-commands',
                                                         'egg_info', '--version',
                                                         'clean')))
    
    cwd = os.path.abspath(os.path.dirname(__file__))
    if not os.path.exists(os.path.join(cwd, 'PKG-INFO')) and not no_frills:
        # Generate Cython sources, unless building from source release
        generate_cython()
    
    # Get numpy include directory
    numpy_incl = get_numpy_include()
    
    # Define extensions
    extensions = [
        Extension(
            "py_stringmatching.similarity_measure.cython.cython_levenshtein",
            ["py_stringmatching/similarity_measure/cython/cython_levenshtein.c"],
            include_dirs=[numpy_incl]
        ),
        Extension(
            "py_stringmatching.similarity_measure.cython.cython_jaro",
            ["py_stringmatching/similarity_measure/cython/cython_jaro.c"],
            include_dirs=[numpy_incl]
        ),
        Extension(
            "py_stringmatching.similarity_measure.cython.cython_jaro_winkler",
            ["py_stringmatching/similarity_measure/cython/cython_jaro_winkler.c"],
            include_dirs=[numpy_incl]
        ),
        Extension(
            "py_stringmatching.similarity_measure.cython.cython_utils",
            ["py_stringmatching/similarity_measure/cython/cython_utils.c"],
            include_dirs=[numpy_incl]
        ),
        Extension(
            "py_stringmatching.similarity_measure.cython.cython_needleman_wunsch",
            ["py_stringmatching/similarity_measure/cython/cython_needleman_wunsch.c"],
            include_dirs=[numpy_incl]
        ),
        Extension(
            "py_stringmatching.similarity_measure.cython.cython_smith_waterman",
            ["py_stringmatching/similarity_measure/cython/cython_smith_waterman.c"],
            include_dirs=[numpy_incl]
        ),
        Extension(
            "py_stringmatching.similarity_measure.cython.cython_affine",
            ["py_stringmatching/similarity_measure/cython/cython_affine.c"],
            include_dirs=[numpy_incl]
        )
    ]
    
    setup(ext_modules=extensions)


if __name__ == "__main__":
    main()