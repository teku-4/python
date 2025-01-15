#try:
    #with open("file.txt","r") as file:
        # print(file.read(10))
        # print(file.readline())
        # print(file.readlines())
        # for i in file:
        #     print(i)

#except FileNotFoundError:
    #print("there is no such file ")        
# #wrtte file 
# with open("test.txt","w") as written_file:
#     written_file.write("this is written now  to oerrede if the file exist else create new file")
#file appending using 'a' mode
# with open("file.txt","a") as file:
#    file.write("this the appended file to already created file ")
# with open("test.txt","w") as file:
#     file.write("This is witten file")
##wirite and reade file at the time
# try:
#     with open("test.txt","w+") as file:
#         content=file.write("this file is written to read now at a time")
#         print(content.read())
# except Exception as e:
#     print("eror because :",e)     
# try:
#     with open("test.txt","x") as file:
#         file.write("this use to wite if the file does not exst only")
# except Exception as a:
#     print("an error because",a)
    
# deleting file
#deleting file 
# import os
# try:
#     if os.path.exists("test.txt"):
#         os.remove("test.txt")
#     else:
#         print("the file is does not exists")
# except Exception as Error:
#     print("there is an error because ",Error) 
# #deleting folder
# try:
#     os.rmdir("NEW folder")
# except Exception as r:
#     print("error because:",r)  
#try and except error
# while True:
#     balace=2000.0
#     try:

#        deposite=input("eter the deposite ammount")
#        total=balace+deposite
#        print("the tootal amount is ",total)
#        break
#     except ValueError:
#         print("plz enter the correct value")
#creating prodct fle
# def create_product():
#     with open("product.txt","x") as poducts:
        
#         poducts.write("mago, banana, aocado")
# create_product()        
    
#adding products
# def ading_products():
#     with open("products.txt","a") as poducts:
#         poducts.write("oannge,papaya and cherri are added now")
# ading_products()        
#shoping file
#creating file product
# with open("product.txt","w") as file:
#     file.write(" product_id   pro_name     pro_price   pro_quantity\n")
#     file.write(" 1            mango         200          20\n")
#     file.write(" 2            banana        300          100\n")
#     file.write(" 3            apple         400          20\n")
#     file.write(" 4            orange        500          50\n")   
# #adding products

# def adding_prduct(product_id,prouct_name,product_quantity,product_price):
#     with open("product.txt","a") as file:

#         file.write(f"\n {product_id}          {prouct_name}           {product_price}         {product_quantity}")
#     print(f"product name {prouct_name} added successfully") 
# adding_prduct(5,"avocado",700,70)       
# adding_prduct(8,"grabes",900,90)
#reading prduct from a file
# def veiw_product():
#     with open("product.txt","r") as file:
#         products=file.read()
#         print("***the products are listed as following***")
#         print(products)
# veiw_product()        
