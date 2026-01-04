# //python beginner calculator program
c=1

while c!=0:

    o= input("Enter the operator(+,-,*,/,%,^) you want to use: ")
    if o not in ["+", "-", "*", "/", "%", "^"]:
        print("Error in entering the operator")

    else:
        if o=="^":

            a= float(input("Enter the number: "))
            b= float(input(f"Enter the exponent to the entered number {a}: "))
            A=a**b
            print(f"{a}{o}{b} = {A}")

        else:
            a= float(input("Enter the first number: "))
            b= float(input("Enter the second number: "))

            if o=="+":
                A=a+b
                print(f"{a}{o}{b} = {A}")

            elif o=="-":
                A=a-b
                print(f"{a}{o}{b} = {A}")

            elif o=="*":
                A= a*b
                print(f"{a}{o}{b} = {A}")

            elif o=="/":
                if b == 0:
                    print("Error: Division by zero is not allowed!")

                else:
                    A=a/b
                    print(f"The quotient for {a}{o}{b} = {int(A)}")
                    print(f"{a}{o}{b} = {A}")

            elif o=="%":
                if b == 0:
                    print("Error: Modulo by zero is not allowed!")

                else:
                    A= a % b
                    print(f"{a}{o}{b} = {A}")

            else:
                print("Mistake in entering the operator.")

    count=1
    while count!=0:

        check=input("Enter [Yes] if you want to continue with more calculations \nand enter [No] if there is no more calculations: ")
            
        check=check.lower()

        if check=="yes":
            c=1
            count = 0

        elif check=="no":
            c=0
            count = 0

        else:
            print("Mistake while entering [Yes] or [No]. Please enter either [Yes] or [No].")
            count=1
