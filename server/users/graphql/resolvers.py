from ariadne import QueryType, gql, make_executable_schema, load_schema_from_path, ObjectType
from ariadne.asgi import GraphQL

from users.models import User, Group


query = QueryType()

@query.field("users")
def resolve_users(*args):
    return User.objects.all()


user = ObjectType("User")
    
@user.field("groups")
def resolve_groups_for_user(user, *args):
    return user.groups.all()


group = ObjectType("Group")

@query.field("groups")
def resolve_groups(*args):
    return Group.objects.all()


@group.field("users")
def resolve_users_for_group(group, *args):
    return group.user_set.all()

resolvers = [query, user, group]