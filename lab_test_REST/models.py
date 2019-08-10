from django.contrib.auth.models import User, Group


# class UserMethods(User):
#     class Meta:
#         proxy = True
#     def get_role(self):
#         groups = self.groups.first()
#         return Group.objects.get(id=self.id)
