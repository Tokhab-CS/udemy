import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(X)
print(y)

# Taking care of missing data
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print(X)

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)
# Encoding the Dependent Variable
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y = le.fit_transform(y)
print(y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
print(X_train)
print(X_test)
print(y_train)
print(y_test)

# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:, 3:])
print(X_train)
print(X_test)

# from datetime import datetime as dt
#
#
# def timeit(func):
#     def wrapper(*args, **kwargs):
#         start = dt.now()
#         result = func(*args, **kwargs)
#         print(f'Function "{func.__name__}" has worked for {dt.now() - start}')
#         return result
#     return wrapper
#
# @timeit
# def one(n):
#     arr = []
#     for i in range(n):
#         if i %2 == 0:
#             arr.append(i)
#     return arr
#
#
# if __name__ == '__main__':
#     print(one(10000))


# import re
# def convert_phone_number(phone):
#   result = re.sub(r'(\d{3})-(\d{3})-(\d{4}\b)', r'(\1) \2-\3', phone)
#   return result
#
# print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
# print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
# print(convert_phone_number("123-123-12345")) # 123-123-12345
# print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300

# import re
# def transform_comments(line_of_code):
#   result = re.sub(r'##*',r'//', line_of_code)
#   return '# Should be "' + result
#
# print(transform_comments("### Start of program"))
# # Should be "// Start of program"
# print(transform_comments("  number = 0   ## Initialize the variable"))
# # Should be "  number = 0   // Initialize the variable"
# print(transform_comments("  number += 1   # Increment the variable"))
# # Should be "  number += 1   // Increment the variable"
# print(transform_comments("  return(number)"))
# # Should be "  return(number)"

# import re
# def multi_vowel_words(text):
#   pattern = r'\b\w*[aeiou]{3}\w*\b'
#   result = re.findall(pattern, text)
#   return result
#
# print(multi_vowel_words("Life is beautiful"))
# # ['beautiful']
#
# print(multi_vowel_words("Obviously, the queen is courageous and gracious."))
# # ['Obviously', 'queen', 'courageous', 'gracious']
#
# print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner."))
# # ['rambunctious', 'quietly', 'delicious']
#
# print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)"))
# # ['queue']
#
# print(multi_vowel_words("Hello world!"))
# # []

# import re
# def transform_record(record):
#   new_record = re.sub(r'([\w+\s]*),([\d+-]*),([\w+\s]*)', r'\1,+1-\2,\3', record)
#   return new_record
#
# print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# # Sabrina Green,+1-802-867-5309,System Administrator
#
# print(transform_record("Eli Jones,684-3481127,IT specialist"))
# # Eli Jones,+1-684-3481127,IT specialist
#
# print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# # Melody Daniels,+1-846-687-7436,Programmer
#
# print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# # Charlie Rivera,+1-698-746-3357,Web Developer


# import re
# print(re.split(r"the|a", "One sentence. Another one? And the last one!"))

# import re
# def extract_pid(log_line):
#     regex = r"\[(\d+)\]\:\s(\w+)"
#     result = re.search(regex, log_line)
#     if result is None:
#         return None
#     print(result)
#
#     return "{} ({})".format(result[1], result[2])
#
# print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
# print(extract_pid("99 elephants in a [cage]")) # None
# print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
# print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

# import re
# def rearrange_name(name):
#   result = re.search(r"^(\w*), (\w*|\w*.)$", name)
#   if result == None:
#     return name
#   return "{} {}".format(result[2], result[1])
#
# name=rearrange_name("Kennedy, John F.")
# print(name)
#

# import re
# def check_zip_code (text):
#   result = re.search(r"[ ]\d{5}", text)
#   return result != None
#
# print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
# print(check_zip_code("90210 is a TV show")) # False
# print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
# print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False

# import re
# def contains_acronym(text):
#   pattern = r"[\(]\w*[\)]"
#   result = re.search(pattern, text)
#   return result != None
#
# print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
# print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
# print(contains_acronym("Please do NOT enter without permission!")) # False
# print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
# print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

# import re
# def check_time(text):
#   pattern = r"^(1[012]|[1-9]):([0-5][0-9])[ ]?(am|pm|AM|PM)"
#   result = re.search(pattern, text)
#   return result != None
#
# print(check_time("12:45pm")) # True
# print(check_time("9:59 AM")) # True
# print(check_time("6:60am")) # False
# print(check_time("five o'clock")) # False

# import re
# def repeating_letter_a(text):
#   result = re.search(r"[a].*[a]", text, re.IGNORECASE)
#   return result != None
#
# print(repeating_letter_a("banana")) # True
# print(repeating_letter_a("pineapple")) # False
# print(repeating_letter_a("Animal Kingdom")) # True
# print(repeating_letter_a("A is for apple")) # True

# import csv
#
# def read_employees(csv_file_location):
#   csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
#   employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
#   employee_list = []
#   for data in employee_file:
#     employee_list.append(data)
#   return employee_list
#
#
# def process_data(employee_list):
#   department_list = []
#   for employee_data in employee_list:
#     department_list.append(employee_data['Department'])
#   department_data = {}
#   for department_name in set(department_list):
#     department_data[department_name] = department_list.count(department_name)
#   return department_data
#
#
# def write_report(dictionary, report_file):
#   with open(report_file, "w+") as f:
#     for k in sorted(dictionary):
#       f.write(str(k)+':'+str(dictionary[k])+'\n')
#     f.close()
#
#
# employee_list = read_employees('employees.csv')
#print(employee_list)

#
# dictionary = process_data(employee_list)
# print(dictionary)
#
# write_report(dictionary, 'test_report.txt')
#

# import os
# def parent_directory():
#   # Create a relative path to the parent
#   # of the current working directory
#   #relative_parent = os.path.join(___, ___)
#
#   # Return the absolute path of the parent directory
#   return 10
#
# print(parent_directory())
# print(os.listdir())
# print((os.path))
# print(os.getcwd())
# #
# import os
# def create_python_script(filename):
#   comments = "# Start of a new Python program"
#   with open('program.py', mode='w') as f:
#     f.write(comments)
#   filesize = os.path.getsize('program.py')
#   return(filesize)
#
# print(create_python_script("program.py"))
#
# import os
#
# def new_directory(directory, filename):
#   # Before creating a new directory, check to see if it already exists
#   if os.path.isdir(directory) == False:
#     os.mkdir(directory)
#   # Create the new file inside of the new directory
#   os.chdir(directory)
#   with open (filename, mode='w') as file:
#     pass
#
#   # Return the list of files in the new directory
#   return os.listdir()
#
# print(new_directory("PythonPrograms", "script.py"))
#
# import os
# import datetime as dt
#
#
# def file_date(filename):
#   # Create the file in the current directory
#   with open(filename, mode='w') as f:
#     f.write('')
#   timestamp = os.path.getmtime(filename)
#   # Convert the timestamp into a readable format, then into a string
#
#   # Return just the date portion
#   # Hint: how many characters are in “yyyy-mm-dd”?
#   return dt.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
#
#
# print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd