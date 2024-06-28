
### main function
def main():
    ## sets where to find the file, relative path
    book_path = "books/frankenstein.txt"
    ## calls the get_book_text function, sets the output to a variable
    text = get_book_text(book_path)
    ## prints the outcome of the function
    texts = text.split()
    #print(text)
    numba_o_words(text)
    pre_list = count_characta(text)
    sorted_report(pre_list)


def numba_o_words(text):
    words = text.split()
    return ( len(words))

def count_characta(text):
    character_count_dict= {} 
    for character in text:
        lowered_character = character.lower()
        if lowered_character in character_count_dict:
            character_count_dict[lowered_character] +=1
        else:
            character_count_dict[lowered_character] = 1
    return character_count_dict      

def sorted_report(pre_list):
    sorted_dict = sorted(key for key in pre_list.keys() if key.isalpha())
    for key in sorted_dict:
        print(f"The", "'", key, "'",  "character was found", pre_list[key] , "times")

### function for reading the file
def get_book_text(path):
    ### users the open function and creates a variable
    with open(path) as f:
        ## returns the files contents
        return f.read()


main()