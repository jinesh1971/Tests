
#This project was made by Jinesh Piyush Modi.
def tests():
        
        choice = int(input("1. Mental math\n2. Python quiz\n-"))
        if choice == 1:
            mentalMath()
        elif choice == 2:
            print()
            print('*'*80)
            python()

        else:
            print("Invalid entry")
    
            
        
def mentalMath():
    

    levelSelect()
def levelSelect():
        difficult =int(input('Please choice your difficulty level: \n1. Kiddo\n2. Advanced\n3. Expert\n4. Impossible\n5. No seriously, give up now: '))
        mentalMaths(difficult)



def mentalMaths(difficultyLevel):
        import random
        if difficultyLevel == 1:
                answers = 111
                correct = 0
                incorrect = 0
                print("Enter the correct answers(to stop press -9): ")
                while answers != -9:
                    
                    number1 = random.randint(1,10)
                    number2 = random.randint(1,10)
                    sumi = number1 + number2
                    print('-->',number1,'+',number2)
                    answers = int(input())
                    if answers == sumi:
                        correct += 1
                    else:
                        incorrect += 1
                carryOn = input("Hit enter to display the result")
                print("%-30s%-30s"%('Correct','Incorrect'))
                print('%-30d  %-30d'%(correct,(incorrect-1)))
                carryOn = int(input("Enter 1 to continue practicing in the same difficulty level\nEnter 2 to change difficulty level\nEnter 3 to terminate "))
                if carryOn == 1:
                    mentalMaths(difficultyLevel)
                elif carryOn == 2:
                    levelSelect()
                else:
                    print("Thankyou for trying")

                    
                    
        elif difficultyLevel == 2:
                answers = 111
                correct = 0
                incorrect = 0
                print("Enter the correct answers(to stop press -9): ")
                while answers != -9:
                    
                    number1 = random.randint(1,10)
                    number2 = random.randint(1,10)
                    number3 = random.randint(1,10)
                    right = number1 + number2 - number3
                    print('-->',number1,'+',number2,'-',number3)
                    answers = int(input())
                    if answers == right:
                        correct += 1
                    else:
                        incorrect += 1
                carryOn = input("Hit enter to display the result")
                print("%-30s%-30s"%('Correct','Incorrect'))
                print('%-30d   %-30d'%(correct,(incorrect-1)))
                carryOn = int(input("Enter 1 to continue practicing in the same difficulty level\nEnter 2 to change difficulty level\nEnter 3 to terminate "))
                if carryOn == 1:
                    mentalMaths(difficultyLevel)
                elif carryOn == 2:
                    levelSelect()
                else:
                    print("Thankyou for trying")

        elif difficultyLevel == 3:
                answers = 111
                correct = 0
                incorrect = 0
                print("Enter the correct answers(to stop press -9): ")
                while answers != -9:
                    
                    number1 = random.randint(1,10)
                    number2 = random.randint(1,10)
                    number3 = random.randint(4,40)
                    number4 = random.randint(1,10)
                    right = (number1 * number2) + number3 - number4
                    print('-->(',number1,'*',number2,')+',number3,'-',number4)
                    answers = int(input())
                    if answers == right:
                        correct += 1
                    else:
                        incorrect += 1
                carryOn = input("Hit enter to display the result")
                print("%-30s%-30s"%('Correct','Incorrect'))
                print('%-30d  %-30d'%(correct,(incorrect-1)))
                carryOn = int(input("Enter 1 to continue practicing in the same difficulty level\nEnter 2 to change difficulty level\nEnter 3 to terminate "))
                if carryOn == 1:
                    mentalMaths(difficultyLevel)
                elif carryOn == 2:
                    levelSelect()
                else:
                    print("Thankyou for trying")
        elif difficultyLevel == 4:
                answers = 111
                correct = 0
                incorrect = 0
                print("Enter the correct answers(to stop press -9): ")
                while answers != -9:
                    
                    number1 = random.randint(2,20)
                    number2 = random.randint(2,20)
                    number3 = random.randint(1,20)
                    right = (number1 * number2) + number2 - number3
                    
                    print('-->(',number1,'*',number2,')+',number2,'-',number3)
                    answers = int(input())
                    if answers == right:
                        correct += 1
                    else:
                        incorrect += 1
                carryOn = input("Hit enter to display the result")
                print("%-30s%-30s"%('Correct','Incorrect'))
                print('%-30d  %-30d'%(correct,(incorrect-1)))
                carryOn = int(input("Enter 1 to continue practicing in the same difficulty level\nEnter 2 to change difficulty level\nEnter 3 to terminate "))
                if carryOn == 1:
                    mentalMaths(difficultyLevel)
                elif carryOn == 2:
                    levelSelect()
                else:
                    print("Thankyou for trying")

        elif difficultyLevel == 5:
                answers = 111
                correct = 0
                incorrect = 0
                print("Enter the correct answers(to stop press -9): ")
                while answers != -9:
                    
                    number1 = random.randint(3,30)
                    number2 = random.randint(3,30)
                    number3 =  random.randint(3,30)
                    number4 = random.randint(3,30)
                    number5 = random.randint(3,30)
                    number6 = random.randint(1,5)
                    right = ((number1 * number5) - number2 + number3 + number4)//number6
                    print('-->((',number1,'*',number5,')-',number2,'+',number3,'+',number4,')//',number6)
                    answers = int(input())
                    if answers == right:
                        correct += 1
                    else:
                        incorrect += 1
                carryOn = input("Hit enter to display the result")
                print("%-30s%-30s"%('Correct','Incorrect'))
                print('%-30d  %-30d'%(correct,(incorrect-1)))
                carryOn = int(input("Enter 1 to continue practicing in the same difficulty level\nEnter 2 to change difficulty level\nEnter 3 to terminate "))
                if carryOn == 1:
                    mentalMaths(difficultyLevel)
                elif carryOn == 2:
                    levelSelect()
                else:
                    print("Thankyou for trying")
        else:
            print("Incorrect entry, rerun this program")

                    

def python():
    ryt = []
    wrng = []
    import random
    number1 = random.randint(1,10)
    number2 = random.randint(1,10)
    number3 = random.randint(1,10)
    number4 = random.randint(20,30)
    practice = int(input("Please enter what you would like to practice:\n1. Basics\n2. For loops\n3. While loops\n4. Lists\n5. recursion\n6. Classes\n7. Functions\n8. Mid term\n9. Final exam\n-")) 
    if practice == 9:
            mcq4(ryt,wrng)
            print('*'*80,'\n')
            list3(ryt,wrng)
            print('*'*80,'\n')
            matrix(ryt,wrng)
            mcq3(ryt,wrng)
            mcq2(ryt,wrng)
            list1(number4,ryt,wrng)
            list2(ryt,wrng)
            function2(number1,number2,number3,ryt,wrng)
            mcq1(number1,ryt,wrng)
            stringConca(number1,number2,number3,ryt,wrng)
            simpleFloorDivision(number1,number2,number3,ryt,wrng)
            recursion2(number1,number2,ryt,wrng)
            ifnotelse(number1,number2,number3,ryt,wrng)
            whileloop1(number1,ryt,wrng)
            whileloop2(number1,ryt,wrng)
            whileloop3(number1,number2,ryt,wrng)
            forloop1(ryt,wrng)
            recursion1(ryt,wrng)
            print('*'*80,'\n')
            recursion3(ryt,wrng,number1,number2)
            function1(number1,ryt,wrng)
            basic1(number4,ryt,wrng)
            basic2(number1,number2,number3,number4,ryt,wrng)
            result(ryt,wrng)
    elif practice == 2:
            forloop1(ryt,wrng)
            mcq3(ryt,wrng)
            mcq2(ryt,wrng)
            result(ryt,wrng)
            

    elif practice == 3:
            whileloop1(number1,ryt,wrng)
            whileloop2(number1,ryt,wrng)
            whileloop3(number1,number2,ryt,wrng)
            result(ryt,wrng)
            
    elif practice == 4:
            list1(number4,ryt,wrng)
            list2(ryt,wrng)
            list3(ryt,wrng)
            matrix(ryt,wrng)
            result(ryt,wrng)
            
            

    elif practice == 5:
            recursion1(ryt,wrng)
            recursion2(number1,number2,ryt,wrng)
            print('*'*80,'\n')
            recursion3(ryt,wrng,number1,number2)
            result(ryt,wrng)
           
            
    elif practice == 6:
            mcq1(number1,ryt,wrng)
            result(ryt,wrng)

    elif practice == 1:
            stringConca(number1,number2,number3,ryt,wrng)
            simpleFloorDivision(number1,number2,number3,ryt,wrng)
            ifnotelse(number1,number2,number3,ryt,wrng)
            basic1(number4,ryt,wrng)
            basic2(number1,number2,number3,number4,ryt,wrng)
            result(ryt,wrng)
            
    elif practice == 7:
            function2(number1,number2,number3,ryt,wrng)
            function1(number1,ryt,wrng)
            result(ryt,wrng)
            
    elif practice == 8:
            stringConca(number1,number2,number3,ryt,wrng)
            simpleFloorDivision(number1,number2,number3,ryt,wrng)
            ifnotelse(number1,number2,number3,ryt,wrng)
            basic1(number4,ryt,wrng)
            basic2(number1,number2,number3,number4,ryt,wrng)
            forloop1(ryt,wrng)
            mcq3(ryt,wrng)
            mcq2(ryt,wrng)
            whileloop1(number1,ryt,wrng)
            whileloop2(number1,ryt,wrng)
            whileloop3(number1,number2,ryt,wrng)
            result(ryt,wrng)

            
    else:
            print("-"*15,"Invalid entry, please try again","-"*15)
            print()
            python()
            
        
        
            
def whileloop3(number1,number2,ryt,wrng):
        x = number1
        z = number2
        while x !=0:
            y = x - 1
            while y!=0:
                z = z + 1
                y = y - 1
            x = x - 1
        print('What is the output of the following code:\nx = ',number1,'\nz = ',number2,'\nwhile x ! = 0:\n\ty = x - 1\n\twhile y ! = 0:\n\t\tz = z + 1\n\t\ty = y - 1\n\tx = x - 1\nprint(z)')
        answer = int(input())
        if answer == z:
                print('CORRECT')
                ryt.append(1)
        else:
                print("INCORRECT, the correct answer is:",z)
                wrng.append(1)
        
                
                
                
        

        
            
            
def recursion2(number1,number2,ryt,wrng):
        
        def mult(a,b):
            if a == 1:
                return b
            else:
                return b + mult(a - 1,b)
        print('*'*80,'\nWhat is the value of y?\ny = mult(',number1,',',number2,')\ndef mult(a,b):\n\tif a == 1:\n\t\treturn b\n\telse:\n\t\treturn b + mult(a-1,b)')
        y = mult(number1,number2)
        answer = int(input('-'))
        if answer == y:
                print('CORRECT')
                ryt.append(1)
        else:
                print("INCORRECT, the right answer is:",y)
                wrng.append(1)
        
                
        
                
                
def recursion1(ryt,wrng):
        import random
        number = random.randint(3,5)
        
        def factorial(n):
                if n == 1:
                    return 1
                else:
                    return n * factorial(n-1)
        print('*'*80,'\nWhat is value of yola?\nyola = factorial(',number,')\ndef factorial(n):\n\tif n == 1:\n\t\treturn1\n\telse:\n\t\treturn n*factorial(n-1)')
        answer = int(input())
        yola = factorial(number)
        if answer == yola:
                print("CORRECT")
                ryt.append(1)
        else:
                print("INCORRECT, the correct answer is:",yola)
                wrng.append(1)
                
                
                
                
            
        
            
            
def basic1(number,ryt,wrng):
        right = int(number) + float(number*5)
        print('*'*80,'\nEnter the output of:\nint(',number,') + float(',number*5,')')
        answer = float(input('-'))
        if right == answer:
                print("CORRECT")
                ryt.append(1)
        else:
                print("INCORRECT, the correct answer is: ",right)
                wrng.append(1)
                
def basic2(number1,number2,number3,number4,ryt,wrng):
        x = number1
        y = number2
        z = number3
        if x == number1:
                z = z+ 1
        elif y == number2:
                z = z - number4
        if y == number2:
                z = z + 4
                
                
        print('*'*80,'\nGive the output of:\nx = ',number1,'\ny = ',number2,'\nz = ',number3,'\nif x == ',number1,':\n\tz = z + 1\nelif y == ',number2,':\n\tz = z - ',number4,'\nif y == ',number2,':\n\tz = z + 4\nprint(z)')
        answer = int(input())
        if answer == z:
                print("CORRECT")
                ryt.append(1)
        else:
                print("INCORRECT, the correct answer is: ",z)
                
                
        
    
def recursion3(ryt,wrng,a,b):
    elements = []
    ans = []
    checker = 0
    def numberP(a,b,elements):
        if a == 0:
            return 0
        if a != 0:
            numberP(a-1,b,elements)
            elements.append(a)
    
    numberP(a,b,elements)
    length = len(elements)
    print("Enter the elements of the list elements:\na = ",a,", b = ",b,"\ndef recursion(a,b,elements):\n\tif a == 0:\n\t\treturn 0\n\tif a != 0:\n\t\tnumberP(a-1,b,elements)\n\t\telements.append(a)")
    for i in range(length):
        num = int(input('- '))
        ans.append(num)
    for j in range(length):
        if elements[j] != ans[j]:
              checker = 1
    if checker == 0:
             print("CORRECT")
             ryt.append(1)
    else:
             print("INCORRECT\nCorrect ans is  - ",elements)
             wrng.append(1)

             
             
         

