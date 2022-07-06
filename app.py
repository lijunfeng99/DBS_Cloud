#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask , render_template , request
import joblib


# In[2]:


app = Flask(__name__)
@app.route("/", methods = ["GET" , "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        model = joblib.load("regression.jl")
        r = model.predict([[rates]])
        return(render_template("index.html", result = r))
    else:        
        return(render_template("index.html", result = "Waiting"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:




