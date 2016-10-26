import random, hashlib

class SolitaireByteEncryptor():
    def __init__(self):
        pass
    
    def set_deck(self, deck):
        ''' (SolitaireDeck) -> NoneType
        Set deck for encryption and decryption
        '''
        self.deck = deck
        
    def get_next_value(self, deck):
        ''' (list of int) -> int
        Get the next value of the deck (does not need to be valid).
        This method will mutate the lsit. This function does not return anything
        '''
        deck.move_jokers()
        deck.triple_cut()
        deck.insert_top_to_bottom()
        return deck.get_card_at_top_index()
    
    def get_next_keystream_value(self, deck):
        ''' (list of int) -> int
        Get the next valid value of the deck (keystream value)
        This method will mutate the lsit. This function does not return anything
        '''
        val = deck.joker1
        while val == deck.joker1 or val == deck.joker2:
            val = self.get_next_value(self.deck)
        return val
    
    def encrypt(self, byte):
        hex_msg = hex(byte)[2:].upper()
        encrypted = ""
        char_map = "0123456789ABCDEF"
        for c in hex_msg:
            key = self.get_next_keystream_value(self.deck)
            encrypted += char_map[(key + char_map.index(c)) % 16]
        return encrypted
    
    def decrypt(self, byte):
        decrypted = ""
        char_map = "0123456789ABCDEF"
        for c in byte:
            key = self.get_next_keystream_value(self.deck)
            decrypted += char_map[(char_map.index(c) - key) % 16]
        decrypted = int(decrypted, 16)
        return decrypted        


class SolitaireDeck():
    def __init__(self, deck, joker1, joker2):
        ''' (list of int or string) -> SolitaireDeck
        Initialize the deck, enter a list of int or a string (password) to
        genterate a 52 card deck.
        '''
        if type(deck) is str:
            self.deck = self.gen_deck_with_password(deck)
        else:
            self.deck = deck
        self.deck_copy = self.deck[:]
        self.joker1 = joker1
        self.joker2 = joker2
        
    def gen_deck_with_password(self, password):
        ''' (str) -> list of int
        Generate a deck of card based on a string's (password) SHA result
        '''
        pwd_hash = hashlib.sha1(bytes(password, "utf-8")).hexdigest()
        random.seed(pwd_hash)
        result = []
        while len(result) != 52:
            num = random.randint(1,52)
            if not num in result:
                result.append(num)
        return result
    
    def swap_down(self, card):
        ''' (list of int, int) -> NoneType
        Swap card to one position below.
        This method mutates the deck.
        '''
        card_index = self.deck.index(card)
        temp = self.deck[card_index]
        self.deck[card_index] = self.deck[(card_index + 1) % len(self.deck)]
        self.deck[(card_index + 1) % len(self.deck)] = temp
    
    def move_jokers(self):
        ''' (list of int) -> NoneType
        Move joker 1 one place down, joker 2 two place down.
        This method mutates the deck
        '''
        self.swap_down(self.joker1)
        self.swap_down(self.joker2)
        self.swap_down(self.joker2)
            
    def triple_cut(self):
        ''' (list of int) -> NoneType
        Do a triple cut.
        This method mutates the deck
        '''
        # Find index for min joker index
        joker1_index = min(self.deck.index(self.joker1), 
                           self.deck.index(self.joker2))
        # Find index for max joker index
        joker2_index = max(self.deck.index(self.joker1),
                           self.deck.index(self.joker2))
        # Find before, middle and end of the list
        before = self.deck[:joker1_index]
        middle = self.deck[joker1_index:joker2_index + 1]
        end = self.deck[joker2_index + 1:]
        # Form new list
        new_deck = end + middle + before
        # Mutate the input list
        for i in range(len(self.deck)):
            self.deck[i] = new_deck[i]

    def insert_top_to_bottom(self):
        ''' (list of int) -> NoneType
        Get the last card number, grab that amount of card from the
        beginning, and insert them before the last card.
        This method will mutate the list. This function does not return
        anything
        REQ: Last card must <= len(deck) not fatal
        '''
        # Get last card number max out to be len(deck) - 1
        last_num = min(self.deck[len(self.deck) - 1], len(self.deck) - 1)
        # Find before, middle and end of the list, and form new list
        before = self.deck[last_num:len(self.deck) - 1]
        middle = self.deck[:last_num]
        end = self.deck[len(self.deck) - 1:]
        # Form new list
        new_deck = before + middle + end
        # Mutate the input list
        for i in range(len(self.deck)):
            self.deck[i] = new_deck[i]
    
    def get_card_at_top_index(self):
        ''' (list of int) -> int
        Get first card number, and return the card at that index.
        '''
        # Get first card number max out to be len(deck) - 1
        first_num = min(self.deck[0], len(self.deck) - 1)
        return self.deck[first_num]
    
    def reset(self):
        ''' () -> NoneType
        Reset the deck
        '''
        self.deck = self.deck_copy[:]


class SolitaireUTF8():
    def __init__(self):
        self.byte_encryptor = SolitaireByteEncryptor()
    
    def set_deck(self, deck):
        ''' (SolitaireDeck) -> NoneType
        Set deck for encryption and decryption
        '''
        self.deck = deck
        self.byte_encryptor.set_deck(deck)
    
    def encrypt(self, message):
        message = bytes(message, "utf-8")
        encrypted = ""
        for b in message:
            encrypted += self.byte_encryptor.encrypt(b)
        return encrypted
    
    def decrypt(self, message):
        byte_list = []
        while message:
            byte_list.append(message[:2])
            message = message[2:]
        decrypted = []
        for b in byte_list:
            decrypted.append(self.byte_encryptor.decrypt(b))
        decrypted = bytearray(decrypted)
        decrypted = decrypted.decode("utf-8")
        return decrypted

# Generate a deck based on password, set jokers to be 51 and 52
deck = SolitaireDeck("this is a really good password", 51, 52)

# Initialize encryptor
encryptor = SolitaireUTF8()
encryptor.set_deck(deck)

encrypted = encryptor.encrypt("myname")

deck.reset()

decrypted = encryptor.decrypt(encrypted)