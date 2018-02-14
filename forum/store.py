class MemberStore :
    members = []

    def add(self, member) :
        self.members.append(member)
    
    def get_all(self) :
        for m in self.members :
            return m.name
    
    def entity_exist(self, member) :
        if member in self.members :
            return True
        return False
    
class PostStore:
    posts = []

    def add(self, post):
        self.posts.append(post)

    def get_all(self):
        for p in self.posts :
            return p.title 

    def entity_exist(self, post) :
        if post in self.posts :
            return True
        return False