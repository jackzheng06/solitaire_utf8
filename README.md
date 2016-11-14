# Solitaire UTF-8
Solitaire Encryption that works for UTF-8 (really works for anything)

**Copyleft Jun Zheng, feel free to fork, distribute and modify!**

## Examples
### UTF-8 String Encryption and Decryption
```python
# Generate a deck based on password, set jokers to be 51 and 52
deck = SolitaireDeck("this is a really good password", 51, 52)

# Initialize utf 8 encryptor
encryptor = SolitaireUTF8()
encryptor.set_deck(deck)

encrypted = encryptor.encrypt("Solitaire is really cool!!!! 接龙是真的很酷, ソリティアは本当にクールです סוליטר הוא ממש מגניב")
# Result - 949C3B4A84886B263D7CE73C92627F5F755D2886C615600E293788E90CAA29769D2D79C3AB53D716117FF3939A97297A4D06CDF6848237967FA9CF306C35788B49081DC390EF87C2C3A235B2F53976D0424E6A9ECF855555ED3CBC46C42D138D2B8826CB6B3CB843B168503E6240537993CE22229A58FC81F53C310989BDFAC3A1E23D50

# Remember to reset the deck before decryption!
deck.reset()

decrypted = encryptor.decrypt(encrypted)
# Result - Solitaire is really cool!!!! 接龙是真的很酷, ソリティアは本当にクールです סוליטר הוא ממש מגניב
```

### Byte Encryption and Decryption
```python
# Generate a deck based on password, set jokers to be 51 and 52
deck = SolitaireDeck("this is a really good password", 51, 52)

# Initialize byte encryptor
encryptor = SolitaireByteEncryptor()
encryptor.set_deck(deck)

encrypted = encryptor.encrypt(255)
# Result - '30'

# Remember to reset the deck before decryption!
deck.reset()

decrypted = encryptor.decrypt(encrypted)
# Result - 255
```

## SolitaireUTF8 class
Encrypts or decrypts a UTF-8 string.
```python
encryptor = SolitaireUTF8()
encryptor.set_deck(deck)
```

## SolitaireByteEncryptor class
Encrypts or decrypts one byte (00000000 to 11111111)
```python
byte_encryptor = SolitaireByteEncryptor()
byte_encryptor.set_deck(deck)
```
## SolitaireDeck class
The solitaire deck used for encryption and decryption
```python
deck = SolitaireDeck("password",51,52)
```
