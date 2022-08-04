# def  user_input(self):
while rows not in '12345678':
        try:
            rows = int(input("Enter row in which you want to attack: "))
        except ValueError:
            print('wrong')
            continue
        else:
            break      
        
if rows is  '12345678':
    print("hallo")

        # try:
        #     rows = int(input("Enter row in which you want to attack: "))
        #     while rows not in '12345678':
        #         except ValueError:
        #             print('sorry, you are wrong')