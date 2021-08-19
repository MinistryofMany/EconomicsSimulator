class User():
    def __init__(self, name: str,  deposit: float):
        self.name = name  # ens name
        self.karma = 0
        self.deposited = deposit
        self.tokens = 10
        self.founder = [str]
        print(f"User created: {name}")

    def found_community(self, community_name):
        self.founder.append(community_name)