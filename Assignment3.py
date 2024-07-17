#%%
not_pal = "python"
pal = "hannah"
def is_palindrome(word) :
    letters = [x for x in word]
    while len(letters) > 1: 
        if letters[0].lower() != letters[len(letters)-1].lower(): 
            return False
        else:
            letters.pop(0)
            letters.pop(-1)
    return True
is_pal = is_palindrome(pal)
print(is_pal)
no_pal = is_palindrome(not_pal)
print(no_pal)

# %%
words = ["hello", "world", "hello", "python"]
wordCount = {}

def count_words(word_list): 
    word_count = {}
    for word in word_list: 
        if word in word_count:
            word_count[word] += 1
        else: 
            word_count[word] = 1
    return word_count

num_words = count_words(words)
print(num_words)
# %%
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
r = Rectangle(3, 4)
print("Area:", r.area())          
print("Perimeter:", r.perimeter())
# %%
