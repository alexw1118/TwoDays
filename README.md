# TwoDays

SRS/Scenario
Admin (contract management)
- batch upload property (frontend show, backend required SFTP job(not cover in demo))
- upload property purchase contract (frontend show, backend required SFTP job(not cover in demo))
- view all property list
- update property details (optional)
- view all request for purchase list
- permit property purchase

Landlord (buyer)
- view all the property uploaded by admin in list (where ownership = null)
- search and filter property list
- view property purchase contract
- request for permit to purchase property - landlord will require to upload necessay document to gain approval from admin (contract signed and uploaded here)
- purchase property (by unit) - after permitted, the landlord will able to buy property and once purchasing is done he/she will be the owner of the property
- view all the property owned by him/herself - will not show the sold property (sold property will be soft deleted)
- update the property owned by him/herself - furnish level, usage, rent price, sell price, etc.
- upload the image of the property (unit/house)
- view property details - include the billing statement (whether the tenant paid the rent)
- upload rental contract(for tenant)/selling contract(for buyer)
- view rent request list, approve rent request, update the rent period, set the start date and end date
- view purchase request list, approve purchase request
*buyer can contact landlord to buy the unit/house from landlord (buyer purchase ownership and signed contract)
- view all the property available for sales (where usage = for sell, for both)
- upload/send the signed contract to landlord to request for purchase
- purchase the property - after approval of landlord, make payment
- contact landlord

Tenant
- view all the property list owned by different landlord (where usage = for rent and date > rentenddate)
- search and filter property list 
- view the rental contract
- contact landlord
- upload/send the signed contract to landlord to request for rent
- rent the owned property - after landlord approved, tenant will need to pay deposit
- pay rental
- check bill
