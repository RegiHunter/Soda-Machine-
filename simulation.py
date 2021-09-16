from coins import Coin
from soda_machine import SodaMachine
from customer import Customer
import user_interface

class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        """The central method called in main.py."""
        customer = Customer()
        soda_machine = SodaMachine()
        will_proceed = True
        while will_proceed:
            user_option = user_interface.simulation_main_menu()
            if user_option == 0:
                soda_machine.begin_transaction(customer)
            if user_option == 1:
                customer.check_coins_in_wallet(Coin)
            elif user_option == 2:
                customer.check_backpack()
            elif user_option == 3:
                will_proceed = False