def mcq4(ryt,wrng):
    import random
    shufler  = random.randint(1,3)
    if shufler == 1:
        print('def __init__(self, balance = 100, annualInterestRate = 0):\n\tself.id = type(self).__acct_num\n\tself.balance = balance\n\tself.annualInterestRate = annualInterestRate\n\ttype(self).__acct_num += 1\n\nWhat is wrong with this initializer method for the class Account(shown above)?\n1. It defines public data fields instead of private data fields\n2. It defines local variables instead of instance variables\n3. It has the incorrect number of arguments\n4. It fails to define default values for the instance variables')
        answer = int(input())
        if answer == 1:
            print("CORRECT")
            ryt.append(1)
        else:
            print("INCORRECT\nThe correct answer is option 1")
            wrng.append(1)
    elif shufler == 2:
        print('def __init__(self, balance = 100, annualInterestRate = 0):\n\tself.id = type(self).__acct_num\n\tself.balance = balance\n\tself.annualInterestRate = annualInterestRate\n\ttype(self).__acct_num += 1\n\nWhat is wrong with this initializer method for the class Account(shown above)?\n1. It has the incorrect number of arguments\n2. It defines public data fields instead of private data fields\n3. It defines local variables instead of instance variables\n4. It fails to define default values for the instance variables')
        answer = int(input())
        if answer == 2:
            print("CORRECT")
            ryt.append(1)
        else:
            print("INCORRECT\nThe correct answer is option 2")
            wrng.append(1)

    else:
        print('def __init__(self, balance = 100, annualInterestRate = 0):\n\tself.id = type(self).__acct_num\n\tself.balance = balance\n\tself.annualInterestRate = annualInterestRate\n\ttype(self).__acct_num += 1\n\nWhat is wrong with this initializer method for the class Account(shown above)?\n1. It has the incorrect number of arguments\n2. It fails to define default values for the instance variables\n3. It defines public data fields instead of private data fields\n4. It defines local variables instead of instance variables')
        answer = int(input())
        if answer == 3:
            print("CORRECT")
            ryt.append(1)
        else:
            print("INCORRECT\nThe correct answer is option 3")
            wrng.append(1)
        
            
        
            
        
    
        
    

def matrix(ryt,wrng):
    t1 = [[0,1,2],[1,10,3],[2,3,0]]
    t2 = [[10,11,12],[11,130,34],[42,33,10]]
    t3 = [[40,51,62],[11,120,34],[24,34,6]]
    t4 = [[1,10,3],[2,3,0],[0,1,2]]
    def checkDiag(aMatrix):
        for i in range(len(aMatrix)):
            if aMatrix[i][i] != 0:
                return False
        return True
    import random
    number = random.randint(1,4)
    if number == 1:
        bundle = checkDiag(t1)
        print('#Assume that aMatrix has an equal number of rows and columns\n\ndef checkDiag(aMatrix):\n\tfor i in range(len(aMatrix)):\n\t\tif aMatrix[i][i] != 0:\n\t\t\treturn False\n\treturn True\nWithout typing the code into Python,what does the function shown above return when called like this: checkDiag(',t1,')\n\n1. True\n2. None\n3. It has an index error.\n4. False\n5. It never returns: it has an infinite loop.')
        correct = 4
        userAns = int(input())
        if correct == userAns:
            print("CORRECT")
            ryt.append(1)
        else:
            print("INCORRECT\nThe correct answer is option 4")
            wrng.append(1)
    elif number == 2:
        bundle = checkDiag(t2)
        if bundle:
            opposite = False
        else:
            opposite = True
            
        print('#Assume that aMatrix has an equal number of rows and columns\n\ndef checkDiag(aMatrix):\n\tfor i in range(len(aMatrix)):\n\t\tif aMatrix[i][i] != 0:\n\t\t\treturn False\n\treturn True\nWithout typing the code into Python,what does the function shown above return when called like this: checkDiag(',t2,')\n\n1.',bundle,'\n2. None\n3. It has an index error.\n4.',opposite,'\n5. It never returns: it has an infinite loop.')
        correct = 1
        userAns = int(input())
        if correct == userAns:
            print("CORRECT")
            ryt.append(1)
        else:
            print("WRONG\nThe correct answer is ",bundle)
            wrng.append(1)
    elif number == 3:
        bundle = checkDiag(t3)
        if bundle:
            opposite = False
        else:
            opposite = True
            
        print('#Assume that aMatrix has an equal number of rows and columns\n\ndef checkDiag(aMatrix):\n\tfor i in range(len(aMatrix)):\n\t\tif aMatrix[i][i] != 0:\n\t\t\treturn False\n\treturn True\nWithout typing the code into Python,what does the function shown above return when called like this: checkDiag(',t3,')\n\n1. None\n2.',bundle,'\n3. It has an index error.\n4.',opposite,'\n5. It never returns: it has an infinite loop.')
        correct = 2
        userAns = int(input())
        if correct == userAns:
            print("CORRECT")
            ryt.append(1)
        else:
            print("WRONG\nThe correct answer is ",bundle)
            wrng.append(1)

    else:
        bundle = checkDiag(t4)
        if bundle:
            opposite = False
        else:
            opposite = True
            
        print('#Assume that aMatrix has an equal number of rows and columns\n\ndef checkDiag(aMatrix):\n\tfor i in range(len(aMatrix)):\n\t\tif aMatrix[i][i] != 0:\n\t\t\treturn False\n\treturn True\nWithout typing the code into Python,what does the function shown above return when called like this: checkDiag(',t4,')\n\n1. None\n2. It has an index error\n3.',bundle,'\n4.',opposite,'\n5. It never returns: it has an infinite loop.')
        correct = 3
        userAns = int(input())
        if correct == userAns:
            print("CORRECT")
            ryt.append(1)
        else:
            print("WRONG\nThe correct answer is ",bundle)
            wrng.append(1)
        




