import facebook
token='EAACEdEose0cBAKKzPCmD9PMzZCFL35DfZCBEjZCNKZA33PeEMYspzFnlO7dMM7Awh29SpTHcSoDPXksJct1NmpZB0ZCFTCWcewsR0wQwHLPPQ04x0NMWpZCCAwcNPJuEX2hVw2XyRIMttyWfTvHwEDLNmBkvu9eS0IFTx8izdbkAu0uc6xmn5NPrSS2LMdASovbLR5xuvZACR9W4YdySyXYZBll750CIJ1NwZD'
graph=facebook.GraphAPI(token)
profile=graph.get_object("me")
friends=graph.get_connections("me","friends")
print(friends)
