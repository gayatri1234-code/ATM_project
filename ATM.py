class ATM:
   def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()
   def menu(self):
       print(""" How can i help you?
       1.create pin
       2.change pin
       3.withdraw
       4.Deposit
       5.Check balance
       6.Exit
       """)
       a=input("enter your choise")
       if a=='1':
           self.create_pin()
           self.menu()
       elif a=='2':
           self.change_pin()
           self.menu()
       elif a=='3':
           self.withdraw()
           self.menu()
       elif a=='4':
            self.deposit()
            self.menu()
       elif a=='5':
            self.check_balance()
            self.menu()
       elif a=='6':
           print("thank you")
       else :
           print(" Invalid input")
   def create_pin(self):
        self.pin=input("enter your pin")
        
   def change_pin(self):
        old_pin=input("enter your old pin")
        if old_pin==self.pin:
         self.pin=input("enter your new pin")
        else:
            print("wrong pin")
            
   def withdraw(self):
        old_pin=input("enter your old pin")
        if old_pin==self.pin:      
           if self.balance > 0:
               withdraw=int(input("enter amount"))
               if withdraw < self.balance:
                  self.balance=self.balance-withdraw
                  print("new balance is",self.balance)
               else:
                   print("low balance")
           else:
             print("low balance")   
   def deposit(self):
        old_pin=input("enter your old pin")
        if old_pin==self.pin: 
          deposit=int(input("enter amount"))
          self.balance=self.balance + deposit
          print("your current balance is=", self.balance)
        else:
           print("wrong pin")
   def check_balance(self):
        old_pin=input("enter your old pin")
        if old_pin==self.pin: 
          print("your current balance is=", self.balance)
        else:
           print("wrong pin")
           
a=ATM()          

