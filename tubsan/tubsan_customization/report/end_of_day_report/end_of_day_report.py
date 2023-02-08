# Copyright (c) 2023, Geoffrey Karani and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    
    return  columns, data


def get_data(filters):
    
    from_date, to_date = filters.get('from'), filters.get('to')
    
    conditions = "1=1"
    if(filters.get('customer_group')):conditions += f" AND c.customer_group='{filters.get('customer_group')}' "
    if(filters.get('territory')):conditions += f" AND c.territory='{filters.get('territory')}' "
    
    
    fetch_query = f"""
		SELECT
			(
       			SELECT SUM(grand_total) 
   				FROM `tabSales Invoice` si
				JOIN tabCustomer AS c ON c.name=si.customer WHERE {conditions} AND (si.posting_date BETWEEN '{from_date}' AND '{to_date}')
       			AND si.status <> 'Draft' AND si.status <> 'Cancelled'
     		)
          		AS sales,
            
            (
                SELECT SUM(paid_amount) 
   				FROM `tabPayment Entry` pe
       			JOIN tabCustomer AS c ON c.name=pe.party_name WHERE {conditions} AND (pe.posting_date BETWEEN '{from_date}' AND '{to_date}')
				AND pe.status <> 'Draft' AND pe.status <> 'Cancelled'
       		) 
          		AS payments,
      
   			(
          		SELECT SUM(outstanding_amount) 
   				FROM `tabSales Invoice` si 
				JOIN tabCustomer AS c ON c.name=si.customer WHERE {conditions} AND (si.posting_date BETWEEN '{from_date}' AND '{to_date}')
       			AND si.status <> 'Paid' AND si.status <> 'Draft' AND si.status <> 'Cancelled'
          	) 
          		AS credits
       	FROM 
        	`tabSales Invoice` AS si
        JOIN 
        	tabCustomer AS c
		ON 
  			c.name=si.customer
		WHERE
  			{conditions}
		AND (si.posting_date BETWEEN '{from_date}' AND '{to_date}')
		LIMIT 1
    """
    
    data = frappe.db.sql( fetch_query )
    
    return data


def get_columns():
    return [
		"Total Sales:Currency:165",
 		"Payments Received:Currency:150",
		"Unpaid Invoices:Currency:150"
	]