hex = input('Enter hex: ').lstrip('#')
rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
print(rgb)
inverse_rgb = tuple(int((255**2-int(rgb[i])**2)**(1/2)) for i in range(3))
print(inverse_rgb)
inverse_hex = '%02x%02x%02x' % inverse_rgb
print(inverse_hex)