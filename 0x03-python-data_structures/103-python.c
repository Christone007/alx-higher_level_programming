#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p) {
    PyBytesObject *byte_obj = (PyBytesObject *)p;
    Py_ssize_t size = PyObject_Size(p);

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);

    if (size > 0){
	    printf("  trying string: %s\n", PyUnicode_AsUTF8AndSize(p, NULL));
	    printf("  first 6 bytes:");

	    for (Py_ssize_t i = 0; i < size && i < 6; ++i) 
	    {
		    printf(" %02x", (unsigned char)byte_obj->ob_sval[i]);
	    }
	    printf("\n");
    }
}

void print_python_list(PyObject *p) {
    Py_ssize_t size = PyObject_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject *element = ((PyListObject *)p)->ob_item[i];
        printf("Element %zd: ", i);

        if (PyBytes_Check(element)) {
            print_python_bytes(element);
        } else {
            printf("%s\n", ((PyObject *)(element))->ob_type->tp_name);
        }
    }
}
