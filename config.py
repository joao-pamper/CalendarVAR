import os

class Config:
    """Base configuration."""
    DEBUG = False
    TESTING = False
    API_URL = "https://api-futebol.com.br/v1/matches/team/"
    GOOGLE_CALENDAR_API_URL = "https://www.googleapis.com/calendar/v3"
    
    # Fetch sensitive data from environment variables
    API_KEY = os.getenv("API_KEY")
    GOOGLE_CALENDAR_CREDENTIALS = os.getenv("GOOGLE_CALENDAR_CREDENTIALS")

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    # You could have other development-specific settings

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DEBUG = True
    # You could have mock API URLs or other test-specific settings

class ProductionConfig(Config):
    """Production configuration."""
    # Production-specific settings
    pass
