import random

class solitaire_utf8():
    def __init__(self):
        pass
    
    def init_deck(self, deck):
        self.deck = deck
        
    def init_joker(self, joker1, joker2):
        self.joker1 = joker1
        self.joker2 = joker2
    
    def swap_down(self, deck, card):
        ''' (list of int, int) -> NoneType
        Swap card to one position below.
        This method mutates the deck.
        '''
        card_index = deck.index(card)
        temp = deck[card_index]
        deck[card_index] = deck[(card_index + 1) % len(deck)]
        deck[(card_index + 1) % len(deck)] = temp
    
    def move_jokers(self, deck):
        ''' (list of int) -> NoneType
        Move joker 1 one place down, joker 2 two place down.
        This method mutates the deck
        '''
        self.swap_down(deck, self.joker1)
        self.swap_down(deck, self.joker2)
        self.swap_down(deck, self.joker2)
        
    def triple_cut(self, deck):
        ''' (list of int) -> NoneType
        Do a triple cut.
        This method mutates the deck
        '''
        # Find index for min joker index
        joker1_index = min(deck.index(self.joker1), deck.index(self.joker2))
        # Find index for max joker index
        joker2_index = max(deck.index(self.joker1), deck.index(self.joker2))
        # Find before, middle and end of the list
        before = deck[:joker1_index]
        middle = deck[joker1_index:joker2_index + 1]
        end = deck[joker2_index + 1:]
        # Form new list
        new_deck = end + middle + before
        # Mutate the input list
        for i in range(len(deck)):
            deck[i] = new_deck[i]
    
    def insert_top_to_bottom(self, deck):
        ''' (list of int) -> NoneType
        Get the last card number, grab that amount of card from the beginning, and
        insert them before the last card.
        This method will mutate the list. This function does not return anything
        REQ: Last card must <= len(deck) not fatal
        '''
        # Get last card number max out to be len(deck) - 1
        last_num = min(deck[len(deck) - 1], len(deck) - 1)
        # Find before, middle and end of the list, and form new list
        before = deck[last_num:len(deck) - 1]
        middle = deck[:last_num]
        end = deck[len(deck) - 1:]
        # Form new list
        new_deck = before + middle + end
        # Mutate the input list
        for i in range(len(deck)):
            deck[i] = new_deck[i]
    
    def get_card_at_top_index(self, deck):
        ''' (list of int) -> int
        Get first card number, and return the card at that index.
        '''
        # Get first card number max out to be len(deck) - 1
        first_num = min(deck[0], len(deck) - 1)
        return deck[first_num]
    
    def get_next_value(self, deck):
        ''' (list of int) -> int
        Get the next value of the deck (does not need to be valid).
        This method will mutate the lsit. This function does not return anything
        '''
        self.move_jokers(deck)
        self.triple_cut(deck)
        self.insert_top_to_bottom(deck)
        return self.get_card_at_top_index(deck)
    
    def get_next_keystream_value(self, deck):
        ''' (list of int) -> int
        Get the next valid value of the deck (keystream value)
        This method will mutate the lsit. This function does not return anything
        '''
        val = self.joker1
        while val == self.joker1 or val == self.joker2:
            val = self.get_next_value(deck)
        return val    
        
    def gen_deck(self):
        ''' () -> list of int
        Generate a random deck for encryption
        '''
        result = []
        while len(result) != 52:
            num = random.randint(1,52)
            if not num in result:
                result.append(num)
        return result
    
    def encrypt(self, message):
        message = bytes(message, "utf-8")
        hex_msg = ""
        for b in message:
            hex_msg += hex(b)[2:].upper()
            
        encrypted = ""
        char_map = "0123456789ABCDEF"
        deck_copy = self.deck[:]
        keychain = ""
        for c in hex_msg:
            key = self.get_next_keystream_value(deck_copy)
            encrypted += char_map[(key + char_map.index(c)) % 16]
        return encrypted
    
    def decrypt(self, message):
        decrypted = ""
        char_map = "0123456789ABCDEF"
        deck_copy = self.deck[:]
        keychain = ""
        for c in message:
            key = self.get_next_keystream_value(deck_copy)
            decrypted += char_map[(char_map.index(c) - key) % 16]
            
        hex_list = []
        while decrypted:
            hex_list.append(int(decrypted[:2],16))
            decrypted = decrypted[2:]
        
        hex_list = bytearray(hex_list)
        hex_list = hex_list.decode("utf-8")
        return hex_list

instance = solitaire_utf8()
deck = instance.gen_deck()
instance.init_deck(deck)
instance.init_joker(51,52)
encrypted = instance.encrypt("我就是试一试，好蛋疼啊")
instance.decrypt(encrypted)