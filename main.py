from bardapi import BardCookies
from config import cookie_dict


bard = BardCookies(cookie_dict=cookie_dict)

question = input("Ask anything : ")
result = bard.get_answer(question)
final = result["content"]
final1 = final.replace("*", "").replace("`", "").replace("#", "")
print(final1)
