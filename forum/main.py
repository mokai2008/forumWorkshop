from models import Member , Post
from store import MemberStore , PostStore

member1 = Member("Hany" , 40)
member2 = Member("Tawfik" , 32)

post1 = Post("Python" , "13/02/2018" , member1.name , "I love Python")
post2 = Post("Web development" , "14/02/2018" , member2.name , "I'd like to be a full stack web developer")

print (member1.name, member1.age)
print (post2.title, post2.published_date, "written by " +post2.author_name, post2.content)

member_store = MemberStore()

member_store.add(member1)
member_store.add(member2)

print (member_store.get_all())
print (member_store.entity_exist(member1))
print (member_store.entity_exist(member2))

post_store = PostStore()

post_store.add(post1)
post_store.add(post2)

print (post_store.get_all())
print (post_store.entity_exist(post1))
print (post_store.entity_exist(post2))