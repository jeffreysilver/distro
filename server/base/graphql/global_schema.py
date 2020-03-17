from ariadne import QueryType, make_executable_schema, load_schema_from_path

from users.graphql.resolvers import resolvers as users_resolvers
from posts.graphql.resolvers import resolvers as posts_resolvers

type_defs = load_schema_from_path("/")

query = QueryType()

resolvers = [query]

resolvers += users_resolvers
resolvers += posts_resolvers

schema = make_executable_schema(type_defs, resolvers)
