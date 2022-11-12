# ecommerce

**General Notes**

This is an simple ecommerce application made using HTML, Bootstrap, Javascript and Django. It has basic features of an ecommerce website.

- To run this project do the following:

    Pre-requisites: Python, pip and django should be installed in your system. All the coding is done using VScode.
    1. To install the dependencies: \
       `pip install -r requirements.txt` 
    2. Make the migrations:\
        `python manage.py makemigrations` 
    3. Migrate the tables: \
        `python manage.py migrate` 
    4. Create a superuser for your project: \
        `python manage.py createsuperuser`   
        This will prompt you to enter username, email and password for the superuser.  
    5. Run the server using: \
        `python manage.py runserver` 
        
- Features: \
    -> Login and register facilities. \
    -> View the products and add them to cart. \
    -> View the cart and add or delete quantity of items as per your needs. \
    -> Proceed to checkout to add delivery address and go to Paypal payment gateway for payment. 
    
- Additional feature: \
    -> Added functionality for guest users to create carts for orders without logging in by using cookies to save the cart information in their browser. 

- main page: Without logged in
![home page](https://user-images.githubusercontent.com/93663329/201495198-41b1baad-5eaf-4b57-b572-35756d414345.png)

- main page: Logged in 
![logged in home page](https://user-images.githubusercontent.com/93663329/201495208-4bbaa284-0f8f-4dc2-a882-aeff548d567d.png)

- cart page: 
![cart](https://user-images.githubusercontent.com/93663329/201495222-91e52b6a-ea9e-43ec-b151-78de8effc51a.png)

- checkout page: Not logged in
![checkout not logged](https://user-images.githubusercontent.com/93663329/201495233-44a5c813-48d3-4bef-9e79-1462bd3c6b00.png)

- checkout page: Logged in
![checkout logged in](https://user-images.githubusercontent.com/93663329/201495244-26a00ee8-1027-40fb-8472-9a81b59ae3ce.png)

- Payment gateway: 
![payment gateway](https://user-images.githubusercontent.com/93663329/201495253-b643ee5a-1fcf-4a71-97ad-694f85e229fa.png)



