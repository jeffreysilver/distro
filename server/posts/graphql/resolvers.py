from ariadne import QueryType, gql, make_executable_schema, load_schema_from_path, ObjectType, MutationType
from ariadne.asgi import GraphQL

from posts.models import Post
from users.models import User, Group

group = ObjectType("Group")

@group.field("posts")
def resolve_posts_for_group(group, *args):
    return Post.objects.filter(group=group)


mutation = MutationType()

@mutation.field("createPost")
def resolve_create_post(_, info, input):
    # todo: get the user from the request?
    user = User.objects.first()

    group_id = input["groupId"]
    if group_id not in user.groups.values_list("id", flat=True):
        return {
            "post": None,
            "error": {
                "code": "user_not_in_group",
                "description": "Posting user is not in the selected group"
            }
        }

    return {
        "post": Post.objects.create(user=user, group_id=group_id, link=input["link"]),
        "error": None
    }
   


resolvers = [mutation, group]