def result(ryt,wrng):
    totalCorrect =  sum(ryt)
    totalIncorrect = sum(wrng)
    enter = input('\nHit enter to view your result')
    print("%-20s%-20s"%('Correct','Incorrect'))
    print("%-20d%-20d"%(totalCorrect,totalIncorrect))
        
    


def list3(ryt,wrng):
    import random
    number = random.randint(1,3)
    table1 = [['T','U','V'],['W','X','Y']]
    table2 = [['QQ','DF','CD'],['VF','BG','NH']]
    table3 = [['1','2','3'],['22','33','2221']]
    if number == 1:
        correct = 1
        print('Table1: ',end='')
        print(table1,'\nWhich statement will display U?\n1. print(table1[0][1])\n2. print(table1[1][2])\n3. print(table1[0][0])\n4. print(table1[1][0])')
        userAns = int(input())
        if correct == userAns:
            print("CORRECT")
            ryt.append(1)
        else:
            print("INCORRECT.\nThe correct answer is option 1")
            wrng.append(1)
    elif number == 2:
        correct = 3
        print('Table2: ',end='')
        print(table2,'\nWhich statement will display VF?\n1. print(table1[1][0])\n2. print(table2[1][2])\n3. print(table2[1][0])\n4. print(table2[0][0])')
        userAns = int(input())
        if correct == userAns:
            print("CORRECT")
            ryt.append(1)
        else:
            print("INCORRECT.\nThe correct answer is option 3")
            wrng.append(1)
        
    else:
        correct = 2
        print('Table3: ',end='')
        print(table3,'\nWhich statement will display 2221?\n1. print(table3[0][0])\n2. print(table3[1][2])\n3. print(table3[1][0])\n4. print(table3[1][0])')
        userAns = int(input())
        if correct == userAns:
            print("CORRECT")
            ryt.append(1)
        else:
            print("INCORRECT.\nThe correct answer is option 2")
            wrng.append(1)
        
            
        
    
    


def mcq3(ryt,wrng):
    import random
    number = 1
    if number == 1:
        print('*'*80,'\nFrom the statements given below which statement prints the first n even numbers\n\n1. for i in range(0,n):\n\tif i % 2 == 0:\n\t\tprint(i)\n\n2. for i in range(0,n):\n\tif 2 % i == 0:\n\t\tprint(i)\n\n3. for i in range(n,0):\n\tif i % i == 0:\n\t\tprint(i)\n\n4. for i in range(0,n):\n\tprint(i)')
        inputt = int(input("- "))
        if inputt == 1:
            print('CORRECT')
            ryt.append(1)
        else:
            print('INCORRECT.\nThe correct answer is option 2')
            wrng.append(1)

    elif number == 2:
        print('*'*80,'\nFrom the statements given below which statement prints the first n even numbers\n\n1. for i in range(0,n):\n\tif 2 % i == 0:\n\t\tprint(i)\n\n2. for i in range(0,n):\n\tif i % 2 == 0:\n\t\tprint(i)\n\n3. for i in range(n,0):\n\tif i % i == 0:\n\t\tprint(i)\n\n4. for i in range(0,n):\n\tprint(i)')
        inputt = int(input("- "))
        if inputt == 2:
            print('CORRECT')
            ryt.append(1)
        else:
            print('INCORRECT.\nThe correct answer is option 2')
            wrng.append(1)

    else :
        print('*'*80,'\nFrom the statements given below which statement prints the first n even numbers\n\n1. for i in range(0,n):\n\tif 2 % i == 0:\n\t\tprint(i)\n\n2. for i in range(n,0):\n\tif i % 2 == 0:\n\t\tprint(i)\n\n3. for i in range(0,n):\n\tif i % 2 == 0:\n\t\tprint(i)\n\n4. for i in range(0,n):\n\tprint(i)')
        inputt = int(input("- "))
        if inputt == 3:
            ryt.append(1)
            print('CORRECT')
        else:
            print('INCORRECT.\nThe correct answer is option 3')
            wrng.append(1)
def mcq2(ryt,wrng):
    import random
    number = random.randint(1,4)
    if number == 1:
        print('*'*80,'\nGiven a list values that contains the first ten prime numbers, which statement prints the index and value of each element in the list\n\n1. for i in range(10):\n\tprint(i,values[i])\n\n2. for i in range(11):\n\tprint(i,values[i])\n\n3. for i in range(1,11):\n\tprint(i,values[i])\n\n4. for i in range(1,10):\n\tprint(i,values[i])')
        inputt = int(input("- "))
        if inputt == 1:
            print('CORRECT')
            ryt.append(1)
        else:
            print('INCORRECT.\nThe correct answer is option 1')
            wrng.append(1)

    elif number == 2:
        print('*'*80,'\nGiven a list values that contains the first ten prime numbers, which statement prints the index and value of each element in the list\n\n1. for i in range(11):\n\tprint(i,values[i])\n\n2. for i in range(10):\n\tprint(i,values[i])\n\n3. for i in range(1,10):\n\tprint(i,values[i])\n\n4. for i in range(1,11):\n\tprint(i,values[i])')
        inputt = int(input("- "))
        if inputt == 2:
            print('CORRECT')
            ryt.append(1)
        else:
            print('INCORRECT.\nThe correct answer is option 2')
            wrng.append(1)

    
    elif number == 3:
        print('*'*80,'\nGiven a list values that contains the first ten prime numbers, which statement prints the index and value of each element in the list\n\n1. for i in range(1,11):\n\tprint(i,values[i])\n\n2. for i in range(1,10):\n\tprint(i,values[i])\n\n3. for i in range(10):\n\tprint(i,values[i])\n\n4. for i in range(11):\n\tprint(i,values[i])')
        inputt = int(input("- "))
        if inputt == 3:
            print('CORRECT')
            ryt.append(1)
        else:
            print('INCORRECT.\nThe correct answer is option 3')
            wrng.append(1)

    else:
        print('*'*80,'\nGiven a list values that contains the first ten prime numbers, which statement prints the index and value of each element in the list\n\n1. for i in range(1,11):\n\tprint(i,values[i])\n\n2. for i in range(1,10):\n\tprint(i,values[i])\n\n3. for i in range(11):\n\tprint(i,values[i])\n\n4. for i in range(10):\n\tprint(i,values[i])')
        inputt = int(input("- "))
        if inputt == 4:
            print('CORRECT')
            ryt.append(1)
        else:
            print('INCORRECT.\nThe correct answer is option 4')
            wrng.append(1)
        
   
    
