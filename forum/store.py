class MemberStore :
    members = []
    last_id = 1
  	
    def add(self, member):
  		member.id = MemberStore.last_id	
  		MemberStore.members.append(member)
  		MemberStore.last_id += 1    
    
    def get_all(self) :
        return MemberStore.members
    
    def entity_exist(self, member) :
        result = False
        if self.get_by_id(member.id) != None :
            result=  True
        return result
    
    def get_by_id(self, id):
        result = None
        all_members = self.get_all()
        for m in all_members:
            if m.id == id:
                result =  m
            return result

    def delete(self, id):
        member = self.get_by_id(id)
        MemberStore.members.remove(member)

    def get_by_name (self, name):
        result = []
        all_members = self.get_all()
        for m in all_members :
            if m.name == name :
                result.append(m)
            break
        return result

    def update(self, member):
        result = member
        
        all_members = self.get_all()

        for index, current_member in enumerate(all_members):
            if current_member.id == member.id:
                all_members[index] = member

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