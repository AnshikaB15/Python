
import MyAccount

try:
    anshul = MyAccount.Account(101, "Anshul Navale", "Savings", 1500)
    print(anshul)
    anshul.deposit(400)
    print(anshul)

    print()

    rohan = MyAccount.Account(201, "Rohan Vanteri", "Checking", 1200)
    print(rohan)

    rohan.withdrawal(1000)
    print(rohan)

except MyAccount.OpeningAccountDepositAmountException as e:
    print(e)
    print("Please go back to your home, get at least 1000 and then we will talk...")

except MyAccount.DepositAmountNotIntegerException as e:
    print(e)
    print("We accept only INTEGER values for deposits/withdrawals...")

except MyAccount.DepositAmountValueNotValid as e:
    print(e)
    print("Please deposit/withdraw only POSITIVE INTEGER values....")

except MyAccount.MinimumBalanceException as e:
    print(e)
    print("Sorry, hard luck...once you give amount to us, we will never back to you...")

except Exception as e:
    print(e)

finally:
    print("\nPlease try our application once again!")
