import re
text = """The Passage: Created by Liz Heldens. With Mark-Paul Gosselaar, Saniyya Sidney, Jamie McShane, Caroline Chikezie. When a botched U.S. government experiment turns a group of death row inmates into highly infectious vampires, an orphan girl might be the only person able to stop the ensuing"""
s = re.compile("[A-Z]+", re.I)
print(s.search(text).group())
x = s.findall(text)
print(x)