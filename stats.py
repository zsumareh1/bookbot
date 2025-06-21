def get_num_words(f):
     
     with open(f) as fileString:
          
          splits = fileString.read()
          return len(splits.split())
     
alpha = {
     "a": 0,"b": 0, "c":0,"d": 0, "e": 0,"f": 0,"g": 0,"h": 0,"i": 0,"j": 0,"k": 0,"l": 0,"m": 0,
     "n": 0,"o": 0,"p": 0,"q": 0,"r": 0,"s": 0,"t": 0,"u": 0,"v": 0,"w": 0,"x": 0,"y": 0,"z": 0, 
}


def count_charachter(book):

     output = {}

     with open(book) as text:
          string = text.read()

          for char in string:
               lwr = char.lower()
               if lwr in alpha:
                    alpha[lwr] += 1
                    

     for char, count in sorted(alpha.items()):
          if count > 0:
               output[char] = count
          
     return output


def report(results):
     lijst = []
     
     for char, chabi in results.items():
          lijst.append({"char": char, "num":chabi})
          
     lijst.sort(reverse=True, key=sorteren)   
     return lijst

def sorteren(report):
     return report["num"]

