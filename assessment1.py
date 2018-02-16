import  random
import datetime
# w, h = 10, 5
# Matrix = [[random.random() for x in range(w)] for y in range(h)]
# for i in range(0,10):
#     for j in range(0,5):
#         if Matrix[j][i] >0.65:
#             print("{} is larger than 0.65 which is the tolerance, error in machine {}".format(Matrix[j][i],j+1))


def generate_sensor():
    w, h = 16, 32
    matrix = [[random.random() for x in range(w)] for y in range(h)]
    return matrix

def check_error(readings =[[]]):
    print(readings)
    output=[[]]
    for i in range(0,32):
        added = False
        for j in range(0,16):
            if isinstance(readings[i][j], basestring):
                readings[i][j] = 999
                if added == False:
                    output.append(readings[i])

    return  output



readings = generate_sensor()
readings[2][5] = 'err'
errors = check_error(readings)
print(errors)
sensor_date = datetime.datetime.now()
# for i in range(0,32):
#     print("Sensor {} at {} values: {}".format(i+1,sensor_date,readings[i]))