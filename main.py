from api import app

if __name__ == '__main__':
    import uvicorn
    import nltk

    nltk.download('punkt_tab')
    uvicorn.run("main:app", port=10000, host="0.0.0.0", log_level="info")