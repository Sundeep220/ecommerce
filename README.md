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
    -> Proceed to checkout to add delivery address and go to Paypal payment gateway for payment. \
    
- Additional feature: \
    -> Added functionality for guest users to create carts for orders without logging in by using cookies to save the cart information in their browser. \
