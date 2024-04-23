import bcrypt

def hashing_password(new_password):
      encoded_password = new_password.encode('utf-8')
      salt = bcrypt.gensalt(4)
      return bcrypt.hashpw(encoded_password, salt)

new_password = input