from typing import Dict
from community import Community
from user import User


class deForum():
    def __init__(self):
        self.communities = {}
        self.users = {}
        self.community_fund_amount = 10
        self.pending_communities = {}

    def found_community(self, community_name: str):
        print("Founding community: " + community_name)
        c = Community(community_name)
        self.communities[community_name] = c

    def register_user(self, username: str, deposit: float = 10):
        u = User(username, deposit)
        self.users[username] = u

    def fund_community_founding(self, community_name, username, amount):
        if username not in self.users.keys():
            print(f"User {username} does not exist")
            return "User does not exist"
        print(f"Funding Community: {community_name}")
        self.pending_communities[community_name]['total'] += amount
        self.pending_communities[community_name]['users'][username] += amount
        if self.pending_communities[community_name]['total'] >= self.community_fund_amount:
            self.found_community(community_name)
            for u in self.pending_communities[community_name]['users'].keys:
                _user = self.users[u]
                _user.found_community(community_name)
                print(f"{username} is helping found {community_name}")

    @staticmethod
    def mint_tokens_for_post(_post_karma: float):
        e = 1.05
        karma_divider = 5
        center = 0.5
        multiplier = 20
        if _post_karma <= 0:
            print(f"No tokens minted")
            return 0
        else:
            tokens = (1 / (1 + e**(-_post_karma / karma_divider)) - center) * multiplier
            print(f"Tokens minted: {tokens}")
            return tokens

    @staticmethod
    def post_fee_rexlu(_karma: float):
        base_fee = 0.01
        neg_karma_multiplier = 2
        karma_divider = 50
        if _karma < 0:
            fee = (- neg_karma_multiplier * _karma) + base_fee
        elif _karma == 0:
            fee = 0.5 + base_fee
        else:
            fee = (1 / (1 + 2.71828 ** (_karma / karma_divider))) + base_fee
        print(f"Post fee: {fee}")
        return fee

    def comment_fee(self, _karma: float):
        fee = self.post_fee_rexlu(_karma) / 10
        print(f"Comment fee: {fee}")
        return fee

    def make_post(self, community_name, username, title, description):
        u = self.users[username]
        fee = self.post_fee_rexlu(u.karma)
        if u.tokens < fee:
            return "User doesn't have enough tokens"
        u.tokens = u.tokens - fee
        c = self.communities[community_name]
        c.create_post(title, description, username)
