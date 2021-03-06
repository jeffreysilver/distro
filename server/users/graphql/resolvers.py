from ariadne import (
    QueryType,
    ObjectType,
    MutationType,
)

from users.models import User, Group


query = QueryType()


@query.field("users")
def resolve_users(*args):
    return User.objects.all()


mutation = MutationType()


@mutation.field("createGroup")
def resolve_create_group(_, info, input):
    group = Group.objects.create(name=input["name"])
    return {"group": group, "error": None}


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


resolvers = [query, mutation, user, group]
