def translate(phrase):
  translations = ""
  for letter in phrase:
    if letter in "AEIOUaeiou":
      translations = translations + "g"
    else:
      translations = translations + letter
  return translations

print(translate(input("Enter a phrase: ")))