def list2(ryt,wrng):
    import random
    number = random.randint(1,3)
    wordList1 = ['Alabama','Arkansas','Connecticut','Idaho','New Jersey','New York','Delaware','Arizona']
    wordList2 = ['Alberta','Labrador','Nova Scotia','Nunavut','Manitoba','Newfoundland','Quebec','Yukon']
    wordList3 = ["Wyoming","Washington","West Virginia","Idaho","Arkansas","Newfoundland","Delaware","Arizona","Alberta","Labrador"]
    if number == 1:
        print('*'*80,'\nGiven the following code snippet, what is the content of the list bums?\nbums = ',wordList1,'\nbums.pop(4)\n\n1. wordList1 = ["Alabama","Arkansas","Connecticut","Idaho","New Jersey","New York","Delaware","Arizona"]\n2. []\n3. wordList1 = ["Alabama","Arkansas","Connecticut","Idaho","New York","Delaware","Arizona"]\n4. wordList1 = ["Arkansas","Connecticut","Idaho","New York","Delaware","Arizona"]')
        userAns = int(input('- '))
        if userAns == 3:
            print('CORRECT')
            ryt.append(1)
        else:
            print('INCORRECT.\nThe correct answer is option 3')
            wrng.append(1)
    elif number == 2:
        print('*'*80,'\nGiven the following code snippet, what is the content of the list bums?\nbums = ',wordList2,'\nbums.pop(2)\n\n1. wordList2 = ["Alberta","Labrador","Quebec","Yukon"]\n2. wordList2 = ["Alberta","Labrador","Nunavut","Manitoba","Newfoundland","Quebec","Yukon"]\n3. wordList2 = ["Nova Scotia","Nunavut","Manitoba","Newfoundland","Quebec","Yukon"]\n4. wordList1 = []')
        userAns = int(input('- '))
        if userAns == 2:
            print('CORRECT')
            ryt.append(1)
        else:
            print('INCORRECT.\nThe correct answer is option 2')
            wrng.append(1)
    
    else:
        print('*'*80,'\nGiven the following code snippet, what is the content of the list bums?\nbums = ',wordList3,'\nbums.pop(6)\nbums.pop(1)\n\n1. wordList3 = ["Wyoming","West Virginia","Idaho","Arkansas","Newfoundland","Arizona","Alberta","Labrador"]\n2. wordList3 = ["Wyoming","West Virginia","Idaho","Arkansas","Newfoundland","Delaware","Arizona","Alberta","Labrador"]\n3. wordList3 = ["Wyoming","West Virginia","Idaho","Arkansas","Alberta","Labrador"] \n4. wordList3 = []')
        userAns = int(input('- '))
        if userAns == 1:
            print('CORRECT')
            ryt.append(1)
        else:
            print('INCORRECT.\nThe correct answer is option 1')
            wrng.append(1)
        
            
            
    
def list1(number4,ryt,wrng):
    
    letters = []
    for i in range(number4):
        letters.append(chr(i+97))
    print('*'*80,'\nsomeList = ',letters)
    highest = letters[number4 - 1]
    print('Given the list above, what are the upper and lower bounds(lowest and highest index)?\n1. 0,',number4-3,'\n2. 0,',number4-2,'\n3. 0,',number4-1,'\n4. 0,',number4)
    userAns = int(input("- "))
    if userAns == 3:
        print('CORRECT')
        ryt.append(1)
    else:
        print("INCORRECT.\nThe correct answer is option 3")
        wrng.append(1)
        print()
        
    
    
    

def function2(number1,number2,number3,ryt,wrng):
    right = []
    userAns = []
    def watch1(d):
        c  = v + d + watch2(d)
        return c
    def watch2(c):
        v = c * 2
        c = c + v + 1
        d = c
        return d
    v = number2
    c = number3
    d = number1
    v = watch1(v)
    right.append(v)
    right.append(c)
    right.append(d)
    print('*'*80,'\ndef f1(d):\n\tc = v + d + f2(d)\n\treturn c\ndef f2(c):\n\tv = c * 2\n\tc = c+v+1\n\td = c\n\treturn d\nv = ',number2,'\nc = ',number3,'d = ',number1,'\nv = f1(v)\nprint(v,c,d)\nWhat is the value of v, c, d?(Ans in the same order)')
    for i in range(len(right)):
        inputt = int(input('- '))
        userAns.append(inputt)
    checker = 0
    for j in range(len(right)):
        if right[j] == userAns[j]:
            checker = 1
        else:
            checker = -1
    if checker == 1:
        print("CORRECT")
        ryt.append(1)
    else:
        print("INCORRECT.\nCorrect - : ",end='')
        print(right)
        wrng.append(1)
    
        
            
        
            
            
            





def mcq1(n,ryt,wrng):
    print('*'*80,'\nWhich function header best matches the following function call?\nResult = whichMethod(',n,',"%1d'%(n*8+2),'", True)\n1. def whichMethod():\n2. def whichMethod(intNum,boolValue,code):\n3. def whichMethod(boolValue,code,intNum): \n4. def whichMethod(boolValue,code,intNum):\n5. def whichMethod(intNum,code,boolValue):')
    answer = int(input())
    if answer == 5:
        print('CORRECT')
        ryt.append(1)
    else:
        print('INCORRECT.\nThe correct answer is option 5')
        wrng.append(1)

        
        
    
    


def function1(number1,ryt,wrng):
    def bums1(v):
        v = v + 1 + bums2(v)
        return v
    def bums2(v):
        return v + 1
    v = number1
    v = bums1(v)
    right = v
    print('*'*80,'\ndef function1(v):\n\tv = v + 1 + function2(v)\n\treturn v\ndef function2(v):\n\treturn v + 1\nv = ',number1,'v = function1(v)\nprint(v)\nWhat is the value of v?')
    answer = int(input())
    if answer == right:
        print('CORRECT: ',right)
        ryt.append(1)
    else:
        print('INCORRECT.\nThe correct answer is: ',right)
        wrng.append(1)

    
    

    

