# def rev_each_word_sentence(sentence):
#   words=sentence.split()
#   for i in words:
#     print(i[::-1],end=" ")



def rev_each_word_sentence(sentence):
  stack=[]
  output=""
  for i in sentence:
    if i !=" ":
      stack.append(i)
    else:
      while stack:
        output+=stack.pop()
      output+=" "
      
  while stack:
    output+=stack.pop()
  return output
  
sentence="hi me"
x=rev_each_word_sentence(sentence)
print(x)