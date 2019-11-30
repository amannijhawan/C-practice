class Trie(object):
  def __init__(self, char):
    self.children = {}
    self.char = char
    self.is_terminal = False

  def add(self, word):
    if not word:
      self.is_terminal = True
      return

    next_char = word[0]
    if next_char == "":
      self.is_terminal = True
      return

    word_suffix = word[1:]
    if next_char not in self.children:
      self.children[next_char] = Trie(next_char)

    child = self.children[next_char]
    return child.add(word_suffix)

  def remove(self, word):
    pass

  def get_all_words_root(self, prefix='', words=None):
    if not words:
      words = []
    if self.is_terminal:
      words.append(prefix)
    for char, child in self.children.items():
      child.get_all_words_root(prefix=prefix+char, words=words)
    return words


  def find(self, prefix):
    if not prefix:
      return self
    next_char = prefix[0]
    if next_char in self.children:
      child = self.children[next_char]
      return child.find(prefix[1:])
    else:
      return None

  def get_matches(self, prefix):
    node = self.find(prefix)
    if node:
      return node.get_all_words_root(prefix=prefix, words=None)


t = Trie("")
for word in ("f", "fo", "foo", "fb", "fbo", "fboo"):
  t.add(word)
print t.find("f").get_all_words_root(prefix="f")
print t.find("fo").get_all_words_root(prefix="fo")
print t.find("fb").get_all_words_root(prefix="fb")
