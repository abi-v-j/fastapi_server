from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mongo_url: str = "mongodb+srv://aj123:aj123@shoppify.fsyemvp.mongodb.net/my_database"


    class Config:
        env_file = ".env"

settings = Settings()
