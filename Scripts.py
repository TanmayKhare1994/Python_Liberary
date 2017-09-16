def func():
    print("Simple Function")

if __name__=="__main__":
    print("This is script")

#
# Most Python code is either a module to be imported, or a script that does something.
# However, sometimes it is useful to make a file that can be both imported as a module and run as a script.
# To do this, place script code inside if __name__ == "__main__".
# This ensures that it won't be run if the file is imported.
# ! note :- try to run in console then name will run but if you import this in your project then the function will run .

for i in range(10):
  try:
    if 10 / i == 2.0:
      break
  except ZeroDivisionError:
    print(1)
  else:
    print(2)