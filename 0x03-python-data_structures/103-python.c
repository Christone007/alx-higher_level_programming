#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p) 
{
    PyBytesObject *byte_obj = (PyBytesObject *)p;
    Py_ssize_t size = PyBytes_Size(p);

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
	    printf("[ERROR] Invalid Bytes Object");
	    return;
    }
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));
    printf("  first 6 bytes:");

    for (Py_ssize_t i = 0; i < 6; ++i) {
        printf(" %02x", (unsigned char)PyBytes_AS_STRING(byte_obj)[i]);
    }
    printf("\n");
}

void print_python_list(PyObject *p) {
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject *element = PyList_GetItem(p, i);
        printf("Element %zd: ", i);

        if (PyBytes_Check(element)) {
            print_python_bytes(element);
        } else {
            printf("%s\n", Py_TYPE(element)->tp_name);
        }
    }
}
