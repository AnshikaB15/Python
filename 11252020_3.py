"""
    Class imitating Salesman functionality.
    
        FYI -
                sales amount = units sold * unit price
                commission calculation
                    sales amount    commission
                    ============    ==========
                     > 15000           10% of sales amount
                     > 10000            7% of sales amount
                     >  6000            4% of sales amount
                     Otherwise          1% of sales amount
"""

class Salesman:







rob = Salesman(100, "Robert", "Hurley", "Phoenix")
rob.set_units_sold(20)
rob.set_unit_price(1000)
rob.find_sales_amount()
rob.find_commission()
rob.print_results()


jack = Salesman(100, "Jack", "Huntington", "Los Angeles")
jack.set_units_sold(30)
jack.set_unit_price(500)
jack.find_sales_amount()
jack.find_commission()
jack.print_results()



