
class Config:
    #FORMAT: "postgres://username:password@server_address:server_port/database"
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:password@localhost:5432/python_blog_2"
    # It has to be called SQLALCHEMY_DATABASE_URI

    SECRET_KEY = "chocolate"
