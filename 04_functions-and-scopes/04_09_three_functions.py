# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

def karma_yoga(restless_mind):
    print("First: a restless mind full of desires, is calmed by selfless actions")
    calm_mind = restless_mind
    aware_actions = raja_yoga(calm_mind)
    return aware_actions

def raja_yoga(calm_mind): 
    print("Secondly: The calmed mind aquires concentration and focus through mediation")
    focused_mind = calm_mind
    qualified_mind = jnana_yoga(focused_mind)
    return qualified_mind

def jnana_yoga(focused_mind):
    print("Thridly: The Calm and focused mind gain the knowlegde of the True Self")
    dissolved_mind = focused_mind
    True_self = dissolved_mind
    return True_self


print(karma_yoga("me"))