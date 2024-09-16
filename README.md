# OOP course homework

## Initialized with poetry

### General for the last version:
    
    > Example of working with new functionality at main.py
    > Current test coverage: 100%

## v4.0:

### Module 'src/submodels.py':

    > added LawnGrass and Smartphone as Product subclasses,
        their constructors and tests

### Module 'src/models.py':

    > Validation of Product adding magic method changed

## v3.0:

### Module 'src/models.py':

    > added Product adding and string magic methods
    > added Category string magic method, products getter optimized

## v2.0:

### Module 'src/models.py':

    > added Product price field getter and setter, made field private
    > added Category products field getter, made field private

    > added Product new_product class method to init Product with dictionary
    > added Category add_product method to append its products

### General:

    > Typos fixed

## v1.0:

### Module 'src/models.py':

    > added class Product with following object fields:
        - name
        - description
        - price
        - quantity
    > added class Category with following object fields:
        - name
        - description
        - products (list of Product objects)
    > added counting general numbers of products
    and categories in class Category fields:
        - product_count
        - categoriy_count

### Module 'src/fileio.py':

    > added from json file reading categories and transforming them
    to objects function read_json

### _sky.pro // indpd58.0 // Belin Mikhail_