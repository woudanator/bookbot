def main():
  path_to_book = "./books/frankenstein.txt"
  text = get_book_text(path_to_book)
  count = book_word_count(text)
  lt_count =get_chars_dict(text)
  report_of_text(lt_count,count)


def get_book_text(path_to_book):
  with open(path_to_book) as f:
    return f.read()
  
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
   return dict['count']

def report_of_text(lt_dict, word_count):
   letter_dict_list = []
   for lt in lt_dict:
      new_dict = {'char':lt, 'count':lt_dict[lt]}
      letter_dict_list.append(new_dict)
   letter_dict_list.sort(reverse=True, key=sort_on)
   print("--- Begin report of books/frankenstein.txt ---")
   print(f"{word_count} words found in the document\n\n")
   for dict in letter_dict_list:
      if dict['char'].isalpha():
        print(f"The {dict['char']} character was found {dict['count']} times")
   print()
   print("--- End report ---")
   
  
def book_word_count(book_text):
  split_words= book_text.split()
  return len(split_words)


main()