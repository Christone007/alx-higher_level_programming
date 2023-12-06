#include <stdio.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - Prints certain info about a list
 * @p: The list object
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;

	Py_ssize_t size = Py_SIZE(list);
	Py_ssize_t allocated = list->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *element = list->ob_item[i];

		printf("Element %zd: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
