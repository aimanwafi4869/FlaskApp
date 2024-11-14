# import tensorflow as tf

# # Avoid maximum Memory Allocation
# # devices = tf.config.list_physical_devices('GPU') 
# # tf.config.experimental.set_memory_growth(devices[0], True)

# #Initialize
# x = tf.constant(4,shape=(1,1), dtype=tf.float32)
# x = tf.constant([[1,2,3],[4,5,6]])

# x = tf.ones((3,3))
# x = tf.zeros((2,3))
# x = tf.eye(3) #Identity Matrix
# x = tf.random.normal((3,3), mean=0, stddev=1) # Random Distribution
# x = tf.random.uniform((1,3), minval=0, maxval=1) # Normal Distribution
# x = tf.range(start=1, limit=10, delta=2) #Delta is increment
# x = tf.cast(x, dtype=tf.float64)

# #Math Operation

# #Initialize
# x = tf.constant([[1,2,3]])
# y = tf.constant([[9,8,7]])

# z = tf.add(x,y) #Addition
# z = tf.subtract(x,y) #Substraction
# z = tf.multiply(x,y) #Multiplication
# z = tf.divide(x,y) #Division
# z = x + y # Alt. Addition
# z = x - y # Alt. Substraction
# z = x * y # Alt. Multiplication
# z = x / y # Alt. Division

# z = x ** 2 #Exponentiate each element by 2 (Power each elemtent by 2)

# x = tf.constant([[1,2,3]])
# y = tf.constant([[9],[8],[7]])
# z = tf.tensordot(x, y, axes=1)
# z = tf.reduce_sum(x*y, axis=0)

# x = tf.random.normal((2,3))
# y = tf.random.normal((3,4))
# z = tf.matmul(x,y) #matrix multiply
# z = x @ y #matrix multiply

# #Indexing
# x = tf.constant([0,1,2,3,4,5,6])
# # print(x[:]) #[0,1,2,3,4,5,6] (print all)
# # print(x[1:]) #[1,2,3,4,5,6] (start from index 1)
# # print(x[1:3]) #[1,2] (start from index 1 end before index 3)
# # print(x[::2]) #[0,2,4,6] (increment by 2)
# # print(x[::-1]) #[6,5,4,3,2,1,0] (Reverse)

# index = tf.constant([0,3,5])
# x_ind = tf.gather(x,index) # Search the same number as index (above)

# x = tf.constant([[1,2],
#                  [3,4],
#                  [5,6]])
# # print(x[0,:]) #[1,2] seperate dimension by using , (comma) 
# # print(x[0:2,]) #[1,2],[3,4] start from index 0 end before index 2

# #Reshaping

# x = tf.range(9)
# print(x) # [0 1 2 3 4 5 6 7 8]

# x = tf.reshape(x, (3,3))
# print(x)

# x = tf.transpose(x,perm=[1,0])
# print(x)

# print(len({1: 'a', 2: 'b', 3: 'c'}))
# _asd = "avx"
# print(_asd)
# print("Python".startswith('P'))
# print(f"Result: {10+5}")

# try:
#     if x == 10:
#         print("x is equal to 10")
# except Exception as e:
#     print(e)


# x = 14
# if x > 5:
#     print("x is greater than 5")
# # Executed if condition one is True.
# if x < 10:
#     print("x is less than 10")
# # Executed if condition two is True.
# if x == 10:
#     print("x is equal to 10")
# # Executed if condition three is True.
# else:
#     print('else will be executed')

# ready = "Y"
# print(ready == ("Yes" or "Y" or "y"))
# name = input("What is your name? ")
# birthYear = input("What year were you born in? ")


# birthYear = birthYear.replace('k','0')

# birthYear = int(birthYear)
# if birthYear >= 2012:
#     print(name,", you are a member of Generation Alpha", sep='213', end='9999')

# a = input("A: ")
# # b = input("B: ")
# # c = input("C: ")

# # if a == b:
# #     if b == c:
# #         print('Wow what are the odds')
# #     else:
# #         print('They wont all be the same')
# # # Executed if condition three is True.
# # else:
# #     print('They wont all be the same')
# match a:
#     case 'a':
#         print('A')
#     case 'b':
#         print('B')