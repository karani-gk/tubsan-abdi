# Copyright (c) 2023, Geoffrey Karani and contributors
# For license information, please see license.txt

import frappe
from erpnext.accounts.utils import get_balance_on


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    
    return  columns, data


def get_data(filters):
    fetch_query = """
		SELECT    
			(
       			SELECT SUM(grand_total) 
   				FROM `tabSales Invoice` si
       			WHERE si.status <> 'Draft' AND si.status <> 'Cancelled'
     		)
          		AS sales,
            
            (
                SELECT SUM(paid_amount) 
   				FROM `tabPayment Entry` pe
				WHERE pe.status <> 'Draft' AND pe.status <> 'Cancelled'
       		) 
          		AS payments,
      
   			(
          		SELECT SUM(outstanding_amount) 
   				FROM `tabSales Invoice` si 
       			WHERE si.status <> 'Paid' AND si.status <> 'Draft' AND si.status <> 'Cancelled'
          	) 
          		AS credits
       	FROM 
        	`tabSales Invoice` AS si
		LIMIT 1
    """
    
    data = frappe.db.sql( fetch_query )
    
    return data


def get_columns():
    return [
		"Sales:Currency:165",
 		"Payments:Currency:150",
		"Credits:Currency:100"
	]
    
    
    
def get_balances():
    customers = frappe.db.get_all("Customer")
    
    total_balance = 0
    for customer in customers:
        balance =  get_balance_on(party_type="Customer", party=customer)
        total_balance = total_balance + balance
        
        return total_balance