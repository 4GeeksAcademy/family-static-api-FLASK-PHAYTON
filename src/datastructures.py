from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {"id": self._generateId(), "first_name": "John", "last_name": last_name, "age": 33, "lucky_numbers": [7, 13, 22]},
            {"id": self._generateId(), "first_name": "Jane", "last_name": last_name, "age": 35, "lucky_numbers": [10, 14, 3]},
            {"id": self._generateId(), "first_name": "Jimmy", "last_name": last_name, "age": 5, "lucky_numbers": [1]}
        ]

    def _generateId(self):
        return randint(0, 99999999)
    
    def add_member(self, member):
        if not member.get("id"):
            member["id"] = self._generateId()
        self._members.append(member)
        print("Añadir miembro", member)

    def delete_member(self, id): 
        initial_length = len(self._members)
        self._members = [m for m in self._members if m['id'] != id]
        return len(self._members) < initial_length

    def update_member(self, id, member):
        for i, family_member in enumerate(self._members):
            if family_member["id"] == id:
                member["id"] = id
                self._members[i] = member
                return True
        return False
    
    def get_member(self, id):
        for family_member in self._members:
            if family_member["id"] == id:
                return family_member
        return None
    
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
