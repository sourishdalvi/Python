import numpy as np
data_type=[('Name', 'S15'), ('Class',int), ('Height', float)]
students_details =([('Alice', 20, 5.5), ('Bob', 22, 6.0), ('Charlie', 19, 5.8)])
students= np.array(students_details, dtype=data_type)
print("Original Array:")
print(students)
print("Sorted by height:")
print(np.sort(students, order='Height'))