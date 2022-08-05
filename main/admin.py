from django.contrib import admin
from .models import UserDetail, Cart
<<<<<<< HEAD
from seller.models import Product,ProductSize,SellerDetail, category, MyCart, Orders
=======
from seller.models import Product,SellerDetail, category, MyCart, Orders
>>>>>>> 5ff1561f39af3cd9c554e4ce363d14387ccc10b3

admin.site.site_header = 'Kriti-Vity'

admin.site.register(UserDetail)
admin.site.register(Product)
<<<<<<< HEAD
admin.site.register(ProductSize)
=======
# admin.site.register(ProductSize)
>>>>>>> 5ff1561f39af3cd9c554e4ce363d14387ccc10b3
admin.site.register(SellerDetail)
# admin.site.register(Slider)
admin.site.register(category)
# admin.site.register(dow)
# admin.site.register(Contact)
# admin.site.register(SellerSlider)
admin.site.register(MyCart)
# admin.site.register(WholeSaleProduct)
# admin.site.register(WholeSaleProductOrders)
admin.site.register(Cart)
admin.site.register(Orders)
# admin.site.register(trend)