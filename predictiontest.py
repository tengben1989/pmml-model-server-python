###pip install --user --upgrade git+https://github.com/jpmml/openscoring-python.git
import openscoring
os = openscoring.Openscoring("http://localhost:8080/openscoring")

kwargs = {"auth" : ("admin", "adminadmin")}
os.deploy("Iris", "output_RF.pmml", **kwargs)
os.evaluateCsv("Iris", "simulated_data.csv","results12.csv")