def whileloop2(number1,ryt,wrng):
    right = []
    userAns = []
    checker = 0
    x = number1
    while x > 0:
        sum = 1
        y = x
        while y > 0:
            sum += x
            y = y - 1
        right.append(sum)
        x -= 1
    print('*'*80,'\nx = ',number1,',total = []\nwhile x > 0:\n\tsum = 1\n\ty = x\n\twhile y > 0:\n\t\tsum = sum + x\n\t\ty = y - 1\n\ttotal.append(sum)\n\tx = x - 1\nWhat is the value of the list total?')
    for i in range(number1):
        inputt = int(input("- "))
        userAns.append(inputt)
    for j in range(number1):
        if userAns[j] == right[j]:
            checker = 0
        else:
            checker = -1
    if checker == 0:
        print("CORRECT: ",end='')
        print(right)
        ryt.append(1)

    else:
        print("INCORRECT.\nThe correct answer is: ",end='')
        print(right)
        wrng.append(1)
        
            
            
            
        
        
        
            
        
    


def forloop1(ryt,wrng):
    import random
    limit = random.randint(1,2)
    start = random.randint(4,20)
    limit = limit * (-1)
    listN = []
    listC = []
    for i in range(start,1,limit):
        listN.append(i)

    print('*'*80,'\nlistN = []\nfor i in range(',start,',1,',limit,'):\n\tlistN.append(i)\nState the values of the listN(Hint: There are as many values as many dashes you have to fill')
    if limit == -1:
        for j in range(start-1):
            inputt = int(input('- '))
            listC.append(inputt)
    else:
        for j in range(start//2):
            inputt = int(input('- '))
            listC.append(inputt)
        
   
    
    length = 0
    checker = 0
    while length != len(listN):
        if listN[length] == listC[length]:
            #This section needs revision.
            checker = 1
        else:
            checker = -1
        length += 1
            
    if checker == 1:
        print('CORRECT: ')
        ryt.append(1)
    else:
        print('INCORRECT.\nThe correct answer is: ',end ='')
        print(listN)
        wrng.append(1)
        
            
            
            
            
        
    
    
    

def whileloop1(number,ryt,wrng):
    x = number
    odd = 0
    even = 0
    while number!=0:
        number -=1
        if number%2 == 1:
            odd +=1
        else:
            even +=1
    print('*'*80,'\nodd = 0\neven = 0\nx = ',x,'\nwhile x!=0:\n   x = x - 1\n   if x%2 == 1:\n       odd += 1\n   else:\n       even += 1')
    oddUser = int(input('Odd - :'))
    evenUser = int(input('Even - :'))
    if oddUser == odd and evenUser == even:
        print('CORRECT')
        ryt.append(1)
    else:
        print('INCORRECT\nOdd - ',odd,' Even - ',even)
        wrng.append(1)
        
     
def ifnotelse(number1,number2,number3,ryt,wrng):
    if not (number1 < number2):
        number1 = number1 - 51
    if not (number1>number3):
        number1 = number1 + 26
    print('*'*80,'\nnumber1 = ',number1,'\nnumber2 = ',number2,'\nnumber3 = ',number3,'\nif not (number1 < number2):\n\tnumber1 = number1 - 51\nif not (number1 > number3):\n\tnumber1 = number1 + 26\nprint(number1)')
    answers = int(input())
    if answers == number1:
          print('CORRECT')
          ryt.append(1)
    else:
          print('INCORRECT.\nThe correct answer is:',number1)
          wrng.append(1)
                  
    

def simpleFloorDivision(number1,number2,number3,ryt,wrng):
        right = number1//number2//number3
        print('*'*80,'\n',number1,'//',number2,'//',number3)
        answers = int(input())
        if answers == right:
            print('CORRECT')
            ryt.append(1)
        else:
            print('INCORRECT.\nThe correct answer is:',right)
            wrng.append(1)

            
    
    
def stringConca(number1,number2,number3,ryt,wrng):
        right = str(number1)+str(number2)+str(number3)
        print('*'*80,'\n"',number1,'+',number2,'+',number3,'"')
        answers = input()
        if answers == right:
            print('CORRECT')
            ryt.append(1)
        else:
            print('INCORRECT.\nThe correct answer is:',right)
            wrng.append(1)
            
            
              
tests()
