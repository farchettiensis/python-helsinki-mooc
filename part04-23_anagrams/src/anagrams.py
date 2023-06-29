# Write your solution here
def anagrams(word1: str, word2: str):
  word1 = word1.lower()
  word2 = word2.lower()
  return sorted(word1) == sorted(word2)

if __name__ == "__main__":
  print(anagrams("python", "typhoon"))
  print(anagrams("tame", "mate"))