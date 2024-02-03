from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
import time
#def encrypt_and_display_data(data, matrix):
  # Encrypt data
 #   encrypted_data = data.encode('utf-8').hex()
    
    # Create a color-coded pattern from the encrypted data
  #  pattern = [int(encrypted_data[i:i+2], 16) for i in range(0, len(encrypted_data), 2)]
    
    # Display on the 8x8 Dot Matrix
   # with canvas(matrix) as draw:
    #    for i in range(min(len(pattern), 64)):
     #       row = i// 8
      #      col = i % 8
       #     draw.point((col, row), fill=pattern[i])
    
    #matrix.show()
    # Flash the hexadecimal value on the MAX7219 LED matrix
    
def string_to_hex_and_flash(string, matrix):
    # Convert the string to hexadecimal
    hex_value = string.encode('utf-8').hex()

    for _ in range(5):  # Flash three times
        with canvas(matrix) as draw:
            for i, hex_digit in enumerate(hex_value):
                row = i // matrix.width
                col = i % matrix.width
                draw.text((col, row), hex_digit, fill="white")

        matrix.show()
        time.sleep(5)  # Display for 1 second

        with canvas(matrix) as draw:
            matrix.show()  # Clear the display
        time.sleep(1)  # Pause for 1 second before the next flash

# Example Usage
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)
data_to_encrypt = "Ã¿"
string_to_hex_and_flash(data_to_encrypt, device)
#encrypt_and_display_data(data_to_encrypt, device)