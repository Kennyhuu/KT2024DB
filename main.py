import uvicorn
from interface.rest_api import app

def main():
    uvicorn.run(app, host="127.0.0.1", port=8000)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
