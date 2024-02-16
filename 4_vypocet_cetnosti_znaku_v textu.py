class CharCounter:
    def __init__(self):
        # Initialize the dictionary for storing character frequencies
        self.char_freq = {}

    def count_chars(self, text):
        # Browsing the text and counting the frequency of individual characters
        for char in text:
            # Ignoring characters outside the specification (A-Ž, a-ž, 0-9, ,.?!;)
            if self.valid_char(char):
                if char in self.char_freq:
                    self.char_freq[char] += 1
                else:
                    self.char_freq[char] = 1
                    
    def valid_char(self, char):
        valid_chars = set("AÁBCČDĎEĚÉFGHIÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽaábcčdďeěéfghiíjklmnňoópqrřsštťuůúvwxyýzž0123456789,.?!;")
        return char in valid_chars

    def sort_chars_freq(self): 
        # Sorting the dictionary by frequency values (descending)
        sorted_char_freq = self.sort_chars(list(self.char_freq.items()))
        return sorted_char_freq

    def sort_chars(self, char_freq_pairs):
        # Custom sorting function (bubble sort)
        n = len(char_freq_pairs)
        for i in range(n):
            for j in range(0, n-i-1):
                if char_freq_pairs[j][1] < char_freq_pairs[j+1][1]:
                    char_freq_pairs[j], char_freq_pairs[j+1] = char_freq_pairs[j+1], char_freq_pairs[j]
        return char_freq_pairs

    def calculate_total_chars(self):
        # Calculation of the total length of the text
        return sum(self.char_freq.values())

    def print_chars_freq(self, total_chars):
        # List of absolute and relative frequencies of characters
        for char, freq in self.sort_chars_freq():
            relative_freq = freq / total_chars
            print(f"Character: {char}, Absolute Frequency: {freq}, Relative Frequency: {relative_freq:.1%}")

text = input('Type or copy your text: ')

# Creating an instance of CharCounter
counter = CharCounter()

# Running the function to calculate character frequencies
counter.count_chars(text)

# Calculation of the total length of the text
total_chars = counter.calculate_total_chars()

# Printing character frequencies
counter.print_chars_freq(total_chars)