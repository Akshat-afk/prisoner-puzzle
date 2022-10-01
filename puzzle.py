import random

#The setup
boxes = []
numbers = []
prisoner_num = []
main_dict = {}

for i in range(1,101):
    boxes.append(i)
    numbers.append(i)
    prisoner_num.append(i)

random.shuffle(numbers)

for i in range(0,100):
    main_dict[boxes[i]] = numbers[i]


loop_data=[]
rand_data=[]

#The loop way
def alg(n):
    for t in range(n):
        random.shuffle(numbers)

        for i in range(0,100):
            main_dict[boxes[i]] = numbers[i]

        i=0
        loop_time= 0

        for p in prisoner_num:

            while True:
                num = main_dict.get(p)
                loop_time+=1
                p = num
                if num == prisoner_num[i]:
                    i+=1
                    break

            if loop_time > 50:
                loop_data.append("Fail")
                break

            loop_time = 0

        if i == 100:
            loop_data.append("Success")


#The random way
def rand_alg():
    loop_time = 0
    while True:
        i=0

        for p in prisoner_num:

            box_num = random.choice(boxes)
            num = main_dict.get(box_num)

            if num == p:
                print(f"found the number : {box_num}-->{num}")
                i +=1

            else:
                loop_time +=1

        if loop_time > 50:
            print("Fail")
            rand_data.append("Fail")
            break

    if i == 100:
        print("Success")
        rand_data.append("Success")
        
alg(1000)
print(f"Fails: {loop_data.count('Fail')}, Success: {loop_data.count('Success')} ")


