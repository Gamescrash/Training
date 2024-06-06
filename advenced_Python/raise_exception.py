# class Accident(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def print_exception(self):
#         print("User defined exception: ", self.msg)

# try:
#     raise Accident('crash between two cars')
# except Accident as e:
#     e.print_exception()

def process_file():
    try:
        f = open("testo.txt")
        x = 1/0
    except FileNotFoundError as e:
        print("inside except")
    finally:
        print("cleaning up file")
        f.close()

process_file()