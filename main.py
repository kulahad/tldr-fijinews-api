from api import app

if __name__ == '__main__':
    import uvicorn
    import nltk

    nltk.download('punkt_tab')
    uvicorn.run(app)