# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44
page_count = 100
page_line = 50
line_symbol = 25
byte = 4
mbyte = 1024 ** 2
disk_size_byte = disk_size * mbyte
book_size = page_count * page_line * line_symbol * byte
amount = disk_size_byte // book_size
print("Количество книг, помещающихся на дискету:", int(amount))
