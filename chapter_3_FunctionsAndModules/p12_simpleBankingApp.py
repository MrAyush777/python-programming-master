balance = 0.0
kyc_documents = {}

def checkBalance():
    print(f"\nyour current balance is {balance}\n")


def deposit(amount):
    global balance
    if amount > 0: # here user not allowed to enter negative value...
        balance += amount
    else:
        print("\ncan'not deposit a negative amount...\n")
    
def withdraw(amount):
    global balance
    if amount <= 0:
        print("\ncan'not withdraw a negative amount...\n")  
    elif amount > balance:
        print("\ninsufficient balance...\n")
    else:
        balance -= amount
    
def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    
    if len(kyc_documents) == 0:
        print("\n kyc not done...")
    else:
        for doc in kyc_documents:
            print(f"{doc} : {kyc_documents[doc]} ")
    

if __name__ == "__main__":
    
    print("welcome to Kotak Bank...")

    while True:
        print("1. check balance")
        print("2. deposit amount")
        print("3. withdraw amount")
        print("4. check kyc") 
        print("5. update kyc") 
        print("6. exit") 
        
        choice = input("enter you choice between 1 and 6 : ")

        if choice == '1': 
            checkBalance()
        elif choice == '2':
            amount = float(input("enter the amount to deposit : "))
            deposit(amount)
            print("amount of rs{amount}  deposited successfullly...")
        elif choice == '3':
            amount = float(input("enter the amount to withdraw : "))
            withdraw(amount)
        elif choice == '4':
            check_kyc() 
        elif choice == '5':
            kyc_docs = {}
            n_documents = int(input("enter the number of documents you want to update : "))
            for i in range(n_documents):
                key = input("enter the document type : ")
                value = input("enter the document number : ")
                kyc_docs[key] = value
            update_kyc(kyc_docs)
            print("kyc updated successfully...")
        elif choice == '6':
            print("quiting have a nice day...")
            break
        else:
            print("invalid choice...Retry")

    print("thank you for using our banking app...")
