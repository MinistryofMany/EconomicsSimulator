from deforum import deForum

d = deForum()
Users = ["GeorgeBush", "EdwardScissorhands", "Einstein", "ElonMusk", "MarkZuckerberg", "BillGates", "SteveJobs", "SteveWozniak", "MarkTwain"]

for user in Users:
    d.register_user(user, 10)
