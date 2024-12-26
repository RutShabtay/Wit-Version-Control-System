
import Exceptions
import basicFunctions
from commandLine import wit

# try:
#     wit.wit_init(r"C:\Users\user1\Desktop\Python\Lesson4\H.W")
# except Exceptions.FileExistsError as e:
#     print (e.message)
# wit.wit_add(r"C:\Users\user1\Desktop\Python\Lesson4\H.W", "shabtay.txt")
# wit.wit_add(r"C:\Users\user1\Desktop\Python\Lesson4\H.W", "shabtay.txt")

# wit.wit_commit_m_message("C:\\Users\\user1\\Desktop\\Python\\Lesson4\\H.W","eeeee")
# wit.wit_status("C:\\Users\\user1\\Desktop\\Python\\Lesson4\\H.W")
# wit.wit_checkout("C:\\Users\\user1\\Desktop\\Python\\Lesson4\\H.W","1")
wit.wit_add(r"C:\Users\user1\Desktop\Python\Lesson4\H.W", "shabtay.txt")

wit.wit_commit_m_message("C:\\Users\\user1\\Desktop\\Python\\Lesson4\\H.W","eeeee")
