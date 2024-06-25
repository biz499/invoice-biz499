from django.db import models

class Size(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=20)
    size = models.ManyToManyField(Size, help_text="Create or Select sizes related to this Product(e.g., xl,xxl,xxxl)")

    def __str__(self):
        return self.title


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.title} - {self.size.title}: {self.price}"


class CompanyDetail(models.Model):
    company_name = models.CharField(max_length=20)
    gst_number = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    pan = models.CharField(max_length=20)
    billing_address = models.CharField(max_length=20)

    def __str__(self):
        return self.company_name


class Order(models.Model):
    company = models.ForeignKey(CompanyDetail, default=None, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='InvoiceItem')
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, help_text="Discount in percentage (e.g., 10 for 10%)")

    def __str__(self):
        return self.company.company_name


class InvoiceItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price_product_size = models.ForeignKey(Price, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.product.title} - {self.size.title} - Quantity: {self.quantity} - Quantity: {self.price_product_size}"
    
    def get_price(self):
        return self.price_product_size.price
    get_price.short_description = 'Price'
