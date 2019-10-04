#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_steal(self):

        prod = Product('Test Product',price=1000)
        self.assertEqual(prod.stealability(), 'Very stealable!')

    def test_default_product_flame(self):

        prod = Product('Test Product',flammability=10)
        self.assertEqual(prod.explode(), '...BABOOM!!!')


class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        """Test default number of product weight being 30."""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        r = generate_products()
        for product in r:
            first = product.name.split()[0]
            second = product.name.split()[1]
            self.assertIn(first,ADJECTIVES)
            self.assertIn(second,NOUNS)






if __name__ == '__main__':
    unittest.main()