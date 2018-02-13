from models import member , post

member1 = member("Hany" , 40)
member2 = member("Tawfik" , 32)

post1 = post("Python" , "13/02/2018" , member1.name , "I love Python")
post2 = post("Web development" , "14/02/2018" , member2.name , "I'd like to be a full stack web developer")

print (member1.name, member1.age)
print (post2.title, post2.published_date, "written by " +post2.author_name, post2.content)