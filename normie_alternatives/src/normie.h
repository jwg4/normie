#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION

#include <Python.h>
#include <math.h>

#include <stdlib.h>
#include <stdbool.h>

PyObject* pdf(PyObject*, PyObject*);
PyObject* cdf(PyObject*, PyObject*);
PyObject* invcdf(PyObject*, PyObject*);

