from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# 要加密的内容
data = "123456"
# 随机生成16字节（即128位）的加密密钥
key = get_random_bytes(16)
# 实例化加密套件，使用CBC模式
cipher = AES.new(key, AES.MODE_CBC)
# 对内容进行加密，pad函数用于分组和填充
encrypted_data = cipher.encrypt(pad(data, AES.block_size))
print(encrypted_data)