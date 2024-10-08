# path=(r"C:\Users\nikhi\codeforces\lister.txt")
# newfile=(r"C:\Users\nikhi\codeforces\problems.txt")
# f=open(path,"r",encoding="utf8")
# g=open(newfile,"w",encoding="utf8")
# lines=f.readlines()
# for l in lines:
#     s=l.split('-')
#     probname=(s[1])
#     probname=probname[1::]
#     print(probname)
#     g.write(probname)
# f.close()
# g.close()

# path=(r"C:\Users\nikhi\codeforces\submitted.txt")
# newfile=(r"C:\Users\nikhi\codeforces\subfin.txt")
# f=open(path,"r",encoding="utf-8")
# g=open(newfile,"w",encoding='utf-8')
# lines=f.readlines()
# for l in lines:
#     s=l.split('-')
#     str=s[1]
#     st=str.split('Java')
#     fin=st[0].strip()
#     g.write(fin+"\n")

import webbrowser
import requests

response = requests.get(f"https://codeforces.com/api/user.status?handle=oreothicc&from=1")

    # Check for errors in response
if response.status_code == 400:
    print("No such handle exists :(")

newprobspath=(r"C:\Users\nikhi\codeforces\problemsnew.txt")
f=open(newprobspath,"w",encoding="utf-8")
stat = response.json()['result']
for submission in stat:
            if submission['verdict'] == 'OK':
                problem_name = submission['problem']['name']
                f.write(problem_name + "\n")
    
#now i have all the submissions succesfully stored in problemsnew

#now to read all the problems to do
probspath=(r"C:\Users\nikhi\codeforces\problems.txt")

#and my submissions
subspath=(r"C:\Users\nikhi\codeforces\problemsnew.txt")

#file to store questions to do
todopath=(r"C:\Users\nikhi\codeforces\todo.txt")


todo=open(todopath,"w",encoding='utf-8')
f=open(probspath,"r",encoding="utf-8")
g=open(subspath,"r",encoding="utf-8")

problems=f.readlines()
submissions=g.readlines()
for p in problems:
    if p in submissions:
        continue
    else:
        todo.write(p+"\n")

print("All done! You'll have a file called to-do list in your directory :) ")

#teehee
url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
webbrowser.open(url)

