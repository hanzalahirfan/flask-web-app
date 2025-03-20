from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        try:
            marks1 = int(request.form["marks1"])
            marks2 = int(request.form["marks2"])
            is_pm_son = request.form.get("pm_son")  # Checkbox (None if unchecked)

            # Apply the passing logic
            if (marks1 >= 40 and marks2 >= 40) or is_pm_son:
                result = "🎉 Congratulations! You passed both subjects."
            else:
                result = "❌ You failed in at least one subject."
        except ValueError:
            result = "⚠️ Please enter valid numeric marks."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
