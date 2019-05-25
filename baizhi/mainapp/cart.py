# class Cartltem():
#     def __init__(self,book,amount):
#         self.amount = amount
#         self.book = book
#         self.status = 1
#
#
# class Cart():
#     def __init__(self):
#         self.save_price = 0
#         self.total_price = 0
#         self.cartltem = []
#         #计算购物车中上面的节省金额和总金额
#
#
#     def sums(self):
#         self.total_price = 0
#         self.save_price = 0
#         for i in self.cartltem:
#             self.total_price += i.book.dangdang_price * i.amount
#             self.save_price += (i.book.dangdang_price - i.book.dangdang_price)*i.amount
#
#
#         #向购物车中添加书籍
#     def add_book_toCart(self,book,count=1):
#         for i in self.cartltem:
#             if i.book.id == book.id:
#                 i.amount += count
#                 self.sums()
#                 return None
#         self.cartltem.append(Cartltem(book,count))
#         self.sums()
#
#         #修改购物成的商品信息
#     def modify_cait(self,book,amount):
#         for i in self.cartltem:
#             if i.book.id == book.id:
#                 i.amount =amount
#         self.sums()
#         #删除购物车
#     def delete_book(self,book):
#         for i in self.cartltem:
#             if i.book.id == book.id:
#                 self.cartltem.remove(i)
#         self.sums()