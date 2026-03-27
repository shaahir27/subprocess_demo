from flask import Flask, render_template, request
import os, subprocess 

# Subprocess -> It is used to run external files here C exe file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TMPL_DIR = os.path.join(BASE_DIR, "Frontend", "templates")
BACKEND_DIR = os.path.join(BASE_DIR, "Backend")

# Initializing Flask App

app = Flask(__name__,
            template_folder = TMPL_DIR)


# Route for Homepage (Patient form here)

@app.route("/") # when user visits "/"
def patient():
    return render_template("patient.html")

#In the upcoming Route we are gonna Integrate the Backend C (exe file) with Frontend

#Route to handle form Submission (Subprocess Route)
@app.route("/add_patient", methods=["POST"])
def add_patient():

    # It is used to get form data sent from patient.html
    # request.form acts like a dictionary

    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    phone = request.form["phone"]    
    address = request.form["address"]
    symptoms = request.form["symptoms"]
    visit_type = request.form["visit_type"]
    priority = request.form["priority"]

    # C exe file path
    exe_path = os.path.join(BACKEND_DIR, "c_modules", "patient.exe")

    # Combine all data into a single string separated by "|"
    # This is because C program receives input via argv[1]
    data_string = f"{name}|{age}|{gender}|{phone}|{address}|{symptoms}|{visit_type}|{priority}"
    

    # Run the C program using subprocess
    # Pass data_string as argument
    # capture_output=True → captures output from C (printf)
    # text=True → output will be string (not bytes)

    patient_output = subprocess.run(
        [exe_path, data_string],  # You can see that exe file path and data string is passed as an array which will be recieved by the int main function
        capture_output=True,
        text=True
    )

    # In the upcoming steps I will be extracting values using strip() and split() functions 
    
    # patient_output.stdout is what C prints using printf
    patient_output = patient_output.stdout.strip() 
    data = patient_output.split("|")
    id = data[0]
    view_type = data[1]
    priority = data[2]

    # Send data to HTML page (Jinja will display it)
    # patient_id, visit_type, priority -> Jinja Templates
    # Analyse the html code of add_patient.html to know how jinja templates are used

    return render_template("add_patient.html", patient_id=id, visit_type=visit_type, priority=priority)

# Start Flask server
if __name__ == "__main__":
    app.run(debug=True, port=5000)