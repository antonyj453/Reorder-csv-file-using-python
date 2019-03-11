import csv

with open('/home/uvionics/data/Latest_mar6/shoppe_result/reoder/shopee_milkformula_SG_2019-01-07_sku.csv', 'r') as infile, open('/home/uvionics/data/Latest_mar6/shoppe_result/reoder/shopee_milkformula_SG_2019-01-07_sku_reorder.csv', 'a') as outfile:
    # output dict needs a list for new column ordering
    fieldnames = ['Channel', ' Product_number', ' p_no:_without_models', ' IND_Date & Time', ' SGP_Date & Time',' Category',' Product_Name',' Variation_name','Product_url',' Item_Id',' Shop_Id',' Model_id',' SKU',' Currency',' Selling_Price',' Original_price',' Discount',' Sold',' Brand',' Brand_id',' Expiry',' Seller_name ',' Stock']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    # reorder the header first
    writer.writeheader()
    for row in csv.DictReader(infile):
        # writes the reordered rows to the new file
        writer.writerow(row)
