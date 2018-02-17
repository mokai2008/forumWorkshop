class MemberStore :
    members = []
    last_id = 1
  	
    def add(self, member):
  		member.id = MemberStore.last_id	
  		MemberStore.members.append(member)
  		MemberStore.last_id += 1    
    
    def get_all(self) :
        return self.members
    
    def entity_exist(self, member) :
        if member in self.members :
            return True
        return False
    
    def get_by_id(self, id):
        all_members = self.get_all()
        for m in all_members:
            if m.id == id:
                return m
            return None

    def delete(self, id):
        member = self.get_by_id(id)
        MemberStore.members.remove(member)

class PostStore:
    posts = []

    def add(self, post):
        self.posts.append(post)

    def get_all(self):
        return self.posts

    def entity_exist(self, post) :
        if post in self.posts :
            return True
        return False