import frappe
from erpnext.accounts.utils import get_balance_on

@frappe.whitelist()
def get_outstanding_balance(customer):
    
    current_balance =  get_balance_on(party_type="Customer", party=customer)
    
    return current_balance